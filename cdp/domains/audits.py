"""Generated bindings for the CDP Audits domain. Do not edit manually."""

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
    from . import runtime as Runtime


class AffectedCookie(TypedDict):
    name: str
    path: str
    domain: str


class AffectedRequest(TypedDict):
    requestId: NotRequired[Network.RequestId]
    url: str


class AffectedFrame(TypedDict):
    frameId: Page.FrameId


CookieExclusionReason: TypeAlias = Literal[
    "ExcludeSameSiteUnspecifiedTreatedAsLax",
    "ExcludeSameSiteNoneInsecure",
    "ExcludeSameSiteLax",
    "ExcludeSameSiteStrict",
    "ExcludeDomainNonASCII",
    "ExcludeThirdPartyCookieBlockedInFirstPartySet",
    "ExcludeThirdPartyPhaseout",
    "ExcludePortMismatch",
    "ExcludeSchemeMismatch",
]

CookieWarningReason: TypeAlias = Literal[
    "WarnSameSiteUnspecifiedCrossSiteContext",
    "WarnSameSiteNoneInsecure",
    "WarnSameSiteUnspecifiedLaxAllowUnsafe",
    "WarnSameSiteStrictLaxDowngradeStrict",
    "WarnSameSiteStrictCrossDowngradeStrict",
    "WarnSameSiteStrictCrossDowngradeLax",
    "WarnSameSiteLaxCrossDowngradeStrict",
    "WarnSameSiteLaxCrossDowngradeLax",
    "WarnAttributeValueExceedsMaxSize",
    "WarnDomainNonASCII",
    "WarnThirdPartyPhaseout",
    "WarnCrossSiteRedirectDowngradeChangesInclusion",
    "WarnDeprecationTrialMetadata",
    "WarnThirdPartyCookieHeuristic",
]

CookieOperation: TypeAlias = Literal["SetCookie", "ReadCookie"]

InsightType: TypeAlias = Literal["GitHubResource", "GracePeriod", "Heuristics"]


class CookieIssueInsight(TypedDict):
    type: InsightType
    tableEntryUrl: NotRequired[str]


class CookieIssueDetails(TypedDict):
    cookie: NotRequired[AffectedCookie]
    rawCookieLine: NotRequired[str]
    cookieWarningReasons: list[CookieWarningReason]
    cookieExclusionReasons: list[CookieExclusionReason]
    operation: CookieOperation
    siteForCookies: NotRequired[str]
    cookieUrl: NotRequired[str]
    request: NotRequired[AffectedRequest]
    insight: NotRequired[CookieIssueInsight]


PerformanceIssueType: TypeAlias = Literal["DocumentCookie"]


class PerformanceIssueDetails(TypedDict):
    performanceIssueType: PerformanceIssueType
    sourceCodeLocation: NotRequired[SourceCodeLocation]


MixedContentResolutionStatus: TypeAlias = Literal[
    "MixedContentBlocked", "MixedContentAutomaticallyUpgraded", "MixedContentWarning"
]

MixedContentResourceType: TypeAlias = Literal[
    "Audio",
    "Beacon",
    "CSPReport",
    "Download",
    "EventSource",
    "Favicon",
    "Font",
    "Form",
    "Frame",
    "Image",
    "Import",
    "JSON",
    "Manifest",
    "Ping",
    "PluginData",
    "PluginResource",
    "Prefetch",
    "Resource",
    "Script",
    "ServiceWorker",
    "SharedWorker",
    "SpeculationRules",
    "Stylesheet",
    "Track",
    "Video",
    "Worker",
    "XMLHttpRequest",
    "XSLT",
]


class MixedContentIssueDetails(TypedDict):
    resourceType: NotRequired[MixedContentResourceType]
    resolutionStatus: MixedContentResolutionStatus
    insecureURL: str
    mainResourceURL: str
    request: NotRequired[AffectedRequest]
    frame: NotRequired[AffectedFrame]


