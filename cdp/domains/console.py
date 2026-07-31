"""Generated bindings for the CDP Console domain. Do not edit manually."""

from __future__ import annotations

from collections.abc import Awaitable, Mapping
from typing import Literal, cast, overload

from typing_extensions import NotRequired, TypedDict

from cdp.domain import Domain as BaseDomain, EventCallback, Unsubscribe
from cdp.types import JsonObject


class ConsoleMessage(TypedDict):
    source: Literal[
        "xml",
        "javascript",
        "network",
        "console-api",
        "storage",
        "appcache",
        "rendering",
        "security",
        "other",
        "deprecation",
        "worker",
    ]
    level: Literal["log", "warning", "error", "debug", "info"]
    text: str
    url: NotRequired[str]
    line: NotRequired[int]
    column: NotRequired[int]


class MessageAddedEvent(TypedDict):
    message: ConsoleMessage


class Console(BaseDomain):
    """This domain is deprecated - use Runtime or Log instead."""

    domain_name = "Console"

    async def clearMessages(
        self,
        session_id: str | None = None,
    ) -> JsonObject:
        """Does nothing."""

        return await self._command("clearMessages", None, session_id, {})

    async def disable(
        self,
        session_id: str | None = None,
    ) -> JsonObject:
        """Disables console domain, prevents further console messages from being reported to the client."""

        return await self._command("disable", None, session_id, {})

    async def enable(
        self,
        session_id: str | None = None,
    ) -> JsonObject:
        """Enables console domain, sends the messages collected so far to the client by means of the `messageAdded` notification."""

        return await self._command("enable", None, session_id, {})

    @overload
    def messageAdded(
        self,
        callback_or_session: EventCallback[MessageAddedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def messageAdded(
        self,
        callback_or_session: str,
        handler: EventCallback[MessageAddedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def messageAdded(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[MessageAddedEvent]: ...

    def messageAdded(
        self,
        callback_or_session: EventCallback[MessageAddedEvent] | str | None = None,
        handler: EventCallback[MessageAddedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[MessageAddedEvent] | Unsubscribe:
        """Issued when new console message is added."""

        return cast(
            Awaitable[MessageAddedEvent] | Unsubscribe,
            self._event(
                "messageAdded",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )


__all__ = ["Console", "ConsoleMessage", "MessageAddedEvent"]
