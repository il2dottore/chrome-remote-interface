"""Generated bindings for the CDP Overlay domain. Do not edit manually."""

from __future__ import annotations

from collections.abc import Awaitable, Mapping
from typing import TYPE_CHECKING, Literal, TypeAlias, cast, overload

from typing_extensions import NotRequired, TypedDict, Unpack

from cdp.domain import Domain as BaseDomain, EventCallback, Unsubscribe
from cdp.types import JsonObject

if TYPE_CHECKING:
    from . import dom as DOM
    from . import page as Page
    from . import runtime as Runtime


class SourceOrderConfig(TypedDict):
    parentOutlineColor: DOM.RGBA
    childOutlineColor: DOM.RGBA


class GridHighlightConfig(TypedDict):
    showGridExtensionLines: NotRequired[bool]
    showPositiveLineNumbers: NotRequired[bool]
    showNegativeLineNumbers: NotRequired[bool]
    showAreaNames: NotRequired[bool]
    showLineNames: NotRequired[bool]
    showTrackSizes: NotRequired[bool]
    gridBorderColor: NotRequired[DOM.RGBA]
    cellBorderColor: NotRequired[DOM.RGBA]
    rowLineColor: NotRequired[DOM.RGBA]
    columnLineColor: NotRequired[DOM.RGBA]
    gridBorderDash: NotRequired[bool]
    cellBorderDash: NotRequired[bool]
    rowLineDash: NotRequired[bool]
    columnLineDash: NotRequired[bool]
    rowGapColor: NotRequired[DOM.RGBA]
    rowHatchColor: NotRequired[DOM.RGBA]
    columnGapColor: NotRequired[DOM.RGBA]
    columnHatchColor: NotRequired[DOM.RGBA]
    areaBorderColor: NotRequired[DOM.RGBA]
    gridBackgroundColor: NotRequired[DOM.RGBA]


class FlexContainerHighlightConfig(TypedDict):
    containerBorder: NotRequired[LineStyle]
    lineSeparator: NotRequired[LineStyle]
    itemSeparator: NotRequired[LineStyle]
    mainDistributedSpace: NotRequired[BoxStyle]
    crossDistributedSpace: NotRequired[BoxStyle]
    rowGapSpace: NotRequired[BoxStyle]
    columnGapSpace: NotRequired[BoxStyle]
    crossAlignment: NotRequired[LineStyle]


class FlexItemHighlightConfig(TypedDict):
    baseSizeBox: NotRequired[BoxStyle]
    baseSizeBorder: NotRequired[LineStyle]
    flexibilityArrow: NotRequired[LineStyle]


class LineStyle(TypedDict):
    color: NotRequired[DOM.RGBA]
    pattern: NotRequired[Literal["dashed", "dotted"]]


class BoxStyle(TypedDict):
    fillColor: NotRequired[DOM.RGBA]
    hatchColor: NotRequired[DOM.RGBA]


ContrastAlgorithm: TypeAlias = Literal["aa", "aaa", "apca"]


class HighlightConfig(TypedDict):
    showInfo: NotRequired[bool]
    showStyles: NotRequired[bool]
    showRulers: NotRequired[bool]
    showAccessibilityInfo: NotRequired[bool]
    showExtensionLines: NotRequired[bool]
    contentColor: NotRequired[DOM.RGBA]
    paddingColor: NotRequired[DOM.RGBA]
    borderColor: NotRequired[DOM.RGBA]
    marginColor: NotRequired[DOM.RGBA]
    eventTargetColor: NotRequired[DOM.RGBA]
    shapeColor: NotRequired[DOM.RGBA]
    shapeMarginColor: NotRequired[DOM.RGBA]
    cssGridColor: NotRequired[DOM.RGBA]
    colorFormat: NotRequired[ColorFormat]
    gridHighlightConfig: NotRequired[GridHighlightConfig]
    flexContainerHighlightConfig: NotRequired[FlexContainerHighlightConfig]
    flexItemHighlightConfig: NotRequired[FlexItemHighlightConfig]
    contrastAlgorithm: NotRequired[ContrastAlgorithm]
    containerQueryContainerHighlightConfig: NotRequired[
        ContainerQueryContainerHighlightConfig
    ]


ColorFormat: TypeAlias = Literal["rgb", "hsl", "hwb", "hex"]


class GridNodeHighlightConfig(TypedDict):
    gridHighlightConfig: GridHighlightConfig
    nodeId: DOM.NodeId