BlockedByResponseReason: TypeAlias = Literal[
    "CoepFrameResourceNeedsCoepHeader",
    "CoopSandboxedIFrameCannotNavigateToCoopPage",
    "CorpNotSameOrigin",
    "CorpNotSameOriginAfterDefaultedToSameOriginByCoep",
    "CorpNotSameOriginAfterDefaultedToSameOriginByDip",
    "CorpNotSameOriginAfterDefaultedToSameOriginByCoepAndDip",
    "CorpNotSameSite",
    "SRIMessageSignatureMismatch",
]


class BlockedByResponseIssueDetails(TypedDict):
    request: AffectedRequest
    parentFrame: NotRequired[AffectedFrame]
    blockedFrame: NotRequired[AffectedFrame]
    reason: BlockedByResponseReason


HeavyAdResolutionStatus: TypeAlias = Literal["HeavyAdBlocked", "HeavyAdWarning"]

HeavyAdReason: TypeAlias = Literal["NetworkTotalLimit", "CpuTotalLimit", "CpuPeakLimit"]


class HeavyAdIssueDetails(TypedDict):
    resolution: HeavyAdResolutionStatus
    reason: HeavyAdReason
    frame: AffectedFrame


ContentSecurityPolicyViolationType: TypeAlias = Literal[
    "kInlineViolation",
    "kEvalViolation",
    "kURLViolation",
    "kSRIViolation",
    "kTrustedTypesSinkViolation",
    "kTrustedTypesPolicyViolation",
    "kWasmEvalViolation",
]


class SourceCodeLocation(TypedDict):
    scriptId: NotRequired[Runtime.ScriptId]
    url: str
    lineNumber: int
    columnNumber: int


class ContentSecurityPolicyIssueDetails(TypedDict):
    blockedURL: NotRequired[str]
    violatedDirective: str
    isReportOnly: bool
    contentSecurityPolicyViolationType: ContentSecurityPolicyViolationType
    frameAncestor: NotRequired[AffectedFrame]
    sourceCodeLocation: NotRequired[SourceCodeLocation]
    violatingNodeId: NotRequired[DOM.BackendNodeId]


SharedArrayBufferIssueType: TypeAlias = Literal["TransferIssue", "CreationIssue"]


class SharedArrayBufferIssueDetails(TypedDict):
    sourceCodeLocation: SourceCodeLocation
    isWarning: bool
    type: SharedArrayBufferIssueType


class CorsIssueDetails(TypedDict):
    corsErrorStatus: Network.CorsErrorStatus
    isWarning: bool
    request: AffectedRequest
    location: NotRequired[SourceCodeLocation]
    initiatorOrigin: NotRequired[str]
    resourceIPAddressSpace: NotRequired[Network.IPAddressSpace]
    clientSecurityState: NotRequired[Network.ClientSecurityState]


SharedDictionaryError: TypeAlias = Literal[
    "UseErrorCrossOriginNoCorsRequest",
    "UseErrorDictionaryLoadFailure",
    "UseErrorMatchingDictionaryNotUsed",
    "UseErrorUnexpectedContentDictionaryHeader",
    "WriteErrorCossOriginNoCorsRequest",
    "WriteErrorDisallowedBySettings",
    "WriteErrorExpiredResponse",
    "WriteErrorFeatureDisabled",
    "WriteErrorInsufficientResources",
    "WriteErrorInvalidMatchField",
    "WriteErrorInvalidStructuredHeader",
    "WriteErrorInvalidTTLField",
    "WriteErrorNavigationRequest",
    "WriteErrorNoMatchField",
    "WriteErrorNonIntegerTTLField",
    "WriteErrorNonListMatchDestField",
    "WriteErrorNonSecureContext",
    "WriteErrorNonStringIdField",
    "WriteErrorNonStringInMatchDestList",
    "WriteErrorInvalidMatchDestList",
    "WriteErrorNonStringMatchField",
    "WriteErrorNonTokenTypeField",
    "WriteErrorRequestAborted",
    "WriteErrorShuttingDown",
    "WriteErrorTooLongIdField",
    "WriteErrorUnsupportedType",
]

