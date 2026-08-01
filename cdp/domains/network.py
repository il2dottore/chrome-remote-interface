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
    "FedCM",
    "Other",
]

LoaderId: TypeAlias = str

RequestId: TypeAlias = str

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
    workerRouterEvaluationStart: NotRequired[float]
    workerCacheLookupStart: NotRequired[float]
    sendStart: float
    sendEnd: float
    pushStart: float
    pushEnd: float
    receiveHeadersStart: float
    receiveHeadersEnd: float


ResourcePriority: TypeAlias = Literal["VeryLow", "Low", "Medium", "High", "VeryHigh"]

RenderBlockingBehavior: TypeAlias = Literal[
    "Blocking",
    "InBodyParserBlocking",
    "NonBlocking",
    "NonBlockingDynamic",
    "PotentiallyBlocking",
]


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
    isAdRelated: NotRequired[bool]


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
    "integrity",
    "subresource-filter",
    "content-type",
    "coep-frame-resource-needs-coep-header",
    "coop-sandboxed-iframe-cannot-navigate-to-coop-page",
    "corp-not-same-origin",
    "corp-not-same-origin-after-defaulted-to-same-origin-by-coep",
    "corp-not-same-origin-after-defaulted-to-same-origin-by-dip",
    "corp-not-same-origin-after-defaulted-to-same-origin-by-coep-and-dip",
    "corp-not-same-site",
    "sri-message-signature-mismatch",
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
    "InvalidAllowMethodsPreflightResponse",
    "InvalidAllowHeadersPreflightResponse",
    "MethodDisallowedByPreflightResponse",
    "HeaderDisallowedByPreflightResponse",
    "RedirectContainsCredentials",
    "InsecureLocalNetwork",
    "InvalidLocalNetworkAccess",
    "NoCorsRedirectModeNotFollow",
    "LocalNetworkAccessPermissionDenied",
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

ServiceWorkerRouterSource: TypeAlias = Literal[
    "network",
    "cache",
    "fetch-event",
    "race-network-and-fetch-handler",
    "race-network-and-cache",
]


class ServiceWorkerRouterInfo(TypedDict):
    ruleIdMatched: NotRequired[int]
    matchedSourceType: NotRequired[ServiceWorkerRouterSource]
    actualSourceType: NotRequired[ServiceWorkerRouterSource]


class Response(TypedDict):
    url: str
    status: int
    statusText: str
    headers: Headers
    headersText: NotRequired[str]
    mimeType: str
    charset: str
    requestHeaders: NotRequired[Headers]
    requestHeadersText: NotRequired[str]
    connectionReused: bool
    connectionId: float
    remoteIPAddress: NotRequired[str]
    remotePort: NotRequired[int]
    fromDiskCache: NotRequired[bool]
    fromServiceWorker: NotRequired[bool]
    fromPrefetchCache: NotRequired[bool]
    fromEarlyHints: NotRequired[bool]
    serviceWorkerRouterInfo: NotRequired[ServiceWorkerRouterInfo]
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
    type: Literal[
        "parser", "script", "preload", "SignedExchange", "preflight", "FedCM", "other"
    ]
    stack: NotRequired[Runtime.StackTrace]
    url: NotRequired[str]
    lineNumber: NotRequired[float]
    columnNumber: NotRequired[float]
    requestId: NotRequired[RequestId]


class CookiePartitionKey(TypedDict):
    topLevelSite: str
    hasCrossSiteAncestor: bool


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
    sourceScheme: CookieSourceScheme
    sourcePort: int
    partitionKey: NotRequired[CookiePartitionKey]
    partitionKeyOpaque: NotRequired[bool]


SetCookieBlockedReason: TypeAlias = Literal[
    "SecureOnly",
    "SameSiteStrict",
    "SameSiteLax",
    "SameSiteUnspecifiedTreatedAsLax",
    "SameSiteNoneInsecure",
    "UserPreferences",
    "ThirdPartyPhaseout",
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
    "NameValuePairExceedsMaxSize",
    "DisallowedCharacter",
    "NoCookieContent",
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
    "ThirdPartyPhaseout",
    "ThirdPartyBlockedInFirstPartySet",
    "UnknownError",
    "SchemefulSameSiteStrict",
    "SchemefulSameSiteLax",
    "SchemefulSameSiteUnspecifiedTreatedAsLax",
    "NameValuePairExceedsMaxSize",
    "PortMismatch",
    "SchemeMismatch",
    "AnonymousContext",
]

CookieExemptionReason: TypeAlias = Literal[
    "None",
    "UserSetting",
    "EnterprisePolicy",
    "StorageAccess",
    "TopLevelStorageAccess",
    "Scheme",
    "SameSiteNoneCookiesInSandbox",
]


class BlockedSetCookieWithReason(TypedDict):
    blockedReasons: list[SetCookieBlockedReason]
    cookieLine: str
    cookie: NotRequired[Cookie]


class ExemptedSetCookieWithReason(TypedDict):
    exemptionReason: CookieExemptionReason
    cookieLine: str
    cookie: Cookie


class AssociatedCookie(TypedDict):
    cookie: Cookie
    blockedReasons: list[CookieBlockedReason]
    exemptionReason: NotRequired[CookieExemptionReason]


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
    sourceScheme: NotRequired[CookieSourceScheme]
    sourcePort: NotRequired[int]
    partitionKey: NotRequired[CookiePartitionKey]


class AuthChallenge(TypedDict):
    source: NotRequired[Literal["Server", "Proxy"]]
    origin: str
    scheme: str
    realm: str


class AuthChallengeResponse(TypedDict):
    response: Literal["Default", "CancelAuth", "ProvideCredentials"]
    username: NotRequired[str]
    password: NotRequired[str]


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
    hasExtraInfo: bool
    header: NotRequired[SignedExchangeHeader]
    securityDetails: NotRequired[SecurityDetails]
    errors: NotRequired[list[SignedExchangeError]]


ContentEncoding: TypeAlias = Literal["deflate", "gzip", "br", "zstd"]


class NetworkConditions(TypedDict):
    urlPattern: str
    latency: float
    downloadThroughput: float
    uploadThroughput: float
    connectionType: NotRequired[ConnectionType]
    packetLoss: NotRequired[float]
    packetQueueLength: NotRequired[int]
    packetReordering: NotRequired[bool]
    offline: NotRequired[bool]


