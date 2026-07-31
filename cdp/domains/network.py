"""Generated bindings for the CDP Network domain. Do not edit manually."""

from __future__ import annotations

from collections.abc import Awaitable, Mapping
from typing import TYPE_CHECKING, Literal, TypeAlias, cast, overload

from typing_extensions import NotRequired, TypedDict, Unpack

from cdp.domain import Domain as BaseDomain, EventCallback, Unsubscribe
from cdp.types import JsonObject

if TYPE_CHECKING:
    from . import debugger as Debugger
    from . import emulation as Emulation
    from . import io as IO
    from . import page as Page
    from . import runtime as Runtime
    from . import security as Security


ResourceType: TypeAlias = Literal[
    "Document",
    "Stylesheet",
    "Image",
    "Media",
    "Font",
    "Script",
    "TextTrack",
    "XHR",
    "Fetch",
    "Prefetch",
    "EventSource",
    "WebSocket",
    "Manifest",
    "SignedExchange",
    "Ping",
    "CSPViolationReport",
    "Preflight",
    "Other",
]

LoaderId: TypeAlias = str

RequestId: TypeAlias = str

InterceptionId: TypeAlias = str

ErrorReason: TypeAlias = Literal[
    "Failed",
    "Aborted",
    "TimedOut",
    "AccessDenied",
    "ConnectionClosed",
    "ConnectionReset",
    "ConnectionRefused",
    "ConnectionAborted",
    "ConnectionFailed",
    "NameNotResolved",
    "InternetDisconnected",
    "AddressUnreachable",
    "BlockedByClient",
    "BlockedByResponse",
]

TimeSinceEpoch: TypeAlias = float

MonotonicTime: TypeAlias = float

Headers: TypeAlias = JsonObject

ConnectionType: TypeAlias = Literal[
    "none",
    "cellular2g",
    "cellular3g",
    "cellular4g",
    "bluetooth",
    "ethernet",
    "wifi",
    "wimax",
    "other",
]

CookieSameSite: TypeAlias = Literal["Strict", "Lax", "None"]

CookiePriority: TypeAlias = Literal["Low", "Medium", "High"]

CookieSourceScheme: TypeAlias = Literal["Unset", "NonSecure", "Secure"]


class ResourceTiming(TypedDict):
    requestTime: float
    proxyStart: float
    proxyEnd: float
    dnsStart: float
    dnsEnd: float
    connectStart: float
    connectEnd: float
    sslStart: float
    sslEnd: float
    workerStart: float
    workerReady: float
    workerFetchStart: float
    workerRespondWithSettled: float
    sendStart: float
    sendEnd: float
    pushStart: float
    pushEnd: float
    receiveHeadersStart: float
    receiveHeadersEnd: float


ResourcePriority: TypeAlias = Literal["VeryLow", "Low", "Medium", "High", "VeryHigh"]


class PostDataEntry(TypedDict):
    bytes: NotRequired[str]


class Request(TypedDict):
    url: str
    urlFragment: NotRequired[str]
    method: str
    headers: Headers
    postData: NotRequired[str]
    hasPostData: NotRequired[bool]
    postDataEntries: NotRequired[list[PostDataEntry]]
    mixedContentType: NotRequired[Security.MixedContentType]
    initialPriority: ResourcePriority
    referrerPolicy: Literal[
        "unsafe-url",
        "no-referrer-when-downgrade",
        "no-referrer",
        "origin",
        "origin-when-cross-origin",
        "same-origin",
        "strict-origin",
        "strict-origin-when-cross-origin",
    ]
    isLinkPreload: NotRequired[bool]
    trustTokenParams: NotRequired[TrustTokenParams]
    isSameSite: NotRequired[bool]


class SignedCertificateTimestamp(TypedDict):
    status: str
    origin: str
    logDescription: str
    logId: str
    timestamp: float
    hashAlgorithm: str
    signatureAlgorithm: str
    signatureData: str


class SecurityDetails(TypedDict):
    protocol: str
    keyExchange: str
    keyExchangeGroup: NotRequired[str]
    cipher: str
    mac: NotRequired[str]
    certificateId: Security.CertificateId
    subjectName: str
    sanList: list[str]
    issuer: str
    validFrom: TimeSinceEpoch
    validTo: TimeSinceEpoch
    signedCertificateTimestampList: list[SignedCertificateTimestamp]
    certificateTransparencyCompliance: CertificateTransparencyCompliance
    serverSignatureAlgorithm: NotRequired[int]
    encryptedClientHello: bool


CertificateTransparencyCompliance: TypeAlias = Literal[
    "unknown", "not-compliant", "compliant"
]

BlockedReason: TypeAlias = Literal[
    "other",
    "csp",
    "mixed-content",
    "origin",
    "inspector",
    "subresource-filter",
    "content-type",
    "coep-frame-resource-needs-coep-header",
    "coop-sandboxed-iframe-cannot-navigate-to-coop-page",
    "corp-not-same-origin",
    "corp-not-same-origin-after-defaulted-to-same-origin-by-coep",
    "corp-not-same-site",
]

CorsError: TypeAlias = Literal[
    "DisallowedByMode",
    "InvalidResponse",
    "WildcardOriginNotAllowed",
    "MissingAllowOriginHeader",
    "MultipleAllowOriginValues",
    "InvalidAllowOriginValue",
    "AllowOriginMismatch",
    "InvalidAllowCredentials",
    "CorsDisabledScheme",
    "PreflightInvalidStatus",
    "PreflightDisallowedRedirect",
    "PreflightWildcardOriginNotAllowed",
    "PreflightMissingAllowOriginHeader",
    "PreflightMultipleAllowOriginValues",
    "PreflightInvalidAllowOriginValue",
    "PreflightAllowOriginMismatch",
    "PreflightInvalidAllowCredentials",
    "PreflightMissingAllowExternal",
    "PreflightInvalidAllowExternal",
    "PreflightMissingAllowPrivateNetwork",
    "PreflightInvalidAllowPrivateNetwork",
    "InvalidAllowMethodsPreflightResponse",
    "InvalidAllowHeadersPreflightResponse",
    "MethodDisallowedByPreflightResponse",
    "HeaderDisallowedByPreflightResponse",
    "RedirectContainsCredentials",
    "InsecurePrivateNetwork",
    "InvalidPrivateNetworkAccess",
    "UnexpectedPrivateNetworkAccess",
    "NoCorsRedirectModeNotFollow",
    "PreflightMissingPrivateNetworkAccessId",
    "PreflightMissingPrivateNetworkAccessName",
    "PrivateNetworkAccessPermissionUnavailable",
    "PrivateNetworkAccessPermissionDenied",
]


class CorsErrorStatus(TypedDict):
    corsError: CorsError
    failedParameter: str


ServiceWorkerResponseSource: TypeAlias = Literal[
    "cache-storage", "http-cache", "fallback-code", "network"
]


class TrustTokenParams(TypedDict):
    operation: TrustTokenOperationType
    refreshPolicy: Literal["UseCached", "Refresh"]
    issuers: NotRequired[list[str]]


TrustTokenOperationType: TypeAlias = Literal["Issuance", "Redemption", "Signing"]

AlternateProtocolUsage: TypeAlias = Literal[
    "alternativeJobWonWithoutRace",
    "alternativeJobWonRace",
    "mainJobWonRace",
    "mappingMissing",
    "broken",
    "dnsAlpnH3JobWonWithoutRace",
    "dnsAlpnH3JobWonRace",
    "unspecifiedReason",
]


class Response(TypedDict):
    url: str
    status: int
    statusText: str
    headers: Headers
    headersText: NotRequired[str]
    mimeType: str
    requestHeaders: NotRequired[Headers]
    requestHeadersText: NotRequired[str]
    connectionReused: bool
    connectionId: float
    remoteIPAddress: NotRequired[str]
    remotePort: NotRequired[int]
    fromDiskCache: NotRequired[bool]
    fromServiceWorker: NotRequired[bool]
    fromPrefetchCache: NotRequired[bool]
    encodedDataLength: float
    timing: NotRequired[ResourceTiming]
    serviceWorkerResponseSource: NotRequired[ServiceWorkerResponseSource]
    responseTime: NotRequired[TimeSinceEpoch]
    cacheStorageCacheName: NotRequired[str]
    protocol: NotRequired[str]
    alternateProtocolUsage: NotRequired[AlternateProtocolUsage]
    securityState: Security.SecurityState
    securityDetails: NotRequired[SecurityDetails]


class WebSocketRequest(TypedDict):
    headers: Headers


class WebSocketResponse(TypedDict):
    status: int
    statusText: str
    headers: Headers
    headersText: NotRequired[str]
    requestHeaders: NotRequired[Headers]
    requestHeadersText: NotRequired[str]


class WebSocketFrame(TypedDict):
    opcode: float
    mask: bool
    payloadData: str


