from __future__ import annotations

import datetime as _dt
import enum
from typing import Any, Dict, List, Mapping, Optional, Tuple
from urllib.parse import quote

from ._types import NotGiven

__all__ = ["format_datetime", "build_query", "build_body", "path_param"]


def format_datetime(value: _dt.datetime) -> str:
    """Format a ``datetime`` the way the API takes it: ``YYYY-MM-DD HH:MM:SS`` in UTC.

    A naive ``datetime`` is taken as UTC.
    """
    if value.tzinfo is not None:
        value = value.astimezone(_dt.timezone.utc)
    return value.strftime("%Y-%m-%d %H:%M:%S")


def _scalar(value: object) -> str:
    if isinstance(value, bool):
        return "1" if value else "0"
    if isinstance(value, _dt.datetime):
        return format_datetime(value)
    if isinstance(value, _dt.date):
        return value.isoformat()
    if isinstance(value, enum.Enum):
        return str(value.value)
    return str(value)


def build_query(*parts: Optional[Mapping[str, object]]) -> List[Tuple[str, str]]:
    """Encode query parameters. Lists repeat the key (``dongle_ids[]=1&dongle_ids[]=2``); unset values are dropped."""
    out: List[Tuple[str, str]] = []
    for params in parts:
        if not params:
            continue
        for key, value in params.items():
            if value is None or isinstance(value, NotGiven):
                continue
            if isinstance(value, (list, tuple, set, frozenset)) or (
                hasattr(value, "__iter__") and not isinstance(value, (str, bytes, Mapping))
            ):
                for item in value:  # type: ignore[attr-defined]
                    out.append((key, _scalar(item)))
            else:
                out.append((key, _scalar(value)))
    return out


def _json_value(value: Any) -> Any:
    if isinstance(value, _dt.datetime):
        return format_datetime(value)
    if isinstance(value, _dt.date):
        return value.isoformat()
    if isinstance(value, enum.Enum):
        return value.value
    if isinstance(value, Mapping):
        return {k: _json_value(v) for k, v in value.items() if not isinstance(v, NotGiven)}
    if isinstance(value, (str, bytes)):
        return value
    if isinstance(value, (list, tuple, set, frozenset)) or hasattr(value, "__iter__"):
        return [_json_value(v) for v in value]
    return value


def build_body(*parts: Optional[Mapping[str, object]]) -> Optional[Dict[str, Any]]:
    """Build a JSON body: unset fields are dropped, ``None`` stays as ``null``, dates become API strings."""
    body: Dict[str, Any] = {}
    seen = False
    for params in parts:
        if params is None:
            continue
        seen = True
        for key, value in params.items():
            if isinstance(value, NotGiven):
                continue
            body[key] = _json_value(value)
    return body if seen else None


def path_param(value: object, *, keep_slashes: bool = False) -> str:
    """Encode a path parameter. ``keep_slashes`` leaves ``/`` as a separator (used for temporary file ids)."""
    text = _scalar(value)
    if not text:
        raise ValueError("Expected a non-empty value for a path parameter")
    return quote(text, safe="/" if keep_slashes else "")
