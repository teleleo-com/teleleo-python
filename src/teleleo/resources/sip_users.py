# File generated from spec/openapi.yaml by scripts/generate.py. Do not edit by hand.

from __future__ import annotations

from typing import Iterable, List, Optional, Union, cast

from .._models import construct_type
from .._resource import AsyncAPIResource, SyncAPIResource
from .._types import NOT_GIVEN, Headers, NotGiven, Query, Timeout
from .._utils import path_param
from ..types import PbxSipUser

__all__ = ["SipUsersResource", "AsyncSipUsersResource"]


class SipUsersResource(SyncAPIResource):
    """SIP accounts of the modems."""

    def list(
        self,
        *,
        dongle_call_type_ids: Union[Iterable[int], NotGiven] = NOT_GIVEN,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> List[PbxSipUser]:
        """
        List SIP users.

        SIP accounts of the modems of the account, one per modem (dongle_id is always set; the softphone login
        of the cabinet and the mobile app is not listed). Modems deleted from the account are not listed.
        pbx_sip_connections lists the SIP servers to register at (TLS and UDP/TCP).

        Args:
          dongle_call_type_ids: Array of integers representing dongle call type IDs

        Error codes (``error_message``): REQUEST_VALIDATION_EXCEPTION.
        """
        data = self._client._request(
            "GET",
            "/sip-user",
            query={"dongle_call_type_ids[]": dongle_call_type_ids},
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
        )
        items = data.get("pbx_sip_users") if isinstance(data, dict) else data
        return cast(List[PbxSipUser], construct_type(List[PbxSipUser], items if isinstance(items, list) else []))

    def get(
        self,
        sip_user_id: int,
        *,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> PbxSipUser:
        """
        Get SIP user.

        One SIP account of a modem of the account. An unknown id, the SIP account of a deleted modem and the
        softphone login of the cabinet and the mobile app answer 404
        PBX_SIP_ERROR_IDENTIFIER_CANT_FIND_PBX_USER.

        Args:
          sip_user_id: Identifier in the path

        Error codes (``error_message``): PBX_SIP_ERROR_IDENTIFIER_CANT_FIND_PBX_USER.
        """
        data = self._client._request(
            "GET",
            f"/sip-user/{path_param(sip_user_id)}",
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
        )
        return cast(PbxSipUser, construct_type(PbxSipUser, data))


class AsyncSipUsersResource(AsyncAPIResource):
    """SIP accounts of the modems."""

    async def list(
        self,
        *,
        dongle_call_type_ids: Union[Iterable[int], NotGiven] = NOT_GIVEN,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> List[PbxSipUser]:
        """
        List SIP users.

        SIP accounts of the modems of the account, one per modem (dongle_id is always set; the softphone login
        of the cabinet and the mobile app is not listed). Modems deleted from the account are not listed.
        pbx_sip_connections lists the SIP servers to register at (TLS and UDP/TCP).

        Args:
          dongle_call_type_ids: Array of integers representing dongle call type IDs

        Error codes (``error_message``): REQUEST_VALIDATION_EXCEPTION.
        """
        data = await self._client._request(
            "GET",
            "/sip-user",
            query={"dongle_call_type_ids[]": dongle_call_type_ids},
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
        )
        items = data.get("pbx_sip_users") if isinstance(data, dict) else data
        return cast(List[PbxSipUser], construct_type(List[PbxSipUser], items if isinstance(items, list) else []))

    async def get(
        self,
        sip_user_id: int,
        *,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> PbxSipUser:
        """
        Get SIP user.

        One SIP account of a modem of the account. An unknown id, the SIP account of a deleted modem and the
        softphone login of the cabinet and the mobile app answer 404
        PBX_SIP_ERROR_IDENTIFIER_CANT_FIND_PBX_USER.

        Args:
          sip_user_id: Identifier in the path

        Error codes (``error_message``): PBX_SIP_ERROR_IDENTIFIER_CANT_FIND_PBX_USER.
        """
        data = await self._client._request(
            "GET",
            f"/sip-user/{path_param(sip_user_id)}",
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
        )
        return cast(PbxSipUser, construct_type(PbxSipUser, data))
