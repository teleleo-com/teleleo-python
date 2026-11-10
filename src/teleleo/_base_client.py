from __future__ import annotations

import asyncio
import email.utils
import random
import time
from typing import Any, Dict, List, Mapping, Optional, Tuple, Type, TypeVar, Union

import httpx

from ._exceptions import APIConnectionError, APIResponseValidationError, APITimeoutError, make_status_error
from ._models import construct_type
from ._pagination import AsyncPage, SyncPage
from ._types import NOT_GIVEN, Body, Headers, NotGiven, Query, Timeout
from ._utils import build_body, build_query
from ._version import __version__

__all__ = ["SyncAPIClient", "AsyncAPIClient", "DEFAULT_BASE_URL", "DEFAULT_TIMEOUT", "DEFAULT_MAX_RETRIES"]

DEFAULT_BASE_URL = "https://app.teleleo.com/react_api"
DEFAULT_TIMEOUT = httpx.Timeout(60.0, connect=10.0)
DEFAULT_MAX_RETRIES = 2

INITIAL_RETRY_DELAY = 0.5
MAX_RETRY_DELAY = 8.0
MAX_RETRY_AFTER = 60.0

_IDEMPOTENT_METHODS = frozenset({"GET", "HEAD", "OPTIONS", "PUT", "DELETE"})
# The server refused the request before acting on it: safe to repeat for any method.
_RETRY_ANY_METHOD = frozenset({429})
# The outcome is unknown: repeat only requests that are safe to repeat.
_RETRY_IDEMPOTENT = frozenset({408, 502, 503, 504})
# Nothing reached the server.
_NOT_SENT_ERRORS = (httpx.ConnectError, httpx.ConnectTimeout, httpx.PoolTimeout)

_T = TypeVar("_T")


def _clean_query(query: Optional[Mapping[str, object]]) -> Dict[str, Any]:
    out: Dict[str, Any] = {}
    for key, value in (query or {}).items():
        if value is None or isinstance(value, NotGiven):
            continue
        if not isinstance(value, (str, bytes, Mapping)) and hasattr(value, "__iter__"):
            value = list(value)  # a generator would be used up by the first page
        out[key] = value
    return out


class _BaseClient:
    api_key: str
    base_url: str
    timeout: Timeout
    max_retries: int

    def __init__(
        self,
        *,
        api_key: str,
        base_url: Union[str, httpx.URL],
        timeout: Timeout,
        max_retries: int,
        default_headers: Optional[Headers],
    ) -> None:
        self.api_key = api_key
        self.base_url = str(base_url).rstrip("/")
        self.timeout = timeout
        self.max_retries = max_retries
        self._custom_headers: Dict[str, str] = dict(default_headers or {})

    @property
    def default_headers(self) -> Dict[str, str]:
        return {
            "Accept": "application/json",
            "User-Agent": f"teleleo-python/{__version__}",
            "auth-key": self.api_key,
            **self._custom_headers,
        }

    def _prepare(
        self,
        query: Optional[Query],
        body: Optional[Body],
        extra_query: Optional[Query],
        extra_body: Optional[Body],
    ) -> Tuple[List[Tuple[str, str]], Optional[Dict[str, Any]]]:
        params = build_query(query, extra_query)
        json_body = build_body(body, extra_body) if body is not None or extra_body is not None else None
        return params, json_body

    def _headers(self, extra_headers: Optional[Headers], accept: Optional[str]) -> Dict[str, str]:
        headers = self.default_headers
        if accept:
            headers["Accept"] = accept
        if extra_headers:
            headers.update(extra_headers)
        return headers

    def _timeout(self, timeout: Union[Timeout, NotGiven]) -> Timeout:
        return self.timeout if isinstance(timeout, NotGiven) else timeout

    @staticmethod
    def _should_retry_status(method: str, status: int) -> bool:
        return status in _RETRY_ANY_METHOD or (status in _RETRY_IDEMPOTENT and method in _IDEMPOTENT_METHODS)

    @staticmethod
    def _should_retry_exception(method: str, exc: Exception) -> bool:
        return isinstance(exc, _NOT_SENT_ERRORS) or method in _IDEMPOTENT_METHODS

    @staticmethod
    def _retry_delay(attempt: int, response: Optional[httpx.Response]) -> float:
        if response is not None:
            header = response.headers.get("retry-after")
            if header:
                seconds: float
                try:
                    seconds = float(header)
                except ValueError:
                    parsed = email.utils.parsedate_tz(header)
                    seconds = float(email.utils.mktime_tz(parsed) - time.time()) if parsed else -1.0
                if 0 <= seconds <= MAX_RETRY_AFTER:
                    return seconds
        delay = min(INITIAL_RETRY_DELAY * (2.0**attempt), MAX_RETRY_DELAY)
        return delay * (1 - 0.25 * random.random())

    @staticmethod
    def _decode_data(response: httpx.Response) -> Any:
        try:
            payload = response.json()
        except ValueError:
            content_type = response.headers.get("content-type") or "no content type"
            raise APIResponseValidationError(
                response, message=f"Expected a JSON answer from {response.request.url.path}, got {content_type}"
            ) from None
        if isinstance(payload, dict) and "data" in payload:
            return payload["data"]
        return payload

    @staticmethod
    def _page_items(data: Any, item_key: str, item_type: Type[_T]) -> Tuple[List[_T], Optional[int]]:
        raw: Any = []
        total: Any = None
        if isinstance(data, dict):
            raw = data.get(item_key) or []
            total = data.get("total_count")
        elif isinstance(data, list):
            raw = data
        items = construct_type(List[item_type], raw)  # type: ignore[valid-type]
        if not isinstance(items, list):
            items = []
        return items, total if isinstance(total, int) and not isinstance(total, bool) else None