class CachedResource(TypedDict):
    url: str
    type: ResourceType
    response: NotRequired[Response]
    bodySize: float


class Initiator(TypedDict):
    type: Literal["parser", "script", "preload", "SignedExchange", "preflight", "other"]
    stack: NotRequired[Runtime.StackTrace]
    url: NotRequired[str]
    lineNumber: NotRequired[float]
    columnNumber: NotRequired[float]
    requestId: NotRequired[RequestId]


class Cookie(TypedDict):
    name: str
    value: str
    domain: str
    path: str
    expires: float
    size: int
    httpOnly: bool
    secure: bool
    session: bool
    sameSite: NotRequired[CookieSameSite]
    priority: CookiePriority
    sameParty: bool
    sourceScheme: CookieSourceScheme
    sourcePort: int
    partitionKey: NotRequired[str]
    partitionKeyOpaque: NotRequired[bool]


SetCookieBlockedReason: TypeAlias = Literal[
    "SecureOnly",
    "SameSiteStrict",
    "SameSiteLax",
    "SameSiteUnspecifiedTreatedAsLax",
    "SameSiteNoneInsecure",
    "UserPreferences",
    "ThirdPartyBlockedInFirstPartySet",
    "SyntaxError",
    "SchemeNotSupported",
    "OverwriteSecure",
    "InvalidDomain",
    "InvalidPrefix",
    "UnknownError",
    "SchemefulSameSiteStrict",
    "SchemefulSameSiteLax",
    "SchemefulSameSiteUnspecifiedTreatedAsLax",
    "SamePartyFromCrossPartyContext",
    "SamePartyConflictsWithOtherAttributes",
    "NameValuePairExceedsMaxSize",
]

CookieBlockedReason: TypeAlias = Literal[
    "SecureOnly",
    "NotOnPath",
    "DomainMismatch",
    "SameSiteStrict",
    "SameSiteLax",
    "SameSiteUnspecifiedTreatedAsLax",
    "SameSiteNoneInsecure",
    "UserPreferences",
    "ThirdPartyBlockedInFirstPartySet",
    "UnknownError",
    "SchemefulSameSiteStrict",
    "SchemefulSameSiteLax",
    "SchemefulSameSiteUnspecifiedTreatedAsLax",
    "SamePartyFromCrossPartyContext",
    "NameValuePairExceedsMaxSize",
]


class BlockedSetCookieWithReason(TypedDict):
    blockedReasons: list[SetCookieBlockedReason]
    cookieLine: str
    cookie: NotRequired[Cookie]


class BlockedCookieWithReason(TypedDict):
    blockedReasons: list[CookieBlockedReason]
    cookie: Cookie


class CookieParam(TypedDict):
    name: str
    value: str
    url: NotRequired[str]
    domain: NotRequired[str]
    path: NotRequired[str]
    secure: NotRequired[bool]
    httpOnly: NotRequired[bool]
    sameSite: NotRequired[CookieSameSite]
    expires: NotRequired[TimeSinceEpoch]
    priority: NotRequired[CookiePriority]
    sameParty: NotRequired[bool]
    sourceScheme: NotRequired[CookieSourceScheme]
    sourcePort: NotRequired[int]
    partitionKey: NotRequired[str]


class AuthChallenge(TypedDict):
    source: NotRequired[Literal["Server", "Proxy"]]
    origin: str
    scheme: str
    realm: str


class AuthChallengeResponse(TypedDict):
    response: Literal["Default", "CancelAuth", "ProvideCredentials"]
    username: NotRequired[str]
    password: NotRequired[str]


InterceptionStage: TypeAlias = Literal["Request", "HeadersReceived"]


class RequestPattern(TypedDict):
    urlPattern: NotRequired[str]
    resourceType: NotRequired[ResourceType]
    interceptionStage: NotRequired[InterceptionStage]


class SignedExchangeSignature(TypedDict):
    label: str
    signature: str
    integrity: str
    certUrl: NotRequired[str]
    certSha256: NotRequired[str]
    validityUrl: str
    date: int
    expires: int
    certificates: NotRequired[list[str]]


class SignedExchangeHeader(TypedDict):
    requestUrl: str
    responseCode: int
    responseHeaders: Headers
    signatures: list[SignedExchangeSignature]
    headerIntegrity: str


SignedExchangeErrorField: TypeAlias = Literal[
    "signatureSig",
    "signatureIntegrity",
    "signatureCertUrl",
    "signatureCertSha256",
    "signatureValidityUrl",
    "signatureTimestamps",
]


class SignedExchangeError(TypedDict):
    message: str
    signatureIndex: NotRequired[int]
    errorField: NotRequired[SignedExchangeErrorField]


class SignedExchangeInfo(TypedDict):
    outerResponse: Response
    header: NotRequired[SignedExchangeHeader]
    securityDetails: NotRequired[SecurityDetails]
    errors: NotRequired[list[SignedExchangeError]]


ContentEncoding: TypeAlias = Literal["deflate", "gzip", "br", "zstd"]

PrivateNetworkRequestPolicy: TypeAlias = Literal[
    "Allow",
    "BlockFromInsecureToMorePrivate",
    "WarnFromInsecureToMorePrivate",
    "PreflightBlock",
    "PreflightWarn",
]

IPAddressSpace: TypeAlias = Literal["Local", "Private", "Public", "Unknown"]


class ConnectTiming(TypedDict):
    requestTime: float


class ClientSecurityState(TypedDict):
    initiatorIsSecureContext: bool
    initiatorIPAddressSpace: IPAddressSpace
    privateNetworkRequestPolicy: PrivateNetworkRequestPolicy


CrossOriginOpenerPolicyValue: TypeAlias = Literal[
    "SameOrigin",
    "SameOriginAllowPopups",
    "RestrictProperties",
    "UnsafeNone",
    "SameOriginPlusCoep",
    "RestrictPropertiesPlusCoep",
]


class CrossOriginOpenerPolicyStatus(TypedDict):
    value: CrossOriginOpenerPolicyValue
    reportOnlyValue: CrossOriginOpenerPolicyValue
    reportingEndpoint: NotRequired[str]
    reportOnlyReportingEndpoint: NotRequired[str]


CrossOriginEmbedderPolicyValue: TypeAlias = Literal[
    "None", "Credentialless", "RequireCorp"
]


class CrossOriginEmbedderPolicyStatus(TypedDict):
    value: CrossOriginEmbedderPolicyValue
    reportOnlyValue: CrossOriginEmbedderPolicyValue
    reportingEndpoint: NotRequired[str]
    reportOnlyReportingEndpoint: NotRequired[str]


ContentSecurityPolicySource: TypeAlias = Literal["HTTP", "Meta"]


class ContentSecurityPolicyStatus(TypedDict):
    effectiveDirectives: str
    isEnforced: bool
    source: ContentSecurityPolicySource


class SecurityIsolationStatus(TypedDict):
    coop: NotRequired[CrossOriginOpenerPolicyStatus]
    coep: NotRequired[CrossOriginEmbedderPolicyStatus]
    csp: NotRequired[list[ContentSecurityPolicyStatus]]


ReportStatus: TypeAlias = Literal["Queued", "Pending", "MarkedForRemoval", "Success"]

ReportId: TypeAlias = str


class ReportingApiReport(TypedDict):
    id: ReportId
    initiatorUrl: str
    destination: str
    type: str
    timestamp: TimeSinceEpoch
    depth: int
    completedAttempts: int
    body: JsonObject
    status: ReportStatus


class ReportingApiEndpoint(TypedDict):
    url: str
    groupName: str


class LoadNetworkResourcePageResult(TypedDict):
    success: bool
    netError: NotRequired[float]
    netErrorName: NotRequired[str]
    httpStatusCode: NotRequired[float]
    stream: NotRequired[IO.StreamHandle]
    headers: NotRequired[Headers]


class LoadNetworkResourceOptions(TypedDict):
    disableCache: bool
    includeCredentials: bool


class SetAcceptedEncodingsParameters(TypedDict):
    encodings: list[ContentEncoding]


class CanClearBrowserCacheResult(TypedDict):
    result: bool


class CanClearBrowserCookiesResult(TypedDict):
    result: bool


class CanEmulateNetworkConditionsResult(TypedDict):
    result: bool


class ContinueInterceptedRequestParameters(TypedDict):
    interceptionId: InterceptionId
    errorReason: NotRequired[ErrorReason]
    rawResponse: NotRequired[str]
    url: NotRequired[str]
    method: NotRequired[str]
    postData: NotRequired[str]
    headers: NotRequired[Headers]
    authChallengeResponse: NotRequired[AuthChallengeResponse]


class DeleteCookiesParameters(TypedDict):
    name: str
    url: NotRequired[str]
    domain: NotRequired[str]
    path: NotRequired[str]


