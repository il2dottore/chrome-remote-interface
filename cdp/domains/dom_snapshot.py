"""Generated bindings for the CDP DOMSnapshot domain. Do not edit manually."""

from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, TypeAlias, cast, overload

from typing_extensions import NotRequired, TypedDict, Unpack

from cdp.domain import Domain as BaseDomain
from cdp.types import JsonObject

if TYPE_CHECKING:
    from . import dom as DOM
    from . import dom_debugger as DOMDebugger
    from . import page as Page


class DOMNode(TypedDict):
    nodeType: int
    nodeName: str
    nodeValue: str
    textValue: NotRequired[str]
    inputValue: NotRequired[str]
    inputChecked: NotRequired[bool]
    optionSelected: NotRequired[bool]
    backendNodeId: DOM.BackendNodeId
    childNodeIndexes: NotRequired[list[int]]
    attributes: NotRequired[list[NameValue]]
    pseudoElementIndexes: NotRequired[list[int]]
    layoutNodeIndex: NotRequired[int]
    documentURL: NotRequired[str]
    baseURL: NotRequired[str]
    contentLanguage: NotRequired[str]
    documentEncoding: NotRequired[str]
    publicId: NotRequired[str]
    systemId: NotRequired[str]
    frameId: NotRequired[Page.FrameId]
    contentDocumentIndex: NotRequired[int]
    pseudoType: NotRequired[DOM.PseudoType]
    shadowRootType: NotRequired[DOM.ShadowRootType]
    isClickable: NotRequired[bool]
    eventListeners: NotRequired[list[DOMDebugger.EventListener]]
    currentSourceURL: NotRequired[str]
    originURL: NotRequired[str]
    scrollOffsetX: NotRequired[float]
    scrollOffsetY: NotRequired[float]


class InlineTextBox(TypedDict):
    boundingBox: DOM.Rect
    startCharacterIndex: int
    numCharacters: int


class LayoutTreeNode(TypedDict):
    domNodeIndex: int
    boundingBox: DOM.Rect
    layoutText: NotRequired[str]
    inlineTextNodes: NotRequired[list[InlineTextBox]]
    styleIndex: NotRequired[int]
    paintOrder: NotRequired[int]
    isStackingContext: NotRequired[bool]


class ComputedStyle(TypedDict):
    properties: list[NameValue]


class NameValue(TypedDict):
    name: str
    value: str


StringIndex: TypeAlias = int

ArrayOfStrings: TypeAlias = list[StringIndex]


class RareStringData(TypedDict):
    index: list[int]
    value: list[StringIndex]


class RareBooleanData(TypedDict):
    index: list[int]


class RareIntegerData(TypedDict):
    index: list[int]
    value: list[int]


Rectangle: TypeAlias = list[float]


class DocumentSnapshot(TypedDict):
    documentURL: StringIndex
    title: StringIndex
    baseURL: StringIndex
    contentLanguage: StringIndex
    encodingName: StringIndex
    publicId: StringIndex
    systemId: StringIndex
    frameId: StringIndex
    nodes: NodeTreeSnapshot
    layout: LayoutTreeSnapshot
    textBoxes: TextBoxSnapshot
    scrollOffsetX: NotRequired[float]
    scrollOffsetY: NotRequired[float]
    contentWidth: NotRequired[float]
    contentHeight: NotRequired[float]


class NodeTreeSnapshot(TypedDict):
    parentIndex: NotRequired[list[int]]
    nodeType: NotRequired[list[int]]
    shadowRootType: NotRequired[RareStringData]
    nodeName: NotRequired[list[StringIndex]]
    nodeValue: NotRequired[list[StringIndex]]
    backendNodeId: NotRequired[list[DOM.BackendNodeId]]
    attributes: NotRequired[list[ArrayOfStrings]]
    textValue: NotRequired[RareStringData]
    inputValue: NotRequired[RareStringData]
    inputChecked: NotRequired[RareBooleanData]
    optionSelected: NotRequired[RareBooleanData]
    contentDocumentIndex: NotRequired[RareIntegerData]
    pseudoType: NotRequired[RareStringData]
    pseudoIdentifier: NotRequired[RareStringData]
    isClickable: NotRequired[RareBooleanData]
    currentSourceURL: NotRequired[RareStringData]
    originURL: NotRequired[RareStringData]


