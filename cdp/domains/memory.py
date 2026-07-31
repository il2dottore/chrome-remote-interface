"""Generated bindings for the CDP Memory domain. Do not edit manually."""

from __future__ import annotations

from collections.abc import Mapping
from typing import Literal, TypeAlias, cast, overload

from typing_extensions import NotRequired, TypedDict, Unpack

from cdp.domain import Domain as BaseDomain
from cdp.types import JsonObject


PressureLevel: TypeAlias = Literal["moderate", "critical"]


class SamplingProfileNode(TypedDict):
    size: float
    total: float
    stack: list[str]


class SamplingProfile(TypedDict):
    samples: list[SamplingProfileNode]
    modules: list[Module]


class Module(TypedDict):
    name: str
    uuid: str
    baseAddress: str
    size: float


class DOMCounter(TypedDict):
    name: str
    count: int


class GetDOMCountersResult(TypedDict):
    documents: int
    nodes: int
    jsEventListeners: int


class GetDOMCountersForLeakDetectionResult(TypedDict):
    counters: list[DOMCounter]


class SetPressureNotificationsSuppressedParameters(TypedDict):
    suppressed: bool


class SimulatePressureNotificationParameters(TypedDict):
    level: PressureLevel


class StartSamplingParameters(TypedDict):
    samplingInterval: NotRequired[int]
    suppressRandomness: NotRequired[bool]


class GetAllTimeSamplingProfileResult(TypedDict):
    profile: SamplingProfile


class GetBrowserSamplingProfileResult(TypedDict):
    profile: SamplingProfile


class GetSamplingProfileResult(TypedDict):
    profile: SamplingProfile


class Memory(BaseDomain):
    """The CDP Memory domain."""

    domain_name = "Memory"

    async def getDOMCounters(
        self,
        session_id: str | None = None,
    ) -> GetDOMCountersResult:
        """Retruns current DOM object counters."""

        return cast(
            GetDOMCountersResult,
            await self._command("getDOMCounters", None, session_id, {}),
        )

    async def getDOMCountersForLeakDetection(
        self,
        session_id: str | None = None,
    ) -> GetDOMCountersForLeakDetectionResult:
        """Retruns DOM object counters after preparing renderer for leak detection."""

        return cast(
            GetDOMCountersForLeakDetectionResult,
            await self._command("getDOMCountersForLeakDetection", None, session_id, {}),
        )

    async def prepareForLeakDetection(
        self,
        session_id: str | None = None,
    ) -> JsonObject:
        """Prepares for leak detection by terminating workers, stopping spellcheckers, dropping non-essential internal caches, running garbage collections, etc."""

        return await self._command("prepareForLeakDetection", None, session_id, {})

    async def forciblyPurgeJavaScriptMemory(
        self,
        session_id: str | None = None,
    ) -> JsonObject:
        """Simulate OomIntervention by purging V8 memory."""

        return await self._command(
            "forciblyPurgeJavaScriptMemory", None, session_id, {}
        )

    @overload
    async def setPressureNotificationsSuppressed(
        self,
        params: SetPressureNotificationsSuppressedParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def setPressureNotificationsSuppressed(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetPressureNotificationsSuppressedParameters],
    ) -> JsonObject: ...

    async def setPressureNotificationsSuppressed(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Enable/disable suppressing memory pressure notifications in all processes."""

        return await self._command(
            "setPressureNotificationsSuppressed", params, session_id, kwargs
        )

    @overload
    async def simulatePressureNotification(
        self,
        params: SimulatePressureNotificationParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def simulatePressureNotification(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SimulatePressureNotificationParameters],
    ) -> JsonObject: ...

    async def simulatePressureNotification(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Simulate a memory pressure notification in all processes."""

        return await self._command(
            "simulatePressureNotification", params, session_id, kwargs
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
        """Start collecting native memory profile."""

        return await self._command("startSampling", params, session_id, kwargs)

    async def stopSampling(
        self,
        session_id: str | None = None,
    ) -> JsonObject:
        """Stop collecting native memory profile."""

        return await self._command("stopSampling", None, session_id, {})

    async def getAllTimeSamplingProfile(
        self,
        session_id: str | None = None,
    ) -> GetAllTimeSamplingProfileResult:
        """Retrieve native memory allocations profile collected since renderer process startup."""

        return cast(
            GetAllTimeSamplingProfileResult,
            await self._command("getAllTimeSamplingProfile", None, session_id, {}),
        )

    async def getBrowserSamplingProfile(
        self,
        session_id: str | None = None,
    ) -> GetBrowserSamplingProfileResult:
        """Retrieve native memory allocations profile collected since browser process startup."""

        return cast(
            GetBrowserSamplingProfileResult,
            await self._command("getBrowserSamplingProfile", None, session_id, {}),
        )

    async def getSamplingProfile(
        self,
        session_id: str | None = None,
    ) -> GetSamplingProfileResult:
        """Retrieve native memory allocations profile collected since last `startSampling` call."""

        return cast(
            GetSamplingProfileResult,
            await self._command("getSamplingProfile", None, session_id, {}),
        )


__all__ = [
    "DOMCounter",
    "GetAllTimeSamplingProfileResult",
    "GetBrowserSamplingProfileResult",
    "GetDOMCountersForLeakDetectionResult",
    "GetDOMCountersResult",
    "GetSamplingProfileResult",
    "Memory",
    "Module",
    "PressureLevel",
    "SamplingProfile",
    "SamplingProfileNode",
    "SetPressureNotificationsSuppressedParameters",
    "SimulatePressureNotificationParameters",
    "StartSamplingParameters",
]
