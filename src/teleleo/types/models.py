# File generated from spec/openapi.yaml by scripts/generate.py. Do not edit by hand.

from __future__ import annotations

import datetime
from typing import Any, Dict, List, Optional

from .._models import BaseModel
from .enums import (
    CallScenarioApplyStatus,
    CallScenarioDeliveryError,
    CallScenarioType,
    CallStatus,
    CallType,
    DongleOnlineErrorCode,
    DongleOnlineStatus,
    DongleSignalQuality,
    MailingEntityType,
    MailingStatus,
    MailingType,
    RedirectionType,
    SmsSourceType,
    SmsStatus,
    SmsType,
    UssdStatus,
    UssdType,
)

__all__ = [
    "Call",
    "CallScenario",
    "CallScenarioFile",
    "CallScenarioPhone",
    "Contact",
    "ContactGroup",
    "ContactImportError",
    "ContactImportErrorContact",
    "ContactImportResult",
    "Dongle",
    "DongleBootstrapDongle",
    "DongleDongleSetting",
    "DongleListItem",
    "DongleListItemBootstrapDongle",
    "DongleListItemDongleSetting",
    "DongleListItemPublicVpnServer",
    "DongleNetworkInfo",
    "DonglePublicVpnServer",
    "DongleSimIdentifiers",
    "DongleSocksProxy",
    "DongleSocksProxyServer",
    "DongleStatistic",
    "FollowUpSmsSetting",
    "Mailing",
    "MailingHistory",
    "MailingPhone",
    "PbxSipConnection",
    "PbxSipUser",
    "PublicVpnSession",
    "Redirection",
    "RedirectionCondition",
    "RedirectionParams",
    "Sms",
    "SmsPdu",
    "SmsThread",
    "SmsThreadLastMessage",
    "TmpFile",
    "Ussd",
]


class Call(BaseModel):
    call_id: int

    dongle_id: int

    call_type_id: CallType

    number_caller: str

    number_receiver: str

    created_at: datetime.datetime
    """UTC, `YYYY-MM-DD HH:MM:SS[.ffffff]`."""

    updated_at: datetime.datetime
    """UTC, `YYYY-MM-DD HH:MM:SS[.ffffff]`."""

    call_status_id: CallStatus

    contact: Optional[Contact] = None
    """
    The contact whose phone is the other party of the call. Returned by GET /call only, and only when there is
    such a contact (the key is absent otherwise).
    """

    duration: Optional[int]

    file_id: Optional[int]

    call_scenario_file_id: Optional[int]

    external_id: Optional[str]

    sip_call_id: Optional[str]
    """SIP Call-ID of the call."""

    mailing_history_id: Optional[int]

    scheduled_at: Optional[datetime.datetime]
    """UTC, `YYYY-MM-DD HH:MM:SS[.ffffff]`."""

    sent_at: Optional[datetime.datetime]
    """When the call was placed; null until then. UTC, `YYYY-MM-DD HH:MM:SS[.ffffff]`."""

    dongle_name: str

    initial_contact_group_ids: Optional[List[int]]
    """Contact groups the other party belonged to when the call was made."""


class CallScenario(BaseModel):
    call_scenario_id: Optional[int] = None

    dongle_id: Optional[int] = None

    call_scenario_type_id: Optional[CallScenarioType] = None

    file_id: Optional[int] = None

    is_call_record: Optional[bool] = None

    is_deleted: Optional[bool] = None

    created_at: Optional[datetime.datetime] = None
    """UTC, `YYYY-MM-DD HH:MM:SS[.ffffff]`."""

    updated_at: Optional[datetime.datetime] = None
    """UTC, `YYYY-MM-DD HH:MM:SS[.ffffff]`."""

    call_scenario_phones: Optional[List[CallScenarioPhone]] = None

    file: Optional[CallScenarioFile] = None

    name: Optional[str] = None

    version_uuid: Optional[str] = None
    """Version of the scenario; changes with every edit"""

    call_scenario_apply_status_id: Optional[CallScenarioApplyStatus] = None

    call_scenario_delivery_error_id: Optional[CallScenarioDeliveryError] = None

    apply_error_code: Optional[int] = None
    """
    Error the dongle reported for the current version: 3001 generic error such as a failed download, 3002
    invalid url, 3003 file too large for the dongle, 3011 invalid wav
    """

    applied_at: Optional[datetime.datetime] = None
    """
    When the dongle last applied the scenario (on firmware without apply reports, accepted the push). UTC,
    `YYYY-MM-DD HH:MM:SS[.ffffff]`.
    """