class FlexNodeHighlightConfig(TypedDict):
    flexContainerHighlightConfig: FlexContainerHighlightConfig
    nodeId: DOM.NodeId


class ScrollSnapContainerHighlightConfig(TypedDict):
    snapportBorder: NotRequired[LineStyle]
    snapAreaBorder: NotRequired[LineStyle]
    scrollMarginColor: NotRequired[DOM.RGBA]
    scrollPaddingColor: NotRequired[DOM.RGBA]


class ScrollSnapHighlightConfig(TypedDict):
    scrollSnapContainerHighlightConfig: ScrollSnapContainerHighlightConfig
    nodeId: DOM.NodeId


class HingeConfig(TypedDict):
    rect: DOM.Rect
    contentColor: NotRequired[DOM.RGBA]
    outlineColor: NotRequired[DOM.RGBA]


class ContainerQueryHighlightConfig(TypedDict):
    containerQueryContainerHighlightConfig: ContainerQueryContainerHighlightConfig
    nodeId: DOM.NodeId


class ContainerQueryContainerHighlightConfig(TypedDict):
    containerBorder: NotRequired[LineStyle]
    descendantBorder: NotRequired[LineStyle]


class IsolatedElementHighlightConfig(TypedDict):
    isolationModeHighlightConfig: IsolationModeHighlightConfig
    nodeId: DOM.NodeId


class IsolationModeHighlightConfig(TypedDict):
    resizerColor: NotRequired[DOM.RGBA]
    resizerHandleColor: NotRequired[DOM.RGBA]
    maskColor: NotRequired[DOM.RGBA]


InspectMode: TypeAlias = Literal[
    "searchForNode",
    "searchForUAShadowDOM",
    "captureAreaScreenshot",
    "showDistances",
    "none",
]


class GetHighlightObjectForTestParameters(TypedDict):
    nodeId: DOM.NodeId
    includeDistance: NotRequired[bool]
    includeStyle: NotRequired[bool]
    colorFormat: NotRequired[ColorFormat]
    showAccessibilityInfo: NotRequired[bool]


class GetHighlightObjectForTestResult(TypedDict):
    highlight: JsonObject


class GetGridHighlightObjectsForTestParameters(TypedDict):
    nodeIds: list[DOM.NodeId]


class GetGridHighlightObjectsForTestResult(TypedDict):
    highlights: JsonObject


class GetSourceOrderHighlightObjectForTestParameters(TypedDict):
    nodeId: DOM.NodeId


class GetSourceOrderHighlightObjectForTestResult(TypedDict):
    highlight: JsonObject


class HighlightFrameParameters(TypedDict):
    frameId: Page.FrameId
    contentColor: NotRequired[DOM.RGBA]
    contentOutlineColor: NotRequired[DOM.RGBA]


class HighlightNodeParameters(TypedDict):
    highlightConfig: HighlightConfig
    nodeId: NotRequired[DOM.NodeId]
    backendNodeId: NotRequired[DOM.BackendNodeId]
    objectId: NotRequired[Runtime.RemoteObjectId]
    selector: NotRequired[str]


class HighlightQuadParameters(TypedDict):
    quad: DOM.Quad
    color: NotRequired[DOM.RGBA]
    outlineColor: NotRequired[DOM.RGBA]


class HighlightRectParameters(TypedDict):
    x: int
    y: int
    width: int
    height: int
    color: NotRequired[DOM.RGBA]
    outlineColor: NotRequired[DOM.RGBA]


class HighlightSourceOrderParameters(TypedDict):
    sourceOrderConfig: SourceOrderConfig
    nodeId: NotRequired[DOM.NodeId]
    backendNodeId: NotRequired[DOM.BackendNodeId]
    objectId: NotRequired[Runtime.RemoteObjectId]


class SetInspectModeParameters(TypedDict):
    mode: InspectMode
    highlightConfig: NotRequired[HighlightConfig]


class SetShowAdHighlightsParameters(TypedDict):
    show: bool


class SetPausedInDebuggerMessageParameters(TypedDict):
    message: NotRequired[str]


class SetShowDebugBordersParameters(TypedDict):
    show: bool


class SetShowFPSCounterParameters(TypedDict):
    show: bool


class SetShowGridOverlaysParameters(TypedDict):
    gridNodeHighlightConfigs: list[GridNodeHighlightConfig]


class SetShowFlexOverlaysParameters(TypedDict):
    flexNodeHighlightConfigs: list[FlexNodeHighlightConfig]


