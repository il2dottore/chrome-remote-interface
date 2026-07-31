"""Generated bindings for the CDP Emulation domain. Do not edit manually."""

from __future__ import annotations

from collections.abc import Awaitable, Mapping
from typing import TYPE_CHECKING, Literal, TypeAlias, cast, overload

from typing_extensions import NotRequired, TypedDict, Unpack

from cdp.domain import Domain as BaseDomain, EventCallback, Unsubscribe
from cdp.types import JsonObject

if TYPE_CHECKING:
    from . import dom as DOM
    from . import network as Network
    from . import page as Page


class SafeAreaInsets(TypedDict):
    top: NotRequired[int]
    topMax: NotRequired[int]
    left: NotRequired[int]
    leftMax: NotRequired[int]
    bottom: NotRequired[int]
    bottomMax: NotRequired[int]
    right: NotRequired[int]
    rightMax: NotRequired[int]


class ScreenOrientation(TypedDict):
    type: Literal[
        "portraitPrimary", "portraitSecondary", "landscapePrimary", "landscapeSecondary"
    ]
    angle: int


class DisplayFeature(TypedDict):
    orientation: Literal["vertical", "horizontal"]
    offset: int
    maskLength: int


class DevicePosture(TypedDict):
    type: Literal["continuous", "folded"]


class MediaFeature(TypedDict):
    name: str
    value: str


VirtualTimePolicy: TypeAlias = Literal[
    "advance", "pause", "pauseIfNetworkFetchesPending"
]


class UserAgentBrandVersion(TypedDict):
    brand: str
    version: str


class UserAgentMetadata(TypedDict):
    brands: NotRequired[list[UserAgentBrandVersion]]
    fullVersionList: NotRequired[list[UserAgentBrandVersion]]
    fullVersion: NotRequired[str]
    platform: str
    platformVersion: str
    architecture: str
    model: str
    mobile: bool
    bitness: NotRequired[str]
    wow64: NotRequired[bool]
    formFactors: NotRequired[list[str]]


SensorType: TypeAlias = Literal[
    "absolute-orientation",
    "accelerometer",
    "ambient-light",
    "gravity",
    "gyroscope",
    "linear-acceleration",
    "magnetometer",
    "relative-orientation",
]


class SensorMetadata(TypedDict):
    available: NotRequired[bool]
    minimumFrequency: NotRequired[float]
    maximumFrequency: NotRequired[float]


class SensorReadingSingle(TypedDict):
    value: float


class SensorReadingXYZ(TypedDict):
    x: float
    y: float
    z: float


class SensorReadingQuaternion(TypedDict):
    x: float
    y: float
    z: float
    w: float


class SensorReading(TypedDict):
    single: NotRequired[SensorReadingSingle]
    xyz: NotRequired[SensorReadingXYZ]
    quaternion: NotRequired[SensorReadingQuaternion]


PressureSource: TypeAlias = Literal["cpu"]

PressureState: TypeAlias = Literal["nominal", "fair", "serious", "critical"]


class PressureMetadata(TypedDict):
    available: NotRequired[bool]


class WorkAreaInsets(TypedDict):
    top: NotRequired[int]
    left: NotRequired[int]
    bottom: NotRequired[int]
    right: NotRequired[int]


ScreenId: TypeAlias = str


class ScreenInfo(TypedDict):
    left: int
    top: int
    width: int
    height: int
    availLeft: int
    availTop: int
    availWidth: int
    availHeight: int
    devicePixelRatio: float
    orientation: ScreenOrientation
    colorDepth: int
    isExtended: bool
    isInternal: bool
    isPrimary: bool
    label: str
    id: ScreenId


DisabledImageType: TypeAlias = Literal["avif", "jxl", "webp"]


class CanEmulateResult(TypedDict):
    result: bool


class SetFocusEmulationEnabledParameters(TypedDict):
    enabled: bool


class SetAutoDarkModeOverrideParameters(TypedDict):
    enabled: NotRequired[bool]


class SetCPUThrottlingRateParameters(TypedDict):
    rate: float


class SetDefaultBackgroundColorOverrideParameters(TypedDict):
    color: NotRequired[DOM.RGBA]


class SetSafeAreaInsetsOverrideParameters(TypedDict):
    insets: SafeAreaInsets


