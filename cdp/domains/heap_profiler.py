"""Generated bindings for the CDP HeapProfiler domain. Do not edit manually."""

from __future__ import annotations

from collections.abc import Awaitable, Mapping
from typing import TYPE_CHECKING, TypeAlias, cast, overload

from typing_extensions import NotRequired, TypedDict, Unpack

from cdp.domain import Domain as BaseDomain, EventCallback, Unsubscribe
from cdp.types import JsonObject

if TYPE_CHECKING:
    from . import runtime as Runtime


HeapSnapshotObjectId: TypeAlias = str


class SamplingHeapProfileNode(TypedDict):
    callFrame: Runtime.CallFrame
    selfSize: float
    id: int
    children: list[SamplingHeapProfileNode]


class SamplingHeapProfileSample(TypedDict):
    size: float
    nodeId: int
    ordinal: float


class SamplingHeapProfile(TypedDict):
    head: SamplingHeapProfileNode
    samples: list[SamplingHeapProfileSample]


class AddInspectedHeapObjectParameters(TypedDict):
    heapObjectId: HeapSnapshotObjectId


class GetHeapObjectIdParameters(TypedDict):
    objectId: Runtime.RemoteObjectId


class GetHeapObjectIdResult(TypedDict):
    heapSnapshotObjectId: HeapSnapshotObjectId


class GetObjectByHeapObjectIdParameters(TypedDict):
    objectId: HeapSnapshotObjectId
    objectGroup: NotRequired[str]


class GetObjectByHeapObjectIdResult(TypedDict):
    result: Runtime.RemoteObject


class GetSamplingProfileResult(TypedDict):
    profile: SamplingHeapProfile


class StartSamplingParameters(TypedDict):
    samplingInterval: NotRequired[float]
    stackDepth: NotRequired[float]
    includeObjectsCollectedByMajorGC: NotRequired[bool]
    includeObjectsCollectedByMinorGC: NotRequired[bool]


class StartTrackingHeapObjectsParameters(TypedDict):
    trackAllocations: NotRequired[bool]


class StopSamplingResult(TypedDict):
    profile: SamplingHeapProfile


class StopTrackingHeapObjectsParameters(TypedDict):
    reportProgress: NotRequired[bool]
    treatGlobalObjectsAsRoots: NotRequired[bool]
    captureNumericValue: NotRequired[bool]
    exposeInternals: NotRequired[bool]


class TakeHeapSnapshotParameters(TypedDict):
    reportProgress: NotRequired[bool]
    treatGlobalObjectsAsRoots: NotRequired[bool]
    captureNumericValue: NotRequired[bool]
    exposeInternals: NotRequired[bool]


class AddHeapSnapshotChunkEvent(TypedDict):
    chunk: str


class HeapStatsUpdateEvent(TypedDict):
    statsUpdate: list[int]


class LastSeenObjectIdEvent(TypedDict):
    lastSeenObjectId: int
    timestamp: float


class ReportHeapSnapshotProgressEvent(TypedDict):
    done: int
    total: int
    finished: NotRequired[bool]


