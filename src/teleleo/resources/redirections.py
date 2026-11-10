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
from ..types import Redirection
from ..types import params as _params

__all__ = ["RedirectionsResource", "AsyncRedirectionsResource"]


class RedirectionsResource(SyncAPIResource):
    """Rules for incoming SMS and calls: forwarding, auto reply, HTTP callback."""

    def list(
        self,
        *,
        name: Union[str, NotGiven] = NOT_GIVEN,
        auto_reply_message: Union[str, NotGiven] = NOT_GIVEN,
        dongle_id: Union[int, NotGiven] = NOT_GIVEN,
        dongle_ids: Union[Iterable[int], NotGiven] = NOT_GIVEN,
        from_: Union[str, datetime.datetime, NotGiven] = NOT_GIVEN,
        to: Union[str, datetime.datetime, NotGiven] = NOT_GIVEN,
        page: Union[int, NotGiven] = NOT_GIVEN,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        order_by: Union[str, NotGiven] = NOT_GIVEN,
        order: Union[Literal["asc", "desc"], NotGiven] = NOT_GIVEN,
        redirection_type_ids: Union[Iterable[int], NotGiven] = NOT_GIVEN,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> SyncPage[Redirection]:
        """
        List redirections.

        Redirection rules of the account: forwarding of incoming SMS and calls, auto replies and HTTP
        callbacks. Newest first by default (created_at descending, then the id descending).

        Args:
          name: Filter by a fragment of the name, case-insensitive.
          auto_reply_message: Filter by a fragment of the auto reply message, case-insensitive.
          dongle_id: Only redirections that apply to this dongle, including those without a dongle condition.
          dongle_ids: Only redirections that apply to any of these dongles, including those without a dongle
                condition.
          from_: Redirections created at or after this moment. `YYYY-MM-DD HH:MM:SS` in UTC or an RFC 3339 date-
                time with an offset (`2020-01-01T00:00:00Z`, `2020-01-01T03:00:00+03:00`, fractional
                seconds allowed); any other value answers 400 PARSING_DATE_TIME_EXCEPTION.
          to: Redirections created before this moment. `YYYY-MM-DD HH:MM:SS` in UTC or an RFC 3339 date-time with
                an offset (`2020-01-01T00:00:00Z`, `2020-01-01T03:00:00+03:00`, fractional seconds
                allowed); any other value answers 400 PARSING_DATE_TIME_EXCEPTION.
          page: Page number, 0-based.
          limit: Number of items per page, 1 to 1000.
          order_by: Attribute to sort by, sent together with order. One of: redirectionId, name, redirectionType,
                createdAt, updatedAt.
          order: Sort direction, sent together with order_by. Without order_by and order the list is newest first:
                created_at descending, then the id descending.
          redirection_type_ids: Array of integers representing Redirection type IDs

        Error codes (``error_message``): REQUEST_VALIDATION_EXCEPTION, PARSING_DATE_TIME_EXCEPTION.
        """
        return self._client._get_page(
            "/redirection",
            query={
                "name": name,
                "auto_reply_message": auto_reply_message,
                "dongle_id": dongle_id,
                "dongle_ids[]": dongle_ids,
                "from": from_,
                "to": to,
                "page": page,
                "limit": limit,
                "order_by": order_by,
                "order": order,
                "redirection_type_ids[]": redirection_type_ids,
            },
            item_key="redirections",
            item_type=Redirection,
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
        )

    def create(
        self,
        *,
        condition: _params.RedirectionConditionParam,
        name: str,
        params: _params.RedirectionParamsParam,
        redirection_type_id: int,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> Redirection:
        """
        Create redirection.

        Creates a redirection rule; condition and params are checked on save (see RedirectionCondition and
        RedirectionParams).

        Error codes (``error_message``): REQUEST_VALIDATION_EXCEPTION, PARAMS_NOT_VALID_EXCEPTION,
        CONDITION_NOT_VALID_EXCEPTION, DONGLE_NOT_FOUND,
        BILLING_ERROR_IDENTIFIER_DONGLE_SUBSCRIPTION_NOT_ACTIVE.
        """
        data = self._client._request(
            "POST",
            "/redirection",
            body={"condition": condition, "name": name, "params": params, "redirection_type_id": redirection_type_id},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return cast(Redirection, construct_type(Redirection, data))

    def get(
        self,
        redirection_id: int,
        *,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> Redirection:
        """
        Get redirection.

        One redirection rule of the account.

        Args:
          redirection_id: Identifier in the path

        Error codes (``error_message``): REQUEST_VALIDATION_EXCEPTION, REDIRECTION_NOT_FOUND_EXCEPTION.
        """
        data = self._client._request(
            "GET",
            f"/redirection/{path_param(redirection_id)}",
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
        )
        return cast(Redirection, construct_type(Redirection, data))

    def update(
        self,
        redirection_id: int,
        *,
        condition: _params.RedirectionConditionParam,
        name: str,
        params: _params.RedirectionParamsParam,
        redirection_type_id: int,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> Redirection:
        """
        Update redirection.

        Replaces the redirection rule; the body is checked as on create.

        Args:
          redirection_id: Identifier in the path

        Error codes (``error_message``): REQUEST_VALIDATION_EXCEPTION, REDIRECTION_NOT_FOUND_EXCEPTION,
        PARAMS_NOT_VALID_EXCEPTION, CONDITION_NOT_VALID_EXCEPTION, DONGLE_NOT_FOUND,
        BILLING_ERROR_IDENTIFIER_DONGLE_SUBSCRIPTION_NOT_ACTIVE.
        """
        data = self._client._request(
            "PUT",
            f"/redirection/{path_param(redirection_id)}",
            body={"condition": condition, "name": name, "params": params, "redirection_type_id": redirection_type_id},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return cast(Redirection, construct_type(Redirection, data))

    def delete(
        self,
        redirection_id: int,
        *,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> bool:
        """
        Delete redirection.

        Deletes the redirection rule.

        Args:
          redirection_id: Identifier in the path

        Error codes (``error_message``): REQUEST_VALIDATION_EXCEPTION, REDIRECTION_NOT_FOUND_EXCEPTION.
        """
        data = self._client._request(
            "DELETE",
            f"/redirection/{path_param(redirection_id)}",
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
        )
        return bool(isinstance(data, dict) and data.get("status"))


class AsyncRedirectionsResource(AsyncAPIResource):
    """Rules for incoming SMS and calls: forwarding, auto reply, HTTP callback."""

    async def list(
        self,
        *,
        name: Union[str, NotGiven] = NOT_GIVEN,
        auto_reply_message: Union[str, NotGiven] = NOT_GIVEN,
        dongle_id: Union[int, NotGiven] = NOT_GIVEN,
        dongle_ids: Union[Iterable[int], NotGiven] = NOT_GIVEN,
        from_: Union[str, datetime.datetime, NotGiven] = NOT_GIVEN,
        to: Union[str, datetime.datetime, NotGiven] = NOT_GIVEN,
        page: Union[int, NotGiven] = NOT_GIVEN,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        order_by: Union[str, NotGiven] = NOT_GIVEN,
        order: Union[Literal["asc", "desc"], NotGiven] = NOT_GIVEN,
        redirection_type_ids: Union[Iterable[int], NotGiven] = NOT_GIVEN,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> AsyncPage[Redirection]:
        """
        List redirections.

        Redirection rules of the account: forwarding of incoming SMS and calls, auto replies and HTTP
        callbacks. Newest first by default (created_at descending, then the id descending).

        Args:
          name: Filter by a fragment of the name, case-insensitive.
          auto_reply_message: Filter by a fragment of the auto reply message, case-insensitive.
          dongle_id: Only redirections that apply to this dongle, including those without a dongle condition.
          dongle_ids: Only redirections that apply to any of these dongles, including those without a dongle
                condition.
          from_: Redirections created at or after this moment. `YYYY-MM-DD HH:MM:SS` in UTC or an RFC 3339 date-
                time with an offset (`2020-01-01T00:00:00Z`, `2020-01-01T03:00:00+03:00`, fractional
                seconds allowed); any other value answers 400 PARSING_DATE_TIME_EXCEPTION.
          to: Redirections created before this moment. `YYYY-MM-DD HH:MM:SS` in UTC or an RFC 3339 date-time with
                an offset (`2020-01-01T00:00:00Z`, `2020-01-01T03:00:00+03:00`, fractional seconds
                allowed); any other value answers 400 PARSING_DATE_TIME_EXCEPTION.
          page: Page number, 0-based.
          limit: Number of items per page, 1 to 1000.
          order_by: Attribute to sort by, sent together with order. One of: redirectionId, name, redirectionType,
                createdAt, updatedAt.
          order: Sort direction, sent together with order_by. Without order_by and order the list is newest first:
                created_at descending, then the id descending.
          redirection_type_ids: Array of integers representing Redirection type IDs

        Error codes (``error_message``): REQUEST_VALIDATION_EXCEPTION, PARSING_DATE_TIME_EXCEPTION.
        """
        return await self._client._get_page(
            "/redirection",
            query={
                "name": name,
                "auto_reply_message": auto_reply_message,
                "dongle_id": dongle_id,
                "dongle_ids[]": dongle_ids,
                "from": from_,
                "to": to,
                "page": page,
                "limit": limit,
                "order_by": order_by,
                "order": order,
                "redirection_type_ids[]": redirection_type_ids,
            },
            item_key="redirections",
            item_type=Redirection,
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
        )

    async def create(
        self,
        *,
        condition: _params.RedirectionConditionParam,
        name: str,
        params: _params.RedirectionParamsParam,
        redirection_type_id: int,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> Redirection:
        """
        Create redirection.

        Creates a redirection rule; condition and params are checked on save (see RedirectionCondition and
        RedirectionParams).

        Error codes (``error_message``): REQUEST_VALIDATION_EXCEPTION, PARAMS_NOT_VALID_EXCEPTION,
        CONDITION_NOT_VALID_EXCEPTION, DONGLE_NOT_FOUND,
        BILLING_ERROR_IDENTIFIER_DONGLE_SUBSCRIPTION_NOT_ACTIVE.
        """
        data = await self._client._request(
            "POST",
            "/redirection",
            body={"condition": condition, "name": name, "params": params, "redirection_type_id": redirection_type_id},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return cast(Redirection, construct_type(Redirection, data))

    async def get(
        self,
        redirection_id: int,
        *,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> Redirection:
        """
        Get redirection.

        One redirection rule of the account.

        Args:
          redirection_id: Identifier in the path

        Error codes (``error_message``): REQUEST_VALIDATION_EXCEPTION, REDIRECTION_NOT_FOUND_EXCEPTION.
        """
        data = await self._client._request(
            "GET",
            f"/redirection/{path_param(redirection_id)}",
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
        )
        return cast(Redirection, construct_type(Redirection, data))

    async def update(
        self,
        redirection_id: int,
        *,
        condition: _params.RedirectionConditionParam,
        name: str,
        params: _params.RedirectionParamsParam,
        redirection_type_id: int,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> Redirection:
        """
        Update redirection.

        Replaces the redirection rule; the body is checked as on create.

        Args:
          redirection_id: Identifier in the path

        Error codes (``error_message``): REQUEST_VALIDATION_EXCEPTION, REDIRECTION_NOT_FOUND_EXCEPTION,
        PARAMS_NOT_VALID_EXCEPTION, CONDITION_NOT_VALID_EXCEPTION, DONGLE_NOT_FOUND,
        BILLING_ERROR_IDENTIFIER_DONGLE_SUBSCRIPTION_NOT_ACTIVE.
        """
        data = await self._client._request(
            "PUT",
            f"/redirection/{path_param(redirection_id)}",
            body={"condition": condition, "name": name, "params": params, "redirection_type_id": redirection_type_id},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return cast(Redirection, construct_type(Redirection, data))

    async def delete(
        self,
        redirection_id: int,
        *,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> bool:
        """
        Delete redirection.

        Deletes the redirection rule.

        Args:
          redirection_id: Identifier in the path

        Error codes (``error_message``): REQUEST_VALIDATION_EXCEPTION, REDIRECTION_NOT_FOUND_EXCEPTION.
        """
        data = await self._client._request(
            "DELETE",
            f"/redirection/{path_param(redirection_id)}",
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
        )
        return bool(isinstance(data, dict) and data.get("status"))
