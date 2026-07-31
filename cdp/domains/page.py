"""Generated bindings for the CDP Page domain. Do not edit manually."""

from __future__ import annotations

from collections.abc import Awaitable, Mapping
from typing import TYPE_CHECKING, Literal, TypeAlias, cast, overload

from typing_extensions import NotRequired, TypedDict, Unpack

from cdp.domain import Domain as BaseDomain, EventCallback, Unsubscribe
from cdp.types import JsonObject

if TYPE_CHECKING:
    from . import dom as DOM
    from . import debugger as Debugger
    from . import emulation as Emulation
    from . import io as IO
    from . import network as Network
    from . import runtime as Runtime


FrameId: TypeAlias = str

AdFrameType: TypeAlias = Literal["none", "child", "root"]

AdFrameExplanation: TypeAlias = Literal[
    "ParentIsAd", "CreatedByAdScript", "MatchedBlockingRule"
]


class AdFrameStatus(TypedDict):
    adFrameType: AdFrameType
    explanations: NotRequired[list[AdFrameExplanation]]


class AdScriptId(TypedDict):
    scriptId: Runtime.ScriptId
    debuggerId: Runtime.UniqueDebuggerId


SecureContextType: TypeAlias = Literal[
    "Secure", "SecureLocalhost", "InsecureScheme", "InsecureAncestor"
]

CrossOriginIsolatedContextType: TypeAlias = Literal[
    "Isolated", "NotIsolated", "NotIsolatedFeatureDisabled"
]

GatedAPIFeatures: TypeAlias = Literal[
    "SharedArrayBuffers",
    "SharedArrayBuffersTransferAllowed",
    "PerformanceMeasureMemory",
    "PerformanceProfile",
]

PermissionsPolicyFeature: TypeAlias = Literal[
    "accelerometer",
    "ambient-light-sensor",
    "attribution-reporting",
    "autoplay",
    "bluetooth",
    "browsing-topics",
    "camera",
    "ch-dpr",
    "ch-device-memory",
    "ch-downlink",
    "ch-ect",
    "ch-prefers-color-scheme",
    "ch-prefers-reduced-motion",
    "ch-rtt",
    "ch-save-data",
    "ch-ua",
    "ch-ua-arch",
    "ch-ua-bitness",
    "ch-ua-platform",
    "ch-ua-model",
    "ch-ua-mobile",
    "ch-ua-form-factor",
    "ch-ua-full-version",
    "ch-ua-full-version-list",
    "ch-ua-platform-version",
    "ch-ua-wow64",
    "ch-viewport-height",
    "ch-viewport-width",
    "ch-width",
    "clipboard-read",
    "clipboard-write",
    "compute-pressure",
    "cross-origin-isolated",
    "direct-sockets",
    "display-capture",
    "document-domain",
    "encrypted-media",
    "execution-while-out-of-viewport",
    "execution-while-not-rendered",
    "focus-without-user-activation",
    "fullscreen",
    "frobulate",
    "gamepad",
    "geolocation",
    "gyroscope",
    "hid",
    "identity-credentials-get",
    "idle-detection",
    "interest-cohort",
    "join-ad-interest-group",
    "keyboard-map",
    "local-fonts",
    "magnetometer",
    "microphone",
    "midi",
    "otp-credentials",
    "payment",
    "picture-in-picture",
    "private-aggregation",
    "private-state-token-issuance",
    "private-state-token-redemption",
    "publickey-credentials-get",
    "run-ad-auction",
    "screen-wake-lock",
    "serial",
    "shared-autofill",
    "shared-storage",
    "shared-storage-select-url",
    "smart-card",
    "storage-access",
    "sync-xhr",
    "unload",
    "usb",
    "vertical-scroll",
    "web-share",
    "window-management",
    "window-placement",
    "xr-spatial-tracking",
]

PermissionsPolicyBlockReason: TypeAlias = Literal[
    "Header", "IframeAttribute", "InFencedFrameTree", "InIsolatedApp"
]


class PermissionsPolicyBlockLocator(TypedDict):
    frameId: FrameId
    blockReason: PermissionsPolicyBlockReason


class PermissionsPolicyFeatureState(TypedDict):
    feature: PermissionsPolicyFeature
    allowed: bool
    locator: NotRequired[PermissionsPolicyBlockLocator]


OriginTrialTokenStatus: TypeAlias = Literal[
    "Success",
    "NotSupported",
    "Insecure",
    "Expired",
    "WrongOrigin",
    "InvalidSignature",
    "Malformed",
    "WrongVersion",
    "FeatureDisabled",
    "TokenDisabled",
    "FeatureDisabledForUser",
    "UnknownTrial",
]

OriginTrialStatus: TypeAlias = Literal[
    "Enabled", "ValidTokenNotProvided", "OSNotSupported", "TrialNotAllowed"
]

OriginTrialUsageRestriction: TypeAlias = Literal["None", "Subset"]


class OriginTrialToken(TypedDict):
    origin: str
    matchSubDomains: bool
    trialName: str
    expiryTime: Network.TimeSinceEpoch
    isThirdParty: bool
    usageRestriction: OriginTrialUsageRestriction


class OriginTrialTokenWithStatus(TypedDict):
    rawTokenText: str
    parsedToken: NotRequired[OriginTrialToken]
    status: OriginTrialTokenStatus


class OriginTrial(TypedDict):
    trialName: str
    status: OriginTrialStatus
    tokensWithStatus: list[OriginTrialTokenWithStatus]


class Frame(TypedDict):
    id: FrameId
    parentId: NotRequired[FrameId]
    loaderId: Network.LoaderId
    name: NotRequired[str]
    url: str
    urlFragment: NotRequired[str]
    domainAndRegistry: str
    securityOrigin: str
    mimeType: str
    unreachableUrl: NotRequired[str]
    adFrameStatus: NotRequired[AdFrameStatus]
    secureContextType: SecureContextType
    crossOriginIsolatedContextType: CrossOriginIsolatedContextType
    gatedAPIFeatures: list[GatedAPIFeatures]


class FrameResource(TypedDict):
    url: str
    type: Network.ResourceType
    mimeType: str
    lastModified: NotRequired[Network.TimeSinceEpoch]
    contentSize: NotRequired[float]
    failed: NotRequired[bool]
    canceled: NotRequired[bool]


class FrameResourceTree(TypedDict):
    frame: Frame
    childFrames: NotRequired[list[FrameResourceTree]]
    resources: list[FrameResource]


class FrameTree(TypedDict):
    frame: Frame
    childFrames: NotRequired[list[FrameTree]]


ScriptIdentifier: TypeAlias = str

TransitionType: TypeAlias = Literal[
    "link",
    "typed",
    "address_bar",
    "auto_bookmark",
    "auto_subframe",
    "manual_subframe",
    "generated",
    "auto_toplevel",
    "form_submit",
    "reload",
    "keyword",
    "keyword_generated",
    "other",
]


class NavigationEntry(TypedDict):
    id: int
    url: str
    userTypedURL: str
    title: str
    transitionType: TransitionType


class ScreencastFrameMetadata(TypedDict):
    offsetTop: float
    pageScaleFactor: float
    deviceWidth: float
    deviceHeight: float
    scrollOffsetX: float
    scrollOffsetY: float
    timestamp: NotRequired[Network.TimeSinceEpoch]


DialogType: TypeAlias = Literal["alert", "confirm", "prompt", "beforeunload"]


class AppManifestError(TypedDict):
    message: str
    critical: int
    line: int
    column: int


class AppManifestParsedProperties(TypedDict):
    scope: str


class LayoutViewport(TypedDict):
    pageX: int
    pageY: int
    clientWidth: int
    clientHeight: int


class VisualViewport(TypedDict):
    offsetX: float
    offsetY: float
    pageX: float
    pageY: float
    clientWidth: float
    clientHeight: float
    scale: float
    zoom: NotRequired[float]


class Viewport(TypedDict):
    x: float
    y: float
    width: float
    height: float
    scale: float


class FontFamilies(TypedDict):
    standard: NotRequired[str]
    fixed: NotRequired[str]
    serif: NotRequired[str]
    sansSerif: NotRequired[str]
    cursive: NotRequired[str]
    fantasy: NotRequired[str]
    math: NotRequired[str]


class ScriptFontFamilies(TypedDict):
    script: str
    fontFamilies: FontFamilies


class FontSizes(TypedDict):
    standard: NotRequired[int]
    fixed: NotRequired[int]


ClientNavigationReason: TypeAlias = Literal[
    "formSubmissionGet",
    "formSubmissionPost",
    "httpHeaderRefresh",
    "scriptInitiated",
    "metaTagRefresh",
    "pageBlockInterstitial",
    "reload",
    "anchorClick",
]

ClientNavigationDisposition: TypeAlias = Literal[
    "currentTab", "newTab", "newWindow", "download"
]