class CallScenarioFile(BaseModel):
    cdn_url: Optional[str] = None


class CallScenarioPhone(BaseModel):
    call_scenario_phone_id: Optional[int] = None

    call_scenario_id: Optional[int] = None

    phone: Optional[str] = None


class Contact(BaseModel):
    contact_id: int

    user_id: int

    groups_count: Optional[int] = None
    """
    Number of groups of the contact. Returned by the /contact operations; absent in a contact nested in
    another object.
    """

    phone: str

    name: Optional[str]

    email: Optional[str]

    contact_groups: Optional[List[ContactGroup]] = None
    """
    Groups of the contact (without their contacts). Returned by the /contact operations; absent in a contact
    nested in another object.
    """


class ContactGroup(BaseModel):
    contact_group_id: int

    user_id: int

    name: str

    contacts_count: Optional[int] = None
    """
    Number of contacts of the group. Returned by the /contact-group operations; absent in a group nested in
    another object.
    """

    contacts: Optional[List[Contact]] = None
    """
    Contacts of the group (without their groups). Returned by the /contact-group operations; absent in a group
    nested in another object.
    """


class ContactImportError(BaseModel):
    contact: Optional[ContactImportErrorContact] = None

    error: Optional[str] = None
    """Error code from ContactManagementExceptionEnum or PG/validation message"""


class ContactImportErrorContact(BaseModel):
    name: Optional[str] = None

    phone: Optional[str] = None

    email: Optional[str] = None


class ContactImportResult(BaseModel):
    imported: Optional[int] = None
    """Number of successfully created contacts"""

    errors: Optional[List[ContactImportError]] = None
    """Rows that failed to import; main flow continues even if individual rows fail"""


