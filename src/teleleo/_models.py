from __future__ import annotations

import datetime as _dt
import enum
import re
import sys
from typing import Any, Dict, ForwardRef, List, Optional, Type, TypeVar, Union, cast, get_args, get_origin

import pydantic

_UNION_ORIGINS: tuple[Any, ...]
if sys.version_info >= (3, 10):
    from types import UnionType

    _UNION_ORIGINS = (Union, UnionType)
else:  # pragma: no cover
    _UNION_ORIGINS = (Union,)

__all__ = ["BaseModel", "construct_type", "parse_datetime"]

_T = TypeVar("_T")
_M = TypeVar("_M", bound="BaseModel")

_DATETIME_RE = re.compile(r"^(\d{4})-(\d{2})-(\d{2})[ T](\d{2}):(\d{2}):(\d{2})(\.\d{1,6})?\d*(Z|z|[+-]\d{2}:?\d{2})?$")


def parse_datetime(value: str) -> Optional[_dt.datetime]:
    """Parse a date-time of the API.

    Answers carry ``YYYY-MM-DD HH:MM:SS[.ffffff]`` in UTC without an offset; RFC 3339 with an offset is accepted too.
    Returns a timezone-aware ``datetime``, or ``None`` when the value is not a date-time.
    """
    match = _DATETIME_RE.match(value.strip())
    if match is None:
        return None
    year, month, day, hour, minute, second, fraction, offset = match.groups()
    micro = int(fraction[1:].ljust(6, "0")) if fraction else 0
    tz: _dt.tzinfo
    if offset is None or offset in ("Z", "z"):
        tz = _dt.timezone.utc
    else:
        sign = 1 if offset[0] == "+" else -1
        digits = offset[1:].replace(":", "")
        tz = _dt.timezone(sign * _dt.timedelta(hours=int(digits[:2]), minutes=int(digits[2:])))
    try:
        return _dt.datetime(int(year), int(month), int(day), int(hour), int(minute), int(second), micro, tzinfo=tz)
    except ValueError:
        return None


class BaseModel(pydantic.BaseModel):
    """Base class of every model the API returns.

    Answers are not validated: a value that does not match the declared type is kept as it came, a field missing in
    the answer is ``None``, and fields the library does not know yet are kept and reachable as attributes.
    """

    model_config = pydantic.ConfigDict(
        extra="allow",
        populate_by_name=True,
        protected_namespaces=(),
        arbitrary_types_allowed=True,
    )

    @classmethod
    def construct_from(cls: Type[_M], data: Dict[str, Any]) -> _M:
        """Build the model from a decoded JSON object without validation."""
        values: Dict[str, Any] = {}
        known: set[str] = set()
        fields_set: set[str] = set()
        for name, field in cls.model_fields.items():
            key = field.alias or name
            known.add(key)
            if key in data:
                values[name] = construct_type(field.annotation, data[key])
                fields_set.add(name)
            else:
                values[name] = None
        for key, value in data.items():
            if key not in known:
                values[key] = value
                fields_set.add(key)
        return cast(_M, cls.model_construct(_fields_set=fields_set, **values))

    def to_dict(self) -> Dict[str, Any]:
        """The fields that came in the answer, as a JSON-compatible ``dict``."""
        return self.model_dump(mode="json", by_alias=True, exclude_unset=True, warnings=False)

    def to_json(self, *, indent: Optional[int] = 2) -> str:
        """The fields that came in the answer, as a JSON string."""
        return self.model_dump_json(by_alias=True, exclude_unset=True, warnings=False, indent=indent)


def construct_type(type_: Any, value: object) -> Any:
    """Turn decoded JSON into the declared type without raising: values that do not fit are returned as they are."""
    if value is None or type_ is Any or isinstance(type_, (str, ForwardRef)):
        return value

    origin = get_origin(type_)
    if origin in _UNION_ORIGINS:
        args = [arg for arg in get_args(type_) if arg is not type(None)]
        if len(args) == 1:
            return construct_type(args[0], value)
        for arg in args:
            if isinstance(value, dict) and isinstance(arg, type) and issubclass(arg, BaseModel):
                return arg.construct_from(value)
            if isinstance(value, list) and get_origin(arg) in (list, List):
                return construct_type(arg, value)
        return value

    if origin in (list, List):
        if not isinstance(value, list):
            return value
        (item_type,) = get_args(type_) or (Any,)
        return [construct_type(item_type, item) for item in value]

    if origin is not None:
        return value

    if isinstance(type_, type):
        if issubclass(type_, BaseModel):
            return type_.construct_from(value) if isinstance(value, dict) else value
        if issubclass(type_, enum.Enum):
            try:
                return type_(value)
            except ValueError:
                return value
        if issubclass(type_, _dt.datetime):
            if isinstance(value, str):
                parsed = parse_datetime(value)
                return parsed if parsed is not None else value
            return value
        if type_ is float and isinstance(value, int) and not isinstance(value, bool):
            return float(value)
    return value