class LayoutTreeSnapshot(TypedDict):
    nodeIndex: list[int]
    styles: list[ArrayOfStrings]
    bounds: list[Rectangle]
    text: list[StringIndex]
    stackingContexts: RareBooleanData
    paintOrders: NotRequired[list[int]]
    offsetRects: NotRequired[list[Rectangle]]
    scrollRects: NotRequired[list[Rectangle]]
    clientRects: NotRequired[list[Rectangle]]
    blendedBackgroundColors: NotRequired[list[StringIndex]]
    textColorOpacities: NotRequired[list[float]]


class TextBoxSnapshot(TypedDict):
    layoutIndex: list[int]
    bounds: list[Rectangle]
    start: list[int]
    length: list[int]


class GetSnapshotParameters(TypedDict):
    computedStyleWhitelist: list[str]
    includeEventListeners: NotRequired[bool]
    includePaintOrder: NotRequired[bool]
    includeUserAgentShadowTree: NotRequired[bool]


class GetSnapshotResult(TypedDict):
    domNodes: list[DOMNode]
    layoutTreeNodes: list[LayoutTreeNode]
    computedStyles: list[ComputedStyle]


class CaptureSnapshotParameters(TypedDict):
    computedStyles: list[str]
    includePaintOrder: NotRequired[bool]
    includeDOMRects: NotRequired[bool]
    includeBlendedBackgroundColors: NotRequired[bool]
    includeTextColorOpacities: NotRequired[bool]


class CaptureSnapshotResult(TypedDict):
    documents: list[DocumentSnapshot]
    strings: list[str]


class DOMSnapshot(BaseDomain):
    """This domain facilitates obtaining document snapshots with DOM, layout, and style information."""

    domain_name = "DOMSnapshot"

    async def disable(
        self,
        session_id: str | None = None,
    ) -> JsonObject:
        """Disables DOM snapshot agent for the given page."""

        return await self._command("disable", None, session_id, {})

    async def enable(
        self,
        session_id: str | None = None,
    ) -> JsonObject:
        """Enables DOM snapshot agent for the given page."""

        return await self._command("enable", None, session_id, {})

    @overload
    async def getSnapshot(
        self,
        params: GetSnapshotParameters,
        session_id: str | None = None,
    ) -> GetSnapshotResult: ...

    @overload
    async def getSnapshot(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[GetSnapshotParameters],
    ) -> GetSnapshotResult: ...

    async def getSnapshot(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> GetSnapshotResult:
        """Returns a document snapshot, including the full DOM tree of the root node (including iframes, template contents, and imported documents) in a flattened array, as well as layout and white-listed computed style information for the nodes. Shadow DOM in the returned DOM tree is flattened."""

        return cast(
            GetSnapshotResult,
            await self._command("getSnapshot", params, session_id, kwargs),
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
        """Returns a document snapshot, including the full DOM tree of the root node (including iframes, template contents, and imported documents) in a flattened array, as well as layout and white-listed computed style information for the nodes. Shadow DOM in the returned DOM tree is flattened."""

        return cast(
            CaptureSnapshotResult,
            await self._command("captureSnapshot", params, session_id, kwargs),
        )


__all__ = [
    "ArrayOfStrings",
    "CaptureSnapshotParameters",
    "CaptureSnapshotResult",
    "ComputedStyle",
    "DOMNode",
    "DOMSnapshot",
    "DocumentSnapshot",
    "GetSnapshotParameters",
    "GetSnapshotResult",
    "InlineTextBox",
    "LayoutTreeNode",
    "LayoutTreeSnapshot",
    "NameValue",
    "NodeTreeSnapshot",
    "RareBooleanData",
    "RareIntegerData",
    "RareStringData",
    "Rectangle",
    "StringIndex",
    "TextBoxSnapshot",
]
