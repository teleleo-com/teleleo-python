# File generated from spec/openapi.yaml by scripts/generate.py. Do not edit by hand.

from __future__ import annotations

import datetime
from typing import Iterable, Optional, Union, cast

from typing_extensions import Literal

from .._models import construct_type
from .._pagination import AsyncPage, SyncPage
from .._resource import AsyncAPIResource, SyncAPIResource
from .._types import NOT_GIVEN, Body, Headers, NotGiven, Query, Timeout
from .._utils import path_param
from ..types import Call

__all__ = ["CallsResource", "AsyncCallsResource"]


class CallsResource(SyncAPIResource):
    """Calls of the modems: history, outgoing calls."""

    def list(
        self,
        *,
        call_type_ids: Union[Iterable[int], NotGiven] = NOT_GIVEN,
        duration_presets: Union[Iterable[int], NotGiven] = NOT_GIVEN,
        call_status_ids: Union[Iterable[int], NotGiven] = NOT_GIVEN,
        mailing_history_ids: Union[Iterable[int], NotGiven] = NOT_GIVEN,
        dongle_ids: Union[Iterable[int], NotGiven] = NOT_GIVEN,
        number: Union[str, NotGiven] = NOT_GIVEN,
        caller: Union[str, NotGiven] = NOT_GIVEN,
        receiver: Union[str, NotGiven] = NOT_GIVEN,
        from_: Union[str, datetime.datetime, NotGiven] = NOT_GIVEN,
        to: Union[str, datetime.datetime, NotGiven] = NOT_GIVEN,
        is_empty_file_id: Union[bool, NotGiven] = NOT_GIVEN,
        is_empty_call_scenario_file_id: Union[bool, NotGiven] = NOT_GIVEN,
        page: Union[int, NotGiven] = NOT_GIVEN,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        order_by: Union[str, NotGiven] = NOT_GIVEN,
        order: Union[Literal["asc", "desc"], NotGiven] = NOT_GIVEN,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> SyncPage[Call]:
        """
        List calls.

        Calls of the account, newest first by default. Both the caller and the receiver filters match a
        fragment of the number.

        Args:
          call_type_ids: Array of integers representing call type IDs
          duration_presets: Duration preset filters: 1 - less than 1 minute, 2 - 1-3 minutes, 3 - 3-5 minutes, 4 -
                more than 5 minutes
          call_status_ids: Filter by call status
          mailing_history_ids: Only calls made by these mailing runs
          dongle_ids: Array of integers representing dongle IDs
          number: Name of the field to use for filtering by phone number
          caller: Filter by caller phone number
          receiver: Filter by receiver phone number
          from_: Calls created strictly after this moment. `YYYY-MM-DD HH:MM:SS` in UTC or an RFC 3339 date-time
                with an offset (`2020-01-01T00:00:00Z`, `2020-01-01T03:00:00+03:00`, fractional seconds
                allowed); any other value answers 400 PARSING_DATE_TIME_EXCEPTION.
          to: Calls created strictly before this moment. `YYYY-MM-DD HH:MM:SS` in UTC or an RFC 3339 date-time
                with an offset (`2020-01-01T00:00:00Z`, `2020-01-01T03:00:00+03:00`, fractional seconds
                allowed); any other value answers 400 PARSING_DATE_TIME_EXCEPTION.
          is_empty_file_id: true - only calls without a recording, false - only calls with one.
          is_empty_call_scenario_file_id: true - only calls without a call scenario audio file, false - only calls
                with one.
          page: Page number, 0-based.
          limit: Number of items per page, 1 to 1000.
          order_by: Attribute to sort by, sent together with order. One of: callId, callType, callStatus,
                duration, createdAt, updatedAt, scheduledAt, sentAt.
          order: Sort direction, sent together with order_by. Without order_by and order the list is newest first:
                created_at descending, then the id descending.

        Error codes (``error_message``): REQUEST_VALIDATION_EXCEPTION, PARSING_DATE_TIME_EXCEPTION.
        """
        return self._client._get_page(
            "/call",
            query={
                "call_type_ids[]": call_type_ids,
                "duration_presets[]": duration_presets,
                "call_status_ids[]": call_status_ids,
                "mailing_history_ids[]": mailing_history_ids,
                "dongle_ids[]": dongle_ids,
                "number": number,
                "caller": caller,
                "receiver": receiver,
                "from": from_,
                "to": to,
                "is_empty_file_id": is_empty_file_id,
                "is_empty_call_scenario_file_id": is_empty_call_scenario_file_id,
                "page": page,
                "limit": limit,
                "order_by": order_by,
                "order": order,
            },
            item_key="calls",
            item_type=Call,
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
        )

    def create(
        self,
        dongle_id: int,
        *,
        number: Union[str, NotGiven] = NOT_GIVEN,
        contact_id: Union[int, NotGiven] = NOT_GIVEN,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> Call:
        """
        Make call.

        Starts an outgoing call from the modem to number, or to the phone of the contact contact_id. Works
        where the operator has 3G coverage.

        Args:
          dongle_id: Identifier in the path
          number: Phone number to call, in international format.
          contact_id: Contact whose phone is called; an alternative to number.

        Error codes (``error_message``): DONGLE_ERROR_DONGLE_NOT_FOUND, CALL_ERROR_IDENTIFIER_EMPTY_FIELDS,
        CALL_ERROR_INVALID_RECEIVER_NUMBER, CONTACT_ERROR_IDENTIFIER_CONTACT_NOT_FOUND.
        """
        data = self._client._request(
            "POST",
            f"/dongle/{path_param(dongle_id)}/call",
            body={"number": number, "contact_id": contact_id},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return cast(Call, construct_type(Call, data))

    def get(
        self,
        dongle_id: int,
        call_id: int,
        *,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> Call:
        """
        Get call.

        One call of the modem.

        Args:
          dongle_id: Identifier in the path
          call_id: Identifier in the path

        Error codes (``error_message``): CALL_ERROR_ERROR_CALL_NOT_FOUND.
        """
        data = self._client._request(
            "GET",
            f"/dongle/{path_param(dongle_id)}/call/{path_param(call_id)}",
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
        )
        return cast(Call, construct_type(Call, data))

    def delete(
        self,
        dongle_id: int,
        call_id: int,
        *,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> None:
        """
        Delete call.

        Deletes the call from the history.

        Args:
          dongle_id: Identifier in the path
          call_id: Identifier in the path

        Error codes (``error_message``): CALL_ERROR_ERROR_CALL_NOT_FOUND.
        """
        self._client._request(
            "DELETE",
            f"/dongle/{path_param(dongle_id)}/call/{path_param(call_id)}",
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
        )
        return None


class AsyncCallsResource(AsyncAPIResource):
    """Calls of the modems: history, outgoing calls."""

    async def list(
        self,
        *,
        call_type_ids: Union[Iterable[int], NotGiven] = NOT_GIVEN,
        duration_presets: Union[Iterable[int], NotGiven] = NOT_GIVEN,
        call_status_ids: Union[Iterable[int], NotGiven] = NOT_GIVEN,
        mailing_history_ids: Union[Iterable[int], NotGiven] = NOT_GIVEN,
        dongle_ids: Union[Iterable[int], NotGiven] = NOT_GIVEN,
        number: Union[str, NotGiven] = NOT_GIVEN,
        caller: Union[str, NotGiven] = NOT_GIVEN,
        receiver: Union[str, NotGiven] = NOT_GIVEN,
        from_: Union[str, datetime.datetime, NotGiven] = NOT_GIVEN,
        to: Union[str, datetime.datetime, NotGiven] = NOT_GIVEN,
        is_empty_file_id: Union[bool, NotGiven] = NOT_GIVEN,
        is_empty_call_scenario_file_id: Union[bool, NotGiven] = NOT_GIVEN,
        page: Union[int, NotGiven] = NOT_GIVEN,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        order_by: Union[str, NotGiven] = NOT_GIVEN,
        order: Union[Literal["asc", "desc"], NotGiven] = NOT_GIVEN,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> AsyncPage[Call]:
        """
        List calls.

        Calls of the account, newest first by default. Both the caller and the receiver filters match a
        fragment of the number.

        Args:
          call_type_ids: Array of integers representing call type IDs
          duration_presets: Duration preset filters: 1 - less than 1 minute, 2 - 1-3 minutes, 3 - 3-5 minutes, 4 -
                more than 5 minutes
          call_status_ids: Filter by call status
          mailing_history_ids: Only calls made by these mailing runs
          dongle_ids: Array of integers representing dongle IDs
          number: Name of the field to use for filtering by phone number
          caller: Filter by caller phone number
          receiver: Filter by receiver phone number
          from_: Calls created strictly after this moment. `YYYY-MM-DD HH:MM:SS` in UTC or an RFC 3339 date-time
                with an offset (`2020-01-01T00:00:00Z`, `2020-01-01T03:00:00+03:00`, fractional seconds
                allowed); any other value answers 400 PARSING_DATE_TIME_EXCEPTION.
          to: Calls created strictly before this moment. `YYYY-MM-DD HH:MM:SS` in UTC or an RFC 3339 date-time
                with an offset (`2020-01-01T00:00:00Z`, `2020-01-01T03:00:00+03:00`, fractional seconds
                allowed); any other value answers 400 PARSING_DATE_TIME_EXCEPTION.
          is_empty_file_id: true - only calls without a recording, false - only calls with one.
          is_empty_call_scenario_file_id: true - only calls without a call scenario audio file, false - only calls
                with one.
          page: Page number, 0-based.
          limit: Number of items per page, 1 to 1000.
          order_by: Attribute to sort by, sent together with order. One of: callId, callType, callStatus,
                duration, createdAt, updatedAt, scheduledAt, sentAt.
          order: Sort direction, sent together with order_by. Without order_by and order the list is newest first:
                created_at descending, then the id descending.

        Error codes (``error_message``): REQUEST_VALIDATION_EXCEPTION, PARSING_DATE_TIME_EXCEPTION.
        """
        return await self._client._get_page(
            "/call",
            query={
                "call_type_ids[]": call_type_ids,
                "duration_presets[]": duration_presets,
                "call_status_ids[]": call_status_ids,
                "mailing_history_ids[]": mailing_history_ids,
                "dongle_ids[]": dongle_ids,
                "number": number,
                "caller": caller,
                "receiver": receiver,
                "from": from_,
                "to": to,
                "is_empty_file_id": is_empty_file_id,
                "is_empty_call_scenario_file_id": is_empty_call_scenario_file_id,
                "page": page,
                "limit": limit,
                "order_by": order_by,
                "order": order,
            },
            item_key="calls",
            item_type=Call,
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
        )

    async def create(
        self,
        dongle_id: int,
        *,
        number: Union[str, NotGiven] = NOT_GIVEN,
        contact_id: Union[int, NotGiven] = NOT_GIVEN,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> Call:
        """
        Make call.

        Starts an outgoing call from the modem to number, or to the phone of the contact contact_id. Works
        where the operator has 3G coverage.

        Args:
          dongle_id: Identifier in the path
          number: Phone number to call, in international format.
          contact_id: Contact whose phone is called; an alternative to number.

        Error codes (``error_message``): DONGLE_ERROR_DONGLE_NOT_FOUND, CALL_ERROR_IDENTIFIER_EMPTY_FIELDS,
        CALL_ERROR_INVALID_RECEIVER_NUMBER, CONTACT_ERROR_IDENTIFIER_CONTACT_NOT_FOUND.
        """
        data = await self._client._request(
            "POST",
            f"/dongle/{path_param(dongle_id)}/call",
            body={"number": number, "contact_id": contact_id},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return cast(Call, construct_type(Call, data))

    async def get(
        self,
        dongle_id: int,
        call_id: int,
        *,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> Call:
        """
        Get call.

        One call of the modem.

        Args:
          dongle_id: Identifier in the path
          call_id: Identifier in the path

        Error codes (``error_message``): CALL_ERROR_ERROR_CALL_NOT_FOUND.
        """
        data = await self._client._request(
            "GET",
            f"/dongle/{path_param(dongle_id)}/call/{path_param(call_id)}",
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
        )
        return cast(Call, construct_type(Call, data))

    async def delete(
        self,
        dongle_id: int,
        call_id: int,
        *,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> None:
        """
        Delete call.

        Deletes the call from the history.

        Args:
          dongle_id: Identifier in the path
          call_id: Identifier in the path

        Error codes (``error_message``): CALL_ERROR_ERROR_CALL_NOT_FOUND.
        """
        await self._client._request(
            "DELETE",
            f"/dongle/{path_param(dongle_id)}/call/{path_param(call_id)}",
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
        )
        return None
