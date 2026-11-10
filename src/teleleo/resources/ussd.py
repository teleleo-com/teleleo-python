# File generated from spec/openapi.yaml by scripts/generate.py. Do not edit by hand.

from __future__ import annotations

from typing import Optional, Union, cast

from typing_extensions import Literal

from .._models import construct_type
from .._pagination import AsyncPage, SyncPage
from .._resource import AsyncAPIResource, SyncAPIResource
from .._types import NOT_GIVEN, Body, Headers, NotGiven, Query, Timeout
from .._utils import path_param
from ..types import Ussd

__all__ = ["UssdResource", "AsyncUssdResource"]


class UssdResource(SyncAPIResource):
    """USSD requests through a modem."""

    def list(
        self,
        dongle_id: int,
        *,
        page: Union[int, NotGiven] = NOT_GIVEN,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        order_by: Union[str, NotGiven] = NOT_GIVEN,
        order: Union[Literal["asc", "desc"], NotGiven] = NOT_GIVEN,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> SyncPage[Ussd]:
        """
        List USSD requests.

        USSD requests and answers of the modem. Newest first by default (created_at descending, then the id
        descending).

        Args:
          dongle_id: Identifier in the path
          page: Page number, 0-based.
          limit: Number of items per page, 1 to 1000.
          order_by: Attribute to sort by, sent together with order. One of: ussdId, ussdStatus, ussdType, command,
                response, createdAt, updatedAt.
          order: Sort direction, sent together with order_by. Without order_by and order the list is newest first:
                created_at descending, then the id descending.

        Error codes (``error_message``): REQUEST_VALIDATION_EXCEPTION, DONGLE_NOT_FOUND_EXCEPTION.
        """
        return self._client._get_page(
            f"/dongle/{path_param(dongle_id)}/ussd",
            query={"page": page, "limit": limit, "order_by": order_by, "order": order},
            item_key="ussds",
            item_type=Ussd,
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
        )

    def send(
        self,
        dongle_id: int,
        *,
        command: str,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> Ussd:
        """
        Send USSD.

        Sends a USSD command through the modem; the answer arrives later in response of the USSD object. Works
        where the operator has 3G coverage; interactive (menu) USSD is not supported.

        Args:
          dongle_id: Identifier in the path

        Error codes (``error_message``): REQUEST_VALIDATION_EXCEPTION, DONGLE_NOT_FOUND_EXCEPTION,
        USSD_INVALID_COMMAND_FORMAT_EXCEPTION, BILLING_ERROR_IDENTIFIER_DONGLE_SUBSCRIPTION_NOT_ACTIVE,
        USSD_LAST_USSD_NOT_PROCESSED_EXCEPTION.
        """
        data = self._client._request(
            "POST",
            f"/dongle/{path_param(dongle_id)}/ussd",
            body={"command": command},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return cast(Ussd, construct_type(Ussd, data))

    def get(
        self,
        dongle_id: int,
        ussd_id: int,
        *,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> Ussd:
        """
        Get USSD request.

        One USSD request of the modem with its answer.

        Args:
          dongle_id: Identifier in the path
          ussd_id: Identifier in the path

        Error codes (``error_message``): REQUEST_VALIDATION_EXCEPTION, DONGLE_NOT_FOUND_EXCEPTION,
        USSD_NOT_FOUND_EXCEPTION.
        """
        data = self._client._request(
            "GET",
            f"/dongle/{path_param(dongle_id)}/ussd/{path_param(ussd_id)}",
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
        )
        return cast(Ussd, construct_type(Ussd, data))

    def delete(
        self,
        dongle_id: int,
        ussd_id: int,
        *,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> bool:
        """
        Delete USSD request.

        Deletes one USSD request from the history of the modem.

        Args:
          dongle_id: Identifier in the path
          ussd_id: Identifier in the path

        Error codes (``error_message``): REQUEST_VALIDATION_EXCEPTION, DONGLE_NOT_FOUND_EXCEPTION,
        USSD_NOT_FOUND_EXCEPTION.
        """
        data = self._client._request(
            "DELETE",
            f"/dongle/{path_param(dongle_id)}/ussd/{path_param(ussd_id)}",
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
        )
        return bool(isinstance(data, dict) and data.get("status"))

    def delete_all(
        self,
        dongle_id: int,
        *,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> bool:
        """
        Delete USSD history.

        Deletes the whole USSD history of the modem.

        Args:
          dongle_id: Identifier in the path

        Error codes (``error_message``): REQUEST_VALIDATION_EXCEPTION, DONGLE_NOT_FOUND_EXCEPTION.
        """
        data = self._client._request(
            "DELETE",
            f"/dongle/{path_param(dongle_id)}/ussds",
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
        )
        return bool(isinstance(data, dict) and data.get("status"))


class AsyncUssdResource(AsyncAPIResource):
    """USSD requests through a modem."""

    async def list(
        self,
        dongle_id: int,
        *,
        page: Union[int, NotGiven] = NOT_GIVEN,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        order_by: Union[str, NotGiven] = NOT_GIVEN,
        order: Union[Literal["asc", "desc"], NotGiven] = NOT_GIVEN,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> AsyncPage[Ussd]:
        """
        List USSD requests.

        USSD requests and answers of the modem. Newest first by default (created_at descending, then the id
        descending).

        Args:
          dongle_id: Identifier in the path
          page: Page number, 0-based.
          limit: Number of items per page, 1 to 1000.
          order_by: Attribute to sort by, sent together with order. One of: ussdId, ussdStatus, ussdType, command,
                response, createdAt, updatedAt.
          order: Sort direction, sent together with order_by. Without order_by and order the list is newest first:
                created_at descending, then the id descending.

        Error codes (``error_message``): REQUEST_VALIDATION_EXCEPTION, DONGLE_NOT_FOUND_EXCEPTION.
        """
        return await self._client._get_page(
            f"/dongle/{path_param(dongle_id)}/ussd",
            query={"page": page, "limit": limit, "order_by": order_by, "order": order},
            item_key="ussds",
            item_type=Ussd,
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
        )

    async def send(
        self,
        dongle_id: int,
        *,
        command: str,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> Ussd:
        """
        Send USSD.

        Sends a USSD command through the modem; the answer arrives later in response of the USSD object. Works
        where the operator has 3G coverage; interactive (menu) USSD is not supported.

        Args:
          dongle_id: Identifier in the path

        Error codes (``error_message``): REQUEST_VALIDATION_EXCEPTION, DONGLE_NOT_FOUND_EXCEPTION,
        USSD_INVALID_COMMAND_FORMAT_EXCEPTION, BILLING_ERROR_IDENTIFIER_DONGLE_SUBSCRIPTION_NOT_ACTIVE,
        USSD_LAST_USSD_NOT_PROCESSED_EXCEPTION.
        """
        data = await self._client._request(
            "POST",
            f"/dongle/{path_param(dongle_id)}/ussd",
            body={"command": command},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return cast(Ussd, construct_type(Ussd, data))

    async def get(
        self,
        dongle_id: int,
        ussd_id: int,
        *,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> Ussd:
        """
        Get USSD request.

        One USSD request of the modem with its answer.

        Args:
          dongle_id: Identifier in the path
          ussd_id: Identifier in the path

        Error codes (``error_message``): REQUEST_VALIDATION_EXCEPTION, DONGLE_NOT_FOUND_EXCEPTION,
        USSD_NOT_FOUND_EXCEPTION.
        """
        data = await self._client._request(
            "GET",
            f"/dongle/{path_param(dongle_id)}/ussd/{path_param(ussd_id)}",
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
        )
        return cast(Ussd, construct_type(Ussd, data))

    async def delete(
        self,
        dongle_id: int,
        ussd_id: int,
        *,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> bool:
        """
        Delete USSD request.

        Deletes one USSD request from the history of the modem.

        Args:
          dongle_id: Identifier in the path
          ussd_id: Identifier in the path

        Error codes (``error_message``): REQUEST_VALIDATION_EXCEPTION, DONGLE_NOT_FOUND_EXCEPTION,
        USSD_NOT_FOUND_EXCEPTION.
        """
        data = await self._client._request(
            "DELETE",
            f"/dongle/{path_param(dongle_id)}/ussd/{path_param(ussd_id)}",
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
        )
        return bool(isinstance(data, dict) and data.get("status"))

    async def delete_all(
        self,
        dongle_id: int,
        *,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> bool:
        """
        Delete USSD history.

        Deletes the whole USSD history of the modem.

        Args:
          dongle_id: Identifier in the path

        Error codes (``error_message``): REQUEST_VALIDATION_EXCEPTION, DONGLE_NOT_FOUND_EXCEPTION.
        """
        data = await self._client._request(
            "DELETE",
            f"/dongle/{path_param(dongle_id)}/ussds",
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
        )
        return bool(isinstance(data, dict) and data.get("status"))