class Dongle(BaseModel):
    """
    A modem. GET /dongle/{dongle_id} and PUT /dongle/{dongle_id} return every attribute plus the counters and
    bootstrap_dongle; GET /dongle returns the attributes and, in full mode, dongle_setting and
    public_vpn_server.
    """

    dongle_id: int

    bootstrap_dongle_id: int

    user_id: int

    name: str

    is_hotspot_enable: Optional[bool]

    hotspot_name: Optional[str]

    hotspot_password: Optional[str]
    """Password of the Wi-Fi hotspot of the modem."""

    number: Optional[str]

    is_deleted: bool

    created_at: datetime.datetime
    """UTC, `YYYY-MM-DD HH:MM:SS[.ffffff]`."""

    updated_at: datetime.datetime
    """UTC, `YYYY-MM-DD HH:MM:SS[.ffffff]`."""

    tariff_package_id: Optional[int]

    tariff_package_end: Optional[datetime.datetime]
    """UTC, `YYYY-MM-DD HH:MM:SS[.ffffff]`."""

    imsi: Optional[str]

    iccid: Optional[str]

    is_active: bool

    mcc: Optional[str]

    activated_at: Optional[datetime.datetime]
    """UTC, `YYYY-MM-DD HH:MM:SS[.ffffff]`."""

    daily_sms_limit: Optional[int]

    is_tariff_package_active: bool

    is_tariff_package_enabled: bool

    dongle_signal_quality_id: Optional[DongleSignalQuality]
    """1: Bad, 2: Medium, 3: Good. Null when not set."""

    is_send_report: bool

    dongle_call_type_id: int

    is_public_vpn_enabled: bool

    public_vpn_login: Optional[str]
    """IKEv2 login for public_vpn_server."""

    public_vpn_password: Optional[str]
    """
    IKEv2 password for public_vpn_server; POST /dongle/{dongle_id}/public-vpn/refresh-password replaces it and
    the new value is read here.
    """

    is_mute_incoming_call: bool

    is_trial: bool

    trial_end: Optional[datetime.datetime]
    """UTC, `YYYY-MM-DD HH:MM:SS[.ffffff]`."""

    dongle_online_error_code_id: Optional[DongleOnlineErrorCode]
    """
    1: Phone determination error, 2: Timeout error, 3: Unexpected error, 4: Health check failed error. Null
    when not set.
    """

    last_online_at: Optional[datetime.datetime]
    """UTC, `YYYY-MM-DD HH:MM:SS[.ffffff]`."""

    wifi_extender_ssid: Optional[str] = None
    """Network name of the Wi-Fi extender."""

    wifi_extender_password: Optional[str] = None
    """Password of the Wi-Fi extender network."""

    wifi_extender_mode: Optional[int] = None
    """
    Wi-Fi extender mode of the modem. Returned by the operations served by backend-api (GET /dongle, the
    nested dongle of mailings); the operations served by backend return the same value as
    dongle_wifi_extender_mode_id.
    """

    dongle_wifi_extender_mode_id: Optional[int] = None
    """
    Wi-Fi extender mode of the modem as GET /dongle/{dongle_id} and PUT /dongle/{dongle_id} return it (the
    column name); the operations served by backend-api return it as wifi_extender_mode.
    """

    dialplan_id: Optional[int] = None
    """FreeSWITCH dialplan of the modem."""

    is_wifi_extender_processing: Optional[bool] = None
    """True while a wifi extender enable/disable command is being processed by the modem."""

    dongle_setting: Optional[DongleDongleSetting] = None
    """
    Per-modem settings the client may see. Returned by GET /dongle only, and only in full mode: absent - not
    null - in is_short mode and when the modem has no settings.
    """

    public_vpn_endpoint: Optional[str] = None
    """Use public_vpn_server.address. Returned by GET /dongle only, in full mode."""

    public_vpn_server: Optional[DonglePublicVpnServer] = None
    """
    VPN gateway the client connects to with public_vpn_login and public_vpn_password, the same for every
    dongle. Returned by GET /dongle only, and only in full mode: absent - not null - in is_short mode.
    """

    dongle_online_status: Optional[DongleOnlineStatus] = None

    sms_outgoing: Optional[int] = None
    """Number of outgoing SMS of the modem. Returned by GET /dongle/{dongle_id} and PUT /dongle/{dongle_id} only."""

    sms_incoming: Optional[int] = None
    """Number of incoming SMS of the modem. Returned by GET /dongle/{dongle_id} and PUT /dongle/{dongle_id} only."""

    call_outgoing: Optional[int] = None
    """
    Number of outgoing calls of the modem. Returned by GET /dongle/{dongle_id} and PUT /dongle/{dongle_id}
    only.
    """

    call_incoming: Optional[int] = None
    """
    Number of incoming calls of the modem. Returned by GET /dongle/{dongle_id} and PUT /dongle/{dongle_id}
    only.
    """

    bootstrap_dongle: Optional[DongleBootstrapDongle] = None
    """Hardware identity of the modem. Returned by GET /dongle/{dongle_id} and PUT /dongle/{dongle_id} only."""


class DongleBootstrapDongle(BaseModel):
    """Hardware identity of the modem. Returned by GET /dongle/{dongle_id} and PUT /dongle/{dongle_id} only."""

    imei_manufacture: Optional[str] = None
    """IMEI as manufactured."""

    pbx_sip_user: Optional[str] = None
    """SIP login of the modem on the PBX."""


