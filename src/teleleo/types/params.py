# File generated from spec/openapi.yaml by scripts/generate.py. Do not edit by hand.

from __future__ import annotations

from typing import List, Optional

from typing_extensions import TypedDict

__all__ = ["ImportContactRowParam", "RedirectionConditionParam", "RedirectionParamsParam"]


class ImportContactRowParam(TypedDict, total=False):
    A: Optional[str]
    """Contact name"""

    B: str
    """Contact phone"""

    C: Optional[str]
    """Contact email"""


class RedirectionConditionParam(TypedDict, total=False):
    """
    When the redirection fires: one rule, checked against every incoming SMS (redirection types 1, 3, 4, 5) or
    incoming call (type 2) of the account.

    A rule is a JSON array. A comparison is `[operator, field, value]`; `["and", rule, rule, ...]` and `["or",
    rule, rule, ...]` combine rules. The top level is a single rule, usually `and`.

    Fields are the attributes of the event, prefixed by the object: `sms_<field>` (the SMS schema:
    `sms_number_caller`, `sms_contact_id`, `sms_initial_contact_group_ids`, `sms_sms_source_type_id`,
    `sms_message_decoded`, ...), `call_<field>` (the call: `call_number_caller`, `call_contact_id`,
    `call_initial_contact_group_ids`, ...), `dongle_<field>` (the modem that received it: `dongle_dongle_id`,
    `dongle_name`, ...) and `contact_<field>` (the contact of the sender, when there is one). A field the
    event does not have compares as null.

    Operators: `=`, `!=`, `<`, `>` (one value); `in`, `!in` (a list of values); `regexp`, `!regexp` (a PCRE
    with delimiters, for example `/^bank$/ui`); `like`, `!like` (case-insensitive substring);
    `intersect_source`, `!intersect_source` (a list field such as `sms_initial_contact_group_ids` shares a
    value with the list); `is_empty`, `!is_empty` (`[operator, field]`, no value).

    Checked on save (400 CONDITION_NOT_VALID_EXCEPTION unless said otherwise):
    - the rule must parse: not empty, a known operator, the right number and types of arguments;
    - `["in", "dongle_dongle_id", [ids]]` as a direct child of the top-level `and` limits the redirection to
    these modems (GET /redirection filters by it too); every id must be a modem of the account with an active
    tariff (400 DONGLE_NOT_FOUND for an unknown id or an id of another account, a tariff error otherwise).
    Without it the redirection applies to every modem;
    - a `regexp` inside an `or` that is a direct child of the top-level rule may only test `sms_number_caller`
    or `call_number_caller` and must be `/^<letters or digits>$/ui` (an alphanumeric sender name);
    - for an auto reply (type 3), every number of a `sms_number_caller` list that is a direct child of the
    top-level rule is a valid phone number in `+<digits>` form.
    """

    pass


class RedirectionParamsParam(TypedDict, total=False):
    """
    What the redirection does. Required keys depend on redirection_type_id (400 PARAMS_NOT_VALID_EXCEPTION
    otherwise):
    - 1 (SMS) and 2 (call): at least one delivery target - a non-empty `email`, or at least one item in
    `emails` or `telegram_chat_ids`;
    - 3 (auto reply): `auto_reply_message`;
    - 4 (silent) and 5 (HTTP): `url`, an absolute URL.

    Other keys are stored as sent and returned as is.
    """

    email: str
    """One e-mail address to deliver to (types 1 and 2)."""

    emails: List[str]
    """E-mail addresses to deliver to (types 1 and 2); each must be a valid address."""

    telegram_chat_ids: List[str]
    """
    Telegram chat ids to deliver to (types 1 and 2); digits with an optional leading minus, as a string or a
    number.
    """

    auto_reply_message: str
    """Text of the reply SMS (type 3, required)."""

    forwarding_message: str
    """Optional text stored with the redirection."""

    url: str
    """URL that receives the event (types 4 and 5, required)."""
