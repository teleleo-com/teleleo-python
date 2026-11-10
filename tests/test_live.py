"""Read-only checks against the real API.

Skipped unless TELELEO_LIVE_TESTS=1 and TELELEO_API_KEY are set. Nothing here sends, creates, changes or deletes.
"""

from __future__ import annotations

import os

import pytest

import teleleo
from teleleo import Teleleo

pytestmark = pytest.mark.skipif(
    os.environ.get("TELELEO_LIVE_TESTS") != "1" or not os.environ.get("TELELEO_API_KEY"),
    reason="set TELELEO_LIVE_TESTS=1 and TELELEO_API_KEY to run against the real API",
)


@pytest.fixture(scope="module")
def client() -> Teleleo:
    return Teleleo(max_retries=1)


def test_lists(client: Teleleo) -> None:
    dongles = client.dongles.list(is_short=True, limit=5)
    assert isinstance(dongles, teleleo.SyncPage)
    for page in (
        client.sms.list(limit=5),
        client.calls.list(limit=5),
        client.contacts.list(limit=5),
        client.contact_groups.list(limit=5),
        client.mailings.list(limit=5),
        client.redirections.list(limit=5),
        client.call_scenarios.list(limit=5),
        client.follow_up_sms_settings.list(limit=5),
        client.socks_proxies.list(limit=5),
        client.sms.list_threads(limit=5),
    ):
        assert isinstance(page, teleleo.SyncPage)
        assert page.total_count is None or page.total_count >= len(page.items)
    assert isinstance(client.public_vpn.list_sessions(), list)
    assert isinstance(client.sip_users.list(), list)


def test_dongle_details(client: Teleleo) -> None:
    page = client.dongles.list(limit=1)
    if not page.items:
        pytest.skip("the account has no modems")
    dongle_id = page.items[0].dongle_id
    dongle = client.dongles.get(dongle_id)
    assert dongle.dongle_id == dongle_id
    assert isinstance(client.ussd.list(dongle_id, limit=5), teleleo.SyncPage)
    assert isinstance(client.sms.list_for_dongle(dongle_id, limit=5), teleleo.SyncPage)
    assert isinstance(client.dongles.list_statistics(dongle_id), list)


def test_pagination_matches_total(client: Teleleo) -> None:
    first = client.sms.list(limit=2)
    if first.total_count is None or first.total_count < 3:
        pytest.skip("not enough SMS to page through")
    second = first.get_next_page()
    assert {s.sms_id for s in first.items}.isdisjoint({s.sms_id for s in second.items})


def test_errors(client: Teleleo) -> None:
    with pytest.raises(teleleo.NotFoundError):
        client.contacts.get(2_000_000_000)
    with pytest.raises(teleleo.AuthenticationError):
        client.with_options(api_key="invalid-key", max_retries=0).dongles.list(limit=1)