class InstallabilityErrorArgument(TypedDict):
    name: str
    value: str


class InstallabilityError(TypedDict):
    errorId: str
    errorArguments: list[InstallabilityErrorArgument]


ReferrerPolicy: TypeAlias = Literal[
    "noReferrer",
    "noReferrerWhenDowngrade",
    "origin",
    "originWhenCrossOrigin",
    "sameOrigin",
    "strictOrigin",
    "strictOriginWhenCrossOrigin",
    "unsafeUrl",
]


class CompilationCacheParams(TypedDict):
    url: str
    eager: NotRequired[bool]


AutoResponseMode: TypeAlias = Literal["none", "autoAccept", "autoReject", "autoOptOut"]

NavigationType: TypeAlias = Literal["Navigation", "BackForwardCacheRestore"]

BackForwardCacheNotRestoredReason: TypeAlias = Literal[
    "NotPrimaryMainFrame",
    "BackForwardCacheDisabled",
    "RelatedActiveContentsExist",
    "HTTPStatusNotOK",
    "SchemeNotHTTPOrHTTPS",
    "Loading",
    "WasGrantedMediaAccess",
    "DisableForRenderFrameHostCalled",
    "DomainNotAllowed",
    "HTTPMethodNotGET",
    "SubframeIsNavigating",
    "Timeout",
    "CacheLimit",
    "JavaScriptExecution",
    "RendererProcessKilled",
    "RendererProcessCrashed",
    "SchedulerTrackedFeatureUsed",
    "ConflictingBrowsingInstance",
    "CacheFlushed",
    "ServiceWorkerVersionActivation",
    "SessionRestored",
    "ServiceWorkerPostMessage",
    "EnteredBackForwardCacheBeforeServiceWorkerHostAdded",
    "RenderFrameHostReused_SameSite",
    "RenderFrameHostReused_CrossSite",
    "ServiceWorkerClaim",
    "IgnoreEventAndEvict",
    "HaveInnerContents",
    "TimeoutPuttingInCache",
    "BackForwardCacheDisabledByLowMemory",
    "BackForwardCacheDisabledByCommandLine",
    "NetworkRequestDatapipeDrainedAsBytesConsumer",
    "NetworkRequestRedirected",
    "NetworkRequestTimeout",
    "NetworkExceedsBufferLimit",
    "NavigationCancelledWhileRestoring",
    "NotMostRecentNavigationEntry",
    "BackForwardCacheDisabledForPrerender",
    "UserAgentOverrideDiffers",
    "ForegroundCacheLimit",
    "BrowsingInstanceNotSwapped",
    "BackForwardCacheDisabledForDelegate",
    "UnloadHandlerExistsInMainFrame",
    "UnloadHandlerExistsInSubFrame",
    "ServiceWorkerUnregistration",
    "CacheControlNoStore",
    "CacheControlNoStoreCookieModified",
    "CacheControlNoStoreHTTPOnlyCookieModified",
    "NoResponseHead",
    "Unknown",
    "ActivationNavigationsDisallowedForBug1234857",
    "ErrorDocument",
    "FencedFramesEmbedder",
    "CookieDisabled",
    "HTTPAuthRequired",
    "CookieFlushed",
    "WebSocket",
    "WebTransport",
    "WebRTC",
    "MainResourceHasCacheControlNoStore",
    "MainResourceHasCacheControlNoCache",
    "SubresourceHasCacheControlNoStore",
    "SubresourceHasCacheControlNoCache",
    "ContainsPlugins",
    "DocumentLoaded",
    "DedicatedWorkerOrWorklet",
    "OutstandingNetworkRequestOthers",
    "RequestedMIDIPermission",
    "RequestedAudioCapturePermission",
    "RequestedVideoCapturePermission",
    "RequestedBackForwardCacheBlockedSensors",
    "RequestedBackgroundWorkPermission",
    "BroadcastChannel",
    "WebXR",
    "SharedWorker",
    "WebLocks",
    "WebHID",
    "WebShare",
    "RequestedStorageAccessGrant",
    "WebNfc",
    "OutstandingNetworkRequestFetch",
    "OutstandingNetworkRequestXHR",
    "AppBanner",
    "Printing",
    "WebDatabase",
    "PictureInPicture",
    "Portal",
    "SpeechRecognizer",
    "IdleManager",
    "PaymentManager",
    "SpeechSynthesis",
    "KeyboardLock",
    "WebOTPService",
    "OutstandingNetworkRequestDirectSocket",
    "InjectedJavascript",
    "InjectedStyleSheet",
    "KeepaliveRequest",
    "IndexedDBEvent",
    "Dummy",
    "JsNetworkRequestReceivedCacheControlNoStoreResource",
    "WebRTCSticky",
    "WebTransportSticky",
    "WebSocketSticky",
    "ContentSecurityHandler",
    "ContentWebAuthenticationAPI",
    "ContentFileChooser",
    "ContentSerial",
    "ContentFileSystemAccess",
    "ContentMediaDevicesDispatcherHost",
    "ContentWebBluetooth",
    "ContentWebUSB",
    "ContentMediaSessionService",
    "ContentScreenReader",
    "EmbedderPopupBlockerTabHelper",
    "EmbedderSafeBrowsingTriggeredPopupBlocker",
    "EmbedderSafeBrowsingThreatDetails",
    "EmbedderAppBannerManager",
    "EmbedderDomDistillerViewerSource",
    "EmbedderDomDistillerSelfDeletingRequestDelegate",
    "EmbedderOomInterventionTabHelper",
    "EmbedderOfflinePage",
    "EmbedderChromePasswordManagerClientBindCredentialManager",
    "EmbedderPermissionRequestManager",
    "EmbedderModalDialog",
    "EmbedderExtensions",
    "EmbedderExtensionMessaging",
    "EmbedderExtensionMessagingForOpenPort",
    "EmbedderExtensionSentMessageToCachedFrame",
]

BackForwardCacheNotRestoredReasonType: TypeAlias = Literal[
    "SupportPending", "PageSupportNeeded", "Circumstantial"
]


class BackForwardCacheNotRestoredExplanation(TypedDict):
    type: BackForwardCacheNotRestoredReasonType
    reason: BackForwardCacheNotRestoredReason
    context: NotRequired[str]


class BackForwardCacheNotRestoredExplanationTree(TypedDict):
    url: str
    explanations: list[BackForwardCacheNotRestoredExplanation]
    children: list[BackForwardCacheNotRestoredExplanationTree]


class AddScriptToEvaluateOnLoadParameters(TypedDict):
    scriptSource: str


class AddScriptToEvaluateOnLoadResult(TypedDict):
    identifier: ScriptIdentifier


class AddScriptToEvaluateOnNewDocumentParameters(TypedDict):
    source: str
    worldName: NotRequired[str]
    includeCommandLineAPI: NotRequired[bool]
    runImmediately: NotRequired[bool]


class AddScriptToEvaluateOnNewDocumentResult(TypedDict):
    identifier: ScriptIdentifier


class CaptureScreenshotParameters(TypedDict):
    format: NotRequired[Literal["jpeg", "png", "webp"]]
    quality: NotRequired[int]
    clip: NotRequired[Viewport]
    fromSurface: NotRequired[bool]
    captureBeyondViewport: NotRequired[bool]
    optimizeForSpeed: NotRequired[bool]


class CaptureScreenshotResult(TypedDict):
    data: str


class CaptureSnapshotParameters(TypedDict):
    format: NotRequired[Literal["mhtml"]]


class CaptureSnapshotResult(TypedDict):
    data: str


class CreateIsolatedWorldParameters(TypedDict):
    frameId: FrameId
    worldName: NotRequired[str]
    grantUniveralAccess: NotRequired[bool]


class CreateIsolatedWorldResult(TypedDict):
    executionContextId: Runtime.ExecutionContextId


class DeleteCookieParameters(TypedDict):
    cookieName: str
    url: str


class GetAppManifestResult(TypedDict):
    url: str
    errors: list[AppManifestError]
    data: NotRequired[str]
    parsed: NotRequired[AppManifestParsedProperties]


class GetInstallabilityErrorsResult(TypedDict):
    installabilityErrors: list[InstallabilityError]


class GetManifestIconsResult(TypedDict):
    primaryIcon: NotRequired[str]


class GetAppIdResult(TypedDict):
    appId: NotRequired[str]
    recommendedId: NotRequired[str]


class GetAdScriptIdParameters(TypedDict):
    frameId: FrameId


class GetAdScriptIdResult(TypedDict):
    adScriptId: NotRequired[AdScriptId]


class GetCookiesResult(TypedDict):
    cookies: list[Network.Cookie]


class GetFrameTreeResult(TypedDict):
    frameTree: FrameTree


class GetLayoutMetricsResult(TypedDict):
    layoutViewport: LayoutViewport
    visualViewport: VisualViewport
    contentSize: DOM.Rect
    cssLayoutViewport: LayoutViewport
    cssVisualViewport: VisualViewport
    cssContentSize: DOM.Rect