class SetDeviceMetricsOverrideParameters(TypedDict):
    width: int
    height: int
    deviceScaleFactor: float
    mobile: bool
    scale: NotRequired[float]
    screenWidth: NotRequired[int]
    screenHeight: NotRequired[int]
    positionX: NotRequired[int]
    positionY: NotRequired[int]
    dontSetVisibleSize: NotRequired[bool]
    screenOrientation: NotRequired[ScreenOrientation]
    viewport: NotRequired[Page.Viewport]
    displayFeature: NotRequired[DisplayFeature]
    devicePosture: NotRequired[DevicePosture]
    scrollbarType: NotRequired[Literal["overlay", "default"]]
    screenOrientationLockEmulation: NotRequired[bool]


class SetDevicePostureOverrideParameters(TypedDict):
    posture: DevicePosture


class SetDisplayFeaturesOverrideParameters(TypedDict):
    features: list[DisplayFeature]


class SetScrollbarsHiddenParameters(TypedDict):
    hidden: bool


class SetDocumentCookieDisabledParameters(TypedDict):
    disabled: bool


class SetEmitTouchEventsForMouseParameters(TypedDict):
    enabled: bool
    configuration: NotRequired[Literal["mobile", "desktop"]]


class SetEmulatedMediaParameters(TypedDict):
    media: NotRequired[str]
    features: NotRequired[list[MediaFeature]]


class SetEmulatedVisionDeficiencyParameters(TypedDict):
    type: Literal[
        "none",
        "blurredVision",
        "reducedContrast",
        "achromatopsia",
        "deuteranopia",
        "protanopia",
        "tritanopia",
    ]


class SetEmulatedOSTextScaleParameters(TypedDict):
    scale: NotRequired[float]


class SetGeolocationOverrideParameters(TypedDict):
    latitude: NotRequired[float]
    longitude: NotRequired[float]
    accuracy: NotRequired[float]
    altitude: NotRequired[float]
    altitudeAccuracy: NotRequired[float]
    heading: NotRequired[float]
    speed: NotRequired[float]


class GetOverriddenSensorInformationParameters(TypedDict):
    type: SensorType


class GetOverriddenSensorInformationResult(TypedDict):
    requestedSamplingFrequency: float


class SetSensorOverrideEnabledParameters(TypedDict):
    enabled: bool
    type: SensorType
    metadata: NotRequired[SensorMetadata]


class SetSensorOverrideReadingsParameters(TypedDict):
    type: SensorType
    reading: SensorReading


class SetPressureSourceOverrideEnabledParameters(TypedDict):
    enabled: bool
    source: PressureSource
    metadata: NotRequired[PressureMetadata]


class SetPressureStateOverrideParameters(TypedDict):
    source: PressureSource
    state: PressureState


class SetIdleOverrideParameters(TypedDict):
    isUserActive: bool
    isScreenUnlocked: bool


class SetNavigatorOverridesParameters(TypedDict):
    platform: str


class SetPageScaleFactorParameters(TypedDict):
    pageScaleFactor: float


class SetScriptExecutionDisabledParameters(TypedDict):
    value: bool


class SetTouchEmulationEnabledParameters(TypedDict):
    enabled: bool
    maxTouchPoints: NotRequired[int]


class SetVirtualTimePolicyParameters(TypedDict):
    policy: VirtualTimePolicy
    budget: NotRequired[float]
    maxVirtualTimeTaskStarvationCount: NotRequired[int]
    initialVirtualTime: NotRequired[Network.TimeSinceEpoch]


class SetVirtualTimePolicyResult(TypedDict):
    virtualTimeTicksBase: float


class SetLocaleOverrideParameters(TypedDict):
    locale: NotRequired[str]


class SetTimezoneOverrideParameters(TypedDict):
    timezoneId: str


class SetVisibleSizeParameters(TypedDict):
    width: int
    height: int


class SetDisabledImageTypesParameters(TypedDict):
    imageTypes: list[DisabledImageType]


class SetDataSaverOverrideParameters(TypedDict):
    dataSaverEnabled: NotRequired[bool]


class SetHardwareConcurrencyOverrideParameters(TypedDict):
    hardwareConcurrency: int


class SetUserAgentOverrideParameters(TypedDict):
    userAgent: str
    acceptLanguage: NotRequired[str]
    platform: NotRequired[str]
    userAgentMetadata: NotRequired[UserAgentMetadata]


