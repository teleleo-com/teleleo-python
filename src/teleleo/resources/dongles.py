# File generated from spec/openapi.yaml by scripts/generate.py. Do not edit by hand.

from __future__ import annotations

import datetime
from typing import Iterable, List, Optional, Union, cast

from typing_extensions import Literal

from .._models import construct_type
from .._pagination import AsyncPage, SyncPage
from .._resource import AsyncAPIResource, SyncAPIResource
from .._types import NOT_GIVEN, Body, Headers, NotGiven, Query, Timeout
from .._utils import path_param
from ..types import Dongle, DongleListItem, DongleNetworkInfo, DongleSimIdentifiers, DongleStatistic

__all__ = ["DonglesResource", "AsyncDonglesResource"]


class DonglesResource(SyncAPIResource):
    """Modems of the account and their commands: reboot, Wi-Fi, Wi-Fi extender, number, network info."""

    def list(
        self,
        *,
        page: Union[int, NotGiven] = NOT_GIVEN,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        dongle_ids: Union[Iterable[int], NotGiven] = NOT_GIVEN,
        order_by: Union[str, NotGiven] = NOT_GIVEN,
        order: Union[Literal["asc", "desc"], NotGiven] = NOT_GIVEN,
        is_active: Union[bool, NotGiven] = NOT_GIVEN,
        is_short: Union[bool, NotGiven] = NOT_GIVEN,
        is_tariff_package_active: Union[bool, NotGiven] = NOT_GIVEN,
        is_tariff_package_enabled: Union[bool, NotGiven] = NOT_GIVEN,
        dongle_call_type_ids: Union[Iterable[int], NotGiven] = NOT_GIVEN,
        name: Union[str, NotGiven] = NOT_GIVEN,
        number: Union[str, NotGiven] = NOT_GIVEN,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> SyncPage[DongleListItem]:
        """
        List modems.

        Modems of the account. In full mode every field of the Dongle schema that the list serves is returned;
        dongle_setting and public_vpn_server are present in full mode only. The cheapest call is GET
        /dongle?is_short=1&limit=1: use it to check that an API key works. Newest first by default (created_at
        descending, then the id descending).

        Args:
          page: Page number, 0-based.
          limit: Number of items per page, 1 to 1000.
          dongle_ids: Array of integers representing dongle IDs
          order_by: Attribute to sort by, sent together with order. One of: dongleId, name, number, createdAt,
                updatedAt, activatedAt, lastOnlineAt, isActive, isTariffPackageActive, tariffPackageEnd,
                recentOutgoingSmsCount, recentOutgoingCallCount.
          order: Sort direction, sent together with order_by. Without order_by and order the list is newest first:
                created_at descending, then the id descending.
          is_active: Filter by dongle active flag
          is_short: Short mode: only dongle_id, name, number, is_trial, is_tariff_package_active,
                dongle_online_status, dongle_online_error_code_id, dongle_call_type_id and
                is_wifi_extender_processing per modem; the cheapest call, also fit to check that the key
                works.
          is_tariff_package_active: Filter by an active subscription.
          is_tariff_package_enabled: Filter by an enabled subscription.
          dongle_call_type_ids: Filter by how incoming calls are handled: 1 - SIP, 2 - call scenario
          name: Filter by a fragment of the name, case-insensitive.
          number: Filter by a fragment of the phone number.

        Error codes (``error_message``): REQUEST_VALIDATION_EXCEPTION.
        """
        return self._client._get_page(
            "/dongle",
            query={
                "page": page,
                "limit": limit,
                "dongle_ids[]": dongle_ids,
                "order_by": order_by,
                "order": order,
                "is_active": is_active,
                "is_short": is_short,
                "is_tariff_package_active": is_tariff_package_active,
                "is_tariff_package_enabled": is_tariff_package_enabled,
                "dongle_call_type_ids[]": dongle_call_type_ids,
                "name": name,
                "number": number,
            },
            item_key="dongles",
            item_type=DongleListItem,
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
        )

    def reboot(
        self,
        dongle_id: int,
        *,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> bool:
        """
        Reboot modem.

        200 means the reboot is accepted, not done: dongle_online_status becomes 7 (REBOOTING) at once and
        goes back to an online or offline status when the modem returns. A repeated call while a reboot is in
        progress (about 180 s for the API stage, then the SMS stage) is a no-op that also answers 200. The
        reboot is accepted regardless of the subscription and of the online state; track progress through
        dongle_online_status in GET /dongle or GET /dongle/{dongle_id}.

        Args:
          dongle_id: Identifier in the path

        Error codes (``error_message``): REQUEST_VALIDATION_EXCEPTION, DONGLE_NOT_FOUND_EXCEPTION.
        """
        data = self._client._request(
            "POST",
            f"/dongle/{path_param(dongle_id)}/reboot",
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
        )
        return bool(isinstance(data, dict) and data.get("status"))

    def enable_wifi(
        self,
        dongle_id: int,
        *,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> bool:
        """
        Enable modem Wi-Fi.

        Turns the Wi-Fi hotspot of the modem on; the modem must be online. Answers {"status": true} when the
        command is accepted; is_hotspot_enable in GET /dongle/{dongle_id} follows once the modem applied it.

        Args:
          dongle_id: ID of the dongle

        Error codes (``error_message``): REQUEST_VALIDATION_EXCEPTION, DONGLE_NOT_FOUND_EXCEPTION,
        DONGLE_WIFI_ALREADY_IN_THE_SAME_STATUS_EXCEPTION, DONGLE_API_CONNECTION_EXCEPTION,
        DONGLE_API_HTTP_RESPONSE_EXCEPTION.
        """
        data = self._client._request(
            "POST",
            f"/dongle/{path_param(dongle_id)}/wifi/enable",
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
        )
        return bool(isinstance(data, dict) and data.get("status"))

    def disable_wifi(
        self,
        dongle_id: int,
        *,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> bool:
        """
        Disable modem Wi-Fi.

        Turns the Wi-Fi hotspot of the modem off; the modem must be online. Answers {"status": true} when the
        command is accepted.

        Args:
          dongle_id: ID of the dongle

        Error codes (``error_message``): REQUEST_VALIDATION_EXCEPTION, DONGLE_NOT_FOUND_EXCEPTION,
        DONGLE_WIFI_ALREADY_IN_THE_SAME_STATUS_EXCEPTION, DONGLE_API_CONNECTION_EXCEPTION,
        DONGLE_API_HTTP_RESPONSE_EXCEPTION.
        """
        data = self._client._request(
            "POST",
            f"/dongle/{path_param(dongle_id)}/wifi/disable",
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
        )
        return bool(isinstance(data, dict) and data.get("status"))

    def set_wifi_credentials(
        self,
        dongle_id: int,
        *,
        hotspot_name: str,
        hotspot_password: str,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> bool:
        """
        Set modem Wi-Fi credentials.

        Sets the name and the password of the Wi-Fi hotspot of the modem.

        Args:
          dongle_id: ID of the dongle

        Error codes (``error_message``): REQUEST_VALIDATION_EXCEPTION, DONGLE_NOT_FOUND_EXCEPTION,
        DONGLE_WIFI_INVALID_SSID_EXCEPTION, DONGLE_WIFI_INVALID_PASSWORD_EXCEPTION, DONGLE_WIFI_API_EXCEPTION.
        """
        data = self._client._request(
            "POST",
            f"/dongle/{path_param(dongle_id)}/wifi/credentials",
            body={"hotspot_name": hotspot_name, "hotspot_password": hotspot_password},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return bool(isinstance(data, dict) and data.get("status"))

    def enable_wifi_extender(
        self,
        dongle_id: int,
        *,
        ssid: str,
        password: str,
        wifi_extender_mode: int,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> bool:
        """
        Enable Wi-Fi extender.

        Connects the modem to an external Wi-Fi network as a client (extender mode); the modem must be online.
        is_wifi_extender_processing is true in GET /dongle while the modem applies the command.

        Args:
          dongle_id: ID of the dongle
          wifi_extender_mode: 2=ENABLED, 3=ENABLED_COMBINED

        Error codes (``error_message``): REQUEST_VALIDATION_EXCEPTION, DONGLE_NOT_FOUND_EXCEPTION,
        BILLING_ERROR_IDENTIFIER_DONGLE_SUBSCRIPTION_NOT_ACTIVE, DONGLE_WIFI_EXTENDER_LOCKED_EXCEPTION,
        DONGLE_API_CONNECTION_EXCEPTION, DONGLE_API_HTTP_RESPONSE_EXCEPTION.
        """
        data = self._client._request(
            "POST",
            f"/dongle/{path_param(dongle_id)}/wifi-extender/enable",
            body={"ssid": ssid, "password": password, "wifi_extender_mode": wifi_extender_mode},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return bool(isinstance(data, dict) and data.get("status"))

    def disable_wifi_extender(
        self,
        dongle_id: int,
        *,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> bool:
        """
        Disable Wi-Fi extender.

        Disconnects the modem from the external Wi-Fi network; the modem must be online.

        Args:
          dongle_id: ID of the dongle

        Error codes (``error_message``): REQUEST_VALIDATION_EXCEPTION, DONGLE_NOT_FOUND_EXCEPTION,
        DONGLE_WIFI_EXTENDER_LOCKED_EXCEPTION, DONGLE_API_CONNECTION_EXCEPTION,
        DONGLE_API_HTTP_RESPONSE_EXCEPTION.
        """
        data = self._client._request(
            "POST",
            f"/dongle/{path_param(dongle_id)}/wifi-extender/disable",
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
        )
        return bool(isinstance(data, dict) and data.get("status"))

    def scan_wifi_networks(
        self,
        dongle_id: int,
        *,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> bool:
        """
        Scan Wi-Fi networks.

        Asks the modem to scan the Wi-Fi networks around it; the modem must be online.

        Args:
          dongle_id: ID of the dongle

        Error codes (``error_message``): REQUEST_VALIDATION_EXCEPTION, DONGLE_NOT_FOUND_EXCEPTION,
        BILLING_ERROR_IDENTIFIER_DONGLE_SUBSCRIPTION_NOT_ACTIVE, DONGLE_API_CONNECTION_EXCEPTION,
        DONGLE_API_HTTP_RESPONSE_EXCEPTION.
        """
        data = self._client._request(
            "POST",
            f"/dongle/{path_param(dongle_id)}/wifi-extender/networks",
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
        )
        return bool(isinstance(data, dict) and data.get("status"))

    def update_offline_notification(
        self,
        dongle_id: int,
        *,
        is_enabled: bool,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> bool:
        """
        Set offline notification.

        Turns the e-mail to the owner about the modem going offline on or off; shown as
        dongle_setting.is_offline_notification_enabled in GET /dongle.

        Args:
          dongle_id: ID of the dongle
          is_enabled: Enable (true) or disable (false) email when the modem goes offline

        Error codes (``error_message``): REQUEST_VALIDATION_EXCEPTION, DONGLE_NOT_FOUND_EXCEPTION,
        DONGLE_SETTING_NOT_FOUND.
        """
        data = self._client._request(
            "PUT",
            f"/dongle/{path_param(dongle_id)}/setting/offline-notification",
            body={"is_enabled": is_enabled},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return bool(isinstance(data, dict) and data.get("status"))

    def set_number(
        self,
        dongle_id: int,
        *,
        number: str,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> bool:
        """
        Set modem number.

        Accepted asynchronously: the number is verified through the dongle and stored on success; 200 means
        queued.

        Args:
          dongle_id: ID of the dongle
          number: Phone number in international format.

        Error codes (``error_message``): REQUEST_VALIDATION_EXCEPTION, DONGLE_NOT_FOUND_EXCEPTION,
        DONGLE_MANUAL_PHONE_DETERMINATION_NUMBER_EXCEPTION,
        DONGLE_MANUAL_PHONE_DETERMINATION_ALREADY_IN_PROGRESS_EXCEPTION.
        """
        data = self._client._request(
            "PUT",
            f"/dongle/{path_param(dongle_id)}/number",
            body={"number": number},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return bool(isinstance(data, dict) and data.get("status"))

    def get(
        self,
        dongle_id: int,
        *,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> Dongle:
        """
        Get modem.

        One modem of the account with its counters and hardware identity.

        Args:
          dongle_id: Identifier in the path

        Error codes (``error_message``): DONGLE_ERROR_DONGLE_NOT_FOUND.
        """
        data = self._client._request(
            "GET",
            f"/dongle/{path_param(dongle_id)}",
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
        )
        return cast(Dongle, construct_type(Dongle, data))

    def update(
        self,
        dongle_id: int,
        *,
        name: Union[str, NotGiven] = NOT_GIVEN,
        number: Union[str, NotGiven] = NOT_GIVEN,
        is_mute_incoming_call: Union[bool, NotGiven] = NOT_GIVEN,
        dongle_call_type_id: Union[int, NotGiven] = NOT_GIVEN,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> Dongle:
        """
        Update modem.

        Only the listed body fields are read; unknown fields are ignored. An omitted field keeps its value.
        The billing fields tariff_package_id, is_tariff_package_enabled, order_dongle_id, is_deleted and
        is_active and the field imei_fake are outside the public API: a body with any of them is refused as a
        whole with 403 PUBLIC_API_FIELD_FORBIDDEN.

        Args:
          dongle_id: Identifier in the path
          name: Display name of the modem.
          number: Phone number of the SIM in international format. Omit the field to keep the current number: null
                does not clear it.
          is_mute_incoming_call: Reject incoming calls on the modem.
          dongle_call_type_id: How incoming calls are handled: 1 - SIP (softphone), 2 - call scenario.

        Error codes (``error_message``): DONGLE_ERROR_DONGLE_NOT_FOUND, PUBLIC_API_FIELD_FORBIDDEN.
        """
        data = self._client._request(
            "PUT",
            f"/dongle/{path_param(dongle_id)}",
            body={
                "name": name,
                "number": number,
                "is_mute_incoming_call": is_mute_incoming_call,
                "dongle_call_type_id": dongle_call_type_id,
            },
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return cast(Dongle, construct_type(Dongle, data))

    def get_network_info(
        self,
        dongle_id: int,
        *,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> DongleNetworkInfo:
        """
        Get modem network info.

        Asks the online modem for its radio state and returns it in the answer: networks, roaming, network
        type and signal. DONGLE_MANAGEMENT_API_ERROR_IDENTIFIER_HTTP_RESPONSE and
        DONGLE_MANAGEMENT_API_ERROR_IDENTIFIER_INVALID_CONTENT mean the modem did not answer or answered
        malformed data: a temporary state, the request can be repeated.

        Args:
          dongle_id: Identifier in the path

        Error codes (``error_message``): DONGLE_ERROR_DONGLE_NOT_FOUND,
        DONGLE_MANAGEMENT_API_ERROR_IDENTIFIER_HTTP_RESPONSE,
        DONGLE_MANAGEMENT_API_ERROR_IDENTIFIER_INVALID_CONTENT.
        """
        data = self._client._request(
            "POST",
            f"/dongle/{path_param(dongle_id)}/mobile-network-info",
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
        )
        result = data.get("result") if isinstance(data, dict) else data
        return cast(DongleNetworkInfo, construct_type(DongleNetworkInfo, result))

    def get_sim_identifiers(
        self,
        dongle_id: int,
        *,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> DongleSimIdentifiers:
        """
        Get modem SIM identifiers.

        Asks the online modem for the identifiers of its SIM card and returns them in the answer.
        DONGLE_MANAGEMENT_API_ERROR_IDENTIFIER_HTTP_RESPONSE and
        DONGLE_MANAGEMENT_API_ERROR_IDENTIFIER_INVALID_CONTENT mean the modem did not answer or answered
        malformed data: a temporary state, the request can be repeated.

        Args:
          dongle_id: Identifier in the path

        Error codes (``error_message``): DONGLE_ERROR_DONGLE_NOT_FOUND,
        DONGLE_MANAGEMENT_API_ERROR_IDENTIFIER_HTTP_RESPONSE,
        DONGLE_MANAGEMENT_API_ERROR_IDENTIFIER_INVALID_CONTENT.
        """
        data = self._client._request(
            "POST",
            f"/dongle/{path_param(dongle_id)}/mobile-network-ids",
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
        )
        result = data.get("result") if isinstance(data, dict) else data
        return cast(DongleSimIdentifiers, construct_type(DongleSimIdentifiers, result))

    def list_statistics(
        self,
        dongle_id: int,
        *,
        from_: Union[str, datetime.datetime, NotGiven] = NOT_GIVEN,
        to: Union[str, datetime.datetime, NotGiven] = NOT_GIVEN,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> List[DongleStatistic]:
        """
        List modem traffic statistics.

        Traffic samples of the modem: read and write are the byte counters reported for the sample taken at
        time. Oldest first: sorted by time ascending. Without from and to the whole history is returned.

        Args:
          dongle_id: Identifier in the path
          from_: Samples taken after this moment (exclusive). `YYYY-MM-DD HH:MM:SS` in UTC or an RFC 3339 date-
                time with an offset (`2020-01-01T00:00:00Z`, `2020-01-01T03:00:00+03:00`, fractional
                seconds allowed); any other value answers 400 PARSING_DATE_TIME_EXCEPTION.
          to: Samples taken before this moment (exclusive). `YYYY-MM-DD HH:MM:SS` in UTC or an RFC 3339 date-time
                with an offset (`2020-01-01T00:00:00Z`, `2020-01-01T03:00:00+03:00`, fractional seconds
                allowed); any other value answers 400 PARSING_DATE_TIME_EXCEPTION.

        Error codes (``error_message``): PARSING_DATE_TIME_EXCEPTION, DONGLE_ERROR_DONGLE_NOT_FOUND.
        """
        data = self._client._request(
            "GET",
            f"/dongle/{path_param(dongle_id)}/statistic",
            query={"from": from_, "to": to},
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
        )
        return cast(
            List[DongleStatistic], construct_type(List[DongleStatistic], data if isinstance(data, list) else [])
        )


class AsyncDonglesResource(AsyncAPIResource):
    """Modems of the account and their commands: reboot, Wi-Fi, Wi-Fi extender, number, network info."""

    async def list(
        self,
        *,
        page: Union[int, NotGiven] = NOT_GIVEN,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        dongle_ids: Union[Iterable[int], NotGiven] = NOT_GIVEN,
        order_by: Union[str, NotGiven] = NOT_GIVEN,
        order: Union[Literal["asc", "desc"], NotGiven] = NOT_GIVEN,
        is_active: Union[bool, NotGiven] = NOT_GIVEN,
        is_short: Union[bool, NotGiven] = NOT_GIVEN,
        is_tariff_package_active: Union[bool, NotGiven] = NOT_GIVEN,
        is_tariff_package_enabled: Union[bool, NotGiven] = NOT_GIVEN,
        dongle_call_type_ids: Union[Iterable[int], NotGiven] = NOT_GIVEN,
        name: Union[str, NotGiven] = NOT_GIVEN,
        number: Union[str, NotGiven] = NOT_GIVEN,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> AsyncPage[DongleListItem]:
        """
        List modems.

        Modems of the account. In full mode every field of the Dongle schema that the list serves is returned;
        dongle_setting and public_vpn_server are present in full mode only. The cheapest call is GET
        /dongle?is_short=1&limit=1: use it to check that an API key works. Newest first by default (created_at
        descending, then the id descending).

        Args:
          page: Page number, 0-based.
          limit: Number of items per page, 1 to 1000.
          dongle_ids: Array of integers representing dongle IDs
          order_by: Attribute to sort by, sent together with order. One of: dongleId, name, number, createdAt,
                updatedAt, activatedAt, lastOnlineAt, isActive, isTariffPackageActive, tariffPackageEnd,
                recentOutgoingSmsCount, recentOutgoingCallCount.
          order: Sort direction, sent together with order_by. Without order_by and order the list is newest first:
                created_at descending, then the id descending.
          is_active: Filter by dongle active flag
          is_short: Short mode: only dongle_id, name, number, is_trial, is_tariff_package_active,
                dongle_online_status, dongle_online_error_code_id, dongle_call_type_id and
                is_wifi_extender_processing per modem; the cheapest call, also fit to check that the key
                works.
          is_tariff_package_active: Filter by an active subscription.
          is_tariff_package_enabled: Filter by an enabled subscription.
          dongle_call_type_ids: Filter by how incoming calls are handled: 1 - SIP, 2 - call scenario
          name: Filter by a fragment of the name, case-insensitive.
          number: Filter by a fragment of the phone number.

        Error codes (``error_message``): REQUEST_VALIDATION_EXCEPTION.
        """
        return await self._client._get_page(
            "/dongle",
            query={
                "page": page,
                "limit": limit,
                "dongle_ids[]": dongle_ids,
                "order_by": order_by,
                "order": order,
                "is_active": is_active,
                "is_short": is_short,
                "is_tariff_package_active": is_tariff_package_active,
                "is_tariff_package_enabled": is_tariff_package_enabled,
                "dongle_call_type_ids[]": dongle_call_type_ids,
                "name": name,
                "number": number,
            },
            item_key="dongles",
            item_type=DongleListItem,
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
        )

    async def reboot(
        self,
        dongle_id: int,
        *,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> bool:
        """
        Reboot modem.

        200 means the reboot is accepted, not done: dongle_online_status becomes 7 (REBOOTING) at once and
        goes back to an online or offline status when the modem returns. A repeated call while a reboot is in
        progress (about 180 s for the API stage, then the SMS stage) is a no-op that also answers 200. The
        reboot is accepted regardless of the subscription and of the online state; track progress through
        dongle_online_status in GET /dongle or GET /dongle/{dongle_id}.

        Args:
          dongle_id: Identifier in the path

        Error codes (``error_message``): REQUEST_VALIDATION_EXCEPTION, DONGLE_NOT_FOUND_EXCEPTION.
        """
        data = await self._client._request(
            "POST",
            f"/dongle/{path_param(dongle_id)}/reboot",
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
        )
        return bool(isinstance(data, dict) and data.get("status"))

    async def enable_wifi(
        self,
        dongle_id: int,
        *,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> bool:
        """
        Enable modem Wi-Fi.

        Turns the Wi-Fi hotspot of the modem on; the modem must be online. Answers {"status": true} when the
        command is accepted; is_hotspot_enable in GET /dongle/{dongle_id} follows once the modem applied it.

        Args:
          dongle_id: ID of the dongle

        Error codes (``error_message``): REQUEST_VALIDATION_EXCEPTION, DONGLE_NOT_FOUND_EXCEPTION,
        DONGLE_WIFI_ALREADY_IN_THE_SAME_STATUS_EXCEPTION, DONGLE_API_CONNECTION_EXCEPTION,
        DONGLE_API_HTTP_RESPONSE_EXCEPTION.
        """
        data = await self._client._request(
            "POST",
            f"/dongle/{path_param(dongle_id)}/wifi/enable",
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
        )
        return bool(isinstance(data, dict) and data.get("status"))

    async def disable_wifi(
        self,
        dongle_id: int,
        *,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> bool:
        """
        Disable modem Wi-Fi.

        Turns the Wi-Fi hotspot of the modem off; the modem must be online. Answers {"status": true} when the
        command is accepted.

        Args:
          dongle_id: ID of the dongle

        Error codes (``error_message``): REQUEST_VALIDATION_EXCEPTION, DONGLE_NOT_FOUND_EXCEPTION,
        DONGLE_WIFI_ALREADY_IN_THE_SAME_STATUS_EXCEPTION, DONGLE_API_CONNECTION_EXCEPTION,
        DONGLE_API_HTTP_RESPONSE_EXCEPTION.
        """
        data = await self._client._request(
            "POST",
            f"/dongle/{path_param(dongle_id)}/wifi/disable",
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
        )
        return bool(isinstance(data, dict) and data.get("status"))

    async def set_wifi_credentials(
        self,
        dongle_id: int,
        *,
        hotspot_name: str,
        hotspot_password: str,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> bool:
        """
        Set modem Wi-Fi credentials.

        Sets the name and the password of the Wi-Fi hotspot of the modem.

        Args:
          dongle_id: ID of the dongle

        Error codes (``error_message``): REQUEST_VALIDATION_EXCEPTION, DONGLE_NOT_FOUND_EXCEPTION,
        DONGLE_WIFI_INVALID_SSID_EXCEPTION, DONGLE_WIFI_INVALID_PASSWORD_EXCEPTION, DONGLE_WIFI_API_EXCEPTION.
        """
        data = await self._client._request(
            "POST",
            f"/dongle/{path_param(dongle_id)}/wifi/credentials",
            body={"hotspot_name": hotspot_name, "hotspot_password": hotspot_password},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return bool(isinstance(data, dict) and data.get("status"))

    async def enable_wifi_extender(
        self,
        dongle_id: int,
        *,
        ssid: str,
        password: str,
        wifi_extender_mode: int,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> bool:
        """
        Enable Wi-Fi extender.

        Connects the modem to an external Wi-Fi network as a client (extender mode); the modem must be online.
        is_wifi_extender_processing is true in GET /dongle while the modem applies the command.

        Args:
          dongle_id: ID of the dongle
          wifi_extender_mode: 2=ENABLED, 3=ENABLED_COMBINED

        Error codes (``error_message``): REQUEST_VALIDATION_EXCEPTION, DONGLE_NOT_FOUND_EXCEPTION,
        BILLING_ERROR_IDENTIFIER_DONGLE_SUBSCRIPTION_NOT_ACTIVE, DONGLE_WIFI_EXTENDER_LOCKED_EXCEPTION,
        DONGLE_API_CONNECTION_EXCEPTION, DONGLE_API_HTTP_RESPONSE_EXCEPTION.
        """
        data = await self._client._request(
            "POST",
            f"/dongle/{path_param(dongle_id)}/wifi-extender/enable",
            body={"ssid": ssid, "password": password, "wifi_extender_mode": wifi_extender_mode},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return bool(isinstance(data, dict) and data.get("status"))

    async def disable_wifi_extender(
        self,
        dongle_id: int,
        *,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> bool:
        """
        Disable Wi-Fi extender.

        Disconnects the modem from the external Wi-Fi network; the modem must be online.

        Args:
          dongle_id: ID of the dongle

        Error codes (``error_message``): REQUEST_VALIDATION_EXCEPTION, DONGLE_NOT_FOUND_EXCEPTION,
        DONGLE_WIFI_EXTENDER_LOCKED_EXCEPTION, DONGLE_API_CONNECTION_EXCEPTION,
        DONGLE_API_HTTP_RESPONSE_EXCEPTION.
        """
        data = await self._client._request(
            "POST",
            f"/dongle/{path_param(dongle_id)}/wifi-extender/disable",
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
        )
        return bool(isinstance(data, dict) and data.get("status"))

    async def scan_wifi_networks(
        self,
        dongle_id: int,
        *,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> bool:
        """
        Scan Wi-Fi networks.

        Asks the modem to scan the Wi-Fi networks around it; the modem must be online.

        Args:
          dongle_id: ID of the dongle

        Error codes (``error_message``): REQUEST_VALIDATION_EXCEPTION, DONGLE_NOT_FOUND_EXCEPTION,
        BILLING_ERROR_IDENTIFIER_DONGLE_SUBSCRIPTION_NOT_ACTIVE, DONGLE_API_CONNECTION_EXCEPTION,
        DONGLE_API_HTTP_RESPONSE_EXCEPTION.
        """
        data = await self._client._request(
            "POST",
            f"/dongle/{path_param(dongle_id)}/wifi-extender/networks",
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
        )
        return bool(isinstance(data, dict) and data.get("status"))

    async def update_offline_notification(
        self,
        dongle_id: int,
        *,
        is_enabled: bool,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> bool:
        """
        Set offline notification.

        Turns the e-mail to the owner about the modem going offline on or off; shown as
        dongle_setting.is_offline_notification_enabled in GET /dongle.

        Args:
          dongle_id: ID of the dongle
          is_enabled: Enable (true) or disable (false) email when the modem goes offline

        Error codes (``error_message``): REQUEST_VALIDATION_EXCEPTION, DONGLE_NOT_FOUND_EXCEPTION,
        DONGLE_SETTING_NOT_FOUND.
        """
        data = await self._client._request(
            "PUT",
            f"/dongle/{path_param(dongle_id)}/setting/offline-notification",
            body={"is_enabled": is_enabled},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return bool(isinstance(data, dict) and data.get("status"))

    async def set_number(
        self,
        dongle_id: int,
        *,
        number: str,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> bool:
        """
        Set modem number.

        Accepted asynchronously: the number is verified through the dongle and stored on success; 200 means
        queued.

        Args:
          dongle_id: ID of the dongle
          number: Phone number in international format.

        Error codes (``error_message``): REQUEST_VALIDATION_EXCEPTION, DONGLE_NOT_FOUND_EXCEPTION,
        DONGLE_MANUAL_PHONE_DETERMINATION_NUMBER_EXCEPTION,
        DONGLE_MANUAL_PHONE_DETERMINATION_ALREADY_IN_PROGRESS_EXCEPTION.
        """
        data = await self._client._request(
            "PUT",
            f"/dongle/{path_param(dongle_id)}/number",
            body={"number": number},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return bool(isinstance(data, dict) and data.get("status"))

    async def get(
        self,
        dongle_id: int,
        *,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> Dongle:
        """
        Get modem.

        One modem of the account with its counters and hardware identity.

        Args:
          dongle_id: Identifier in the path

        Error codes (``error_message``): DONGLE_ERROR_DONGLE_NOT_FOUND.
        """
        data = await self._client._request(
            "GET",
            f"/dongle/{path_param(dongle_id)}",
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
        )
        return cast(Dongle, construct_type(Dongle, data))

    async def update(
        self,
        dongle_id: int,
        *,
        name: Union[str, NotGiven] = NOT_GIVEN,
        number: Union[str, NotGiven] = NOT_GIVEN,
        is_mute_incoming_call: Union[bool, NotGiven] = NOT_GIVEN,
        dongle_call_type_id: Union[int, NotGiven] = NOT_GIVEN,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> Dongle:
        """
        Update modem.

        Only the listed body fields are read; unknown fields are ignored. An omitted field keeps its value.
        The billing fields tariff_package_id, is_tariff_package_enabled, order_dongle_id, is_deleted and
        is_active and the field imei_fake are outside the public API: a body with any of them is refused as a
        whole with 403 PUBLIC_API_FIELD_FORBIDDEN.

        Args:
          dongle_id: Identifier in the path
          name: Display name of the modem.
          number: Phone number of the SIM in international format. Omit the field to keep the current number: null
                does not clear it.
          is_mute_incoming_call: Reject incoming calls on the modem.
          dongle_call_type_id: How incoming calls are handled: 1 - SIP (softphone), 2 - call scenario.

        Error codes (``error_message``): DONGLE_ERROR_DONGLE_NOT_FOUND, PUBLIC_API_FIELD_FORBIDDEN.
        """
        data = await self._client._request(
            "PUT",
            f"/dongle/{path_param(dongle_id)}",
            body={
                "name": name,
                "number": number,
                "is_mute_incoming_call": is_mute_incoming_call,
                "dongle_call_type_id": dongle_call_type_id,
            },
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return cast(Dongle, construct_type(Dongle, data))

    async def get_network_info(
        self,
        dongle_id: int,
        *,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> DongleNetworkInfo:
        """
        Get modem network info.

        Asks the online modem for its radio state and returns it in the answer: networks, roaming, network
        type and signal. DONGLE_MANAGEMENT_API_ERROR_IDENTIFIER_HTTP_RESPONSE and
        DONGLE_MANAGEMENT_API_ERROR_IDENTIFIER_INVALID_CONTENT mean the modem did not answer or answered
        malformed data: a temporary state, the request can be repeated.

        Args:
          dongle_id: Identifier in the path

        Error codes (``error_message``): DONGLE_ERROR_DONGLE_NOT_FOUND,
        DONGLE_MANAGEMENT_API_ERROR_IDENTIFIER_HTTP_RESPONSE,
        DONGLE_MANAGEMENT_API_ERROR_IDENTIFIER_INVALID_CONTENT.
        """
        data = await self._client._request(
            "POST",
            f"/dongle/{path_param(dongle_id)}/mobile-network-info",
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
        )
        result = data.get("result") if isinstance(data, dict) else data
        return cast(DongleNetworkInfo, construct_type(DongleNetworkInfo, result))

    async def get_sim_identifiers(
        self,
        dongle_id: int,
        *,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> DongleSimIdentifiers:
        """
        Get modem SIM identifiers.

        Asks the online modem for the identifiers of its SIM card and returns them in the answer.
        DONGLE_MANAGEMENT_API_ERROR_IDENTIFIER_HTTP_RESPONSE and
        DONGLE_MANAGEMENT_API_ERROR_IDENTIFIER_INVALID_CONTENT mean the modem did not answer or answered
        malformed data: a temporary state, the request can be repeated.

        Args:
          dongle_id: Identifier in the path

        Error codes (``error_message``): DONGLE_ERROR_DONGLE_NOT_FOUND,
        DONGLE_MANAGEMENT_API_ERROR_IDENTIFIER_HTTP_RESPONSE,
        DONGLE_MANAGEMENT_API_ERROR_IDENTIFIER_INVALID_CONTENT.
        """
        data = await self._client._request(
            "POST",
            f"/dongle/{path_param(dongle_id)}/mobile-network-ids",
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
        )
        result = data.get("result") if isinstance(data, dict) else data
        return cast(DongleSimIdentifiers, construct_type(DongleSimIdentifiers, result))

    async def list_statistics(
        self,
        dongle_id: int,
        *,
        from_: Union[str, datetime.datetime, NotGiven] = NOT_GIVEN,
        to: Union[str, datetime.datetime, NotGiven] = NOT_GIVEN,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> List[DongleStatistic]:
        """
        List modem traffic statistics.

        Traffic samples of the modem: read and write are the byte counters reported for the sample taken at
        time. Oldest first: sorted by time ascending. Without from and to the whole history is returned.

        Args:
          dongle_id: Identifier in the path
          from_: Samples taken after this moment (exclusive). `YYYY-MM-DD HH:MM:SS` in UTC or an RFC 3339 date-
                time with an offset (`2020-01-01T00:00:00Z`, `2020-01-01T03:00:00+03:00`, fractional
                seconds allowed); any other value answers 400 PARSING_DATE_TIME_EXCEPTION.
          to: Samples taken before this moment (exclusive). `YYYY-MM-DD HH:MM:SS` in UTC or an RFC 3339 date-time
                with an offset (`2020-01-01T00:00:00Z`, `2020-01-01T03:00:00+03:00`, fractional seconds
                allowed); any other value answers 400 PARSING_DATE_TIME_EXCEPTION.

        Error codes (``error_message``): PARSING_DATE_TIME_EXCEPTION, DONGLE_ERROR_DONGLE_NOT_FOUND.
        """
        data = await self._client._request(
            "GET",
            f"/dongle/{path_param(dongle_id)}/statistic",
            query={"from": from_, "to": to},
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
        )
        return cast(
            List[DongleStatistic], construct_type(List[DongleStatistic], data if isinstance(data, list) else [])
        )
