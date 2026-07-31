"""Generated bindings for the CDP Animation domain. Do not edit manually."""

from __future__ import annotations

from collections.abc import Awaitable, Mapping
from typing import TYPE_CHECKING, Literal, cast, overload

from typing_extensions import NotRequired, TypedDict, Unpack

from cdp.domain import Domain as BaseDomain, EventCallback, Unsubscribe
from cdp.types import JsonObject

if TYPE_CHECKING:
    from . import dom as DOM
    from . import runtime as Runtime


class Animation(TypedDict):
    id: str
    name: str
    pausedState: bool
    playState: str
    playbackRate: float
    startTime: float
    currentTime: float
    type: Literal["CSSTransition", "CSSAnimation", "WebAnimation"]
    source: NotRequired[AnimationEffect]
    cssId: NotRequired[str]
    viewOrScrollTimeline: NotRequired[ViewOrScrollTimeline]


class ViewOrScrollTimeline(TypedDict):
    sourceNodeId: NotRequired[DOM.BackendNodeId]
    startOffset: NotRequired[float]
    endOffset: NotRequired[float]
    subjectNodeId: NotRequired[DOM.BackendNodeId]
    axis: DOM.ScrollOrientation


class AnimationEffect(TypedDict):
    delay: float
    endDelay: float
    iterationStart: float
    iterations: NotRequired[float]
    duration: float
    direction: str
    fill: str
    backendNodeId: NotRequired[DOM.BackendNodeId]
    keyframesRule: NotRequired[KeyframesRule]
    easing: str


class KeyframesRule(TypedDict):
    name: NotRequired[str]
    keyframes: list[KeyframeStyle]


class KeyframeStyle(TypedDict):
    offset: str
    easing: str


class GetCurrentTimeParameters(TypedDict):
    id: str


class GetCurrentTimeResult(TypedDict):
    currentTime: float


class GetPlaybackRateResult(TypedDict):
    playbackRate: float


class ReleaseAnimationsParameters(TypedDict):
    animations: list[str]


class ResolveAnimationParameters(TypedDict):
    animationId: str


class ResolveAnimationResult(TypedDict):
    remoteObject: Runtime.RemoteObject


class SeekAnimationsParameters(TypedDict):
    animations: list[str]
    currentTime: float


class SetPausedParameters(TypedDict):
    animations: list[str]
    paused: bool


class SetPlaybackRateParameters(TypedDict):
    playbackRate: float


class SetTimingParameters(TypedDict):
    animationId: str
    duration: float
    delay: float


class AnimationCanceledEvent(TypedDict):
    id: str


class AnimationCreatedEvent(TypedDict):
    id: str


class AnimationStartedEvent(TypedDict):
    animation: Animation


class AnimationUpdatedEvent(TypedDict):
    animation: Animation