class DongleDongleSetting(BaseModel):
    """
    Per-modem settings the client may see. Returned by GET /dongle only, and only in full mode: absent - not
    null - in is_short mode and when the modem has no settings.
    """

    is_offline_notification_enabled: Optional[bool] = None
    """
    Email the owner when the modem goes offline. Written via PUT /dongle/{dongle_id}/setting/offline-
    notification.
    """


class DongleListItem(BaseModel):
    """
    Dongle item of GET /dongle. In short mode (is_short=true) only the required fields are returned; in full
    mode all fields (including sms/call counters, bootstrap_dongle and public_vpn_server) are present.
    """

    dongle_id: int

    bootstrap_dongle_id: Optional[int] = None

    user_id: Optional[int] = None

    name: str

    is_hotspot_enable: Optional[bool] = None

    hotspot_name: Optional[str] = None

    hotspot_password: Optional[str] = None

    number: Optional[str]

    is_deleted: Optional[bool] = None

    created_at: Optional[datetime.datetime] = None
    """UTC, `YYYY-MM-DD HH:MM:SS[.ffffff]`."""

    updated_at: Optional[datetime.datetime] = None
    """UTC, `YYYY-MM-DD HH:MM:SS[.ffffff]`."""

    tariff_package_id: Optional[int] = None

    tariff_package_end: Optional[datetime.datetime] = None
    """UTC, `YYYY-MM-DD HH:MM:SS[.ffffff]`."""

    imsi: Optional[str] = None

    iccid: Optional[str] = None

    is_active: Optional[bool] = None

    mcc: Optional[str] = None

    activated_at: Optional[datetime.datetime] = None
    """UTC, `YYYY-MM-DD HH:MM:SS[.ffffff]`."""

    daily_sms_limit: Optional[int] = None

    is_tariff_package_active: bool

    is_tariff_package_enabled: Optional[bool] = None

    dongle_signal_quality_id: Optional[DongleSignalQuality] = None
    """1: Bad, 2: Medium, 3: Good. Null when not set."""

    is_send_report: Optional[bool] = None

    dongle_call_type_id: int

    is_public_vpn_enabled: Optional[bool] = None

    public_vpn_login: Optional[str] = None

    public_vpn_password: Optional[str] = None

    is_mute_incoming_call: Optional[bool] = None

    is_trial: bool

    trial_end: Optional[datetime.datetime] = None
    """UTC, `YYYY-MM-DD HH:MM:SS[.ffffff]`."""

    dialplan_id: Optional[int] = None

    dongle_online_error_code_id: Optional[DongleOnlineErrorCode]
    """
    1: Phone determination error, 2: Timeout error, 3: Unexpected error, 4: Health check failed error. Null
    when not set.
    """

    last_online_at: Optional[datetime.datetime] = None
    """UTC, `YYYY-MM-DD HH:MM:SS[.ffffff]`."""

    wifi_extender_ssid: Optional[str] = None

    wifi_extender_password: Optional[str] = None

    dongle_wifi_extender_mode_id: Optional[int] = None

    dongle_online_status: Optional[DongleOnlineStatus]
    """
    1: Offline, 2: Online processing (connecting), 3: Error (see dongle_online_error_code_id), 4: Manual phone
    determination, 5: Online, 6: Updating, 7: Rebooting (set at once by POST /dongle/{dongle_id}/reboot). Null
    when not set.
    """

    is_wifi_extender_processing: bool

    sms_outgoing: Optional[int] = None

    sms_incoming: Optional[int] = None

    call_outgoing: Optional[int] = None

    call_incoming: Optional[int] = None

    bootstrap_dongle: Optional[DongleListItemBootstrapDongle] = None

    public_vpn_endpoint: Optional[str] = None
    """Use public_vpn_server.address."""

    public_vpn_server: Optional[DongleListItemPublicVpnServer] = None
    """
    VPN gateway the client connects to with public_vpn_login and public_vpn_password. The same for every
    dongle.
    """

    dongle_setting: Optional[DongleListItemDongleSetting] = None
    """Per-modem settings the client may see; absent when the modem has no settings."""


