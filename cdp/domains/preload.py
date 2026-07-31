"""Generated bindings for the CDP Preload domain. Do not edit manually."""

from __future__ import annotations

from collections.abc import Awaitable, Mapping
from typing import TYPE_CHECKING, Literal, TypeAlias, cast, overload

from typing_extensions import NotRequired, TypedDict

from cdp.domain import Domain as BaseDomain, EventCallback, Unsubscribe
from cdp.types import JsonObject

if TYPE_CHECKING:
    from . import dom as DOM
    from . import network as Network
    from . import page as Page


RuleSetId: TypeAlias = str


class RuleSet(TypedDict):
    id: RuleSetId
    loaderId: Network.LoaderId
    sourceText: str
    backendNodeId: NotRequired[DOM.BackendNodeId]
    url: NotRequired[str]
    requestId: NotRequired[Network.RequestId]
    errorType: NotRequired[RuleSetErrorType]
    errorMessage: NotRequired[str]
    tag: NotRequired[str]


RuleSetErrorType: TypeAlias = Literal[
    "SourceIsNotJsonObject", "InvalidRulesSkipped", "InvalidRulesetLevelTag"
]

SpeculationAction: TypeAlias = Literal["Prefetch", "Prerender", "PrerenderUntilScript"]

SpeculationTargetHint: TypeAlias = Literal["Blank", "Self"]


class PreloadingAttemptKey(TypedDict):
    loaderId: Network.LoaderId
    action: SpeculationAction
    url: str
    formSubmission: NotRequired[bool]
    targetHint: NotRequired[SpeculationTargetHint]


class PreloadingAttemptSource(TypedDict):
    key: PreloadingAttemptKey
    ruleSetIds: list[RuleSetId]
    nodeIds: list[DOM.BackendNodeId]


PreloadPipelineId: TypeAlias = str

PrerenderFinalStatus: TypeAlias = Literal[
    "Activated",
    "Destroyed",
    "LowEndDevice",
    "InvalidSchemeRedirect",
    "InvalidSchemeNavigation",
    "NavigationRequestBlockedByCsp",
    "MojoBinderPolicy",
    "RendererProcessCrashed",
    "RendererProcessKilled",
    "Download",
    "TriggerDestroyed",
    "NavigationNotCommitted",
    "NavigationBadHttpStatus",
    "ClientCertRequested",
    "NavigationRequestNetworkError",
    "CancelAllHostsForTesting",
    "DidFailLoad",
    "Stop",
    "SslCertificateError",
    "LoginAuthRequested",
    "UaChangeRequiresReload",
    "BlockedByClient",
    "AudioOutputDeviceRequested",
    "MixedContent",
    "TriggerBackgrounded",
    "MemoryLimitExceeded",
    "DataSaverEnabled",
    "TriggerUrlHasEffectiveUrl",
    "ActivatedBeforeStarted",
    "InactivePageRestriction",
    "StartFailed",
    "TimeoutBackgrounded",
    "CrossSiteRedirectInInitialNavigation",
    "CrossSiteNavigationInInitialNavigation",
    "SameSiteCrossOriginRedirectNotOptInInInitialNavigation",
    "SameSiteCrossOriginNavigationNotOptInInInitialNavigation",
    "ActivationNavigationParameterMismatch",
    "ActivatedInBackground",
    "EmbedderHostDisallowed",
    "ActivationNavigationDestroyedBeforeSuccess",
    "TabClosedByUserGesture",
    "TabClosedWithoutUserGesture",
    "PrimaryMainFrameRendererProcessCrashed",
    "PrimaryMainFrameRendererProcessKilled",
    "ActivationFramePolicyNotCompatible",
    "PreloadingDisabled",
    "BatterySaverEnabled",
    "ActivatedDuringMainFrameNavigation",
    "PreloadingUnsupportedByWebContents",
    "CrossSiteRedirectInMainFrameNavigation",
    "CrossSiteNavigationInMainFrameNavigation",
    "SameSiteCrossOriginRedirectNotOptInInMainFrameNavigation",
    "SameSiteCrossOriginNavigationNotOptInInMainFrameNavigation",
    "MemoryPressureOnTrigger",
    "MemoryPressureAfterTriggered",
    "PrerenderingDisabledByDevTools",
    "SpeculationRuleRemoved",
    "ActivatedWithAuxiliaryBrowsingContexts",
    "MaxNumOfRunningEagerPrerendersExceeded",
    "MaxNumOfRunningNonEagerPrerendersExceeded",
    "MaxNumOfRunningEmbedderPrerendersExceeded",
    "PrerenderingUrlHasEffectiveUrl",
    "RedirectedPrerenderingUrlHasEffectiveUrl",
    "ActivationUrlHasEffectiveUrl",
    "JavaScriptInterfaceAdded",
    "JavaScriptInterfaceRemoved",
    "AllPrerenderingCanceled",
    "WindowClosed",
    "SlowNetwork",
    "OtherPrerenderedPageActivated",
    "V8OptimizerDisabled",
    "PrerenderFailedDuringPrefetch",
    "BrowsingDataRemoved",
    "PrerenderHostReused",
    "FormSubmitWhenPrerendering",
    "CrossDocumentRestart",
]