class EmulateNetworkConditionsParameters(TypedDict):
    offline: bool
    latency: float
    downloadThroughput: float
    uploadThroughput: float
    connectionType: NotRequired[ConnectionType]


class EnableParameters(TypedDict):
    maxTotalBufferSize: NotRequired[int]
    maxResourceBufferSize: NotRequired[int]
    maxPostDataSize: NotRequired[int]


class GetAllCookiesResult(TypedDict):
    cookies: list[Cookie]


class GetCertificateParameters(TypedDict):
    origin: str


class GetCertificateResult(TypedDict):
    tableNames: list[str]


class GetCookiesParameters(TypedDict):
    urls: NotRequired[list[str]]


class GetCookiesResult(TypedDict):
    cookies: list[Cookie]


class GetResponseBodyParameters(TypedDict):
    requestId: RequestId


class GetResponseBodyResult(TypedDict):
    body: str
    base64Encoded: bool


class GetRequestPostDataParameters(TypedDict):
    requestId: RequestId


class GetRequestPostDataResult(TypedDict):
    postData: str


class GetResponseBodyForInterceptionParameters(TypedDict):
    interceptionId: InterceptionId


class GetResponseBodyForInterceptionResult(TypedDict):
    body: str
    base64Encoded: bool


class TakeResponseBodyForInterceptionAsStreamParameters(TypedDict):
    interceptionId: InterceptionId


class TakeResponseBodyForInterceptionAsStreamResult(TypedDict):
    stream: IO.StreamHandle


class ReplayXHRParameters(TypedDict):
    requestId: RequestId


class SearchInResponseBodyParameters(TypedDict):
    requestId: RequestId
    query: str
    caseSensitive: NotRequired[bool]
    isRegex: NotRequired[bool]


class SearchInResponseBodyResult(TypedDict):
    result: list[Debugger.SearchMatch]


class SetBlockedURLsParameters(TypedDict):
    urls: list[str]


class SetBypassServiceWorkerParameters(TypedDict):
    bypass: bool


class SetCacheDisabledParameters(TypedDict):
    cacheDisabled: bool


class SetCookieParameters(TypedDict):
    name: str
    value: str
    url: NotRequired[str]
    domain: NotRequired[str]
    path: NotRequired[str]
    secure: NotRequired[bool]
    httpOnly: NotRequired[bool]
    sameSite: NotRequired[CookieSameSite]
    expires: NotRequired[TimeSinceEpoch]
    priority: NotRequired[CookiePriority]
    sameParty: NotRequired[bool]
    sourceScheme: NotRequired[CookieSourceScheme]
    sourcePort: NotRequired[int]
    partitionKey: NotRequired[str]


class SetCookieResult(TypedDict):
    success: bool


class SetCookiesParameters(TypedDict):
    cookies: list[CookieParam]


class SetExtraHTTPHeadersParameters(TypedDict):
    headers: Headers


class SetAttachDebugStackParameters(TypedDict):
    enabled: bool


class SetRequestInterceptionParameters(TypedDict):
    patterns: list[RequestPattern]


class SetUserAgentOverrideParameters(TypedDict):
    userAgent: str
    acceptLanguage: NotRequired[str]
    platform: NotRequired[str]
    userAgentMetadata: NotRequired[Emulation.UserAgentMetadata]


class GetSecurityIsolationStatusParameters(TypedDict):
    frameId: NotRequired[Page.FrameId]


class GetSecurityIsolationStatusResult(TypedDict):
    status: SecurityIsolationStatus


class EnableReportingApiParameters(TypedDict):
    enable: bool


class LoadNetworkResourceParameters(TypedDict):
    frameId: NotRequired[Page.FrameId]
    url: str
    options: LoadNetworkResourceOptions


class LoadNetworkResourceResult(TypedDict):
    resource: LoadNetworkResourcePageResult


class DataReceivedEvent(TypedDict):
    requestId: RequestId
    timestamp: MonotonicTime
    dataLength: int
    encodedDataLength: int


class EventSourceMessageReceivedEvent(TypedDict):
    requestId: RequestId
    timestamp: MonotonicTime
    eventName: str
    eventId: str
    data: str


class LoadingFailedEvent(TypedDict):
    requestId: RequestId
    timestamp: MonotonicTime
    type: ResourceType
    errorText: str
    canceled: NotRequired[bool]
    blockedReason: NotRequired[BlockedReason]
    corsErrorStatus: NotRequired[CorsErrorStatus]


class LoadingFinishedEvent(TypedDict):
    requestId: RequestId
    timestamp: MonotonicTime
    encodedDataLength: float


class RequestInterceptedEvent(TypedDict):
    interceptionId: InterceptionId
    request: Request
    frameId: Page.FrameId
    resourceType: ResourceType
    isNavigationRequest: bool
    isDownload: NotRequired[bool]
    redirectUrl: NotRequired[str]
    authChallenge: NotRequired[AuthChallenge]
    responseErrorReason: NotRequired[ErrorReason]
    responseStatusCode: NotRequired[int]
    responseHeaders: NotRequired[Headers]
    requestId: NotRequired[RequestId]


class RequestServedFromCacheEvent(TypedDict):
    requestId: RequestId


class RequestWillBeSentEvent(TypedDict):
    requestId: RequestId
    loaderId: LoaderId
    documentURL: str
    request: Request
    timestamp: MonotonicTime
    wallTime: TimeSinceEpoch
    initiator: Initiator
    redirectHasExtraInfo: bool
    redirectResponse: NotRequired[Response]
    type: NotRequired[ResourceType]
    frameId: NotRequired[Page.FrameId]
    hasUserGesture: NotRequired[bool]


class ResourceChangedPriorityEvent(TypedDict):
    requestId: RequestId
    newPriority: ResourcePriority
    timestamp: MonotonicTime


class SignedExchangeReceivedEvent(TypedDict):
    requestId: RequestId
    info: SignedExchangeInfo


class ResponseReceivedEvent(TypedDict):
    requestId: RequestId
    loaderId: LoaderId
    timestamp: MonotonicTime
    type: ResourceType
    response: Response
    hasExtraInfo: bool
    frameId: NotRequired[Page.FrameId]


class WebSocketClosedEvent(TypedDict):
    requestId: RequestId
    timestamp: MonotonicTime


class WebSocketCreatedEvent(TypedDict):
    requestId: RequestId
    url: str
    initiator: NotRequired[Initiator]


class WebSocketFrameErrorEvent(TypedDict):
    requestId: RequestId
    timestamp: MonotonicTime
    errorMessage: str


class WebSocketFrameReceivedEvent(TypedDict):
    requestId: RequestId
    timestamp: MonotonicTime
    response: WebSocketFrame


class WebSocketFrameSentEvent(TypedDict):
    requestId: RequestId
    timestamp: MonotonicTime
    response: WebSocketFrame


class WebSocketHandshakeResponseReceivedEvent(TypedDict):
    requestId: RequestId
    timestamp: MonotonicTime
    response: WebSocketResponse


class WebSocketWillSendHandshakeRequestEvent(TypedDict):
    requestId: RequestId
    timestamp: MonotonicTime
    wallTime: TimeSinceEpoch
    request: WebSocketRequest


class WebTransportCreatedEvent(TypedDict):
    transportId: RequestId
    url: str
    timestamp: MonotonicTime
    initiator: NotRequired[Initiator]


class WebTransportConnectionEstablishedEvent(TypedDict):
    transportId: RequestId
    timestamp: MonotonicTime


class WebTransportClosedEvent(TypedDict):
    transportId: RequestId
    timestamp: MonotonicTime


class RequestWillBeSentExtraInfoEvent(TypedDict):
    requestId: RequestId
    associatedCookies: list[BlockedCookieWithReason]
    headers: Headers
    connectTiming: ConnectTiming
    clientSecurityState: NotRequired[ClientSecurityState]
    siteHasCookieInOtherPartition: NotRequired[bool]


class ResponseReceivedExtraInfoEvent(TypedDict):
    requestId: RequestId
    blockedCookies: list[BlockedSetCookieWithReason]
    headers: Headers
    resourceIPAddressSpace: IPAddressSpace
    statusCode: int
    headersText: NotRequired[str]
    cookiePartitionKey: NotRequired[str]
    cookiePartitionKeyOpaque: NotRequired[bool]


class TrustTokenOperationDoneEvent(TypedDict):
    status: Literal[
        "Ok",
        "InvalidArgument",
        "MissingIssuerKeys",
        "FailedPrecondition",
        "ResourceExhausted",
        "AlreadyExists",
        "Unavailable",
        "Unauthorized",
        "BadResponse",
        "InternalError",
        "UnknownError",
        "FulfilledLocally",
    ]
    type: TrustTokenOperationType
    requestId: RequestId
    topLevelOrigin: NotRequired[str]
    issuerOrigin: NotRequired[str]
    issuedTokenCount: NotRequired[int]


