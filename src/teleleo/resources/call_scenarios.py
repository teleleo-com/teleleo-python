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
from ..types import CallScenario

__all__ = ["CallScenariosResource", "AsyncCallScenariosResource"]


class CallScenariosResource(SyncAPIResource):
    """What a modem plays to incoming callers."""

    def list(
        self,
        *,
        dongle_ids: Union[Iterable[int], NotGiven] = NOT_GIVEN,
        name: Union[str, NotGiven] = NOT_GIVEN,
        dongle_name: Union[str, NotGiven] = NOT_GIVEN,
        dongle_phone: Union[str, NotGiven] = NOT_GIVEN,
        from_: Union[str, datetime.datetime, NotGiven] = NOT_GIVEN,
        to: Union[str, datetime.datetime, NotGiven] = NOT_GIVEN,
        is_empty_file_id: Union[bool, NotGiven] = NOT_GIVEN,
        page: Union[int, NotGiven] = NOT_GIVEN,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        order_by: Union[str, NotGiven] = NOT_GIVEN,
        order: Union[Literal["asc", "desc"], NotGiven] = NOT_GIVEN,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> SyncPage[CallScenario]:
        """
        List call scenarios.

        Call scenarios of the account: what a modem plays to incoming callers. Newest first by default
        (created_at descending, then the id descending).

        Args:
          dongle_ids: Array of integers representing dongle IDs
          name: Filter by a fragment of the name, case-insensitive.
          dongle_name: Filter by a fragment of the dongle name, case-insensitive.
          dongle_phone: Filter by a fragment of the dongle phone number, case-insensitive.
          from_: Scenarios created at or after this moment. `YYYY-MM-DD HH:MM:SS` in UTC or an RFC 3339 date-time
                with an offset (`2020-01-01T00:00:00Z`, `2020-01-01T03:00:00+03:00`, fractional seconds
                allowed); any other value answers 400 PARSING_DATE_TIME_EXCEPTION.
          to: Scenarios created before this moment. `YYYY-MM-DD HH:MM:SS` in UTC or an RFC 3339 date-time with an
                offset (`2020-01-01T00:00:00Z`, `2020-01-01T03:00:00+03:00`, fractional seconds allowed);
                any other value answers 400 PARSING_DATE_TIME_EXCEPTION.
          is_empty_file_id: true - only scenarios without an audio file, false - only scenarios with one.
          page: Page number, 0-based.
          limit: Number of items per page, 1 to 1000.
          order_by: Attribute to sort by, sent together with order. One of: callScenarioId, name,
                callScenarioType, createdAt, updatedAt.
          order: Sort direction, sent together with order_by. Without order_by and order the list is newest first:
                created_at descending, then the id descending.

        Error codes (``error_message``): REQUEST_VALIDATION_EXCEPTION, PARSING_DATE_TIME_EXCEPTION.
        """
        return self._client._get_page(
            "/call-scenario",
            query={
                "dongle_ids[]": dongle_ids,
                "name": name,
                "dongle_name": dongle_name,
                "dongle_phone": dongle_phone,
                "from": from_,
                "to": to,
                "is_empty_file_id": is_empty_file_id,
                "page": page,
                "limit": limit,
                "order_by": order_by,
                "order": order,
            },
            item_key="call_scenarios",
            item_type=CallScenario,
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
        )

    def create(
        self,
        *,
        name: str,
        is_call_record: bool,
        dongle_id: int,
        call_scenario_type_id: int,
        tmp_file_id: str,
        call_scenario_contact_ids: Union[Iterable[int], NotGiven] = NOT_GIVEN,
        call_scenario_phones: Union[Iterable[str], NotGiven] = NOT_GIVEN,
        call_scenario_contact_group_ids: Union[Iterable[int], NotGiven] = NOT_GIVEN,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> CallScenario:
        """
        Create call scenario.

        Creates the call scenario of a modem (one per modem) and pushes it to the modem; follow the delivery
        in call_scenario_apply_status_id.

        Args:
          tmp_file_id: Temporary audio file: tmp_file_id returned by POST /file/upload-tmp or POST /file/generate-
                speech, `<2 hex>/<32 hex>/<file name>`.

        Error codes (``error_message``): REQUEST_VALIDATION_EXCEPTION, DONGLE_NOT_FOUND_EXCEPTION,
        CALL_SCENARIO_MANAGEMENT_DONGLE_HAS_SIP_TYPE_EXCEPTION,
        BILLING_ERROR_IDENTIFIER_DONGLE_SUBSCRIPTION_NOT_ACTIVE,
        CALL_SCENARIO_MANAGEMENT_DONGLE_NOT_SUPPORTED_EXCEPTION,
        CALL_SCENARIO_MANAGEMENT_DONGLE_ALREADY_HAS_ACTIVE_SCENARIO_EXCEPTION, TMP_FILE_NOT_FOUND,
        CALL_SCENARIO_MANAGEMENT_CONTACT_NOT_FOUND_EXCEPTION.
        """
        data = self._client._request(
            "POST",
            "/call-scenario",
            body={
                "name": name,
                "is_call_record": is_call_record,
                "dongle_id": dongle_id,
                "call_scenario_type_id": call_scenario_type_id,
                "tmp_file_id": tmp_file_id,
                "call_scenario_contact_ids": call_scenario_contact_ids,
                "call_scenario_phones": call_scenario_phones,
                "call_scenario_contact_group_ids": call_scenario_contact_group_ids,
            },
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return cast(CallScenario, construct_type(CallScenario, data))

    def get(
        self,
        call_scenario_id: int,
        *,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> CallScenario:
        """
        Get call scenario.

        One call scenario of the account with its delivery state.

        Args:
          call_scenario_id: Call scenario id

        Error codes (``error_message``): REQUEST_VALIDATION_EXCEPTION, CALL_SCENARIO_NOT_FOUND_EXCEPTION.
        """
        data = self._client._request(
            "GET",
            f"/call-scenario/{path_param(call_scenario_id)}",
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
        )
        return cast(CallScenario, construct_type(CallScenario, data))

    def update(
        self,
        call_scenario_id: int,
        *,
        name: Union[str, NotGiven] = NOT_GIVEN,
        is_call_record: Union[bool, NotGiven] = NOT_GIVEN,
        call_scenario_type_id: Union[int, NotGiven] = NOT_GIVEN,
        tmp_file_id: Union[str, NotGiven] = NOT_GIVEN,
        call_scenario_contact_ids: Union[Iterable[int], NotGiven] = NOT_GIVEN,
        call_scenario_phones: Union[Iterable[str], NotGiven] = NOT_GIVEN,
        call_scenario_contact_group_ids: Union[Iterable[int], NotGiven] = NOT_GIVEN,
        version_uuid: Union[str, NotGiven] = NOT_GIVEN,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> CallScenario:
        """
        Update call scenario.

        Changes the call scenario and pushes the new version to the modem. Send version_uuid of the version
        you read to avoid overwriting a newer one (409).

        Args:
          call_scenario_id: Call scenario id
          tmp_file_id: Temporary audio file: tmp_file_id returned by POST /file/upload-tmp or POST /file/generate-
                speech, `<2 hex>/<32 hex>/<file name>`.
          version_uuid: Version of the scenario the client edited; a different current version answers 409

        Error codes (``error_message``): REQUEST_VALIDATION_EXCEPTION, CALL_SCENARIO_NOT_FOUND_EXCEPTION,
        CALL_SCENARIO_MANAGEMENT_DONGLE_HAS_SIP_TYPE_EXCEPTION,
        BILLING_ERROR_IDENTIFIER_DONGLE_SUBSCRIPTION_NOT_ACTIVE,
        CALL_SCENARIO_MANAGEMENT_DONGLE_NOT_SUPPORTED_EXCEPTION,
        CALL_SCENARIO_MANAGEMENT_VERSION_CONFLICT_EXCEPTION, TMP_FILE_NOT_FOUND,
        CALL_SCENARIO_MANAGEMENT_CONTACT_NOT_FOUND_EXCEPTION,
        CALL_SCENARIO_MANAGEMENT_DONGLE_ALREADY_HAS_ACTIVE_SCENARIO_EXCEPTION.
        """
        data = self._client._request(
            "PUT",
            f"/call-scenario/{path_param(call_scenario_id)}",
            body={
                "name": name,
                "is_call_record": is_call_record,
                "call_scenario_type_id": call_scenario_type_id,
                "tmp_file_id": tmp_file_id,
                "call_scenario_contact_ids": call_scenario_contact_ids,
                "call_scenario_phones": call_scenario_phones,
                "call_scenario_contact_group_ids": call_scenario_contact_group_ids,
                "version_uuid": version_uuid,
            },
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return cast(CallScenario, construct_type(CallScenario, data))

    def delete(
        self,
        call_scenario_id: int,
        *,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> bool:
        """
        Delete call scenario.

        Deletes the call scenario and removes it from the modem.

        Args:
          call_scenario_id: Identifier in the path

        Error codes (``error_message``): REQUEST_VALIDATION_EXCEPTION, CALL_SCENARIO_NOT_FOUND_EXCEPTION,
        CALL_SCENARIO_MANAGEMENT_DONGLE_UNAVAILABLE_EXCEPTION,
        CALL_SCENARIO_MANAGEMENT_VERSION_CONFLICT_EXCEPTION.
        """
        data = self._client._request(
            "DELETE",
            f"/call-scenario/{path_param(call_scenario_id)}",
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
        )
        return bool(isinstance(data, dict) and data.get("status"))

    def retry(
        self,
        call_scenario_id: int,
        *,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> CallScenario:
        """
        Retry call scenario delivery.

        Re-sends the scenario to the modem after a delivery error (call_scenario_apply_status_id /
        call_scenario_delivery_error_id).

        Args:
          call_scenario_id: Call scenario id

        Error codes (``error_message``): REQUEST_VALIDATION_EXCEPTION, CALL_SCENARIO_NOT_FOUND_EXCEPTION,
        CALL_SCENARIO_MANAGEMENT_DONGLE_HAS_SIP_TYPE_EXCEPTION,
        BILLING_ERROR_IDENTIFIER_DONGLE_SUBSCRIPTION_NOT_ACTIVE,
        CALL_SCENARIO_MANAGEMENT_DONGLE_NOT_SUPPORTED_EXCEPTION.
        """
        data = self._client._request(
            "POST",
            f"/call-scenario/{path_param(call_scenario_id)}/retry",
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
        )
        return cast(CallScenario, construct_type(CallScenario, data))


class AsyncCallScenariosResource(AsyncAPIResource):
    """What a modem plays to incoming callers."""

    async def list(
        self,
        *,
        dongle_ids: Union[Iterable[int], NotGiven] = NOT_GIVEN,
        name: Union[str, NotGiven] = NOT_GIVEN,
        dongle_name: Union[str, NotGiven] = NOT_GIVEN,
        dongle_phone: Union[str, NotGiven] = NOT_GIVEN,
        from_: Union[str, datetime.datetime, NotGiven] = NOT_GIVEN,
        to: Union[str, datetime.datetime, NotGiven] = NOT_GIVEN,
        is_empty_file_id: Union[bool, NotGiven] = NOT_GIVEN,
        page: Union[int, NotGiven] = NOT_GIVEN,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        order_by: Union[str, NotGiven] = NOT_GIVEN,
        order: Union[Literal["asc", "desc"], NotGiven] = NOT_GIVEN,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> AsyncPage[CallScenario]:
        """
        List call scenarios.

        Call scenarios of the account: what a modem plays to incoming callers. Newest first by default
        (created_at descending, then the id descending).

        Args:
          dongle_ids: Array of integers representing dongle IDs
          name: Filter by a fragment of the name, case-insensitive.
          dongle_name: Filter by a fragment of the dongle name, case-insensitive.
          dongle_phone: Filter by a fragment of the dongle phone number, case-insensitive.
          from_: Scenarios created at or after this moment. `YYYY-MM-DD HH:MM:SS` in UTC or an RFC 3339 date-time
                with an offset (`2020-01-01T00:00:00Z`, `2020-01-01T03:00:00+03:00`, fractional seconds
                allowed); any other value answers 400 PARSING_DATE_TIME_EXCEPTION.
          to: Scenarios created before this moment. `YYYY-MM-DD HH:MM:SS` in UTC or an RFC 3339 date-time with an
                offset (`2020-01-01T00:00:00Z`, `2020-01-01T03:00:00+03:00`, fractional seconds allowed);
                any other value answers 400 PARSING_DATE_TIME_EXCEPTION.
          is_empty_file_id: true - only scenarios without an audio file, false - only scenarios with one.
          page: Page number, 0-based.
          limit: Number of items per page, 1 to 1000.
          order_by: Attribute to sort by, sent together with order. One of: callScenarioId, name,
                callScenarioType, createdAt, updatedAt.
          order: Sort direction, sent together with order_by. Without order_by and order the list is newest first:
                created_at descending, then the id descending.

        Error codes (``error_message``): REQUEST_VALIDATION_EXCEPTION, PARSING_DATE_TIME_EXCEPTION.
        """
        return await self._client._get_page(
            "/call-scenario",
            query={
                "dongle_ids[]": dongle_ids,
                "name": name,
                "dongle_name": dongle_name,
                "dongle_phone": dongle_phone,
                "from": from_,
                "to": to,
                "is_empty_file_id": is_empty_file_id,
                "page": page,
                "limit": limit,
                "order_by": order_by,
                "order": order,
            },
            item_key="call_scenarios",
            item_type=CallScenario,
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
        )

    async def create(
        self,
        *,
        name: str,
        is_call_record: bool,
        dongle_id: int,
        call_scenario_type_id: int,
        tmp_file_id: str,
        call_scenario_contact_ids: Union[Iterable[int], NotGiven] = NOT_GIVEN,
        call_scenario_phones: Union[Iterable[str], NotGiven] = NOT_GIVEN,
        call_scenario_contact_group_ids: Union[Iterable[int], NotGiven] = NOT_GIVEN,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> CallScenario:
        """
        Create call scenario.

        Creates the call scenario of a modem (one per modem) and pushes it to the modem; follow the delivery
        in call_scenario_apply_status_id.

        Args:
          tmp_file_id: Temporary audio file: tmp_file_id returned by POST /file/upload-tmp or POST /file/generate-
                speech, `<2 hex>/<32 hex>/<file name>`.

        Error codes (``error_message``): REQUEST_VALIDATION_EXCEPTION, DONGLE_NOT_FOUND_EXCEPTION,
        CALL_SCENARIO_MANAGEMENT_DONGLE_HAS_SIP_TYPE_EXCEPTION,
        BILLING_ERROR_IDENTIFIER_DONGLE_SUBSCRIPTION_NOT_ACTIVE,
        CALL_SCENARIO_MANAGEMENT_DONGLE_NOT_SUPPORTED_EXCEPTION,
        CALL_SCENARIO_MANAGEMENT_DONGLE_ALREADY_HAS_ACTIVE_SCENARIO_EXCEPTION, TMP_FILE_NOT_FOUND,
        CALL_SCENARIO_MANAGEMENT_CONTACT_NOT_FOUND_EXCEPTION.
        """
        data = await self._client._request(
            "POST",
            "/call-scenario",
            body={
                "name": name,
                "is_call_record": is_call_record,
                "dongle_id": dongle_id,
                "call_scenario_type_id": call_scenario_type_id,
                "tmp_file_id": tmp_file_id,
                "call_scenario_contact_ids": call_scenario_contact_ids,
                "call_scenario_phones": call_scenario_phones,
                "call_scenario_contact_group_ids": call_scenario_contact_group_ids,
            },
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return cast(CallScenario, construct_type(CallScenario, data))

    async def get(
        self,
        call_scenario_id: int,
        *,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> CallScenario:
        """
        Get call scenario.

        One call scenario of the account with its delivery state.

        Args:
          call_scenario_id: Call scenario id

        Error codes (``error_message``): REQUEST_VALIDATION_EXCEPTION, CALL_SCENARIO_NOT_FOUND_EXCEPTION.
        """
        data = await self._client._request(
            "GET",
            f"/call-scenario/{path_param(call_scenario_id)}",
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
        )
        return cast(CallScenario, construct_type(CallScenario, data))

    async def update(
        self,
        call_scenario_id: int,
        *,
        name: Union[str, NotGiven] = NOT_GIVEN,
        is_call_record: Union[bool, NotGiven] = NOT_GIVEN,
        call_scenario_type_id: Union[int, NotGiven] = NOT_GIVEN,
        tmp_file_id: Union[str, NotGiven] = NOT_GIVEN,
        call_scenario_contact_ids: Union[Iterable[int], NotGiven] = NOT_GIVEN,
        call_scenario_phones: Union[Iterable[str], NotGiven] = NOT_GIVEN,
        call_scenario_contact_group_ids: Union[Iterable[int], NotGiven] = NOT_GIVEN,
        version_uuid: Union[str, NotGiven] = NOT_GIVEN,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> CallScenario:
        """
        Update call scenario.

        Changes the call scenario and pushes the new version to the modem. Send version_uuid of the version
        you read to avoid overwriting a newer one (409).

        Args:
          call_scenario_id: Call scenario id
          tmp_file_id: Temporary audio file: tmp_file_id returned by POST /file/upload-tmp or POST /file/generate-
                speech, `<2 hex>/<32 hex>/<file name>`.
          version_uuid: Version of the scenario the client edited; a different current version answers 409

        Error codes (``error_message``): REQUEST_VALIDATION_EXCEPTION, CALL_SCENARIO_NOT_FOUND_EXCEPTION,
        CALL_SCENARIO_MANAGEMENT_DONGLE_HAS_SIP_TYPE_EXCEPTION,
        BILLING_ERROR_IDENTIFIER_DONGLE_SUBSCRIPTION_NOT_ACTIVE,
        CALL_SCENARIO_MANAGEMENT_DONGLE_NOT_SUPPORTED_EXCEPTION,
        CALL_SCENARIO_MANAGEMENT_VERSION_CONFLICT_EXCEPTION, TMP_FILE_NOT_FOUND,
        CALL_SCENARIO_MANAGEMENT_CONTACT_NOT_FOUND_EXCEPTION,
        CALL_SCENARIO_MANAGEMENT_DONGLE_ALREADY_HAS_ACTIVE_SCENARIO_EXCEPTION.
        """
        data = await self._client._request(
            "PUT",
            f"/call-scenario/{path_param(call_scenario_id)}",
            body={
                "name": name,
                "is_call_record": is_call_record,
                "call_scenario_type_id": call_scenario_type_id,
                "tmp_file_id": tmp_file_id,
                "call_scenario_contact_ids": call_scenario_contact_ids,
                "call_scenario_phones": call_scenario_phones,
                "call_scenario_contact_group_ids": call_scenario_contact_group_ids,
                "version_uuid": version_uuid,
            },
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return cast(CallScenario, construct_type(CallScenario, data))

    async def delete(
        self,
        call_scenario_id: int,
        *,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> bool:
        """
        Delete call scenario.

        Deletes the call scenario and removes it from the modem.

        Args:
          call_scenario_id: Identifier in the path

        Error codes (``error_message``): REQUEST_VALIDATION_EXCEPTION, CALL_SCENARIO_NOT_FOUND_EXCEPTION,
        CALL_SCENARIO_MANAGEMENT_DONGLE_UNAVAILABLE_EXCEPTION,
        CALL_SCENARIO_MANAGEMENT_VERSION_CONFLICT_EXCEPTION.
        """
        data = await self._client._request(
            "DELETE",
            f"/call-scenario/{path_param(call_scenario_id)}",
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
        )
        return bool(isinstance(data, dict) and data.get("status"))

    async def retry(
        self,
        call_scenario_id: int,
        *,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> CallScenario:
        """
        Retry call scenario delivery.

        Re-sends the scenario to the modem after a delivery error (call_scenario_apply_status_id /
        call_scenario_delivery_error_id).

        Args:
          call_scenario_id: Call scenario id

        Error codes (``error_message``): REQUEST_VALIDATION_EXCEPTION, CALL_SCENARIO_NOT_FOUND_EXCEPTION,
        CALL_SCENARIO_MANAGEMENT_DONGLE_HAS_SIP_TYPE_EXCEPTION,
        BILLING_ERROR_IDENTIFIER_DONGLE_SUBSCRIPTION_NOT_ACTIVE,
        CALL_SCENARIO_MANAGEMENT_DONGLE_NOT_SUPPORTED_EXCEPTION.
        """
        data = await self._client._request(
            "POST",
            f"/call-scenario/{path_param(call_scenario_id)}/retry",
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
        )
        return cast(CallScenario, construct_type(CallScenario, data))
