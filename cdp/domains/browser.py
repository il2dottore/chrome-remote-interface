"""Generated bindings for the CDP Browser domain. Do not edit manually."""

from __future__ import annotations

from collections.abc import Awaitable, Mapping
from typing import TYPE_CHECKING, Literal, TypeAlias, cast, overload

from typing_extensions import NotRequired, TypedDict, Unpack

from cdp.domain import Domain as BaseDomain, EventCallback, Unsubscribe
from cdp.types import JsonObject

if TYPE_CHECKING:
    from . import page as Page
    from . import target as Target


BrowserContextID: TypeAlias = str

WindowID: TypeAlias = int

WindowState: TypeAlias = Literal["normal", "minimized", "maximized", "fullscreen"]


class Bounds(TypedDict):
    left: NotRequired[int]
    top: NotRequired[int]
    width: NotRequired[int]
    height: NotRequired[int]
    windowState: NotRequired[WindowState]


PermissionType: TypeAlias = Literal[
    "accessibilityEvents",
    "audioCapture",
    "backgroundSync",
    "backgroundFetch",
    "clipboardReadWrite",
    "clipboardSanitizedWrite",
    "displayCapture",
    "durableStorage",
    "flash",
    "geolocation",
    "idleDetection",
    "localFonts",
    "midi",
    "midiSysex",
    "nfc",
    "notifications",
    "paymentHandler",
    "periodicBackgroundSync",
    "protectedMediaIdentifier",
    "sensors",
    "storageAccess",
    "topLevelStorageAccess",
    "videoCapture",
    "videoCapturePanTiltZoom",
    "wakeLockScreen",
    "wakeLockSystem",
    "windowManagement",
]

PermissionSetting: TypeAlias = Literal["granted", "denied", "prompt"]


class PermissionDescriptor(TypedDict):
    name: str
    sysex: NotRequired[bool]
    userVisibleOnly: NotRequired[bool]
    allowWithoutSanitization: NotRequired[bool]
    panTiltZoom: NotRequired[bool]


BrowserCommandId: TypeAlias = Literal["openTabSearch", "closeTabSearch"]


class Bucket(TypedDict):
    low: int
    high: int
    count: int


class Histogram(TypedDict):
    name: str
    sum: int
    count: int
    buckets: list[Bucket]


class SetPermissionParameters(TypedDict):
    permission: PermissionDescriptor
    setting: PermissionSetting
    origin: NotRequired[str]
    browserContextId: NotRequired[BrowserContextID]


class GrantPermissionsParameters(TypedDict):
    permissions: list[PermissionType]
    origin: NotRequired[str]
    browserContextId: NotRequired[BrowserContextID]


class ResetPermissionsParameters(TypedDict):
    browserContextId: NotRequired[BrowserContextID]


class SetDownloadBehaviorParameters(TypedDict):
    behavior: Literal["deny", "allow", "allowAndName", "default"]
    browserContextId: NotRequired[BrowserContextID]
    downloadPath: NotRequired[str]
    eventsEnabled: NotRequired[bool]


class CancelDownloadParameters(TypedDict):
    guid: str
    browserContextId: NotRequired[BrowserContextID]


class GetVersionResult(TypedDict):
    protocolVersion: str
    product: str
    revision: str
    userAgent: str
    jsVersion: str


class GetBrowserCommandLineResult(TypedDict):
    arguments: list[str]


class GetHistogramsParameters(TypedDict):
    query: NotRequired[str]
    delta: NotRequired[bool]


class GetHistogramsResult(TypedDict):
    histograms: list[Histogram]


class GetHistogramParameters(TypedDict):
    name: str
    delta: NotRequired[bool]


class GetHistogramResult(TypedDict):
    histogram: Histogram


class GetWindowBoundsParameters(TypedDict):
    windowId: WindowID


class GetWindowBoundsResult(TypedDict):
    bounds: Bounds


class GetWindowForTargetParameters(TypedDict):
    targetId: NotRequired[Target.TargetID]


class GetWindowForTargetResult(TypedDict):
    windowId: WindowID
    bounds: Bounds


class SetWindowBoundsParameters(TypedDict):
    windowId: WindowID
    bounds: Bounds


class SetDockTileParameters(TypedDict):
    badgeLabel: NotRequired[str]
    image: NotRequired[str]


class ExecuteBrowserCommandParameters(TypedDict):
    commandId: BrowserCommandId


class AddPrivacySandboxEnrollmentOverrideParameters(TypedDict):
    url: str