class SetShowScrollSnapOverlaysParameters(TypedDict):
    scrollSnapHighlightConfigs: list[ScrollSnapHighlightConfig]


class SetShowContainerQueryOverlaysParameters(TypedDict):
    containerQueryHighlightConfigs: list[ContainerQueryHighlightConfig]


class SetShowPaintRectsParameters(TypedDict):
    result: bool


class SetShowLayoutShiftRegionsParameters(TypedDict):
    result: bool


class SetShowScrollBottleneckRectsParameters(TypedDict):
    show: bool


class SetShowHitTestBordersParameters(TypedDict):
    show: bool


class SetShowWebVitalsParameters(TypedDict):
    show: bool


class SetShowViewportSizeOnResizeParameters(TypedDict):
    show: bool


class SetShowHingeParameters(TypedDict):
    hingeConfig: NotRequired[HingeConfig]


class SetShowIsolatedElementsParameters(TypedDict):
    isolatedElementHighlightConfigs: list[IsolatedElementHighlightConfig]


class InspectNodeRequestedEvent(TypedDict):
    backendNodeId: DOM.BackendNodeId


class NodeHighlightRequestedEvent(TypedDict):
    nodeId: DOM.NodeId


class ScreenshotRequestedEvent(TypedDict):
    viewport: Page.Viewport


