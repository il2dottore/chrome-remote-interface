"""Runtime support used by generated protocol-domain modules."""

from __future__ import annotations

from collections.abc import Awaitable, Callable, Mapping
from typing import TYPE_CHECKING, TypeAlias, TypeVar

from .types import JsonObject, json_object_list

if TYPE_CHECKING:
    from .client import Client

EventPayload = TypeVar("EventPayload", bound=Mapping[str, object])
EventCallback: TypeAlias = Callable[[EventPayload], object]
Unsubscribe: TypeAlias = Callable[[], None]


class Domain:
    """Base class for generated domain facades."""

    domain_name = ""

    def __init__(self, client: Client) -> None:
        self._client = client
        schema = client.domain_schema(self.domain_name)
        self._commands = {
            str(item["name"])
            for item in json_object_list(schema.get("commands"))
            if isinstance(item.get("name"), str)
        }
        self._events = {
            str(item["name"])
            for item in json_object_list(schema.get("events"))
            if isinstance(item.get("name"), str)
        }
        self._types = {
            str(item["id"]): item
            for item in json_object_list(schema.get("types"))
            if isinstance(item.get("id"), str)
        }

    def __getattr__(self, name: str) -> object:
        """Expose commands/events added by a newer remote descriptor."""

        if name in self._commands:

            async def command(
                params: Mapping[str, object] | str | None = None,
                session_id: str | None = None,
                **kwargs: object,
            ) -> JsonObject:
                return await self._command(name, params, session_id, kwargs)

            return command
        if name in self._events:

            def event(
                callback_or_session: EventCallback[Mapping[str, object]]
                | str
                | None = None,
                handler: EventCallback[Mapping[str, object]] | None = None,
                *,
                session_id: str | None = None,
            ) -> Awaitable[JsonObject] | Unsubscribe:
                return self._event(
                    name,
                    callback_or_session,
                    handler,
                    session_id,
                )

            return event
        if name in self._types:
            return self._types[name]
        raise AttributeError(f"{self.domain_name!s} has no protocol member {name!r}")

    async def _command(
        self,
        command: str,
        params: Mapping[str, object] | str | None,
        session_id: str | None,
        keyword_params: Mapping[str, object],
    ) -> JsonObject:
        if isinstance(params, str):
            if session_id is not None:
                raise TypeError("session_id was provided twice")
            session_id = params
            params = None
        payload = dict(params or {})
        overlap = payload.keys() & keyword_params.keys()
        if overlap:
            names = ", ".join(sorted(overlap))
            raise TypeError(f"parameters were provided twice: {names}")
        payload.update(keyword_params)
        return await self._client.send(
            f"{self.domain_name}.{command}",
            payload,
            session_id=session_id,
        )

    def _event(
        self,
        event: str,
        callback_or_session: EventCallback[Mapping[str, object]] | str | None,
        handler: EventCallback[Mapping[str, object]] | None,
        session_id: str | None,
    ) -> Awaitable[JsonObject] | Unsubscribe:
        callback = handler
        if isinstance(callback_or_session, str):
            if session_id is not None:
                raise TypeError("session_id was provided twice")
            session_id = callback_or_session
        elif callback_or_session is not None:
            if callback is not None:
                raise TypeError("callback was provided twice")
            callback = callback_or_session
        method = f"{self.domain_name}.{event}"
        if callback is None:
            return self._client.wait_for(method, session_id=session_id)
        return self._client.on_event(method, callback, session_id=session_id)

    def on(
        self,
        event_name: str,
        callback: EventCallback[Mapping[str, object]],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe:
        """Subscribe to an event by its unqualified name."""

        return self._client.on_event(
            f"{self.domain_name}.{event_name}",
            callback,
            session_id=session_id,
        )


class DynamicDomain(Domain):
    """Facade for a domain that is absent from the bundled descriptor."""

    def __init__(self, client: Client, domain_name: str) -> None:
        self.domain_name = domain_name
        super().__init__(client)

    async def command(
        self,
        name: str,
        params: Mapping[str, object] | None = None,
        *,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Send a command advertised only by the remote descriptor."""

        return await self._command(name, params, session_id, kwargs)