class DownloadWillBeginEvent(TypedDict):
    frameId: Page.FrameId
    guid: str
    url: str
    suggestedFilename: str


class DownloadProgressEvent(TypedDict):
    guid: str
    totalBytes: float
    receivedBytes: float
    state: Literal["inProgress", "completed", "canceled"]


class Browser(BaseDomain):
    """The Browser domain defines methods and events for browser managing."""

    domain_name = "Browser"

    @overload
    async def setPermission(
        self,
        params: SetPermissionParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def setPermission(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetPermissionParameters],
    ) -> JsonObject: ...

    async def setPermission(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Set permission settings for given origin."""

        return await self._command("setPermission", params, session_id, kwargs)

    @overload
    async def grantPermissions(
        self,
        params: GrantPermissionsParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def grantPermissions(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[GrantPermissionsParameters],
    ) -> JsonObject: ...

    async def grantPermissions(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Grant specific permissions to the given origin and reject all others."""

        return await self._command("grantPermissions", params, session_id, kwargs)

    @overload
    async def resetPermissions(
        self,
        params: ResetPermissionsParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def resetPermissions(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[ResetPermissionsParameters],
    ) -> JsonObject: ...

    async def resetPermissions(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Reset all permission management for all origins."""

        return await self._command("resetPermissions", params, session_id, kwargs)

    @overload
    async def setDownloadBehavior(
        self,
        params: SetDownloadBehaviorParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def setDownloadBehavior(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetDownloadBehaviorParameters],
    ) -> JsonObject: ...

    async def setDownloadBehavior(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Set the behavior when downloading a file."""

        return await self._command("setDownloadBehavior", params, session_id, kwargs)

    @overload
    async def cancelDownload(
        self,
        params: CancelDownloadParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def cancelDownload(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[CancelDownloadParameters],
    ) -> JsonObject: ...

    async def cancelDownload(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Cancel a download if in progress"""

        return await self._command("cancelDownload", params, session_id, kwargs)

    async def close(
        self,
        session_id: str | None = None,
    ) -> JsonObject:
        """Close browser gracefully."""

        return await self._command("close", None, session_id, {})

    async def crash(
        self,
        session_id: str | None = None,
    ) -> JsonObject:
        """Crashes browser on the main thread."""

        return await self._command("crash", None, session_id, {})

    async def crashGpuProcess(
        self,
        session_id: str | None = None,
    ) -> JsonObject:
        """Crashes GPU process."""

        return await self._command("crashGpuProcess", None, session_id, {})

    async def getVersion(
        self,
        session_id: str | None = None,
    ) -> GetVersionResult:
        """Returns version information."""

        return cast(
            GetVersionResult, await self._command("getVersion", None, session_id, {})
        )

    async def getBrowserCommandLine(
        self,
        session_id: str | None = None,
    ) -> GetBrowserCommandLineResult:
        """Returns the command line switches for the browser process if, and only if --enable-automation is on the commandline."""

        return cast(
            GetBrowserCommandLineResult,
            await self._command("getBrowserCommandLine", None, session_id, {}),
        )

    @overload
    async def getHistograms(
        self,
        params: GetHistogramsParameters,
        session_id: str | None = None,
    ) -> GetHistogramsResult: ...

    @overload
    async def getHistograms(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[GetHistogramsParameters],
    ) -> GetHistogramsResult: ...

    async def getHistograms(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> GetHistogramsResult:
        """Get Chrome histograms."""

        return cast(
            GetHistogramsResult,
            await self._command("getHistograms", params, session_id, kwargs),
        )

    @overload
    async def getHistogram(
        self,
        params: GetHistogramParameters,
        session_id: str | None = None,
    ) -> GetHistogramResult: ...

    @overload
    async def getHistogram(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[GetHistogramParameters],
    ) -> GetHistogramResult: ...

    async def getHistogram(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> GetHistogramResult:
        """Get a Chrome histogram by name."""

        return cast(
            GetHistogramResult,
            await self._command("getHistogram", params, session_id, kwargs),
        )

    @overload
    async def getWindowBounds(
        self,
        params: GetWindowBoundsParameters,
        session_id: str | None = None,
    ) -> GetWindowBoundsResult: ...

    @overload
    async def getWindowBounds(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[GetWindowBoundsParameters],
    ) -> GetWindowBoundsResult: ...

    async def getWindowBounds(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> GetWindowBoundsResult:
        """Get position and size of the browser window."""

        return cast(
            GetWindowBoundsResult,
            await self._command("getWindowBounds", params, session_id, kwargs),
        )

    @overload
    async def getWindowForTarget(
        self,
        params: GetWindowForTargetParameters,
        session_id: str | None = None,
    ) -> GetWindowForTargetResult: ...

    @overload
    async def getWindowForTarget(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[GetWindowForTargetParameters],
    ) -> GetWindowForTargetResult: ...

    async def getWindowForTarget(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> GetWindowForTargetResult:
        """Get the browser window that contains the devtools target."""

        return cast(
            GetWindowForTargetResult,
            await self._command("getWindowForTarget", params, session_id, kwargs),
        )

    @overload
    async def setWindowBounds(
        self,
        params: SetWindowBoundsParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def setWindowBounds(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetWindowBoundsParameters],
    ) -> JsonObject: ...

    async def setWindowBounds(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Set position and/or size of the browser window."""

        return await self._command("setWindowBounds", params, session_id, kwargs)

    @overload
    async def setDockTile(
        self,
        params: SetDockTileParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def setDockTile(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetDockTileParameters],
    ) -> JsonObject: ...

    async def setDockTile(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Set dock tile details, platform-specific."""

        return await self._command("setDockTile", params, session_id, kwargs)

    @overload
    async def executeBrowserCommand(
        self,
        params: ExecuteBrowserCommandParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def executeBrowserCommand(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[ExecuteBrowserCommandParameters],
    ) -> JsonObject: ...

    async def executeBrowserCommand(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Invoke custom browser commands used by telemetry."""

        return await self._command("executeBrowserCommand", params, session_id, kwargs)

    @overload
    async def addPrivacySandboxEnrollmentOverride(
        self,
        params: AddPrivacySandboxEnrollmentOverrideParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def addPrivacySandboxEnrollmentOverride(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[AddPrivacySandboxEnrollmentOverrideParameters],
    ) -> JsonObject: ...

    async def addPrivacySandboxEnrollmentOverride(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Allows a site to use privacy sandbox features that require enrollment without the site actually being enrolled. Only supported on page targets."""

        return await self._command(
            "addPrivacySandboxEnrollmentOverride", params, session_id, kwargs
        )

    @overload
    def downloadWillBegin(
        self,
        callback_or_session: EventCallback[DownloadWillBeginEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def downloadWillBegin(
        self,
        callback_or_session: str,
        handler: EventCallback[DownloadWillBeginEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def downloadWillBegin(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[DownloadWillBeginEvent]: ...

    def downloadWillBegin(
        self,
        callback_or_session: EventCallback[DownloadWillBeginEvent] | str | None = None,
        handler: EventCallback[DownloadWillBeginEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[DownloadWillBeginEvent] | Unsubscribe:
        """Fired when page is about to start a download."""

        return cast(
            Awaitable[DownloadWillBeginEvent] | Unsubscribe,
            self._event(
                "downloadWillBegin",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def downloadProgress(
        self,
        callback_or_session: EventCallback[DownloadProgressEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def downloadProgress(
        self,
        callback_or_session: str,
        handler: EventCallback[DownloadProgressEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def downloadProgress(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[DownloadProgressEvent]: ...

    def downloadProgress(
        self,
        callback_or_session: EventCallback[DownloadProgressEvent] | str | None = None,
        handler: EventCallback[DownloadProgressEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[DownloadProgressEvent] | Unsubscribe:
        """Fired when download makes progress. Last call has |done| == true."""

        return cast(
            Awaitable[DownloadProgressEvent] | Unsubscribe,
            self._event(
                "downloadProgress",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )


__all__ = [
    "AddPrivacySandboxEnrollmentOverrideParameters",
    "Bounds",
    "Browser",
    "BrowserCommandId",
    "BrowserContextID",
    "Bucket",
    "CancelDownloadParameters",
    "DownloadProgressEvent",
    "DownloadWillBeginEvent",
    "ExecuteBrowserCommandParameters",
    "GetBrowserCommandLineResult",
    "GetHistogramParameters",
    "GetHistogramResult",
    "GetHistogramsParameters",
    "GetHistogramsResult",
    "GetVersionResult",
    "GetWindowBoundsParameters",
    "GetWindowBoundsResult",
    "GetWindowForTargetParameters",
    "GetWindowForTargetResult",
    "GrantPermissionsParameters",
    "Histogram",
    "PermissionDescriptor",
    "PermissionSetting",
    "PermissionType",
    "ResetPermissionsParameters",
    "SetDockTileParameters",
    "SetDownloadBehaviorParameters",
    "SetPermissionParameters",
    "SetWindowBoundsParameters",
    "WindowID",
    "WindowState",
]