PreloadingStatus: TypeAlias = Literal[
    "Pending", "Running", "Ready", "Success", "Failure", "NotSupported"
]

PrefetchStatus: TypeAlias = Literal[
    "PrefetchAllowed",
    "PrefetchFailedIneligibleRedirect",
    "PrefetchFailedInvalidRedirect",
    "PrefetchFailedMIMENotSupported",
    "PrefetchFailedNetError",
    "PrefetchFailedNon2XX",
    "PrefetchEvictedAfterBrowsingDataRemoved",
    "PrefetchEvictedAfterCandidateRemoved",
    "PrefetchEvictedForNewerPrefetch",
    "PrefetchHeldback",
    "PrefetchIneligibleRetryAfter",
    "PrefetchIsPrivacyDecoy",
    "PrefetchIsStale",
    "PrefetchNotEligibleBlockedByConnectionAllowlist",
    "PrefetchNotEligibleBrowserContextOffTheRecord",
    "PrefetchNotEligibleDataSaverEnabled",
    "PrefetchNotEligibleExistingProxy",
    "PrefetchNotEligibleHostIsNonUnique",
    "PrefetchNotEligibleNonDefaultStoragePartition",
    "PrefetchNotEligibleSameSiteCrossOriginPrefetchRequiredProxy",
    "PrefetchNotEligibleSchemeIsNotHttps",
    "PrefetchNotEligibleUserHasCookies",
    "PrefetchNotEligibleUserHasServiceWorker",
    "PrefetchNotEligibleUserHasServiceWorkerNoFetchHandler",
    "PrefetchNotEligibleRedirectFromServiceWorker",
    "PrefetchNotEligibleRedirectToServiceWorker",
    "PrefetchNotEligibleBatterySaverEnabled",
    "PrefetchNotEligiblePreloadingDisabled",
    "PrefetchNotFinishedInTime",
    "PrefetchNotStarted",
    "PrefetchNotUsedCookiesChanged",
    "PrefetchProxyNotAvailable",
    "PrefetchResponseUsed",
    "PrefetchSuccessfulButNotUsed",
    "PrefetchNotUsedProbeFailed",
    "PrefetchCancelledOnUserNavigation",
]


class PrerenderMismatchedHeaders(TypedDict):
    headerName: str
    initialValue: NotRequired[str]
    activationValue: NotRequired[str]


class RuleSetUpdatedEvent(TypedDict):
    ruleSet: RuleSet


class RuleSetRemovedEvent(TypedDict):
    id: RuleSetId


class PreloadEnabledStateUpdatedEvent(TypedDict):
    disabledByPreference: bool
    disabledByDataSaver: bool
    disabledByBatterySaver: bool
    disabledByHoldbackPrefetchSpeculationRules: bool
    disabledByHoldbackPrerenderSpeculationRules: bool


class PrefetchStatusUpdatedEvent(TypedDict):
    key: PreloadingAttemptKey
    pipelineId: PreloadPipelineId
    initiatingFrameId: Page.FrameId
    prefetchUrl: str
    status: PreloadingStatus
    prefetchStatus: PrefetchStatus
    requestId: Network.RequestId


class PrerenderStatusUpdatedEvent(TypedDict):
    key: PreloadingAttemptKey
    pipelineId: PreloadPipelineId
    status: PreloadingStatus
    prerenderStatus: NotRequired[PrerenderFinalStatus]
    disallowedMojoInterface: NotRequired[str]
    mismatchedHeaders: NotRequired[list[PrerenderMismatchedHeaders]]


class PreloadingAttemptSourcesUpdatedEvent(TypedDict):
    loaderId: Network.LoaderId
    preloadingAttemptSources: list[PreloadingAttemptSource]


