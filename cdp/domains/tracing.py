"""Generated bindings for the CDP Tracing domain. Do not edit manually."""

from __future__ import annotations

from collections.abc import Awaitable, Mapping
from typing import TYPE_CHECKING, Literal, TypeAlias, cast, overload

from typing_extensions import NotRequired, TypedDict, Unpack

from cdp.domain import Domain as BaseDomain, EventCallback, Unsubscribe
from cdp.types import JsonObject

if TYPE_CHECKING:
    from . import io as IO


MemoryDumpConfig: TypeAlias = JsonObject


class TraceConfig(TypedDict):
    recordMode: NotRequired[
        Literal[
            "recordUntilFull",
            "recordContinuously",
            "recordAsMuchAsPossible",
            "echoToConsole",
        ]
    ]
    traceBufferSizeInKb: NotRequired[float]
    enableSampling: NotRequired[bool]
    enableSystrace: NotRequired[bool]
    enableArgumentFilter: NotRequired[bool]
    includedCategories: NotRequired[list[str]]
    excludedCategories: NotRequired[list[str]]
    syntheticDelays: NotRequired[list[str]]
    memoryDumpConfig: NotRequired[MemoryDumpConfig]


StreamFormat: TypeAlias = Literal["json", "proto"]

StreamCompression: TypeAlias = Literal["none", "gzip"]

MemoryDumpLevelOfDetail: TypeAlias = Literal["background", "light", "detailed"]

TracingBackend: TypeAlias = Literal["auto", "chrome", "system"]


class GetCategoriesResult(TypedDict):
    categories: list[str]


class RecordClockSyncMarkerParameters(TypedDict):
    syncId: str


class RequestMemoryDumpParameters(TypedDict):
    deterministic: NotRequired[bool]
    levelOfDetail: NotRequired[MemoryDumpLevelOfDetail]


class RequestMemoryDumpResult(TypedDict):
    dumpGuid: str
    success: bool


class StartParameters(TypedDict):
    categories: NotRequired[str]
    options: NotRequired[str]
    bufferUsageReportingInterval: NotRequired[float]
    transferMode: NotRequired[Literal["ReportEvents", "ReturnAsStream"]]
    streamFormat: NotRequired[StreamFormat]
    streamCompression: NotRequired[StreamCompression]
    traceConfig: NotRequired[TraceConfig]
    perfettoConfig: NotRequired[str]
    tracingBackend: NotRequired[TracingBackend]


class BufferUsageEvent(TypedDict):
    percentFull: NotRequired[float]
    eventCount: NotRequired[float]
    value: NotRequired[float]


class DataCollectedEvent(TypedDict):
    value: list[JsonObject]


class TracingCompleteEvent(TypedDict):
    dataLossOccurred: bool
    stream: NotRequired[IO.StreamHandle]
    traceFormat: NotRequired[StreamFormat]
    streamCompression: NotRequired[StreamCompression]


class Tracing(BaseDomain):
    """The CDP Tracing domain."""

    domain_name = "Tracing"

    async def end(
        self,
        session_id: str | None = None,
    ) -> JsonObject:
        """Stop trace events collection."""

        return await self._command("end", None, session_id, {})

    async def getCategories(
        self,
        session_id: str | None = None,
    ) -> GetCategoriesResult:
        """Gets supported tracing categories."""

        return cast(
            GetCategoriesResult,
            await self._command("getCategories", None, session_id, {}),
        )

    @overload
    async def recordClockSyncMarker(
        self,
        params: RecordClockSyncMarkerParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def recordClockSyncMarker(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[RecordClockSyncMarkerParameters],
    ) -> JsonObject: ...

    async def recordClockSyncMarker(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Record a clock sync marker in the trace."""

        return await self._command("recordClockSyncMarker", params, session_id, kwargs)

    @overload
    async def requestMemoryDump(
        self,
        params: RequestMemoryDumpParameters,
        session_id: str | None = None,
    ) -> RequestMemoryDumpResult: ...

    @overload
    async def requestMemoryDump(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[RequestMemoryDumpParameters],
    ) -> RequestMemoryDumpResult: ...

    async def requestMemoryDump(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> RequestMemoryDumpResult:
        """Request a global memory dump."""

        return cast(
            RequestMemoryDumpResult,
            await self._command("requestMemoryDump", params, session_id, kwargs),
        )

    @overload
    async def start(
        self,
        params: StartParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def start(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[StartParameters],
    ) -> JsonObject: ...

    async def start(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Start trace events collection."""

        return await self._command("start", params, session_id, kwargs)

    @overload
    def bufferUsage(
        self,
        callback_or_session: EventCallback[BufferUsageEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def bufferUsage(
        self,
        callback_or_session: str,
        handler: EventCallback[BufferUsageEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def bufferUsage(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[BufferUsageEvent]: ...

    def bufferUsage(
        self,
        callback_or_session: EventCallback[BufferUsageEvent] | str | None = None,
        handler: EventCallback[BufferUsageEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[BufferUsageEvent] | Unsubscribe:
        """Wait for or subscribe to Tracing.bufferUsage."""

        return cast(
            Awaitable[BufferUsageEvent] | Unsubscribe,
            self._event(
                "bufferUsage",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def dataCollected(
        self,
        callback_or_session: EventCallback[DataCollectedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def dataCollected(
        self,
        callback_or_session: str,
        handler: EventCallback[DataCollectedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def dataCollected(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[DataCollectedEvent]: ...

    def dataCollected(
        self,
        callback_or_session: EventCallback[DataCollectedEvent] | str | None = None,
        handler: EventCallback[DataCollectedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[DataCollectedEvent] | Unsubscribe:
        """Contains a bucket of collected trace events. When tracing is stopped collected events will be sent as a sequence of dataCollected events followed by tracingComplete event."""

        return cast(
            Awaitable[DataCollectedEvent] | Unsubscribe,
            self._event(
                "dataCollected",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def tracingComplete(
        self,
        callback_or_session: EventCallback[TracingCompleteEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def tracingComplete(
        self,
        callback_or_session: str,
        handler: EventCallback[TracingCompleteEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def tracingComplete(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[TracingCompleteEvent]: ...

    def tracingComplete(
        self,
        callback_or_session: EventCallback[TracingCompleteEvent] | str | None = None,
        handler: EventCallback[TracingCompleteEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[TracingCompleteEvent] | Unsubscribe:
        """Signals that tracing is stopped and there is no trace buffers pending flush, all data were delivered via dataCollected events."""

        return cast(
            Awaitable[TracingCompleteEvent] | Unsubscribe,
            self._event(
                "tracingComplete",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )


__all__ = [
    "BufferUsageEvent",
    "DataCollectedEvent",
    "GetCategoriesResult",
    "MemoryDumpConfig",
    "MemoryDumpLevelOfDetail",
    "RecordClockSyncMarkerParameters",
    "RequestMemoryDumpParameters",
    "RequestMemoryDumpResult",
    "StartParameters",
    "StreamCompression",
    "StreamFormat",
    "TraceConfig",
    "Tracing",
    "TracingBackend",
    "TracingCompleteEvent",
]
