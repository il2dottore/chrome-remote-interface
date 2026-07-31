"""Generated bindings for the CDP Log domain. Do not edit manually."""

from __future__ import annotations

from collections.abc import Awaitable, Mapping
from typing import TYPE_CHECKING, Literal, cast, overload

from typing_extensions import NotRequired, TypedDict, Unpack

from cdp.domain import Domain as BaseDomain, EventCallback, Unsubscribe
from cdp.types import JsonObject

if TYPE_CHECKING:
    from . import network as Network
    from . import runtime as Runtime


class LogEntry(TypedDict):
    source: Literal[
        "xml",
        "javascript",
        "network",
        "storage",
        "appcache",
        "rendering",
        "security",
        "deprecation",
        "worker",
        "violation",
        "intervention",
        "recommendation",
        "other",
    ]
    level: Literal["verbose", "info", "warning", "error"]
    text: str
    category: NotRequired[Literal["cors"]]
    timestamp: Runtime.Timestamp
    url: NotRequired[str]
    lineNumber: NotRequired[int]
    stackTrace: NotRequired[Runtime.StackTrace]
    networkRequestId: NotRequired[Network.RequestId]
    workerId: NotRequired[str]
    args: NotRequired[list[Runtime.RemoteObject]]


class ViolationSetting(TypedDict):
    name: Literal[
        "longTask",
        "longLayout",
        "blockedEvent",
        "blockedParser",
        "discouragedAPIUse",
        "handler",
        "recurringHandler",
    ]
    threshold: float


class StartViolationsReportParameters(TypedDict):
    config: list[ViolationSetting]


class EntryAddedEvent(TypedDict):
    entry: LogEntry


class Log(BaseDomain):
    """Provides access to log entries."""

    domain_name = "Log"

    async def clear(
        self,
        session_id: str | None = None,
    ) -> JsonObject:
        """Clears the log."""

        return await self._command("clear", None, session_id, {})

    async def disable(
        self,
        session_id: str | None = None,
    ) -> JsonObject:
        """Disables log domain, prevents further log entries from being reported to the client."""

        return await self._command("disable", None, session_id, {})

    async def enable(
        self,
        session_id: str | None = None,
    ) -> JsonObject:
        """Enables log domain, sends the entries collected so far to the client by means of the `entryAdded` notification."""

        return await self._command("enable", None, session_id, {})

    @overload
    async def startViolationsReport(
        self,
        params: StartViolationsReportParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def startViolationsReport(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[StartViolationsReportParameters],
    ) -> JsonObject: ...

    async def startViolationsReport(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """start violation reporting."""

        return await self._command("startViolationsReport", params, session_id, kwargs)

    async def stopViolationsReport(
        self,
        session_id: str | None = None,
    ) -> JsonObject:
        """Stop violation reporting."""

        return await self._command("stopViolationsReport", None, session_id, {})

    @overload
    def entryAdded(
        self,
        callback_or_session: EventCallback[EntryAddedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def entryAdded(
        self,
        callback_or_session: str,
        handler: EventCallback[EntryAddedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def entryAdded(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[EntryAddedEvent]: ...

    def entryAdded(
        self,
        callback_or_session: EventCallback[EntryAddedEvent] | str | None = None,
        handler: EventCallback[EntryAddedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[EntryAddedEvent] | Unsubscribe:
        """Issued when new message was logged."""

        return cast(
            Awaitable[EntryAddedEvent] | Unsubscribe,
            self._event(
                "entryAdded",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )


__all__ = [
    "EntryAddedEvent",
    "Log",
    "LogEntry",
    "StartViolationsReportParameters",
    "ViolationSetting",
]
