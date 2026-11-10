# File generated from spec/openapi.yaml by scripts/generate.py. Do not edit by hand.

from __future__ import annotations

from typing import List, Optional, Union, cast

from .._models import construct_type
from .._resource import AsyncAPIResource, SyncAPIResource
from .._types import NOT_GIVEN, Headers, NotGiven, Query, Timeout
from .._utils import path_param
from ..types import PublicVpnSession

__all__ = ["PublicVpnResource", "AsyncPublicVpnResource"]


class PublicVpnResource(SyncAPIResource):
    """VPN access through a modem."""

    def enable(
        self,
        dongle_id: int,
        *,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> bool:
        """
        Enable public VPN.

        Creates the VPN account of the modem on the gateway and answers {"status": true}. The credentials are
        not in the answer: read public_vpn_login, public_vpn_password and public_vpn_server from GET /dongle
        (full mode). is_public_vpn_enabled of the modem becomes true.

        Args:
          dongle_id: ID of the dongle

        Error codes (``error_message``): REQUEST_VALIDATION_EXCEPTION, DONGLE_NOT_FOUND_EXCEPTION,
        BILLING_ERROR_IDENTIFIER_DONGLE_SUBSCRIPTION_NOT_ACTIVE, DONGLE_PUBLIC_VPN_ALREADY_ENABLED_EXCEPTION.
        """
        data = self._client._request(
            "POST",
            f"/dongle/{path_param(dongle_id)}/public-vpn/enable",
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
        )
        return bool(isinstance(data, dict) and data.get("status"))

    def disable(
        self,
        dongle_id: int,
        *,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> bool:
        """
        Disable public VPN.

        Removes the VPN account of the modem from the gateway and drops its sessions; answers {"status":
        true}. is_public_vpn_enabled becomes false; the login is kept and reused by a later enable.

        Args:
          dongle_id: ID of the dongle

        Error codes (``error_message``): REQUEST_VALIDATION_EXCEPTION, DONGLE_NOT_FOUND_EXCEPTION,
        DONGLE_PUBLIC_VPN_ALREADY_DISABLED_EXCEPTION.
        """
        data = self._client._request(
            "POST",
            f"/dongle/{path_param(dongle_id)}/public-vpn/disable",
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
        )
        return bool(isinstance(data, dict) and data.get("status"))

    def refresh_password(
        self,
        dongle_id: int,
        *,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> bool:
        """
        Refresh public VPN password.

        The response carries only status; the new password is returned by GET /dongle (public_vpn_password,
        full mode). Requires an active tariff.

        Args:
          dongle_id: ID of the dongle

        Error codes (``error_message``): REQUEST_VALIDATION_EXCEPTION, DONGLE_NOT_FOUND_EXCEPTION,
        BILLING_ERROR_IDENTIFIER_DONGLE_SUBSCRIPTION_NOT_ACTIVE.
        """
        data = self._client._request(
            "POST",
            f"/dongle/{path_param(dongle_id)}/public-vpn/refresh-password",
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
        )
        return bool(isinstance(data, dict) and data.get("status"))

    def list_sessions(
        self,
        *,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> List[PublicVpnSession]:
        """
        List public VPN sessions.

        Live VPN sessions of the modems of the account, as the VPN gateway reports them. Not paginated.
        """
        data = self._client._request(
            "GET",
            "/public-vpn/connect-session-list",
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
        )
        items = data.get("connect_sessions") if isinstance(data, dict) else data
        return cast(
            List[PublicVpnSession], construct_type(List[PublicVpnSession], items if isinstance(items, list) else [])
        )


class AsyncPublicVpnResource(AsyncAPIResource):
    """VPN access through a modem."""

    async def enable(
        self,
        dongle_id: int,
        *,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> bool:
        """
        Enable public VPN.

        Creates the VPN account of the modem on the gateway and answers {"status": true}. The credentials are
        not in the answer: read public_vpn_login, public_vpn_password and public_vpn_server from GET /dongle
        (full mode). is_public_vpn_enabled of the modem becomes true.

        Args:
          dongle_id: ID of the dongle

        Error codes (``error_message``): REQUEST_VALIDATION_EXCEPTION, DONGLE_NOT_FOUND_EXCEPTION,
        BILLING_ERROR_IDENTIFIER_DONGLE_SUBSCRIPTION_NOT_ACTIVE, DONGLE_PUBLIC_VPN_ALREADY_ENABLED_EXCEPTION.
        """
        data = await self._client._request(
            "POST",
            f"/dongle/{path_param(dongle_id)}/public-vpn/enable",
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
        )
        return bool(isinstance(data, dict) and data.get("status"))

    async def disable(
        self,
        dongle_id: int,
        *,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> bool:
        """
        Disable public VPN.

        Removes the VPN account of the modem from the gateway and drops its sessions; answers {"status":
        true}. is_public_vpn_enabled becomes false; the login is kept and reused by a later enable.

        Args:
          dongle_id: ID of the dongle

        Error codes (``error_message``): REQUEST_VALIDATION_EXCEPTION, DONGLE_NOT_FOUND_EXCEPTION,
        DONGLE_PUBLIC_VPN_ALREADY_DISABLED_EXCEPTION.
        """
        data = await self._client._request(
            "POST",
            f"/dongle/{path_param(dongle_id)}/public-vpn/disable",
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
        )
        return bool(isinstance(data, dict) and data.get("status"))

    async def refresh_password(
        self,
        dongle_id: int,
        *,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> bool:
        """
        Refresh public VPN password.

        The response carries only status; the new password is returned by GET /dongle (public_vpn_password,
        full mode). Requires an active tariff.

        Args:
          dongle_id: ID of the dongle

        Error codes (``error_message``): REQUEST_VALIDATION_EXCEPTION, DONGLE_NOT_FOUND_EXCEPTION,
        BILLING_ERROR_IDENTIFIER_DONGLE_SUBSCRIPTION_NOT_ACTIVE.
        """
        data = await self._client._request(
            "POST",
            f"/dongle/{path_param(dongle_id)}/public-vpn/refresh-password",
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
        )
        return bool(isinstance(data, dict) and data.get("status"))

    async def list_sessions(
        self,
        *,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> List[PublicVpnSession]:
        """
        List public VPN sessions.

        Live VPN sessions of the modems of the account, as the VPN gateway reports them. Not paginated.
        """
        data = await self._client._request(
            "GET",
            "/public-vpn/connect-session-list",
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
        )
        items = data.get("connect_sessions") if isinstance(data, dict) else data
        return cast(
            List[PublicVpnSession], construct_type(List[PublicVpnSession], items if isinstance(items, list) else [])
        )
