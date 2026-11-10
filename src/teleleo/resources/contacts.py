# File generated from spec/openapi.yaml by scripts/generate.py. Do not edit by hand.

from __future__ import annotations

from typing import Iterable, Optional, Union, cast

from typing_extensions import Literal

from .._models import construct_type
from .._pagination import AsyncPage, SyncPage
from .._resource import AsyncAPIResource, SyncAPIResource
from .._types import NOT_GIVEN, Body, Headers, NotGiven, Query, Timeout
from .._utils import path_param
from ..types import Contact, ContactImportResult
from ..types import params as _params

__all__ = ["ContactsResource", "AsyncContactsResource"]


class ContactsResource(SyncAPIResource):
    """Address book of the account."""

    def list(
        self,
        *,
        contact_group_ids: Union[Iterable[int], NotGiven] = NOT_GIVEN,
        contact_ids: Union[Iterable[int], NotGiven] = NOT_GIVEN,
        name: Union[str, NotGiven] = NOT_GIVEN,
        query: Union[str, NotGiven] = NOT_GIVEN,
        phone: Union[str, NotGiven] = NOT_GIVEN,
        email: Union[str, NotGiven] = NOT_GIVEN,
        phones: Union[Iterable[str], NotGiven] = NOT_GIVEN,
        page: Union[int, NotGiven] = NOT_GIVEN,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        order_by: Union[str, NotGiven] = NOT_GIVEN,
        order: Union[Literal["asc", "desc"], NotGiven] = NOT_GIVEN,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> SyncPage[Contact]:
        """
        List contacts.

        Contacts of the account. Filters combine with AND. Newest first by default (the id descending).

        Args:
          contact_group_ids: Array of integers representing contact groups IDs
          contact_ids: Array of integers representing contact IDs
          name: Filter by name
          query: Filter by query
          phone: Filter by phone
          email: Filter by a fragment of the email, case-insensitive.
          phones: Exact phone numbers.
          page: Page number, 0-based.
          limit: Number of items per page, 1 to 1000.
          order_by: Attribute to sort by, sent together with order. One of: contactId, name, phone, email.
          order: Sort direction, sent together with order_by. Without order_by and order the list is newest first:
                the id descending.

        Error codes (``error_message``): REQUEST_VALIDATION_EXCEPTION.
        """
        return self._client._get_page(
            "/contact",
            query={
                "contact_group_ids[]": contact_group_ids,
                "contact_ids[]": contact_ids,
                "name": name,
                "query": query,
                "phone": phone,
                "email": email,
                "phones[]": phones,
                "page": page,
                "limit": limit,
                "order_by": order_by,
                "order": order,
            },
            item_key="contacts",
            item_type=Contact,
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
        )

    def create(
        self,
        *,
        phone: str,
        name: Optional[str],
        contact_group_ids: Iterable[int],
        email: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> Contact:
        """
        Create contact.

        Creates a contact. The phone number is normalised to E.164; a number that already belongs to a contact
        of the account is refused.

        Args:
          name: Name of the contact; the key is required, the value may be null.
          contact_group_ids: Groups of the contact; send an empty array for none. Replaces the current set on
                update.

        Error codes (``error_message``): REQUEST_VALIDATION_EXCEPTION,
        CONTACT_ERROR_IDENTIFIER_INVALID_EMAIL_FORMAT, CONTACT_ERROR_IDENTIFIER_BIG_NAME,
        CONTACT_ERROR_IDENTIFIER_BIG_PHONE, CONTACT_ERROR_IDENTIFIER_INVALID_PHONE,
        CONTACT_ERROR_IDENTIFIER_ALREADY_EXISTS_SAME_NAME,
        CONTACT_ERROR_IDENTIFIER_ALREADY_EXISTS_SAME_NUMBER,
        CONTACT_MANAGEMENT_INVALID_CONTACT_GROUP_EXCEPTION.
        """
        data = self._client._request(
            "POST",
            "/contact",
            body={"phone": phone, "name": name, "email": email, "contact_group_ids": contact_group_ids},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return cast(Contact, construct_type(Contact, data))

    def get(
        self,
        contact_id: int,
        *,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> Contact:
        """
        Get contact.

        One contact of the account.

        Args:
          contact_id: Identifier in the path

        Error codes (``error_message``): REQUEST_VALIDATION_EXCEPTION, CONTACT_NOT_FOUND_EXCEPTION.
        """
        data = self._client._request(
            "GET",
            f"/contact/{path_param(contact_id)}",
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
        )
        return cast(Contact, construct_type(Contact, data))

    def update(
        self,
        contact_id: int,
        *,
        phone: str,
        name: Optional[str],
        contact_group_ids: Iterable[int],
        email: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> Contact:
        """
        Update contact.

        Replaces the contact: phone, name and the set of groups are written as sent.

        Args:
          contact_id: Identifier in the path
          name: Name of the contact; the key is required, the value may be null.
          contact_group_ids: Groups of the contact; send an empty array for none. Replaces the current set on
                update.

        Error codes (``error_message``): REQUEST_VALIDATION_EXCEPTION, CONTACT_NOT_FOUND_EXCEPTION,
        CONTACT_ERROR_IDENTIFIER_INVALID_EMAIL_FORMAT, CONTACT_ERROR_IDENTIFIER_BIG_NAME,
        CONTACT_ERROR_IDENTIFIER_BIG_PHONE, CONTACT_ERROR_IDENTIFIER_INVALID_PHONE,
        CONTACT_ERROR_IDENTIFIER_ALREADY_EXISTS_SAME_NAME,
        CONTACT_ERROR_IDENTIFIER_ALREADY_EXISTS_SAME_NUMBER,
        CONTACT_MANAGEMENT_INVALID_CONTACT_GROUP_EXCEPTION.
        """
        data = self._client._request(
            "PUT",
            f"/contact/{path_param(contact_id)}",
            body={"phone": phone, "name": name, "email": email, "contact_group_ids": contact_group_ids},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return cast(Contact, construct_type(Contact, data))

    def delete(
        self,
        contact_id: int,
        *,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> bool:
        """
        Delete contact.

        Deletes the contact.

        Args:
          contact_id: Identifier in the path

        Error codes (``error_message``): REQUEST_VALIDATION_EXCEPTION, CONTACT_NOT_FOUND_EXCEPTION,
        CONTACT_ERROR_REDIRECTS_ARE_PRESENT_WHILE_DELETING_CONTACT,
        CONTACT_ERROR_MAILINGS_ARE_PRESENT_WHILE_DELETING_CONTACT.
        """
        data = self._client._request(
            "DELETE",
            f"/contact/{path_param(contact_id)}",
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
        )
        return bool(isinstance(data, dict) and data.get("status"))

    def import_contacts(
        self,
        *,
        data: Iterable[_params.ImportContactRowParam],
        contact_group_id: Union[int, None, NotGiven] = NOT_GIVEN,
        contact_group_name: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> ContactImportResult:
        """
        Import contacts.

        Bulk creation of contacts from the body; duplicates by phone number are skipped.

        Args:
          data: List of contact rows; keys A/B/C are legacy Excel-column ids (A=name, B=phone, C=email)
          contact_group_id: Attach all imported contacts to this existing group
          contact_group_name: Create a new group with this name and attach imported contacts to it (ignored when
                contact_group_id is set)

        Error codes (``error_message``): REQUEST_VALIDATION_EXCEPTION,
        CONTACT_IMPORT_ERROR_IDENTIFIER_EMPTY_DATA, CONTACT_GROUP_ERROR_WITH_SAME_NAME_ALREADY_EXIST.
        """
        data = self._client._request(
            "POST",
            "/contact/import",
            body={"data": data, "contact_group_id": contact_group_id, "contact_group_name": contact_group_name},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return cast(ContactImportResult, construct_type(ContactImportResult, data))


class AsyncContactsResource(AsyncAPIResource):
    """Address book of the account."""

    async def list(
        self,
        *,
        contact_group_ids: Union[Iterable[int], NotGiven] = NOT_GIVEN,
        contact_ids: Union[Iterable[int], NotGiven] = NOT_GIVEN,
        name: Union[str, NotGiven] = NOT_GIVEN,
        query: Union[str, NotGiven] = NOT_GIVEN,
        phone: Union[str, NotGiven] = NOT_GIVEN,
        email: Union[str, NotGiven] = NOT_GIVEN,
        phones: Union[Iterable[str], NotGiven] = NOT_GIVEN,
        page: Union[int, NotGiven] = NOT_GIVEN,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        order_by: Union[str, NotGiven] = NOT_GIVEN,
        order: Union[Literal["asc", "desc"], NotGiven] = NOT_GIVEN,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> AsyncPage[Contact]:
        """
        List contacts.

        Contacts of the account. Filters combine with AND. Newest first by default (the id descending).

        Args:
          contact_group_ids: Array of integers representing contact groups IDs
          contact_ids: Array of integers representing contact IDs
          name: Filter by name
          query: Filter by query
          phone: Filter by phone
          email: Filter by a fragment of the email, case-insensitive.
          phones: Exact phone numbers.
          page: Page number, 0-based.
          limit: Number of items per page, 1 to 1000.
          order_by: Attribute to sort by, sent together with order. One of: contactId, name, phone, email.
          order: Sort direction, sent together with order_by. Without order_by and order the list is newest first:
                the id descending.

        Error codes (``error_message``): REQUEST_VALIDATION_EXCEPTION.
        """
        return await self._client._get_page(
            "/contact",
            query={
                "contact_group_ids[]": contact_group_ids,
                "contact_ids[]": contact_ids,
                "name": name,
                "query": query,
                "phone": phone,
                "email": email,
                "phones[]": phones,
                "page": page,
                "limit": limit,
                "order_by": order_by,
                "order": order,
            },
            item_key="contacts",
            item_type=Contact,
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
        )

    async def create(
        self,
        *,
        phone: str,
        name: Optional[str],
        contact_group_ids: Iterable[int],
        email: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> Contact:
        """
        Create contact.

        Creates a contact. The phone number is normalised to E.164; a number that already belongs to a contact
        of the account is refused.

        Args:
          name: Name of the contact; the key is required, the value may be null.
          contact_group_ids: Groups of the contact; send an empty array for none. Replaces the current set on
                update.

        Error codes (``error_message``): REQUEST_VALIDATION_EXCEPTION,
        CONTACT_ERROR_IDENTIFIER_INVALID_EMAIL_FORMAT, CONTACT_ERROR_IDENTIFIER_BIG_NAME,
        CONTACT_ERROR_IDENTIFIER_BIG_PHONE, CONTACT_ERROR_IDENTIFIER_INVALID_PHONE,
        CONTACT_ERROR_IDENTIFIER_ALREADY_EXISTS_SAME_NAME,
        CONTACT_ERROR_IDENTIFIER_ALREADY_EXISTS_SAME_NUMBER,
        CONTACT_MANAGEMENT_INVALID_CONTACT_GROUP_EXCEPTION.
        """
        data = await self._client._request(
            "POST",
            "/contact",
            body={"phone": phone, "name": name, "email": email, "contact_group_ids": contact_group_ids},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return cast(Contact, construct_type(Contact, data))

    async def get(
        self,
        contact_id: int,
        *,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> Contact:
        """
        Get contact.

        One contact of the account.

        Args:
          contact_id: Identifier in the path

        Error codes (``error_message``): REQUEST_VALIDATION_EXCEPTION, CONTACT_NOT_FOUND_EXCEPTION.
        """
        data = await self._client._request(
            "GET",
            f"/contact/{path_param(contact_id)}",
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
        )
        return cast(Contact, construct_type(Contact, data))

    async def update(
        self,
        contact_id: int,
        *,
        phone: str,
        name: Optional[str],
        contact_group_ids: Iterable[int],
        email: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> Contact:
        """
        Update contact.

        Replaces the contact: phone, name and the set of groups are written as sent.

        Args:
          contact_id: Identifier in the path
          name: Name of the contact; the key is required, the value may be null.
          contact_group_ids: Groups of the contact; send an empty array for none. Replaces the current set on
                update.

        Error codes (``error_message``): REQUEST_VALIDATION_EXCEPTION, CONTACT_NOT_FOUND_EXCEPTION,
        CONTACT_ERROR_IDENTIFIER_INVALID_EMAIL_FORMAT, CONTACT_ERROR_IDENTIFIER_BIG_NAME,
        CONTACT_ERROR_IDENTIFIER_BIG_PHONE, CONTACT_ERROR_IDENTIFIER_INVALID_PHONE,
        CONTACT_ERROR_IDENTIFIER_ALREADY_EXISTS_SAME_NAME,
        CONTACT_ERROR_IDENTIFIER_ALREADY_EXISTS_SAME_NUMBER,
        CONTACT_MANAGEMENT_INVALID_CONTACT_GROUP_EXCEPTION.
        """
        data = await self._client._request(
            "PUT",
            f"/contact/{path_param(contact_id)}",
            body={"phone": phone, "name": name, "email": email, "contact_group_ids": contact_group_ids},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return cast(Contact, construct_type(Contact, data))

    async def delete(
        self,
        contact_id: int,
        *,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> bool:
        """
        Delete contact.

        Deletes the contact.

        Args:
          contact_id: Identifier in the path

        Error codes (``error_message``): REQUEST_VALIDATION_EXCEPTION, CONTACT_NOT_FOUND_EXCEPTION,
        CONTACT_ERROR_REDIRECTS_ARE_PRESENT_WHILE_DELETING_CONTACT,
        CONTACT_ERROR_MAILINGS_ARE_PRESENT_WHILE_DELETING_CONTACT.
        """
        data = await self._client._request(
            "DELETE",
            f"/contact/{path_param(contact_id)}",
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
        )
        return bool(isinstance(data, dict) and data.get("status"))

    async def import_contacts(
        self,
        *,
        data: Iterable[_params.ImportContactRowParam],
        contact_group_id: Union[int, None, NotGiven] = NOT_GIVEN,
        contact_group_name: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> ContactImportResult:
        """
        Import contacts.

        Bulk creation of contacts from the body; duplicates by phone number are skipped.

        Args:
          data: List of contact rows; keys A/B/C are legacy Excel-column ids (A=name, B=phone, C=email)
          contact_group_id: Attach all imported contacts to this existing group
          contact_group_name: Create a new group with this name and attach imported contacts to it (ignored when
                contact_group_id is set)

        Error codes (``error_message``): REQUEST_VALIDATION_EXCEPTION,
        CONTACT_IMPORT_ERROR_IDENTIFIER_EMPTY_DATA, CONTACT_GROUP_ERROR_WITH_SAME_NAME_ALREADY_EXIST.
        """
        data = await self._client._request(
            "POST",
            "/contact/import",
            body={"data": data, "contact_group_id": contact_group_id, "contact_group_name": contact_group_name},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return cast(ContactImportResult, construct_type(ContactImportResult, data))
