from __future__ import annotations

from typing import Mapping, Optional, Union

import httpx
from typing_extensions import Literal, TypeAlias

__all__ = ["NotGiven", "NOT_GIVEN", "Timeout", "Headers", "Query", "Body"]


class NotGiven:
    """Marks an argument that was not passed.

    ``None`` is a real value that is sent as JSON ``null``; ``NOT_GIVEN`` leaves the field out of the request.
    """

    _instance: Optional[NotGiven] = None

    def __new__(cls) -> NotGiven:
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __bool__(self) -> Literal[False]:
        return False

    def __repr__(self) -> str:
        return "NOT_GIVEN"


NOT_GIVEN = NotGiven()

Timeout: TypeAlias = Union[float, httpx.Timeout, None]
Headers: TypeAlias = Mapping[str, str]
Query: TypeAlias = Mapping[str, object]
Body: TypeAlias = Mapping[str, object]
