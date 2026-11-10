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
from ..types import Mailing

__all__ = ["MailingsResource", "AsyncMailingsResource"]


class MailingsResource(SyncAPIResource):
    """Bulk SMS and call campaigns."""

    def list(
        self,
        *,
        page: Union[int, NotGiven] = NOT_GIVEN,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        order_by: Union[str, NotGiven] = NOT_GIVEN,
        order: Union[Literal["asc", "desc"], NotGiven] = NOT_GIVEN,
        from_: Union[str, datetime.datetime, NotGiven] = NOT_GIVEN,
        to: Union[str, datetime.datetime, NotGiven] = NOT_GIVEN,
        is_deleted: Union[bool, NotGiven] = NOT_GIVEN,
        created_at_from: Union[str, datetime.datetime, NotGiven] = NOT_GIVEN,
        created_at_to: Union[str, datetime.datetime, NotGiven] = NOT_GIVEN,
        scheduled_at_from: Union[str, datetime.datetime, NotGiven] = NOT_GIVEN,
        scheduled_at_to: Union[str, datetime.datetime, NotGiven] = NOT_GIVEN,
        dongle_ids: Union[Iterable[int], NotGiven] = NOT_GIVEN,
        dongle_name: Union[str, NotGiven] = NOT_GIVEN,
        mailing_status_ids: Union[Iterable[int], NotGiven] = NOT_GIVEN,
        mailing_type_id: Union[int, NotGiven] = NOT_GIVEN,
        mailing_entity_type_id: Union[int, NotGiven] = NOT_GIVEN,
        mailing_entity_type_ids: Union[Iterable[int], NotGiven] = NOT_GIVEN,
        mailing_history_id: Union[int, NotGiven] = NOT_GIVEN,
        mailing_history_ids: Union[Iterable[int], NotGiven] = NOT_GIVEN,
        name: Union[str, NotGiven] = NOT_GIVEN,
        text: Union[str, NotGiven] = NOT_GIVEN,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> SyncPage[Mailing]:
        """
        List mailings.

        Mailings (bulk SMS or call campaigns) of the account. Newest first by default (created_at descending,
        then the id descending).

        Args:
          page: Page number, 0-based.
          limit: Number of items per page, 1 to 1000.
          order_by: Attribute to sort by, sent together with order. One of: mailingId, name, scheduledAt,
                createdAt, updatedAt.
          order: Sort direction, sent together with order_by. Without order_by and order the list is newest first:
                created_at descending, then the id descending.
          from_: Alias of created_at_from. `YYYY-MM-DD HH:MM:SS` in UTC or an RFC 3339 date-time with an offset
                (`2020-01-01T00:00:00Z`, `2020-01-01T03:00:00+03:00`, fractional seconds allowed); any
                other value answers 400 PARSING_DATE_TIME_EXCEPTION.
          to: Alias of created_at_to. `YYYY-MM-DD HH:MM:SS` in UTC or an RFC 3339 date-time with an offset
                (`2020-01-01T00:00:00Z`, `2020-01-01T03:00:00+03:00`, fractional seconds allowed); any
                other value answers 400 PARSING_DATE_TIME_EXCEPTION.
          is_deleted: Filter by deletion state. Omitted -> all (legacy default); true -> only deleted; false ->
                only alive.
          created_at_from: Mailings created at or after this moment. `YYYY-MM-DD HH:MM:SS` in UTC or an RFC 3339
                date-time with an offset (`2020-01-01T00:00:00Z`, `2020-01-01T03:00:00+03:00`, fractional
                seconds allowed); any other value answers 400 PARSING_DATE_TIME_EXCEPTION.
          created_at_to: Mailings created at or before this moment. `YYYY-MM-DD HH:MM:SS` in UTC or an RFC 3339
                date-time with an offset (`2020-01-01T00:00:00Z`, `2020-01-01T03:00:00+03:00`, fractional
                seconds allowed); any other value answers 400 PARSING_DATE_TIME_EXCEPTION.
          scheduled_at_from: Mailings scheduled at or after this moment. `YYYY-MM-DD HH:MM:SS` in UTC or an RFC
                3339 date-time with an offset (`2020-01-01T00:00:00Z`, `2020-01-01T03:00:00+03:00`,
                fractional seconds allowed); any other value answers 400 PARSING_DATE_TIME_EXCEPTION.
          scheduled_at_to: Mailings scheduled at or before this moment. `YYYY-MM-DD HH:MM:SS` in UTC or an RFC
                3339 date-time with an offset (`2020-01-01T00:00:00Z`, `2020-01-01T03:00:00+03:00`,
                fractional seconds allowed); any other value answers 400 PARSING_DATE_TIME_EXCEPTION.
          dongle_ids: Filter by dongle ids.
          dongle_name: Filter by dongle name (substring).
          mailing_status_ids: Filter by mailing status ids.
          mailing_type_id: Filter by mailing type id.
          mailing_entity_type_id: Filter by mailing entity type id.
          mailing_entity_type_ids: Filter by mailing entity type ids.
          mailing_history_id: Filter by mailing history id.
          mailing_history_ids: Filter by mailing history ids.
          name: Filter by mailing name (substring).
          text: Filter by mailing text (substring).

        Error codes (``error_message``): REQUEST_VALIDATION_EXCEPTION, PARSING_DATE_TIME_EXCEPTION.
        """
        return self._client._get_page(
            "/mailing",
            query={
                "page": page,
                "limit": limit,
                "order_by": order_by,
                "order": order,
                "from": from_,
                "to": to,
                "is_deleted": is_deleted,
                "created_at_from": created_at_from,
                "created_at_to": created_at_to,
                "scheduled_at_from": scheduled_at_from,
                "scheduled_at_to": scheduled_at_to,
                "dongle_ids[]": dongle_ids,
                "dongle_name": dongle_name,
                "mailing_status_ids[]": mailing_status_ids,
                "mailing_type_id": mailing_type_id,
                "mailing_entity_type_id": mailing_entity_type_id,
                "mailing_entity_type_ids[]": mailing_entity_type_ids,
                "mailing_history_id": mailing_history_id,
                "mailing_history_ids[]": mailing_history_ids,
                "name": name,
                "text": text,
            },
            item_key="mailings",
            item_type=Mailing,
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
        )

    def create(
        self,
        *,
        name: str,
        mailing_type_id: int,
        mailing_entity_type_id: int,
        dongle_id: int,
        text: Union[str, NotGiven] = NOT_GIVEN,
        scheduled_at: Union[str, datetime.datetime, None, NotGiven] = NOT_GIVEN,
        mailing_status_id: Union[int, None, NotGiven] = NOT_GIVEN,
        is_call_record: Union[bool, NotGiven] = NOT_GIVEN,
        tmp_file_id: Union[str, None, NotGiven] = NOT_GIVEN,
        mailing_phones: Union[Iterable[str], NotGiven] = NOT_GIVEN,
        mailing_contact_ids: Union[Iterable[int], NotGiven] = NOT_GIVEN,
        mailing_contact_group_ids: Union[Iterable[int], NotGiven] = NOT_GIVEN,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> Mailing:
        """
        Create mailing.

        Creates an SMS or call mailing. Use POST /mailing/sms or POST /mailing/call instead.

        Args:
          tmp_file_id: Temporary audio file: tmp_file_id returned by POST /file/upload-tmp or POST /file/generate-
                speech, `<2 hex>/<32 hex>/<file name>`. Used by a call mailing.

        Error codes (``error_message``): REQUEST_VALIDATION_EXCEPTION, DONGLE_NOT_FOUND_EXCEPTION,
        PARSING_DATE_TIME_EXCEPTION, MAILING_MANAGEMENT_INVALID_STATUS_FOR_CREATE,
        MAILING_MANAGEMENT_INVALID_SCHEDULED_AT, MAILING_MANAGEMENT_DONGLE_TARIFF_INVALID,
        MAILING_MANAGEMENT_INVALID_PHONE, MAILING_MANAGEMENT_NO_RECIPIENTS,
        MAILING_MANAGEMENT_CONTACT_NOT_FOUND, MAILING_MANAGEMENT_CONTACT_GROUP_NOT_FOUND,
        MAILING_MANAGEMENT_DONGLE_SMS_LIMIT_EXCEEDED, TMP_FILE_NOT_FOUND.
        """
        data = self._client._request(
            "POST",
            "/mailing",
            body={
                "name": name,
                "text": text,
                "mailing_type_id": mailing_type_id,
                "mailing_entity_type_id": mailing_entity_type_id,
                "dongle_id": dongle_id,
                "scheduled_at": scheduled_at,
                "mailing_status_id": mailing_status_id,
                "is_call_record": is_call_record,
                "tmp_file_id": tmp_file_id,
                "mailing_phones": mailing_phones,
                "mailing_contact_ids": mailing_contact_ids,
                "mailing_contact_group_ids": mailing_contact_group_ids,
            },
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return cast(Mailing, construct_type(Mailing, data))

    def create_sms(
        self,
        *,
        name: str,
        text: str,
        mailing_type_id: int,
        dongle_id: int,
        scheduled_at: Union[str, datetime.datetime, None, NotGiven] = NOT_GIVEN,
        mailing_status_id: Union[int, None, NotGiven] = NOT_GIVEN,
        mailing_phones: Union[Iterable[str], NotGiven] = NOT_GIVEN,
        mailing_contact_ids: Union[Iterable[int], NotGiven] = NOT_GIVEN,
        mailing_contact_group_ids: Union[Iterable[int], NotGiven] = NOT_GIVEN,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> Mailing:
        """
        Create SMS mailing.

        Creates an SMS mailing to the listed phones, contacts and contact groups, sent now or at scheduled_at.

        Error codes (``error_message``): REQUEST_VALIDATION_EXCEPTION, DONGLE_NOT_FOUND_EXCEPTION,
        PARSING_DATE_TIME_EXCEPTION, MAILING_MANAGEMENT_INVALID_STATUS_FOR_CREATE,
        MAILING_MANAGEMENT_INVALID_SCHEDULED_AT, MAILING_MANAGEMENT_DONGLE_TARIFF_INVALID,
        MAILING_MANAGEMENT_INVALID_PHONE, MAILING_MANAGEMENT_NO_RECIPIENTS,
        MAILING_MANAGEMENT_CONTACT_NOT_FOUND, MAILING_MANAGEMENT_CONTACT_GROUP_NOT_FOUND,
        MAILING_MANAGEMENT_DONGLE_SMS_LIMIT_EXCEEDED.
        """
        data = self._client._request(
            "POST",
            "/mailing/sms",
            body={
                "name": name,
                "text": text,
                "mailing_type_id": mailing_type_id,
                "dongle_id": dongle_id,
                "scheduled_at": scheduled_at,
                "mailing_status_id": mailing_status_id,
                "mailing_phones": mailing_phones,
                "mailing_contact_ids": mailing_contact_ids,
                "mailing_contact_group_ids": mailing_contact_group_ids,
            },
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return cast(Mailing, construct_type(Mailing, data))

    def create_call(
        self,
        *,
        name: str,
        mailing_type_id: int,
        dongle_id: int,
        text: Union[str, None, NotGiven] = NOT_GIVEN,
        is_call_record: Union[bool, NotGiven] = NOT_GIVEN,
        tmp_file_id: Union[str, None, NotGiven] = NOT_GIVEN,
        scheduled_at: Union[str, datetime.datetime, None, NotGiven] = NOT_GIVEN,
        mailing_status_id: Union[int, None, NotGiven] = NOT_GIVEN,
        mailing_phones: Union[Iterable[str], NotGiven] = NOT_GIVEN,
        mailing_contact_ids: Union[Iterable[int], NotGiven] = NOT_GIVEN,
        mailing_contact_group_ids: Union[Iterable[int], NotGiven] = NOT_GIVEN,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> Mailing:
        """
        Create call mailing.

        Creates a call mailing that plays an audio file (tmp_file_id) to the listed phones, contacts and
        contact groups.

        Args:
          tmp_file_id: Temporary audio file: tmp_file_id returned by POST /file/upload-tmp or POST /file/generate-
                speech, `<2 hex>/<32 hex>/<file name>`. Used by a call mailing.

        Error codes (``error_message``): REQUEST_VALIDATION_EXCEPTION, DONGLE_NOT_FOUND_EXCEPTION,
        PARSING_DATE_TIME_EXCEPTION, MAILING_MANAGEMENT_INVALID_STATUS_FOR_CREATE,
        MAILING_MANAGEMENT_INVALID_SCHEDULED_AT, MAILING_MANAGEMENT_DONGLE_TARIFF_INVALID,
        MAILING_MANAGEMENT_INVALID_PHONE, MAILING_MANAGEMENT_NO_RECIPIENTS,
        MAILING_MANAGEMENT_CONTACT_NOT_FOUND, MAILING_MANAGEMENT_CONTACT_GROUP_NOT_FOUND, TMP_FILE_NOT_FOUND.
        """
        data = self._client._request(
            "POST",
            "/mailing/call",
            body={
                "name": name,
                "text": text,
                "mailing_type_id": mailing_type_id,
                "dongle_id": dongle_id,
                "is_call_record": is_call_record,
                "tmp_file_id": tmp_file_id,
                "scheduled_at": scheduled_at,
                "mailing_status_id": mailing_status_id,
                "mailing_phones": mailing_phones,
                "mailing_contact_ids": mailing_contact_ids,
                "mailing_contact_group_ids": mailing_contact_group_ids,
            },
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return cast(Mailing, construct_type(Mailing, data))

    def get(
        self,
        mailing_id: int,
        *,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> Mailing:
        """
        Get mailing.

        One mailing of the account with its recipients and its last run.

        Args:
          mailing_id: Identifier in the path

        Error codes (``error_message``): REQUEST_VALIDATION_EXCEPTION, MAILING_NOT_FOUND.
        """
        data = self._client._request(
            "GET",
            f"/mailing/{path_param(mailing_id)}",
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
        )
        return cast(Mailing, construct_type(Mailing, data))

    def update(
        self,
        mailing_id: int,
        *,
        name: Union[str, None, NotGiven] = NOT_GIVEN,
        text: Union[str, None, NotGiven] = NOT_GIVEN,
        mailing_type_id: Union[int, None, NotGiven] = NOT_GIVEN,
        mailing_status_id: Union[int, None, NotGiven] = NOT_GIVEN,
        scheduled_at: Union[str, datetime.datetime, None, NotGiven] = NOT_GIVEN,
        is_deleted: Union[bool, None, NotGiven] = NOT_GIVEN,
        tmp_file_id: Union[str, None, NotGiven] = NOT_GIVEN,
        mailing_phones: Union[Iterable[str], NotGiven] = NOT_GIVEN,
        mailing_contact_ids: Union[Iterable[int], NotGiven] = NOT_GIVEN,
        mailing_contact_group_ids: Union[Iterable[int], NotGiven] = NOT_GIVEN,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> Mailing:
        """
        Update mailing.

        Changes the mailing; omitted fields keep their values.

        Args:
          mailing_id: Identifier in the path
          mailing_type_id: 1: Simple (sent at once), 2: Delayed (sent at scheduled_at).
          mailing_status_id: 1: Draft, 2: Planned, 3: In process, 4: Ended, 5: Canceled.
          tmp_file_id: Temporary audio file: tmp_file_id returned by POST /file/upload-tmp or POST /file/generate-
                speech, `<2 hex>/<32 hex>/<file name>`. Used by a call mailing.

        Error codes (``error_message``): REQUEST_VALIDATION_EXCEPTION, MAILING_NOT_FOUND,
        PARSING_DATE_TIME_EXCEPTION, MAILING_MANAGEMENT_INVALID_STATUS_FOR_UPDATE,
        MAILING_MANAGEMENT_INVALID_STATUS_FOR_CANCEL, MAILING_MANAGEMENT_INVALID_STATUS_FOR_SOFT_DELETE,
        MAILING_MANAGEMENT_DONGLE_TARIFF_INVALID, MAILING_MANAGEMENT_INVALID_PHONE,
        MAILING_MANAGEMENT_NO_RECIPIENTS, MAILING_MANAGEMENT_CONTACT_NOT_FOUND,
        MAILING_MANAGEMENT_CONTACT_GROUP_NOT_FOUND, MAILING_MANAGEMENT_DONGLE_SMS_LIMIT_EXCEEDED,
        TMP_FILE_NOT_FOUND.
        """
        data = self._client._request(
            "PUT",
            f"/mailing/{path_param(mailing_id)}",
            body={
                "name": name,
                "text": text,
                "mailing_type_id": mailing_type_id,
                "mailing_status_id": mailing_status_id,
                "scheduled_at": scheduled_at,
                "is_deleted": is_deleted,
                "tmp_file_id": tmp_file_id,
                "mailing_phones": mailing_phones,
                "mailing_contact_ids": mailing_contact_ids,
                "mailing_contact_group_ids": mailing_contact_group_ids,
            },
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return cast(Mailing, construct_type(Mailing, data))

    def delete(
        self,
        mailing_id: int,
        *,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> bool:
        """
        Delete mailing.

        Deletes the mailing.

        Args:
          mailing_id: Identifier in the path

        Error codes (``error_message``): REQUEST_VALIDATION_EXCEPTION, MAILING_NOT_FOUND,
        MAILING_MANAGEMENT_INVALID_STATUS_FOR_HARD_DELETE, DONGLE_NOT_FOUND_EXCEPTION,
        MAILING_MANAGEMENT_DONGLE_TARIFF_INVALID.
        """
        data = self._client._request(
            "DELETE",
            f"/mailing/{path_param(mailing_id)}",
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
        )
        return bool(isinstance(data, dict) and data.get("status"))


class AsyncMailingsResource(AsyncAPIResource):
    """Bulk SMS and call campaigns."""

    async def list(
        self,
        *,
        page: Union[int, NotGiven] = NOT_GIVEN,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        order_by: Union[str, NotGiven] = NOT_GIVEN,
        order: Union[Literal["asc", "desc"], NotGiven] = NOT_GIVEN,
        from_: Union[str, datetime.datetime, NotGiven] = NOT_GIVEN,
        to: Union[str, datetime.datetime, NotGiven] = NOT_GIVEN,
        is_deleted: Union[bool, NotGiven] = NOT_GIVEN,
        created_at_from: Union[str, datetime.datetime, NotGiven] = NOT_GIVEN,
        created_at_to: Union[str, datetime.datetime, NotGiven] = NOT_GIVEN,
        scheduled_at_from: Union[str, datetime.datetime, NotGiven] = NOT_GIVEN,
        scheduled_at_to: Union[str, datetime.datetime, NotGiven] = NOT_GIVEN,
        dongle_ids: Union[Iterable[int], NotGiven] = NOT_GIVEN,
        dongle_name: Union[str, NotGiven] = NOT_GIVEN,
        mailing_status_ids: Union[Iterable[int], NotGiven] = NOT_GIVEN,
        mailing_type_id: Union[int, NotGiven] = NOT_GIVEN,
        mailing_entity_type_id: Union[int, NotGiven] = NOT_GIVEN,
        mailing_entity_type_ids: Union[Iterable[int], NotGiven] = NOT_GIVEN,
        mailing_history_id: Union[int, NotGiven] = NOT_GIVEN,
        mailing_history_ids: Union[Iterable[int], NotGiven] = NOT_GIVEN,
        name: Union[str, NotGiven] = NOT_GIVEN,
        text: Union[str, NotGiven] = NOT_GIVEN,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> AsyncPage[Mailing]:
        """
        List mailings.

        Mailings (bulk SMS or call campaigns) of the account. Newest first by default (created_at descending,
        then the id descending).

        Args:
          page: Page number, 0-based.
          limit: Number of items per page, 1 to 1000.
          order_by: Attribute to sort by, sent together with order. One of: mailingId, name, scheduledAt,
                createdAt, updatedAt.
          order: Sort direction, sent together with order_by. Without order_by and order the list is newest first:
                created_at descending, then the id descending.
          from_: Alias of created_at_from. `YYYY-MM-DD HH:MM:SS` in UTC or an RFC 3339 date-time with an offset
                (`2020-01-01T00:00:00Z`, `2020-01-01T03:00:00+03:00`, fractional seconds allowed); any
                other value answers 400 PARSING_DATE_TIME_EXCEPTION.
          to: Alias of created_at_to. `YYYY-MM-DD HH:MM:SS` in UTC or an RFC 3339 date-time with an offset
                (`2020-01-01T00:00:00Z`, `2020-01-01T03:00:00+03:00`, fractional seconds allowed); any
                other value answers 400 PARSING_DATE_TIME_EXCEPTION.
          is_deleted: Filter by deletion state. Omitted -> all (legacy default); true -> only deleted; false ->
                only alive.
          created_at_from: Mailings created at or after this moment. `YYYY-MM-DD HH:MM:SS` in UTC or an RFC 3339
                date-time with an offset (`2020-01-01T00:00:00Z`, `2020-01-01T03:00:00+03:00`, fractional
                seconds allowed); any other value answers 400 PARSING_DATE_TIME_EXCEPTION.
          created_at_to: Mailings created at or before this moment. `YYYY-MM-DD HH:MM:SS` in UTC or an RFC 3339
                date-time with an offset (`2020-01-01T00:00:00Z`, `2020-01-01T03:00:00+03:00`, fractional
                seconds allowed); any other value answers 400 PARSING_DATE_TIME_EXCEPTION.
          scheduled_at_from: Mailings scheduled at or after this moment. `YYYY-MM-DD HH:MM:SS` in UTC or an RFC
                3339 date-time with an offset (`2020-01-01T00:00:00Z`, `2020-01-01T03:00:00+03:00`,
                fractional seconds allowed); any other value answers 400 PARSING_DATE_TIME_EXCEPTION.
          scheduled_at_to: Mailings scheduled at or before this moment. `YYYY-MM-DD HH:MM:SS` in UTC or an RFC
                3339 date-time with an offset (`2020-01-01T00:00:00Z`, `2020-01-01T03:00:00+03:00`,
                fractional seconds allowed); any other value answers 400 PARSING_DATE_TIME_EXCEPTION.
          dongle_ids: Filter by dongle ids.
          dongle_name: Filter by dongle name (substring).
          mailing_status_ids: Filter by mailing status ids.
          mailing_type_id: Filter by mailing type id.
          mailing_entity_type_id: Filter by mailing entity type id.
          mailing_entity_type_ids: Filter by mailing entity type ids.
          mailing_history_id: Filter by mailing history id.
          mailing_history_ids: Filter by mailing history ids.
          name: Filter by mailing name (substring).
          text: Filter by mailing text (substring).

        Error codes (``error_message``): REQUEST_VALIDATION_EXCEPTION, PARSING_DATE_TIME_EXCEPTION.
        """
        return await self._client._get_page(
            "/mailing",
            query={
                "page": page,
                "limit": limit,
                "order_by": order_by,
                "order": order,
                "from": from_,
                "to": to,
                "is_deleted": is_deleted,
                "created_at_from": created_at_from,
                "created_at_to": created_at_to,
                "scheduled_at_from": scheduled_at_from,
                "scheduled_at_to": scheduled_at_to,
                "dongle_ids[]": dongle_ids,
                "dongle_name": dongle_name,
                "mailing_status_ids[]": mailing_status_ids,
                "mailing_type_id": mailing_type_id,
                "mailing_entity_type_id": mailing_entity_type_id,
                "mailing_entity_type_ids[]": mailing_entity_type_ids,
                "mailing_history_id": mailing_history_id,
                "mailing_history_ids[]": mailing_history_ids,
                "name": name,
                "text": text,
            },
            item_key="mailings",
            item_type=Mailing,
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
        )

    async def create(
        self,
        *,
        name: str,
        mailing_type_id: int,
        mailing_entity_type_id: int,
        dongle_id: int,
        text: Union[str, NotGiven] = NOT_GIVEN,
        scheduled_at: Union[str, datetime.datetime, None, NotGiven] = NOT_GIVEN,
        mailing_status_id: Union[int, None, NotGiven] = NOT_GIVEN,
        is_call_record: Union[bool, NotGiven] = NOT_GIVEN,
        tmp_file_id: Union[str, None, NotGiven] = NOT_GIVEN,
        mailing_phones: Union[Iterable[str], NotGiven] = NOT_GIVEN,
        mailing_contact_ids: Union[Iterable[int], NotGiven] = NOT_GIVEN,
        mailing_contact_group_ids: Union[Iterable[int], NotGiven] = NOT_GIVEN,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> Mailing:
        """
        Create mailing.

        Creates an SMS or call mailing. Use POST /mailing/sms or POST /mailing/call instead.

        Args:
          tmp_file_id: Temporary audio file: tmp_file_id returned by POST /file/upload-tmp or POST /file/generate-
                speech, `<2 hex>/<32 hex>/<file name>`. Used by a call mailing.

        Error codes (``error_message``): REQUEST_VALIDATION_EXCEPTION, DONGLE_NOT_FOUND_EXCEPTION,
        PARSING_DATE_TIME_EXCEPTION, MAILING_MANAGEMENT_INVALID_STATUS_FOR_CREATE,
        MAILING_MANAGEMENT_INVALID_SCHEDULED_AT, MAILING_MANAGEMENT_DONGLE_TARIFF_INVALID,
        MAILING_MANAGEMENT_INVALID_PHONE, MAILING_MANAGEMENT_NO_RECIPIENTS,
        MAILING_MANAGEMENT_CONTACT_NOT_FOUND, MAILING_MANAGEMENT_CONTACT_GROUP_NOT_FOUND,
        MAILING_MANAGEMENT_DONGLE_SMS_LIMIT_EXCEEDED, TMP_FILE_NOT_FOUND.
        """
        data = await self._client._request(
            "POST",
            "/mailing",
            body={
                "name": name,
                "text": text,
                "mailing_type_id": mailing_type_id,
                "mailing_entity_type_id": mailing_entity_type_id,
                "dongle_id": dongle_id,
                "scheduled_at": scheduled_at,
                "mailing_status_id": mailing_status_id,
                "is_call_record": is_call_record,
                "tmp_file_id": tmp_file_id,
                "mailing_phones": mailing_phones,
                "mailing_contact_ids": mailing_contact_ids,
                "mailing_contact_group_ids": mailing_contact_group_ids,
            },
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return cast(Mailing, construct_type(Mailing, data))

    async def create_sms(
        self,
        *,
        name: str,
        text: str,
        mailing_type_id: int,
        dongle_id: int,
        scheduled_at: Union[str, datetime.datetime, None, NotGiven] = NOT_GIVEN,
        mailing_status_id: Union[int, None, NotGiven] = NOT_GIVEN,
        mailing_phones: Union[Iterable[str], NotGiven] = NOT_GIVEN,
        mailing_contact_ids: Union[Iterable[int], NotGiven] = NOT_GIVEN,
        mailing_contact_group_ids: Union[Iterable[int], NotGiven] = NOT_GIVEN,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> Mailing:
        """
        Create SMS mailing.

        Creates an SMS mailing to the listed phones, contacts and contact groups, sent now or at scheduled_at.

        Error codes (``error_message``): REQUEST_VALIDATION_EXCEPTION, DONGLE_NOT_FOUND_EXCEPTION,
        PARSING_DATE_TIME_EXCEPTION, MAILING_MANAGEMENT_INVALID_STATUS_FOR_CREATE,
        MAILING_MANAGEMENT_INVALID_SCHEDULED_AT, MAILING_MANAGEMENT_DONGLE_TARIFF_INVALID,
        MAILING_MANAGEMENT_INVALID_PHONE, MAILING_MANAGEMENT_NO_RECIPIENTS,
        MAILING_MANAGEMENT_CONTACT_NOT_FOUND, MAILING_MANAGEMENT_CONTACT_GROUP_NOT_FOUND,
        MAILING_MANAGEMENT_DONGLE_SMS_LIMIT_EXCEEDED.
        """
        data = await self._client._request(
            "POST",
            "/mailing/sms",
            body={
                "name": name,
                "text": text,
                "mailing_type_id": mailing_type_id,
                "dongle_id": dongle_id,
                "scheduled_at": scheduled_at,
                "mailing_status_id": mailing_status_id,
                "mailing_phones": mailing_phones,
                "mailing_contact_ids": mailing_contact_ids,
                "mailing_contact_group_ids": mailing_contact_group_ids,
            },
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return cast(Mailing, construct_type(Mailing, data))

    async def create_call(
        self,
        *,
        name: str,
        mailing_type_id: int,
        dongle_id: int,
        text: Union[str, None, NotGiven] = NOT_GIVEN,
        is_call_record: Union[bool, NotGiven] = NOT_GIVEN,
        tmp_file_id: Union[str, None, NotGiven] = NOT_GIVEN,
        scheduled_at: Union[str, datetime.datetime, None, NotGiven] = NOT_GIVEN,
        mailing_status_id: Union[int, None, NotGiven] = NOT_GIVEN,
        mailing_phones: Union[Iterable[str], NotGiven] = NOT_GIVEN,
        mailing_contact_ids: Union[Iterable[int], NotGiven] = NOT_GIVEN,
        mailing_contact_group_ids: Union[Iterable[int], NotGiven] = NOT_GIVEN,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> Mailing:
        """
        Create call mailing.

        Creates a call mailing that plays an audio file (tmp_file_id) to the listed phones, contacts and
        contact groups.

        Args:
          tmp_file_id: Temporary audio file: tmp_file_id returned by POST /file/upload-tmp or POST /file/generate-
                speech, `<2 hex>/<32 hex>/<file name>`. Used by a call mailing.

        Error codes (``error_message``): REQUEST_VALIDATION_EXCEPTION, DONGLE_NOT_FOUND_EXCEPTION,
        PARSING_DATE_TIME_EXCEPTION, MAILING_MANAGEMENT_INVALID_STATUS_FOR_CREATE,
        MAILING_MANAGEMENT_INVALID_SCHEDULED_AT, MAILING_MANAGEMENT_DONGLE_TARIFF_INVALID,
        MAILING_MANAGEMENT_INVALID_PHONE, MAILING_MANAGEMENT_NO_RECIPIENTS,
        MAILING_MANAGEMENT_CONTACT_NOT_FOUND, MAILING_MANAGEMENT_CONTACT_GROUP_NOT_FOUND, TMP_FILE_NOT_FOUND.
        """
        data = await self._client._request(
            "POST",
            "/mailing/call",
            body={
                "name": name,
                "text": text,
                "mailing_type_id": mailing_type_id,
                "dongle_id": dongle_id,
                "is_call_record": is_call_record,
                "tmp_file_id": tmp_file_id,
                "scheduled_at": scheduled_at,
                "mailing_status_id": mailing_status_id,
                "mailing_phones": mailing_phones,
                "mailing_contact_ids": mailing_contact_ids,
                "mailing_contact_group_ids": mailing_contact_group_ids,
            },
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return cast(Mailing, construct_type(Mailing, data))

    async def get(
        self,
        mailing_id: int,
        *,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> Mailing:
        """
        Get mailing.

        One mailing of the account with its recipients and its last run.

        Args:
          mailing_id: Identifier in the path

        Error codes (``error_message``): REQUEST_VALIDATION_EXCEPTION, MAILING_NOT_FOUND.
        """
        data = await self._client._request(
            "GET",
            f"/mailing/{path_param(mailing_id)}",
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
        )
        return cast(Mailing, construct_type(Mailing, data))

    async def update(
        self,
        mailing_id: int,
        *,
        name: Union[str, None, NotGiven] = NOT_GIVEN,
        text: Union[str, None, NotGiven] = NOT_GIVEN,
        mailing_type_id: Union[int, None, NotGiven] = NOT_GIVEN,
        mailing_status_id: Union[int, None, NotGiven] = NOT_GIVEN,
        scheduled_at: Union[str, datetime.datetime, None, NotGiven] = NOT_GIVEN,
        is_deleted: Union[bool, None, NotGiven] = NOT_GIVEN,
        tmp_file_id: Union[str, None, NotGiven] = NOT_GIVEN,
        mailing_phones: Union[Iterable[str], NotGiven] = NOT_GIVEN,
        mailing_contact_ids: Union[Iterable[int], NotGiven] = NOT_GIVEN,
        mailing_contact_group_ids: Union[Iterable[int], NotGiven] = NOT_GIVEN,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> Mailing:
        """
        Update mailing.

        Changes the mailing; omitted fields keep their values.

        Args:
          mailing_id: Identifier in the path
          mailing_type_id: 1: Simple (sent at once), 2: Delayed (sent at scheduled_at).
          mailing_status_id: 1: Draft, 2: Planned, 3: In process, 4: Ended, 5: Canceled.
          tmp_file_id: Temporary audio file: tmp_file_id returned by POST /file/upload-tmp or POST /file/generate-
                speech, `<2 hex>/<32 hex>/<file name>`. Used by a call mailing.

        Error codes (``error_message``): REQUEST_VALIDATION_EXCEPTION, MAILING_NOT_FOUND,
        PARSING_DATE_TIME_EXCEPTION, MAILING_MANAGEMENT_INVALID_STATUS_FOR_UPDATE,
        MAILING_MANAGEMENT_INVALID_STATUS_FOR_CANCEL, MAILING_MANAGEMENT_INVALID_STATUS_FOR_SOFT_DELETE,
        MAILING_MANAGEMENT_DONGLE_TARIFF_INVALID, MAILING_MANAGEMENT_INVALID_PHONE,
        MAILING_MANAGEMENT_NO_RECIPIENTS, MAILING_MANAGEMENT_CONTACT_NOT_FOUND,
        MAILING_MANAGEMENT_CONTACT_GROUP_NOT_FOUND, MAILING_MANAGEMENT_DONGLE_SMS_LIMIT_EXCEEDED,
        TMP_FILE_NOT_FOUND.
        """
        data = await self._client._request(
            "PUT",
            f"/mailing/{path_param(mailing_id)}",
            body={
                "name": name,
                "text": text,
                "mailing_type_id": mailing_type_id,
                "mailing_status_id": mailing_status_id,
                "scheduled_at": scheduled_at,
                "is_deleted": is_deleted,
                "tmp_file_id": tmp_file_id,
                "mailing_phones": mailing_phones,
                "mailing_contact_ids": mailing_contact_ids,
                "mailing_contact_group_ids": mailing_contact_group_ids,
            },
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return cast(Mailing, construct_type(Mailing, data))

    async def delete(
        self,
        mailing_id: int,
        *,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> bool:
        """
        Delete mailing.

        Deletes the mailing.

        Args:
          mailing_id: Identifier in the path

        Error codes (``error_message``): REQUEST_VALIDATION_EXCEPTION, MAILING_NOT_FOUND,
        MAILING_MANAGEMENT_INVALID_STATUS_FOR_HARD_DELETE, DONGLE_NOT_FOUND_EXCEPTION,
        MAILING_MANAGEMENT_DONGLE_TARIFF_INVALID.
        """
        data = await self._client._request(
            "DELETE",
            f"/mailing/{path_param(mailing_id)}",
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
        )
        return bool(isinstance(data, dict) and data.get("status"))