class DongleListItemBootstrapDongle(BaseModel):
    imei_manufacture: Optional[str] = None

    pbx_sip_user: Optional[str] = None
    """SIP login of the modem on the PBX."""


class DongleListItemDongleSetting(BaseModel):
    """Per-modem settings the client may see; absent when the modem has no settings."""

    is_offline_notification_enabled: Optional[bool] = None


class DongleListItemPublicVpnServer(BaseModel):
    """
    VPN gateway the client connects to with public_vpn_login and public_vpn_password. The same for every
    dongle.
    """

    type: str

    address: str

    remote_id: str
    """IKEv2 Remote ID: the identity the gateway presents."""


class DongleNetworkInfo(BaseModel):
    """Radio state reported by the modem. Signal fields that the current network type does not report are null."""

    sim_network_plmn: str

    sim_network_name: str

    current_network_plmn: str

    current_network_name: str

    is_roaming: bool

    network_type: str

    mcc: int

    mnc: int

    rsrp: Optional[int] = None

    rsrq: Optional[int] = None

    sinr: Optional[int] = None

    cid: Optional[int] = None

    ci: Optional[int] = None

    pci: Optional[int] = None

    rssi: Optional[int] = None

    tac: Optional[int] = None

    psc: Optional[int] = None

    lac: Optional[int] = None


class DonglePublicVpnServer(BaseModel):
    """
    VPN gateway the client connects to with public_vpn_login and public_vpn_password, the same for every
    dongle. Returned by GET /dongle only, and only in full mode: absent - not null - in is_short mode.
    """

    type: str

    address: str

    remote_id: str
    """IKEv2 Remote ID: the identity the gateway presents."""


class DongleSimIdentifiers(BaseModel):
    """Identifiers of the SIM card and the modem."""

    iccid: str

    imsi: str

    imei: str

    number: str
    """Phone number as the modem reports it; may be empty."""


class DongleSocksProxy(BaseModel):
    dongle_socks_proxy_id: int

    dongle_id: int

    login: str

    password: str

    allowed_ips: List[str]

    server: DongleSocksProxyServer
    """The SOCKS5 gateway the client connects to with login and password; the same for every proxy."""

    is_active: bool
    """
    The proxy accepts connections: true while the modem has an active subscription or trial. The credentials
    stay when it becomes false and work again once the subscription is active.
    """

    created_at: datetime.datetime
    """UTC, `YYYY-MM-DD HH:MM:SS[.ffffff]`."""

    updated_at: datetime.datetime
    """UTC, `YYYY-MM-DD HH:MM:SS[.ffffff]`."""


class DongleSocksProxyServer(BaseModel):
    """The SOCKS5 gateway the client connects to with login and password; the same for every proxy."""

    address: str

    port: int


class DongleStatistic(BaseModel):
    dongle_statistic_id: Optional[int] = None

    dongle_id: Optional[int] = None

    read: Optional[int] = None
    """Bytes received by the modem in the sample."""

    write: Optional[int] = None
    """Bytes sent by the modem in the sample."""

    time: Optional[datetime.datetime] = None
    """Moment of the sample, UTC, `YYYY-MM-DD HH:MM:SS[.ffffff]`."""


class FollowUpSmsSetting(BaseModel):
    follow_up_sms_setting_id: int

    dongle_id: int

    name: str

    text: str

    ringing_duration_timeout: Optional[int] = None

    call_duration_timeout: Optional[int] = None

    daily_sms_limit: Optional[int] = None


