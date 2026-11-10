# File generated from spec/openapi.yaml by scripts/generate.py. Do not edit by hand.

from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING, Any, cast

from .call_scenarios import AsyncCallScenariosResource, CallScenariosResource
from .calls import AsyncCallsResource, CallsResource
from .contact_groups import AsyncContactGroupsResource, ContactGroupsResource
from .contacts import AsyncContactsResource, ContactsResource
from .dongles import AsyncDonglesResource, DonglesResource
from .files import AsyncFilesResource, FilesResource
from .follow_up_sms_settings import AsyncFollowUpSmsSettingsResource, FollowUpSmsSettingsResource
from .mailings import AsyncMailingsResource, MailingsResource
from .public_vpn import AsyncPublicVpnResource, PublicVpnResource
from .redirections import AsyncRedirectionsResource, RedirectionsResource
from .sip_users import AsyncSipUsersResource, SipUsersResource
from .sms import AsyncSmsResource, SmsResource
from .socks_proxies import AsyncSocksProxiesResource, SocksProxiesResource
from .ussd import AsyncUssdResource, UssdResource

if TYPE_CHECKING:
    from .._base_client import AsyncAPIClient, SyncAPIClient

__all__ = [
    "SyncResources",
    "AsyncResources",
    "DonglesResource",
    "AsyncDonglesResource",
    "SmsResource",
    "AsyncSmsResource",
    "CallsResource",
    "AsyncCallsResource",
    "UssdResource",
    "AsyncUssdResource",
    "ContactsResource",
    "AsyncContactsResource",
    "ContactGroupsResource",
    "AsyncContactGroupsResource",
    "MailingsResource",
    "AsyncMailingsResource",
    "RedirectionsResource",
    "AsyncRedirectionsResource",
    "CallScenariosResource",
    "AsyncCallScenariosResource",
    "FollowUpSmsSettingsResource",
    "AsyncFollowUpSmsSettingsResource",
    "PublicVpnResource",
    "AsyncPublicVpnResource",
    "SocksProxiesResource",
    "AsyncSocksProxiesResource",
    "SipUsersResource",
    "AsyncSipUsersResource",
    "FilesResource",
    "AsyncFilesResource",
]


class SyncResources:
    """Resource groups of the client."""

    @cached_property
    def dongles(self) -> DonglesResource:
        """Modems of the account and their commands: reboot, Wi-Fi, Wi-Fi extender, number, network info."""
        return DonglesResource(cast("SyncAPIClient", cast(Any, self)))

    @cached_property
    def sms(self) -> SmsResource:
        """SMS of the modems: history, sending, replies, threads."""
        return SmsResource(cast("SyncAPIClient", cast(Any, self)))

    @cached_property
    def calls(self) -> CallsResource:
        """Calls of the modems: history, outgoing calls."""
        return CallsResource(cast("SyncAPIClient", cast(Any, self)))

    @cached_property
    def ussd(self) -> UssdResource:
        """USSD requests through a modem."""
        return UssdResource(cast("SyncAPIClient", cast(Any, self)))

    @cached_property
    def contacts(self) -> ContactsResource:
        """Address book of the account."""
        return ContactsResource(cast("SyncAPIClient", cast(Any, self)))

    @cached_property
    def contact_groups(self) -> ContactGroupsResource:
        """Groups of contacts, used by mailings, call scenarios and redirections."""
        return ContactGroupsResource(cast("SyncAPIClient", cast(Any, self)))

    @cached_property
    def mailings(self) -> MailingsResource:
        """Bulk SMS and call campaigns."""
        return MailingsResource(cast("SyncAPIClient", cast(Any, self)))

    @cached_property
    def redirections(self) -> RedirectionsResource:
        """Rules for incoming SMS and calls: forwarding, auto reply, HTTP callback."""
        return RedirectionsResource(cast("SyncAPIClient", cast(Any, self)))

    @cached_property
    def call_scenarios(self) -> CallScenariosResource:
        """What a modem plays to incoming callers."""
        return CallScenariosResource(cast("SyncAPIClient", cast(Any, self)))

    @cached_property
    def follow_up_sms_settings(self) -> FollowUpSmsSettingsResource:
        """SMS a modem sends to a caller after a call."""
        return FollowUpSmsSettingsResource(cast("SyncAPIClient", cast(Any, self)))

    @cached_property
    def public_vpn(self) -> PublicVpnResource:
        """VPN access through a modem."""
        return PublicVpnResource(cast("SyncAPIClient", cast(Any, self)))

    @cached_property
    def socks_proxies(self) -> SocksProxiesResource:
        """SOCKS5 proxy through the mobile network of a modem."""
        return SocksProxiesResource(cast("SyncAPIClient", cast(Any, self)))

    @cached_property
    def sip_users(self) -> SipUsersResource:
        """SIP accounts of the modems."""
        return SipUsersResource(cast("SyncAPIClient", cast(Any, self)))

    @cached_property
    def files(self) -> FilesResource:
        """Downloads, temporary audio uploads and text-to-speech."""
        return FilesResource(cast("SyncAPIClient", cast(Any, self)))


