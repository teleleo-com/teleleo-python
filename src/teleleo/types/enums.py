# File generated from spec/openapi.yaml by scripts/generate.py. Do not edit by hand.

from __future__ import annotations

import enum

__all__ = [
    "CallScenarioApplyStatus",
    "CallScenarioDeliveryError",
    "CallScenarioType",
    "CallStatus",
    "CallType",
    "DongleOnlineErrorCode",
    "DongleOnlineStatus",
    "DongleSignalQuality",
    "DurationPreset",
    "MailingEntityType",
    "MailingStatus",
    "MailingType",
    "RedirectionType",
    "SmsSourceType",
    "SmsStatus",
    "SmsType",
    "UssdStatus",
    "UssdType",
]


class CallScenarioApplyStatus(enum.IntEnum):
    """
    1: Pending (the dongle has not confirmed the current version yet), 2: Active (the dongle applied the
    current version; on firmware without apply reports, accepted it), 3: Not delivered (the current version is
    not on the dongle, see call_scenario_delivery_error_id), 4: Failed (the dongle could not apply it, see
    apply_error_code)
    """

    PENDING = 1
    """Pending (the dongle has not confirmed the current version yet)"""
    ACTIVE = 2
    """Active (the dongle applied the current version; on firmware without apply reports, accepted it)"""
    NOT_DELIVERED = 3
    """Not delivered (the current version is not on the dongle, see call_scenario_delivery_error_id)"""
    FAILED = 4
    """Failed (the dongle could not apply it, see apply_error_code)"""


class CallScenarioDeliveryError(enum.IntEnum):
    """
    1: Dongle unreachable (no answer; it may still have received the push), 2: Dongle busy (still applying the
    previous push), 3: Dongle rejected the scenario, 4: Subscription inactive (taken off the dongle until the
    subscription is renewed)
    """

    DONGLE_UNREACHABLE = 1
    """Dongle unreachable (no answer; it may still have received the push)"""
    DONGLE_BUSY = 2
    """Dongle busy (still applying the previous push)"""
    DONGLE_REJECTED_THE_SCENARIO = 3
    """Dongle rejected the scenario"""
    SUBSCRIPTION_INACTIVE = 4
    """Subscription inactive (taken off the dongle until the subscription is renewed)"""


class CallScenarioType(enum.IntEnum):
    """1: Dongle incoming simple"""

    DONGLE_INCOMING_SIMPLE = 1
    """Dongle incoming simple"""


class CallStatus(enum.IntEnum):
    """1: Created, 2: Enqueued, 3: Sent, 4: Received (answered), 5: Not received, 6: Canceled, 7: Missed"""

    CREATED = 1
    """Created"""
    ENQUEUED = 2
    """Enqueued"""
    SENT = 3
    """Sent"""
    RECEIVED = 4
    """Received (answered)"""
    NOT_RECEIVED = 5
    """Not received"""
    CANCELED = 6
    """Canceled"""
    MISSED = 7
    """Missed"""


class CallType(enum.IntEnum):
    """1: Outgoing, 2: Incoming, 3: Robotics incoming, 4: Robotics outgoing"""

    OUTGOING = 1
    """Outgoing"""
    INCOMING = 2
    """Incoming"""
    ROBOTICS_INCOMING = 3
    """Robotics incoming"""
    ROBOTICS_OUTGOING = 4
    """Robotics outgoing"""


class DongleOnlineErrorCode(enum.IntEnum):
    """1: Phone determination error, 2: Timeout error, 3: Unexpected error, 4: Health check failed error"""

    PHONE_DETERMINATION_ERROR = 1
    """Phone determination error"""
    TIMEOUT_ERROR = 2
    """Timeout error"""
    UNEXPECTED_ERROR = 3
    """Unexpected error"""
    HEALTH_CHECK_FAILED_ERROR = 4
    """Health check failed error"""


class DongleOnlineStatus(enum.IntEnum):
    """
    1: Offline, 2: Online processing (connecting), 3: Error (see dongle_online_error_code_id), 4: Manual phone
    determination, 5: Online, 6: Updating, 7: Rebooting (set at once by POST /dongle/{dongle_id}/reboot)
    """

    OFFLINE = 1
    """Offline"""
    ONLINE_PROCESSING = 2
    """Online processing (connecting)"""
    ERROR = 3
    """Error (see dongle_online_error_code_id)"""
    MANUAL_PHONE_DETERMINATION = 4
    """Manual phone determination"""
    ONLINE = 5
    """Online"""
    UPDATING = 6
    """Updating"""
    REBOOTING = 7
    """Rebooting (set at once by POST /dongle/{dongle_id}/reboot)"""


