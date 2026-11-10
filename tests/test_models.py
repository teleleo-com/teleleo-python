from __future__ import annotations

import datetime as dt

import pytest

from teleleo._models import parse_datetime
from teleleo.types import DongleListItem, DongleOnlineErrorCode, Mailing, Sms, SmsStatus, SmsType

UTC = dt.timezone.utc


@pytest.mark.parametrize(
    "value, expected",
    [
        ("2026-11-09 12:42:00", dt.datetime(2026, 11, 9, 12, 42, tzinfo=UTC)),
        ("2026-11-09 12:42:00.5", dt.datetime(2026, 11, 9, 12, 42, 0, 500000, tzinfo=UTC)),
        ("2026-11-09 12:42:00.123456", dt.datetime(2026, 11, 9, 12, 42, 0, 123456, tzinfo=UTC)),
        ("2026-11-09T12:42:00Z", dt.datetime(2026, 11, 9, 12, 42, tzinfo=UTC)),
        ("2026-11-09T15:42:00+03:00", dt.datetime(2026, 11, 9, 12, 42, tzinfo=UTC)),
        ("2026-11-09", None),
        ("not a date", None),
        ("2026-13-40 00:00:00", None),
    ],
)
def test_parse_datetime(value: str, expected: object) -> None:
    assert parse_datetime(value) == expected


def test_answer_with_unexpected_values_does_not_raise() -> None:
    sms = Sms.construct_from(
        {
            "sms_id": 10,
            "sms_type_id": 2,
            "sms_status_id": 42,  # a value the library does not know yet
            "sms_source_type_id": None,
            "created_at": "2026-11-09 12:42:00",
            "scheduled_at": "garbage",
            "api_response_data": {"x": 1},  # a field the library does not know
        }
    )
    assert sms.sms_type_id is SmsType.INCOMING
    assert sms.sms_status_id == 42 and not isinstance(sms.sms_status_id, SmsStatus)
    assert sms.sms_source_type_id is None
    assert sms.created_at == dt.datetime(2026, 11, 9, 12, 42, tzinfo=UTC)
    assert sms.scheduled_at == "garbage"
    assert sms.api_response_data == {"x": 1}  # type: ignore[attr-defined]
    assert sms.dongle_id is None  # missing in the answer


def test_nested_models_and_lists() -> None:
    mailing = Mailing.construct_from({"mailing_id": 1, "mailing_history": None, "dongle": {"dongle_id": 3}})
    assert mailing.mailing_history is None
    assert mailing.dongle is not None and mailing.dongle.dongle_id == 3

    sms = Sms.construct_from({"sms_id": 1, "replied_from_sms": {"sms_id": 0, "pdus": [{"pdu": "07"}]}})
    assert isinstance(sms.replied_from_sms, Sms)
    assert sms.replied_from_sms.pdus is not None and sms.replied_from_sms.pdus[0].pdu == "07"


def test_enum_value_null() -> None:
    item = DongleListItem.construct_from({"dongle_id": 1, "dongle_online_error_code_id": None})
    assert item.dongle_online_error_code_id is None
    item = DongleListItem.construct_from({"dongle_id": 1, "dongle_online_error_code_id": 2})
    assert item.dongle_online_error_code_id is DongleOnlineErrorCode.TIMEOUT_ERROR


def test_to_dict_keeps_answer_fields_only() -> None:
    sms = Sms.construct_from({"sms_id": 1, "created_at": "2026-11-09 12:42:00", "extra": True})
    assert sms.to_dict() == {"sms_id": 1, "created_at": "2026-11-09T12:42:00Z", "extra": True}
    assert '"sms_id": 1' in sms.to_json()
