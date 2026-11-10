# File generated from spec/openapi.yaml by scripts/generate.py. Do not edit by hand.

from __future__ import annotations

from typing import Iterable, Optional, Union, cast

from typing_extensions import Literal

from .._models import construct_type
from .._pagination import AsyncPage, SyncPage
from .._resource import AsyncAPIResource, SyncAPIResource
from .._types import NOT_GIVEN, Body, Headers, NotGiven, Query, Timeout
from .._utils import path_param
from ..types import ContactGroup

__all__ = ["ContactGroupsResource", "AsyncContactGroupsResource"]


class ContactGroupsResource(SyncAPIResource):
    """Groups of contacts, used by mailings, call scenarios and redirections."""

    def list(
        self,
        *,
        contact_group_ids: Union[Iterable[int], NotGiven] = NOT_GIVEN,
        contact_ids: Union[Iterable[int], NotGiven] = NOT_GIVEN,
        name: Union[str, NotGiven] = NOT_GIVEN,
        page: Union[int, NotGiven] = NOT_GIVEN,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        order_by: Union[str, NotGiven] = NOT_GIVEN,
        order: Union[Literal["asc", "desc"], NotGiven] = NOT_GIVEN,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> SyncPage[ContactGroup]:
        """
        List contact groups.

        Contact groups of the account. Newest first by default (the id descending).

        Args:
          contact_group_ids: Array of integers representing contact groups IDs
          contact_ids: Array of integers representing contact IDs
          name: Filter by a fragment of the name, case-insensitive.
          page: Page number, 0-based.
          limit: Number of items per page, 1 to 1000.
          order_by: Attribute to sort by, sent together with order. One of: contactGroupId, name.
          order: Sort direction, sent together with order_by. Without order_by and order the list is newest first:
                the id descending.

        Error codes (``error_message``): REQUEST_VALIDATION_EXCEPTION.
        """
        return self._client._get_page(
            "/contact-group",
            query={
                "contact_group_ids[]": contact_group_ids,
                "contact_ids[]": contact_ids,
                "name": name,
                "page": page,
                "limit": limit,
                "order_by": order_by,
                "order": order,
            },
            item_key="contact_groups",
            item_type=ContactGroup,
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
        )

    def create(
        self,
        *,
        name: str,
        contact_ids: Iterable[int],
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> ContactGroup:
        """
        Create contact group.

        Creates a contact group with the given contacts.

        Args:
          contact_ids: Contacts of the group; send an empty array for none. Replaces the current set on update.

        Error codes (``error_message``): REQUEST_VALIDATION_EXCEPTION,
        CONTACT_GROUP_ERROR_WITH_SAME_NAME_ALREADY_EXIST, CONTACT_GROUP_ERROR_INVALID_CONTACT.
        """
        data = self._client._request(
            "POST",
            "/contact-group",
            body={"name": name, "contact_ids": contact_ids},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return cast(ContactGroup, construct_type(ContactGroup, data))

    def get(
        self,
        contact_group_id: int,
        *,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> ContactGroup:
        """
        Get contact group.

        One contact group of the account.

        Args:
          contact_group_id: Identifier in the path

        Error codes (``error_message``): REQUEST_VALIDATION_EXCEPTION, CONTACT_GROUP_NOT_FOUND_EXCEPTION.
        """
        data = self._client._request(
            "GET",
            f"/contact-group/{path_param(contact_group_id)}",
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
        )
        return cast(ContactGroup, construct_type(ContactGroup, data))

    def update(
        self,
        contact_group_id: int,
        *,
        name: str,
        contact_ids: Iterable[int],
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> ContactGroup:
        """
        Update contact group.

        Replaces the group: name and the set of contacts are written as sent.

        Args:
          contact_group_id: Identifier in the path
          contact_ids: Contacts of the group; send an empty array for none. Replaces the current set on update.

        Error codes (``error_message``): REQUEST_VALIDATION_EXCEPTION, CONTACT_GROUP_NOT_FOUND_EXCEPTION,
        CONTACT_GROUP_ERROR_WITH_SAME_NAME_ALREADY_EXIST, CONTACT_GROUP_ERROR_INVALID_CONTACT.
        """
        data = self._client._request(
            "PUT",
            f"/contact-group/{path_param(contact_group_id)}",
            body={"name": name, "contact_ids": contact_ids},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return cast(ContactGroup, construct_type(ContactGroup, data))

    def delete(
        self,
        contact_group_id: int,
        *,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> bool:
        """
        Delete contact group.

        Deletes the contact group.

        Args:
          contact_group_id: Identifier in the path

        Error codes (``error_message``): REQUEST_VALIDATION_EXCEPTION, CONTACT_GROUP_NOT_FOUND_EXCEPTION,
        CONTACT_GROUP_ERROR_REDIRECTS_ARE_PRESENT_WHILE_DELETING_CONTACT_GROUP,
        CONTACT_GROUP_ERROR_MAILINGS_ARE_PRESENT_WHILE_DELETING_CONTACT_GROUP.
        """
        data = self._client._request(
            "DELETE",
            f"/contact-group/{path_param(contact_group_id)}",
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
        )
        return bool(isinstance(data, dict) and data.get("status"))


class AsyncContactGroupsResource(AsyncAPIResource):
    """Groups of contacts, used by mailings, call scenarios and redirections."""

    async def list(
        self,
        *,
        contact_group_ids: Union[Iterable[int], NotGiven] = NOT_GIVEN,
        contact_ids: Union[Iterable[int], NotGiven] = NOT_GIVEN,
        name: Union[str, NotGiven] = NOT_GIVEN,
        page: Union[int, NotGiven] = NOT_GIVEN,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        order_by: Union[str, NotGiven] = NOT_GIVEN,
        order: Union[Literal["asc", "desc"], NotGiven] = NOT_GIVEN,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> AsyncPage[ContactGroup]:
        """
        List contact groups.

        Contact groups of the account. Newest first by default (the id descending).

        Args:
          contact_group_ids: Array of integers representing contact groups IDs
          contact_ids: Array of integers representing contact IDs
          name: Filter by a fragment of the name, case-insensitive.
          page: Page number, 0-based.
          limit: Number of items per page, 1 to 1000.
          order_by: Attribute to sort by, sent together with order. One of: contactGroupId, name.
          order: Sort direction, sent together with order_by. Without order_by and order the list is newest first:
                the id descending.

        Error codes (``error_message``): REQUEST_VALIDATION_EXCEPTION.
        """
        return await self._client._get_page(
            "/contact-group",
            query={
                "contact_group_ids[]": contact_group_ids,
                "contact_ids[]": contact_ids,
                "name": name,
                "page": page,
                "limit": limit,
                "order_by": order_by,
                "order": order,
            },
            item_key="contact_groups",
            item_type=ContactGroup,
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
        )

    async def create(
        self,
        *,
        name: str,
        contact_ids: Iterable[int],
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> ContactGroup:
        """
        Create contact group.

        Creates a contact group with the given contacts.

        Args:
          contact_ids: Contacts of the group; send an empty array for none. Replaces the current set on update.

        Error codes (``error_message``): REQUEST_VALIDATION_EXCEPTION,
        CONTACT_GROUP_ERROR_WITH_SAME_NAME_ALREADY_EXIST, CONTACT_GROUP_ERROR_INVALID_CONTACT.
        """
        data = await self._client._request(
            "POST",
            "/contact-group",
            body={"name": name, "contact_ids": contact_ids},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return cast(ContactGroup, construct_type(ContactGroup, data))

    async def get(
        self,
        contact_group_id: int,
        *,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> ContactGroup:
        """
        Get contact group.

        One contact group of the account.

        Args:
          contact_group_id: Identifier in the path

        Error codes (``error_message``): REQUEST_VALIDATION_EXCEPTION, CONTACT_GROUP_NOT_FOUND_EXCEPTION.
        """
        data = await self._client._request(
            "GET",
            f"/contact-group/{path_param(contact_group_id)}",
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
        )
        return cast(ContactGroup, construct_type(ContactGroup, data))

    async def update(
        self,
        contact_group_id: int,
        *,
        name: str,
        contact_ids: Iterable[int],
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> ContactGroup:
        """
        Update contact group.

        Replaces the group: name and the set of contacts are written as sent.

        Args:
          contact_group_id: Identifier in the path
          contact_ids: Contacts of the group; send an empty array for none. Replaces the current set on update.

        Error codes (``error_message``): REQUEST_VALIDATION_EXCEPTION, CONTACT_GROUP_NOT_FOUND_EXCEPTION,
        CONTACT_GROUP_ERROR_WITH_SAME_NAME_ALREADY_EXIST, CONTACT_GROUP_ERROR_INVALID_CONTACT.
        """
        data = await self._client._request(
            "PUT",
            f"/contact-group/{path_param(contact_group_id)}",
            body={"name": name, "contact_ids": contact_ids},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return cast(ContactGroup, construct_type(ContactGroup, data))

    async def delete(
        self,
        contact_group_id: int,
        *,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> bool:
        """
        Delete contact group.

        Deletes the contact group.

        Args:
          contact_group_id: Identifier in the path

        Error codes (``error_message``): REQUEST_VALIDATION_EXCEPTION, CONTACT_GROUP_NOT_FOUND_EXCEPTION,
        CONTACT_GROUP_ERROR_REDIRECTS_ARE_PRESENT_WHILE_DELETING_CONTACT_GROUP,
        CONTACT_GROUP_ERROR_MAILINGS_ARE_PRESENT_WHILE_DELETING_CONTACT_GROUP.
        """
        data = await self._client._request(
            "DELETE",
            f"/contact-group/{path_param(contact_group_id)}",
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
        )
        return bool(isinstance(data, dict) and data.get("status"))