SRIMessageSignatureError: TypeAlias = Literal[
    "MissingSignatureHeader",
    "MissingSignatureInputHeader",
    "InvalidSignatureHeader",
    "InvalidSignatureInputHeader",
    "SignatureHeaderValueIsNotByteSequence",
    "SignatureHeaderValueIsParameterized",
    "SignatureHeaderValueIsIncorrectLength",
    "SignatureInputHeaderMissingLabel",
    "SignatureInputHeaderValueNotInnerList",
    "SignatureInputHeaderValueMissingComponents",
    "SignatureInputHeaderInvalidComponentType",
    "SignatureInputHeaderInvalidComponentName",
    "SignatureInputHeaderInvalidHeaderComponentParameter",
    "SignatureInputHeaderInvalidDerivedComponentParameter",
    "SignatureInputHeaderKeyIdLength",
    "SignatureInputHeaderInvalidParameter",
    "SignatureInputHeaderMissingRequiredParameters",
    "ValidationFailedSignatureExpired",
    "ValidationFailedInvalidLength",
    "ValidationFailedSignatureMismatch",
    "ValidationFailedIntegrityMismatch",
    "SignatureBaseUnknownDerivedComponent",
    "SignatureBaseMissingHeader",
    "SignatureBaseInvalidUnencodedDigest",
    "SignatureBaseUnsupportedComponent",
]

UnencodedDigestError: TypeAlias = Literal[
    "MalformedDictionary",
    "UnknownAlgorithm",
    "IncorrectDigestType",
    "IncorrectDigestLength",
]

ConnectionAllowlistError: TypeAlias = Literal[
    "InvalidHeader",
    "MoreThanOneList",
    "ItemNotInnerList",
    "InvalidAllowlistItemType",
    "ReportingEndpointNotToken",
    "InvalidUrlPattern",
]


class QuirksModeIssueDetails(TypedDict):
    isLimitedQuirksMode: bool
    documentNodeId: DOM.BackendNodeId
    url: str
    frameId: Page.FrameId
    loaderId: Network.LoaderId


class NavigatorUserAgentIssueDetails(TypedDict):
    url: str
    location: NotRequired[SourceCodeLocation]


class SharedDictionaryIssueDetails(TypedDict):
    sharedDictionaryError: SharedDictionaryError
    request: AffectedRequest


class SRIMessageSignatureIssueDetails(TypedDict):
    error: SRIMessageSignatureError
    signatureBase: str
    integrityAssertions: list[str]
    request: AffectedRequest


class UnencodedDigestIssueDetails(TypedDict):
    error: UnencodedDigestError
    request: AffectedRequest


class ConnectionAllowlistIssueDetails(TypedDict):
    error: ConnectionAllowlistError
    request: AffectedRequest


GenericIssueErrorType: TypeAlias = Literal[
    "FormLabelForNameError",
    "FormDuplicateIdForInputError",
    "FormInputWithNoLabelError",
    "FormAutocompleteAttributeEmptyError",
    "FormEmptyIdAndNameAttributesForInputError",
    "FormAriaLabelledByToNonExistingIdError",
    "FormInputAssignedAutocompleteValueToIdOrNameAttributeError",
    "FormLabelHasNeitherForNorNestedInputError",
    "FormLabelForMatchesNonExistingIdError",
    "FormInputHasWrongButWellIntendedAutocompleteValueError",
    "ResponseWasBlockedByORB",
    "NavigationEntryMarkedSkippable",
    "BackUINavigationWouldSkipAd",
    "AutofillAndManualTextPolicyControlledFeaturesInfo",
    "AutofillPolicyControlledFeatureInfo",
    "ManualTextPolicyControlledFeatureInfo",
    "FormModelContextParameterMissingTitleAndDescription",
    "FormModelContextMissingToolName",
    "FormModelContextMissingToolDescription",
    "FormModelContextRequiredParameterMissingName",
    "FormModelContextParameterMissingName",
]