class AnimationDomain(BaseDomain):
    """The CDP Animation domain."""

    domain_name = "Animation"

    async def disable(
        self,
        session_id: str | None = None,
    ) -> JsonObject:
        """Disables animation domain notifications."""

        return await self._command("disable", None, session_id, {})

    async def enable(
        self,
        session_id: str | None = None,
    ) -> JsonObject:
        """Enables animation domain notifications."""

        return await self._command("enable", None, session_id, {})

    @overload
    async def getCurrentTime(
        self,
        params: GetCurrentTimeParameters,
        session_id: str | None = None,
    ) -> GetCurrentTimeResult: ...

    @overload
    async def getCurrentTime(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[GetCurrentTimeParameters],
    ) -> GetCurrentTimeResult: ...

    async def getCurrentTime(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> GetCurrentTimeResult:
        """Returns the current time of the an animation."""

        return cast(
            GetCurrentTimeResult,
            await self._command("getCurrentTime", params, session_id, kwargs),
        )

    async def getPlaybackRate(
        self,
        session_id: str | None = None,
    ) -> GetPlaybackRateResult:
        """Gets the playback rate of the document timeline."""

        return cast(
            GetPlaybackRateResult,
            await self._command("getPlaybackRate", None, session_id, {}),
        )

    @overload
    async def releaseAnimations(
        self,
        params: ReleaseAnimationsParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def releaseAnimations(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[ReleaseAnimationsParameters],
    ) -> JsonObject: ...

    async def releaseAnimations(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Releases a set of animations to no longer be manipulated."""

        return await self._command("releaseAnimations", params, session_id, kwargs)

    @overload
    async def resolveAnimation(
        self,
        params: ResolveAnimationParameters,
        session_id: str | None = None,
    ) -> ResolveAnimationResult: ...

    @overload
    async def resolveAnimation(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[ResolveAnimationParameters],
    ) -> ResolveAnimationResult: ...

    async def resolveAnimation(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> ResolveAnimationResult:
        """Gets the remote object of the Animation."""

        return cast(
            ResolveAnimationResult,
            await self._command("resolveAnimation", params, session_id, kwargs),
        )

    @overload
    async def seekAnimations(
        self,
        params: SeekAnimationsParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def seekAnimations(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SeekAnimationsParameters],
    ) -> JsonObject: ...

    async def seekAnimations(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Seek a set of animations to a particular time within each animation."""

        return await self._command("seekAnimations", params, session_id, kwargs)

    @overload
    async def setPaused(
        self,
        params: SetPausedParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def setPaused(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetPausedParameters],
    ) -> JsonObject: ...

    async def setPaused(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Sets the paused state of a set of animations."""

        return await self._command("setPaused", params, session_id, kwargs)

    @overload
    async def setPlaybackRate(
        self,
        params: SetPlaybackRateParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def setPlaybackRate(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetPlaybackRateParameters],
    ) -> JsonObject: ...

    async def setPlaybackRate(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Sets the playback rate of the document timeline."""

        return await self._command("setPlaybackRate", params, session_id, kwargs)

    @overload
    async def setTiming(
        self,
        params: SetTimingParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def setTiming(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetTimingParameters],
    ) -> JsonObject: ...

    async def setTiming(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Sets the timing of an animation node."""

        return await self._command("setTiming", params, session_id, kwargs)

    @overload
    def animationCanceled(
        self,
        callback_or_session: EventCallback[AnimationCanceledEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def animationCanceled(
        self,
        callback_or_session: str,
        handler: EventCallback[AnimationCanceledEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def animationCanceled(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[AnimationCanceledEvent]: ...

    def animationCanceled(
        self,
        callback_or_session: EventCallback[AnimationCanceledEvent] | str | None = None,
        handler: EventCallback[AnimationCanceledEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[AnimationCanceledEvent] | Unsubscribe:
        """Event for when an animation has been cancelled."""

        return cast(
            Awaitable[AnimationCanceledEvent] | Unsubscribe,
            self._event(
                "animationCanceled",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def animationCreated(
        self,
        callback_or_session: EventCallback[AnimationCreatedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def animationCreated(
        self,
        callback_or_session: str,
        handler: EventCallback[AnimationCreatedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def animationCreated(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[AnimationCreatedEvent]: ...

    def animationCreated(
        self,
        callback_or_session: EventCallback[AnimationCreatedEvent] | str | None = None,
        handler: EventCallback[AnimationCreatedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[AnimationCreatedEvent] | Unsubscribe:
        """Event for each animation that has been created."""

        return cast(
            Awaitable[AnimationCreatedEvent] | Unsubscribe,
            self._event(
                "animationCreated",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def animationStarted(
        self,
        callback_or_session: EventCallback[AnimationStartedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def animationStarted(
        self,
        callback_or_session: str,
        handler: EventCallback[AnimationStartedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def animationStarted(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[AnimationStartedEvent]: ...

    def animationStarted(
        self,
        callback_or_session: EventCallback[AnimationStartedEvent] | str | None = None,
        handler: EventCallback[AnimationStartedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[AnimationStartedEvent] | Unsubscribe:
        """Event for animation that has been started."""

        return cast(
            Awaitable[AnimationStartedEvent] | Unsubscribe,
            self._event(
                "animationStarted",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def animationUpdated(
        self,
        callback_or_session: EventCallback[AnimationUpdatedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def animationUpdated(
        self,
        callback_or_session: str,
        handler: EventCallback[AnimationUpdatedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def animationUpdated(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[AnimationUpdatedEvent]: ...

    def animationUpdated(
        self,
        callback_or_session: EventCallback[AnimationUpdatedEvent] | str | None = None,
        handler: EventCallback[AnimationUpdatedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[AnimationUpdatedEvent] | Unsubscribe:
        """Event for animation that has been updated."""

        return cast(
            Awaitable[AnimationUpdatedEvent] | Unsubscribe,
            self._event(
                "animationUpdated",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )


__all__ = [
    "Animation",
    "AnimationCanceledEvent",
    "AnimationCreatedEvent",
    "AnimationDomain",
    "AnimationEffect",
    "AnimationStartedEvent",
    "AnimationUpdatedEvent",
    "GetCurrentTimeParameters",
    "GetCurrentTimeResult",
    "GetPlaybackRateResult",
    "KeyframeStyle",
    "KeyframesRule",
    "ReleaseAnimationsParameters",
    "ResolveAnimationParameters",
    "ResolveAnimationResult",
    "SeekAnimationsParameters",
    "SetPausedParameters",
    "SetPlaybackRateParameters",
    "SetTimingParameters",
    "ViewOrScrollTimeline",
]