class BlockPattern(TypedDict):
    urlPattern: str
    block: bool


DirectSocketDnsQueryType: TypeAlias = Literal["ipv4", "ipv6"]


class DirectTCPSocketOptions(TypedDict):
    noDelay: bool
    keepAliveDelay: NotRequired[float]
    sendBufferSize: NotRequired[float]
    receiveBufferSize: NotRequired[float]
    dnsQueryType: NotRequired[DirectSocketDnsQueryType]


class DirectUDPSocketOptions(TypedDict):
    remoteAddr: NotRequired[str]
    remotePort: NotRequired[int]
    localAddr: NotRequired[str]
    localPort: NotRequired[int]
    dnsQueryType: NotRequired[DirectSocketDnsQueryType]
    sendBufferSize: NotRequired[float]
    receiveBufferSize: NotRequired[float]
    multicastLoopback: NotRequired[bool]
    multicastTimeToLive: NotRequired[int]
    multicastAllowAddressSharing: NotRequired[bool]


class DirectUDPMessage(TypedDict):
    data: str
    remoteAddr: NotRequired[str]
    remotePort: NotRequired[int]


LocalNetworkAccessRequestPolicy: TypeAlias = Literal[
    "Allow",
    "BlockFromInsecureToMorePrivate",
    "WarnFromInsecureToMorePrivate",
    "PermissionBlock",
    "PermissionWarn",
]

IPAddressSpace: TypeAlias = Literal["Loopback", "Local", "Public", "Unknown"]


class ConnectTiming(TypedDict):
    requestTime: float


class ClientSecurityState(TypedDict):
    initiatorIsSecureContext: bool
    initiatorIPAddressSpace: IPAddressSpace
    localNetworkAccessRequestPolicy: LocalNetworkAccessRequestPolicy


class AdScriptIdentifier(TypedDict):
    scriptId: Runtime.ScriptId
    debuggerId: Runtime.UniqueDebuggerId
    name: str


class AdAncestry(TypedDict):
    ancestryChain: list[AdScriptIdentifier]
    rootScriptFilterlistRule: NotRequired[str]


class AdProvenance(TypedDict):
    filterlistRule: NotRequired[str]
    adScriptAncestry: NotRequired[AdAncestry]