class GenericIssueDetails(TypedDict):
    errorType: GenericIssueErrorType
    frameId: NotRequired[Page.FrameId]
    violatingNodeId: NotRequired[DOM.BackendNodeId]
    violatingNodeAttribute: NotRequired[str]
    request: NotRequired[AffectedRequest]


class DeprecationIssueDetails(TypedDict):
    affectedFrame: NotRequired[AffectedFrame]
    sourceCodeLocation: SourceCodeLocation
    type: str


class BounceTrackingIssueDetails(TypedDict):
    trackingSites: list[str]


class CookieDeprecationMetadataIssueDetails(TypedDict):
    allowedSites: list[str]
    optOutPercentage: float
    isOptOutTopLevel: bool
    operation: CookieOperation


ClientHintIssueReason: TypeAlias = Literal[
    "MetaTagAllowListInvalidOrigin", "MetaTagModifiedHTML"
]


class FederatedAuthRequestIssueDetails(TypedDict):
    federatedAuthRequestIssueReason: FederatedAuthRequestIssueReason


FederatedAuthRequestIssueReason: TypeAlias = Literal[
    "ShouldEmbargo",
    "TooManyRequests",
    "WellKnownHttpNotFound",
    "WellKnownNoResponse",
    "WellKnownBlockedByConnectionAllowlist",
    "WellKnownInvalidResponse",
    "WellKnownListEmpty",
    "WellKnownInvalidContentType",
    "ConfigNotInWellKnown",
    "WellKnownTooBig",
    "ConfigHttpNotFound",
    "ConfigNoResponse",
    "ConfigBlockedByConnectionAllowlist",
    "ConfigInvalidResponse",
    "ConfigInvalidContentType",
    "IdpNotPotentiallyTrustworthy",
    "DisabledInSettings",
    "DisabledInFlags",
    "ErrorFetchingSignin",
    "InvalidSigninResponse",
    "AccountsHttpNotFound",
    "AccountsNoResponse",
    "AccountsBlockedByConnectionAllowlist",
    "AccountsInvalidResponse",
    "AccountsListEmpty",
    "AccountsInvalidContentType",
    "IdTokenHttpNotFound",
    "IdTokenNoResponse",
    "IdTokenBlockedByConnectionAllowlist",
    "IdTokenInvalidResponse",
    "IdTokenIdpErrorResponse",
    "IdTokenCrossSiteIdpErrorResponse",
    "IdTokenInvalidRequest",
    "IdTokenInvalidContentType",
    "ErrorIdToken",
    "Canceled",
    "RpPageNotVisible",
    "SilentMediationFailure",
    "NotSignedInWithIdp",
    "MissingTransientUserActivation",
    "ReplacedByActiveMode",
    "RelyingPartyOriginIsOpaque",
    "TypeNotMatching",
    "UiDismissedNoEmbargo",
    "CorsError",
    "SuppressedBySegmentationPlatform",
]


class FederatedAuthUserInfoRequestIssueDetails(TypedDict):
    federatedAuthUserInfoRequestIssueReason: FederatedAuthUserInfoRequestIssueReason


FederatedAuthUserInfoRequestIssueReason: TypeAlias = Literal[
    "NotSameOrigin",
    "NotIframe",
    "NotPotentiallyTrustworthy",
    "NoApiPermission",
    "NotSignedInWithIdp",
    "NoAccountSharingPermission",
    "InvalidConfigOrWellKnown",
    "InvalidAccountsResponse",
    "NoReturningUserFromFetchedAccounts",
]


class EmailVerificationRequestIssueDetails(TypedDict):
    emailVerificationRequestIssueReason: EmailVerificationRequestIssueReason