class DongleSignalQuality(enum.IntEnum):
    """1: Bad, 2: Medium, 3: Good"""

    BAD = 1
    """Bad"""
    MEDIUM = 2
    """Medium"""
    GOOD = 3
    """Good"""


class DurationPreset(enum.IntEnum):
    """1: Less than 1 minute, 2: 1-3 minutes, 3: 3-5 minutes, 4: More than 5 minutes"""

    LESS_THAN_1_MINUTE = 1
    """Less than 1 minute"""
    FROM_1_TO_3_MINUTES = 2
    """1-3 minutes"""
    FROM_3_TO_5_MINUTES = 3
    """3-5 minutes"""
    MORE_THAN_5_MINUTES = 4
    """More than 5 minutes"""


class MailingEntityType(enum.IntEnum):
    """1: Sms, 2: Call"""

    SMS = 1
    """Sms"""
    CALL = 2
    """Call"""


class MailingStatus(enum.IntEnum):
    """1: Draft, 2: Planned, 3: In process, 4: Ended, 5: Canceled"""

    DRAFT = 1
    """Draft"""
    PLANNED = 2
    """Planned"""
    IN_PROCESS = 3
    """In process"""
    ENDED = 4
    """Ended"""
    CANCELED = 5
    """Canceled"""


class MailingType(enum.IntEnum):
    """1: Simple (sent at once), 2: Delayed (sent at scheduled_at)"""

    SIMPLE = 1
    """Simple (sent at once)"""
    DELAYED = 2
    """Delayed (sent at scheduled_at)"""


class RedirectionType(enum.IntEnum):
    """1: Sms, 2: Call, 3: Auto reply, 4: Silent, 5: Http"""

    SMS = 1
    """Sms"""
    CALL = 2
    """Call"""
    AUTO_REPLY = 3
    """Auto reply"""
    SILENT = 4
    """Silent"""
    HTTP = 5
    """Http"""


class SmsSourceType(enum.IntEnum):
    """1: Local, 2: International, 3: Short (short code or alphanumeric sender)"""

    LOCAL = 1
    """Local"""
    INTERNATIONAL = 2
    """International"""
    SHORT = 3
    """Short (short code or alphanumeric sender)"""


class SmsStatus(enum.IntEnum):
    """
    1: Sended - accepted by the mobile network (about a second after creation), not delivered to the handset;
    2: Received (incoming); 3: Not received - the network refused it; 4: Created; 5: Enqueued; 6: Canceled; 7:
    Incoming incomplete - not every part of a multipart SMS arrived
    """

    SENT = 1
    """Sended - accepted by the mobile network (about a second after creation), not delivered to the handset"""
    RECEIVED = 2
    """Received (incoming)"""
    NOT_RECEIVED = 3
    """Not received - the network refused it"""
    CREATED = 4
    """Created"""
    ENQUEUED = 5
    """Enqueued"""
    CANCELED = 6
    """Canceled"""
    INCOMING_INCOMPLETE = 7
    """Incoming incomplete - not every part of a multipart SMS arrived"""


class SmsType(enum.IntEnum):
    """1: Outgoing, 2: Incoming, 3: Auto reply, 4: Reply, 5: Delayed (scheduled), 6: Mailing, 7: Silent"""

    OUTGOING = 1
    """Outgoing"""
    INCOMING = 2
    """Incoming"""
    AUTO_REPLY = 3
    """Auto reply"""
    REPLY = 4
    """Reply"""
    DELAYED = 5
    """Delayed (scheduled)"""
    MAILING = 6
    """Mailing"""
    SILENT = 7
    """Silent"""


class UssdStatus(enum.IntEnum):
    """1: Created, 2: Sending, 3: Success, 4: Error"""

    CREATED = 1
    """Created"""
    SENDING = 2
    """Sending"""
    SUCCESS = 3
    """Success"""
    ERROR = 4
    """Error"""


class UssdType(enum.IntEnum):
    """1: Incoming, 2: Outgoing"""

    INCOMING = 1
    """Incoming"""
    OUTGOING = 2
    """Outgoing"""