class Mailing(BaseModel):
    mailing_id: Optional[int] = None

    dongle_id: Optional[int] = None

    count_mailing_phones: Optional[int] = None

    mailing_type_id: Optional[MailingType] = None

    mailing_status_id: Optional[MailingStatus] = None

    mailing_entity_type_id: Optional[MailingEntityType] = None

    mailing_history: Optional[MailingHistory] = None
    """The last run of the mailing; null while it has not run."""

    name: Optional[str] = None

    is_deleted: Optional[bool] = None

    scheduled_at: Optional[datetime.datetime] = None
    """UTC, `YYYY-MM-DD HH:MM:SS[.ffffff]`."""

    created_at: Optional[datetime.datetime] = None
    """UTC, `YYYY-MM-DD HH:MM:SS[.ffffff]`."""

    updated_at: Optional[datetime.datetime] = None
    """UTC, `YYYY-MM-DD HH:MM:SS[.ffffff]`."""

    text: Optional[str] = None

    file_id: Optional[int] = None

    is_call_record: Optional[bool] = None

    user_id: Optional[int] = None

    contacts: Optional[List[Contact]] = None

    contact_groups: Optional[List[ContactGroup]] = None

    mailing_phones: Optional[List[MailingPhone]] = None

    dongle: Optional[Dongle] = None


class MailingHistory(BaseModel):
    mailing_history_id: Optional[int] = None

    mailing_id: Optional[int] = None

    created_at: Optional[datetime.datetime] = None
    """UTC, `YYYY-MM-DD HH:MM:SS[.ffffff]`."""

    updated_at: Optional[datetime.datetime] = None
    """UTC, `YYYY-MM-DD HH:MM:SS[.ffffff]`."""


class MailingPhone(BaseModel):
    mailing_phone_id: Optional[int] = None

    mailing_id: Optional[int] = None

    phone: Optional[str] = None


class PbxSipConnection(BaseModel):
    pbx_sip_url: Optional[str] = None

    pbx_sip_port: Optional[int] = None

    pbx_sip_protocol: Optional[str] = None


class PbxSipUser(BaseModel):
    pbx_sip_user_id: int

    user_id: int

    sip_login: str

    sip_password: str

    dialplan_id: Optional[int] = None

    dongle_id: Optional[int] = None
    """The modem of the SIP account; always set."""

    pbx_sip_connections: List[PbxSipConnection]


class PublicVpnSession(BaseModel):
    ip: str
    """Client address inside the VPN."""

    name: str
    """Name of the modem."""

    username: str
    """VPN login the session was opened with (public_vpn_login of the modem)."""

    dongle_id: int


class Redirection(BaseModel):
    redirection_id: Optional[int] = None

    user_id: Optional[int] = None

    redirection_type_id: Optional[RedirectionType] = None

    name: Optional[str] = None

    created_at: Optional[datetime.datetime] = None
    """UTC, `YYYY-MM-DD HH:MM:SS[.ffffff]`."""

    updated_at: Optional[datetime.datetime] = None
    """UTC, `YYYY-MM-DD HH:MM:SS[.ffffff]`."""

    condition: Optional[RedirectionCondition] = None

    params: Optional[RedirectionParams] = None