class GetNavigationHistoryResult(TypedDict):
    currentIndex: int
    entries: list[NavigationEntry]


class GetResourceContentParameters(TypedDict):
    frameId: FrameId
    url: str


class GetResourceContentResult(TypedDict):
    content: str
    base64Encoded: bool


class GetResourceTreeResult(TypedDict):
    frameTree: FrameResourceTree


class HandleJavaScriptDialogParameters(TypedDict):
    accept: bool
    promptText: NotRequired[str]


class NavigateParameters(TypedDict):
    url: str
    referrer: NotRequired[str]
    transitionType: NotRequired[TransitionType]
    frameId: NotRequired[FrameId]
    referrerPolicy: NotRequired[ReferrerPolicy]


class NavigateResult(TypedDict):
    frameId: FrameId
    loaderId: NotRequired[Network.LoaderId]
    errorText: NotRequired[str]


class NavigateToHistoryEntryParameters(TypedDict):
    entryId: int


class PrintToPDFParameters(TypedDict):
    landscape: NotRequired[bool]
    displayHeaderFooter: NotRequired[bool]
    printBackground: NotRequired[bool]
    scale: NotRequired[float]
    paperWidth: NotRequired[float]
    paperHeight: NotRequired[float]
    marginTop: NotRequired[float]
    marginBottom: NotRequired[float]
    marginLeft: NotRequired[float]
    marginRight: NotRequired[float]
    pageRanges: NotRequired[str]
    headerTemplate: NotRequired[str]
    footerTemplate: NotRequired[str]
    preferCSSPageSize: NotRequired[bool]
    transferMode: NotRequired[Literal["ReturnAsBase64", "ReturnAsStream"]]


class PrintToPDFResult(TypedDict):
    data: str
    stream: NotRequired[IO.StreamHandle]


class ReloadParameters(TypedDict):
    ignoreCache: NotRequired[bool]
    scriptToEvaluateOnLoad: NotRequired[str]


class RemoveScriptToEvaluateOnLoadParameters(TypedDict):
    identifier: ScriptIdentifier


class RemoveScriptToEvaluateOnNewDocumentParameters(TypedDict):
    identifier: ScriptIdentifier


class ScreencastFrameAckParameters(TypedDict):
    sessionId: int


class SearchInResourceParameters(TypedDict):
    frameId: FrameId
    url: str
    query: str
    caseSensitive: NotRequired[bool]
    isRegex: NotRequired[bool]


class SearchInResourceResult(TypedDict):
    result: list[Debugger.SearchMatch]


class SetAdBlockingEnabledParameters(TypedDict):
    enabled: bool


class SetBypassCSPParameters(TypedDict):
    enabled: bool


class GetPermissionsPolicyStateParameters(TypedDict):
    frameId: FrameId


class GetPermissionsPolicyStateResult(TypedDict):
    states: list[PermissionsPolicyFeatureState]


class GetOriginTrialsParameters(TypedDict):
    frameId: FrameId


class GetOriginTrialsResult(TypedDict):
    originTrials: list[OriginTrial]


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
    screenOrientation: NotRequired[Emulation.ScreenOrientation]
    viewport: NotRequired[Viewport]


class SetDeviceOrientationOverrideParameters(TypedDict):
    alpha: float
    beta: float
    gamma: float


class SetFontFamiliesParameters(TypedDict):
    fontFamilies: FontFamilies
    forScripts: NotRequired[list[ScriptFontFamilies]]


class SetFontSizesParameters(TypedDict):
    fontSizes: FontSizes


class SetDocumentContentParameters(TypedDict):
    frameId: FrameId
    html: str


class SetDownloadBehaviorParameters(TypedDict):
    behavior: Literal["deny", "allow", "default"]
    downloadPath: NotRequired[str]


class SetGeolocationOverrideParameters(TypedDict):
    latitude: NotRequired[float]
    longitude: NotRequired[float]
    accuracy: NotRequired[float]


class SetLifecycleEventsEnabledParameters(TypedDict):
    enabled: bool


class SetTouchEmulationEnabledParameters(TypedDict):
    enabled: bool
    configuration: NotRequired[Literal["mobile", "desktop"]]


class StartScreencastParameters(TypedDict):
    format: NotRequired[Literal["jpeg", "png"]]
    quality: NotRequired[int]
    maxWidth: NotRequired[int]
    maxHeight: NotRequired[int]
    everyNthFrame: NotRequired[int]


class SetWebLifecycleStateParameters(TypedDict):
    state: Literal["frozen", "active"]


class ProduceCompilationCacheParameters(TypedDict):
    scripts: list[CompilationCacheParams]


class AddCompilationCacheParameters(TypedDict):
    url: str
    data: str


class SetSPCTransactionModeParameters(TypedDict):
    mode: AutoResponseMode


class SetRPHRegistrationModeParameters(TypedDict):
    mode: AutoResponseMode


class GenerateTestReportParameters(TypedDict):
    message: str
    group: NotRequired[str]


class SetInterceptFileChooserDialogParameters(TypedDict):
    enabled: bool


class SetPrerenderingAllowedParameters(TypedDict):
    isAllowed: bool


class DomContentEventFiredEvent(TypedDict):
    timestamp: Network.MonotonicTime


class FileChooserOpenedEvent(TypedDict):
    frameId: FrameId
    mode: Literal["selectSingle", "selectMultiple"]
    backendNodeId: NotRequired[DOM.BackendNodeId]


class FrameAttachedEvent(TypedDict):
    frameId: FrameId
    parentFrameId: FrameId
    stack: NotRequired[Runtime.StackTrace]


class FrameClearedScheduledNavigationEvent(TypedDict):
    frameId: FrameId


class FrameDetachedEvent(TypedDict):
    frameId: FrameId
    reason: Literal["remove", "swap"]


class FrameNavigatedEvent(TypedDict):
    frame: Frame
    type: NavigationType


class DocumentOpenedEvent(TypedDict):
    frame: Frame


class FrameRequestedNavigationEvent(TypedDict):
    frameId: FrameId
    reason: ClientNavigationReason
    url: str
    disposition: ClientNavigationDisposition


class FrameScheduledNavigationEvent(TypedDict):
    frameId: FrameId
    delay: float
    reason: ClientNavigationReason
    url: str


class FrameStartedLoadingEvent(TypedDict):
    frameId: FrameId


class FrameStoppedLoadingEvent(TypedDict):
    frameId: FrameId


class DownloadWillBeginEvent(TypedDict):
    frameId: FrameId
    guid: str
    url: str
    suggestedFilename: str


class DownloadProgressEvent(TypedDict):
    guid: str
    totalBytes: float
    receivedBytes: float
    state: Literal["inProgress", "completed", "canceled"]


class JavascriptDialogClosedEvent(TypedDict):
    result: bool
    userInput: str


class JavascriptDialogOpeningEvent(TypedDict):
    url: str
    message: str
    type: DialogType
    hasBrowserHandler: bool
    defaultPrompt: NotRequired[str]


class LifecycleEventEvent(TypedDict):
    frameId: FrameId
    loaderId: Network.LoaderId
    name: str
    timestamp: Network.MonotonicTime


class BackForwardCacheNotUsedEvent(TypedDict):
    loaderId: Network.LoaderId
    frameId: FrameId
    notRestoredExplanations: list[BackForwardCacheNotRestoredExplanation]
    notRestoredExplanationsTree: NotRequired[BackForwardCacheNotRestoredExplanationTree]


class LoadEventFiredEvent(TypedDict):
    timestamp: Network.MonotonicTime


class NavigatedWithinDocumentEvent(TypedDict):
    frameId: FrameId
    url: str


class ScreencastFrameEvent(TypedDict):
    data: str
    metadata: ScreencastFrameMetadata
    sessionId: int


class ScreencastVisibilityChangedEvent(TypedDict):
    visible: bool


class WindowOpenEvent(TypedDict):
    url: str
    windowName: str
    windowFeatures: list[str]
    userGesture: bool


class CompilationCacheProducedEvent(TypedDict):
    url: str
    data: str


