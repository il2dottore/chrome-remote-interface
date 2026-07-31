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


class ScreenOrientation(TypedDict):
    type: Literal[
        "portraitPrimary", "portraitSecondary", "landscapePrimary", "landscapeSecondary"
    ]
    angle: int


class DisplayFeature(TypedDict):
    orientation: Literal["vertical", "horizontal"]
    offset: int
    maskLength: int


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


DisabledImageType: TypeAlias = Literal["avif", "webp"]


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


class SetGeolocationOverrideParameters(TypedDict):
    latitude: NotRequired[float]
    longitude: NotRequired[float]
    accuracy: NotRequired[float]


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


class SetHardwareConcurrencyOverrideParameters(TypedDict):
    hardwareConcurrency: int


class SetUserAgentOverrideParameters(TypedDict):
    userAgent: str
    acceptLanguage: NotRequired[str]
    platform: NotRequired[str]
    userAgentMetadata: NotRequired[UserAgentMetadata]


class SetAutomationOverrideParameters(TypedDict):
    enabled: bool


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
        """Overrides the Geolocation Position or Error. Omitting any of the parameters emulates position unavailable."""

        return await self._command("setGeolocationOverride", params, session_id, kwargs)

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
        """Allows overriding user agent with the given string."""

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


__all__ = [
    "CanEmulateResult",
    "DisabledImageType",
    "DisplayFeature",
    "Emulation",
    "MediaFeature",
    "ScreenOrientation",
    "SetAutoDarkModeOverrideParameters",
    "SetAutomationOverrideParameters",
    "SetCPUThrottlingRateParameters",
    "SetDefaultBackgroundColorOverrideParameters",
    "SetDeviceMetricsOverrideParameters",
    "SetDisabledImageTypesParameters",
    "SetDocumentCookieDisabledParameters",
    "SetEmitTouchEventsForMouseParameters",
    "SetEmulatedMediaParameters",
    "SetEmulatedVisionDeficiencyParameters",
    "SetFocusEmulationEnabledParameters",
    "SetGeolocationOverrideParameters",
    "SetHardwareConcurrencyOverrideParameters",
    "SetIdleOverrideParameters",
    "SetLocaleOverrideParameters",
    "SetNavigatorOverridesParameters",
    "SetPageScaleFactorParameters",
    "SetScriptExecutionDisabledParameters",
    "SetScrollbarsHiddenParameters",
    "SetTimezoneOverrideParameters",
    "SetTouchEmulationEnabledParameters",
    "SetUserAgentOverrideParameters",
    "SetVirtualTimePolicyParameters",
    "SetVirtualTimePolicyResult",
    "SetVisibleSizeParameters",
    "UserAgentBrandVersion",
    "UserAgentMetadata",
    "VirtualTimePolicy",
]