class RedirectionCondition(BaseModel):
    """
    When the redirection fires: one rule, checked against every incoming SMS (redirection types 1, 3, 4, 5) or
    incoming call (type 2) of the account.

    A rule is a JSON array. A comparison is `[operator, field, value]`; `["and", rule, rule, ...]` and `["or",
    rule, rule, ...]` combine rules. The top level is a single rule, usually `and`.

    Fields are the attributes of the event, prefixed by the object: `sms_<field>` (the SMS schema:
    `sms_number_caller`, `sms_contact_id`, `sms_initial_contact_group_ids`, `sms_sms_source_type_id`,
    `sms_message_decoded`, ...), `call_<field>` (the call: `call_number_caller`, `call_contact_id`,
    `call_initial_contact_group_ids`, ...), `dongle_<field>` (the modem that received it: `dongle_dongle_id`,
    `dongle_name`, ...) and `contact_<field>` (the contact of the sender, when there is one). A field the
    event does not have compares as null.

    Operators: `=`, `!=`, `<`, `>` (one value); `in`, `!in` (a list of values); `regexp`, `!regexp` (a PCRE
    with delimiters, for example `/^bank$/ui`); `like`, `!like` (case-insensitive substring);
    `intersect_source`, `!intersect_source` (a list field such as `sms_initial_contact_group_ids` shares a
    value with the list); `is_empty`, `!is_empty` (`[operator, field]`, no value).

    Checked on save (400 CONDITION_NOT_VALID_EXCEPTION unless said otherwise):
    - the rule must parse: not empty, a known operator, the right number and types of arguments;
    - `["in", "dongle_dongle_id", [ids]]` as a direct child of the top-level `and` limits the redirection to
    these modems (GET /redirection filters by it too); every id must be a modem of the account with an active
    tariff (400 DONGLE_NOT_FOUND for an unknown id or an id of another account, a tariff error otherwise).
    Without it the redirection applies to every modem;
    - a `regexp` inside an `or` that is a direct child of the top-level rule may only test `sms_number_caller`
    or `call_number_caller` and must be `/^<letters or digits>$/ui` (an alphanumeric sender name);
    - for an auto reply (type 3), every number of a `sms_number_caller` list that is a direct child of the
    top-level rule is a valid phone number in `+<digits>` form.
    """

    pass


class RedirectionParams(BaseModel):
    """
    What the redirection does. Required keys depend on redirection_type_id (400 PARAMS_NOT_VALID_EXCEPTION
    otherwise):
    - 1 (SMS) and 2 (call): at least one delivery target - a non-empty `email`, or at least one item in
    `emails` or `telegram_chat_ids`;
    - 3 (auto reply): `auto_reply_message`;
    - 4 (silent) and 5 (HTTP): `url`, an absolute URL.

    Other keys are stored as sent and returned as is.
    """

    email: Optional[str] = None
    """One e-mail address to deliver to (types 1 and 2)."""

    emails: Optional[List[str]] = None
    """E-mail addresses to deliver to (types 1 and 2); each must be a valid address."""

    telegram_chat_ids: Optional[List[str]] = None
    """
    Telegram chat ids to deliver to (types 1 and 2); digits with an optional leading minus, as a string or a
    number.
    """

    auto_reply_message: Optional[str] = None
    """Text of the reply SMS (type 3, required)."""

    forwarding_message: Optional[str] = None
    """Optional text stored with the redirection."""

    url: Optional[str] = None
    """URL that receives the event (types 4 and 5, required)."""


class Sms(BaseModel):
    sms_id: int

    dongle_id: int

    sms_type_id: SmsType

    sms_status_id: SmsStatus

    network_status_code: Optional[int]
    """Status code the mobile network reported for an outgoing SMS; null when none was reported."""

    sms_source_type_id: Optional[SmsSourceType]
    """1: Local, 2: International, 3: Short (short code or alphanumeric sender). Null when not set."""

    number_caller: str

    pdus: Optional[List[SmsPdu]]
    """
    Raw PDUs of the message as the modem received them, one item per part of a multipart SMS; null when the
    SMS was not received as PDUs.
    """

    initial_contact_group_ids: Optional[List[int]]
    """Contact groups the sender belonged to when the SMS was received."""

    number_receiver: str

    sms_center: Optional[str]

    sms_source_country_code: Optional[str]

    message_decoded: str

    callback_url: Optional[str]

    created_at: datetime.datetime
    """UTC, `YYYY-MM-DD HH:MM:SS[.ffffff]`."""

    updated_at: datetime.datetime
    """UTC, `YYYY-MM-DD HH:MM:SS[.ffffff]`."""

    scheduled_at: Optional[datetime.datetime]
    """UTC, `YYYY-MM-DD HH:MM:SS[.ffffff]`."""

    external_id: Optional[str]

    dongle_name: Optional[str] = None
    """Name of the modem. Returned by GET /sms and GET /dongle/{dongle_id}/sms only."""

    replied_to_sms_id: Optional[int]

    mailing_history_id: Optional[int]
    """The mailing run that sent this SMS; null for an SMS outside a mailing."""

    contact: Optional[Contact] = None
    """
    The contact whose phone is the other party of the SMS. Returned by GET /sms and GET
    /dongle/{dongle_id}/sms only, and only when there is such a contact (the key is absent otherwise).
    """

    replied_from_sms: Optional[Sms] = None
    """
    The reply sent to this SMS (the SMS whose replied_to_sms_id is this sms_id), null when there is none;
    without its own redirections, replied_from_sms, contact and dongle_name. Returned by GET /sms, GET
    /dongle/{dongle_id}/sms, GET /dongle/{dongle_id}/sms/{sms_id} and PUT /dongle/{dongle_id}/sms/{sms_id};
    absent in the answers of the sending operations.
    """

    redirections: Optional[List[Redirection]] = None
    """
    Redirection rules that fired on this SMS. Returned by GET /sms, GET /dongle/{dongle_id}/sms, GET
    /dongle/{dongle_id}/sms/{sms_id} and PUT /dongle/{dongle_id}/sms/{sms_id}; absent in the answers of the
    sending operations.
    """


