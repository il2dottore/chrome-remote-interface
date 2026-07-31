"""Async wrappers for Chrome's HTTP discovery endpoints."""

from __future__ import annotations

import asyncio
import json
import socket
import ssl
from collections.abc import Callable, Mapping
from importlib import resources
from typing import TypeVar, cast
from urllib.error import HTTPError
from urllib.parse import quote
from urllib.request import Request, urlopen

from .types import JsonValue, ProtocolDescriptor, Target, VersionInfo

HOST = "localhost"
PORT = 9222
REQUEST_TIMEOUT = 10.0

Result = TypeVar("Result")
PathTransform = Callable[[str], str]


def _string_option(
    options: Mapping[str, object],
    key: str,
    default: str,
) -> str:
    value = options.get(key, default)
    if not isinstance(value, str):
        raise TypeError(f"{key} must be a string")
    return value


def _integer_option(
    options: Mapping[str, object],
    key: str,
    default: int,
) -> int:
    value = options.get(key, default)
    if not isinstance(value, int) or isinstance(value, bool):
        raise TypeError(f"{key} must be an integer")
    return value


def _number_option(
    options: Mapping[str, object],
    key: str,
    default: float,
) -> float:
    value = options.get(key, default)
    if not isinstance(value, int | float) or isinstance(value, bool):
        raise TypeError(f"{key} must be a number")
    return float(value)


def _boolean_option(
    options: Mapping[str, object],
    key: str,
    default: bool,
) -> bool:
    value = options.get(key, default)
    if not isinstance(value, bool):
        raise TypeError(f"{key} must be a boolean")
    return value


def _normalize_options(
    options: Mapping[str, object] | None,
    kwargs: Mapping[str, object],
) -> dict[str, object]:
    result = dict(options or {})
    result.update(kwargs)
    aliases = {
        "useHostName": "use_host_name",
        "alterPath": "alter_path",
    }
    for old, new in aliases.items():
        if old in result and new not in result:
            result[new] = result.pop(old)
    return result


def _request_sync(path: str, options: Mapping[str, object]) -> bytes:
    host = _string_option(options, "host", HOST)
    port = _integer_option(options, "port", PORT)
    secure = _boolean_option(options, "secure", False)
    timeout = _number_option(options, "timeout", REQUEST_TIMEOUT)
    use_host_name = _boolean_option(options, "use_host_name", False)
    transform = options.get("alter_path")
    if transform is not None:
        if not callable(transform):
            raise TypeError("alter_path must be callable")
        transformed_path = transform(path)
        if not isinstance(transformed_path, str):
            raise TypeError("alter_path must return a string")
        path = transformed_path
    request_host = host if use_host_name else socket.gethostbyname(host)
    scheme = "https" if secure else "http"
    request = Request(
        f"{scheme}://{request_host}:{port}{path}",
        method=_string_option(options, "method", "GET"),
    )
    context = ssl.create_default_context() if secure else None
    try:
        with urlopen(request, timeout=timeout, context=context) as response:
            return response.read()
    except HTTPError as error:
        try:
            body = error.read().decode("utf-8", errors="replace")
        finally:
            error.close()
        raise RuntimeError(body or str(error)) from error


async def _request(path: str, options: Mapping[str, object]) -> bytes:
    return await asyncio.to_thread(_request_sync, path, options)


async def Protocol(
    options: Mapping[str, object] | None = None,
    **kwargs: object,
) -> ProtocolDescriptor:
    """Return the local or browser-provided protocol descriptor."""

    normalized = _normalize_options(options, kwargs)
    if normalized.get("local"):
        text = resources.files("cdp").joinpath("protocol.json").read_text("utf-8")
        return cast(ProtocolDescriptor, json.loads(text))
    payload = await _request("/json/protocol", normalized)
    return cast(ProtocolDescriptor, json.loads(payload))


async def List(
    options: Mapping[str, object] | None = None,
    **kwargs: object,
) -> list[Target]:
    """List inspectable browser targets."""

    payload = await _request("/json/list", _normalize_options(options, kwargs))
    return cast(list[Target], json.loads(payload))


async def New(
    options: Mapping[str, object] | None = None,
    **kwargs: object,
) -> Target:
    """Create a new browser target."""

    normalized = _normalize_options(options, kwargs)
    path = "/json/new"
    if "url" in normalized and normalized["url"] is not None:
        path += f"?{quote(str(normalized.pop('url')), safe=':/?&=#%')}"
    normalized.setdefault("method", "PUT")
    payload = await _request(path, normalized)
    return cast(Target, json.loads(payload))


async def Activate(
    options: Mapping[str, object] | str | None = None,
    **kwargs: object,
) -> None:
    """Activate an existing target."""

    if isinstance(options, str):
        kwargs = {**kwargs, "id": options}
        options = None
    normalized = _normalize_options(options, kwargs)
    target_id = quote(str(normalized["id"]), safe="")
    await _request(f"/json/activate/{target_id}", normalized)


async def Close(
    options: Mapping[str, object] | str | None = None,
    **kwargs: object,
) -> None:
    """Close an existing target."""

    if isinstance(options, str):
        kwargs = {**kwargs, "id": options}
        options = None
    normalized = _normalize_options(options, kwargs)
    target_id = quote(str(normalized["id"]), safe="")
    await _request(f"/json/close/{target_id}", normalized)


async def Version(
    options: Mapping[str, object] | None = None,
    **kwargs: object,
) -> VersionInfo:
    """Return browser and debugger version details."""

    payload = await _request("/json/version", _normalize_options(options, kwargs))
    raw = cast(dict[str, JsonValue], json.loads(payload))
    # TypedDict keys retain the spelling emitted by Chrome.
    return cast(VersionInfo, raw)


protocol = Protocol
list_targets = List
new_target = New
activate_target = Activate
close_target = Close
version = Version
