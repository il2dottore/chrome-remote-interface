"""Asynchronous Chrome DevTools Protocol WebSocket client."""

from __future__ import annotations

import asyncio
import inspect
import json
from collections import defaultdict
from collections.abc import Awaitable, Callable, Mapping
from contextlib import suppress
from typing import Protocol as TypingProtocol
from typing import cast
from urllib.parse import urlsplit, urlunsplit

import websockets
from websockets.exceptions import ConnectionClosed

from ._domain_hints import DomainHints
from .devtools import HOST, PORT, List, Protocol
from .errors import ConnectionClosedError, ProtocolError
from .types import (
    JsonObject,
    ProtocolDescriptor,
    Target,
    TargetSelector,
    to_json_value,
)

Listener = Callable[..., object]
Unsubscribe = Callable[[], None]


class WebSocket(TypingProtocol):
    async def send(self, message: str) -> None: ...

    async def recv(self) -> str | bytes: ...

    async def close(self) -> None: ...


def _option(options: Mapping[str, object], snake: str, camel: str) -> object | None:
    return options.get(snake, options.get(camel))


def _option_string(
    options: Mapping[str, object],
    key: str,
    default: str,
) -> str:
    value = options.get(key, default)
    if not isinstance(value, str):
        raise TypeError(f"{key} must be a string")
    return value


def _option_integer(
    options: Mapping[str, object],
    key: str,
    default: int,
) -> int:
    value = options.get(key, default)
    if not isinstance(value, int) or isinstance(value, bool):
        raise TypeError(f"{key} must be an integer")
    return value


def _option_number(
    options: Mapping[str, object],
    key: str,
    default: float,
) -> float:
    value = options.get(key, default)
    if not isinstance(value, int | float) or isinstance(value, bool):
        raise TypeError(f"{key} must be a number")
    return float(value)


def _option_boolean(
    options: Mapping[str, object],
    key: str,
    default: bool,
) -> bool:
    value = options.get(key, default)
    if not isinstance(value, bool):
        raise TypeError(f"{key} must be a boolean")
    return value


def _string_mapping(value: Mapping[object, object]) -> dict[str, object]:
    result: dict[str, object] = {}
    for key, item in value.items():
        if not isinstance(key, str):
            raise TypeError("option and target keys must be strings")
        result[key] = item
    return result


def _target_option(value: object) -> str | TargetSelector | Mapping[str, object] | None:
    if value is None or isinstance(value, str):
        return value
    if isinstance(value, Mapping):
        return _string_mapping(cast(Mapping[object, object], value))
    if callable(value):

        def selector(targets: list[Target]) -> int | Target | Mapping[str, object]:
            selected = value(targets)
            if isinstance(selected, int) and not isinstance(selected, bool):
                return selected
            if isinstance(selected, Mapping):
                return _string_mapping(cast(Mapping[object, object], selected))
            raise TypeError("target selector returned an invalid target")

        return selector
    raise TypeError("target must be an id, URL, target object, or selector")