class SetAutomationOverrideParameters(TypedDict):
    enabled: bool


class SetSmallViewportHeightDifferenceOverrideParameters(TypedDict):
    difference: int


class GetScreenInfosResult(TypedDict):
    screenInfos: list[ScreenInfo]


class AddScreenParameters(TypedDict):
    left: int
    top: int
    width: int
    height: int
    workAreaInsets: NotRequired[WorkAreaInsets]
    devicePixelRatio: NotRequired[float]
    rotation: NotRequired[int]
    colorDepth: NotRequired[int]
    label: NotRequired[str]
    isInternal: NotRequired[bool]


class AddScreenResult(TypedDict):
    screenInfo: ScreenInfo


class UpdateScreenParameters(TypedDict):
    screenId: ScreenId
    left: NotRequired[int]
    top: NotRequired[int]
    width: NotRequired[int]
    height: NotRequired[int]
    workAreaInsets: NotRequired[WorkAreaInsets]
    devicePixelRatio: NotRequired[float]
    rotation: NotRequired[int]
    colorDepth: NotRequired[int]
    label: NotRequired[str]
    isInternal: NotRequired[bool]


class UpdateScreenResult(TypedDict):
    screenInfo: ScreenInfo


class RemoveScreenParameters(TypedDict):
    screenId: ScreenId


class SetPrimaryScreenParameters(TypedDict):
    screenId: ScreenId


class ScreenOrientationLockChangedEvent(TypedDict):
    locked: bool
    orientation: NotRequired[ScreenOrientation]


