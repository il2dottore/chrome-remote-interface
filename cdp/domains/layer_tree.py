"""Generated bindings for the CDP LayerTree domain. Do not edit manually."""

from __future__ import annotations

from collections.abc import Awaitable, Mapping
from typing import TYPE_CHECKING, Literal, TypeAlias, cast, overload

from typing_extensions import NotRequired, TypedDict, Unpack

from cdp.domain import Domain as BaseDomain, EventCallback, Unsubscribe
from cdp.types import JsonObject

if TYPE_CHECKING:
    from . import dom as DOM


LayerId: TypeAlias = str

SnapshotId: TypeAlias = str


class ScrollRect(TypedDict):
    rect: DOM.Rect
    type: Literal["RepaintsOnScroll", "TouchEventHandler", "WheelEventHandler"]


class StickyPositionConstraint(TypedDict):
    stickyBoxRect: DOM.Rect
    containingBlockRect: DOM.Rect
    nearestLayerShiftingStickyBox: NotRequired[LayerId]
    nearestLayerShiftingContainingBlock: NotRequired[LayerId]


class PictureTile(TypedDict):
    x: float
    y: float
    picture: str


class Layer(TypedDict):
    layerId: LayerId
    parentLayerId: NotRequired[LayerId]
    backendNodeId: NotRequired[DOM.BackendNodeId]
    offsetX: float
    offsetY: float
    width: float
    height: float
    transform: NotRequired[list[float]]
    anchorX: NotRequired[float]
    anchorY: NotRequired[float]
    anchorZ: NotRequired[float]
    paintCount: int
    drawsContent: bool
    invisible: NotRequired[bool]
    scrollRects: NotRequired[list[ScrollRect]]
    stickyPositionConstraint: NotRequired[StickyPositionConstraint]


PaintProfile: TypeAlias = list[float]


class CompositingReasonsParameters(TypedDict):
    layerId: LayerId


class CompositingReasonsResult(TypedDict):
    compositingReasons: list[str]
    compositingReasonIds: list[str]


class LoadSnapshotParameters(TypedDict):
    tiles: list[PictureTile]


class LoadSnapshotResult(TypedDict):
    snapshotId: SnapshotId


class MakeSnapshotParameters(TypedDict):
    layerId: LayerId


class MakeSnapshotResult(TypedDict):
    snapshotId: SnapshotId


class ProfileSnapshotParameters(TypedDict):
    snapshotId: SnapshotId
    minRepeatCount: NotRequired[int]
    minDuration: NotRequired[float]
    clipRect: NotRequired[DOM.Rect]


class ProfileSnapshotResult(TypedDict):
    timings: list[PaintProfile]


class ReleaseSnapshotParameters(TypedDict):
    snapshotId: SnapshotId


class ReplaySnapshotParameters(TypedDict):
    snapshotId: SnapshotId
    fromStep: NotRequired[int]
    toStep: NotRequired[int]
    scale: NotRequired[float]


class ReplaySnapshotResult(TypedDict):
    dataURL: str


class SnapshotCommandLogParameters(TypedDict):
    snapshotId: SnapshotId


class SnapshotCommandLogResult(TypedDict):
    commandLog: list[JsonObject]


class LayerPaintedEvent(TypedDict):
    layerId: LayerId
    clip: DOM.Rect


class LayerTreeDidChangeEvent(TypedDict):
    layers: NotRequired[list[Layer]]


