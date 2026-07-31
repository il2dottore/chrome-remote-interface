"""Shared public types for the Chrome DevTools Protocol client."""

from __future__ import annotations

import math
from collections.abc import Callable, Mapping
from typing import TypeAlias, cast

from typing_extensions import NotRequired, TypedDict

JsonPrimitive: TypeAlias = bool | int | float | str | None
JsonValue: TypeAlias = JsonPrimitive | list["JsonValue"] | dict[str, "JsonValue"]
JsonObject: TypeAlias = dict[str, JsonValue]


def to_json_value(value: object) -> JsonValue:
    """Validate and normalize a value for JSON/CDP serialization."""

    if value is None or isinstance(value, bool | int | str):
        return value
    if isinstance(value, float):
        if not math.isfinite(value):
            raise ValueError("JSON numbers must be finite")
        return value
    if isinstance(value, list):
        return [to_json_value(item) for item in cast(list[object], value)]
    if isinstance(value, tuple):
        return [to_json_value(item) for item in cast(tuple[object, ...], value)]
    if isinstance(value, Mapping):
        result: JsonObject = {}
        mapping = cast(Mapping[object, object], value)
        for key, item in mapping.items():
            if not isinstance(key, str):
                raise TypeError("CDP object keys must be strings")
            result[key] = to_json_value(item)
        return result
    raise TypeError(f"{type(value).__name__} is not JSON serializable")


def json_object_list(value: JsonValue | None) -> list[JsonObject]:
    """Narrow a JSON array to its object members."""

    if not isinstance(value, list):
        return []
    return [item for item in value if isinstance(item, dict)]


class Target(TypedDict):
    """A target returned by the DevTools ``/json`` endpoints."""

    id: str
    type: str
    title: str
    url: str
    webSocketDebuggerUrl: NotRequired[str]
    devtoolsFrontendUrl: NotRequired[str]
    faviconUrl: NotRequired[str]
    description: NotRequired[str]


VersionInfo = TypedDict(
    "VersionInfo",
    {
        "Browser": NotRequired[str],
        "Protocol-Version": NotRequired[str],
        "User-Agent": NotRequired[str],
        "V8-Version": NotRequired[str],
        "WebKit-Version": NotRequired[str],
        "webSocketDebuggerUrl": NotRequired[str],
    },
)


ProtocolDescriptor: TypeAlias = dict[str, JsonValue]
TargetSelector: TypeAlias = Callable[
    [list[Target]], int | Target | Mapping[str, object]
]