EmailVerificationRequestIssueReason: TypeAlias = Literal[
    "InvalidEmail",
    "DnsFetchFailed",
    "DnsInvalidRecord",
    "WellKnownHttpNotFound",
    "WellKnownNoResponse",
    "WellKnownInvalidResponse",
    "WellKnownListEmpty",
    "WellKnownInvalidContentType",
    "WellKnownMissingIssuanceEndpoint",
    "WellKnownIssuanceEndpointCrossOrigin",
    "WellKnownUnsupportedSigningAlgorithm",
    "TokenHttpNotFound",
    "TokenNoResponse",
    "TokenInvalidResponse",
    "TokenInvalidContentType",
    "TokenMalformedSdJwt",
    "TokenInvalidSdJwt",
    "KeyBindingSigningFailed",
    "RpOriginIsOpaque",
    "WellKnownMissingAccountsEndpoint",
    "UserLoggedOut",
    "WellKnownAccountsEndpointCrossOrigin",
    "AccountsHttpNotFound",
    "AccountsNoResponse",
    "AccountsInvalidResponse",
    "AccountsInvalidContentType",
    "AccountsEmptyList",
    "EmailVerificationWellKnownHttpNotFound",
    "EmailVerificationWellKnownNoResponse",
    "EmailVerificationWellKnownInvalidResponse",
    "EmailVerificationWellKnownInvalidContentType",
    "JwksHttpNotFound",
    "JwksInvalidResponse",
    "TokenVerificationSdJwtUnsupportedHeaderAlg",
    "TokenVerificationSdJwtInvalidTyp",
    "TokenVerificationSdJwtMissingIss",
    "TokenVerificationSdJwtMissingIat",
    "TokenVerificationSdJwtMissingCnf",
    "TokenVerificationSdJwtMissingEmail",
    "TokenVerificationSdJwtInvalidIssuedAt",
    "TokenVerificationSdJwtInvalidIssuer",
    "TokenVerificationSdJwtJwksMissingKeys",
    "TokenVerificationSdJwtSignatureFailed",
    "TokenVerificationSdJwtInvalidEmailVerified",
    "TokenVerificationSdJwtInvalidEmail",
    "TokenVerificationSdJwtInvalidHolderKey",
    "TokenVerificationKbInvalidTyp",
    "TokenVerificationKbMissingAud",
    "TokenVerificationKbMissingNonce",
    "TokenVerificationKbMissingIat",
    "TokenVerificationKbMissingSdHash",
    "TokenVerificationKbInvalidIssuedAt",
    "TokenVerificationKbInvalidAudience",
    "TokenVerificationKbInvalidNonce",
    "TokenVerificationKbInvalidSdHash",
    "TokenVerificationKbMissingCnf",
    "TokenVerificationKbSignatureFailed",
]


class ClientHintIssueDetails(TypedDict):
    sourceCodeLocation: SourceCodeLocation
    clientHintIssueReason: ClientHintIssueReason


class FailedRequestInfo(TypedDict):
    url: str
    failureMessage: str
    requestId: NotRequired[Network.RequestId]


PartitioningBlobURLInfo: TypeAlias = Literal[
    "BlockedCrossPartitionFetching", "EnforceNoopenerForNavigation"
]


class PartitioningBlobURLIssueDetails(TypedDict):
    url: str
    partitioningBlobURLInfo: PartitioningBlobURLInfo


ElementAccessibilityIssueReason: TypeAlias = Literal[
    "DisallowedSelectChild",
    "DisallowedOptGroupChild",
    "NonPhrasingContentOptionChild",
    "InteractiveContentOptionChild",
    "InteractiveContentLegendChild",
    "InteractiveContentSummaryDescendant",
]


class ElementAccessibilityIssueDetails(TypedDict):
    nodeId: DOM.BackendNodeId
    elementAccessibilityIssueReason: ElementAccessibilityIssueReason
    hasDisallowedAttributes: bool


StyleSheetLoadingIssueReason: TypeAlias = Literal["LateImportRule", "RequestFailed"]


class StylesheetLoadingIssueDetails(TypedDict):
    sourceCodeLocation: SourceCodeLocation
    styleSheetLoadingIssueReason: StyleSheetLoadingIssueReason
    failedRequestInfo: NotRequired[FailedRequestInfo]


PropertyRuleIssueReason: TypeAlias = Literal[
    "InvalidSyntax", "InvalidInitialValue", "InvalidInherits", "InvalidName"
]