class LayerTree(BaseDomain):
    """The CDP LayerTree domain."""

    domain_name = "LayerTree"

    @overload
    async def compositingReasons(
        self,
        params: CompositingReasonsParameters,
        session_id: str | None = None,
    ) -> CompositingReasonsResult: ...

    @overload
    async def compositingReasons(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[CompositingReasonsParameters],
    ) -> CompositingReasonsResult: ...

    async def compositingReasons(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> CompositingReasonsResult:
        """Provides the reasons why the given layer was composited."""

        return cast(
            CompositingReasonsResult,
            await self._command("compositingReasons", params, session_id, kwargs),
        )

    async def disable(
        self,
        session_id: str | None = None,
    ) -> JsonObject:
        """Disables compositing tree inspection."""

        return await self._command("disable", None, session_id, {})

    async def enable(
        self,
        session_id: str | None = None,
    ) -> JsonObject:
        """Enables compositing tree inspection."""

        return await self._command("enable", None, session_id, {})

    @overload
    async def loadSnapshot(
        self,
        params: LoadSnapshotParameters,
        session_id: str | None = None,
    ) -> LoadSnapshotResult: ...

    @overload
    async def loadSnapshot(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[LoadSnapshotParameters],
    ) -> LoadSnapshotResult: ...

    async def loadSnapshot(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> LoadSnapshotResult:
        """Returns the snapshot identifier."""

        return cast(
            LoadSnapshotResult,
            await self._command("loadSnapshot", params, session_id, kwargs),
        )

    @overload
    async def makeSnapshot(
        self,
        params: MakeSnapshotParameters,
        session_id: str | None = None,
    ) -> MakeSnapshotResult: ...

    @overload
    async def makeSnapshot(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[MakeSnapshotParameters],
    ) -> MakeSnapshotResult: ...

    async def makeSnapshot(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> MakeSnapshotResult:
        """Returns the layer snapshot identifier."""

        return cast(
            MakeSnapshotResult,
            await self._command("makeSnapshot", params, session_id, kwargs),
        )

    @overload
    async def profileSnapshot(
        self,
        params: ProfileSnapshotParameters,
        session_id: str | None = None,
    ) -> ProfileSnapshotResult: ...

    @overload
    async def profileSnapshot(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[ProfileSnapshotParameters],
    ) -> ProfileSnapshotResult: ...

    async def profileSnapshot(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> ProfileSnapshotResult:
        """Send LayerTree.profileSnapshot."""

        return cast(
            ProfileSnapshotResult,
            await self._command("profileSnapshot", params, session_id, kwargs),
        )

    @overload
    async def releaseSnapshot(
        self,
        params: ReleaseSnapshotParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def releaseSnapshot(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[ReleaseSnapshotParameters],
    ) -> JsonObject: ...

    async def releaseSnapshot(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Releases layer snapshot captured by the back-end."""

        return await self._command("releaseSnapshot", params, session_id, kwargs)

    @overload
    async def replaySnapshot(
        self,
        params: ReplaySnapshotParameters,
        session_id: str | None = None,
    ) -> ReplaySnapshotResult: ...

    @overload
    async def replaySnapshot(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[ReplaySnapshotParameters],
    ) -> ReplaySnapshotResult: ...

    async def replaySnapshot(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> ReplaySnapshotResult:
        """Replays the layer snapshot and returns the resulting bitmap."""

        return cast(
            ReplaySnapshotResult,
            await self._command("replaySnapshot", params, session_id, kwargs),
        )

    @overload
    async def snapshotCommandLog(
        self,
        params: SnapshotCommandLogParameters,
        session_id: str | None = None,
    ) -> SnapshotCommandLogResult: ...

    @overload
    async def snapshotCommandLog(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SnapshotCommandLogParameters],
    ) -> SnapshotCommandLogResult: ...

    async def snapshotCommandLog(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> SnapshotCommandLogResult:
        """Replays the layer snapshot and returns canvas log."""

        return cast(
            SnapshotCommandLogResult,
            await self._command("snapshotCommandLog", params, session_id, kwargs),
        )

    @overload
    def layerPainted(
        self,
        callback_or_session: EventCallback[LayerPaintedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def layerPainted(
        self,
        callback_or_session: str,
        handler: EventCallback[LayerPaintedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def layerPainted(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[LayerPaintedEvent]: ...

    def layerPainted(
        self,
        callback_or_session: EventCallback[LayerPaintedEvent] | str | None = None,
        handler: EventCallback[LayerPaintedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[LayerPaintedEvent] | Unsubscribe:
        """Wait for or subscribe to LayerTree.layerPainted."""

        return cast(
            Awaitable[LayerPaintedEvent] | Unsubscribe,
            self._event(
                "layerPainted",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def layerTreeDidChange(
        self,
        callback_or_session: EventCallback[LayerTreeDidChangeEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def layerTreeDidChange(
        self,
        callback_or_session: str,
        handler: EventCallback[LayerTreeDidChangeEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def layerTreeDidChange(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[LayerTreeDidChangeEvent]: ...

    def layerTreeDidChange(
        self,
        callback_or_session: EventCallback[LayerTreeDidChangeEvent] | str | None = None,
        handler: EventCallback[LayerTreeDidChangeEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[LayerTreeDidChangeEvent] | Unsubscribe:
        """Wait for or subscribe to LayerTree.layerTreeDidChange."""

        return cast(
            Awaitable[LayerTreeDidChangeEvent] | Unsubscribe,
            self._event(
                "layerTreeDidChange",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )


__all__ = [
    "CompositingReasonsParameters",
    "CompositingReasonsResult",
    "Layer",
    "LayerId",
    "LayerPaintedEvent",
    "LayerTree",
    "LayerTreeDidChangeEvent",
    "LoadSnapshotParameters",
    "LoadSnapshotResult",
    "MakeSnapshotParameters",
    "MakeSnapshotResult",
    "PaintProfile",
    "PictureTile",
    "ProfileSnapshotParameters",
    "ProfileSnapshotResult",
    "ReleaseSnapshotParameters",
    "ReplaySnapshotParameters",
    "ReplaySnapshotResult",
    "ScrollRect",
    "SnapshotCommandLogParameters",
    "SnapshotCommandLogResult",
    "SnapshotId",
    "StickyPositionConstraint",
]
