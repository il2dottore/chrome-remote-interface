"""Generated bindings for the CDP Profiler domain. Do not edit manually."""

from __future__ import annotations

from collections.abc import Awaitable, Mapping
from typing import TYPE_CHECKING, cast, overload

from typing_extensions import NotRequired, TypedDict, Unpack

from cdp.domain import Domain as BaseDomain, EventCallback, Unsubscribe
from cdp.types import JsonObject

if TYPE_CHECKING:
    from . import debugger as Debugger
    from . import runtime as Runtime


class ProfileNode(TypedDict):
    id: int
    callFrame: Runtime.CallFrame
    hitCount: NotRequired[int]
    children: NotRequired[list[int]]
    deoptReason: NotRequired[str]
    positionTicks: NotRequired[list[PositionTickInfo]]


class Profile(TypedDict):
    nodes: list[ProfileNode]
    startTime: float
    endTime: float
    samples: NotRequired[list[int]]
    timeDeltas: NotRequired[list[int]]


class PositionTickInfo(TypedDict):
    line: int
    ticks: int


class CoverageRange(TypedDict):
    startOffset: int
    endOffset: int
    count: int


class FunctionCoverage(TypedDict):
    functionName: str
    ranges: list[CoverageRange]
    isBlockCoverage: bool


class ScriptCoverage(TypedDict):
    scriptId: Runtime.ScriptId
    url: str
    functions: list[FunctionCoverage]


class GetBestEffortCoverageResult(TypedDict):
    result: list[ScriptCoverage]


class SetSamplingIntervalParameters(TypedDict):
    interval: int


class StartPreciseCoverageParameters(TypedDict):
    callCount: NotRequired[bool]
    detailed: NotRequired[bool]
    allowTriggeredUpdates: NotRequired[bool]


class StartPreciseCoverageResult(TypedDict):
    timestamp: float


class StopResult(TypedDict):
    profile: Profile


class TakePreciseCoverageResult(TypedDict):
    result: list[ScriptCoverage]
    timestamp: float


class ConsoleProfileFinishedEvent(TypedDict):
    id: str
    location: Debugger.Location
    profile: Profile
    title: NotRequired[str]


class ConsoleProfileStartedEvent(TypedDict):
    id: str
    location: Debugger.Location
    title: NotRequired[str]


class PreciseCoverageDeltaUpdateEvent(TypedDict):
    timestamp: float
    occasion: str
    result: list[ScriptCoverage]