class HeapProfiler(BaseDomain):
    """The CDP HeapProfiler domain."""

    domain_name = "HeapProfiler"

    @overload
    async def addInspectedHeapObject(
        self,
        params: AddInspectedHeapObjectParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def addInspectedHeapObject(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[AddInspectedHeapObjectParameters],
    ) -> JsonObject: ...

    async def addInspectedHeapObject(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Enables console to refer to the node with given id via $x (see Command Line API for more details $x functions)."""

        return await self._command("addInspectedHeapObject", params, session_id, kwargs)

    async def collectGarbage(
        self,
        session_id: str | None = None,
    ) -> JsonObject:
        """Send HeapProfiler.collectGarbage."""

        return await self._command("collectGarbage", None, session_id, {})

    async def disable(
        self,
        session_id: str | None = None,
    ) -> JsonObject:
        """Send HeapProfiler.disable."""

        return await self._command("disable", None, session_id, {})

    async def enable(
        self,
        session_id: str | None = None,
    ) -> JsonObject:
        """Send HeapProfiler.enable."""

        return await self._command("enable", None, session_id, {})

    @overload
    async def getHeapObjectId(
        self,
        params: GetHeapObjectIdParameters,
        session_id: str | None = None,
    ) -> GetHeapObjectIdResult: ...

    @overload
    async def getHeapObjectId(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[GetHeapObjectIdParameters],
    ) -> GetHeapObjectIdResult: ...

    async def getHeapObjectId(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> GetHeapObjectIdResult:
        """Send HeapProfiler.getHeapObjectId."""

        return cast(
            GetHeapObjectIdResult,
            await self._command("getHeapObjectId", params, session_id, kwargs),
        )

    @overload
    async def getObjectByHeapObjectId(
        self,
        params: GetObjectByHeapObjectIdParameters,
        session_id: str | None = None,
    ) -> GetObjectByHeapObjectIdResult: ...

    @overload
    async def getObjectByHeapObjectId(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[GetObjectByHeapObjectIdParameters],
    ) -> GetObjectByHeapObjectIdResult: ...

    async def getObjectByHeapObjectId(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> GetObjectByHeapObjectIdResult:
        """Send HeapProfiler.getObjectByHeapObjectId."""

        return cast(
            GetObjectByHeapObjectIdResult,
            await self._command("getObjectByHeapObjectId", params, session_id, kwargs),
        )

    async def getSamplingProfile(
        self,
        session_id: str | None = None,
    ) -> GetSamplingProfileResult:
        """Send HeapProfiler.getSamplingProfile."""

        return cast(
            GetSamplingProfileResult,
            await self._command("getSamplingProfile", None, session_id, {}),
        )

    @overload
    async def startSampling(
        self,
        params: StartSamplingParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def startSampling(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[StartSamplingParameters],
    ) -> JsonObject: ...

    async def startSampling(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Send HeapProfiler.startSampling."""

        return await self._command("startSampling", params, session_id, kwargs)

    @overload
    async def startTrackingHeapObjects(
        self,
        params: StartTrackingHeapObjectsParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def startTrackingHeapObjects(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[StartTrackingHeapObjectsParameters],
    ) -> JsonObject: ...

    async def startTrackingHeapObjects(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Send HeapProfiler.startTrackingHeapObjects."""

        return await self._command(
            "startTrackingHeapObjects", params, session_id, kwargs
        )

    async def stopSampling(
        self,
        session_id: str | None = None,
    ) -> StopSamplingResult:
        """Send HeapProfiler.stopSampling."""

        return cast(
            StopSamplingResult,
            await self._command("stopSampling", None, session_id, {}),
        )

    @overload
    async def stopTrackingHeapObjects(
        self,
        params: StopTrackingHeapObjectsParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def stopTrackingHeapObjects(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[StopTrackingHeapObjectsParameters],
    ) -> JsonObject: ...

    async def stopTrackingHeapObjects(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Send HeapProfiler.stopTrackingHeapObjects."""

        return await self._command(
            "stopTrackingHeapObjects", params, session_id, kwargs
        )

    @overload
    async def takeHeapSnapshot(
        self,
        params: TakeHeapSnapshotParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def takeHeapSnapshot(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[TakeHeapSnapshotParameters],
    ) -> JsonObject: ...

    async def takeHeapSnapshot(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Send HeapProfiler.takeHeapSnapshot."""

        return await self._command("takeHeapSnapshot", params, session_id, kwargs)

    @overload
    def addHeapSnapshotChunk(
        self,
        callback_or_session: EventCallback[AddHeapSnapshotChunkEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def addHeapSnapshotChunk(
        self,
        callback_or_session: str,
        handler: EventCallback[AddHeapSnapshotChunkEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def addHeapSnapshotChunk(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[AddHeapSnapshotChunkEvent]: ...

    def addHeapSnapshotChunk(
        self,
        callback_or_session: EventCallback[AddHeapSnapshotChunkEvent]
        | str
        | None = None,
        handler: EventCallback[AddHeapSnapshotChunkEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[AddHeapSnapshotChunkEvent] | Unsubscribe:
        """Wait for or subscribe to HeapProfiler.addHeapSnapshotChunk."""

        return cast(
            Awaitable[AddHeapSnapshotChunkEvent] | Unsubscribe,
            self._event(
                "addHeapSnapshotChunk",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def heapStatsUpdate(
        self,
        callback_or_session: EventCallback[HeapStatsUpdateEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def heapStatsUpdate(
        self,
        callback_or_session: str,
        handler: EventCallback[HeapStatsUpdateEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def heapStatsUpdate(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[HeapStatsUpdateEvent]: ...

    def heapStatsUpdate(
        self,
        callback_or_session: EventCallback[HeapStatsUpdateEvent] | str | None = None,
        handler: EventCallback[HeapStatsUpdateEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[HeapStatsUpdateEvent] | Unsubscribe:
        """If heap objects tracking has been started then backend may send update for one or more fragments"""

        return cast(
            Awaitable[HeapStatsUpdateEvent] | Unsubscribe,
            self._event(
                "heapStatsUpdate",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def lastSeenObjectId(
        self,
        callback_or_session: EventCallback[LastSeenObjectIdEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def lastSeenObjectId(
        self,
        callback_or_session: str,
        handler: EventCallback[LastSeenObjectIdEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def lastSeenObjectId(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[LastSeenObjectIdEvent]: ...

    def lastSeenObjectId(
        self,
        callback_or_session: EventCallback[LastSeenObjectIdEvent] | str | None = None,
        handler: EventCallback[LastSeenObjectIdEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[LastSeenObjectIdEvent] | Unsubscribe:
        """If heap objects tracking has been started then backend regularly sends a current value for last seen object id and corresponding timestamp. If the were changes in the heap since last event then one or more heapStatsUpdate events will be sent before a new lastSeenObjectId event."""

        return cast(
            Awaitable[LastSeenObjectIdEvent] | Unsubscribe,
            self._event(
                "lastSeenObjectId",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def reportHeapSnapshotProgress(
        self,
        callback_or_session: EventCallback[ReportHeapSnapshotProgressEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def reportHeapSnapshotProgress(
        self,
        callback_or_session: str,
        handler: EventCallback[ReportHeapSnapshotProgressEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def reportHeapSnapshotProgress(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[ReportHeapSnapshotProgressEvent]: ...

    def reportHeapSnapshotProgress(
        self,
        callback_or_session: EventCallback[ReportHeapSnapshotProgressEvent]
        | str
        | None = None,
        handler: EventCallback[ReportHeapSnapshotProgressEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[ReportHeapSnapshotProgressEvent] | Unsubscribe:
        """Wait for or subscribe to HeapProfiler.reportHeapSnapshotProgress."""

        return cast(
            Awaitable[ReportHeapSnapshotProgressEvent] | Unsubscribe,
            self._event(
                "reportHeapSnapshotProgress",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def resetProfiles(
        self,
        callback_or_session: EventCallback[JsonObject],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def resetProfiles(
        self,
        callback_or_session: str,
        handler: EventCallback[JsonObject],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def resetProfiles(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[JsonObject]: ...

    def resetProfiles(
        self,
        callback_or_session: EventCallback[JsonObject] | str | None = None,
        handler: EventCallback[JsonObject] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[JsonObject] | Unsubscribe:
        """Wait for or subscribe to HeapProfiler.resetProfiles."""

        return self._event(
            "resetProfiles",
            cast(EventCallback[Mapping[str, object]] | str | None, callback_or_session),
            cast(EventCallback[Mapping[str, object]] | None, handler),
            session_id,
        )


__all__ = [
    "AddHeapSnapshotChunkEvent",
    "AddInspectedHeapObjectParameters",
    "GetHeapObjectIdParameters",
    "GetHeapObjectIdResult",
    "GetObjectByHeapObjectIdParameters",
    "GetObjectByHeapObjectIdResult",
    "GetSamplingProfileResult",
    "HeapProfiler",
    "HeapSnapshotObjectId",
    "HeapStatsUpdateEvent",
    "LastSeenObjectIdEvent",
    "ReportHeapSnapshotProgressEvent",
    "SamplingHeapProfile",
    "SamplingHeapProfileNode",
    "SamplingHeapProfileSample",
    "StartSamplingParameters",
    "StartTrackingHeapObjectsParameters",
    "StopSamplingResult",
    "StopTrackingHeapObjectsParameters",
    "TakeHeapSnapshotParameters",
]