class PropertyRuleIssueDetails(TypedDict):
    sourceCodeLocation: SourceCodeLocation
    propertyRuleIssueReason: PropertyRuleIssueReason
    propertyValue: NotRequired[str]


UserReidentificationIssueType: TypeAlias = Literal[
    "BlockedFrameNavigation", "BlockedSubresource", "NoisedCanvasReadback"
]


class UserReidentificationIssueDetails(TypedDict):
    type: UserReidentificationIssueType
    request: NotRequired[AffectedRequest]
    sourceCodeLocation: NotRequired[SourceCodeLocation]


PermissionElementIssueType: TypeAlias = Literal[
    "InvalidType",
    "FencedFrameDisallowed",
    "CspFrameAncestorsMissing",
    "PermissionsPolicyBlocked",
    "PaddingRightUnsupported",
    "PaddingBottomUnsupported",
    "InsetBoxShadowUnsupported",
    "RequestInProgress",
    "UntrustedEvent",
    "RegistrationFailed",
    "TypeNotSupported",
    "InvalidTypeActivation",
    "SecurityChecksFailed",
    "ActivationDisabled",
    "GeolocationDeprecated",
    "InvalidDisplayStyle",
    "NonOpaqueColor",
    "LowContrast",
    "FontSizeTooSmall",
    "FontSizeTooLarge",
    "InvalidSizeValue",
    "NonSecureContext",
    "MissingTransientUserActivation",
]


class PermissionElementIssueDetails(TypedDict):
    issueType: PermissionElementIssueType
    type: NotRequired[str]
    nodeId: NotRequired[DOM.BackendNodeId]
    isWarning: NotRequired[bool]
    permissionName: NotRequired[str]
    occluderNodeInfo: NotRequired[str]
    occluderParentNodeInfo: NotRequired[str]
    disableReason: NotRequired[str]


class SelectivePermissionsInterventionIssueDetails(TypedDict):
    apiName: str
    adAncestry: Network.AdAncestry
    stackTrace: NotRequired[Runtime.StackTrace]


class LazyLoadImageIssueDetails(TypedDict):
    nodeId: DOM.BackendNodeId
    url: str
    frameId: Page.FrameId


InspectorIssueCode: TypeAlias = Literal[
    "CookieIssue",
    "MixedContentIssue",
    "BlockedByResponseIssue",
    "HeavyAdIssue",
    "ContentSecurityPolicyIssue",
    "SharedArrayBufferIssue",
    "CorsIssue",
    "QuirksModeIssue",
    "PartitioningBlobURLIssue",
    "NavigatorUserAgentIssue",
    "GenericIssue",
    "DeprecationIssue",
    "ClientHintIssue",
    "FederatedAuthRequestIssue",
    "BounceTrackingIssue",
    "CookieDeprecationMetadataIssue",
    "StylesheetLoadingIssue",
    "FederatedAuthUserInfoRequestIssue",
    "PropertyRuleIssue",
    "SharedDictionaryIssue",
    "ElementAccessibilityIssue",
    "SRIMessageSignatureIssue",
    "UnencodedDigestIssue",
    "ConnectionAllowlistIssue",
    "UserReidentificationIssue",
    "PermissionElementIssue",
    "PerformanceIssue",
    "SelectivePermissionsInterventionIssue",
    "EmailVerificationRequestIssue",
    "LazyLoadImageIssue",
]