class Profiler(BaseDomain):
    """The CDP Profiler domain."""

    domain_name = "Profiler"

    async def disable(
        self,
        session_id: str | None = None,
    ) -> JsonObject:
        """Send Profiler.disable."""

        return await self._command("disable", None, session_id, {})

    async def enable(
        self,
        session_id: str | None = None,
    ) -> JsonObject:
        """Send Profiler.enable."""

        return await self._command("enable", None, session_id, {})

    async def getBestEffortCoverage(
        self,
        session_id: str | None = None,
    ) -> GetBestEffortCoverageResult:
        """Collect coverage data for the current isolate. The coverage data may be incomplete due to garbage collection."""

        return cast(
            GetBestEffortCoverageResult,
            await self._command("getBestEffortCoverage", None, session_id, {}),
        )

    @overload
    async def setSamplingInterval(
        self,
        params: SetSamplingIntervalParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def setSamplingInterval(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetSamplingIntervalParameters],
    ) -> JsonObject: ...

    async def setSamplingInterval(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Changes CPU profiler sampling interval. Must be called before CPU profiles recording started."""

        return await self._command("setSamplingInterval", params, session_id, kwargs)

    async def start(
        self,
        session_id: str | None = None,
    ) -> JsonObject:
        """Send Profiler.start."""

        return await self._command("start", None, session_id, {})

    @overload
    async def startPreciseCoverage(
        self,
        params: StartPreciseCoverageParameters,
        session_id: str | None = None,
    ) -> StartPreciseCoverageResult: ...

    @overload
    async def startPreciseCoverage(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[StartPreciseCoverageParameters],
    ) -> StartPreciseCoverageResult: ...

    async def startPreciseCoverage(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> StartPreciseCoverageResult:
        """Enable precise code coverage. Coverage data for JavaScript executed before enabling precise code coverage may be incomplete. Enabling prevents running optimized code and resets execution counters."""

        return cast(
            StartPreciseCoverageResult,
            await self._command("startPreciseCoverage", params, session_id, kwargs),
        )

    async def stop(
        self,
        session_id: str | None = None,
    ) -> StopResult:
        """Send Profiler.stop."""

        return cast(StopResult, await self._command("stop", None, session_id, {}))

    async def stopPreciseCoverage(
        self,
        session_id: str | None = None,
    ) -> JsonObject:
        """Disable precise code coverage. Disabling releases unnecessary execution count records and allows executing optimized code."""

        return await self._command("stopPreciseCoverage", None, session_id, {})

    async def takePreciseCoverage(
        self,
        session_id: str | None = None,
    ) -> TakePreciseCoverageResult:
        """Collect coverage data for the current isolate, and resets execution counters. Precise code coverage needs to have started."""

        return cast(
            TakePreciseCoverageResult,
            await self._command("takePreciseCoverage", None, session_id, {}),
        )

    @overload
    def consoleProfileFinished(
        self,
        callback_or_session: EventCallback[ConsoleProfileFinishedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def consoleProfileFinished(
        self,
        callback_or_session: str,
        handler: EventCallback[ConsoleProfileFinishedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def consoleProfileFinished(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[ConsoleProfileFinishedEvent]: ...

    def consoleProfileFinished(
        self,
        callback_or_session: EventCallback[ConsoleProfileFinishedEvent]
        | str
        | None = None,
        handler: EventCallback[ConsoleProfileFinishedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[ConsoleProfileFinishedEvent] | Unsubscribe:
        """Wait for or subscribe to Profiler.consoleProfileFinished."""

        return cast(
            Awaitable[ConsoleProfileFinishedEvent] | Unsubscribe,
            self._event(
                "consoleProfileFinished",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def consoleProfileStarted(
        self,
        callback_or_session: EventCallback[ConsoleProfileStartedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def consoleProfileStarted(
        self,
        callback_or_session: str,
        handler: EventCallback[ConsoleProfileStartedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def consoleProfileStarted(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[ConsoleProfileStartedEvent]: ...

    def consoleProfileStarted(
        self,
        callback_or_session: EventCallback[ConsoleProfileStartedEvent]
        | str
        | None = None,
        handler: EventCallback[ConsoleProfileStartedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[ConsoleProfileStartedEvent] | Unsubscribe:
        """Sent when new profile recording is started using console.profile() call."""

        return cast(
            Awaitable[ConsoleProfileStartedEvent] | Unsubscribe,
            self._event(
                "consoleProfileStarted",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def preciseCoverageDeltaUpdate(
        self,
        callback_or_session: EventCallback[PreciseCoverageDeltaUpdateEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def preciseCoverageDeltaUpdate(
        self,
        callback_or_session: str,
        handler: EventCallback[PreciseCoverageDeltaUpdateEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def preciseCoverageDeltaUpdate(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[PreciseCoverageDeltaUpdateEvent]: ...

    def preciseCoverageDeltaUpdate(
        self,
        callback_or_session: EventCallback[PreciseCoverageDeltaUpdateEvent]
        | str
        | None = None,
        handler: EventCallback[PreciseCoverageDeltaUpdateEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[PreciseCoverageDeltaUpdateEvent] | Unsubscribe:
        """Reports coverage delta since the last poll (either from an event like this, or from `takePreciseCoverage` for the current isolate. May only be sent if precise code coverage has been started. This event can be trigged by the embedder to, for example, trigger collection of coverage data immediately at a certain point in time."""

        return cast(
            Awaitable[PreciseCoverageDeltaUpdateEvent] | Unsubscribe,
            self._event(
                "preciseCoverageDeltaUpdate",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )


__all__ = [
    "ConsoleProfileFinishedEvent",
    "ConsoleProfileStartedEvent",
    "CoverageRange",
    "FunctionCoverage",
    "GetBestEffortCoverageResult",
    "PositionTickInfo",
    "PreciseCoverageDeltaUpdateEvent",
    "Profile",
    "ProfileNode",
    "Profiler",
    "ScriptCoverage",
    "SetSamplingIntervalParameters",
    "StartPreciseCoverageParameters",
    "StartPreciseCoverageResult",
    "StopResult",
    "TakePreciseCoverageResult",
]