class SubresourceWebBundleMetadataReceivedEvent(TypedDict):
    requestId: RequestId
    urls: list[str]


class SubresourceWebBundleMetadataErrorEvent(TypedDict):
    requestId: RequestId
    errorMessage: str


class SubresourceWebBundleInnerResponseParsedEvent(TypedDict):
    innerRequestId: RequestId
    innerRequestURL: str
    bundleRequestId: NotRequired[RequestId]


class SubresourceWebBundleInnerResponseErrorEvent(TypedDict):
    innerRequestId: RequestId
    innerRequestURL: str
    errorMessage: str
    bundleRequestId: NotRequired[RequestId]


class ReportingApiReportAddedEvent(TypedDict):
    report: ReportingApiReport


class ReportingApiReportUpdatedEvent(TypedDict):
    report: ReportingApiReport


class ReportingApiEndpointsChangedForOriginEvent(TypedDict):
    origin: str
    endpoints: list[ReportingApiEndpoint]


class Network(BaseDomain):
    """Network domain allows tracking network activities of the page. It exposes information about http, file, data and other requests and responses, their headers, bodies, timing, etc."""

    domain_name = "Network"

    @overload
    async def setAcceptedEncodings(
        self,
        params: SetAcceptedEncodingsParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def setAcceptedEncodings(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetAcceptedEncodingsParameters],
    ) -> JsonObject: ...

    async def setAcceptedEncodings(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Sets a list of content encodings that will be accepted. Empty list means no encoding is accepted."""

        return await self._command("setAcceptedEncodings", params, session_id, kwargs)

    async def clearAcceptedEncodingsOverride(
        self,
        session_id: str | None = None,
    ) -> JsonObject:
        """Clears accepted encodings set by setAcceptedEncodings"""

        return await self._command(
            "clearAcceptedEncodingsOverride", None, session_id, {}
        )

    async def canClearBrowserCache(
        self,
        session_id: str | None = None,
    ) -> CanClearBrowserCacheResult:
        """Tells whether clearing browser cache is supported."""

        return cast(
            CanClearBrowserCacheResult,
            await self._command("canClearBrowserCache", None, session_id, {}),
        )

    async def canClearBrowserCookies(
        self,
        session_id: str | None = None,
    ) -> CanClearBrowserCookiesResult:
        """Tells whether clearing browser cookies is supported."""

        return cast(
            CanClearBrowserCookiesResult,
            await self._command("canClearBrowserCookies", None, session_id, {}),
        )

    async def canEmulateNetworkConditions(
        self,
        session_id: str | None = None,
    ) -> CanEmulateNetworkConditionsResult:
        """Tells whether emulation of network conditions is supported."""

        return cast(
            CanEmulateNetworkConditionsResult,
            await self._command("canEmulateNetworkConditions", None, session_id, {}),
        )

    async def clearBrowserCache(
        self,
        session_id: str | None = None,
    ) -> JsonObject:
        """Clears browser cache."""

        return await self._command("clearBrowserCache", None, session_id, {})

    async def clearBrowserCookies(
        self,
        session_id: str | None = None,
    ) -> JsonObject:
        """Clears browser cookies."""

        return await self._command("clearBrowserCookies", None, session_id, {})

    @overload
    async def continueInterceptedRequest(
        self,
        params: ContinueInterceptedRequestParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def continueInterceptedRequest(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[ContinueInterceptedRequestParameters],
    ) -> JsonObject: ...

    async def continueInterceptedRequest(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Response to Network.requestIntercepted which either modifies the request to continue with any modifications, or blocks it, or completes it with the provided response bytes. If a network fetch occurs as a result which encounters a redirect an additional Network.requestIntercepted event will be sent with the same InterceptionId. Deprecated, use Fetch.continueRequest, Fetch.fulfillRequest and Fetch.failRequest instead."""

        return await self._command(
            "continueInterceptedRequest", params, session_id, kwargs
        )

    @overload
    async def deleteCookies(
        self,
        params: DeleteCookiesParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def deleteCookies(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[DeleteCookiesParameters],
    ) -> JsonObject: ...

    async def deleteCookies(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Deletes browser cookies with matching name and url or domain/path pair."""

        return await self._command("deleteCookies", params, session_id, kwargs)

    async def disable(
        self,
        session_id: str | None = None,
    ) -> JsonObject:
        """Disables network tracking, prevents network events from being sent to the client."""

        return await self._command("disable", None, session_id, {})

    @overload
    async def emulateNetworkConditions(
        self,
        params: EmulateNetworkConditionsParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def emulateNetworkConditions(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[EmulateNetworkConditionsParameters],
    ) -> JsonObject: ...

    async def emulateNetworkConditions(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Activates emulation of network conditions."""

        return await self._command(
            "emulateNetworkConditions", params, session_id, kwargs
        )

    @overload
    async def enable(
        self,
        params: EnableParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def enable(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[EnableParameters],
    ) -> JsonObject: ...

    async def enable(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Enables network tracking, network events will now be delivered to the client."""

        return await self._command("enable", params, session_id, kwargs)

    async def getAllCookies(
        self,
        session_id: str | None = None,
    ) -> GetAllCookiesResult:
        """Returns all browser cookies. Depending on the backend support, will return detailed cookie information in the `cookies` field. Deprecated. Use Storage.getCookies instead."""

        return cast(
            GetAllCookiesResult,
            await self._command("getAllCookies", None, session_id, {}),
        )

    @overload
    async def getCertificate(
        self,
        params: GetCertificateParameters,
        session_id: str | None = None,
    ) -> GetCertificateResult: ...

    @overload
    async def getCertificate(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[GetCertificateParameters],
    ) -> GetCertificateResult: ...

    async def getCertificate(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> GetCertificateResult:
        """Returns the DER-encoded certificate."""

        return cast(
            GetCertificateResult,
            await self._command("getCertificate", params, session_id, kwargs),
        )

    @overload
    async def getCookies(
        self,
        params: GetCookiesParameters,
        session_id: str | None = None,
    ) -> GetCookiesResult: ...

    @overload
    async def getCookies(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[GetCookiesParameters],
    ) -> GetCookiesResult: ...

    async def getCookies(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> GetCookiesResult:
        """Returns all browser cookies for the current URL. Depending on the backend support, will return detailed cookie information in the `cookies` field."""

        return cast(
            GetCookiesResult,
            await self._command("getCookies", params, session_id, kwargs),
        )

    @overload
    async def getResponseBody(
        self,
        params: GetResponseBodyParameters,
        session_id: str | None = None,
    ) -> GetResponseBodyResult: ...

    @overload
    async def getResponseBody(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[GetResponseBodyParameters],
    ) -> GetResponseBodyResult: ...

    async def getResponseBody(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> GetResponseBodyResult:
        """Returns content served for the given request."""

        return cast(
            GetResponseBodyResult,
            await self._command("getResponseBody", params, session_id, kwargs),
        )

    @overload
    async def getRequestPostData(
        self,
        params: GetRequestPostDataParameters,
        session_id: str | None = None,
    ) -> GetRequestPostDataResult: ...

    @overload
    async def getRequestPostData(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[GetRequestPostDataParameters],
    ) -> GetRequestPostDataResult: ...

    async def getRequestPostData(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> GetRequestPostDataResult:
        """Returns post data sent with the request. Returns an error when no data was sent with the request."""

        return cast(
            GetRequestPostDataResult,
            await self._command("getRequestPostData", params, session_id, kwargs),
        )

    @overload
    async def getResponseBodyForInterception(
        self,
        params: GetResponseBodyForInterceptionParameters,
        session_id: str | None = None,
    ) -> GetResponseBodyForInterceptionResult: ...

    @overload
    async def getResponseBodyForInterception(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[GetResponseBodyForInterceptionParameters],
    ) -> GetResponseBodyForInterceptionResult: ...

    async def getResponseBodyForInterception(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> GetResponseBodyForInterceptionResult:
        """Returns content served for the given currently intercepted request."""

        return cast(
            GetResponseBodyForInterceptionResult,
            await self._command(
                "getResponseBodyForInterception", params, session_id, kwargs
            ),
        )

    @overload
    async def takeResponseBodyForInterceptionAsStream(
        self,
        params: TakeResponseBodyForInterceptionAsStreamParameters,
        session_id: str | None = None,
    ) -> TakeResponseBodyForInterceptionAsStreamResult: ...

    @overload
    async def takeResponseBodyForInterceptionAsStream(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[TakeResponseBodyForInterceptionAsStreamParameters],
    ) -> TakeResponseBodyForInterceptionAsStreamResult: ...

    async def takeResponseBodyForInterceptionAsStream(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> TakeResponseBodyForInterceptionAsStreamResult:
        """Returns a handle to the stream representing the response body. Note that after this command, the intercepted request can't be continued as is -- you either need to cancel it or to provide the response body. The stream only supports sequential read, IO.read will fail if the position is specified."""

        return cast(
            TakeResponseBodyForInterceptionAsStreamResult,
            await self._command(
                "takeResponseBodyForInterceptionAsStream", params, session_id, kwargs
            ),
        )

    @overload
    async def replayXHR(
        self,
        params: ReplayXHRParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def replayXHR(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[ReplayXHRParameters],
    ) -> JsonObject: ...

    async def replayXHR(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """This method sends a new XMLHttpRequest which is identical to the original one. The following parameters should be identical: method, url, async, request body, extra headers, withCredentials attribute, user, password."""

        return await self._command("replayXHR", params, session_id, kwargs)

    @overload
    async def searchInResponseBody(
        self,
        params: SearchInResponseBodyParameters,
        session_id: str | None = None,
    ) -> SearchInResponseBodyResult: ...

    @overload
    async def searchInResponseBody(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SearchInResponseBodyParameters],
    ) -> SearchInResponseBodyResult: ...

    async def searchInResponseBody(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> SearchInResponseBodyResult:
        """Searches for given string in response content."""

        return cast(
            SearchInResponseBodyResult,
            await self._command("searchInResponseBody", params, session_id, kwargs),
        )

    @overload
    async def setBlockedURLs(
        self,
        params: SetBlockedURLsParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def setBlockedURLs(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetBlockedURLsParameters],
    ) -> JsonObject: ...

    async def setBlockedURLs(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Blocks URLs from loading."""

        return await self._command("setBlockedURLs", params, session_id, kwargs)

    @overload
    async def setBypassServiceWorker(
        self,
        params: SetBypassServiceWorkerParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def setBypassServiceWorker(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetBypassServiceWorkerParameters],
    ) -> JsonObject: ...

    async def setBypassServiceWorker(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Toggles ignoring of service worker for each request."""

        return await self._command("setBypassServiceWorker", params, session_id, kwargs)

    @overload
    async def setCacheDisabled(
        self,
        params: SetCacheDisabledParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def setCacheDisabled(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetCacheDisabledParameters],
    ) -> JsonObject: ...

    async def setCacheDisabled(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Toggles ignoring cache for each request. If `true`, cache will not be used."""

        return await self._command("setCacheDisabled", params, session_id, kwargs)

    @overload
    async def setCookie(
        self,
        params: SetCookieParameters,
        session_id: str | None = None,
    ) -> SetCookieResult: ...

    @overload
    async def setCookie(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetCookieParameters],
    ) -> SetCookieResult: ...

    async def setCookie(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> SetCookieResult:
        """Sets a cookie with the given cookie data; may overwrite equivalent cookies if they exist."""

        return cast(
            SetCookieResult,
            await self._command("setCookie", params, session_id, kwargs),
        )

    @overload
    async def setCookies(
        self,
        params: SetCookiesParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def setCookies(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetCookiesParameters],
    ) -> JsonObject: ...

    async def setCookies(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Sets given cookies."""

        return await self._command("setCookies", params, session_id, kwargs)

    @overload
    async def setExtraHTTPHeaders(
        self,
        params: SetExtraHTTPHeadersParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def setExtraHTTPHeaders(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetExtraHTTPHeadersParameters],
    ) -> JsonObject: ...

    async def setExtraHTTPHeaders(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Specifies whether to always send extra HTTP headers with the requests from this page."""

        return await self._command("setExtraHTTPHeaders", params, session_id, kwargs)

    @overload
    async def setAttachDebugStack(
        self,
        params: SetAttachDebugStackParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def setAttachDebugStack(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetAttachDebugStackParameters],
    ) -> JsonObject: ...

    async def setAttachDebugStack(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Specifies whether to attach a page script stack id in requests"""

        return await self._command("setAttachDebugStack", params, session_id, kwargs)

    @overload
    async def setRequestInterception(
        self,
        params: SetRequestInterceptionParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def setRequestInterception(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetRequestInterceptionParameters],
    ) -> JsonObject: ...

    async def setRequestInterception(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Sets the requests to intercept that match the provided patterns and optionally resource types. Deprecated, please use Fetch.enable instead."""

        return await self._command("setRequestInterception", params, session_id, kwargs)

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
    async def getSecurityIsolationStatus(
        self,
        params: GetSecurityIsolationStatusParameters,
        session_id: str | None = None,
    ) -> GetSecurityIsolationStatusResult: ...

    @overload
    async def getSecurityIsolationStatus(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[GetSecurityIsolationStatusParameters],
    ) -> GetSecurityIsolationStatusResult: ...

    async def getSecurityIsolationStatus(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> GetSecurityIsolationStatusResult:
        """Returns information about the COEP/COOP isolation status."""

        return cast(
            GetSecurityIsolationStatusResult,
            await self._command(
                "getSecurityIsolationStatus", params, session_id, kwargs
            ),
        )

    @overload
    async def enableReportingApi(
        self,
        params: EnableReportingApiParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def enableReportingApi(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[EnableReportingApiParameters],
    ) -> JsonObject: ...

    async def enableReportingApi(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Enables tracking for the Reporting API, events generated by the Reporting API will now be delivered to the client. Enabling triggers 'reportingApiReportAdded' for all existing reports."""

        return await self._command("enableReportingApi", params, session_id, kwargs)

    @overload
    async def loadNetworkResource(
        self,
        params: LoadNetworkResourceParameters,
        session_id: str | None = None,
    ) -> LoadNetworkResourceResult: ...

    @overload
    async def loadNetworkResource(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[LoadNetworkResourceParameters],
    ) -> LoadNetworkResourceResult: ...

    async def loadNetworkResource(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> LoadNetworkResourceResult:
        """Fetches the resource and returns the content."""

        return cast(
            LoadNetworkResourceResult,
            await self._command("loadNetworkResource", params, session_id, kwargs),
        )

    @overload
    def dataReceived(
        self,
        callback_or_session: EventCallback[DataReceivedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def dataReceived(
        self,
        callback_or_session: str,
        handler: EventCallback[DataReceivedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def dataReceived(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[DataReceivedEvent]: ...

    def dataReceived(
        self,
        callback_or_session: EventCallback[DataReceivedEvent] | str | None = None,
        handler: EventCallback[DataReceivedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[DataReceivedEvent] | Unsubscribe:
        """Fired when data chunk was received over the network."""

        return cast(
            Awaitable[DataReceivedEvent] | Unsubscribe,
            self._event(
                "dataReceived",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def eventSourceMessageReceived(
        self,
        callback_or_session: EventCallback[EventSourceMessageReceivedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def eventSourceMessageReceived(
        self,
        callback_or_session: str,
        handler: EventCallback[EventSourceMessageReceivedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def eventSourceMessageReceived(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[EventSourceMessageReceivedEvent]: ...

    def eventSourceMessageReceived(
        self,
        callback_or_session: EventCallback[EventSourceMessageReceivedEvent]
        | str
        | None = None,
        handler: EventCallback[EventSourceMessageReceivedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[EventSourceMessageReceivedEvent] | Unsubscribe:
        """Fired when EventSource message is received."""

        return cast(
            Awaitable[EventSourceMessageReceivedEvent] | Unsubscribe,
            self._event(
                "eventSourceMessageReceived",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def loadingFailed(
        self,
        callback_or_session: EventCallback[LoadingFailedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def loadingFailed(
        self,
        callback_or_session: str,
        handler: EventCallback[LoadingFailedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def loadingFailed(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[LoadingFailedEvent]: ...

    def loadingFailed(
        self,
        callback_or_session: EventCallback[LoadingFailedEvent] | str | None = None,
        handler: EventCallback[LoadingFailedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[LoadingFailedEvent] | Unsubscribe:
        """Fired when HTTP request has failed to load."""

        return cast(
            Awaitable[LoadingFailedEvent] | Unsubscribe,
            self._event(
                "loadingFailed",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def loadingFinished(
        self,
        callback_or_session: EventCallback[LoadingFinishedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def loadingFinished(
        self,
        callback_or_session: str,
        handler: EventCallback[LoadingFinishedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def loadingFinished(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[LoadingFinishedEvent]: ...

    def loadingFinished(
        self,
        callback_or_session: EventCallback[LoadingFinishedEvent] | str | None = None,
        handler: EventCallback[LoadingFinishedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[LoadingFinishedEvent] | Unsubscribe:
        """Fired when HTTP request has finished loading."""

        return cast(
            Awaitable[LoadingFinishedEvent] | Unsubscribe,
            self._event(
                "loadingFinished",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def requestIntercepted(
        self,
        callback_or_session: EventCallback[RequestInterceptedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def requestIntercepted(
        self,
        callback_or_session: str,
        handler: EventCallback[RequestInterceptedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def requestIntercepted(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[RequestInterceptedEvent]: ...

    def requestIntercepted(
        self,
        callback_or_session: EventCallback[RequestInterceptedEvent] | str | None = None,
        handler: EventCallback[RequestInterceptedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[RequestInterceptedEvent] | Unsubscribe:
        """Details of an intercepted HTTP request, which must be either allowed, blocked, modified or mocked. Deprecated, use Fetch.requestPaused instead."""

        return cast(
            Awaitable[RequestInterceptedEvent] | Unsubscribe,
            self._event(
                "requestIntercepted",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def requestServedFromCache(
        self,
        callback_or_session: EventCallback[RequestServedFromCacheEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def requestServedFromCache(
        self,
        callback_or_session: str,
        handler: EventCallback[RequestServedFromCacheEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def requestServedFromCache(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[RequestServedFromCacheEvent]: ...

    def requestServedFromCache(
        self,
        callback_or_session: EventCallback[RequestServedFromCacheEvent]
        | str
        | None = None,
        handler: EventCallback[RequestServedFromCacheEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[RequestServedFromCacheEvent] | Unsubscribe:
        """Fired if request ended up loading from cache."""

        return cast(
            Awaitable[RequestServedFromCacheEvent] | Unsubscribe,
            self._event(
                "requestServedFromCache",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def requestWillBeSent(
        self,
        callback_or_session: EventCallback[RequestWillBeSentEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def requestWillBeSent(
        self,
        callback_or_session: str,
        handler: EventCallback[RequestWillBeSentEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def requestWillBeSent(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[RequestWillBeSentEvent]: ...

    def requestWillBeSent(
        self,
        callback_or_session: EventCallback[RequestWillBeSentEvent] | str | None = None,
        handler: EventCallback[RequestWillBeSentEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[RequestWillBeSentEvent] | Unsubscribe:
        """Fired when page is about to send HTTP request."""

        return cast(
            Awaitable[RequestWillBeSentEvent] | Unsubscribe,
            self._event(
                "requestWillBeSent",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def resourceChangedPriority(
        self,
        callback_or_session: EventCallback[ResourceChangedPriorityEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def resourceChangedPriority(
        self,
        callback_or_session: str,
        handler: EventCallback[ResourceChangedPriorityEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def resourceChangedPriority(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[ResourceChangedPriorityEvent]: ...

    def resourceChangedPriority(
        self,
        callback_or_session: EventCallback[ResourceChangedPriorityEvent]
        | str
        | None = None,
        handler: EventCallback[ResourceChangedPriorityEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[ResourceChangedPriorityEvent] | Unsubscribe:
        """Fired when resource loading priority is changed"""

        return cast(
            Awaitable[ResourceChangedPriorityEvent] | Unsubscribe,
            self._event(
                "resourceChangedPriority",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def signedExchangeReceived(
        self,
        callback_or_session: EventCallback[SignedExchangeReceivedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def signedExchangeReceived(
        self,
        callback_or_session: str,
        handler: EventCallback[SignedExchangeReceivedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def signedExchangeReceived(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[SignedExchangeReceivedEvent]: ...

    def signedExchangeReceived(
        self,
        callback_or_session: EventCallback[SignedExchangeReceivedEvent]
        | str
        | None = None,
        handler: EventCallback[SignedExchangeReceivedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[SignedExchangeReceivedEvent] | Unsubscribe:
        """Fired when a signed exchange was received over the network"""

        return cast(
            Awaitable[SignedExchangeReceivedEvent] | Unsubscribe,
            self._event(
                "signedExchangeReceived",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def responseReceived(
        self,
        callback_or_session: EventCallback[ResponseReceivedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def responseReceived(
        self,
        callback_or_session: str,
        handler: EventCallback[ResponseReceivedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def responseReceived(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[ResponseReceivedEvent]: ...

    def responseReceived(
        self,
        callback_or_session: EventCallback[ResponseReceivedEvent] | str | None = None,
        handler: EventCallback[ResponseReceivedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[ResponseReceivedEvent] | Unsubscribe:
        """Fired when HTTP response is available."""

        return cast(
            Awaitable[ResponseReceivedEvent] | Unsubscribe,
            self._event(
                "responseReceived",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def webSocketClosed(
        self,
        callback_or_session: EventCallback[WebSocketClosedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def webSocketClosed(
        self,
        callback_or_session: str,
        handler: EventCallback[WebSocketClosedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def webSocketClosed(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[WebSocketClosedEvent]: ...

    def webSocketClosed(
        self,
        callback_or_session: EventCallback[WebSocketClosedEvent] | str | None = None,
        handler: EventCallback[WebSocketClosedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[WebSocketClosedEvent] | Unsubscribe:
        """Fired when WebSocket is closed."""

        return cast(
            Awaitable[WebSocketClosedEvent] | Unsubscribe,
            self._event(
                "webSocketClosed",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def webSocketCreated(
        self,
        callback_or_session: EventCallback[WebSocketCreatedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def webSocketCreated(
        self,
        callback_or_session: str,
        handler: EventCallback[WebSocketCreatedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def webSocketCreated(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[WebSocketCreatedEvent]: ...

    def webSocketCreated(
        self,
        callback_or_session: EventCallback[WebSocketCreatedEvent] | str | None = None,
        handler: EventCallback[WebSocketCreatedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[WebSocketCreatedEvent] | Unsubscribe:
        """Fired upon WebSocket creation."""

        return cast(
            Awaitable[WebSocketCreatedEvent] | Unsubscribe,
            self._event(
                "webSocketCreated",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def webSocketFrameError(
        self,
        callback_or_session: EventCallback[WebSocketFrameErrorEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def webSocketFrameError(
        self,
        callback_or_session: str,
        handler: EventCallback[WebSocketFrameErrorEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def webSocketFrameError(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[WebSocketFrameErrorEvent]: ...

    def webSocketFrameError(
        self,
        callback_or_session: EventCallback[WebSocketFrameErrorEvent]
        | str
        | None = None,
        handler: EventCallback[WebSocketFrameErrorEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[WebSocketFrameErrorEvent] | Unsubscribe:
        """Fired when WebSocket message error occurs."""

        return cast(
            Awaitable[WebSocketFrameErrorEvent] | Unsubscribe,
            self._event(
                "webSocketFrameError",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def webSocketFrameReceived(
        self,
        callback_or_session: EventCallback[WebSocketFrameReceivedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def webSocketFrameReceived(
        self,
        callback_or_session: str,
        handler: EventCallback[WebSocketFrameReceivedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def webSocketFrameReceived(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[WebSocketFrameReceivedEvent]: ...

    def webSocketFrameReceived(
        self,
        callback_or_session: EventCallback[WebSocketFrameReceivedEvent]
        | str
        | None = None,
        handler: EventCallback[WebSocketFrameReceivedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[WebSocketFrameReceivedEvent] | Unsubscribe:
        """Fired when WebSocket message is received."""

        return cast(
            Awaitable[WebSocketFrameReceivedEvent] | Unsubscribe,
            self._event(
                "webSocketFrameReceived",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def webSocketFrameSent(
        self,
        callback_or_session: EventCallback[WebSocketFrameSentEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def webSocketFrameSent(
        self,
        callback_or_session: str,
        handler: EventCallback[WebSocketFrameSentEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def webSocketFrameSent(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[WebSocketFrameSentEvent]: ...

    def webSocketFrameSent(
        self,
        callback_or_session: EventCallback[WebSocketFrameSentEvent] | str | None = None,
        handler: EventCallback[WebSocketFrameSentEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[WebSocketFrameSentEvent] | Unsubscribe:
        """Fired when WebSocket message is sent."""

        return cast(
            Awaitable[WebSocketFrameSentEvent] | Unsubscribe,
            self._event(
                "webSocketFrameSent",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def webSocketHandshakeResponseReceived(
        self,
        callback_or_session: EventCallback[WebSocketHandshakeResponseReceivedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def webSocketHandshakeResponseReceived(
        self,
        callback_or_session: str,
        handler: EventCallback[WebSocketHandshakeResponseReceivedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def webSocketHandshakeResponseReceived(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[WebSocketHandshakeResponseReceivedEvent]: ...

    def webSocketHandshakeResponseReceived(
        self,
        callback_or_session: EventCallback[WebSocketHandshakeResponseReceivedEvent]
        | str
        | None = None,
        handler: EventCallback[WebSocketHandshakeResponseReceivedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[WebSocketHandshakeResponseReceivedEvent] | Unsubscribe:
        """Fired when WebSocket handshake response becomes available."""

        return cast(
            Awaitable[WebSocketHandshakeResponseReceivedEvent] | Unsubscribe,
            self._event(
                "webSocketHandshakeResponseReceived",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def webSocketWillSendHandshakeRequest(
        self,
        callback_or_session: EventCallback[WebSocketWillSendHandshakeRequestEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def webSocketWillSendHandshakeRequest(
        self,
        callback_or_session: str,
        handler: EventCallback[WebSocketWillSendHandshakeRequestEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def webSocketWillSendHandshakeRequest(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[WebSocketWillSendHandshakeRequestEvent]: ...

    def webSocketWillSendHandshakeRequest(
        self,
        callback_or_session: EventCallback[WebSocketWillSendHandshakeRequestEvent]
        | str
        | None = None,
        handler: EventCallback[WebSocketWillSendHandshakeRequestEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[WebSocketWillSendHandshakeRequestEvent] | Unsubscribe:
        """Fired when WebSocket is about to initiate handshake."""

        return cast(
            Awaitable[WebSocketWillSendHandshakeRequestEvent] | Unsubscribe,
            self._event(
                "webSocketWillSendHandshakeRequest",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def webTransportCreated(
        self,
        callback_or_session: EventCallback[WebTransportCreatedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def webTransportCreated(
        self,
        callback_or_session: str,
        handler: EventCallback[WebTransportCreatedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def webTransportCreated(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[WebTransportCreatedEvent]: ...

    def webTransportCreated(
        self,
        callback_or_session: EventCallback[WebTransportCreatedEvent]
        | str
        | None = None,
        handler: EventCallback[WebTransportCreatedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[WebTransportCreatedEvent] | Unsubscribe:
        """Fired upon WebTransport creation."""

        return cast(
            Awaitable[WebTransportCreatedEvent] | Unsubscribe,
            self._event(
                "webTransportCreated",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def webTransportConnectionEstablished(
        self,
        callback_or_session: EventCallback[WebTransportConnectionEstablishedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def webTransportConnectionEstablished(
        self,
        callback_or_session: str,
        handler: EventCallback[WebTransportConnectionEstablishedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def webTransportConnectionEstablished(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[WebTransportConnectionEstablishedEvent]: ...

    def webTransportConnectionEstablished(
        self,
        callback_or_session: EventCallback[WebTransportConnectionEstablishedEvent]
        | str
        | None = None,
        handler: EventCallback[WebTransportConnectionEstablishedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[WebTransportConnectionEstablishedEvent] | Unsubscribe:
        """Fired when WebTransport handshake is finished."""

        return cast(
            Awaitable[WebTransportConnectionEstablishedEvent] | Unsubscribe,
            self._event(
                "webTransportConnectionEstablished",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def webTransportClosed(
        self,
        callback_or_session: EventCallback[WebTransportClosedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def webTransportClosed(
        self,
        callback_or_session: str,
        handler: EventCallback[WebTransportClosedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def webTransportClosed(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[WebTransportClosedEvent]: ...

    def webTransportClosed(
        self,
        callback_or_session: EventCallback[WebTransportClosedEvent] | str | None = None,
        handler: EventCallback[WebTransportClosedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[WebTransportClosedEvent] | Unsubscribe:
        """Fired when WebTransport is disposed."""

        return cast(
            Awaitable[WebTransportClosedEvent] | Unsubscribe,
            self._event(
                "webTransportClosed",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def requestWillBeSentExtraInfo(
        self,
        callback_or_session: EventCallback[RequestWillBeSentExtraInfoEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def requestWillBeSentExtraInfo(
        self,
        callback_or_session: str,
        handler: EventCallback[RequestWillBeSentExtraInfoEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def requestWillBeSentExtraInfo(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[RequestWillBeSentExtraInfoEvent]: ...

    def requestWillBeSentExtraInfo(
        self,
        callback_or_session: EventCallback[RequestWillBeSentExtraInfoEvent]
        | str
        | None = None,
        handler: EventCallback[RequestWillBeSentExtraInfoEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[RequestWillBeSentExtraInfoEvent] | Unsubscribe:
        """Fired when additional information about a requestWillBeSent event is available from the network stack. Not every requestWillBeSent event will have an additional requestWillBeSentExtraInfo fired for it, and there is no guarantee whether requestWillBeSent or requestWillBeSentExtraInfo will be fired first for the same request."""

        return cast(
            Awaitable[RequestWillBeSentExtraInfoEvent] | Unsubscribe,
            self._event(
                "requestWillBeSentExtraInfo",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def responseReceivedExtraInfo(
        self,
        callback_or_session: EventCallback[ResponseReceivedExtraInfoEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def responseReceivedExtraInfo(
        self,
        callback_or_session: str,
        handler: EventCallback[ResponseReceivedExtraInfoEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def responseReceivedExtraInfo(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[ResponseReceivedExtraInfoEvent]: ...

    def responseReceivedExtraInfo(
        self,
        callback_or_session: EventCallback[ResponseReceivedExtraInfoEvent]
        | str
        | None = None,
        handler: EventCallback[ResponseReceivedExtraInfoEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[ResponseReceivedExtraInfoEvent] | Unsubscribe:
        """Fired when additional information about a responseReceived event is available from the network stack. Not every responseReceived event will have an additional responseReceivedExtraInfo for it, and responseReceivedExtraInfo may be fired before or after responseReceived."""

        return cast(
            Awaitable[ResponseReceivedExtraInfoEvent] | Unsubscribe,
            self._event(
                "responseReceivedExtraInfo",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def trustTokenOperationDone(
        self,
        callback_or_session: EventCallback[TrustTokenOperationDoneEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def trustTokenOperationDone(
        self,
        callback_or_session: str,
        handler: EventCallback[TrustTokenOperationDoneEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def trustTokenOperationDone(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[TrustTokenOperationDoneEvent]: ...

    def trustTokenOperationDone(
        self,
        callback_or_session: EventCallback[TrustTokenOperationDoneEvent]
        | str
        | None = None,
        handler: EventCallback[TrustTokenOperationDoneEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[TrustTokenOperationDoneEvent] | Unsubscribe:
        """Fired exactly once for each Trust Token operation. Depending on the type of the operation and whether the operation succeeded or failed, the event is fired before the corresponding request was sent or after the response was received."""

        return cast(
            Awaitable[TrustTokenOperationDoneEvent] | Unsubscribe,
            self._event(
                "trustTokenOperationDone",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def subresourceWebBundleMetadataReceived(
        self,
        callback_or_session: EventCallback[SubresourceWebBundleMetadataReceivedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def subresourceWebBundleMetadataReceived(
        self,
        callback_or_session: str,
        handler: EventCallback[SubresourceWebBundleMetadataReceivedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def subresourceWebBundleMetadataReceived(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[SubresourceWebBundleMetadataReceivedEvent]: ...

    def subresourceWebBundleMetadataReceived(
        self,
        callback_or_session: EventCallback[SubresourceWebBundleMetadataReceivedEvent]
        | str
        | None = None,
        handler: EventCallback[SubresourceWebBundleMetadataReceivedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[SubresourceWebBundleMetadataReceivedEvent] | Unsubscribe:
        """Fired once when parsing the .wbn file has succeeded. The event contains the information about the web bundle contents."""

        return cast(
            Awaitable[SubresourceWebBundleMetadataReceivedEvent] | Unsubscribe,
            self._event(
                "subresourceWebBundleMetadataReceived",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def subresourceWebBundleMetadataError(
        self,
        callback_or_session: EventCallback[SubresourceWebBundleMetadataErrorEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def subresourceWebBundleMetadataError(
        self,
        callback_or_session: str,
        handler: EventCallback[SubresourceWebBundleMetadataErrorEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def subresourceWebBundleMetadataError(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[SubresourceWebBundleMetadataErrorEvent]: ...

    def subresourceWebBundleMetadataError(
        self,
        callback_or_session: EventCallback[SubresourceWebBundleMetadataErrorEvent]
        | str
        | None = None,
        handler: EventCallback[SubresourceWebBundleMetadataErrorEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[SubresourceWebBundleMetadataErrorEvent] | Unsubscribe:
        """Fired once when parsing the .wbn file has failed."""

        return cast(
            Awaitable[SubresourceWebBundleMetadataErrorEvent] | Unsubscribe,
            self._event(
                "subresourceWebBundleMetadataError",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def subresourceWebBundleInnerResponseParsed(
        self,
        callback_or_session: EventCallback[
            SubresourceWebBundleInnerResponseParsedEvent
        ],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def subresourceWebBundleInnerResponseParsed(
        self,
        callback_or_session: str,
        handler: EventCallback[SubresourceWebBundleInnerResponseParsedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def subresourceWebBundleInnerResponseParsed(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[SubresourceWebBundleInnerResponseParsedEvent]: ...

    def subresourceWebBundleInnerResponseParsed(
        self,
        callback_or_session: EventCallback[SubresourceWebBundleInnerResponseParsedEvent]
        | str
        | None = None,
        handler: EventCallback[SubresourceWebBundleInnerResponseParsedEvent]
        | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[SubresourceWebBundleInnerResponseParsedEvent] | Unsubscribe:
        """Fired when handling requests for resources within a .wbn file. Note: this will only be fired for resources that are requested by the webpage."""

        return cast(
            Awaitable[SubresourceWebBundleInnerResponseParsedEvent] | Unsubscribe,
            self._event(
                "subresourceWebBundleInnerResponseParsed",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def subresourceWebBundleInnerResponseError(
        self,
        callback_or_session: EventCallback[SubresourceWebBundleInnerResponseErrorEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def subresourceWebBundleInnerResponseError(
        self,
        callback_or_session: str,
        handler: EventCallback[SubresourceWebBundleInnerResponseErrorEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def subresourceWebBundleInnerResponseError(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[SubresourceWebBundleInnerResponseErrorEvent]: ...

    def subresourceWebBundleInnerResponseError(
        self,
        callback_or_session: EventCallback[SubresourceWebBundleInnerResponseErrorEvent]
        | str
        | None = None,
        handler: EventCallback[SubresourceWebBundleInnerResponseErrorEvent]
        | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[SubresourceWebBundleInnerResponseErrorEvent] | Unsubscribe:
        """Fired when request for resources within a .wbn file failed."""

        return cast(
            Awaitable[SubresourceWebBundleInnerResponseErrorEvent] | Unsubscribe,
            self._event(
                "subresourceWebBundleInnerResponseError",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def reportingApiReportAdded(
        self,
        callback_or_session: EventCallback[ReportingApiReportAddedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def reportingApiReportAdded(
        self,
        callback_or_session: str,
        handler: EventCallback[ReportingApiReportAddedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def reportingApiReportAdded(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[ReportingApiReportAddedEvent]: ...

    def reportingApiReportAdded(
        self,
        callback_or_session: EventCallback[ReportingApiReportAddedEvent]
        | str
        | None = None,
        handler: EventCallback[ReportingApiReportAddedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[ReportingApiReportAddedEvent] | Unsubscribe:
        """Is sent whenever a new report is added. And after 'enableReportingApi' for all existing reports."""

        return cast(
            Awaitable[ReportingApiReportAddedEvent] | Unsubscribe,
            self._event(
                "reportingApiReportAdded",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def reportingApiReportUpdated(
        self,
        callback_or_session: EventCallback[ReportingApiReportUpdatedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def reportingApiReportUpdated(
        self,
        callback_or_session: str,
        handler: EventCallback[ReportingApiReportUpdatedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def reportingApiReportUpdated(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[ReportingApiReportUpdatedEvent]: ...

    def reportingApiReportUpdated(
        self,
        callback_or_session: EventCallback[ReportingApiReportUpdatedEvent]
        | str
        | None = None,
        handler: EventCallback[ReportingApiReportUpdatedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[ReportingApiReportUpdatedEvent] | Unsubscribe:
        """Wait for or subscribe to Network.reportingApiReportUpdated."""

        return cast(
            Awaitable[ReportingApiReportUpdatedEvent] | Unsubscribe,
            self._event(
                "reportingApiReportUpdated",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def reportingApiEndpointsChangedForOrigin(
        self,
        callback_or_session: EventCallback[ReportingApiEndpointsChangedForOriginEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def reportingApiEndpointsChangedForOrigin(
        self,
        callback_or_session: str,
        handler: EventCallback[ReportingApiEndpointsChangedForOriginEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def reportingApiEndpointsChangedForOrigin(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[ReportingApiEndpointsChangedForOriginEvent]: ...

    def reportingApiEndpointsChangedForOrigin(
        self,
        callback_or_session: EventCallback[ReportingApiEndpointsChangedForOriginEvent]
        | str
        | None = None,
        handler: EventCallback[ReportingApiEndpointsChangedForOriginEvent]
        | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[ReportingApiEndpointsChangedForOriginEvent] | Unsubscribe:
        """Wait for or subscribe to Network.reportingApiEndpointsChangedForOrigin."""

        return cast(
            Awaitable[ReportingApiEndpointsChangedForOriginEvent] | Unsubscribe,
            self._event(
                "reportingApiEndpointsChangedForOrigin",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )


__all__ = [
    "AlternateProtocolUsage",
    "AuthChallenge",
    "AuthChallengeResponse",
    "BlockedCookieWithReason",
    "BlockedReason",
    "BlockedSetCookieWithReason",
    "CachedResource",
    "CanClearBrowserCacheResult",
    "CanClearBrowserCookiesResult",
    "CanEmulateNetworkConditionsResult",
    "CertificateTransparencyCompliance",
    "ClientSecurityState",
    "ConnectTiming",
    "ConnectionType",
    "ContentEncoding",
    "ContentSecurityPolicySource",
    "ContentSecurityPolicyStatus",
    "ContinueInterceptedRequestParameters",
    "Cookie",
    "CookieBlockedReason",
    "CookieParam",
    "CookiePriority",
    "CookieSameSite",
    "CookieSourceScheme",
    "CorsError",
    "CorsErrorStatus",
    "CrossOriginEmbedderPolicyStatus",
    "CrossOriginEmbedderPolicyValue",
    "CrossOriginOpenerPolicyStatus",
    "CrossOriginOpenerPolicyValue",
    "DataReceivedEvent",
    "DeleteCookiesParameters",
    "EmulateNetworkConditionsParameters",
    "EnableParameters",
    "EnableReportingApiParameters",
    "ErrorReason",
    "EventSourceMessageReceivedEvent",
    "GetAllCookiesResult",
    "GetCertificateParameters",
    "GetCertificateResult",
    "GetCookiesParameters",
    "GetCookiesResult",
    "GetRequestPostDataParameters",
    "GetRequestPostDataResult",
    "GetResponseBodyForInterceptionParameters",
    "GetResponseBodyForInterceptionResult",
    "GetResponseBodyParameters",
    "GetResponseBodyResult",
    "GetSecurityIsolationStatusParameters",
    "GetSecurityIsolationStatusResult",
    "Headers",
    "IPAddressSpace",
    "Initiator",
    "InterceptionId",
    "InterceptionStage",
    "LoadNetworkResourceOptions",
    "LoadNetworkResourcePageResult",
    "LoadNetworkResourceParameters",
    "LoadNetworkResourceResult",
    "LoaderId",
    "LoadingFailedEvent",
    "LoadingFinishedEvent",
    "MonotonicTime",
    "Network",
    "PostDataEntry",
    "PrivateNetworkRequestPolicy",
    "ReplayXHRParameters",
    "ReportId",
    "ReportStatus",
    "ReportingApiEndpoint",
    "ReportingApiEndpointsChangedForOriginEvent",
    "ReportingApiReport",
    "ReportingApiReportAddedEvent",
    "ReportingApiReportUpdatedEvent",
    "Request",
    "RequestId",
    "RequestInterceptedEvent",
    "RequestPattern",
    "RequestServedFromCacheEvent",
    "RequestWillBeSentEvent",
    "RequestWillBeSentExtraInfoEvent",
    "ResourceChangedPriorityEvent",
    "ResourcePriority",
    "ResourceTiming",
    "ResourceType",
    "Response",
    "ResponseReceivedEvent",
    "ResponseReceivedExtraInfoEvent",
    "SearchInResponseBodyParameters",
    "SearchInResponseBodyResult",
    "SecurityDetails",
    "SecurityIsolationStatus",
    "ServiceWorkerResponseSource",
    "SetAcceptedEncodingsParameters",
    "SetAttachDebugStackParameters",
    "SetBlockedURLsParameters",
    "SetBypassServiceWorkerParameters",
    "SetCacheDisabledParameters",
    "SetCookieBlockedReason",
    "SetCookieParameters",
    "SetCookieResult",
    "SetCookiesParameters",
    "SetExtraHTTPHeadersParameters",
    "SetRequestInterceptionParameters",
    "SetUserAgentOverrideParameters",
    "SignedCertificateTimestamp",
    "SignedExchangeError",
    "SignedExchangeErrorField",
    "SignedExchangeHeader",
    "SignedExchangeInfo",
    "SignedExchangeReceivedEvent",
    "SignedExchangeSignature",
    "SubresourceWebBundleInnerResponseErrorEvent",
    "SubresourceWebBundleInnerResponseParsedEvent",
    "SubresourceWebBundleMetadataErrorEvent",
    "SubresourceWebBundleMetadataReceivedEvent",
    "TakeResponseBodyForInterceptionAsStreamParameters",
    "TakeResponseBodyForInterceptionAsStreamResult",
    "TimeSinceEpoch",
    "TrustTokenOperationDoneEvent",
    "TrustTokenOperationType",
    "TrustTokenParams",
    "WebSocketClosedEvent",
    "WebSocketCreatedEvent",
    "WebSocketFrame",
    "WebSocketFrameErrorEvent",
    "WebSocketFrameReceivedEvent",
    "WebSocketFrameSentEvent",
    "WebSocketHandshakeResponseReceivedEvent",
    "WebSocketRequest",
    "WebSocketResponse",
    "WebSocketWillSendHandshakeRequestEvent",
    "WebTransportClosedEvent",
    "WebTransportConnectionEstablishedEvent",
    "WebTransportCreatedEvent",
]