class InspectorIssueDetails(TypedDict):
    cookieIssueDetails: NotRequired[CookieIssueDetails]
    mixedContentIssueDetails: NotRequired[MixedContentIssueDetails]
    blockedByResponseIssueDetails: NotRequired[BlockedByResponseIssueDetails]
    heavyAdIssueDetails: NotRequired[HeavyAdIssueDetails]
    contentSecurityPolicyIssueDetails: NotRequired[ContentSecurityPolicyIssueDetails]
    sharedArrayBufferIssueDetails: NotRequired[SharedArrayBufferIssueDetails]
    corsIssueDetails: NotRequired[CorsIssueDetails]
    quirksModeIssueDetails: NotRequired[QuirksModeIssueDetails]
    partitioningBlobURLIssueDetails: NotRequired[PartitioningBlobURLIssueDetails]
    navigatorUserAgentIssueDetails: NotRequired[NavigatorUserAgentIssueDetails]
    genericIssueDetails: NotRequired[GenericIssueDetails]
    deprecationIssueDetails: NotRequired[DeprecationIssueDetails]
    clientHintIssueDetails: NotRequired[ClientHintIssueDetails]
    federatedAuthRequestIssueDetails: NotRequired[FederatedAuthRequestIssueDetails]
    bounceTrackingIssueDetails: NotRequired[BounceTrackingIssueDetails]
    cookieDeprecationMetadataIssueDetails: NotRequired[
        CookieDeprecationMetadataIssueDetails
    ]
    stylesheetLoadingIssueDetails: NotRequired[StylesheetLoadingIssueDetails]
    propertyRuleIssueDetails: NotRequired[PropertyRuleIssueDetails]
    federatedAuthUserInfoRequestIssueDetails: NotRequired[
        FederatedAuthUserInfoRequestIssueDetails
    ]
    sharedDictionaryIssueDetails: NotRequired[SharedDictionaryIssueDetails]
    elementAccessibilityIssueDetails: NotRequired[ElementAccessibilityIssueDetails]
    sriMessageSignatureIssueDetails: NotRequired[SRIMessageSignatureIssueDetails]
    unencodedDigestIssueDetails: NotRequired[UnencodedDigestIssueDetails]
    connectionAllowlistIssueDetails: NotRequired[ConnectionAllowlistIssueDetails]
    userReidentificationIssueDetails: NotRequired[UserReidentificationIssueDetails]
    permissionElementIssueDetails: NotRequired[PermissionElementIssueDetails]
    performanceIssueDetails: NotRequired[PerformanceIssueDetails]
    selectivePermissionsInterventionIssueDetails: NotRequired[
        SelectivePermissionsInterventionIssueDetails
    ]
    emailVerificationRequestIssueDetails: NotRequired[
        EmailVerificationRequestIssueDetails
    ]
    lazyLoadImageIssueDetails: NotRequired[LazyLoadImageIssueDetails]


IssueId: TypeAlias = str


class InspectorIssue(TypedDict):
    code: InspectorIssueCode
    details: InspectorIssueDetails
    issueId: NotRequired[IssueId]


class GetEncodedResponseParameters(TypedDict):
    requestId: Network.RequestId
    encoding: Literal["webp", "jpeg", "png"]
    quality: NotRequired[float]
    sizeOnly: NotRequired[bool]


class GetEncodedResponseResult(TypedDict):
    body: NotRequired[str]
    originalSize: int
    encodedSize: int


class CheckFormsIssuesResult(TypedDict):
    formIssues: list[GenericIssueDetails]


class IssueAddedEvent(TypedDict):
    issue: InspectorIssue