class Overlay(BaseDomain):
    """This domain provides various functionality related to drawing atop the inspected page."""

    domain_name = "Overlay"

    async def disable(
        self,
        session_id: str | None = None,
    ) -> JsonObject:
        """Disables domain notifications."""

        return await self._command("disable", None, session_id, {})

    async def enable(
        self,
        session_id: str | None = None,
    ) -> JsonObject:
        """Enables domain notifications."""

        return await self._command("enable", None, session_id, {})

    @overload
    async def getHighlightObjectForTest(
        self,
        params: GetHighlightObjectForTestParameters,
        session_id: str | None = None,
    ) -> GetHighlightObjectForTestResult: ...

    @overload
    async def getHighlightObjectForTest(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[GetHighlightObjectForTestParameters],
    ) -> GetHighlightObjectForTestResult: ...

    async def getHighlightObjectForTest(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> GetHighlightObjectForTestResult:
        """For testing."""

        return cast(
            GetHighlightObjectForTestResult,
            await self._command(
                "getHighlightObjectForTest", params, session_id, kwargs
            ),
        )

    @overload
    async def getGridHighlightObjectsForTest(
        self,
        params: GetGridHighlightObjectsForTestParameters,
        session_id: str | None = None,
    ) -> GetGridHighlightObjectsForTestResult: ...

    @overload
    async def getGridHighlightObjectsForTest(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[GetGridHighlightObjectsForTestParameters],
    ) -> GetGridHighlightObjectsForTestResult: ...

    async def getGridHighlightObjectsForTest(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> GetGridHighlightObjectsForTestResult:
        """For Persistent Grid testing."""

        return cast(
            GetGridHighlightObjectsForTestResult,
            await self._command(
                "getGridHighlightObjectsForTest", params, session_id, kwargs
            ),
        )

    @overload
    async def getSourceOrderHighlightObjectForTest(
        self,
        params: GetSourceOrderHighlightObjectForTestParameters,
        session_id: str | None = None,
    ) -> GetSourceOrderHighlightObjectForTestResult: ...

    @overload
    async def getSourceOrderHighlightObjectForTest(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[GetSourceOrderHighlightObjectForTestParameters],
    ) -> GetSourceOrderHighlightObjectForTestResult: ...

    async def getSourceOrderHighlightObjectForTest(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> GetSourceOrderHighlightObjectForTestResult:
        """For Source Order Viewer testing."""

        return cast(
            GetSourceOrderHighlightObjectForTestResult,
            await self._command(
                "getSourceOrderHighlightObjectForTest", params, session_id, kwargs
            ),
        )

    async def hideHighlight(
        self,
        session_id: str | None = None,
    ) -> JsonObject:
        """Hides any highlight."""

        return await self._command("hideHighlight", None, session_id, {})

    @overload
    async def highlightFrame(
        self,
        params: HighlightFrameParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def highlightFrame(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[HighlightFrameParameters],
    ) -> JsonObject: ...

    async def highlightFrame(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Highlights owner element of the frame with given id. Deprecated: Doesn't work reliablity and cannot be fixed due to process separatation (the owner node might be in a different process). Determine the owner node in the client and use highlightNode."""

        return await self._command("highlightFrame", params, session_id, kwargs)

    @overload
    async def highlightNode(
        self,
        params: HighlightNodeParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def highlightNode(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[HighlightNodeParameters],
    ) -> JsonObject: ...

    async def highlightNode(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Highlights DOM node with given id or with the given JavaScript object wrapper. Either nodeId or objectId must be specified."""

        return await self._command("highlightNode", params, session_id, kwargs)

    @overload
    async def highlightQuad(
        self,
        params: HighlightQuadParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def highlightQuad(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[HighlightQuadParameters],
    ) -> JsonObject: ...

    async def highlightQuad(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Highlights given quad. Coordinates are absolute with respect to the main frame viewport."""

        return await self._command("highlightQuad", params, session_id, kwargs)

    @overload
    async def highlightRect(
        self,
        params: HighlightRectParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def highlightRect(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[HighlightRectParameters],
    ) -> JsonObject: ...

    async def highlightRect(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Highlights given rectangle. Coordinates are absolute with respect to the main frame viewport."""

        return await self._command("highlightRect", params, session_id, kwargs)

    @overload
    async def highlightSourceOrder(
        self,
        params: HighlightSourceOrderParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def highlightSourceOrder(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[HighlightSourceOrderParameters],
    ) -> JsonObject: ...

    async def highlightSourceOrder(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Highlights the source order of the children of the DOM node with given id or with the given JavaScript object wrapper. Either nodeId or objectId must be specified."""

        return await self._command("highlightSourceOrder", params, session_id, kwargs)

    @overload
    async def setInspectMode(
        self,
        params: SetInspectModeParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def setInspectMode(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetInspectModeParameters],
    ) -> JsonObject: ...

    async def setInspectMode(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Enters the 'inspect' mode. In this mode, elements that user is hovering over are highlighted. Backend then generates 'inspectNodeRequested' event upon element selection."""

        return await self._command("setInspectMode", params, session_id, kwargs)

    @overload
    async def setShowAdHighlights(
        self,
        params: SetShowAdHighlightsParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def setShowAdHighlights(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetShowAdHighlightsParameters],
    ) -> JsonObject: ...

    async def setShowAdHighlights(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Highlights owner element of all frames detected to be ads."""

        return await self._command("setShowAdHighlights", params, session_id, kwargs)

    @overload
    async def setPausedInDebuggerMessage(
        self,
        params: SetPausedInDebuggerMessageParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def setPausedInDebuggerMessage(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetPausedInDebuggerMessageParameters],
    ) -> JsonObject: ...

    async def setPausedInDebuggerMessage(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Send Overlay.setPausedInDebuggerMessage."""

        return await self._command(
            "setPausedInDebuggerMessage", params, session_id, kwargs
        )

    @overload
    async def setShowDebugBorders(
        self,
        params: SetShowDebugBordersParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def setShowDebugBorders(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetShowDebugBordersParameters],
    ) -> JsonObject: ...

    async def setShowDebugBorders(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Requests that backend shows debug borders on layers"""

        return await self._command("setShowDebugBorders", params, session_id, kwargs)

    @overload
    async def setShowFPSCounter(
        self,
        params: SetShowFPSCounterParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def setShowFPSCounter(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetShowFPSCounterParameters],
    ) -> JsonObject: ...

    async def setShowFPSCounter(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Requests that backend shows the FPS counter"""

        return await self._command("setShowFPSCounter", params, session_id, kwargs)

    @overload
    async def setShowGridOverlays(
        self,
        params: SetShowGridOverlaysParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def setShowGridOverlays(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetShowGridOverlaysParameters],
    ) -> JsonObject: ...

    async def setShowGridOverlays(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Highlight multiple elements with the CSS Grid overlay."""

        return await self._command("setShowGridOverlays", params, session_id, kwargs)

    @overload
    async def setShowFlexOverlays(
        self,
        params: SetShowFlexOverlaysParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def setShowFlexOverlays(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetShowFlexOverlaysParameters],
    ) -> JsonObject: ...

    async def setShowFlexOverlays(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Send Overlay.setShowFlexOverlays."""

        return await self._command("setShowFlexOverlays", params, session_id, kwargs)

    @overload
    async def setShowScrollSnapOverlays(
        self,
        params: SetShowScrollSnapOverlaysParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def setShowScrollSnapOverlays(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetShowScrollSnapOverlaysParameters],
    ) -> JsonObject: ...

    async def setShowScrollSnapOverlays(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Send Overlay.setShowScrollSnapOverlays."""

        return await self._command(
            "setShowScrollSnapOverlays", params, session_id, kwargs
        )

    @overload
    async def setShowContainerQueryOverlays(
        self,
        params: SetShowContainerQueryOverlaysParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def setShowContainerQueryOverlays(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetShowContainerQueryOverlaysParameters],
    ) -> JsonObject: ...

    async def setShowContainerQueryOverlays(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Send Overlay.setShowContainerQueryOverlays."""

        return await self._command(
            "setShowContainerQueryOverlays", params, session_id, kwargs
        )

    @overload
    async def setShowPaintRects(
        self,
        params: SetShowPaintRectsParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def setShowPaintRects(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetShowPaintRectsParameters],
    ) -> JsonObject: ...

    async def setShowPaintRects(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Requests that backend shows paint rectangles"""

        return await self._command("setShowPaintRects", params, session_id, kwargs)

    @overload
    async def setShowLayoutShiftRegions(
        self,
        params: SetShowLayoutShiftRegionsParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def setShowLayoutShiftRegions(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetShowLayoutShiftRegionsParameters],
    ) -> JsonObject: ...

    async def setShowLayoutShiftRegions(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Requests that backend shows layout shift regions"""

        return await self._command(
            "setShowLayoutShiftRegions", params, session_id, kwargs
        )

    @overload
    async def setShowScrollBottleneckRects(
        self,
        params: SetShowScrollBottleneckRectsParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def setShowScrollBottleneckRects(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetShowScrollBottleneckRectsParameters],
    ) -> JsonObject: ...

    async def setShowScrollBottleneckRects(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Requests that backend shows scroll bottleneck rects"""

        return await self._command(
            "setShowScrollBottleneckRects", params, session_id, kwargs
        )

    @overload
    async def setShowHitTestBorders(
        self,
        params: SetShowHitTestBordersParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def setShowHitTestBorders(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetShowHitTestBordersParameters],
    ) -> JsonObject: ...

    async def setShowHitTestBorders(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Deprecated, no longer has any effect."""

        return await self._command("setShowHitTestBorders", params, session_id, kwargs)

    @overload
    async def setShowWebVitals(
        self,
        params: SetShowWebVitalsParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def setShowWebVitals(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetShowWebVitalsParameters],
    ) -> JsonObject: ...

    async def setShowWebVitals(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Request that backend shows an overlay with web vital metrics."""

        return await self._command("setShowWebVitals", params, session_id, kwargs)

    @overload
    async def setShowViewportSizeOnResize(
        self,
        params: SetShowViewportSizeOnResizeParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def setShowViewportSizeOnResize(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetShowViewportSizeOnResizeParameters],
    ) -> JsonObject: ...

    async def setShowViewportSizeOnResize(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Paints viewport size upon main frame resize."""

        return await self._command(
            "setShowViewportSizeOnResize", params, session_id, kwargs
        )

    @overload
    async def setShowHinge(
        self,
        params: SetShowHingeParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def setShowHinge(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetShowHingeParameters],
    ) -> JsonObject: ...

    async def setShowHinge(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Add a dual screen device hinge"""

        return await self._command("setShowHinge", params, session_id, kwargs)

    @overload
    async def setShowIsolatedElements(
        self,
        params: SetShowIsolatedElementsParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def setShowIsolatedElements(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetShowIsolatedElementsParameters],
    ) -> JsonObject: ...

    async def setShowIsolatedElements(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Show elements in isolation mode with overlays."""

        return await self._command(
            "setShowIsolatedElements", params, session_id, kwargs
        )

    @overload
    def inspectNodeRequested(
        self,
        callback_or_session: EventCallback[InspectNodeRequestedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def inspectNodeRequested(
        self,
        callback_or_session: str,
        handler: EventCallback[InspectNodeRequestedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def inspectNodeRequested(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[InspectNodeRequestedEvent]: ...

    def inspectNodeRequested(
        self,
        callback_or_session: EventCallback[InspectNodeRequestedEvent]
        | str
        | None = None,
        handler: EventCallback[InspectNodeRequestedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[InspectNodeRequestedEvent] | Unsubscribe:
        """Fired when the node should be inspected. This happens after call to `setInspectMode` or when user manually inspects an element."""

        return cast(
            Awaitable[InspectNodeRequestedEvent] | Unsubscribe,
            self._event(
                "inspectNodeRequested",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def nodeHighlightRequested(
        self,
        callback_or_session: EventCallback[NodeHighlightRequestedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def nodeHighlightRequested(
        self,
        callback_or_session: str,
        handler: EventCallback[NodeHighlightRequestedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def nodeHighlightRequested(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[NodeHighlightRequestedEvent]: ...

    def nodeHighlightRequested(
        self,
        callback_or_session: EventCallback[NodeHighlightRequestedEvent]
        | str
        | None = None,
        handler: EventCallback[NodeHighlightRequestedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[NodeHighlightRequestedEvent] | Unsubscribe:
        """Fired when the node should be highlighted. This happens after call to `setInspectMode`."""

        return cast(
            Awaitable[NodeHighlightRequestedEvent] | Unsubscribe,
            self._event(
                "nodeHighlightRequested",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def screenshotRequested(
        self,
        callback_or_session: EventCallback[ScreenshotRequestedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def screenshotRequested(
        self,
        callback_or_session: str,
        handler: EventCallback[ScreenshotRequestedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def screenshotRequested(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[ScreenshotRequestedEvent]: ...

    def screenshotRequested(
        self,
        callback_or_session: EventCallback[ScreenshotRequestedEvent]
        | str
        | None = None,
        handler: EventCallback[ScreenshotRequestedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[ScreenshotRequestedEvent] | Unsubscribe:
        """Fired when user asks to capture screenshot of some area on the page."""

        return cast(
            Awaitable[ScreenshotRequestedEvent] | Unsubscribe,
            self._event(
                "screenshotRequested",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def inspectModeCanceled(
        self,
        callback_or_session: EventCallback[JsonObject],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def inspectModeCanceled(
        self,
        callback_or_session: str,
        handler: EventCallback[JsonObject],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def inspectModeCanceled(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[JsonObject]: ...

    def inspectModeCanceled(
        self,
        callback_or_session: EventCallback[JsonObject] | str | None = None,
        handler: EventCallback[JsonObject] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[JsonObject] | Unsubscribe:
        """Fired when user cancels the inspect mode."""

        return self._event(
            "inspectModeCanceled",
            cast(EventCallback[Mapping[str, object]] | str | None, callback_or_session),
            cast(EventCallback[Mapping[str, object]] | None, handler),
            session_id,
        )


__all__ = [
    "BoxStyle",
    "ColorFormat",
    "ContainerQueryContainerHighlightConfig",
    "ContainerQueryHighlightConfig",
    "ContrastAlgorithm",
    "FlexContainerHighlightConfig",
    "FlexItemHighlightConfig",
    "FlexNodeHighlightConfig",
    "GetGridHighlightObjectsForTestParameters",
    "GetGridHighlightObjectsForTestResult",
    "GetHighlightObjectForTestParameters",
    "GetHighlightObjectForTestResult",
    "GetSourceOrderHighlightObjectForTestParameters",
    "GetSourceOrderHighlightObjectForTestResult",
    "GridHighlightConfig",
    "GridNodeHighlightConfig",
    "HighlightConfig",
    "HighlightFrameParameters",
    "HighlightNodeParameters",
    "HighlightQuadParameters",
    "HighlightRectParameters",
    "HighlightSourceOrderParameters",
    "HingeConfig",
    "InspectMode",
    "InspectNodeRequestedEvent",
    "IsolatedElementHighlightConfig",
    "IsolationModeHighlightConfig",
    "LineStyle",
    "NodeHighlightRequestedEvent",
    "Overlay",
    "ScreenshotRequestedEvent",
    "ScrollSnapContainerHighlightConfig",
    "ScrollSnapHighlightConfig",
    "SetInspectModeParameters",
    "SetPausedInDebuggerMessageParameters",
    "SetShowAdHighlightsParameters",
    "SetShowContainerQueryOverlaysParameters",
    "SetShowDebugBordersParameters",
    "SetShowFPSCounterParameters",
    "SetShowFlexOverlaysParameters",
    "SetShowGridOverlaysParameters",
    "SetShowHingeParameters",
    "SetShowHitTestBordersParameters",
    "SetShowIsolatedElementsParameters",
    "SetShowLayoutShiftRegionsParameters",
    "SetShowPaintRectsParameters",
    "SetShowScrollBottleneckRectsParameters",
    "SetShowScrollSnapOverlaysParameters",
    "SetShowViewportSizeOnResizeParameters",
    "SetShowWebVitalsParameters",
    "SourceOrderConfig",
]