class SyncAPIClient(_BaseClient):
    _http: httpx.Client

    def __init__(
        self,
        *,
        api_key: str,
        base_url: Union[str, httpx.URL],
        timeout: Timeout,
        max_retries: int,
        default_headers: Optional[Headers],
        http_client: Optional[httpx.Client],
    ) -> None:
        super().__init__(
            api_key=api_key,
            base_url=base_url,
            timeout=timeout,
            max_retries=max_retries,
            default_headers=default_headers,
        )
        self._owns_http = http_client is None
        self._http = http_client or httpx.Client(timeout=timeout, follow_redirects=True)

    def close(self) -> None:
        """Close the underlying HTTP connections."""
        if self._owns_http:
            self._http.close()

    def _send(
        self,
        method: str,
        path: str,
        *,
        query: Optional[Query] = None,
        body: Optional[Body] = None,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
        accept: Optional[str] = None,
    ) -> httpx.Response:
        params, json_body = self._prepare(query, body, extra_query, extra_body)
        headers = self._headers(extra_headers, accept)
        attempt = 0
        while True:
            request = self._http.build_request(
                method,
                self.base_url + path,
                params=tuple(params) if params else None,
                json=json_body,
                headers=headers,
                timeout=self._timeout(timeout),
            )
            try:
                response = self._http.send(request)
            except httpx.TimeoutException as exc:
                if attempt < self.max_retries and self._should_retry_exception(method, exc):
                    time.sleep(self._retry_delay(attempt, None))
                    attempt += 1
                    continue
                raise APITimeoutError(request) from exc
            except httpx.TransportError as exc:
                if attempt < self.max_retries and self._should_retry_exception(method, exc):
                    time.sleep(self._retry_delay(attempt, None))
                    attempt += 1
                    continue
                raise APIConnectionError(request=request) from exc

            if response.is_success:
                return response
            if attempt < self.max_retries and self._should_retry_status(method, response.status_code):
                delay = self._retry_delay(attempt, response)
                response.close()
                time.sleep(delay)
                attempt += 1
                continue
            response.read()
            raise make_status_error(response)

    def _request(
        self,
        method: str,
        path: str,
        *,
        query: Optional[Query] = None,
        body: Optional[Body] = None,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> Any:
        response = self._send(
            method,
            path,
            query=query,
            body=body,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._decode_data(response)

    def _request_bytes(
        self,
        method: str,
        path: str,
        *,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> bytes:
        response = self._send(
            method, path, extra_headers=extra_headers, extra_query=extra_query, timeout=timeout, accept="*/*"
        )
        return response.content

    def _get_page(
        self,
        path: str,
        *,
        query: Query,
        item_key: str,
        item_type: Type[_T],
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> SyncPage[_T]:
        clean = _clean_query(query)
        data = self._request(
            "GET", path, query=clean, extra_headers=extra_headers, extra_query=extra_query, timeout=timeout
        )
        items, total = self._page_items(data, item_key, item_type)

        def fetch(next_query: Dict[str, Any]) -> SyncPage[_T]:
            return self._get_page(
                path,
                query=next_query,
                item_key=item_key,
                item_type=item_type,
                extra_headers=extra_headers,
                extra_query=extra_query,
                timeout=timeout,
            )

        return SyncPage(items=items, total_count=total, query=clean, fetch=fetch)


class AsyncAPIClient(_BaseClient):
    _http: httpx.AsyncClient

    def __init__(
        self,
        *,
        api_key: str,
        base_url: Union[str, httpx.URL],
        timeout: Timeout,
        max_retries: int,
        default_headers: Optional[Headers],
        http_client: Optional[httpx.AsyncClient],
    ) -> None:
        super().__init__(
            api_key=api_key,
            base_url=base_url,
            timeout=timeout,
            max_retries=max_retries,
            default_headers=default_headers,
        )
        self._owns_http = http_client is None
        self._http = http_client or httpx.AsyncClient(timeout=timeout, follow_redirects=True)

    async def close(self) -> None:
        """Close the underlying HTTP connections."""
        if self._owns_http:
            await self._http.aclose()

    async def _send(
        self,
        method: str,
        path: str,
        *,
        query: Optional[Query] = None,
        body: Optional[Body] = None,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
        accept: Optional[str] = None,
    ) -> httpx.Response:
        params, json_body = self._prepare(query, body, extra_query, extra_body)
        headers = self._headers(extra_headers, accept)
        attempt = 0
        while True:
            request = self._http.build_request(
                method,
                self.base_url + path,
                params=tuple(params) if params else None,
                json=json_body,
                headers=headers,
                timeout=self._timeout(timeout),
            )
            try:
                response = await self._http.send(request)
            except httpx.TimeoutException as exc:
                if attempt < self.max_retries and self._should_retry_exception(method, exc):
                    await asyncio.sleep(self._retry_delay(attempt, None))
                    attempt += 1
                    continue
                raise APITimeoutError(request) from exc
            except httpx.TransportError as exc:
                if attempt < self.max_retries and self._should_retry_exception(method, exc):
                    await asyncio.sleep(self._retry_delay(attempt, None))
                    attempt += 1
                    continue
                raise APIConnectionError(request=request) from exc

            if response.is_success:
                return response
            if attempt < self.max_retries and self._should_retry_status(method, response.status_code):
                delay = self._retry_delay(attempt, response)
                await response.aclose()
                await asyncio.sleep(delay)
                attempt += 1
                continue
            await response.aread()
            raise make_status_error(response)

    async def _request(
        self,
        method: str,
        path: str,
        *,
        query: Optional[Query] = None,
        body: Optional[Body] = None,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> Any:
        response = await self._send(
            method,
            path,
            query=query,
            body=body,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._decode_data(response)

    async def _request_bytes(
        self,
        method: str,
        path: str,
        *,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> bytes:
        response = await self._send(
            method, path, extra_headers=extra_headers, extra_query=extra_query, timeout=timeout, accept="*/*"
        )
        return response.content

    async def _get_page(
        self,
        path: str,
        *,
        query: Query,
        item_key: str,
        item_type: Type[_T],
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> AsyncPage[_T]:
        clean = _clean_query(query)
        data = await self._request(
            "GET", path, query=clean, extra_headers=extra_headers, extra_query=extra_query, timeout=timeout
        )
        items, total = self._page_items(data, item_key, item_type)

        async def fetch(next_query: Dict[str, Any]) -> AsyncPage[_T]:
            return await self._get_page(
                path,
                query=next_query,
                item_key=item_key,
                item_type=item_type,
                extra_headers=extra_headers,
                extra_query=extra_query,
                timeout=timeout,
            )

        return AsyncPage(items=items, total_count=total, query=clean, fetch=fetch)
