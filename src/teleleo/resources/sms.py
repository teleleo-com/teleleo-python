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
from ..types import Sms, SmsThread

__all__ = ["SmsResource", "AsyncSmsResource"]


class SmsResource(SyncAPIResource):
    """SMS of the modems: history, sending, replies, threads."""

    def send(
        self,
        dongle_id: int,
        *,
        number: str,
        message: str,
        scheduled_at: Union[str, datetime.datetime, None, NotGiven] = NOT_GIVEN,
        callback_url: Union[str, NotGiven] = NOT_GIVEN,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> Sms:
        """
        Send SMS.

        Sends an SMS from the modem to a phone number, now or at scheduled_at. sms_status_id 1 (Sended) means
        the mobile network accepted it, not that the handset received it.

        Args:
          dongle_id: ID of the dongle
          number: Recipient phone number
          message: Text message content
          scheduled_at: When to send the SMS, in UTC: `YYYY-MM-DD hh:mm:ss` (for example 2023-01-01 11:11:11),
                without a T, an offset or fractional seconds. Omitted, null or an empty string sends now.
                A value in another format is refused with error_message PARSING_DATE_TIME_EXCEPTION.
          callback_url: Optional callback URL for status updates

        Error codes (``error_message``): REQUEST_VALIDATION_EXCEPTION, PARSING_DATE_TIME_EXCEPTION,
        DONGLE_NOT_FOUND_EXCEPTION, SMS_ERROR_INVALID_RECEIVER_NUMBER,
        SMS_ERROR_IDENTIFIER_INVALID_CALLBACK_URL, BILLING_ERROR_IDENTIFIER_DONGLE_SUBSCRIPTION_NOT_ACTIVE,
        SMS_ERROR_IDENTIFIER_LONG_MESSAGE, SMS_ERROR_IDENTIFIER_INVALID_SCHEDULED_AT,
        SMS_ERROR_IDENTIFIER_EMPTY_FIELDS.
        """
        data = self._client._request(
            "POST",
            f"/dongle/{path_param(dongle_id)}/outgoing-sms",
            body={"number": number, "message": message, "scheduled_at": scheduled_at, "callback_url": callback_url},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return cast(Sms, construct_type(Sms, data))

    def send_to_contact(
        self,
        dongle_id: int,
        *,
        contact_id: int,
        message: str,
        scheduled_at: Union[str, datetime.datetime, None, NotGiven] = NOT_GIVEN,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> Sms:
        """
        Send SMS to contact.

        Sends an SMS from the modem to the phone number of a contact, now or at scheduled_at.

        Args:
          dongle_id: ID of the dongle
          contact_id: Recipient Contact ID
          message: Text message content
          scheduled_at: When to send the SMS, in UTC: `YYYY-MM-DD hh:mm:ss` (for example 2023-01-01 11:11:11),
                without a T, an offset or fractional seconds. Omitted, null or an empty string sends now.
                A value in another format is refused with error_message PARSING_DATE_TIME_EXCEPTION.

        Error codes (``error_message``): REQUEST_VALIDATION_EXCEPTION, PARSING_DATE_TIME_EXCEPTION,
        DONGLE_NOT_FOUND_EXCEPTION, CONTACT_NOT_FOUND_EXCEPTION,
        BILLING_ERROR_IDENTIFIER_DONGLE_SUBSCRIPTION_NOT_ACTIVE, SMS_ERROR_IDENTIFIER_LONG_MESSAGE,
        SMS_ERROR_IDENTIFIER_INVALID_SCHEDULED_AT, SMS_ERROR_IDENTIFIER_EMPTY_FIELDS.
        """
        data = self._client._request(
            "POST",
            f"/dongle/{path_param(dongle_id)}/outgoing-contact-sms",
            body={"contact_id": contact_id, "message": message, "scheduled_at": scheduled_at},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return cast(Sms, construct_type(Sms, data))

    def reply(
        self,
        dongle_id: int,
        *,
        replied_to_sms_id: int,
        message: str,
        scheduled_at: Union[str, datetime.datetime, None, NotGiven] = NOT_GIVEN,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> Sms:
        """
        Reply to SMS.

        Sends an SMS in reply to an SMS of the modem, to its sender; the new SMS carries replied_to_sms_id.

        Args:
          dongle_id: ID of the dongle
          replied_to_sms_id: ID of the SMS message being replied to
          message: Text message content
          scheduled_at: When to send the SMS, in UTC: `YYYY-MM-DD hh:mm:ss` (for example 2023-01-01 11:11:11),
                without a T, an offset or fractional seconds. Omitted, null or an empty string sends now.
                A value in another format is refused with error_message PARSING_DATE_TIME_EXCEPTION.

        Error codes (``error_message``): REQUEST_VALIDATION_EXCEPTION, PARSING_DATE_TIME_EXCEPTION,
        DONGLE_NOT_FOUND_EXCEPTION, SMS_NOT_FOUND_EXCEPTION,
        BILLING_ERROR_IDENTIFIER_DONGLE_SUBSCRIPTION_NOT_ACTIVE, SMS_ERROR_IDENTIFIER_LONG_MESSAGE,
        SMS_ERROR_IDENTIFIER_INVALID_SCHEDULED_AT, SMS_ERROR_IDENTIFIER_EMPTY_FIELDS.
        """
        data = self._client._request(
            "POST",
            f"/dongle/{path_param(dongle_id)}/reply-sms",
            body={"replied_to_sms_id": replied_to_sms_id, "message": message, "scheduled_at": scheduled_at},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return cast(Sms, construct_type(Sms, data))

    def list_threads(
        self,
        *,
        dongle_id: Union[int, NotGiven] = NOT_GIVEN,
        page: Union[int, NotGiven] = NOT_GIVEN,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> SyncPage[SmsThread]:
        """
        List SMS threads.

        Conversation view: the last SMS per phone number of the modem, newest first.

        Args:
          dongle_id: Filter by dongle ID
          page: Page number, 0-based.
          limit: Number of items per page, 1 to 1000.

        Error codes (``error_message``): REQUEST_VALIDATION_EXCEPTION.
        """
        return self._client._get_page(
            "/sms/thread",
            query={"dongle_id": dongle_id, "page": page, "limit": limit},
            item_key="sms_threads",
            item_type=SmsThread,
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
        )

    def list(
        self,
        *,
        sms_type_ids: Union[Iterable[int], NotGiven] = NOT_GIVEN,
        mailing_history_ids: Union[Iterable[int], NotGiven] = NOT_GIVEN,
        page: Union[int, NotGiven] = NOT_GIVEN,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        dongle_ids: Union[Iterable[int], NotGiven] = NOT_GIVEN,
        number: Union[str, NotGiven] = NOT_GIVEN,
        from_: Union[str, datetime.datetime, NotGiven] = NOT_GIVEN,
        to: Union[str, datetime.datetime, NotGiven] = NOT_GIVEN,
        order_by: Union[Literal["createdAt", "smsId", "scheduledAt", "updatedAt"], NotGiven] = NOT_GIVEN,
        order: Union[Literal["asc", "desc"], NotGiven] = NOT_GIVEN,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> SyncPage[Sms]:
        """
        List SMS.

        SMS of all modems of the account, incoming and outgoing. Newest first by default (created_at
        descending, then the id descending).

        Args:
          sms_type_ids: Array of integers representing SMS type IDs
          mailing_history_ids: Array of integers representing mailing history IDs
          page: Page number, 0-based.
          limit: Number of items per page, 1 to 1000.
          dongle_ids: Array of integers representing dongle IDs
          number: Name of the field to use for filtering by phone number
          from_: SMS created at or after this moment. `YYYY-MM-DD HH:MM:SS` in UTC or an RFC 3339 date-time with
                an offset (`2020-01-01T00:00:00Z`, `2020-01-01T03:00:00+03:00`, fractional seconds
                allowed); any other value answers 400 PARSING_DATE_TIME_EXCEPTION.
          to: SMS created before this moment. `YYYY-MM-DD HH:MM:SS` in UTC or an RFC 3339 date-time with an offset
                (`2020-01-01T00:00:00Z`, `2020-01-01T03:00:00+03:00`, fractional seconds allowed); any
                other value answers 400 PARSING_DATE_TIME_EXCEPTION.
          order_by: Attribute to sort by, sent together with order. One of: createdAt, smsId, scheduledAt,
                updatedAt.
          order: Sort direction, sent together with order_by. Without order_by and order the list is newest first:
                created_at descending, then the id descending.

        Error codes (``error_message``): REQUEST_VALIDATION_EXCEPTION, PARSING_DATE_TIME_EXCEPTION,
        SMS_ERROR_IDENTIFIER_INVALID_SMS_TYPE.
        """
        return self._client._get_page(
            "/sms",
            query={
                "sms_type_ids[]": sms_type_ids,
                "mailing_history_ids[]": mailing_history_ids,
                "page": page,
                "limit": limit,
                "dongle_ids[]": dongle_ids,
                "number": number,
                "from": from_,
                "to": to,
                "order_by": order_by,
                "order": order,
            },
            item_key="smses",
            item_type=Sms,
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
        )

    def list_for_dongle(
        self,
        dongle_id: int,
        *,
        sms_type_ids: Union[Iterable[int], NotGiven] = NOT_GIVEN,
        number: Union[str, NotGiven] = NOT_GIVEN,
        from_: Union[str, datetime.datetime, NotGiven] = NOT_GIVEN,
        to: Union[str, datetime.datetime, NotGiven] = NOT_GIVEN,
        page: Union[int, NotGiven] = NOT_GIVEN,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        order_by: Union[Literal["createdAt", "smsId", "scheduledAt", "updatedAt"], NotGiven] = NOT_GIVEN,
        order: Union[Literal["asc", "desc"], NotGiven] = NOT_GIVEN,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> SyncPage[Sms]:
        """
        List modem SMS.

        SMS of one modem, incoming and outgoing. Newest first by default (created_at descending, then the id
        descending).

        Args:
          dongle_id: Identifier in the path
          sms_type_ids: Array of integers representing SMS type IDs
          number: Name of the field to use for filtering by phone number
          from_: SMS created at or after this moment. `YYYY-MM-DD HH:MM:SS` in UTC or an RFC 3339 date-time with
                an offset (`2020-01-01T00:00:00Z`, `2020-01-01T03:00:00+03:00`, fractional seconds
                allowed); any other value answers 400 PARSING_DATE_TIME_EXCEPTION.
          to: SMS created before this moment. `YYYY-MM-DD HH:MM:SS` in UTC or an RFC 3339 date-time with an offset
                (`2020-01-01T00:00:00Z`, `2020-01-01T03:00:00+03:00`, fractional seconds allowed); any
                other value answers 400 PARSING_DATE_TIME_EXCEPTION.
          page: Page number, 0-based.
          limit: Number of items per page, 1 to 1000.
          order_by: Attribute to sort by, sent together with order. One of: createdAt, smsId, scheduledAt,
                updatedAt.
          order: Sort direction, sent together with order_by. Without order_by and order the list is newest first:
                created_at descending, then the id descending.

        Error codes (``error_message``): REQUEST_VALIDATION_EXCEPTION, PARSING_DATE_TIME_EXCEPTION,
        SMS_ERROR_IDENTIFIER_INVALID_SMS_TYPE.
        """
        return self._client._get_page(
            f"/dongle/{path_param(dongle_id)}/sms",
            query={
                "sms_type_ids[]": sms_type_ids,
                "number": number,
                "from": from_,
                "to": to,
                "page": page,
                "limit": limit,
                "order_by": order_by,
                "order": order,
            },
            item_key="smses",
            item_type=Sms,
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
        )

    def get(
        self,
        dongle_id: int,
        sms_id: int,
        *,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> Sms:
        """
        Get SMS.

        One SMS of the modem.

        Args:
          dongle_id: Identifier in the path
          sms_id: Identifier in the path

        Error codes (``error_message``): SMS_ERROR_ERROR_SMS_NOT_FOUND.
        """
        data = self._client._request(
            "GET",
            f"/dongle/{path_param(dongle_id)}/sms/{path_param(sms_id)}",
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
        )
        return cast(Sms, construct_type(Sms, data))

    def update(
        self,
        dongle_id: int,
        sms_id: int,
        *,
        number: Union[str, NotGiven] = NOT_GIVEN,
        message: Union[str, NotGiven] = NOT_GIVEN,
        contact_id: Union[int, NotGiven] = NOT_GIVEN,
        new_dongle_id: Union[int, NotGiven] = NOT_GIVEN,
        scheduled_at: Union[str, datetime.datetime, None, NotGiven] = NOT_GIVEN,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> Sms:
        """
        Update SMS.

        Changes a scheduled SMS (sms_type_id 5) that is not sent yet: number, text, contact, scheduled_at;
        omitted fields keep their values. Any other SMS answers SMS_ERROR_ERROR_SMS_NOT_FOUND.

        Args:
          dongle_id: Identifier in the path
          sms_id: Identifier in the path

        Error codes (``error_message``): SMS_ERROR_ERROR_SMS_NOT_FOUND, DONGLE_ERROR_DONGLE_NOT_FOUND,
        CONTACT_ERROR_IDENTIFIER_CONTACT_NOT_FOUND, SMS_ERROR_IDENTIFIER_INVALID_SMS_TYPE,
        SMS_ERROR_IDENTIFIER_LONG_MESSAGE, SMS_ERROR_IDENTIFIER_INVALID_SCHEDULED_AT,
        PARSING_DATE_TIME_EXCEPTION.
        """
        data = self._client._request(
            "PUT",
            f"/dongle/{path_param(dongle_id)}/sms/{path_param(sms_id)}",
            body={
                "number": number,
                "message": message,
                "contact_id": contact_id,
                "dongle_id": new_dongle_id,
                "scheduled_at": scheduled_at,
            },
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return cast(Sms, construct_type(Sms, data))

    def delete(
        self,
        dongle_id: int,
        sms_id: int,
        *,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> None:
        """
        Delete SMS.

        Deletes the SMS from the history of the modem. An SMS in status 1 (Sended) or 5 (Enqueued) cannot be
        deleted and answers SMS_ERROR_ERROR_SMS_NOT_FOUND.

        Args:
          dongle_id: Identifier in the path
          sms_id: Identifier in the path

        Error codes (``error_message``): SMS_ERROR_ERROR_SMS_NOT_FOUND.
        """
        self._client._request(
            "DELETE",
            f"/dongle/{path_param(dongle_id)}/sms/{path_param(sms_id)}",
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
        )
        return None


class AsyncSmsResource(AsyncAPIResource):
    """SMS of the modems: history, sending, replies, threads."""

    async def send(
        self,
        dongle_id: int,
        *,
        number: str,
        message: str,
        scheduled_at: Union[str, datetime.datetime, None, NotGiven] = NOT_GIVEN,
        callback_url: Union[str, NotGiven] = NOT_GIVEN,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> Sms:
        """
        Send SMS.

        Sends an SMS from the modem to a phone number, now or at scheduled_at. sms_status_id 1 (Sended) means
        the mobile network accepted it, not that the handset received it.

        Args:
          dongle_id: ID of the dongle
          number: Recipient phone number
          message: Text message content
          scheduled_at: When to send the SMS, in UTC: `YYYY-MM-DD hh:mm:ss` (for example 2023-01-01 11:11:11),
                without a T, an offset or fractional seconds. Omitted, null or an empty string sends now.
                A value in another format is refused with error_message PARSING_DATE_TIME_EXCEPTION.
          callback_url: Optional callback URL for status updates

        Error codes (``error_message``): REQUEST_VALIDATION_EXCEPTION, PARSING_DATE_TIME_EXCEPTION,
        DONGLE_NOT_FOUND_EXCEPTION, SMS_ERROR_INVALID_RECEIVER_NUMBER,
        SMS_ERROR_IDENTIFIER_INVALID_CALLBACK_URL, BILLING_ERROR_IDENTIFIER_DONGLE_SUBSCRIPTION_NOT_ACTIVE,
        SMS_ERROR_IDENTIFIER_LONG_MESSAGE, SMS_ERROR_IDENTIFIER_INVALID_SCHEDULED_AT,
        SMS_ERROR_IDENTIFIER_EMPTY_FIELDS.
        """
        data = await self._client._request(
            "POST",
            f"/dongle/{path_param(dongle_id)}/outgoing-sms",
            body={"number": number, "message": message, "scheduled_at": scheduled_at, "callback_url": callback_url},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return cast(Sms, construct_type(Sms, data))

    async def send_to_contact(
        self,
        dongle_id: int,
        *,
        contact_id: int,
        message: str,
        scheduled_at: Union[str, datetime.datetime, None, NotGiven] = NOT_GIVEN,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> Sms:
        """
        Send SMS to contact.

        Sends an SMS from the modem to the phone number of a contact, now or at scheduled_at.

        Args:
          dongle_id: ID of the dongle
          contact_id: Recipient Contact ID
          message: Text message content
          scheduled_at: When to send the SMS, in UTC: `YYYY-MM-DD hh:mm:ss` (for example 2023-01-01 11:11:11),
                without a T, an offset or fractional seconds. Omitted, null or an empty string sends now.
                A value in another format is refused with error_message PARSING_DATE_TIME_EXCEPTION.

        Error codes (``error_message``): REQUEST_VALIDATION_EXCEPTION, PARSING_DATE_TIME_EXCEPTION,
        DONGLE_NOT_FOUND_EXCEPTION, CONTACT_NOT_FOUND_EXCEPTION,
        BILLING_ERROR_IDENTIFIER_DONGLE_SUBSCRIPTION_NOT_ACTIVE, SMS_ERROR_IDENTIFIER_LONG_MESSAGE,
        SMS_ERROR_IDENTIFIER_INVALID_SCHEDULED_AT, SMS_ERROR_IDENTIFIER_EMPTY_FIELDS.
        """
        data = await self._client._request(
            "POST",
            f"/dongle/{path_param(dongle_id)}/outgoing-contact-sms",
            body={"contact_id": contact_id, "message": message, "scheduled_at": scheduled_at},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return cast(Sms, construct_type(Sms, data))

    async def reply(
        self,
        dongle_id: int,
        *,
        replied_to_sms_id: int,
        message: str,
        scheduled_at: Union[str, datetime.datetime, None, NotGiven] = NOT_GIVEN,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> Sms:
        """
        Reply to SMS.

        Sends an SMS in reply to an SMS of the modem, to its sender; the new SMS carries replied_to_sms_id.

        Args:
          dongle_id: ID of the dongle
          replied_to_sms_id: ID of the SMS message being replied to
          message: Text message content
          scheduled_at: When to send the SMS, in UTC: `YYYY-MM-DD hh:mm:ss` (for example 2023-01-01 11:11:11),
                without a T, an offset or fractional seconds. Omitted, null or an empty string sends now.
                A value in another format is refused with error_message PARSING_DATE_TIME_EXCEPTION.

        Error codes (``error_message``): REQUEST_VALIDATION_EXCEPTION, PARSING_DATE_TIME_EXCEPTION,
        DONGLE_NOT_FOUND_EXCEPTION, SMS_NOT_FOUND_EXCEPTION,
        BILLING_ERROR_IDENTIFIER_DONGLE_SUBSCRIPTION_NOT_ACTIVE, SMS_ERROR_IDENTIFIER_LONG_MESSAGE,
        SMS_ERROR_IDENTIFIER_INVALID_SCHEDULED_AT, SMS_ERROR_IDENTIFIER_EMPTY_FIELDS.
        """
        data = await self._client._request(
            "POST",
            f"/dongle/{path_param(dongle_id)}/reply-sms",
            body={"replied_to_sms_id": replied_to_sms_id, "message": message, "scheduled_at": scheduled_at},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return cast(Sms, construct_type(Sms, data))

    async def list_threads(
        self,
        *,
        dongle_id: Union[int, NotGiven] = NOT_GIVEN,
        page: Union[int, NotGiven] = NOT_GIVEN,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> AsyncPage[SmsThread]:
        """
        List SMS threads.

        Conversation view: the last SMS per phone number of the modem, newest first.

        Args:
          dongle_id: Filter by dongle ID
          page: Page number, 0-based.
          limit: Number of items per page, 1 to 1000.

        Error codes (``error_message``): REQUEST_VALIDATION_EXCEPTION.
        """
        return await self._client._get_page(
            "/sms/thread",
            query={"dongle_id": dongle_id, "page": page, "limit": limit},
            item_key="sms_threads",
            item_type=SmsThread,
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
        )

    async def list(
        self,
        *,
        sms_type_ids: Union[Iterable[int], NotGiven] = NOT_GIVEN,
        mailing_history_ids: Union[Iterable[int], NotGiven] = NOT_GIVEN,
        page: Union[int, NotGiven] = NOT_GIVEN,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        dongle_ids: Union[Iterable[int], NotGiven] = NOT_GIVEN,
        number: Union[str, NotGiven] = NOT_GIVEN,
        from_: Union[str, datetime.datetime, NotGiven] = NOT_GIVEN,
        to: Union[str, datetime.datetime, NotGiven] = NOT_GIVEN,
        order_by: Union[Literal["createdAt", "smsId", "scheduledAt", "updatedAt"], NotGiven] = NOT_GIVEN,
        order: Union[Literal["asc", "desc"], NotGiven] = NOT_GIVEN,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> AsyncPage[Sms]:
        """
        List SMS.

        SMS of all modems of the account, incoming and outgoing. Newest first by default (created_at
        descending, then the id descending).

        Args:
          sms_type_ids: Array of integers representing SMS type IDs
          mailing_history_ids: Array of integers representing mailing history IDs
          page: Page number, 0-based.
          limit: Number of items per page, 1 to 1000.
          dongle_ids: Array of integers representing dongle IDs
          number: Name of the field to use for filtering by phone number
          from_: SMS created at or after this moment. `YYYY-MM-DD HH:MM:SS` in UTC or an RFC 3339 date-time with
                an offset (`2020-01-01T00:00:00Z`, `2020-01-01T03:00:00+03:00`, fractional seconds
                allowed); any other value answers 400 PARSING_DATE_TIME_EXCEPTION.
          to: SMS created before this moment. `YYYY-MM-DD HH:MM:SS` in UTC or an RFC 3339 date-time with an offset
                (`2020-01-01T00:00:00Z`, `2020-01-01T03:00:00+03:00`, fractional seconds allowed); any
                other value answers 400 PARSING_DATE_TIME_EXCEPTION.
          order_by: Attribute to sort by, sent together with order. One of: createdAt, smsId, scheduledAt,
                updatedAt.
          order: Sort direction, sent together with order_by. Without order_by and order the list is newest first:
                created_at descending, then the id descending.

        Error codes (``error_message``): REQUEST_VALIDATION_EXCEPTION, PARSING_DATE_TIME_EXCEPTION,
        SMS_ERROR_IDENTIFIER_INVALID_SMS_TYPE.
        """
        return await self._client._get_page(
            "/sms",
            query={
                "sms_type_ids[]": sms_type_ids,
                "mailing_history_ids[]": mailing_history_ids,
                "page": page,
                "limit": limit,
                "dongle_ids[]": dongle_ids,
                "number": number,
                "from": from_,
                "to": to,
                "order_by": order_by,
                "order": order,
            },
            item_key="smses",
            item_type=Sms,
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
        )

    async def list_for_dongle(
        self,
        dongle_id: int,
        *,
        sms_type_ids: Union[Iterable[int], NotGiven] = NOT_GIVEN,
        number: Union[str, NotGiven] = NOT_GIVEN,
        from_: Union[str, datetime.datetime, NotGiven] = NOT_GIVEN,
        to: Union[str, datetime.datetime, NotGiven] = NOT_GIVEN,
        page: Union[int, NotGiven] = NOT_GIVEN,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        order_by: Union[Literal["createdAt", "smsId", "scheduledAt", "updatedAt"], NotGiven] = NOT_GIVEN,
        order: Union[Literal["asc", "desc"], NotGiven] = NOT_GIVEN,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> AsyncPage[Sms]:
        """
        List modem SMS.

        SMS of one modem, incoming and outgoing. Newest first by default (created_at descending, then the id
        descending).

        Args:
          dongle_id: Identifier in the path
          sms_type_ids: Array of integers representing SMS type IDs
          number: Name of the field to use for filtering by phone number
          from_: SMS created at or after this moment. `YYYY-MM-DD HH:MM:SS` in UTC or an RFC 3339 date-time with
                an offset (`2020-01-01T00:00:00Z`, `2020-01-01T03:00:00+03:00`, fractional seconds
                allowed); any other value answers 400 PARSING_DATE_TIME_EXCEPTION.
          to: SMS created before this moment. `YYYY-MM-DD HH:MM:SS` in UTC or an RFC 3339 date-time with an offset
                (`2020-01-01T00:00:00Z`, `2020-01-01T03:00:00+03:00`, fractional seconds allowed); any
                other value answers 400 PARSING_DATE_TIME_EXCEPTION.
          page: Page number, 0-based.
          limit: Number of items per page, 1 to 1000.
          order_by: Attribute to sort by, sent together with order. One of: createdAt, smsId, scheduledAt,
                updatedAt.
          order: Sort direction, sent together with order_by. Without order_by and order the list is newest first:
                created_at descending, then the id descending.

        Error codes (``error_message``): REQUEST_VALIDATION_EXCEPTION, PARSING_DATE_TIME_EXCEPTION,
        SMS_ERROR_IDENTIFIER_INVALID_SMS_TYPE.
        """
        return await self._client._get_page(
            f"/dongle/{path_param(dongle_id)}/sms",
            query={
                "sms_type_ids[]": sms_type_ids,
                "number": number,
                "from": from_,
                "to": to,
                "page": page,
                "limit": limit,
                "order_by": order_by,
                "order": order,
            },
            item_key="smses",
            item_type=Sms,
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
        )

    async def get(
        self,
        dongle_id: int,
        sms_id: int,
        *,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> Sms:
        """
        Get SMS.

        One SMS of the modem.

        Args:
          dongle_id: Identifier in the path
          sms_id: Identifier in the path

        Error codes (``error_message``): SMS_ERROR_ERROR_SMS_NOT_FOUND.
        """
        data = await self._client._request(
            "GET",
            f"/dongle/{path_param(dongle_id)}/sms/{path_param(sms_id)}",
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
        )
        return cast(Sms, construct_type(Sms, data))

    async def update(
        self,
        dongle_id: int,
        sms_id: int,
        *,
        number: Union[str, NotGiven] = NOT_GIVEN,
        message: Union[str, NotGiven] = NOT_GIVEN,
        contact_id: Union[int, NotGiven] = NOT_GIVEN,
        new_dongle_id: Union[int, NotGiven] = NOT_GIVEN,
        scheduled_at: Union[str, datetime.datetime, None, NotGiven] = NOT_GIVEN,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> Sms:
        """
        Update SMS.

        Changes a scheduled SMS (sms_type_id 5) that is not sent yet: number, text, contact, scheduled_at;
        omitted fields keep their values. Any other SMS answers SMS_ERROR_ERROR_SMS_NOT_FOUND.

        Args:
          dongle_id: Identifier in the path
          sms_id: Identifier in the path

        Error codes (``error_message``): SMS_ERROR_ERROR_SMS_NOT_FOUND, DONGLE_ERROR_DONGLE_NOT_FOUND,
        CONTACT_ERROR_IDENTIFIER_CONTACT_NOT_FOUND, SMS_ERROR_IDENTIFIER_INVALID_SMS_TYPE,
        SMS_ERROR_IDENTIFIER_LONG_MESSAGE, SMS_ERROR_IDENTIFIER_INVALID_SCHEDULED_AT,
        PARSING_DATE_TIME_EXCEPTION.
        """
        data = await self._client._request(
            "PUT",
            f"/dongle/{path_param(dongle_id)}/sms/{path_param(sms_id)}",
            body={
                "number": number,
                "message": message,
                "contact_id": contact_id,
                "dongle_id": new_dongle_id,
                "scheduled_at": scheduled_at,
            },
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return cast(Sms, construct_type(Sms, data))

    async def delete(
        self,
        dongle_id: int,
        sms_id: int,
        *,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> None:
        """
        Delete SMS.

        Deletes the SMS from the history of the modem. An SMS in status 1 (Sended) or 5 (Enqueued) cannot be
        deleted and answers SMS_ERROR_ERROR_SMS_NOT_FOUND.

        Args:
          dongle_id: Identifier in the path
          sms_id: Identifier in the path

        Error codes (``error_message``): SMS_ERROR_ERROR_SMS_NOT_FOUND.
        """
        await self._client._request(
            "DELETE",
            f"/dongle/{path_param(dongle_id)}/sms/{path_param(sms_id)}",
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
        )
        return None
