"""Generated bindings for the CDP SystemInfo domain. Do not edit manually."""

from __future__ import annotations

from collections.abc import Mapping
from typing import Literal, TypeAlias, cast, overload

from typing_extensions import NotRequired, TypedDict, Unpack

from cdp.domain import Domain as BaseDomain
from cdp.types import JsonObject


class GPUDevice(TypedDict):
    vendorId: float
    deviceId: float
    subSysId: NotRequired[float]
    revision: NotRequired[float]
    vendorString: str
    deviceString: str
    driverVendor: str
    driverVersion: str


class Size(TypedDict):
    width: int
    height: int


class VideoDecodeAcceleratorCapability(TypedDict):
    profile: str
    maxResolution: Size
    minResolution: Size


class VideoEncodeAcceleratorCapability(TypedDict):
    profile: str
    maxResolution: Size
    maxFramerateNumerator: int
    maxFramerateDenominator: int


SubsamplingFormat: TypeAlias = Literal["yuv420", "yuv422", "yuv444"]

ImageType: TypeAlias = Literal["jpeg", "webp", "unknown"]


class GPUInfo(TypedDict):
    devices: list[GPUDevice]
    auxAttributes: NotRequired[JsonObject]
    featureStatus: NotRequired[JsonObject]
    driverBugWorkarounds: list[str]
    videoDecoding: list[VideoDecodeAcceleratorCapability]
    videoEncoding: list[VideoEncodeAcceleratorCapability]


class ProcessInfo(TypedDict):
    type: str
    id: int
    cpuTime: float


class GetInfoResult(TypedDict):
    gpu: GPUInfo
    modelName: str
    modelVersion: str
    commandLine: str


class GetFeatureStateParameters(TypedDict):
    featureState: str


class GetFeatureStateResult(TypedDict):
    featureEnabled: bool


class GetProcessInfoResult(TypedDict):
    processInfo: list[ProcessInfo]


class SystemInfo(BaseDomain):
    """The SystemInfo domain defines methods and events for querying low-level system information."""

    domain_name = "SystemInfo"

    async def getInfo(
        self,
        session_id: str | None = None,
    ) -> GetInfoResult:
        """Returns information about the system."""

        return cast(GetInfoResult, await self._command("getInfo", None, session_id, {}))

    @overload
    async def getFeatureState(
        self,
        params: GetFeatureStateParameters,
        session_id: str | None = None,
    ) -> GetFeatureStateResult: ...

    @overload
    async def getFeatureState(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[GetFeatureStateParameters],
    ) -> GetFeatureStateResult: ...

    async def getFeatureState(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> GetFeatureStateResult:
        """Returns information about the feature state."""

        return cast(
            GetFeatureStateResult,
            await self._command("getFeatureState", params, session_id, kwargs),
        )

    async def getProcessInfo(
        self,
        session_id: str | None = None,
    ) -> GetProcessInfoResult:
        """Returns information about all running processes."""

        return cast(
            GetProcessInfoResult,
            await self._command("getProcessInfo", None, session_id, {}),
        )


__all__ = [
    "GPUDevice",
    "GPUInfo",
    "GetFeatureStateParameters",
    "GetFeatureStateResult",
    "GetInfoResult",
    "GetProcessInfoResult",
    "ImageType",
    "ProcessInfo",
    "Size",
    "SubsamplingFormat",
    "SystemInfo",
    "VideoDecodeAcceleratorCapability",
    "VideoEncodeAcceleratorCapability",
]
