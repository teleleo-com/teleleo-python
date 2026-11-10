# File generated from spec/openapi.yaml by scripts/generate.py. Do not edit by hand.

from __future__ import annotations

from typing import Iterable, Optional, Union, cast

from typing_extensions import Literal

from .._models import construct_type
from .._pagination import AsyncPage, SyncPage
from .._resource import AsyncAPIResource, SyncAPIResource
from .._types import NOT_GIVEN, Body, Headers, NotGiven, Query, Timeout
from .._utils import path_param
from ..types import FollowUpSmsSetting

__all__ = ["FollowUpSmsSettingsResource", "AsyncFollowUpSmsSettingsResource"]


class FollowUpSmsSettingsResource(SyncAPIResource):
    """SMS a modem sends to a caller after a call."""

    def list(
        self,
        *,
        dongle_ids: Union[Iterable[int], NotGiven] = NOT_GIVEN,
        page: Union[int, NotGiven] = NOT_GIVEN,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        order_by: Union[str, NotGiven] = NOT_GIVEN,
        order: Union[Literal["asc", "desc"], NotGiven] = NOT_GIVEN,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> SyncPage[FollowUpSmsSetting]:
        """
        List follow-up SMS settings.

        Follow-up SMS settings of the account: the SMS a modem sends to a caller after a call. Newest first by
        default (the id descending).

        Args:
          dongle_ids: Array of dongle IDs
          page: Page number, 0-based.
          limit: Number of items per page, 1 to 1000.
          order_by: Attribute to sort by, sent together with order. One of: followUpSmsSettingId, dongleId, name.
          order: Sort direction, sent together with order_by. Without order_by and order the list is newest first:
                the id descending.

        Error codes (``error_message``): REQUEST_VALIDATION_EXCEPTION.
        """
        return self._client._get_page(
            "/follow-up-sms-setting",
            query={"dongle_ids[]": dongle_ids, "page": page, "limit": limit, "order_by": order_by, "order": order},
            item_key="follow_up_sms_settings",
            item_type=FollowUpSmsSetting,
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
        )

    def create(
        self,
        *,
        dongle_id: int,
        name: str,
        text: str,
        ringing_duration_timeout: Union[int, None, NotGiven] = NOT_GIVEN,
        call_duration_timeout: Union[int, None, NotGiven] = NOT_GIVEN,
        daily_sms_limit: Union[int, None, NotGiven] = NOT_GIVEN,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> FollowUpSmsSetting:
        """
        Create follow-up SMS setting.

        Creates a follow-up SMS setting for a modem.

        Error codes (``error_message``): REQUEST_VALIDATION_EXCEPTION, DONGLE_NOT_FOUND_EXCEPTION,
        INVALID_DONGLE_TYPE, BILLING_ERROR_IDENTIFIER_DONGLE_SUBSCRIPTION_NOT_ACTIVE,
        INVALID_RINGING_DURATION_TIMEOUT, INVALID_CALL_DURATION_TIMEOUT, INVALID_DAILY_SMS_LIMIT,
        DUPLICATE_DONGLE_FOLLOW_UP_SMS_SETTING.
        """
        data = self._client._request(
            "POST",
            "/follow-up-sms-setting",
            body={
                "dongle_id": dongle_id,
                "name": name,
                "text": text,
                "ringing_duration_timeout": ringing_duration_timeout,
                "call_duration_timeout": call_duration_timeout,
                "daily_sms_limit": daily_sms_limit,
            },
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return cast(FollowUpSmsSetting, construct_type(FollowUpSmsSetting, data))

    def get(
        self,
        follow_up_sms_setting_id: int,
        *,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> FollowUpSmsSetting:
        """
        Get follow-up SMS setting.

        One follow-up SMS setting of the account.

        Args:
          follow_up_sms_setting_id: Follow Up Sms Setting ID

        Error codes (``error_message``): REQUEST_VALIDATION_EXCEPTION,
        FOLLOW_UP_SMS_SETTING_NOT_FOUND_EXCEPTION.
        """
        data = self._client._request(
            "GET",
            f"/follow-up-sms-setting/{path_param(follow_up_sms_setting_id)}",
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
        )
        return cast(FollowUpSmsSetting, construct_type(FollowUpSmsSetting, data))

    def update(
        self,
        follow_up_sms_setting_id: int,
        *,
        dongle_id: int,
        name: str,
        text: str,
        ringing_duration_timeout: Union[int, None, NotGiven] = NOT_GIVEN,
        call_duration_timeout: Union[int, None, NotGiven] = NOT_GIVEN,
        daily_sms_limit: Union[int, None, NotGiven] = NOT_GIVEN,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> FollowUpSmsSetting:
        """
        Update follow-up SMS setting.

        Replaces the follow-up SMS setting.

        Args:
          follow_up_sms_setting_id: Follow-up SMS setting ID

        Error codes (``error_message``): REQUEST_VALIDATION_EXCEPTION,
        FOLLOW_UP_SMS_SETTING_NOT_FOUND_EXCEPTION, DONGLE_NOT_FOUND_EXCEPTION, INVALID_DONGLE_TYPE,
        BILLING_ERROR_IDENTIFIER_DONGLE_SUBSCRIPTION_NOT_ACTIVE, INVALID_RINGING_DURATION_TIMEOUT,
        INVALID_CALL_DURATION_TIMEOUT, INVALID_DAILY_SMS_LIMIT, DUPLICATE_DONGLE_FOLLOW_UP_SMS_SETTING.
        """
        data = self._client._request(
            "PUT",
            f"/follow-up-sms-setting/{path_param(follow_up_sms_setting_id)}",
            body={
                "dongle_id": dongle_id,
                "name": name,
                "text": text,
                "ringing_duration_timeout": ringing_duration_timeout,
                "call_duration_timeout": call_duration_timeout,
                "daily_sms_limit": daily_sms_limit,
            },
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return cast(FollowUpSmsSetting, construct_type(FollowUpSmsSetting, data))

    def delete(
        self,
        follow_up_sms_setting_id: int,
        *,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> bool:
        """
        Delete follow-up SMS setting.

        Deletes the follow-up SMS setting.

        Args:
          follow_up_sms_setting_id: Follow-up SMS setting ID

        Error codes (``error_message``): REQUEST_VALIDATION_EXCEPTION,
        FOLLOW_UP_SMS_SETTING_NOT_FOUND_EXCEPTION, BILLING_ERROR_IDENTIFIER_DONGLE_SUBSCRIPTION_NOT_ACTIVE.
        """
        data = self._client._request(
            "DELETE",
            f"/follow-up-sms-setting/{path_param(follow_up_sms_setting_id)}",
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
        )
        return bool(isinstance(data, dict) and data.get("status"))


class AsyncFollowUpSmsSettingsResource(AsyncAPIResource):
    """SMS a modem sends to a caller after a call."""

    async def list(
        self,
        *,
        dongle_ids: Union[Iterable[int], NotGiven] = NOT_GIVEN,
        page: Union[int, NotGiven] = NOT_GIVEN,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        order_by: Union[str, NotGiven] = NOT_GIVEN,
        order: Union[Literal["asc", "desc"], NotGiven] = NOT_GIVEN,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> AsyncPage[FollowUpSmsSetting]:
        """
        List follow-up SMS settings.

        Follow-up SMS settings of the account: the SMS a modem sends to a caller after a call. Newest first by
        default (the id descending).

        Args:
          dongle_ids: Array of dongle IDs
          page: Page number, 0-based.
          limit: Number of items per page, 1 to 1000.
          order_by: Attribute to sort by, sent together with order. One of: followUpSmsSettingId, dongleId, name.
          order: Sort direction, sent together with order_by. Without order_by and order the list is newest first:
                the id descending.

        Error codes (``error_message``): REQUEST_VALIDATION_EXCEPTION.
        """
        return await self._client._get_page(
            "/follow-up-sms-setting",
            query={"dongle_ids[]": dongle_ids, "page": page, "limit": limit, "order_by": order_by, "order": order},
            item_key="follow_up_sms_settings",
            item_type=FollowUpSmsSetting,
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
        )

    async def create(
        self,
        *,
        dongle_id: int,
        name: str,
        text: str,
        ringing_duration_timeout: Union[int, None, NotGiven] = NOT_GIVEN,
        call_duration_timeout: Union[int, None, NotGiven] = NOT_GIVEN,
        daily_sms_limit: Union[int, None, NotGiven] = NOT_GIVEN,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> FollowUpSmsSetting:
        """
        Create follow-up SMS setting.

        Creates a follow-up SMS setting for a modem.

        Error codes (``error_message``): REQUEST_VALIDATION_EXCEPTION, DONGLE_NOT_FOUND_EXCEPTION,
        INVALID_DONGLE_TYPE, BILLING_ERROR_IDENTIFIER_DONGLE_SUBSCRIPTION_NOT_ACTIVE,
        INVALID_RINGING_DURATION_TIMEOUT, INVALID_CALL_DURATION_TIMEOUT, INVALID_DAILY_SMS_LIMIT,
        DUPLICATE_DONGLE_FOLLOW_UP_SMS_SETTING.
        """
        data = await self._client._request(
            "POST",
            "/follow-up-sms-setting",
            body={
                "dongle_id": dongle_id,
                "name": name,
                "text": text,
                "ringing_duration_timeout": ringing_duration_timeout,
                "call_duration_timeout": call_duration_timeout,
                "daily_sms_limit": daily_sms_limit,
            },
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return cast(FollowUpSmsSetting, construct_type(FollowUpSmsSetting, data))

    async def get(
        self,
        follow_up_sms_setting_id: int,
        *,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> FollowUpSmsSetting:
        """
        Get follow-up SMS setting.

        One follow-up SMS setting of the account.

        Args:
          follow_up_sms_setting_id: Follow Up Sms Setting ID

        Error codes (``error_message``): REQUEST_VALIDATION_EXCEPTION,
        FOLLOW_UP_SMS_SETTING_NOT_FOUND_EXCEPTION.
        """
        data = await self._client._request(
            "GET",
            f"/follow-up-sms-setting/{path_param(follow_up_sms_setting_id)}",
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
        )
        return cast(FollowUpSmsSetting, construct_type(FollowUpSmsSetting, data))

    async def update(
        self,
        follow_up_sms_setting_id: int,
        *,
        dongle_id: int,
        name: str,
        text: str,
        ringing_duration_timeout: Union[int, None, NotGiven] = NOT_GIVEN,
        call_duration_timeout: Union[int, None, NotGiven] = NOT_GIVEN,
        daily_sms_limit: Union[int, None, NotGiven] = NOT_GIVEN,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> FollowUpSmsSetting:
        """
        Update follow-up SMS setting.

        Replaces the follow-up SMS setting.

        Args:
          follow_up_sms_setting_id: Follow-up SMS setting ID

        Error codes (``error_message``): REQUEST_VALIDATION_EXCEPTION,
        FOLLOW_UP_SMS_SETTING_NOT_FOUND_EXCEPTION, DONGLE_NOT_FOUND_EXCEPTION, INVALID_DONGLE_TYPE,
        BILLING_ERROR_IDENTIFIER_DONGLE_SUBSCRIPTION_NOT_ACTIVE, INVALID_RINGING_DURATION_TIMEOUT,
        INVALID_CALL_DURATION_TIMEOUT, INVALID_DAILY_SMS_LIMIT, DUPLICATE_DONGLE_FOLLOW_UP_SMS_SETTING.
        """
        data = await self._client._request(
            "PUT",
            f"/follow-up-sms-setting/{path_param(follow_up_sms_setting_id)}",
            body={
                "dongle_id": dongle_id,
                "name": name,
                "text": text,
                "ringing_duration_timeout": ringing_duration_timeout,
                "call_duration_timeout": call_duration_timeout,
                "daily_sms_limit": daily_sms_limit,
            },
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return cast(FollowUpSmsSetting, construct_type(FollowUpSmsSetting, data))

    async def delete(
        self,
        follow_up_sms_setting_id: int,
        *,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> bool:
        """
        Delete follow-up SMS setting.

        Deletes the follow-up SMS setting.

        Args:
          follow_up_sms_setting_id: Follow-up SMS setting ID

        Error codes (``error_message``): REQUEST_VALIDATION_EXCEPTION,
        FOLLOW_UP_SMS_SETTING_NOT_FOUND_EXCEPTION, BILLING_ERROR_IDENTIFIER_DONGLE_SUBSCRIPTION_NOT_ACTIVE.
        """
        data = await self._client._request(
            "DELETE",
            f"/follow-up-sms-setting/{path_param(follow_up_sms_setting_id)}",
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
        )
        return bool(isinstance(data, dict) and data.get("status"))