class Emulation(BaseDomain):
    """This domain emulates different environments for the page."""

    domain_name = "Emulation"

    async def canEmulate(
        self,
        session_id: str | None = None,
    ) -> CanEmulateResult:
        """Tells whether emulation is supported."""

        return cast(
            CanEmulateResult, await self._command("canEmulate", None, session_id, {})
        )

    async def clearDeviceMetricsOverride(
        self,
        session_id: str | None = None,
    ) -> JsonObject:
        """Clears the overridden device metrics."""

        return await self._command("clearDeviceMetricsOverride", None, session_id, {})

    async def clearGeolocationOverride(
        self,
        session_id: str | None = None,
    ) -> JsonObject:
        """Clears the overridden Geolocation Position and Error."""

        return await self._command("clearGeolocationOverride", None, session_id, {})

    async def resetPageScaleFactor(
        self,
        session_id: str | None = None,
    ) -> JsonObject:
        """Requests that page scale factor is reset to initial values."""

        return await self._command("resetPageScaleFactor", None, session_id, {})

    @overload
    async def setFocusEmulationEnabled(
        self,
        params: SetFocusEmulationEnabledParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def setFocusEmulationEnabled(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetFocusEmulationEnabledParameters],
    ) -> JsonObject: ...

    async def setFocusEmulationEnabled(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Enables or disables simulating a focused and active page."""

        return await self._command(
            "setFocusEmulationEnabled", params, session_id, kwargs
        )

    @overload
    async def setAutoDarkModeOverride(
        self,
        params: SetAutoDarkModeOverrideParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def setAutoDarkModeOverride(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetAutoDarkModeOverrideParameters],
    ) -> JsonObject: ...

    async def setAutoDarkModeOverride(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Automatically render all web contents using a dark theme."""

        return await self._command(
            "setAutoDarkModeOverride", params, session_id, kwargs
        )

    @overload
    async def setCPUThrottlingRate(
        self,
        params: SetCPUThrottlingRateParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def setCPUThrottlingRate(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetCPUThrottlingRateParameters],
    ) -> JsonObject: ...

    async def setCPUThrottlingRate(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Enables CPU throttling to emulate slow CPUs."""

        return await self._command("setCPUThrottlingRate", params, session_id, kwargs)

    @overload
    async def setDefaultBackgroundColorOverride(
        self,
        params: SetDefaultBackgroundColorOverrideParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def setDefaultBackgroundColorOverride(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetDefaultBackgroundColorOverrideParameters],
    ) -> JsonObject: ...

    async def setDefaultBackgroundColorOverride(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Sets or clears an override of the default background color of the frame. This override is used if the content does not specify one."""

        return await self._command(
            "setDefaultBackgroundColorOverride", params, session_id, kwargs
        )

    @overload
    async def setSafeAreaInsetsOverride(
        self,
        params: SetSafeAreaInsetsOverrideParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def setSafeAreaInsetsOverride(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetSafeAreaInsetsOverrideParameters],
    ) -> JsonObject: ...

    async def setSafeAreaInsetsOverride(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Overrides the values for env(safe-area-inset-*) and env(safe-area-max-inset-*). Unset values will cause the respective variables to be undefined, even if previously overridden."""

        return await self._command(
            "setSafeAreaInsetsOverride", params, session_id, kwargs
        )

    @overload
    async def setDeviceMetricsOverride(
        self,
        params: SetDeviceMetricsOverrideParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def setDeviceMetricsOverride(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetDeviceMetricsOverrideParameters],
    ) -> JsonObject: ...

    async def setDeviceMetricsOverride(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Overrides the values of device screen dimensions (window.screen.width, window.screen.height, window.innerWidth, window.innerHeight, and "device-width"/"device-height"-related CSS media query results)."""

        return await self._command(
            "setDeviceMetricsOverride", params, session_id, kwargs
        )

    @overload
    async def setDevicePostureOverride(
        self,
        params: SetDevicePostureOverrideParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def setDevicePostureOverride(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetDevicePostureOverrideParameters],
    ) -> JsonObject: ...

    async def setDevicePostureOverride(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Start reporting the given posture value to the Device Posture API. This override can also be set in setDeviceMetricsOverride()."""

        return await self._command(
            "setDevicePostureOverride", params, session_id, kwargs
        )

    async def clearDevicePostureOverride(
        self,
        session_id: str | None = None,
    ) -> JsonObject:
        """Clears a device posture override set with either setDeviceMetricsOverride() or setDevicePostureOverride() and starts using posture information from the platform again. Does nothing if no override is set."""

        return await self._command("clearDevicePostureOverride", None, session_id, {})

    @overload
    async def setDisplayFeaturesOverride(
        self,
        params: SetDisplayFeaturesOverrideParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def setDisplayFeaturesOverride(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetDisplayFeaturesOverrideParameters],
    ) -> JsonObject: ...

    async def setDisplayFeaturesOverride(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Start using the given display features to pupulate the Viewport Segments API. This override can also be set in setDeviceMetricsOverride()."""

        return await self._command(
            "setDisplayFeaturesOverride", params, session_id, kwargs
        )

    async def clearDisplayFeaturesOverride(
        self,
        session_id: str | None = None,
    ) -> JsonObject:
        """Clears the display features override set with either setDeviceMetricsOverride() or setDisplayFeaturesOverride() and starts using display features from the platform again. Does nothing if no override is set."""

        return await self._command("clearDisplayFeaturesOverride", None, session_id, {})

    @overload
    async def setScrollbarsHidden(
        self,
        params: SetScrollbarsHiddenParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def setScrollbarsHidden(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetScrollbarsHiddenParameters],
    ) -> JsonObject: ...

    async def setScrollbarsHidden(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Send Emulation.setScrollbarsHidden."""

        return await self._command("setScrollbarsHidden", params, session_id, kwargs)

    @overload
    async def setDocumentCookieDisabled(
        self,
        params: SetDocumentCookieDisabledParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def setDocumentCookieDisabled(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetDocumentCookieDisabledParameters],
    ) -> JsonObject: ...

    async def setDocumentCookieDisabled(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Send Emulation.setDocumentCookieDisabled."""

        return await self._command(
            "setDocumentCookieDisabled", params, session_id, kwargs
        )

    @overload
    async def setEmitTouchEventsForMouse(
        self,
        params: SetEmitTouchEventsForMouseParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def setEmitTouchEventsForMouse(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetEmitTouchEventsForMouseParameters],
    ) -> JsonObject: ...

    async def setEmitTouchEventsForMouse(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Send Emulation.setEmitTouchEventsForMouse."""

        return await self._command(
            "setEmitTouchEventsForMouse", params, session_id, kwargs
        )

    @overload
    async def setEmulatedMedia(
        self,
        params: SetEmulatedMediaParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def setEmulatedMedia(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetEmulatedMediaParameters],
    ) -> JsonObject: ...

    async def setEmulatedMedia(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Emulates the given media type or media feature for CSS media queries."""

        return await self._command("setEmulatedMedia", params, session_id, kwargs)

    @overload
    async def setEmulatedVisionDeficiency(
        self,
        params: SetEmulatedVisionDeficiencyParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def setEmulatedVisionDeficiency(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetEmulatedVisionDeficiencyParameters],
    ) -> JsonObject: ...

    async def setEmulatedVisionDeficiency(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Emulates the given vision deficiency."""

        return await self._command(
            "setEmulatedVisionDeficiency", params, session_id, kwargs
        )

    @overload
    async def setEmulatedOSTextScale(
        self,
        params: SetEmulatedOSTextScaleParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def setEmulatedOSTextScale(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetEmulatedOSTextScaleParameters],
    ) -> JsonObject: ...

    async def setEmulatedOSTextScale(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Emulates the given OS text scale."""

        return await self._command("setEmulatedOSTextScale", params, session_id, kwargs)

    @overload
    async def setGeolocationOverride(
        self,
        params: SetGeolocationOverrideParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def setGeolocationOverride(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetGeolocationOverrideParameters],
    ) -> JsonObject: ...

    async def setGeolocationOverride(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Overrides the Geolocation Position or Error. Omitting latitude, longitude or accuracy emulates position unavailable."""

        return await self._command("setGeolocationOverride", params, session_id, kwargs)

    @overload
    async def getOverriddenSensorInformation(
        self,
        params: GetOverriddenSensorInformationParameters,
        session_id: str | None = None,
    ) -> GetOverriddenSensorInformationResult: ...

    @overload
    async def getOverriddenSensorInformation(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[GetOverriddenSensorInformationParameters],
    ) -> GetOverriddenSensorInformationResult: ...

    async def getOverriddenSensorInformation(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> GetOverriddenSensorInformationResult:
        """Send Emulation.getOverriddenSensorInformation."""

        return cast(
            GetOverriddenSensorInformationResult,
            await self._command(
                "getOverriddenSensorInformation", params, session_id, kwargs
            ),
        )

    @overload
    async def setSensorOverrideEnabled(
        self,
        params: SetSensorOverrideEnabledParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def setSensorOverrideEnabled(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetSensorOverrideEnabledParameters],
    ) -> JsonObject: ...

    async def setSensorOverrideEnabled(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Overrides a platform sensor of a given type. If |enabled| is true, calls to Sensor.start() will use a virtual sensor as backend rather than fetching data from a real hardware sensor. Otherwise, existing virtual sensor-backend Sensor objects will fire an error event and new calls to Sensor.start() will attempt to use a real sensor instead."""

        return await self._command(
            "setSensorOverrideEnabled", params, session_id, kwargs
        )

    @overload
    async def setSensorOverrideReadings(
        self,
        params: SetSensorOverrideReadingsParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def setSensorOverrideReadings(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetSensorOverrideReadingsParameters],
    ) -> JsonObject: ...

    async def setSensorOverrideReadings(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Updates the sensor readings reported by a sensor type previously overridden by setSensorOverrideEnabled."""

        return await self._command(
            "setSensorOverrideReadings", params, session_id, kwargs
        )

    @overload
    async def setPressureSourceOverrideEnabled(
        self,
        params: SetPressureSourceOverrideEnabledParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def setPressureSourceOverrideEnabled(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetPressureSourceOverrideEnabledParameters],
    ) -> JsonObject: ...

    async def setPressureSourceOverrideEnabled(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Overrides a pressure source of a given type, as used by the Compute Pressure API, so that updates to PressureObserver.observe() are provided via setPressureStateOverride instead of being retrieved from platform-provided telemetry data."""

        return await self._command(
            "setPressureSourceOverrideEnabled", params, session_id, kwargs
        )

    @overload
    async def setPressureStateOverride(
        self,
        params: SetPressureStateOverrideParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def setPressureStateOverride(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetPressureStateOverrideParameters],
    ) -> JsonObject: ...

    async def setPressureStateOverride(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Provides a given pressure state that will be processed and eventually be delivered to PressureObserver users. |source| must have been previously overridden by setPressureSourceOverrideEnabled."""

        return await self._command(
            "setPressureStateOverride", params, session_id, kwargs
        )

    @overload
    async def setIdleOverride(
        self,
        params: SetIdleOverrideParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def setIdleOverride(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetIdleOverrideParameters],
    ) -> JsonObject: ...

    async def setIdleOverride(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Overrides the Idle state."""

        return await self._command("setIdleOverride", params, session_id, kwargs)

    async def clearIdleOverride(
        self,
        session_id: str | None = None,
    ) -> JsonObject:
        """Clears Idle state overrides."""

        return await self._command("clearIdleOverride", None, session_id, {})

    @overload
    async def setNavigatorOverrides(
        self,
        params: SetNavigatorOverridesParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def setNavigatorOverrides(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetNavigatorOverridesParameters],
    ) -> JsonObject: ...

    async def setNavigatorOverrides(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Overrides value returned by the javascript navigator object."""

        return await self._command("setNavigatorOverrides", params, session_id, kwargs)

    @overload
    async def setPageScaleFactor(
        self,
        params: SetPageScaleFactorParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def setPageScaleFactor(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetPageScaleFactorParameters],
    ) -> JsonObject: ...

    async def setPageScaleFactor(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Sets a specified page scale factor."""

        return await self._command("setPageScaleFactor", params, session_id, kwargs)

    @overload
    async def setScriptExecutionDisabled(
        self,
        params: SetScriptExecutionDisabledParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def setScriptExecutionDisabled(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetScriptExecutionDisabledParameters],
    ) -> JsonObject: ...

    async def setScriptExecutionDisabled(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Switches script execution in the page."""

        return await self._command(
            "setScriptExecutionDisabled", params, session_id, kwargs
        )

    @overload
    async def setTouchEmulationEnabled(
        self,
        params: SetTouchEmulationEnabledParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def setTouchEmulationEnabled(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetTouchEmulationEnabledParameters],
    ) -> JsonObject: ...

    async def setTouchEmulationEnabled(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Enables touch on platforms which do not support them."""

        return await self._command(
            "setTouchEmulationEnabled", params, session_id, kwargs
        )

    @overload
    async def setVirtualTimePolicy(
        self,
        params: SetVirtualTimePolicyParameters,
        session_id: str | None = None,
    ) -> SetVirtualTimePolicyResult: ...

    @overload
    async def setVirtualTimePolicy(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetVirtualTimePolicyParameters],
    ) -> SetVirtualTimePolicyResult: ...

    async def setVirtualTimePolicy(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> SetVirtualTimePolicyResult:
        """Turns on virtual time for all frames (replacing real-time with a synthetic time source) and sets the current virtual time policy. Note this supersedes any previous time budget."""

        return cast(
            SetVirtualTimePolicyResult,
            await self._command("setVirtualTimePolicy", params, session_id, kwargs),
        )

    @overload
    async def setLocaleOverride(
        self,
        params: SetLocaleOverrideParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def setLocaleOverride(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetLocaleOverrideParameters],
    ) -> JsonObject: ...

    async def setLocaleOverride(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Overrides default host system locale with the specified one."""

        return await self._command("setLocaleOverride", params, session_id, kwargs)

    @overload
    async def setTimezoneOverride(
        self,
        params: SetTimezoneOverrideParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def setTimezoneOverride(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetTimezoneOverrideParameters],
    ) -> JsonObject: ...

    async def setTimezoneOverride(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Overrides default host system timezone with the specified one."""

        return await self._command("setTimezoneOverride", params, session_id, kwargs)

    @overload
    async def setVisibleSize(
        self,
        params: SetVisibleSizeParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def setVisibleSize(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetVisibleSizeParameters],
    ) -> JsonObject: ...

    async def setVisibleSize(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Resizes the frame/viewport of the page. Note that this does not affect the frame's container (e.g. browser window). Can be used to produce screenshots of the specified size. Not supported on Android."""

        return await self._command("setVisibleSize", params, session_id, kwargs)

    @overload
    async def setDisabledImageTypes(
        self,
        params: SetDisabledImageTypesParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def setDisabledImageTypes(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetDisabledImageTypesParameters],
    ) -> JsonObject: ...

    async def setDisabledImageTypes(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Send Emulation.setDisabledImageTypes."""

        return await self._command("setDisabledImageTypes", params, session_id, kwargs)

    @overload
    async def setDataSaverOverride(
        self,
        params: SetDataSaverOverrideParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def setDataSaverOverride(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetDataSaverOverrideParameters],
    ) -> JsonObject: ...

    async def setDataSaverOverride(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Override the value of navigator.connection.saveData"""

        return await self._command("setDataSaverOverride", params, session_id, kwargs)

    @overload
    async def setHardwareConcurrencyOverride(
        self,
        params: SetHardwareConcurrencyOverrideParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def setHardwareConcurrencyOverride(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetHardwareConcurrencyOverrideParameters],
    ) -> JsonObject: ...

    async def setHardwareConcurrencyOverride(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Send Emulation.setHardwareConcurrencyOverride."""

        return await self._command(
            "setHardwareConcurrencyOverride", params, session_id, kwargs
        )

    @overload
    async def setUserAgentOverride(
        self,
        params: SetUserAgentOverrideParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def setUserAgentOverride(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetUserAgentOverrideParameters],
    ) -> JsonObject: ...

    async def setUserAgentOverride(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Allows overriding user agent with the given string. `userAgentMetadata` must be set for Client Hint headers to be sent."""

        return await self._command("setUserAgentOverride", params, session_id, kwargs)

    @overload
    async def setAutomationOverride(
        self,
        params: SetAutomationOverrideParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def setAutomationOverride(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetAutomationOverrideParameters],
    ) -> JsonObject: ...

    async def setAutomationOverride(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Allows overriding the automation flag."""

        return await self._command("setAutomationOverride", params, session_id, kwargs)

    @overload
    async def setSmallViewportHeightDifferenceOverride(
        self,
        params: SetSmallViewportHeightDifferenceOverrideParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def setSmallViewportHeightDifferenceOverride(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetSmallViewportHeightDifferenceOverrideParameters],
    ) -> JsonObject: ...

    async def setSmallViewportHeightDifferenceOverride(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Allows overriding the difference between the small and large viewport sizes, which determine the value of the `svh` and `lvh` unit, respectively. Only supported for top-level frames."""

        return await self._command(
            "setSmallViewportHeightDifferenceOverride", params, session_id, kwargs
        )

    async def getScreenInfos(
        self,
        session_id: str | None = None,
    ) -> GetScreenInfosResult:
        """Returns device's screen configuration. In headful mode, the physical screens configuration is returned, whereas in headless mode, a virtual headless screen configuration is provided instead."""

        return cast(
            GetScreenInfosResult,
            await self._command("getScreenInfos", None, session_id, {}),
        )

    @overload
    async def addScreen(
        self,
        params: AddScreenParameters,
        session_id: str | None = None,
    ) -> AddScreenResult: ...

    @overload
    async def addScreen(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[AddScreenParameters],
    ) -> AddScreenResult: ...

    async def addScreen(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> AddScreenResult:
        """Add a new screen to the device. Only supported in headless mode."""

        return cast(
            AddScreenResult,
            await self._command("addScreen", params, session_id, kwargs),
        )

    @overload
    async def updateScreen(
        self,
        params: UpdateScreenParameters,
        session_id: str | None = None,
    ) -> UpdateScreenResult: ...

    @overload
    async def updateScreen(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[UpdateScreenParameters],
    ) -> UpdateScreenResult: ...

    async def updateScreen(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> UpdateScreenResult:
        """Updates specified screen parameters. Only supported in headless mode."""

        return cast(
            UpdateScreenResult,
            await self._command("updateScreen", params, session_id, kwargs),
        )

    @overload
    async def removeScreen(
        self,
        params: RemoveScreenParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def removeScreen(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[RemoveScreenParameters],
    ) -> JsonObject: ...

    async def removeScreen(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Remove screen from the device. Only supported in headless mode."""

        return await self._command("removeScreen", params, session_id, kwargs)

    @overload
    async def setPrimaryScreen(
        self,
        params: SetPrimaryScreenParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def setPrimaryScreen(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetPrimaryScreenParameters],
    ) -> JsonObject: ...

    async def setPrimaryScreen(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Set primary screen. Only supported in headless mode. Note that this changes the coordinate system origin to the top-left of the new primary screen, updating the bounds and work areas of all existing screens accordingly."""

        return await self._command("setPrimaryScreen", params, session_id, kwargs)

    @overload
    def virtualTimeBudgetExpired(
        self,
        callback_or_session: EventCallback[JsonObject],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def virtualTimeBudgetExpired(
        self,
        callback_or_session: str,
        handler: EventCallback[JsonObject],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def virtualTimeBudgetExpired(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[JsonObject]: ...

    def virtualTimeBudgetExpired(
        self,
        callback_or_session: EventCallback[JsonObject] | str | None = None,
        handler: EventCallback[JsonObject] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[JsonObject] | Unsubscribe:
        """Notification sent after the virtual time budget for the current VirtualTimePolicy has run out."""

        return self._event(
            "virtualTimeBudgetExpired",
            cast(EventCallback[Mapping[str, object]] | str | None, callback_or_session),
            cast(EventCallback[Mapping[str, object]] | None, handler),
            session_id,
        )

    @overload
    def screenOrientationLockChanged(
        self,
        callback_or_session: EventCallback[ScreenOrientationLockChangedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def screenOrientationLockChanged(
        self,
        callback_or_session: str,
        handler: EventCallback[ScreenOrientationLockChangedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def screenOrientationLockChanged(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[ScreenOrientationLockChangedEvent]: ...

    def screenOrientationLockChanged(
        self,
        callback_or_session: EventCallback[ScreenOrientationLockChangedEvent]
        | str
        | None = None,
        handler: EventCallback[ScreenOrientationLockChangedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[ScreenOrientationLockChangedEvent] | Unsubscribe:
        """Fired when a page calls screen.orientation.lock() or screen.orientation.unlock() while device emulation is enabled. This allows the DevTools frontend to update the emulated device orientation accordingly."""

        return cast(
            Awaitable[ScreenOrientationLockChangedEvent] | Unsubscribe,
            self._event(
                "screenOrientationLockChanged",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )


__all__ = [
    "AddScreenParameters",
    "AddScreenResult",
    "CanEmulateResult",
    "DevicePosture",
    "DisabledImageType",
    "DisplayFeature",
    "Emulation",
    "GetOverriddenSensorInformationParameters",
    "GetOverriddenSensorInformationResult",
    "GetScreenInfosResult",
    "MediaFeature",
    "PressureMetadata",
    "PressureSource",
    "PressureState",
    "RemoveScreenParameters",
    "SafeAreaInsets",
    "ScreenId",
    "ScreenInfo",
    "ScreenOrientation",
    "ScreenOrientationLockChangedEvent",
    "SensorMetadata",
    "SensorReading",
    "SensorReadingQuaternion",
    "SensorReadingSingle",
    "SensorReadingXYZ",
    "SensorType",
    "SetAutoDarkModeOverrideParameters",
    "SetAutomationOverrideParameters",
    "SetCPUThrottlingRateParameters",
    "SetDataSaverOverrideParameters",
    "SetDefaultBackgroundColorOverrideParameters",
    "SetDeviceMetricsOverrideParameters",
    "SetDevicePostureOverrideParameters",
    "SetDisabledImageTypesParameters",
    "SetDisplayFeaturesOverrideParameters",
    "SetDocumentCookieDisabledParameters",
    "SetEmitTouchEventsForMouseParameters",
    "SetEmulatedMediaParameters",
    "SetEmulatedOSTextScaleParameters",
    "SetEmulatedVisionDeficiencyParameters",
    "SetFocusEmulationEnabledParameters",
    "SetGeolocationOverrideParameters",
    "SetHardwareConcurrencyOverrideParameters",
    "SetIdleOverrideParameters",
    "SetLocaleOverrideParameters",
    "SetNavigatorOverridesParameters",
    "SetPageScaleFactorParameters",
    "SetPressureSourceOverrideEnabledParameters",
    "SetPressureStateOverrideParameters",
    "SetPrimaryScreenParameters",
    "SetSafeAreaInsetsOverrideParameters",
    "SetScriptExecutionDisabledParameters",
    "SetScrollbarsHiddenParameters",
    "SetSensorOverrideEnabledParameters",
    "SetSensorOverrideReadingsParameters",
    "SetSmallViewportHeightDifferenceOverrideParameters",
    "SetTimezoneOverrideParameters",
    "SetTouchEmulationEnabledParameters",
    "SetUserAgentOverrideParameters",
    "SetVirtualTimePolicyParameters",
    "SetVirtualTimePolicyResult",
    "SetVisibleSizeParameters",
    "UpdateScreenParameters",
    "UpdateScreenResult",
    "UserAgentBrandVersion",
    "UserAgentMetadata",
    "VirtualTimePolicy",
    "WorkAreaInsets",
]
