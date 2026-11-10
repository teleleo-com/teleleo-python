from __future__ import annotations

from typing import Any, AsyncIterator, Awaitable, Callable, Dict, Generic, Iterator, List, Optional, TypeVar

__all__ = ["SyncPage", "AsyncPage"]

_T = TypeVar("_T")

DEFAULT_PAGE_SIZE = 50


class _BasePage(Generic[_T]):
    items: List[_T]
    """The items of this page."""
    total_count: Optional[int]
    """How many items match the request across all pages."""

    def __init__(self, *, items: List[_T], total_count: Optional[int], query: Dict[str, Any]) -> None:
        self.items = items
        self.total_count = total_count
        self._query = query

    def _position(self) -> tuple[int, Optional[int]]:
        page = self._query.get("page")
        limit = self._query.get("limit")
        page_index = int(page) if isinstance(page, int) else 0
        if isinstance(limit, int):
            return page_index, limit
        if page is not None:
            return page_index, DEFAULT_PAGE_SIZE
        return page_index, len(self.items) or None

    def has_next_page(self) -> bool:
        if not self.items:
            return False
        page_index, limit = self._position()
        if limit is None:
            return False
        if self.total_count is None:
            return len(self.items) >= limit
        return page_index * limit + len(self.items) < self.total_count

    def _next_query(self) -> Dict[str, Any]:
        page_index, limit = self._position()
        return {**self._query, "page": page_index + 1, "limit": limit}

    def __repr__(self) -> str:
        return f"{type(self).__name__}(items={len(self.items)}, total_count={self.total_count})"


class SyncPage(_BasePage[_T]):
    """One page of a list.

    ``page.items`` holds this page. Iterating the page itself goes through every item of every page and requests
    the next pages as needed::

        for sms in client.sms.list(limit=100):
            print(sms.message_decoded)
    """

    def __init__(
        self,
        *,
        items: List[_T],
        total_count: Optional[int],
        query: Dict[str, Any],
        fetch: Callable[[Dict[str, Any]], SyncPage[_T]],
    ) -> None:
        super().__init__(items=items, total_count=total_count, query=query)
        self._fetch = fetch

    def get_next_page(self) -> SyncPage[_T]:
        if not self.has_next_page():
            raise RuntimeError("No next page; check has_next_page() first")
        return self._fetch(self._next_query())

    def iter_pages(self) -> Iterator[SyncPage[_T]]:
        page: SyncPage[_T] = self
        while True:
            yield page
            if not page.has_next_page():
                return
            page = page.get_next_page()

    def auto_paging_iter(self) -> Iterator[_T]:
        for page in self.iter_pages():
            yield from page.items

    def __iter__(self) -> Iterator[_T]:
        return self.auto_paging_iter()


class AsyncPage(_BasePage[_T]):
    """One page of a list.

    ``page.items`` holds this page. ``async for`` over the page goes through every item of every page::

        page = await client.sms.list(limit=100)
        async for sms in page:
            print(sms.message_decoded)
    """

    def __init__(
        self,
        *,
        items: List[_T],
        total_count: Optional[int],
        query: Dict[str, Any],
        fetch: Callable[[Dict[str, Any]], Awaitable[AsyncPage[_T]]],
    ) -> None:
        super().__init__(items=items, total_count=total_count, query=query)
        self._fetch = fetch

    async def get_next_page(self) -> AsyncPage[_T]:
        if not self.has_next_page():
            raise RuntimeError("No next page; check has_next_page() first")
        return await self._fetch(self._next_query())

    async def iter_pages(self) -> AsyncIterator[AsyncPage[_T]]:
        page: AsyncPage[_T] = self
        while True:
            yield page
            if not page.has_next_page():
                return
            page = await page.get_next_page()

    async def auto_paging_iter(self) -> AsyncIterator[_T]:
        async for page in self.iter_pages():
            for item in page.items:
                yield item

    def __aiter__(self) -> AsyncIterator[_T]:
        return self.auto_paging_iter()