class Page(BaseDomain):
    """Actions and events related to the inspected page belong to the page domain."""

    domain_name = "Page"

    @overload
    async def addScriptToEvaluateOnLoad(
        self,
        params: AddScriptToEvaluateOnLoadParameters,
        session_id: str | None = None,
    ) -> AddScriptToEvaluateOnLoadResult: ...

    @overload
    async def addScriptToEvaluateOnLoad(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[AddScriptToEvaluateOnLoadParameters],
    ) -> AddScriptToEvaluateOnLoadResult: ...

    async def addScriptToEvaluateOnLoad(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> AddScriptToEvaluateOnLoadResult:
        """Deprecated, please use addScriptToEvaluateOnNewDocument instead."""

        return cast(
            AddScriptToEvaluateOnLoadResult,
            await self._command(
                "addScriptToEvaluateOnLoad", params, session_id, kwargs
            ),
        )

    @overload
    async def addScriptToEvaluateOnNewDocument(
        self,
        params: AddScriptToEvaluateOnNewDocumentParameters,
        session_id: str | None = None,
    ) -> AddScriptToEvaluateOnNewDocumentResult: ...

    @overload
    async def addScriptToEvaluateOnNewDocument(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[AddScriptToEvaluateOnNewDocumentParameters],
    ) -> AddScriptToEvaluateOnNewDocumentResult: ...

    async def addScriptToEvaluateOnNewDocument(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> AddScriptToEvaluateOnNewDocumentResult:
        """Evaluates given script in every frame upon creation (before loading frame's scripts)."""

        return cast(
            AddScriptToEvaluateOnNewDocumentResult,
            await self._command(
                "addScriptToEvaluateOnNewDocument", params, session_id, kwargs
            ),
        )

    async def bringToFront(
        self,
        session_id: str | None = None,
    ) -> JsonObject:
        """Brings page to front (activates tab)."""

        return await self._command("bringToFront", None, session_id, {})

    @overload
    async def captureScreenshot(
        self,
        params: CaptureScreenshotParameters,
        session_id: str | None = None,
    ) -> CaptureScreenshotResult: ...

    @overload
    async def captureScreenshot(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[CaptureScreenshotParameters],
    ) -> CaptureScreenshotResult: ...

    async def captureScreenshot(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> CaptureScreenshotResult:
        """Capture page screenshot."""

        return cast(
            CaptureScreenshotResult,
            await self._command("captureScreenshot", params, session_id, kwargs),
        )

    @overload
    async def captureSnapshot(
        self,
        params: CaptureSnapshotParameters,
        session_id: str | None = None,
    ) -> CaptureSnapshotResult: ...

    @overload
    async def captureSnapshot(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[CaptureSnapshotParameters],
    ) -> CaptureSnapshotResult: ...

    async def captureSnapshot(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> CaptureSnapshotResult:
        """Returns a snapshot of the page as a string. For MHTML format, the serialization includes iframes, shadow DOM, external resources, and element-inline styles."""

        return cast(
            CaptureSnapshotResult,
            await self._command("captureSnapshot", params, session_id, kwargs),
        )

    async def clearDeviceMetricsOverride(
        self,
        session_id: str | None = None,
    ) -> JsonObject:
        """Clears the overridden device metrics."""

        return await self._command("clearDeviceMetricsOverride", None, session_id, {})

    async def clearDeviceOrientationOverride(
        self,
        session_id: str | None = None,
    ) -> JsonObject:
        """Clears the overridden Device Orientation."""

        return await self._command(
            "clearDeviceOrientationOverride", None, session_id, {}
        )

    async def clearGeolocationOverride(
        self,
        session_id: str | None = None,
    ) -> JsonObject:
        """Clears the overridden Geolocation Position and Error."""

        return await self._command("clearGeolocationOverride", None, session_id, {})

    @overload
    async def createIsolatedWorld(
        self,
        params: CreateIsolatedWorldParameters,
        session_id: str | None = None,
    ) -> CreateIsolatedWorldResult: ...

    @overload
    async def createIsolatedWorld(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[CreateIsolatedWorldParameters],
    ) -> CreateIsolatedWorldResult: ...

    async def createIsolatedWorld(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> CreateIsolatedWorldResult:
        """Creates an isolated world for the given frame."""

        return cast(
            CreateIsolatedWorldResult,
            await self._command("createIsolatedWorld", params, session_id, kwargs),
        )

    @overload
    async def deleteCookie(
        self,
        params: DeleteCookieParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def deleteCookie(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[DeleteCookieParameters],
    ) -> JsonObject: ...

    async def deleteCookie(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Deletes browser cookie with given name, domain and path."""

        return await self._command("deleteCookie", params, session_id, kwargs)

    async def disable(
        self,
        session_id: str | None = None,
    ) -> JsonObject:
        """Disables page domain notifications."""

        return await self._command("disable", None, session_id, {})

    async def enable(
        self,
        session_id: str | None = None,
    ) -> JsonObject:
        """Enables page domain notifications."""

        return await self._command("enable", None, session_id, {})

    async def getAppManifest(
        self,
        session_id: str | None = None,
    ) -> GetAppManifestResult:
        """Send Page.getAppManifest."""

        return cast(
            GetAppManifestResult,
            await self._command("getAppManifest", None, session_id, {}),
        )

    async def getInstallabilityErrors(
        self,
        session_id: str | None = None,
    ) -> GetInstallabilityErrorsResult:
        """Send Page.getInstallabilityErrors."""

        return cast(
            GetInstallabilityErrorsResult,
            await self._command("getInstallabilityErrors", None, session_id, {}),
        )

    async def getManifestIcons(
        self,
        session_id: str | None = None,
    ) -> GetManifestIconsResult:
        """Deprecated because it's not guaranteed that the returned icon is in fact the one used for PWA installation."""

        return cast(
            GetManifestIconsResult,
            await self._command("getManifestIcons", None, session_id, {}),
        )

    async def getAppId(
        self,
        session_id: str | None = None,
    ) -> GetAppIdResult:
        """Returns the unique (PWA) app id. Only returns values if the feature flag 'WebAppEnableManifestId' is enabled"""

        return cast(
            GetAppIdResult, await self._command("getAppId", None, session_id, {})
        )

    @overload
    async def getAdScriptId(
        self,
        params: GetAdScriptIdParameters,
        session_id: str | None = None,
    ) -> GetAdScriptIdResult: ...

    @overload
    async def getAdScriptId(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[GetAdScriptIdParameters],
    ) -> GetAdScriptIdResult: ...

    async def getAdScriptId(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> GetAdScriptIdResult:
        """Send Page.getAdScriptId."""

        return cast(
            GetAdScriptIdResult,
            await self._command("getAdScriptId", params, session_id, kwargs),
        )

    async def getCookies(
        self,
        session_id: str | None = None,
    ) -> GetCookiesResult:
        """Returns all browser cookies for the page and all of its subframes. Depending on the backend support, will return detailed cookie information in the `cookies` field."""

        return cast(
            GetCookiesResult, await self._command("getCookies", None, session_id, {})
        )

    async def getFrameTree(
        self,
        session_id: str | None = None,
    ) -> GetFrameTreeResult:
        """Returns present frame tree structure."""

        return cast(
            GetFrameTreeResult,
            await self._command("getFrameTree", None, session_id, {}),
        )

    async def getLayoutMetrics(
        self,
        session_id: str | None = None,
    ) -> GetLayoutMetricsResult:
        """Returns metrics relating to the layouting of the page, such as viewport bounds/scale."""

        return cast(
            GetLayoutMetricsResult,
            await self._command("getLayoutMetrics", None, session_id, {}),
        )

    async def getNavigationHistory(
        self,
        session_id: str | None = None,
    ) -> GetNavigationHistoryResult:
        """Returns navigation history for the current page."""

        return cast(
            GetNavigationHistoryResult,
            await self._command("getNavigationHistory", None, session_id, {}),
        )

    async def resetNavigationHistory(
        self,
        session_id: str | None = None,
    ) -> JsonObject:
        """Resets navigation history for the current page."""

        return await self._command("resetNavigationHistory", None, session_id, {})

    @overload
    async def getResourceContent(
        self,
        params: GetResourceContentParameters,
        session_id: str | None = None,
    ) -> GetResourceContentResult: ...

    @overload
    async def getResourceContent(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[GetResourceContentParameters],
    ) -> GetResourceContentResult: ...

    async def getResourceContent(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> GetResourceContentResult:
        """Returns content of the given resource."""

        return cast(
            GetResourceContentResult,
            await self._command("getResourceContent", params, session_id, kwargs),
        )

    async def getResourceTree(
        self,
        session_id: str | None = None,
    ) -> GetResourceTreeResult:
        """Returns present frame / resource tree structure."""

        return cast(
            GetResourceTreeResult,
            await self._command("getResourceTree", None, session_id, {}),
        )

    @overload
    async def handleJavaScriptDialog(
        self,
        params: HandleJavaScriptDialogParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def handleJavaScriptDialog(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[HandleJavaScriptDialogParameters],
    ) -> JsonObject: ...

    async def handleJavaScriptDialog(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Accepts or dismisses a JavaScript initiated dialog (alert, confirm, prompt, or onbeforeunload)."""

        return await self._command("handleJavaScriptDialog", params, session_id, kwargs)

    @overload
    async def navigate(
        self,
        params: NavigateParameters,
        session_id: str | None = None,
    ) -> NavigateResult: ...

    @overload
    async def navigate(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[NavigateParameters],
    ) -> NavigateResult: ...

    async def navigate(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> NavigateResult:
        """Navigates current page to the given URL."""

        return cast(
            NavigateResult, await self._command("navigate", params, session_id, kwargs)
        )

    @overload
    async def navigateToHistoryEntry(
        self,
        params: NavigateToHistoryEntryParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def navigateToHistoryEntry(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[NavigateToHistoryEntryParameters],
    ) -> JsonObject: ...

    async def navigateToHistoryEntry(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Navigates current page to the given history entry."""

        return await self._command("navigateToHistoryEntry", params, session_id, kwargs)

    @overload
    async def printToPDF(
        self,
        params: PrintToPDFParameters,
        session_id: str | None = None,
    ) -> PrintToPDFResult: ...

    @overload
    async def printToPDF(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[PrintToPDFParameters],
    ) -> PrintToPDFResult: ...

    async def printToPDF(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> PrintToPDFResult:
        """Print page as PDF."""

        return cast(
            PrintToPDFResult,
            await self._command("printToPDF", params, session_id, kwargs),
        )

    @overload
    async def reload(
        self,
        params: ReloadParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def reload(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[ReloadParameters],
    ) -> JsonObject: ...

    async def reload(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Reloads given page optionally ignoring the cache."""

        return await self._command("reload", params, session_id, kwargs)

    @overload
    async def removeScriptToEvaluateOnLoad(
        self,
        params: RemoveScriptToEvaluateOnLoadParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def removeScriptToEvaluateOnLoad(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[RemoveScriptToEvaluateOnLoadParameters],
    ) -> JsonObject: ...

    async def removeScriptToEvaluateOnLoad(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Deprecated, please use removeScriptToEvaluateOnNewDocument instead."""

        return await self._command(
            "removeScriptToEvaluateOnLoad", params, session_id, kwargs
        )

    @overload
    async def removeScriptToEvaluateOnNewDocument(
        self,
        params: RemoveScriptToEvaluateOnNewDocumentParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def removeScriptToEvaluateOnNewDocument(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[RemoveScriptToEvaluateOnNewDocumentParameters],
    ) -> JsonObject: ...

    async def removeScriptToEvaluateOnNewDocument(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Removes given script from the list."""

        return await self._command(
            "removeScriptToEvaluateOnNewDocument", params, session_id, kwargs
        )

    @overload
    async def screencastFrameAck(
        self,
        params: ScreencastFrameAckParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def screencastFrameAck(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[ScreencastFrameAckParameters],
    ) -> JsonObject: ...

    async def screencastFrameAck(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Acknowledges that a screencast frame has been received by the frontend."""

        return await self._command("screencastFrameAck", params, session_id, kwargs)

    @overload
    async def searchInResource(
        self,
        params: SearchInResourceParameters,
        session_id: str | None = None,
    ) -> SearchInResourceResult: ...

    @overload
    async def searchInResource(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SearchInResourceParameters],
    ) -> SearchInResourceResult: ...

    async def searchInResource(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> SearchInResourceResult:
        """Searches for given string in resource content."""

        return cast(
            SearchInResourceResult,
            await self._command("searchInResource", params, session_id, kwargs),
        )

    @overload
    async def setAdBlockingEnabled(
        self,
        params: SetAdBlockingEnabledParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def setAdBlockingEnabled(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetAdBlockingEnabledParameters],
    ) -> JsonObject: ...

    async def setAdBlockingEnabled(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Enable Chrome's experimental ad filter on all sites."""

        return await self._command("setAdBlockingEnabled", params, session_id, kwargs)

    @overload
    async def setBypassCSP(
        self,
        params: SetBypassCSPParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def setBypassCSP(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetBypassCSPParameters],
    ) -> JsonObject: ...

    async def setBypassCSP(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Enable page Content Security Policy by-passing."""

        return await self._command("setBypassCSP", params, session_id, kwargs)

    @overload
    async def getPermissionsPolicyState(
        self,
        params: GetPermissionsPolicyStateParameters,
        session_id: str | None = None,
    ) -> GetPermissionsPolicyStateResult: ...

    @overload
    async def getPermissionsPolicyState(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[GetPermissionsPolicyStateParameters],
    ) -> GetPermissionsPolicyStateResult: ...

    async def getPermissionsPolicyState(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> GetPermissionsPolicyStateResult:
        """Get Permissions Policy state on given frame."""

        return cast(
            GetPermissionsPolicyStateResult,
            await self._command(
                "getPermissionsPolicyState", params, session_id, kwargs
            ),
        )

    @overload
    async def getOriginTrials(
        self,
        params: GetOriginTrialsParameters,
        session_id: str | None = None,
    ) -> GetOriginTrialsResult: ...

    @overload
    async def getOriginTrials(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[GetOriginTrialsParameters],
    ) -> GetOriginTrialsResult: ...

    async def getOriginTrials(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> GetOriginTrialsResult:
        """Get Origin Trials on given frame."""

        return cast(
            GetOriginTrialsResult,
            await self._command("getOriginTrials", params, session_id, kwargs),
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
    async def setDeviceOrientationOverride(
        self,
        params: SetDeviceOrientationOverrideParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def setDeviceOrientationOverride(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetDeviceOrientationOverrideParameters],
    ) -> JsonObject: ...

    async def setDeviceOrientationOverride(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Overrides the Device Orientation."""

        return await self._command(
            "setDeviceOrientationOverride", params, session_id, kwargs
        )

    @overload
    async def setFontFamilies(
        self,
        params: SetFontFamiliesParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def setFontFamilies(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetFontFamiliesParameters],
    ) -> JsonObject: ...

    async def setFontFamilies(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Set generic font families."""

        return await self._command("setFontFamilies", params, session_id, kwargs)

    @overload
    async def setFontSizes(
        self,
        params: SetFontSizesParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def setFontSizes(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetFontSizesParameters],
    ) -> JsonObject: ...

    async def setFontSizes(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Set default font sizes."""

        return await self._command("setFontSizes", params, session_id, kwargs)

    @overload
    async def setDocumentContent(
        self,
        params: SetDocumentContentParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def setDocumentContent(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetDocumentContentParameters],
    ) -> JsonObject: ...

    async def setDocumentContent(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Sets given markup as the document's HTML."""

        return await self._command("setDocumentContent", params, session_id, kwargs)

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
    async def setLifecycleEventsEnabled(
        self,
        params: SetLifecycleEventsEnabledParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def setLifecycleEventsEnabled(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetLifecycleEventsEnabledParameters],
    ) -> JsonObject: ...

    async def setLifecycleEventsEnabled(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Controls whether page will emit lifecycle events."""

        return await self._command(
            "setLifecycleEventsEnabled", params, session_id, kwargs
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
        """Toggles mouse event-based touch event emulation."""

        return await self._command(
            "setTouchEmulationEnabled", params, session_id, kwargs
        )

    @overload
    async def startScreencast(
        self,
        params: StartScreencastParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def startScreencast(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[StartScreencastParameters],
    ) -> JsonObject: ...

    async def startScreencast(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Starts sending each frame using the `screencastFrame` event."""

        return await self._command("startScreencast", params, session_id, kwargs)

    async def stopLoading(
        self,
        session_id: str | None = None,
    ) -> JsonObject:
        """Force the page stop all navigations and pending resource fetches."""

        return await self._command("stopLoading", None, session_id, {})

    async def crash(
        self,
        session_id: str | None = None,
    ) -> JsonObject:
        """Crashes renderer on the IO thread, generates minidumps."""

        return await self._command("crash", None, session_id, {})

    async def close(
        self,
        session_id: str | None = None,
    ) -> JsonObject:
        """Tries to close page, running its beforeunload hooks, if any."""

        return await self._command("close", None, session_id, {})

    @overload
    async def setWebLifecycleState(
        self,
        params: SetWebLifecycleStateParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def setWebLifecycleState(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetWebLifecycleStateParameters],
    ) -> JsonObject: ...

    async def setWebLifecycleState(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Tries to update the web lifecycle state of the page. It will transition the page to the given state according to: https://github.com/WICG/web-lifecycle/"""

        return await self._command("setWebLifecycleState", params, session_id, kwargs)

    async def stopScreencast(
        self,
        session_id: str | None = None,
    ) -> JsonObject:
        """Stops sending each frame in the `screencastFrame`."""

        return await self._command("stopScreencast", None, session_id, {})

    @overload
    async def produceCompilationCache(
        self,
        params: ProduceCompilationCacheParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def produceCompilationCache(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[ProduceCompilationCacheParameters],
    ) -> JsonObject: ...

    async def produceCompilationCache(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Requests backend to produce compilation cache for the specified scripts. `scripts` are appeneded to the list of scripts for which the cache would be produced. The list may be reset during page navigation. When script with a matching URL is encountered, the cache is optionally produced upon backend discretion, based on internal heuristics. See also: `Page.compilationCacheProduced`."""

        return await self._command(
            "produceCompilationCache", params, session_id, kwargs
        )

    @overload
    async def addCompilationCache(
        self,
        params: AddCompilationCacheParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def addCompilationCache(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[AddCompilationCacheParameters],
    ) -> JsonObject: ...

    async def addCompilationCache(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Seeds compilation cache for given url. Compilation cache does not survive cross-process navigation."""

        return await self._command("addCompilationCache", params, session_id, kwargs)

    async def clearCompilationCache(
        self,
        session_id: str | None = None,
    ) -> JsonObject:
        """Clears seeded compilation cache."""

        return await self._command("clearCompilationCache", None, session_id, {})

    @overload
    async def setSPCTransactionMode(
        self,
        params: SetSPCTransactionModeParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def setSPCTransactionMode(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetSPCTransactionModeParameters],
    ) -> JsonObject: ...

    async def setSPCTransactionMode(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Sets the Secure Payment Confirmation transaction mode. https://w3c.github.io/secure-payment-confirmation/#sctn-automation-set-spc-transaction-mode"""

        return await self._command("setSPCTransactionMode", params, session_id, kwargs)

    @overload
    async def setRPHRegistrationMode(
        self,
        params: SetRPHRegistrationModeParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def setRPHRegistrationMode(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetRPHRegistrationModeParameters],
    ) -> JsonObject: ...

    async def setRPHRegistrationMode(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Extensions for Custom Handlers API: https://html.spec.whatwg.org/multipage/system-state.html#rph-automation"""

        return await self._command("setRPHRegistrationMode", params, session_id, kwargs)

    @overload
    async def generateTestReport(
        self,
        params: GenerateTestReportParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def generateTestReport(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[GenerateTestReportParameters],
    ) -> JsonObject: ...

    async def generateTestReport(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Generates a report for testing."""

        return await self._command("generateTestReport", params, session_id, kwargs)

    async def waitForDebugger(
        self,
        session_id: str | None = None,
    ) -> JsonObject:
        """Pauses page execution. Can be resumed using generic Runtime.runIfWaitingForDebugger."""

        return await self._command("waitForDebugger", None, session_id, {})

    @overload
    async def setInterceptFileChooserDialog(
        self,
        params: SetInterceptFileChooserDialogParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def setInterceptFileChooserDialog(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetInterceptFileChooserDialogParameters],
    ) -> JsonObject: ...

    async def setInterceptFileChooserDialog(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Intercept file chooser requests and transfer control to protocol clients. When file chooser interception is enabled, native file chooser dialog is not shown. Instead, a protocol event `Page.fileChooserOpened` is emitted."""

        return await self._command(
            "setInterceptFileChooserDialog", params, session_id, kwargs
        )

    @overload
    async def setPrerenderingAllowed(
        self,
        params: SetPrerenderingAllowedParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def setPrerenderingAllowed(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetPrerenderingAllowedParameters],
    ) -> JsonObject: ...

    async def setPrerenderingAllowed(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Enable/disable prerendering manually. This command is a short-term solution for https://crbug.com/1440085. See https://docs.google.com/document/d/12HVmFxYj5Jc-eJr5OmWsa2bqTJsbgGLKI6ZIyx0_wpA for more details. TODO(https://crbug.com/1440085): Remove this once Puppeteer supports tab targets."""

        return await self._command("setPrerenderingAllowed", params, session_id, kwargs)

    @overload
    def domContentEventFired(
        self,
        callback_or_session: EventCallback[DomContentEventFiredEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def domContentEventFired(
        self,
        callback_or_session: str,
        handler: EventCallback[DomContentEventFiredEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def domContentEventFired(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[DomContentEventFiredEvent]: ...

    def domContentEventFired(
        self,
        callback_or_session: EventCallback[DomContentEventFiredEvent]
        | str
        | None = None,
        handler: EventCallback[DomContentEventFiredEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[DomContentEventFiredEvent] | Unsubscribe:
        """Wait for or subscribe to Page.domContentEventFired."""

        return cast(
            Awaitable[DomContentEventFiredEvent] | Unsubscribe,
            self._event(
                "domContentEventFired",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def fileChooserOpened(
        self,
        callback_or_session: EventCallback[FileChooserOpenedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def fileChooserOpened(
        self,
        callback_or_session: str,
        handler: EventCallback[FileChooserOpenedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def fileChooserOpened(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[FileChooserOpenedEvent]: ...

    def fileChooserOpened(
        self,
        callback_or_session: EventCallback[FileChooserOpenedEvent] | str | None = None,
        handler: EventCallback[FileChooserOpenedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[FileChooserOpenedEvent] | Unsubscribe:
        """Emitted only when `page.interceptFileChooser` is enabled."""

        return cast(
            Awaitable[FileChooserOpenedEvent] | Unsubscribe,
            self._event(
                "fileChooserOpened",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def frameAttached(
        self,
        callback_or_session: EventCallback[FrameAttachedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def frameAttached(
        self,
        callback_or_session: str,
        handler: EventCallback[FrameAttachedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def frameAttached(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[FrameAttachedEvent]: ...

    def frameAttached(
        self,
        callback_or_session: EventCallback[FrameAttachedEvent] | str | None = None,
        handler: EventCallback[FrameAttachedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[FrameAttachedEvent] | Unsubscribe:
        """Fired when frame has been attached to its parent."""

        return cast(
            Awaitable[FrameAttachedEvent] | Unsubscribe,
            self._event(
                "frameAttached",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def frameClearedScheduledNavigation(
        self,
        callback_or_session: EventCallback[FrameClearedScheduledNavigationEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def frameClearedScheduledNavigation(
        self,
        callback_or_session: str,
        handler: EventCallback[FrameClearedScheduledNavigationEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def frameClearedScheduledNavigation(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[FrameClearedScheduledNavigationEvent]: ...

    def frameClearedScheduledNavigation(
        self,
        callback_or_session: EventCallback[FrameClearedScheduledNavigationEvent]
        | str
        | None = None,
        handler: EventCallback[FrameClearedScheduledNavigationEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[FrameClearedScheduledNavigationEvent] | Unsubscribe:
        """Fired when frame no longer has a scheduled navigation."""

        return cast(
            Awaitable[FrameClearedScheduledNavigationEvent] | Unsubscribe,
            self._event(
                "frameClearedScheduledNavigation",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def frameDetached(
        self,
        callback_or_session: EventCallback[FrameDetachedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def frameDetached(
        self,
        callback_or_session: str,
        handler: EventCallback[FrameDetachedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def frameDetached(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[FrameDetachedEvent]: ...

    def frameDetached(
        self,
        callback_or_session: EventCallback[FrameDetachedEvent] | str | None = None,
        handler: EventCallback[FrameDetachedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[FrameDetachedEvent] | Unsubscribe:
        """Fired when frame has been detached from its parent."""

        return cast(
            Awaitable[FrameDetachedEvent] | Unsubscribe,
            self._event(
                "frameDetached",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def frameNavigated(
        self,
        callback_or_session: EventCallback[FrameNavigatedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def frameNavigated(
        self,
        callback_or_session: str,
        handler: EventCallback[FrameNavigatedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def frameNavigated(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[FrameNavigatedEvent]: ...

    def frameNavigated(
        self,
        callback_or_session: EventCallback[FrameNavigatedEvent] | str | None = None,
        handler: EventCallback[FrameNavigatedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[FrameNavigatedEvent] | Unsubscribe:
        """Fired once navigation of the frame has completed. Frame is now associated with the new loader."""

        return cast(
            Awaitable[FrameNavigatedEvent] | Unsubscribe,
            self._event(
                "frameNavigated",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def documentOpened(
        self,
        callback_or_session: EventCallback[DocumentOpenedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def documentOpened(
        self,
        callback_or_session: str,
        handler: EventCallback[DocumentOpenedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def documentOpened(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[DocumentOpenedEvent]: ...

    def documentOpened(
        self,
        callback_or_session: EventCallback[DocumentOpenedEvent] | str | None = None,
        handler: EventCallback[DocumentOpenedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[DocumentOpenedEvent] | Unsubscribe:
        """Fired when opening document to write to."""

        return cast(
            Awaitable[DocumentOpenedEvent] | Unsubscribe,
            self._event(
                "documentOpened",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def frameResized(
        self,
        callback_or_session: EventCallback[JsonObject],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def frameResized(
        self,
        callback_or_session: str,
        handler: EventCallback[JsonObject],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def frameResized(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[JsonObject]: ...

    def frameResized(
        self,
        callback_or_session: EventCallback[JsonObject] | str | None = None,
        handler: EventCallback[JsonObject] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[JsonObject] | Unsubscribe:
        """Wait for or subscribe to Page.frameResized."""

        return self._event(
            "frameResized",
            cast(EventCallback[Mapping[str, object]] | str | None, callback_or_session),
            cast(EventCallback[Mapping[str, object]] | None, handler),
            session_id,
        )

    @overload
    def frameRequestedNavigation(
        self,
        callback_or_session: EventCallback[FrameRequestedNavigationEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def frameRequestedNavigation(
        self,
        callback_or_session: str,
        handler: EventCallback[FrameRequestedNavigationEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def frameRequestedNavigation(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[FrameRequestedNavigationEvent]: ...

    def frameRequestedNavigation(
        self,
        callback_or_session: EventCallback[FrameRequestedNavigationEvent]
        | str
        | None = None,
        handler: EventCallback[FrameRequestedNavigationEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[FrameRequestedNavigationEvent] | Unsubscribe:
        """Fired when a renderer-initiated navigation is requested. Navigation may still be cancelled after the event is issued."""

        return cast(
            Awaitable[FrameRequestedNavigationEvent] | Unsubscribe,
            self._event(
                "frameRequestedNavigation",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def frameScheduledNavigation(
        self,
        callback_or_session: EventCallback[FrameScheduledNavigationEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def frameScheduledNavigation(
        self,
        callback_or_session: str,
        handler: EventCallback[FrameScheduledNavigationEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def frameScheduledNavigation(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[FrameScheduledNavigationEvent]: ...

    def frameScheduledNavigation(
        self,
        callback_or_session: EventCallback[FrameScheduledNavigationEvent]
        | str
        | None = None,
        handler: EventCallback[FrameScheduledNavigationEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[FrameScheduledNavigationEvent] | Unsubscribe:
        """Fired when frame schedules a potential navigation."""

        return cast(
            Awaitable[FrameScheduledNavigationEvent] | Unsubscribe,
            self._event(
                "frameScheduledNavigation",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def frameStartedLoading(
        self,
        callback_or_session: EventCallback[FrameStartedLoadingEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def frameStartedLoading(
        self,
        callback_or_session: str,
        handler: EventCallback[FrameStartedLoadingEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def frameStartedLoading(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[FrameStartedLoadingEvent]: ...

    def frameStartedLoading(
        self,
        callback_or_session: EventCallback[FrameStartedLoadingEvent]
        | str
        | None = None,
        handler: EventCallback[FrameStartedLoadingEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[FrameStartedLoadingEvent] | Unsubscribe:
        """Fired when frame has started loading."""

        return cast(
            Awaitable[FrameStartedLoadingEvent] | Unsubscribe,
            self._event(
                "frameStartedLoading",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def frameStoppedLoading(
        self,
        callback_or_session: EventCallback[FrameStoppedLoadingEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def frameStoppedLoading(
        self,
        callback_or_session: str,
        handler: EventCallback[FrameStoppedLoadingEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def frameStoppedLoading(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[FrameStoppedLoadingEvent]: ...

    def frameStoppedLoading(
        self,
        callback_or_session: EventCallback[FrameStoppedLoadingEvent]
        | str
        | None = None,
        handler: EventCallback[FrameStoppedLoadingEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[FrameStoppedLoadingEvent] | Unsubscribe:
        """Fired when frame has stopped loading."""

        return cast(
            Awaitable[FrameStoppedLoadingEvent] | Unsubscribe,
            self._event(
                "frameStoppedLoading",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
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
        """Fired when page is about to start a download. Deprecated. Use Browser.downloadWillBegin instead."""

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
        """Fired when download makes progress. Last call has |done| == true. Deprecated. Use Browser.downloadProgress instead."""

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

    @overload
    def interstitialHidden(
        self,
        callback_or_session: EventCallback[JsonObject],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def interstitialHidden(
        self,
        callback_or_session: str,
        handler: EventCallback[JsonObject],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def interstitialHidden(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[JsonObject]: ...

    def interstitialHidden(
        self,
        callback_or_session: EventCallback[JsonObject] | str | None = None,
        handler: EventCallback[JsonObject] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[JsonObject] | Unsubscribe:
        """Fired when interstitial page was hidden"""

        return self._event(
            "interstitialHidden",
            cast(EventCallback[Mapping[str, object]] | str | None, callback_or_session),
            cast(EventCallback[Mapping[str, object]] | None, handler),
            session_id,
        )

    @overload
    def interstitialShown(
        self,
        callback_or_session: EventCallback[JsonObject],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def interstitialShown(
        self,
        callback_or_session: str,
        handler: EventCallback[JsonObject],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def interstitialShown(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[JsonObject]: ...

    def interstitialShown(
        self,
        callback_or_session: EventCallback[JsonObject] | str | None = None,
        handler: EventCallback[JsonObject] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[JsonObject] | Unsubscribe:
        """Fired when interstitial page was shown"""

        return self._event(
            "interstitialShown",
            cast(EventCallback[Mapping[str, object]] | str | None, callback_or_session),
            cast(EventCallback[Mapping[str, object]] | None, handler),
            session_id,
        )

    @overload
    def javascriptDialogClosed(
        self,
        callback_or_session: EventCallback[JavascriptDialogClosedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def javascriptDialogClosed(
        self,
        callback_or_session: str,
        handler: EventCallback[JavascriptDialogClosedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def javascriptDialogClosed(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[JavascriptDialogClosedEvent]: ...

    def javascriptDialogClosed(
        self,
        callback_or_session: EventCallback[JavascriptDialogClosedEvent]
        | str
        | None = None,
        handler: EventCallback[JavascriptDialogClosedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[JavascriptDialogClosedEvent] | Unsubscribe:
        """Fired when a JavaScript initiated dialog (alert, confirm, prompt, or onbeforeunload) has been closed."""

        return cast(
            Awaitable[JavascriptDialogClosedEvent] | Unsubscribe,
            self._event(
                "javascriptDialogClosed",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def javascriptDialogOpening(
        self,
        callback_or_session: EventCallback[JavascriptDialogOpeningEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def javascriptDialogOpening(
        self,
        callback_or_session: str,
        handler: EventCallback[JavascriptDialogOpeningEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def javascriptDialogOpening(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[JavascriptDialogOpeningEvent]: ...

    def javascriptDialogOpening(
        self,
        callback_or_session: EventCallback[JavascriptDialogOpeningEvent]
        | str
        | None = None,
        handler: EventCallback[JavascriptDialogOpeningEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[JavascriptDialogOpeningEvent] | Unsubscribe:
        """Fired when a JavaScript initiated dialog (alert, confirm, prompt, or onbeforeunload) is about to open."""

        return cast(
            Awaitable[JavascriptDialogOpeningEvent] | Unsubscribe,
            self._event(
                "javascriptDialogOpening",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def lifecycleEvent(
        self,
        callback_or_session: EventCallback[LifecycleEventEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def lifecycleEvent(
        self,
        callback_or_session: str,
        handler: EventCallback[LifecycleEventEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def lifecycleEvent(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[LifecycleEventEvent]: ...

    def lifecycleEvent(
        self,
        callback_or_session: EventCallback[LifecycleEventEvent] | str | None = None,
        handler: EventCallback[LifecycleEventEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[LifecycleEventEvent] | Unsubscribe:
        """Fired for top level page lifecycle events such as navigation, load, paint, etc."""

        return cast(
            Awaitable[LifecycleEventEvent] | Unsubscribe,
            self._event(
                "lifecycleEvent",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def backForwardCacheNotUsed(
        self,
        callback_or_session: EventCallback[BackForwardCacheNotUsedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def backForwardCacheNotUsed(
        self,
        callback_or_session: str,
        handler: EventCallback[BackForwardCacheNotUsedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def backForwardCacheNotUsed(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[BackForwardCacheNotUsedEvent]: ...

    def backForwardCacheNotUsed(
        self,
        callback_or_session: EventCallback[BackForwardCacheNotUsedEvent]
        | str
        | None = None,
        handler: EventCallback[BackForwardCacheNotUsedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[BackForwardCacheNotUsedEvent] | Unsubscribe:
        """Fired for failed bfcache history navigations if BackForwardCache feature is enabled. Do not assume any ordering with the Page.frameNavigated event. This event is fired only for main-frame history navigation where the document changes (non-same-document navigations), when bfcache navigation fails."""

        return cast(
            Awaitable[BackForwardCacheNotUsedEvent] | Unsubscribe,
            self._event(
                "backForwardCacheNotUsed",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def loadEventFired(
        self,
        callback_or_session: EventCallback[LoadEventFiredEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def loadEventFired(
        self,
        callback_or_session: str,
        handler: EventCallback[LoadEventFiredEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def loadEventFired(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[LoadEventFiredEvent]: ...

    def loadEventFired(
        self,
        callback_or_session: EventCallback[LoadEventFiredEvent] | str | None = None,
        handler: EventCallback[LoadEventFiredEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[LoadEventFiredEvent] | Unsubscribe:
        """Wait for or subscribe to Page.loadEventFired."""

        return cast(
            Awaitable[LoadEventFiredEvent] | Unsubscribe,
            self._event(
                "loadEventFired",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def navigatedWithinDocument(
        self,
        callback_or_session: EventCallback[NavigatedWithinDocumentEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def navigatedWithinDocument(
        self,
        callback_or_session: str,
        handler: EventCallback[NavigatedWithinDocumentEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def navigatedWithinDocument(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[NavigatedWithinDocumentEvent]: ...

    def navigatedWithinDocument(
        self,
        callback_or_session: EventCallback[NavigatedWithinDocumentEvent]
        | str
        | None = None,
        handler: EventCallback[NavigatedWithinDocumentEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[NavigatedWithinDocumentEvent] | Unsubscribe:
        """Fired when same-document navigation happens, e.g. due to history API usage or anchor navigation."""

        return cast(
            Awaitable[NavigatedWithinDocumentEvent] | Unsubscribe,
            self._event(
                "navigatedWithinDocument",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def screencastFrame(
        self,
        callback_or_session: EventCallback[ScreencastFrameEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def screencastFrame(
        self,
        callback_or_session: str,
        handler: EventCallback[ScreencastFrameEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def screencastFrame(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[ScreencastFrameEvent]: ...

    def screencastFrame(
        self,
        callback_or_session: EventCallback[ScreencastFrameEvent] | str | None = None,
        handler: EventCallback[ScreencastFrameEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[ScreencastFrameEvent] | Unsubscribe:
        """Compressed image data requested by the `startScreencast`."""

        return cast(
            Awaitable[ScreencastFrameEvent] | Unsubscribe,
            self._event(
                "screencastFrame",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def screencastVisibilityChanged(
        self,
        callback_or_session: EventCallback[ScreencastVisibilityChangedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def screencastVisibilityChanged(
        self,
        callback_or_session: str,
        handler: EventCallback[ScreencastVisibilityChangedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def screencastVisibilityChanged(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[ScreencastVisibilityChangedEvent]: ...

    def screencastVisibilityChanged(
        self,
        callback_or_session: EventCallback[ScreencastVisibilityChangedEvent]
        | str
        | None = None,
        handler: EventCallback[ScreencastVisibilityChangedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[ScreencastVisibilityChangedEvent] | Unsubscribe:
        """Fired when the page with currently enabled screencast was shown or hidden `."""

        return cast(
            Awaitable[ScreencastVisibilityChangedEvent] | Unsubscribe,
            self._event(
                "screencastVisibilityChanged",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def windowOpen(
        self,
        callback_or_session: EventCallback[WindowOpenEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def windowOpen(
        self,
        callback_or_session: str,
        handler: EventCallback[WindowOpenEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def windowOpen(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[WindowOpenEvent]: ...

    def windowOpen(
        self,
        callback_or_session: EventCallback[WindowOpenEvent] | str | None = None,
        handler: EventCallback[WindowOpenEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[WindowOpenEvent] | Unsubscribe:
        """Fired when a new window is going to be opened, via window.open(), link click, form submission, etc."""

        return cast(
            Awaitable[WindowOpenEvent] | Unsubscribe,
            self._event(
                "windowOpen",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def compilationCacheProduced(
        self,
        callback_or_session: EventCallback[CompilationCacheProducedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def compilationCacheProduced(
        self,
        callback_or_session: str,
        handler: EventCallback[CompilationCacheProducedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def compilationCacheProduced(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[CompilationCacheProducedEvent]: ...

    def compilationCacheProduced(
        self,
        callback_or_session: EventCallback[CompilationCacheProducedEvent]
        | str
        | None = None,
        handler: EventCallback[CompilationCacheProducedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[CompilationCacheProducedEvent] | Unsubscribe:
        """Issued for every compilation cache generated. Is only available if Page.setGenerateCompilationCache is enabled."""

        return cast(
            Awaitable[CompilationCacheProducedEvent] | Unsubscribe,
            self._event(
                "compilationCacheProduced",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )


__all__ = [
    "AdFrameExplanation",
    "AdFrameStatus",
    "AdFrameType",
    "AdScriptId",
    "AddCompilationCacheParameters",
    "AddScriptToEvaluateOnLoadParameters",
    "AddScriptToEvaluateOnLoadResult",
    "AddScriptToEvaluateOnNewDocumentParameters",
    "AddScriptToEvaluateOnNewDocumentResult",
    "AppManifestError",
    "AppManifestParsedProperties",
    "AutoResponseMode",
    "BackForwardCacheNotRestoredExplanation",
    "BackForwardCacheNotRestoredExplanationTree",
    "BackForwardCacheNotRestoredReason",
    "BackForwardCacheNotRestoredReasonType",
    "BackForwardCacheNotUsedEvent",
    "CaptureScreenshotParameters",
    "CaptureScreenshotResult",
    "CaptureSnapshotParameters",
    "CaptureSnapshotResult",
    "ClientNavigationDisposition",
    "ClientNavigationReason",
    "CompilationCacheParams",
    "CompilationCacheProducedEvent",
    "CreateIsolatedWorldParameters",
    "CreateIsolatedWorldResult",
    "CrossOriginIsolatedContextType",
    "DeleteCookieParameters",
    "DialogType",
    "DocumentOpenedEvent",
    "DomContentEventFiredEvent",
    "DownloadProgressEvent",
    "DownloadWillBeginEvent",
    "FileChooserOpenedEvent",
    "FontFamilies",
    "FontSizes",
    "Frame",
    "FrameAttachedEvent",
    "FrameClearedScheduledNavigationEvent",
    "FrameDetachedEvent",
    "FrameId",
    "FrameNavigatedEvent",
    "FrameRequestedNavigationEvent",
    "FrameResource",
    "FrameResourceTree",
    "FrameScheduledNavigationEvent",
    "FrameStartedLoadingEvent",
    "FrameStoppedLoadingEvent",
    "FrameTree",
    "GatedAPIFeatures",
    "GenerateTestReportParameters",
    "GetAdScriptIdParameters",
    "GetAdScriptIdResult",
    "GetAppIdResult",
    "GetAppManifestResult",
    "GetCookiesResult",
    "GetFrameTreeResult",
    "GetInstallabilityErrorsResult",
    "GetLayoutMetricsResult",
    "GetManifestIconsResult",
    "GetNavigationHistoryResult",
    "GetOriginTrialsParameters",
    "GetOriginTrialsResult",
    "GetPermissionsPolicyStateParameters",
    "GetPermissionsPolicyStateResult",
    "GetResourceContentParameters",
    "GetResourceContentResult",
    "GetResourceTreeResult",
    "HandleJavaScriptDialogParameters",
    "InstallabilityError",
    "InstallabilityErrorArgument",
    "JavascriptDialogClosedEvent",
    "JavascriptDialogOpeningEvent",
    "LayoutViewport",
    "LifecycleEventEvent",
    "LoadEventFiredEvent",
    "NavigateParameters",
    "NavigateResult",
    "NavigateToHistoryEntryParameters",
    "NavigatedWithinDocumentEvent",
    "NavigationEntry",
    "NavigationType",
    "OriginTrial",
    "OriginTrialStatus",
    "OriginTrialToken",
    "OriginTrialTokenStatus",
    "OriginTrialTokenWithStatus",
    "OriginTrialUsageRestriction",
    "Page",
    "PermissionsPolicyBlockLocator",
    "PermissionsPolicyBlockReason",
    "PermissionsPolicyFeature",
    "PermissionsPolicyFeatureState",
    "PrintToPDFParameters",
    "PrintToPDFResult",
    "ProduceCompilationCacheParameters",
    "ReferrerPolicy",
    "ReloadParameters",
    "RemoveScriptToEvaluateOnLoadParameters",
    "RemoveScriptToEvaluateOnNewDocumentParameters",
    "ScreencastFrameAckParameters",
    "ScreencastFrameEvent",
    "ScreencastFrameMetadata",
    "ScreencastVisibilityChangedEvent",
    "ScriptFontFamilies",
    "ScriptIdentifier",
    "SearchInResourceParameters",
    "SearchInResourceResult",
    "SecureContextType",
    "SetAdBlockingEnabledParameters",
    "SetBypassCSPParameters",
    "SetDeviceMetricsOverrideParameters",
    "SetDeviceOrientationOverrideParameters",
    "SetDocumentContentParameters",
    "SetDownloadBehaviorParameters",
    "SetFontFamiliesParameters",
    "SetFontSizesParameters",
    "SetGeolocationOverrideParameters",
    "SetInterceptFileChooserDialogParameters",
    "SetLifecycleEventsEnabledParameters",
    "SetPrerenderingAllowedParameters",
    "SetRPHRegistrationModeParameters",
    "SetSPCTransactionModeParameters",
    "SetTouchEmulationEnabledParameters",
    "SetWebLifecycleStateParameters",
    "StartScreencastParameters",
    "TransitionType",
    "Viewport",
    "VisualViewport",
    "WindowOpenEvent",
]
