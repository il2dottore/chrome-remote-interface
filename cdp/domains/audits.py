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
    requestId: Network.RequestId
    url: NotRequired[str]


class AffectedFrame(TypedDict):
    frameId: Page.FrameId


CookieExclusionReason: TypeAlias = Literal[
    "ExcludeSameSiteUnspecifiedTreatedAsLax",
    "ExcludeSameSiteNoneInsecure",
    "ExcludeSameSiteLax",
    "ExcludeSameSiteStrict",
    "ExcludeInvalidSameParty",
    "ExcludeSamePartyCrossPartyContext",
    "ExcludeDomainNonASCII",
    "ExcludeThirdPartyCookieBlockedInFirstPartySet",
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
]

CookieOperation: TypeAlias = Literal["SetCookie", "ReadCookie"]


class CookieIssueDetails(TypedDict):
    cookie: NotRequired[AffectedCookie]
    rawCookieLine: NotRequired[str]
    cookieWarningReasons: list[CookieWarningReason]
    cookieExclusionReasons: list[CookieExclusionReason]
    operation: CookieOperation
    siteForCookies: NotRequired[str]
    cookieUrl: NotRequired[str]
    request: NotRequired[AffectedRequest]


MixedContentResolutionStatus: TypeAlias = Literal[
    "MixedContentBlocked", "MixedContentAutomaticallyUpgraded", "MixedContentWarning"
]

