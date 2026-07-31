"""Generated bindings for the CDP PerformanceTimeline domain. Do not edit manually."""

from __future__ import annotations

from collections.abc import Awaitable, Mapping
from typing import TYPE_CHECKING, cast, overload

from typing_extensions import NotRequired, TypedDict, Unpack

from cdp.domain import Domain as BaseDomain, EventCallback, Unsubscribe
from cdp.types import JsonObject

if TYPE_CHECKING:
    from . import dom as DOM
    from . import network as Network
    from . import page as Page


class LargestContentfulPaint(TypedDict):
    renderTime: Network.TimeSinceEpoch
    loadTime: Network.TimeSinceEpoch
    size: float
    elementId: NotRequired[str]
    url: NotRequired[str]
    nodeId: NotRequired[DOM.BackendNodeId]


class LayoutShiftAttribution(TypedDict):
    previousRect: DOM.Rect
    currentRect: DOM.Rect
    nodeId: NotRequired[DOM.BackendNodeId]


class LayoutShift(TypedDict):
    value: float
    hadRecentInput: bool
    lastInputTime: Network.TimeSinceEpoch
    sources: list[LayoutShiftAttribution]


class TimelineEvent(TypedDict):
    frameId: Page.FrameId
    type: str
    name: str
    time: Network.TimeSinceEpoch
    duration: NotRequired[float]
    lcpDetails: NotRequired[LargestContentfulPaint]
    layoutShiftDetails: NotRequired[LayoutShift]


class EnableParameters(TypedDict):
    eventTypes: list[str]


class TimelineEventAddedEvent(TypedDict):
    event: TimelineEvent


class PerformanceTimeline(BaseDomain):
    """Reporting of performance timeline events, as specified in https://w3c.github.io/performance-timeline/#dom-performanceobserver."""

    domain_name = "PerformanceTimeline"

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
        """Previously buffered events would be reported before method returns. See also: timelineEventAdded"""

        return await self._command("enable", params, session_id, kwargs)

    @overload
    def timelineEventAdded(
        self,
        callback_or_session: EventCallback[TimelineEventAddedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def timelineEventAdded(
        self,
        callback_or_session: str,
        handler: EventCallback[TimelineEventAddedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def timelineEventAdded(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[TimelineEventAddedEvent]: ...

    def timelineEventAdded(
        self,
        callback_or_session: EventCallback[TimelineEventAddedEvent] | str | None = None,
        handler: EventCallback[TimelineEventAddedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[TimelineEventAddedEvent] | Unsubscribe:
        """Sent when a performance timeline event is added. See reportPerformanceTimeline method."""

        return cast(
            Awaitable[TimelineEventAddedEvent] | Unsubscribe,
            self._event(
                "timelineEventAdded",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )


__all__ = [
    "EnableParameters",
    "LargestContentfulPaint",
    "LayoutShift",
    "LayoutShiftAttribution",
    "PerformanceTimeline",
    "TimelineEvent",
    "TimelineEventAddedEvent",
]
