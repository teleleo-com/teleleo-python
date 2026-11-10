from __future__ import annotations

from typing import List, Optional

import httpx

__all__ = [
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
]


class TeleleoError(Exception):
    """Base class for every error raised by this library."""


class APIError(TeleleoError):
    """An error that happened while talking to the API."""

    message: str
    request: httpx.Request
    body: object
    """The decoded body of the answer, if there was one."""

    def __init__(self, message: str, request: httpx.Request, *, body: object = None) -> None:
        super().__init__(message)
        self.message = message
        self.request = request
        self.body = body


class APIConnectionError(APIError):
    """The API could not be reached."""

    def __init__(self, *, request: httpx.Request, message: str = "Connection error.") -> None:
        super().__init__(message, request)


class APITimeoutError(APIConnectionError):
    """The request timed out."""

    def __init__(self, request: httpx.Request) -> None:
        super().__init__(request=request, message="Request timed out.")


class APIResponseValidationError(APIError):
    """The API answered with a success status, but the body is not the JSON the library expects."""

    response: httpx.Response
    status_code: int

    def __init__(self, response: httpx.Response, *, message: str) -> None:
        super().__init__(message, response.request, body=response.text)
        self.response = response
        self.status_code = response.status_code


class APIStatusError(APIError):
    """The API answered with a 4xx or 5xx status."""

    response: httpx.Response
    status_code: int
    error_message: Optional[str]
    """Machine-readable error code from the answer, for example ``DONGLE_ERROR_DONGLE_NOT_FOUND``. Act on this."""
    error_details: List[str]
    """Human-readable details; may be empty."""
    request_id: Optional[str]
    """Quote it to Teleleo support."""

    def __init__(
        self,
        message: str,
        *,
        response: httpx.Response,
        body: object,
        error_message: Optional[str],
        error_details: List[str],
        request_id: Optional[str],
    ) -> None:
        super().__init__(message, response.request, body=body)
        self.response = response
        self.status_code = response.status_code
        self.error_message = error_message
        self.error_details = error_details
        self.request_id = request_id


class BadRequestError(APIStatusError):
    """400: the request is invalid."""


class AuthenticationError(APIStatusError):
    """401: the API key is missing or unknown, or the account is not active."""


class PermissionDeniedError(APIStatusError):
    """403: the request is outside the public API, or a field is not allowed."""


class NotFoundError(APIStatusError):
    """The object or path does not exist.

    API v1 answers 400 with an ``error_message`` that contains ``NOT_FOUND`` for a missing object, and 404 for an
    unknown path. Both raise this error; ``status_code`` keeps the real status.
    """


class ConflictError(APIStatusError):
    """409: the request conflicts with the current state."""


class RateLimitError(APIStatusError):
    """429: too many requests."""


class InternalServerError(APIStatusError):
    """5xx: a failure on the Teleleo side. Retry later and quote ``request_id`` if it persists."""


def _parse_error(response: httpx.Response) -> tuple[object, Optional[str], List[str], Optional[str]]:
    body: object
    try:
        body = response.json()
    except ValueError:
        body = response.text or None

    error_message: Optional[str] = None
    details: List[str] = []
    request_id: Optional[str] = None
    if isinstance(body, dict):
        value = body.get("error_message")
        if isinstance(value, str) and value:
            error_message = value
        elif isinstance(body.get("code"), str):
            error_message = body["code"]
        for key in ("error_details", "error_message_detail"):
            raw = body.get(key)
            if isinstance(raw, list) and raw:
                details = [str(item) for item in raw]
                break
            if isinstance(raw, str) and raw:
                details = [raw]
                break
        rid = body.get("request_id")
        if rid:
            request_id = str(rid)
    elif isinstance(body, str) and body.strip() and not body.lstrip().startswith("<"):
        details = [body.strip()[:500]]
    if request_id is None:
        request_id = response.headers.get("x-request-id")
    return body, error_message, details, request_id


def make_status_error(response: httpx.Response) -> APIStatusError:
    body, error_message, details, request_id = _parse_error(response)
    status = response.status_code

    message = f"Error code: {status}"
    if error_message:
        message += f" - {error_message}"
    if details:
        message += f": {'; '.join(details)}"
    if request_id:
        message += f" (request_id: {request_id})"

    cls: type[APIStatusError]
    if status == 404 or (status == 400 and error_message is not None and "NOT_FOUND" in error_message):
        cls = NotFoundError
    elif status == 400:
        cls = BadRequestError
    elif status == 401:
        cls = AuthenticationError
    elif status == 403:
        cls = PermissionDeniedError
    elif status == 409:
        cls = ConflictError
    elif status == 429:
        cls = RateLimitError
    elif status >= 500:
        cls = InternalServerError
    else:
        cls = APIStatusError
    return cls(
        message,
        response=response,
        body=body,
        error_message=error_message,
        error_details=details,
        request_id=request_id,
    )