MixedContentResourceType: TypeAlias = Literal[
    "AttributionSrc",
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
    "Manifest",
    "Ping",
    "PluginData",
    "PluginResource",
    "Prefetch",
    "Resource",
    "Script",
    "ServiceWorker",
    "SharedWorker",
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
    "CorpNotSameSite",
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


class LowTextContrastIssueDetails(TypedDict):
    violatingNodeId: DOM.BackendNodeId
    violatingNodeSelector: str
    contrastRatio: float
    thresholdAA: float
    thresholdAAA: float
    fontSize: str
    fontWeight: str


class CorsIssueDetails(TypedDict):
    corsErrorStatus: Network.CorsErrorStatus
    isWarning: bool
    request: AffectedRequest
    location: NotRequired[SourceCodeLocation]
    initiatorOrigin: NotRequired[str]
    resourceIPAddressSpace: NotRequired[Network.IPAddressSpace]
    clientSecurityState: NotRequired[Network.ClientSecurityState]


AttributionReportingIssueType: TypeAlias = Literal[
    "PermissionPolicyDisabled",
    "UntrustworthyReportingOrigin",
    "InsecureContext",
    "InvalidHeader",
    "InvalidRegisterTriggerHeader",
    "SourceAndTriggerHeaders",
    "SourceIgnored",
    "TriggerIgnored",
    "OsSourceIgnored",
    "OsTriggerIgnored",
    "InvalidRegisterOsSourceHeader",
    "InvalidRegisterOsTriggerHeader",
    "WebAndOsHeaders",
    "NoWebOrOsSupport",
    "NavigationRegistrationWithoutTransientUserActivation",
]


class AttributionReportingIssueDetails(TypedDict):
    violationType: AttributionReportingIssueType
    request: NotRequired[AffectedRequest]
    violatingNodeId: NotRequired[DOM.BackendNodeId]
    invalidParameter: NotRequired[str]


class QuirksModeIssueDetails(TypedDict):
    isLimitedQuirksMode: bool
    documentNodeId: DOM.BackendNodeId
    url: str
    frameId: Page.FrameId
    loaderId: Network.LoaderId


class NavigatorUserAgentIssueDetails(TypedDict):
    url: str
    location: NotRequired[SourceCodeLocation]


GenericIssueErrorType: TypeAlias = Literal[
    "CrossOriginPortalPostMessageError",
    "FormLabelForNameError",
    "FormDuplicateIdForInputError",
    "FormInputWithNoLabelError",
    "FormAutocompleteAttributeEmptyError",
    "FormEmptyIdAndNameAttributesForInputError",
    "FormAriaLabelledByToNonExistingId",
    "FormInputAssignedAutocompleteValueToIdOrNameAttributeError",
    "FormLabelHasNeitherForNorNestedInput",
    "FormLabelForMatchesNonExistingIdError",
    "FormInputHasWrongButWellIntendedAutocompleteValueError",
    "ResponseWasBlockedByORB",
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
    "WellKnownInvalidResponse",
    "WellKnownListEmpty",
    "WellKnownInvalidContentType",
    "ConfigNotInWellKnown",
    "WellKnownTooBig",
    "ConfigHttpNotFound",
    "ConfigNoResponse",
    "ConfigInvalidResponse",
    "ConfigInvalidContentType",
    "ClientMetadataHttpNotFound",
    "ClientMetadataNoResponse",
    "ClientMetadataInvalidResponse",
    "ClientMetadataInvalidContentType",
    "DisabledInSettings",
    "ErrorFetchingSignin",
    "InvalidSigninResponse",
    "AccountsHttpNotFound",
    "AccountsNoResponse",
    "AccountsInvalidResponse",
    "AccountsListEmpty",
    "AccountsInvalidContentType",
    "IdTokenHttpNotFound",
    "IdTokenNoResponse",
    "IdTokenInvalidResponse",
    "IdTokenInvalidRequest",
    "IdTokenInvalidContentType",
    "ErrorIdToken",
    "Canceled",
    "RpPageNotVisible",
    "SilentMediationFailure",
    "ThirdPartyCookiesBlocked",
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


class ClientHintIssueDetails(TypedDict):
    sourceCodeLocation: SourceCodeLocation
    clientHintIssueReason: ClientHintIssueReason


class FailedRequestInfo(TypedDict):
    url: str
    failureMessage: str
    requestId: NotRequired[Network.RequestId]


StyleSheetLoadingIssueReason: TypeAlias = Literal["LateImportRule", "RequestFailed"]


class StylesheetLoadingIssueDetails(TypedDict):
    sourceCodeLocation: SourceCodeLocation
    styleSheetLoadingIssueReason: StyleSheetLoadingIssueReason
    failedRequestInfo: NotRequired[FailedRequestInfo]


InspectorIssueCode: TypeAlias = Literal[
    "CookieIssue",
    "MixedContentIssue",
    "BlockedByResponseIssue",
    "HeavyAdIssue",
    "ContentSecurityPolicyIssue",
    "SharedArrayBufferIssue",
    "LowTextContrastIssue",
    "CorsIssue",
    "AttributionReportingIssue",
    "QuirksModeIssue",
    "NavigatorUserAgentIssue",
    "GenericIssue",
    "DeprecationIssue",
    "ClientHintIssue",
    "FederatedAuthRequestIssue",
    "BounceTrackingIssue",
    "StylesheetLoadingIssue",
    "FederatedAuthUserInfoRequestIssue",
]


class InspectorIssueDetails(TypedDict):
    cookieIssueDetails: NotRequired[CookieIssueDetails]
    mixedContentIssueDetails: NotRequired[MixedContentIssueDetails]
    blockedByResponseIssueDetails: NotRequired[BlockedByResponseIssueDetails]
    heavyAdIssueDetails: NotRequired[HeavyAdIssueDetails]
    contentSecurityPolicyIssueDetails: NotRequired[ContentSecurityPolicyIssueDetails]
    sharedArrayBufferIssueDetails: NotRequired[SharedArrayBufferIssueDetails]
    lowTextContrastIssueDetails: NotRequired[LowTextContrastIssueDetails]
    corsIssueDetails: NotRequired[CorsIssueDetails]
    attributionReportingIssueDetails: NotRequired[AttributionReportingIssueDetails]
    quirksModeIssueDetails: NotRequired[QuirksModeIssueDetails]
    navigatorUserAgentIssueDetails: NotRequired[NavigatorUserAgentIssueDetails]
    genericIssueDetails: NotRequired[GenericIssueDetails]
    deprecationIssueDetails: NotRequired[DeprecationIssueDetails]
    clientHintIssueDetails: NotRequired[ClientHintIssueDetails]
    federatedAuthRequestIssueDetails: NotRequired[FederatedAuthRequestIssueDetails]
    bounceTrackingIssueDetails: NotRequired[BounceTrackingIssueDetails]
    stylesheetLoadingIssueDetails: NotRequired[StylesheetLoadingIssueDetails]
    federatedAuthUserInfoRequestIssueDetails: NotRequired[
        FederatedAuthUserInfoRequestIssueDetails
    ]


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


class CheckContrastParameters(TypedDict):
    reportAAA: NotRequired[bool]


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

    @overload
    async def checkContrast(
        self,
        params: CheckContrastParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def checkContrast(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[CheckContrastParameters],
    ) -> JsonObject: ...

    async def checkContrast(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Runs the contrast check for the target page. Found issues are reported using Audits.issueAdded event."""

        return await self._command("checkContrast", params, session_id, kwargs)

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
    "AttributionReportingIssueDetails",
    "AttributionReportingIssueType",
    "Audits",
    "BlockedByResponseIssueDetails",
    "BlockedByResponseReason",
    "BounceTrackingIssueDetails",
    "CheckContrastParameters",
    "CheckFormsIssuesResult",
    "ClientHintIssueDetails",
    "ClientHintIssueReason",
    "ContentSecurityPolicyIssueDetails",
    "ContentSecurityPolicyViolationType",
    "CookieExclusionReason",
    "CookieIssueDetails",
    "CookieOperation",
    "CookieWarningReason",
    "CorsIssueDetails",
    "DeprecationIssueDetails",
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
    "InspectorIssue",
    "InspectorIssueCode",
    "InspectorIssueDetails",
    "IssueAddedEvent",
    "IssueId",
    "LowTextContrastIssueDetails",
    "MixedContentIssueDetails",
    "MixedContentResolutionStatus",
    "MixedContentResourceType",
    "NavigatorUserAgentIssueDetails",
    "QuirksModeIssueDetails",
    "SharedArrayBufferIssueDetails",
    "SharedArrayBufferIssueType",
    "SourceCodeLocation",
    "StyleSheetLoadingIssueReason",
    "StylesheetLoadingIssueDetails",
]