class AsyncResources:
    """Resource groups of the client."""

    @cached_property
    def dongles(self) -> AsyncDonglesResource:
        """Modems of the account and their commands: reboot, Wi-Fi, Wi-Fi extender, number, network info."""
        return AsyncDonglesResource(cast("AsyncAPIClient", cast(Any, self)))

    @cached_property
    def sms(self) -> AsyncSmsResource:
        """SMS of the modems: history, sending, replies, threads."""
        return AsyncSmsResource(cast("AsyncAPIClient", cast(Any, self)))

    @cached_property
    def calls(self) -> AsyncCallsResource:
        """Calls of the modems: history, outgoing calls."""
        return AsyncCallsResource(cast("AsyncAPIClient", cast(Any, self)))

    @cached_property
    def ussd(self) -> AsyncUssdResource:
        """USSD requests through a modem."""
        return AsyncUssdResource(cast("AsyncAPIClient", cast(Any, self)))

    @cached_property
    def contacts(self) -> AsyncContactsResource:
        """Address book of the account."""
        return AsyncContactsResource(cast("AsyncAPIClient", cast(Any, self)))

    @cached_property
    def contact_groups(self) -> AsyncContactGroupsResource:
        """Groups of contacts, used by mailings, call scenarios and redirections."""
        return AsyncContactGroupsResource(cast("AsyncAPIClient", cast(Any, self)))

    @cached_property
    def mailings(self) -> AsyncMailingsResource:
        """Bulk SMS and call campaigns."""
        return AsyncMailingsResource(cast("AsyncAPIClient", cast(Any, self)))

    @cached_property
    def redirections(self) -> AsyncRedirectionsResource:
        """Rules for incoming SMS and calls: forwarding, auto reply, HTTP callback."""
        return AsyncRedirectionsResource(cast("AsyncAPIClient", cast(Any, self)))

    @cached_property
    def call_scenarios(self) -> AsyncCallScenariosResource:
        """What a modem plays to incoming callers."""
        return AsyncCallScenariosResource(cast("AsyncAPIClient", cast(Any, self)))

    @cached_property
    def follow_up_sms_settings(self) -> AsyncFollowUpSmsSettingsResource:
        """SMS a modem sends to a caller after a call."""
        return AsyncFollowUpSmsSettingsResource(cast("AsyncAPIClient", cast(Any, self)))

    @cached_property
    def public_vpn(self) -> AsyncPublicVpnResource:
        """VPN access through a modem."""
        return AsyncPublicVpnResource(cast("AsyncAPIClient", cast(Any, self)))

    @cached_property
    def socks_proxies(self) -> AsyncSocksProxiesResource:
        """SOCKS5 proxy through the mobile network of a modem."""
        return AsyncSocksProxiesResource(cast("AsyncAPIClient", cast(Any, self)))

    @cached_property
    def sip_users(self) -> AsyncSipUsersResource:
        """SIP accounts of the modems."""
        return AsyncSipUsersResource(cast("AsyncAPIClient", cast(Any, self)))

    @cached_property
    def files(self) -> AsyncFilesResource:
        """Downloads, temporary audio uploads and text-to-speech."""
        return AsyncFilesResource(cast("AsyncAPIClient", cast(Any, self)))
