from __future__ import annotations

from typing import Any, Dict, List

import httpx
import respx

from teleleo import AsyncTeleleo, Teleleo
from teleleo.types import Contact

BASE_URL = "https://api.example.test/react_api"


def _contacts_handler(total: int, default_limit: int = 1000) -> Any:
    def handler(request: httpx.Request) -> httpx.Response:
        params = request.url.params
        limit = int(params.get("limit", default_limit))
        page = int(params.get("page", 0))
        start = page * limit
        items: List[Dict[str, Any]] = [
            {"contact_id": i, "name": f"c{i}"} for i in range(start, min(start + limit, total))
        ]
        return httpx.Response(200, json={"data": {"contacts": items, "total_count": total}})

    return handler


@respx.mock
def test_auto_paging() -> None:
    route = respx.get(f"{BASE_URL}/contact").mock(side_effect=_contacts_handler(total=7))
    client = Teleleo(api_key="k", base_url=BASE_URL)
    page = client.contacts.list(limit=3, name="c")
    assert page.total_count == 7 and len(page.items) == 3
    assert all(isinstance(c, Contact) for c in page.items)
    assert [c.contact_id for c in page] == list(range(7))
    assert route.call_count == 3  # iteration reuses the first page, then requests pages 1 and 2
    last = route.calls.last.request.url.params
    assert last["page"] == "2" and last["limit"] == "3" and last["name"] == "c"


@respx.mock
def test_manual_paging() -> None:
    respx.get(f"{BASE_URL}/contact").mock(side_effect=_contacts_handler(total=5))
    client = Teleleo(api_key="k", base_url=BASE_URL)
    page = client.contacts.list(limit=2)
    pages = 1
    while page.has_next_page():
        page = page.get_next_page()
        pages += 1
    assert pages == 3
    assert [c.contact_id for c in page.items] == [4]


@respx.mock
def test_whole_list_without_page_and_limit() -> None:
    route = respx.get(f"{BASE_URL}/contact").mock(side_effect=_contacts_handler(total=4))
    client = Teleleo(api_key="k", base_url=BASE_URL)
    page = client.contacts.list()
    assert not page.has_next_page()
    assert len(list(page)) == 4
    assert route.call_count == 1


@respx.mock
def test_mailings_default_first_50() -> None:
    route = respx.get(f"{BASE_URL}/mailing").mock(
        side_effect=lambda request: httpx.Response(
            200,
            json={
                "data": {
                    "mailings": [{"mailing_id": i} for i in range(50 if "page" not in request.url.params else 10)],
                    "total_count": 60,
                }
            },
        )
    )
    client = Teleleo(api_key="k", base_url=BASE_URL)
    assert len(list(client.mailings.list())) == 60
    assert route.calls.last.request.url.params["page"] == "1"
    assert route.calls.last.request.url.params["limit"] == "50"


@respx.mock
async def test_async_auto_paging() -> None:
    respx.get(f"{BASE_URL}/contact").mock(side_effect=_contacts_handler(total=5))
    async with AsyncTeleleo(api_key="k", base_url=BASE_URL) as client:
        page = await client.contacts.list(limit=2)
        ids = [c.contact_id async for c in page]
    assert ids == [0, 1, 2, 3, 4]
