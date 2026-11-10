from __future__ import annotations

import os
from types import TracebackType
from typing import Optional, Type, Union

import httpx

from ._base_client import DEFAULT_BASE_URL, DEFAULT_MAX_RETRIES, DEFAULT_TIMEOUT, AsyncAPIClient, SyncAPIClient
from ._exceptions import TeleleoError
from ._types import NOT_GIVEN, Headers, NotGiven, Timeout
from .resources import AsyncResources, SyncResources

__all__ = ["Teleleo", "AsyncTeleleo"]

_MISSING_KEY = (
    "The API key is not set: pass api_key to the client or set the TELELEO_API_KEY environment variable. "
    "The key is in the Teleleo cabinet, Settings - API key."
)


def _resolve(
    api_key: Optional[str], base_url: Union[str, httpx.URL, None], timeout: Union[Timeout, NotGiven]
) -> tuple[str, str, Timeout]:
    key = api_key if api_key is not None else os.environ.get("TELELEO_API_KEY")
    if not key:
        raise TeleleoError(_MISSING_KEY)
    url = str(base_url) if base_url is not None else (os.environ.get("TELELEO_BASE_URL") or DEFAULT_BASE_URL)
    return key, url, DEFAULT_TIMEOUT if isinstance(timeout, NotGiven) else timeout


class Teleleo(SyncResources, SyncAPIClient):
    """Client for the Teleleo API.

    ::

        from teleleo import Teleleo

        client = Teleleo()  # reads TELELEO_API_KEY
        for dongle in client.dongles.list():
            print(dongle.dongle_id, dongle.name)

    Args:
        api_key: The API key from the Teleleo cabinet (Settings - API key). Defaults to ``TELELEO_API_KEY``.
        base_url: Defaults to ``TELELEO_BASE_URL``, then to ``https://app.teleleo.com/react_api``.
        timeout: Seconds or an ``httpx.Timeout``; 60 seconds by default.
        max_retries: How many times to repeat a request that failed for a transient reason; 2 by default.
            Requests that create something (POST) are repeated only when the server could not have acted on them.
        default_headers: Headers to send with every request.
        http_client: Your own ``httpx.Client``, for proxies or custom transports.
    """

    def __init__(
        self,
        *,
        api_key: Optional[str] = None,
        base_url: Union[str, httpx.URL, None] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Optional[Headers] = None,
        http_client: Optional[httpx.Client] = None,
    ) -> None:
        key, url, resolved_timeout = _resolve(api_key, base_url, timeout)
        super().__init__(
            api_key=key,
            base_url=url,
            timeout=resolved_timeout,
            max_retries=max_retries,
            default_headers=default_headers,
            http_client=http_client,
        )

    def with_options(
        self,
        *,
        api_key: Optional[str] = None,
        base_url: Union[str, httpx.URL, None] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
        max_retries: Optional[int] = None,
        default_headers: Optional[Headers] = None,
    ) -> Teleleo:
        """A copy of the client with some options changed; it shares the connection pool with this one.

        ::

            client.with_options(timeout=5, max_retries=0).dongles.list()
        """
        return Teleleo(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            max_retries=self.max_retries if max_retries is None else max_retries,
            default_headers={**self._custom_headers, **(default_headers or {})},
            http_client=self._http,
        )

    def __enter__(self) -> Teleleo:
        return self

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc: Optional[BaseException],
        tb: Optional[TracebackType],
    ) -> None:
        self.close()


class AsyncTeleleo(AsyncResources, AsyncAPIClient):
    """Asynchronous client for the Teleleo API.

    ::

        import asyncio
        from teleleo import AsyncTeleleo

        async def main() -> None:
            async with AsyncTeleleo() as client:
                page = await client.dongles.list()
                async for dongle in page:
                    print(dongle.dongle_id, dongle.name)

        asyncio.run(main())

    Takes the same arguments as :class:`Teleleo`; ``http_client`` is an ``httpx.AsyncClient``.
    """

    def __init__(
        self,
        *,
        api_key: Optional[str] = None,
        base_url: Union[str, httpx.URL, None] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Optional[Headers] = None,
        http_client: Optional[httpx.AsyncClient] = None,
    ) -> None:
        key, url, resolved_timeout = _resolve(api_key, base_url, timeout)
        super().__init__(
            api_key=key,
            base_url=url,
            timeout=resolved_timeout,
            max_retries=max_retries,
            default_headers=default_headers,
            http_client=http_client,
        )

    def with_options(
        self,
        *,
        api_key: Optional[str] = None,
        base_url: Union[str, httpx.URL, None] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
        max_retries: Optional[int] = None,
        default_headers: Optional[Headers] = None,
    ) -> AsyncTeleleo:
        """A copy of the client with some options changed; it shares the connection pool with this one."""
        return AsyncTeleleo(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            max_retries=self.max_retries if max_retries is None else max_retries,
            default_headers={**self._custom_headers, **(default_headers or {})},
            http_client=self._http,
        )

    async def __aenter__(self) -> AsyncTeleleo:
        return self

    async def __aexit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc: Optional[BaseException],
        tb: Optional[TracebackType],
    ) -> None:
        await self.close()