class Client(DomainHints):
    """A connected CDP endpoint with generated domain attributes."""

    def __init__(
        self,
        websocket: WebSocket,
        websocket_url: str,
        protocol: ProtocolDescriptor,
    ) -> None:
        self.webSocketUrl = websocket_url
        self.websocket_url = websocket_url
        self.protocol = protocol
        self._websocket = websocket
        self._next_command_id = 1
        self._pending: dict[int, tuple[asyncio.Future[JsonObject], JsonObject]] = {}
        self._listeners: dict[str, list[Listener]] = defaultdict(list)
        self._session_listeners: dict[tuple[str, str], list[Listener]] = defaultdict(
            list
        )
        self._callback_tasks: set[asyncio.Future[object]] = set()
        self._closed = False
        self._receiver = asyncio.create_task(
            self._receive_loop(),
            name="chrome-remote-interface receiver",
        )
        self._install_domains()

    def _install_domains(self) -> None:
        from .domain import DynamicDomain
        from .domains import DOMAIN_CLASSES

        for schema in cast(list[JsonObject], self.protocol.get("domains", [])):
            name = schema.get("domain")
            if not isinstance(name, str):
                continue
            domain_class = DOMAIN_CLASSES.get(name)
            domain = (
                domain_class(self)
                if domain_class is not None
                else DynamicDomain(self, name)
            )
            setattr(self, name, domain)

    def domain_schema(self, name: str) -> JsonObject:
        for schema in cast(list[JsonObject], self.protocol.get("domains", [])):
            if schema.get("domain") == name:
                return schema
        return {}

    def __getitem__(self, qualified_name: str) -> object:
        """Look up ``Domain.member`` using the Node library's flat syntax."""

        domain_name, separator, member_name = qualified_name.partition(".")
        if not separator:
            return getattr(self, domain_name)
        return getattr(getattr(self, domain_name), member_name)

    async def send(
        self,
        method: str,
        params: Mapping[str, object] | None = None,
        session_id: str | None = None,
        **keyword_params: object,
    ) -> JsonObject:
        """Send a command and await its result."""

        if self._closed:
            raise ConnectionClosedError("WebSocket connection closed")
        raw_payload = dict(params or {})
        overlap = raw_payload.keys() & keyword_params.keys()
        if overlap:
            names = ", ".join(sorted(overlap))
            raise TypeError(f"parameters were provided twice: {names}")
        raw_payload.update(keyword_params)
        payload = {key: to_json_value(value) for key, value in raw_payload.items()}
        command_id = self._next_command_id
        self._next_command_id += 1
        request: JsonObject = {
            "id": command_id,
            "method": method,
            "params": payload,
        }
        if session_id is not None:
            request["sessionId"] = session_id
        future = asyncio.get_running_loop().create_future()
        self._pending[command_id] = (future, request)
        try:
            await self._websocket.send(
                json.dumps(request, separators=(",", ":"), ensure_ascii=False)
            )
        except Exception:
            self._pending.pop(command_id, None)
            raise
        return await future

    def on(self, event_name: str, callback: Listener) -> Unsubscribe:
        """Subscribe to a raw client event."""

        listeners = self._listeners[event_name]
        listeners.append(callback)

        def unsubscribe() -> None:
            with suppress(ValueError):
                listeners.remove(callback)

        return unsubscribe

    def once(self, event_name: str) -> Awaitable[object]:
        """Return an awaitable resolved by the next raw client event."""

        loop = asyncio.get_running_loop()
        future: asyncio.Future[object] = loop.create_future()
        unsubscribe: Unsubscribe

        def resolve(*args: object) -> None:
            unsubscribe()
            if not future.done():
                future.set_result(args[0] if len(args) == 1 else args)

        unsubscribe = self.on(event_name, resolve)
        return future

    def on_event(
        self,
        method: str,
        callback: Listener,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe:
        """Subscribe to a CDP event, optionally restricted to a session."""

        if session_id is None:
            listeners = self._listeners[method]
        else:
            listeners = self._session_listeners[(method, session_id)]
        listeners.append(callback)

        def unsubscribe() -> None:
            with suppress(ValueError):
                listeners.remove(callback)

        return unsubscribe

    def wait_for(
        self,
        method: str,
        *,
        session_id: str | None = None,
    ) -> Awaitable[JsonObject]:
        """Wait for one CDP event."""

        loop = asyncio.get_running_loop()
        future: asyncio.Future[JsonObject] = loop.create_future()
        unsubscribe: Unsubscribe

        def resolve(payload: JsonObject) -> None:
            unsubscribe()
            if not future.done():
                future.set_result(payload)

        unsubscribe = self.on_event(method, resolve, session_id=session_id)
        return future

    def remove_all_listeners(self, event_name: str | None = None) -> None:
        """Remove raw and protocol event listeners."""

        if event_name is None:
            self._listeners.clear()
            self._session_listeners.clear()
        else:
            self._listeners.pop(event_name, None)
            for key in [key for key in self._session_listeners if key[0] == event_name]:
                self._session_listeners.pop(key, None)

    async def close(self) -> None:
        """Close the connection and fail commands that are still pending."""

        if self._closed:
            return
        self._closed = True
        await self._websocket.close()
        for task in self._callback_tasks:
            task.cancel()
        self._callback_tasks.clear()
        if self._receiver is not asyncio.current_task():
            if not self._receiver.done():
                self._receiver.cancel()
            with suppress(asyncio.CancelledError, ConnectionClosed):
                await self._receiver
        self._fail_pending()

    async def __aenter__(self) -> Client:
        return self

    async def __aexit__(
        self,
        exception_type: type[BaseException] | None,
        exception: BaseException | None,
        traceback: object | None,
    ) -> None:
        await self.close()

    async def _receive_loop(self) -> None:
        try:
            while True:
                raw = await self._websocket.recv()
                if isinstance(raw, bytes):
                    raw = raw.decode("utf-8")
                message = cast(JsonObject, json.loads(raw))
                self._handle_message(message)
        except (ConnectionClosed, asyncio.CancelledError):
            pass
        finally:
            was_closed = self._closed
            self._closed = True
            self._fail_pending()
            if not was_closed:
                self._emit("disconnect")

    def _fail_pending(self) -> None:
        for future, _request in self._pending.values():
            if not future.done():
                future.set_exception(
                    ConnectionClosedError("WebSocket connection closed")
                )
        self._pending.clear()

    def _handle_message(self, message: JsonObject) -> None:
        command_id = message.get("id")
        if isinstance(command_id, int):
            pending = self._pending.pop(command_id, None)
            if pending is None:
                return
            future, request = pending
            if future.done():
                return
            error = message.get("error")
            if isinstance(error, dict):
                future.set_exception(
                    ProtocolError(
                        request,
                        cast(JsonObject, error),
                    )
                )
            else:
                result = message.get("result", {})
                future.set_result(cast(JsonObject, result))
            if not self._pending:
                self._emit("ready")
            return
        method = message.get("method")
        if not isinstance(method, str):
            return
        params = message.get("params", {})
        payload = cast(JsonObject, params if isinstance(params, dict) else {})
        session_id = message.get("sessionId")
        self._emit("event", message)
        self._emit(method, payload)
        if isinstance(session_id, str):
            for callback in tuple(self._session_listeners[(method, session_id)]):
                self._invoke(callback, payload)

    def _emit(self, event_name: str, *args: object) -> None:
        for callback in tuple(self._listeners[event_name]):
            self._invoke(callback, *args)

    def _invoke(self, callback: Listener, *args: object) -> None:
        try:
            result = callback(*args)
            if inspect.isawaitable(result):
                task = asyncio.ensure_future(cast(Awaitable[object], result))
                self._callback_tasks.add(task)
                task.add_done_callback(self._callback_tasks.discard)
        except Exception as error:
            asyncio.get_running_loop().call_exception_handler(
                {
                    "message": "Unhandled exception in CDP event callback",
                    "exception": error,
                }
            )


async def connect(
    target: str | TargetSelector | Mapping[str, object] | None = None,
    *,
    host: str = HOST,
    port: int = PORT,
    secure: bool = False,
    use_host_name: bool = False,
    alter_path: Callable[[str], str] | None = None,
    protocol: ProtocolDescriptor | None = None,
    local: bool = False,
    timeout: float = 10.0,
) -> Client:
    """Connect to a Chrome DevTools Protocol target."""

    target_mapping = (
        _string_mapping(cast(Mapping[object, object], target))
        if isinstance(target, Mapping)
        else None
    )
    resolved_target: str | TargetSelector | Mapping[str, object] | None
    if target_mapping is not None and "webSocketDebuggerUrl" not in target_mapping:
        option_keys = {
            "host",
            "port",
            "secure",
            "use_host_name",
            "useHostName",
            "alter_path",
            "alterPath",
            "protocol",
            "local",
            "timeout",
            "target",
        }
        if target_mapping.keys() & option_keys:
            options = target_mapping
            resolved_target = _target_option(options.get("target"))
            host = _option_string(options, "host", host)
            port = _option_integer(options, "port", port)
            secure = _option_boolean(options, "secure", secure)
            host_name_value = _option(options, "use_host_name", "useHostName")
            if host_name_value is not None:
                if not isinstance(host_name_value, bool):
                    raise TypeError("use_host_name must be a boolean")
                use_host_name = host_name_value
            alter_path_value = _option(options, "alter_path", "alterPath")
            if alter_path_value is not None:
                if not callable(alter_path_value):
                    raise TypeError("alter_path must be callable")

                def checked_alter_path(path: str) -> str:
                    transformed = alter_path_value(path)
                    if not isinstance(transformed, str):
                        raise TypeError("alter_path must return a string")
                    return transformed

                alter_path = checked_alter_path
            protocol_value = options.get("protocol")
            if protocol_value is not None:
                normalized_protocol = to_json_value(protocol_value)
                if not isinstance(normalized_protocol, dict):
                    raise TypeError("protocol must be a JSON object")
                protocol = normalized_protocol
            local = _option_boolean(options, "local", local)
            timeout = _option_number(options, "timeout", timeout)
        else:
            resolved_target = target_mapping
    elif target_mapping is not None:
        resolved_target = target_mapping
    else:
        resolved_target = _target_option(cast(object, target))
    http_options: dict[str, object] = {
        "host": host,
        "port": port,
        "secure": secure,
        "use_host_name": use_host_name,
        "timeout": timeout,
    }
    if alter_path is not None:
        http_options["alter_path"] = alter_path
    websocket_url = await _resolve_target(resolved_target, http_options)
    parsed = urlsplit(websocket_url)
    path = parsed.path
    if alter_path is not None:
        path = alter_path(path)
    scheme = "wss" if secure else parsed.scheme
    websocket_url = urlunsplit(
        (scheme, parsed.netloc, path, parsed.query, parsed.fragment)
    )
    protocol_options = dict(http_options)
    if parsed.hostname:
        protocol_options["host"] = parsed.hostname
    if parsed.port:
        protocol_options["port"] = parsed.port
    descriptor = (
        protocol
        if protocol is not None
        else await Protocol({**protocol_options, "local": local})
    )
    websocket = await websockets.connect(
        websocket_url,
        compression=None,
        max_size=256 * 1024 * 1024,
        open_timeout=timeout,
    )
    return Client(cast(WebSocket, websocket), websocket_url, descriptor)


async def _resolve_target(
    target: str | TargetSelector | Mapping[str, object] | None,
    options: Mapping[str, object],
) -> str:
    if isinstance(target, str):
        if target.startswith("/"):
            scheme = "wss" if options.get("secure") else "ws"
            return f"{scheme}://{options['host']}:{options['port']}{target}"
        if target.lower().startswith(("ws://", "wss://")):
            return target
        targets = await List(options)
        match = next((item for item in targets if item["id"] == target), None)
        if match is None or "webSocketDebuggerUrl" not in match:
            raise ValueError(f"No inspectable target with id {target!r}")
        return match["webSocketDebuggerUrl"]
    if isinstance(target, Mapping):
        target_mapping = _string_mapping(cast(Mapping[object, object], target))
        url = target_mapping.get("webSocketDebuggerUrl")
        if not isinstance(url, str):
            raise ValueError("Target has no webSocketDebuggerUrl")
        return url
    targets = await List(options)
    selected: int | Target | Mapping[str, object] | None
    if callable(target):
        selected = target(targets)
    else:
        selected = next(
            (
                item
                for item in targets
                if item.get("type") == "page" and item.get("webSocketDebuggerUrl")
            ),
            None,
        )
        if selected is None:
            selected = next(
                (item for item in targets if item.get("webSocketDebuggerUrl")),
                None,
            )
    if isinstance(selected, int):
        if selected < 0 or selected >= len(targets):
            raise ValueError(f"Target index out of range: {selected}")
        selected = targets[selected]
    if not isinstance(selected, Mapping):
        raise ValueError("No inspectable targets")
    selected_mapping = _string_mapping(cast(Mapping[object, object], selected))
    url = selected_mapping.get("webSocketDebuggerUrl")
    if not isinstance(url, str):
        raise ValueError("Selected target has no webSocketDebuggerUrl")
    return url


CDP = connect
Chrome = connect