class SmsPdu(BaseModel):
    pdu: str
    """PDU in hex."""

    length: Optional[int] = None
    """Present on SMS received before 2024-04."""

    time: Optional[int] = None
    """Unix time; present on SMS received before 2024-04."""


class SmsThread(BaseModel):
    dongle_id: int

    contact_number: str

    last_message: SmsThreadLastMessage


class SmsThreadLastMessage(BaseModel):
    sms_id: int

    preview: str

    created_at: datetime.datetime
    """UTC, `YYYY-MM-DD HH:MM:SS[.ffffff]`."""

    is_incoming: bool

    sms_status_id: int


class TmpFile(BaseModel):
    tmp_file_id: str
    """
    Temporary file id: `<2 hex>/<32 hex>/<file name>` (three segments with slashes). Read it with GET
    /file/tmp/{file_id}, attach it through tmp_file_id of a call scenario or a call mailing.
    """


class Ussd(BaseModel):
    ussd_id: Optional[int] = None

    dongle_id: Optional[int] = None

    ussd_status_id: Optional[UssdStatus] = None

    ussd_type_id: Optional[UssdType] = None

    command: Optional[str] = None

    response: Optional[str] = None

    external_id: Optional[str] = None

    raw_webhook_data: Optional[Dict[str, Any]] = None

    created_at: Optional[datetime.datetime] = None
    """UTC, `YYYY-MM-DD HH:MM:SS[.ffffff]`."""

    updated_at: Optional[datetime.datetime] = None
    """UTC, `YYYY-MM-DD HH:MM:SS[.ffffff]`."""


for _model in (
    Call,
    CallScenario,
    CallScenarioFile,
    CallScenarioPhone,
    Contact,
    ContactGroup,
    ContactImportError,
    ContactImportErrorContact,
    ContactImportResult,
    Dongle,
    DongleBootstrapDongle,
    DongleDongleSetting,
    DongleListItem,
    DongleListItemBootstrapDongle,
    DongleListItemDongleSetting,
    DongleListItemPublicVpnServer,
    DongleNetworkInfo,
    DonglePublicVpnServer,
    DongleSimIdentifiers,
    DongleSocksProxy,
    DongleSocksProxyServer,
    DongleStatistic,
    FollowUpSmsSetting,
    Mailing,
    MailingHistory,
    MailingPhone,
    PbxSipConnection,
    PbxSipUser,
    PublicVpnSession,
    Redirection,
    RedirectionCondition,
    RedirectionParams,
    Sms,
    SmsPdu,
    SmsThread,
    SmsThreadLastMessage,
    TmpFile,
    Ussd,
):
    _model.model_rebuild()