CrossOriginOpenerPolicyValue: TypeAlias = Literal[
    "SameOrigin",
    "SameOriginAllowPopups",
    "RestrictProperties",
    "UnsafeNone",
    "SameOriginPlusCoep",
    "RestrictPropertiesPlusCoep",
    "NoopenerAllowPopups",
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


class DeviceBoundSessionKey(TypedDict):
    site: str
    id: str


class DeviceBoundSessionWithUsage(TypedDict):
    sessionKey: DeviceBoundSessionKey
    usage: Literal[
        "NotInScope",
        "InScopeRefreshNotYetNeeded",
        "InScopeRefreshNotAllowed",
        "ProactiveRefreshNotPossible",
        "ProactiveRefreshAttempted",
        "Deferred",
    ]


class DeviceBoundSessionCookieCraving(TypedDict):
    name: str
    domain: str
    path: str
    secure: bool
    httpOnly: bool
    sameSite: NotRequired[CookieSameSite]


class DeviceBoundSessionUrlRule(TypedDict):
    ruleType: Literal["Exclude", "Include"]
    hostPattern: str
    pathPrefix: str


class DeviceBoundSessionInclusionRules(TypedDict):
    origin: str
    includeSite: bool
    urlRules: list[DeviceBoundSessionUrlRule]


class DeviceBoundSession(TypedDict):
    key: DeviceBoundSessionKey
    refreshUrl: str
    inclusionRules: DeviceBoundSessionInclusionRules
    cookieCravings: list[DeviceBoundSessionCookieCraving]
    expiryDate: TimeSinceEpoch
    cachedChallenge: NotRequired[str]
    allowedRefreshInitiators: list[str]


DeviceBoundSessionEventId: TypeAlias = str

DeviceBoundSessionFetchResult: TypeAlias = Literal[
    "Success",
    "SigningKeyGenerationError",
    "AttestationKeyGenerationError",
    "SigningError",
    "TransientSigningError",
    "ServerRequestedTermination",
    "InvalidSessionId",
    "InvalidChallenge",
    "TooManyChallenges",
    "InvalidFetcherUrl",
    "InvalidRefreshUrl",
    "TransientHttpError",
    "ScopeOriginSameSiteMismatch",
    "RefreshUrlSameSiteMismatch",
    "MismatchedSessionId",
    "MissingScope",
    "NoCredentials",
    "SubdomainRegistrationWellKnownUnavailable",
    "SubdomainRegistrationUnauthorized",
    "SubdomainRegistrationWellKnownMalformed",
    "SessionProviderWellKnownUnavailable",
    "RelyingPartyWellKnownUnavailable",
    "FederatedKeyThumbprintMismatch",
    "InvalidFederatedSessionUrl",
    "InvalidFederatedKey",
    "TooManyRelyingOriginLabels",
    "BoundCookieSetForbidden",
    "NetError",
    "ProxyError",
    "EmptySessionConfig",
    "InvalidCredentialsConfig",
    "InvalidCredentialsType",
    "InvalidCredentialsEmptyName",
    "InvalidCredentialsCookie",
    "PersistentHttpError",
    "RegistrationAttemptedChallenge",
    "InvalidScopeOrigin",
    "ScopeOriginContainsPath",
    "RefreshInitiatorNotString",
    "RefreshInitiatorInvalidHostPattern",
    "InvalidScopeSpecification",
    "MissingScopeSpecificationType",
    "EmptyScopeSpecificationDomain",
    "EmptyScopeSpecificationPath",
    "InvalidScopeSpecificationType",
    "InvalidScopeIncludeSite",
    "MissingScopeIncludeSite",
    "FederatedNotAuthorizedByProvider",
    "FederatedNotAuthorizedByRelyingParty",
    "SessionProviderWellKnownMalformed",
    "SessionProviderWellKnownHasProviderOrigin",
    "RelyingPartyWellKnownMalformed",
    "RelyingPartyWellKnownHasRelyingOrigins",
    "InvalidFederatedSessionProviderSessionMissing",
    "InvalidFederatedSessionWrongProviderOrigin",
    "InvalidCredentialsCookieCreationTime",
    "InvalidCredentialsCookieName",
    "InvalidCredentialsCookieParsing",
    "InvalidCredentialsCookieUnpermittedAttribute",
    "InvalidCredentialsCookieInvalidDomain",
    "InvalidCredentialsCookiePrefix",
    "InvalidScopeRulePath",
    "InvalidScopeRuleHostPattern",
    "ScopeRuleOriginScopedHostPatternMismatch",
    "ScopeRuleSiteScopedHostPatternMismatch",
    "SigningQuotaExceeded",
    "InvalidConfigJson",
    "InvalidFederatedSessionProviderFailedToRestoreKey",
    "FailedToUnwrapKey",
    "SessionDeletedDuringRefresh",
    "CrossOriginRegistrationSiteNotIncluded",
    "InvalidPreProvisionedKeyInitiatorMissing",
    "PreProvisionedKeyAccessNotGranted",
    "PreProvisionedKeyNotFound",
]


class DeviceBoundSessionFailedRequest(TypedDict):
    requestUrl: str
    netError: NotRequired[str]
    responseError: NotRequired[int]
    responseErrorBody: NotRequired[str]


class CreationEventDetails(TypedDict):
    fetchResult: DeviceBoundSessionFetchResult
    newSession: NotRequired[DeviceBoundSession]
    failedRequest: NotRequired[DeviceBoundSessionFailedRequest]


class RefreshEventDetails(TypedDict):
    refreshResult: Literal[
        "Refreshed",
        "InitializedService",
        "Unreachable",
        "ServerError",
        "FatalError",
        "SigningQuotaExceeded",
        "RefreshedAsWaiter",
        "TransientSigningError",
        "InScopeRefreshNotYetNeeded",
    ]
    fetchResult: NotRequired[DeviceBoundSessionFetchResult]
    newSession: NotRequired[DeviceBoundSession]
    wasFullyProactiveRefresh: bool
    failedRequest: NotRequired[DeviceBoundSessionFailedRequest]


class TerminationEventDetails(TypedDict):
    deletionReason: Literal[
        "Expired",
        "FailedToRestoreKey",
        "FailedToUnwrapKey",
        "StoragePartitionCleared",
        "ClearBrowsingData",
        "ServerRequested",
        "InvalidSessionParams",
        "RefreshFatalError",
        "DevTools",
    ]


class ChallengeEventDetails(TypedDict):
    challengeResult: Literal[
        "Success", "NoSessionId", "NoSessionMatch", "CantSetBoundCookie"
    ]
    challenge: str


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


class DeleteCookiesParameters(TypedDict):
    name: str
    url: NotRequired[str]
    domain: NotRequired[str]
    path: NotRequired[str]
    partitionKey: NotRequired[CookiePartitionKey]


class EmulateNetworkConditionsParameters(TypedDict):
    offline: bool
    latency: float
    downloadThroughput: float
    uploadThroughput: float
    connectionType: NotRequired[ConnectionType]
    packetLoss: NotRequired[float]
    packetQueueLength: NotRequired[int]
    packetReordering: NotRequired[bool]


class EmulateNetworkConditionsByRuleParameters(TypedDict):
    offline: NotRequired[bool]
    emulateOfflineServiceWorker: NotRequired[bool]
    matchedNetworkConditions: list[NetworkConditions]


class EmulateNetworkConditionsByRuleResult(TypedDict):
    ruleIds: list[str]


class OverrideNetworkStateParameters(TypedDict):
    offline: bool
    latency: float
    downloadThroughput: float
    uploadThroughput: float
    connectionType: NotRequired[ConnectionType]


class EnableParameters(TypedDict):
    maxTotalBufferSize: NotRequired[int]
    maxResourceBufferSize: NotRequired[int]
    maxPostDataSize: NotRequired[int]
    reportDirectSocketTraffic: NotRequired[bool]
    enableDurableMessages: NotRequired[bool]


class ConfigureDurableMessagesParameters(TypedDict):
    maxTotalBufferSize: NotRequired[int]
    maxResourceBufferSize: NotRequired[int]


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
    base64Encoded: bool


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
    urlPatterns: NotRequired[list[BlockPattern]]
    urls: NotRequired[list[str]]


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
    sourceScheme: NotRequired[CookieSourceScheme]
    sourcePort: NotRequired[int]
    partitionKey: NotRequired[CookiePartitionKey]


class SetCookieResult(TypedDict):
    success: bool


class SetCookiesParameters(TypedDict):
    cookies: list[CookieParam]


class SetExtraHTTPHeadersParameters(TypedDict):
    headers: Headers


class SetAttachDebugStackParameters(TypedDict):
    enabled: bool


class SetUserAgentOverrideParameters(TypedDict):
    userAgent: str
    acceptLanguage: NotRequired[str]
    platform: NotRequired[str]
    userAgentMetadata: NotRequired[Emulation.UserAgentMetadata]


class StreamResourceContentParameters(TypedDict):
    requestId: RequestId


class StreamResourceContentResult(TypedDict):
    bufferedData: str


class GetSecurityIsolationStatusParameters(TypedDict):
    frameId: NotRequired[Page.FrameId]


class GetSecurityIsolationStatusResult(TypedDict):
    status: SecurityIsolationStatus


class EnableReportingApiParameters(TypedDict):
    enable: bool


class EnableDeviceBoundSessionsParameters(TypedDict):
    enable: bool


class DeleteDeviceBoundSessionParameters(TypedDict):
    key: DeviceBoundSessionKey


class FetchSchemefulSiteParameters(TypedDict):
    origin: str


class FetchSchemefulSiteResult(TypedDict):
    schemefulSite: str


class LoadNetworkResourceParameters(TypedDict):
    frameId: NotRequired[Page.FrameId]
    url: str
    options: LoadNetworkResourceOptions


class LoadNetworkResourceResult(TypedDict):
    resource: LoadNetworkResourcePageResult


class SetCookieControlsParameters(TypedDict):
    enableThirdPartyCookieRestriction: bool


class DataReceivedEvent(TypedDict):
    requestId: RequestId
    timestamp: MonotonicTime
    dataLength: int
    encodedDataLength: int
    data: NotRequired[str]


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
    renderBlockingBehavior: NotRequired[RenderBlockingBehavior]


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


class DirectTCPSocketCreatedEvent(TypedDict):
    identifier: RequestId
    remoteAddr: str
    remotePort: int
    options: DirectTCPSocketOptions
    timestamp: MonotonicTime
    initiator: NotRequired[Initiator]


class DirectTCPSocketOpenedEvent(TypedDict):
    identifier: RequestId
    remoteAddr: str
    remotePort: int
    timestamp: MonotonicTime
    localAddr: NotRequired[str]
    localPort: NotRequired[int]


class DirectTCPSocketAbortedEvent(TypedDict):
    identifier: RequestId
    errorMessage: ErrorReason
    timestamp: MonotonicTime


class DirectTCPSocketClosedEvent(TypedDict):
    identifier: RequestId
    timestamp: MonotonicTime


class DirectTCPSocketChunkSentEvent(TypedDict):
    identifier: RequestId
    data: str
    timestamp: MonotonicTime


class DirectTCPSocketChunkReceivedEvent(TypedDict):
    identifier: RequestId
    data: str
    timestamp: MonotonicTime


class DirectUDPSocketJoinedMulticastGroupEvent(TypedDict):
    identifier: RequestId
    IPAddress: str


class DirectUDPSocketLeftMulticastGroupEvent(TypedDict):
    identifier: RequestId
    IPAddress: str


class DirectUDPSocketCreatedEvent(TypedDict):
    identifier: RequestId
    options: DirectUDPSocketOptions
    timestamp: MonotonicTime
    initiator: NotRequired[Initiator]


class DirectUDPSocketOpenedEvent(TypedDict):
    identifier: RequestId
    localAddr: str
    localPort: int
    timestamp: MonotonicTime
    remoteAddr: NotRequired[str]
    remotePort: NotRequired[int]


class DirectUDPSocketAbortedEvent(TypedDict):
    identifier: RequestId
    errorMessage: ErrorReason
    timestamp: MonotonicTime


class DirectUDPSocketClosedEvent(TypedDict):
    identifier: RequestId
    timestamp: MonotonicTime


class DirectUDPSocketChunkSentEvent(TypedDict):
    identifier: RequestId
    message: DirectUDPMessage
    timestamp: MonotonicTime


class DirectUDPSocketChunkReceivedEvent(TypedDict):
    identifier: RequestId
    message: DirectUDPMessage
    timestamp: MonotonicTime


class RequestWillBeSentExtraInfoEvent(TypedDict):
    requestId: RequestId
    associatedCookies: list[AssociatedCookie]
    headers: Headers
    connectTiming: ConnectTiming
    deviceBoundSessionUsages: NotRequired[list[DeviceBoundSessionWithUsage]]
    clientSecurityState: NotRequired[ClientSecurityState]
    siteHasCookieInOtherPartition: NotRequired[bool]
    appliedNetworkConditionsId: NotRequired[str]


class ResponseReceivedExtraInfoEvent(TypedDict):
    requestId: RequestId
    blockedCookies: list[BlockedSetCookieWithReason]
    headers: Headers
    resourceIPAddressSpace: IPAddressSpace
    statusCode: int
    headersText: NotRequired[str]
    cookiePartitionKey: NotRequired[CookiePartitionKey]
    cookiePartitionKeyOpaque: NotRequired[bool]
    exemptedCookies: NotRequired[list[ExemptedSetCookieWithReason]]


class ResponseReceivedEarlyHintsEvent(TypedDict):
    requestId: RequestId
    headers: Headers


class TrustTokenOperationDoneEvent(TypedDict):
    status: Literal[
        "Ok",
        "InvalidArgument",
        "MissingIssuerKeys",
        "FailedPrecondition",
        "ResourceExhausted",
        "AlreadyExists",
        "ResourceLimited",
        "Unauthorized",
        "BadResponse",
        "InternalError",
        "UnknownError",
        "FulfilledLocally",
        "SiteIssuerLimit",
    ]
    type: TrustTokenOperationType
    requestId: RequestId
    topLevelOrigin: NotRequired[str]
    issuerOrigin: NotRequired[str]
    issuedTokenCount: NotRequired[int]


class ReportingApiReportAddedEvent(TypedDict):
    report: ReportingApiReport


class ReportingApiReportUpdatedEvent(TypedDict):
    report: ReportingApiReport


class ReportingApiEndpointsChangedForOriginEvent(TypedDict):
    origin: str
    endpoints: list[ReportingApiEndpoint]


class DeviceBoundSessionsAddedEvent(TypedDict):
    sessions: list[DeviceBoundSession]


class DeviceBoundSessionEventOccurredEvent(TypedDict):
    eventId: DeviceBoundSessionEventId
    site: str
    succeeded: bool
    sessionId: NotRequired[str]
    creationEventDetails: NotRequired[CreationEventDetails]
    refreshEventDetails: NotRequired[RefreshEventDetails]
    terminationEventDetails: NotRequired[TerminationEventDetails]
    challengeEventDetails: NotRequired[ChallengeEventDetails]


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
        """Deletes browser cookies with matching name and url or domain/path/partitionKey pair."""

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
        """Activates emulation of network conditions. This command is deprecated in favor of the emulateNetworkConditionsByRule and overrideNetworkState commands, which can be used together to the same effect."""

        return await self._command(
            "emulateNetworkConditions", params, session_id, kwargs
        )

    @overload
    async def emulateNetworkConditionsByRule(
        self,
        params: EmulateNetworkConditionsByRuleParameters,
        session_id: str | None = None,
    ) -> EmulateNetworkConditionsByRuleResult: ...

    @overload
    async def emulateNetworkConditionsByRule(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[EmulateNetworkConditionsByRuleParameters],
    ) -> EmulateNetworkConditionsByRuleResult: ...

    async def emulateNetworkConditionsByRule(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> EmulateNetworkConditionsByRuleResult:
        """Activates emulation of network conditions for individual requests using URL match patterns. Unlike the deprecated Network.emulateNetworkConditions this method does not affect `navigator` state. Use Network.overrideNetworkState to explicitly modify `navigator` behavior."""

        return cast(
            EmulateNetworkConditionsByRuleResult,
            await self._command(
                "emulateNetworkConditionsByRule", params, session_id, kwargs
            ),
        )

    @overload
    async def overrideNetworkState(
        self,
        params: OverrideNetworkStateParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def overrideNetworkState(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[OverrideNetworkStateParameters],
    ) -> JsonObject: ...

    async def overrideNetworkState(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Override the state of navigator.onLine and navigator.connection."""

        return await self._command("overrideNetworkState", params, session_id, kwargs)

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

    @overload
    async def configureDurableMessages(
        self,
        params: ConfigureDurableMessagesParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def configureDurableMessages(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[ConfigureDurableMessagesParameters],
    ) -> JsonObject: ...

    async def configureDurableMessages(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Configures storing response bodies outside of renderer, so that these survive a cross-process navigation. If maxTotalBufferSize is not set, durable messages are disabled."""

        return await self._command(
            "configureDurableMessages", params, session_id, kwargs
        )

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
    async def streamResourceContent(
        self,
        params: StreamResourceContentParameters,
        session_id: str | None = None,
    ) -> StreamResourceContentResult: ...

    @overload
    async def streamResourceContent(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[StreamResourceContentParameters],
    ) -> StreamResourceContentResult: ...

    async def streamResourceContent(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> StreamResourceContentResult:
        """Enables streaming of the response for the given requestId. If enabled, the dataReceived event contains the data that was received during streaming."""

        return cast(
            StreamResourceContentResult,
            await self._command("streamResourceContent", params, session_id, kwargs),
        )

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
    async def enableDeviceBoundSessions(
        self,
        params: EnableDeviceBoundSessionsParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def enableDeviceBoundSessions(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[EnableDeviceBoundSessionsParameters],
    ) -> JsonObject: ...

    async def enableDeviceBoundSessions(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Sets up tracking device bound sessions and fetching of initial set of sessions."""

        return await self._command(
            "enableDeviceBoundSessions", params, session_id, kwargs
        )

    @overload
    async def deleteDeviceBoundSession(
        self,
        params: DeleteDeviceBoundSessionParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def deleteDeviceBoundSession(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[DeleteDeviceBoundSessionParameters],
    ) -> JsonObject: ...

    async def deleteDeviceBoundSession(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Deletes a device bound session."""

        return await self._command(
            "deleteDeviceBoundSession", params, session_id, kwargs
        )

    @overload
    async def fetchSchemefulSite(
        self,
        params: FetchSchemefulSiteParameters,
        session_id: str | None = None,
    ) -> FetchSchemefulSiteResult: ...

    @overload
    async def fetchSchemefulSite(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[FetchSchemefulSiteParameters],
    ) -> FetchSchemefulSiteResult: ...

    async def fetchSchemefulSite(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> FetchSchemefulSiteResult:
        """Fetches the schemeful site for a specific origin."""

        return cast(
            FetchSchemefulSiteResult,
            await self._command("fetchSchemefulSite", params, session_id, kwargs),
        )

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
    async def setCookieControls(
        self,
        params: SetCookieControlsParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def setCookieControls(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetCookieControlsParameters],
    ) -> JsonObject: ...

    async def setCookieControls(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Sets Controls for third-party cookie access Page reload is required before the new cookie behavior will be observed"""

        return await self._command("setCookieControls", params, session_id, kwargs)

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
    def directTCPSocketCreated(
        self,
        callback_or_session: EventCallback[DirectTCPSocketCreatedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def directTCPSocketCreated(
        self,
        callback_or_session: str,
        handler: EventCallback[DirectTCPSocketCreatedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def directTCPSocketCreated(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[DirectTCPSocketCreatedEvent]: ...

    def directTCPSocketCreated(
        self,
        callback_or_session: EventCallback[DirectTCPSocketCreatedEvent]
        | str
        | None = None,
        handler: EventCallback[DirectTCPSocketCreatedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[DirectTCPSocketCreatedEvent] | Unsubscribe:
        """Fired upon direct_socket.TCPSocket creation."""

        return cast(
            Awaitable[DirectTCPSocketCreatedEvent] | Unsubscribe,
            self._event(
                "directTCPSocketCreated",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def directTCPSocketOpened(
        self,
        callback_or_session: EventCallback[DirectTCPSocketOpenedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def directTCPSocketOpened(
        self,
        callback_or_session: str,
        handler: EventCallback[DirectTCPSocketOpenedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def directTCPSocketOpened(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[DirectTCPSocketOpenedEvent]: ...

    def directTCPSocketOpened(
        self,
        callback_or_session: EventCallback[DirectTCPSocketOpenedEvent]
        | str
        | None = None,
        handler: EventCallback[DirectTCPSocketOpenedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[DirectTCPSocketOpenedEvent] | Unsubscribe:
        """Fired when direct_socket.TCPSocket connection is opened."""

        return cast(
            Awaitable[DirectTCPSocketOpenedEvent] | Unsubscribe,
            self._event(
                "directTCPSocketOpened",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def directTCPSocketAborted(
        self,
        callback_or_session: EventCallback[DirectTCPSocketAbortedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def directTCPSocketAborted(
        self,
        callback_or_session: str,
        handler: EventCallback[DirectTCPSocketAbortedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def directTCPSocketAborted(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[DirectTCPSocketAbortedEvent]: ...

    def directTCPSocketAborted(
        self,
        callback_or_session: EventCallback[DirectTCPSocketAbortedEvent]
        | str
        | None = None,
        handler: EventCallback[DirectTCPSocketAbortedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[DirectTCPSocketAbortedEvent] | Unsubscribe:
        """Fired when direct_socket.TCPSocket is aborted."""

        return cast(
            Awaitable[DirectTCPSocketAbortedEvent] | Unsubscribe,
            self._event(
                "directTCPSocketAborted",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def directTCPSocketClosed(
        self,
        callback_or_session: EventCallback[DirectTCPSocketClosedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def directTCPSocketClosed(
        self,
        callback_or_session: str,
        handler: EventCallback[DirectTCPSocketClosedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def directTCPSocketClosed(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[DirectTCPSocketClosedEvent]: ...

    def directTCPSocketClosed(
        self,
        callback_or_session: EventCallback[DirectTCPSocketClosedEvent]
        | str
        | None = None,
        handler: EventCallback[DirectTCPSocketClosedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[DirectTCPSocketClosedEvent] | Unsubscribe:
        """Fired when direct_socket.TCPSocket is closed."""

        return cast(
            Awaitable[DirectTCPSocketClosedEvent] | Unsubscribe,
            self._event(
                "directTCPSocketClosed",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def directTCPSocketChunkSent(
        self,
        callback_or_session: EventCallback[DirectTCPSocketChunkSentEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def directTCPSocketChunkSent(
        self,
        callback_or_session: str,
        handler: EventCallback[DirectTCPSocketChunkSentEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def directTCPSocketChunkSent(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[DirectTCPSocketChunkSentEvent]: ...

    def directTCPSocketChunkSent(
        self,
        callback_or_session: EventCallback[DirectTCPSocketChunkSentEvent]
        | str
        | None = None,
        handler: EventCallback[DirectTCPSocketChunkSentEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[DirectTCPSocketChunkSentEvent] | Unsubscribe:
        """Fired when data is sent to tcp direct socket stream."""

        return cast(
            Awaitable[DirectTCPSocketChunkSentEvent] | Unsubscribe,
            self._event(
                "directTCPSocketChunkSent",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def directTCPSocketChunkReceived(
        self,
        callback_or_session: EventCallback[DirectTCPSocketChunkReceivedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def directTCPSocketChunkReceived(
        self,
        callback_or_session: str,
        handler: EventCallback[DirectTCPSocketChunkReceivedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def directTCPSocketChunkReceived(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[DirectTCPSocketChunkReceivedEvent]: ...

    def directTCPSocketChunkReceived(
        self,
        callback_or_session: EventCallback[DirectTCPSocketChunkReceivedEvent]
        | str
        | None = None,
        handler: EventCallback[DirectTCPSocketChunkReceivedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[DirectTCPSocketChunkReceivedEvent] | Unsubscribe:
        """Fired when data is received from tcp direct socket stream."""

        return cast(
            Awaitable[DirectTCPSocketChunkReceivedEvent] | Unsubscribe,
            self._event(
                "directTCPSocketChunkReceived",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def directUDPSocketJoinedMulticastGroup(
        self,
        callback_or_session: EventCallback[DirectUDPSocketJoinedMulticastGroupEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def directUDPSocketJoinedMulticastGroup(
        self,
        callback_or_session: str,
        handler: EventCallback[DirectUDPSocketJoinedMulticastGroupEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def directUDPSocketJoinedMulticastGroup(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[DirectUDPSocketJoinedMulticastGroupEvent]: ...

    def directUDPSocketJoinedMulticastGroup(
        self,
        callback_or_session: EventCallback[DirectUDPSocketJoinedMulticastGroupEvent]
        | str
        | None = None,
        handler: EventCallback[DirectUDPSocketJoinedMulticastGroupEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[DirectUDPSocketJoinedMulticastGroupEvent] | Unsubscribe:
        """Wait for or subscribe to Network.directUDPSocketJoinedMulticastGroup."""

        return cast(
            Awaitable[DirectUDPSocketJoinedMulticastGroupEvent] | Unsubscribe,
            self._event(
                "directUDPSocketJoinedMulticastGroup",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def directUDPSocketLeftMulticastGroup(
        self,
        callback_or_session: EventCallback[DirectUDPSocketLeftMulticastGroupEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def directUDPSocketLeftMulticastGroup(
        self,
        callback_or_session: str,
        handler: EventCallback[DirectUDPSocketLeftMulticastGroupEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def directUDPSocketLeftMulticastGroup(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[DirectUDPSocketLeftMulticastGroupEvent]: ...

    def directUDPSocketLeftMulticastGroup(
        self,
        callback_or_session: EventCallback[DirectUDPSocketLeftMulticastGroupEvent]
        | str
        | None = None,
        handler: EventCallback[DirectUDPSocketLeftMulticastGroupEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[DirectUDPSocketLeftMulticastGroupEvent] | Unsubscribe:
        """Wait for or subscribe to Network.directUDPSocketLeftMulticastGroup."""

        return cast(
            Awaitable[DirectUDPSocketLeftMulticastGroupEvent] | Unsubscribe,
            self._event(
                "directUDPSocketLeftMulticastGroup",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def directUDPSocketCreated(
        self,
        callback_or_session: EventCallback[DirectUDPSocketCreatedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def directUDPSocketCreated(
        self,
        callback_or_session: str,
        handler: EventCallback[DirectUDPSocketCreatedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def directUDPSocketCreated(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[DirectUDPSocketCreatedEvent]: ...

    def directUDPSocketCreated(
        self,
        callback_or_session: EventCallback[DirectUDPSocketCreatedEvent]
        | str
        | None = None,
        handler: EventCallback[DirectUDPSocketCreatedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[DirectUDPSocketCreatedEvent] | Unsubscribe:
        """Fired upon direct_socket.UDPSocket creation."""

        return cast(
            Awaitable[DirectUDPSocketCreatedEvent] | Unsubscribe,
            self._event(
                "directUDPSocketCreated",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def directUDPSocketOpened(
        self,
        callback_or_session: EventCallback[DirectUDPSocketOpenedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def directUDPSocketOpened(
        self,
        callback_or_session: str,
        handler: EventCallback[DirectUDPSocketOpenedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def directUDPSocketOpened(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[DirectUDPSocketOpenedEvent]: ...

    def directUDPSocketOpened(
        self,
        callback_or_session: EventCallback[DirectUDPSocketOpenedEvent]
        | str
        | None = None,
        handler: EventCallback[DirectUDPSocketOpenedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[DirectUDPSocketOpenedEvent] | Unsubscribe:
        """Fired when direct_socket.UDPSocket connection is opened."""

        return cast(
            Awaitable[DirectUDPSocketOpenedEvent] | Unsubscribe,
            self._event(
                "directUDPSocketOpened",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def directUDPSocketAborted(
        self,
        callback_or_session: EventCallback[DirectUDPSocketAbortedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def directUDPSocketAborted(
        self,
        callback_or_session: str,
        handler: EventCallback[DirectUDPSocketAbortedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def directUDPSocketAborted(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[DirectUDPSocketAbortedEvent]: ...

    def directUDPSocketAborted(
        self,
        callback_or_session: EventCallback[DirectUDPSocketAbortedEvent]
        | str
        | None = None,
        handler: EventCallback[DirectUDPSocketAbortedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[DirectUDPSocketAbortedEvent] | Unsubscribe:
        """Fired when direct_socket.UDPSocket is aborted."""

        return cast(
            Awaitable[DirectUDPSocketAbortedEvent] | Unsubscribe,
            self._event(
                "directUDPSocketAborted",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def directUDPSocketClosed(
        self,
        callback_or_session: EventCallback[DirectUDPSocketClosedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def directUDPSocketClosed(
        self,
        callback_or_session: str,
        handler: EventCallback[DirectUDPSocketClosedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def directUDPSocketClosed(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[DirectUDPSocketClosedEvent]: ...

    def directUDPSocketClosed(
        self,
        callback_or_session: EventCallback[DirectUDPSocketClosedEvent]
        | str
        | None = None,
        handler: EventCallback[DirectUDPSocketClosedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[DirectUDPSocketClosedEvent] | Unsubscribe:
        """Fired when direct_socket.UDPSocket is closed."""

        return cast(
            Awaitable[DirectUDPSocketClosedEvent] | Unsubscribe,
            self._event(
                "directUDPSocketClosed",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def directUDPSocketChunkSent(
        self,
        callback_or_session: EventCallback[DirectUDPSocketChunkSentEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def directUDPSocketChunkSent(
        self,
        callback_or_session: str,
        handler: EventCallback[DirectUDPSocketChunkSentEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def directUDPSocketChunkSent(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[DirectUDPSocketChunkSentEvent]: ...

    def directUDPSocketChunkSent(
        self,
        callback_or_session: EventCallback[DirectUDPSocketChunkSentEvent]
        | str
        | None = None,
        handler: EventCallback[DirectUDPSocketChunkSentEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[DirectUDPSocketChunkSentEvent] | Unsubscribe:
        """Fired when message is sent to udp direct socket stream."""

        return cast(
            Awaitable[DirectUDPSocketChunkSentEvent] | Unsubscribe,
            self._event(
                "directUDPSocketChunkSent",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def directUDPSocketChunkReceived(
        self,
        callback_or_session: EventCallback[DirectUDPSocketChunkReceivedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def directUDPSocketChunkReceived(
        self,
        callback_or_session: str,
        handler: EventCallback[DirectUDPSocketChunkReceivedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def directUDPSocketChunkReceived(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[DirectUDPSocketChunkReceivedEvent]: ...

    def directUDPSocketChunkReceived(
        self,
        callback_or_session: EventCallback[DirectUDPSocketChunkReceivedEvent]
        | str
        | None = None,
        handler: EventCallback[DirectUDPSocketChunkReceivedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[DirectUDPSocketChunkReceivedEvent] | Unsubscribe:
        """Fired when message is received from udp direct socket stream."""

        return cast(
            Awaitable[DirectUDPSocketChunkReceivedEvent] | Unsubscribe,
            self._event(
                "directUDPSocketChunkReceived",
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
    def responseReceivedEarlyHints(
        self,
        callback_or_session: EventCallback[ResponseReceivedEarlyHintsEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def responseReceivedEarlyHints(
        self,
        callback_or_session: str,
        handler: EventCallback[ResponseReceivedEarlyHintsEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def responseReceivedEarlyHints(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[ResponseReceivedEarlyHintsEvent]: ...

    def responseReceivedEarlyHints(
        self,
        callback_or_session: EventCallback[ResponseReceivedEarlyHintsEvent]
        | str
        | None = None,
        handler: EventCallback[ResponseReceivedEarlyHintsEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[ResponseReceivedEarlyHintsEvent] | Unsubscribe:
        """Fired when 103 Early Hints headers is received in addition to the common response. Not every responseReceived event will have an responseReceivedEarlyHints fired. Only one responseReceivedEarlyHints may be fired for eached responseReceived event."""

        return cast(
            Awaitable[ResponseReceivedEarlyHintsEvent] | Unsubscribe,
            self._event(
                "responseReceivedEarlyHints",
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
    def policyUpdated(
        self,
        callback_or_session: EventCallback[JsonObject],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def policyUpdated(
        self,
        callback_or_session: str,
        handler: EventCallback[JsonObject],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def policyUpdated(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[JsonObject]: ...

    def policyUpdated(
        self,
        callback_or_session: EventCallback[JsonObject] | str | None = None,
        handler: EventCallback[JsonObject] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[JsonObject] | Unsubscribe:
        """Fired once security policy has been updated."""

        return self._event(
            "policyUpdated",
            cast(EventCallback[Mapping[str, object]] | str | None, callback_or_session),
            cast(EventCallback[Mapping[str, object]] | None, handler),
            session_id,
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

    @overload
    def deviceBoundSessionsAdded(
        self,
        callback_or_session: EventCallback[DeviceBoundSessionsAddedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def deviceBoundSessionsAdded(
        self,
        callback_or_session: str,
        handler: EventCallback[DeviceBoundSessionsAddedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def deviceBoundSessionsAdded(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[DeviceBoundSessionsAddedEvent]: ...

    def deviceBoundSessionsAdded(
        self,
        callback_or_session: EventCallback[DeviceBoundSessionsAddedEvent]
        | str
        | None = None,
        handler: EventCallback[DeviceBoundSessionsAddedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[DeviceBoundSessionsAddedEvent] | Unsubscribe:
        """Triggered when the initial set of device bound sessions is added."""

        return cast(
            Awaitable[DeviceBoundSessionsAddedEvent] | Unsubscribe,
            self._event(
                "deviceBoundSessionsAdded",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def deviceBoundSessionEventOccurred(
        self,
        callback_or_session: EventCallback[DeviceBoundSessionEventOccurredEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def deviceBoundSessionEventOccurred(
        self,
        callback_or_session: str,
        handler: EventCallback[DeviceBoundSessionEventOccurredEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def deviceBoundSessionEventOccurred(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[DeviceBoundSessionEventOccurredEvent]: ...

    def deviceBoundSessionEventOccurred(
        self,
        callback_or_session: EventCallback[DeviceBoundSessionEventOccurredEvent]
        | str
        | None = None,
        handler: EventCallback[DeviceBoundSessionEventOccurredEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[DeviceBoundSessionEventOccurredEvent] | Unsubscribe:
        """Triggered when a device bound session event occurs."""

        return cast(
            Awaitable[DeviceBoundSessionEventOccurredEvent] | Unsubscribe,
            self._event(
                "deviceBoundSessionEventOccurred",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )


__all__ = [
    "AdAncestry",
    "AdProvenance",
    "AdScriptIdentifier",
    "AlternateProtocolUsage",
    "AssociatedCookie",
    "AuthChallenge",
    "AuthChallengeResponse",
    "BlockPattern",
    "BlockedReason",
    "BlockedSetCookieWithReason",
    "CachedResource",
    "CanClearBrowserCacheResult",
    "CanClearBrowserCookiesResult",
    "CanEmulateNetworkConditionsResult",
    "CertificateTransparencyCompliance",
    "ChallengeEventDetails",
    "ClientSecurityState",
    "ConfigureDurableMessagesParameters",
    "ConnectTiming",
    "ConnectionType",
    "ContentEncoding",
    "ContentSecurityPolicySource",
    "ContentSecurityPolicyStatus",
    "Cookie",
    "CookieBlockedReason",
    "CookieExemptionReason",
    "CookieParam",
    "CookiePartitionKey",
    "CookiePriority",
    "CookieSameSite",
    "CookieSourceScheme",
    "CorsError",
    "CorsErrorStatus",
    "CreationEventDetails",
    "CrossOriginEmbedderPolicyStatus",
    "CrossOriginEmbedderPolicyValue",
    "CrossOriginOpenerPolicyStatus",
    "CrossOriginOpenerPolicyValue",
    "DataReceivedEvent",
    "DeleteCookiesParameters",
    "DeleteDeviceBoundSessionParameters",
    "DeviceBoundSession",
    "DeviceBoundSessionCookieCraving",
    "DeviceBoundSessionEventId",
    "DeviceBoundSessionEventOccurredEvent",
    "DeviceBoundSessionFailedRequest",
    "DeviceBoundSessionFetchResult",
    "DeviceBoundSessionInclusionRules",
    "DeviceBoundSessionKey",
    "DeviceBoundSessionUrlRule",
    "DeviceBoundSessionWithUsage",
    "DeviceBoundSessionsAddedEvent",
    "DirectSocketDnsQueryType",
    "DirectTCPSocketAbortedEvent",
    "DirectTCPSocketChunkReceivedEvent",
    "DirectTCPSocketChunkSentEvent",
    "DirectTCPSocketClosedEvent",
    "DirectTCPSocketCreatedEvent",
    "DirectTCPSocketOpenedEvent",
    "DirectTCPSocketOptions",
    "DirectUDPMessage",
    "DirectUDPSocketAbortedEvent",
    "DirectUDPSocketChunkReceivedEvent",
    "DirectUDPSocketChunkSentEvent",
    "DirectUDPSocketClosedEvent",
    "DirectUDPSocketCreatedEvent",
    "DirectUDPSocketJoinedMulticastGroupEvent",
    "DirectUDPSocketLeftMulticastGroupEvent",
    "DirectUDPSocketOpenedEvent",
    "DirectUDPSocketOptions",
    "EmulateNetworkConditionsByRuleParameters",
    "EmulateNetworkConditionsByRuleResult",
    "EmulateNetworkConditionsParameters",
    "EnableDeviceBoundSessionsParameters",
    "EnableParameters",
    "EnableReportingApiParameters",
    "ErrorReason",
    "EventSourceMessageReceivedEvent",
    "ExemptedSetCookieWithReason",
    "FetchSchemefulSiteParameters",
    "FetchSchemefulSiteResult",
    "GetAllCookiesResult",
    "GetCertificateParameters",
    "GetCertificateResult",
    "GetCookiesParameters",
    "GetCookiesResult",
    "GetRequestPostDataParameters",
    "GetRequestPostDataResult",
    "GetResponseBodyParameters",
    "GetResponseBodyResult",
    "GetSecurityIsolationStatusParameters",
    "GetSecurityIsolationStatusResult",
    "Headers",
    "IPAddressSpace",
    "Initiator",
    "LoadNetworkResourceOptions",
    "LoadNetworkResourcePageResult",
    "LoadNetworkResourceParameters",
    "LoadNetworkResourceResult",
    "LoaderId",
    "LoadingFailedEvent",
    "LoadingFinishedEvent",
    "LocalNetworkAccessRequestPolicy",
    "MonotonicTime",
    "Network",
    "NetworkConditions",
    "OverrideNetworkStateParameters",
    "PostDataEntry",
    "RefreshEventDetails",
    "RenderBlockingBehavior",
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
    "RequestServedFromCacheEvent",
    "RequestWillBeSentEvent",
    "RequestWillBeSentExtraInfoEvent",
    "ResourceChangedPriorityEvent",
    "ResourcePriority",
    "ResourceTiming",
    "ResourceType",
    "Response",
    "ResponseReceivedEarlyHintsEvent",
    "ResponseReceivedEvent",
    "ResponseReceivedExtraInfoEvent",
    "SearchInResponseBodyParameters",
    "SearchInResponseBodyResult",
    "SecurityDetails",
    "SecurityIsolationStatus",
    "ServiceWorkerResponseSource",
    "ServiceWorkerRouterInfo",
    "ServiceWorkerRouterSource",
    "SetAcceptedEncodingsParameters",
    "SetAttachDebugStackParameters",
    "SetBlockedURLsParameters",
    "SetBypassServiceWorkerParameters",
    "SetCacheDisabledParameters",
    "SetCookieBlockedReason",
    "SetCookieControlsParameters",
    "SetCookieParameters",
    "SetCookieResult",
    "SetCookiesParameters",
    "SetExtraHTTPHeadersParameters",
    "SetUserAgentOverrideParameters",
    "SignedCertificateTimestamp",
    "SignedExchangeError",
    "SignedExchangeErrorField",
    "SignedExchangeHeader",
    "SignedExchangeInfo",
    "SignedExchangeReceivedEvent",
    "SignedExchangeSignature",
    "StreamResourceContentParameters",
    "StreamResourceContentResult",
    "TerminationEventDetails",
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
