"""The official Python library for the Teleleo API.

::

    from teleleo import Teleleo

    client = Teleleo()  # reads TELELEO_API_KEY
    for dongle in client.dongles.list():
        print(dongle.dongle_id, dongle.name)
"""

from . import types
from ._base_client import DEFAULT_BASE_URL, DEFAULT_MAX_RETRIES, DEFAULT_TIMEOUT
from ._client import AsyncTeleleo, Teleleo
from ._exceptions import (
    APIConnectionError,
    APIError,
    APIResponseValidationError,
    APIStatusError,
    APITimeoutError,
    AuthenticationError,
    BadRequestError,
    ConflictError,
    InternalServerError,
    NotFoundError,
    PermissionDeniedError,
    RateLimitError,
    TeleleoError,
)
from ._models import BaseModel
from ._pagination import AsyncPage, SyncPage
from ._types import NOT_GIVEN, NotGiven
from ._version import __version__

__all__ = [
    "Teleleo",
    "AsyncTeleleo",
    "types",
    "SyncPage",
    "AsyncPage",
    "BaseModel",
    "NOT_GIVEN",
    "NotGiven",
    "DEFAULT_BASE_URL",
    "DEFAULT_TIMEOUT",
    "DEFAULT_MAX_RETRIES",
    "TeleleoError",
    "APIError",
    "APIConnectionError",
    "APITimeoutError",
    "APIResponseValidationError",
    "APIStatusError",
    "BadRequestError",
    "AuthenticationError",
    "PermissionDeniedError",
    "NotFoundError",
    "ConflictError",
    "RateLimitError",
    "InternalServerError",
    "__version__",
]