class Preload(BaseDomain):
    """The CDP Preload domain."""

    domain_name = "Preload"

    async def enable(
        self,
        session_id: str | None = None,
    ) -> JsonObject:
        """Send Preload.enable."""

        return await self._command("enable", None, session_id, {})

    async def disable(
        self,
        session_id: str | None = None,
    ) -> JsonObject:
        """Send Preload.disable."""

        return await self._command("disable", None, session_id, {})

    @overload
    def ruleSetUpdated(
        self,
        callback_or_session: EventCallback[RuleSetUpdatedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def ruleSetUpdated(
        self,
        callback_or_session: str,
        handler: EventCallback[RuleSetUpdatedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def ruleSetUpdated(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[RuleSetUpdatedEvent]: ...

    def ruleSetUpdated(
        self,
        callback_or_session: EventCallback[RuleSetUpdatedEvent] | str | None = None,
        handler: EventCallback[RuleSetUpdatedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[RuleSetUpdatedEvent] | Unsubscribe:
        """Upsert. Currently, it is only emitted when a rule set added."""

        return cast(
            Awaitable[RuleSetUpdatedEvent] | Unsubscribe,
            self._event(
                "ruleSetUpdated",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def ruleSetRemoved(
        self,
        callback_or_session: EventCallback[RuleSetRemovedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def ruleSetRemoved(
        self,
        callback_or_session: str,
        handler: EventCallback[RuleSetRemovedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def ruleSetRemoved(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[RuleSetRemovedEvent]: ...

    def ruleSetRemoved(
        self,
        callback_or_session: EventCallback[RuleSetRemovedEvent] | str | None = None,
        handler: EventCallback[RuleSetRemovedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[RuleSetRemovedEvent] | Unsubscribe:
        """Wait for or subscribe to Preload.ruleSetRemoved."""

        return cast(
            Awaitable[RuleSetRemovedEvent] | Unsubscribe,
            self._event(
                "ruleSetRemoved",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def preloadEnabledStateUpdated(
        self,
        callback_or_session: EventCallback[PreloadEnabledStateUpdatedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def preloadEnabledStateUpdated(
        self,
        callback_or_session: str,
        handler: EventCallback[PreloadEnabledStateUpdatedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def preloadEnabledStateUpdated(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[PreloadEnabledStateUpdatedEvent]: ...

    def preloadEnabledStateUpdated(
        self,
        callback_or_session: EventCallback[PreloadEnabledStateUpdatedEvent]
        | str
        | None = None,
        handler: EventCallback[PreloadEnabledStateUpdatedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[PreloadEnabledStateUpdatedEvent] | Unsubscribe:
        """Fired when a preload enabled state is updated."""

        return cast(
            Awaitable[PreloadEnabledStateUpdatedEvent] | Unsubscribe,
            self._event(
                "preloadEnabledStateUpdated",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def prefetchStatusUpdated(
        self,
        callback_or_session: EventCallback[PrefetchStatusUpdatedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def prefetchStatusUpdated(
        self,
        callback_or_session: str,
        handler: EventCallback[PrefetchStatusUpdatedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def prefetchStatusUpdated(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[PrefetchStatusUpdatedEvent]: ...

    def prefetchStatusUpdated(
        self,
        callback_or_session: EventCallback[PrefetchStatusUpdatedEvent]
        | str
        | None = None,
        handler: EventCallback[PrefetchStatusUpdatedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[PrefetchStatusUpdatedEvent] | Unsubscribe:
        """Fired when a prefetch attempt is updated."""

        return cast(
            Awaitable[PrefetchStatusUpdatedEvent] | Unsubscribe,
            self._event(
                "prefetchStatusUpdated",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def prerenderStatusUpdated(
        self,
        callback_or_session: EventCallback[PrerenderStatusUpdatedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def prerenderStatusUpdated(
        self,
        callback_or_session: str,
        handler: EventCallback[PrerenderStatusUpdatedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def prerenderStatusUpdated(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[PrerenderStatusUpdatedEvent]: ...

    def prerenderStatusUpdated(
        self,
        callback_or_session: EventCallback[PrerenderStatusUpdatedEvent]
        | str
        | None = None,
        handler: EventCallback[PrerenderStatusUpdatedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[PrerenderStatusUpdatedEvent] | Unsubscribe:
        """Fired when a prerender attempt is updated."""

        return cast(
            Awaitable[PrerenderStatusUpdatedEvent] | Unsubscribe,
            self._event(
                "prerenderStatusUpdated",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def preloadingAttemptSourcesUpdated(
        self,
        callback_or_session: EventCallback[PreloadingAttemptSourcesUpdatedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def preloadingAttemptSourcesUpdated(
        self,
        callback_or_session: str,
        handler: EventCallback[PreloadingAttemptSourcesUpdatedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def preloadingAttemptSourcesUpdated(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[PreloadingAttemptSourcesUpdatedEvent]: ...

    def preloadingAttemptSourcesUpdated(
        self,
        callback_or_session: EventCallback[PreloadingAttemptSourcesUpdatedEvent]
        | str
        | None = None,
        handler: EventCallback[PreloadingAttemptSourcesUpdatedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[PreloadingAttemptSourcesUpdatedEvent] | Unsubscribe:
        """Send a list of sources for all preloading attempts in a document."""

        return cast(
            Awaitable[PreloadingAttemptSourcesUpdatedEvent] | Unsubscribe,
            self._event(
                "preloadingAttemptSourcesUpdated",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )


__all__ = [
    "PrefetchStatus",
    "PrefetchStatusUpdatedEvent",
    "Preload",
    "PreloadEnabledStateUpdatedEvent",
    "PreloadPipelineId",
    "PreloadingAttemptKey",
    "PreloadingAttemptSource",
    "PreloadingAttemptSourcesUpdatedEvent",
    "PreloadingStatus",
    "PrerenderFinalStatus",
    "PrerenderMismatchedHeaders",
    "PrerenderStatusUpdatedEvent",
    "RuleSet",
    "RuleSetErrorType",
    "RuleSetId",
    "RuleSetRemovedEvent",
    "RuleSetUpdatedEvent",
    "SpeculationAction",
    "SpeculationTargetHint",
]