class Audits(BaseDomain):
    """Audits domain allows investigation of page violations and possible improvements."""

    domain_name = "Audits"

    @overload
    async def getEncodedResponse(
        self,
        params: GetEncodedResponseParameters,
        session_id: str | None = None,
    ) -> GetEncodedResponseResult: ...

    @overload
    async def getEncodedResponse(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[GetEncodedResponseParameters],
    ) -> GetEncodedResponseResult: ...

    async def getEncodedResponse(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> GetEncodedResponseResult:
        """Returns the response body and size if it were re-encoded with the specified settings. Only applies to images."""

        return cast(
            GetEncodedResponseResult,
            await self._command("getEncodedResponse", params, session_id, kwargs),
        )

    async def disable(
        self,
        session_id: str | None = None,
    ) -> JsonObject:
        """Disables issues domain, prevents further issues from being reported to the client."""

        return await self._command("disable", None, session_id, {})

    async def enable(
        self,
        session_id: str | None = None,
    ) -> JsonObject:
        """Enables issues domain, sends the issues collected so far to the client by means of the `issueAdded` event."""

        return await self._command("enable", None, session_id, {})

    async def checkFormsIssues(
        self,
        session_id: str | None = None,
    ) -> CheckFormsIssuesResult:
        """Runs the form issues check for the target page. Found issues are reported using Audits.issueAdded event."""

        return cast(
            CheckFormsIssuesResult,
            await self._command("checkFormsIssues", None, session_id, {}),
        )

    @overload
    def issueAdded(
        self,
        callback_or_session: EventCallback[IssueAddedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def issueAdded(
        self,
        callback_or_session: str,
        handler: EventCallback[IssueAddedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def issueAdded(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[IssueAddedEvent]: ...

    def issueAdded(
        self,
        callback_or_session: EventCallback[IssueAddedEvent] | str | None = None,
        handler: EventCallback[IssueAddedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[IssueAddedEvent] | Unsubscribe:
        """Wait for or subscribe to Audits.issueAdded."""

        return cast(
            Awaitable[IssueAddedEvent] | Unsubscribe,
            self._event(
                "issueAdded",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )


__all__ = [
    "AffectedCookie",
    "AffectedFrame",
    "AffectedRequest",
    "Audits",
    "BlockedByResponseIssueDetails",
    "BlockedByResponseReason",
    "BounceTrackingIssueDetails",
    "CheckFormsIssuesResult",
    "ClientHintIssueDetails",
    "ClientHintIssueReason",
    "ConnectionAllowlistError",
    "ConnectionAllowlistIssueDetails",
    "ContentSecurityPolicyIssueDetails",
    "ContentSecurityPolicyViolationType",
    "CookieDeprecationMetadataIssueDetails",
    "CookieExclusionReason",
    "CookieIssueDetails",
    "CookieIssueInsight",
    "CookieOperation",
    "CookieWarningReason",
    "CorsIssueDetails",
    "DeprecationIssueDetails",
    "ElementAccessibilityIssueDetails",
    "ElementAccessibilityIssueReason",
    "EmailVerificationRequestIssueDetails",
    "EmailVerificationRequestIssueReason",
    "FailedRequestInfo",
    "FederatedAuthRequestIssueDetails",
    "FederatedAuthRequestIssueReason",
    "FederatedAuthUserInfoRequestIssueDetails",
    "FederatedAuthUserInfoRequestIssueReason",
    "GenericIssueDetails",
    "GenericIssueErrorType",
    "GetEncodedResponseParameters",
    "GetEncodedResponseResult",
    "HeavyAdIssueDetails",
    "HeavyAdReason",
    "HeavyAdResolutionStatus",
    "InsightType",
    "InspectorIssue",
    "InspectorIssueCode",
    "InspectorIssueDetails",
    "IssueAddedEvent",
    "IssueId",
    "LazyLoadImageIssueDetails",
    "MixedContentIssueDetails",
    "MixedContentResolutionStatus",
    "MixedContentResourceType",
    "NavigatorUserAgentIssueDetails",
    "PartitioningBlobURLInfo",
    "PartitioningBlobURLIssueDetails",
    "PerformanceIssueDetails",
    "PerformanceIssueType",
    "PermissionElementIssueDetails",
    "PermissionElementIssueType",
    "PropertyRuleIssueDetails",
    "PropertyRuleIssueReason",
    "QuirksModeIssueDetails",
    "SRIMessageSignatureError",
    "SRIMessageSignatureIssueDetails",
    "SelectivePermissionsInterventionIssueDetails",
    "SharedArrayBufferIssueDetails",
    "SharedArrayBufferIssueType",
    "SharedDictionaryError",
    "SharedDictionaryIssueDetails",
    "SourceCodeLocation",
    "StyleSheetLoadingIssueReason",
    "StylesheetLoadingIssueDetails",
    "UnencodedDigestError",
    "UnencodedDigestIssueDetails",
    "UserReidentificationIssueDetails",
    "UserReidentificationIssueType",
]
