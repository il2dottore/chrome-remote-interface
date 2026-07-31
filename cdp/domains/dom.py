"""Generated bindings for the CDP DOM domain. Do not edit manually."""

from __future__ import annotations

from collections.abc import Awaitable, Mapping
from typing import TYPE_CHECKING, Literal, TypeAlias, cast, overload

from typing_extensions import NotRequired, TypedDict, Unpack

from cdp.domain import Domain as BaseDomain, EventCallback, Unsubscribe
from cdp.types import JsonObject, JsonValue

if TYPE_CHECKING:
    from . import page as Page
    from . import runtime as Runtime


NodeId: TypeAlias = int

BackendNodeId: TypeAlias = int


class BackendNode(TypedDict):
    nodeType: int
    nodeName: str
    backendNodeId: BackendNodeId


PseudoType: TypeAlias = Literal[
    "first-line",
    "first-letter",
    "before",
    "after",
    "marker",
    "backdrop",
    "selection",
    "target-text",
    "spelling-error",
    "grammar-error",
    "highlight",
    "first-line-inherited",
    "scrollbar",
    "scrollbar-thumb",
    "scrollbar-button",
    "scrollbar-track",
    "scrollbar-track-piece",
    "scrollbar-corner",
    "resizer",
    "input-list-button",
    "view-transition",
    "view-transition-group",
    "view-transition-image-pair",
    "view-transition-old",
    "view-transition-new",
]

ShadowRootType: TypeAlias = Literal["user-agent", "open", "closed"]

CompatibilityMode: TypeAlias = Literal[
    "QuirksMode", "LimitedQuirksMode", "NoQuirksMode"
]

PhysicalAxes: TypeAlias = Literal["Horizontal", "Vertical", "Both"]

LogicalAxes: TypeAlias = Literal["Inline", "Block", "Both"]


class Node(TypedDict):
    nodeId: NodeId
    parentId: NotRequired[NodeId]
    backendNodeId: BackendNodeId
    nodeType: int
    nodeName: str
    localName: str
    nodeValue: str
    childNodeCount: NotRequired[int]
    children: NotRequired[list[Node]]
    attributes: NotRequired[list[str]]
    documentURL: NotRequired[str]
    baseURL: NotRequired[str]
    publicId: NotRequired[str]
    systemId: NotRequired[str]
    internalSubset: NotRequired[str]
    xmlVersion: NotRequired[str]
    name: NotRequired[str]
    value: NotRequired[str]
    pseudoType: NotRequired[PseudoType]
    pseudoIdentifier: NotRequired[str]
    shadowRootType: NotRequired[ShadowRootType]
    frameId: NotRequired[Page.FrameId]
    contentDocument: NotRequired[Node]
    shadowRoots: NotRequired[list[Node]]
    templateContent: NotRequired[Node]
    pseudoElements: NotRequired[list[Node]]
    importedDocument: NotRequired[Node]
    distributedNodes: NotRequired[list[BackendNode]]
    isSVG: NotRequired[bool]
    compatibilityMode: NotRequired[CompatibilityMode]
    assignedSlot: NotRequired[BackendNode]


class RGBA(TypedDict):
    r: int
    g: int
    b: int
    a: NotRequired[float]


Quad: TypeAlias = list[float]


class BoxModel(TypedDict):
    content: Quad
    padding: Quad
    border: Quad
    margin: Quad
    width: int
    height: int
    shapeOutside: NotRequired[ShapeOutsideInfo]


class ShapeOutsideInfo(TypedDict):
    bounds: Quad
    shape: list[JsonValue]
    marginShape: list[JsonValue]


class Rect(TypedDict):
    x: float
    y: float
    width: float
    height: float


class CSSComputedStyleProperty(TypedDict):
    name: str
    value: str


class CollectClassNamesFromSubtreeParameters(TypedDict):
    nodeId: NodeId


class CollectClassNamesFromSubtreeResult(TypedDict):
    classNames: list[str]


class CopyToParameters(TypedDict):
    nodeId: NodeId
    targetNodeId: NodeId
    insertBeforeNodeId: NotRequired[NodeId]


class CopyToResult(TypedDict):
    nodeId: NodeId


class DescribeNodeParameters(TypedDict):
    nodeId: NotRequired[NodeId]
    backendNodeId: NotRequired[BackendNodeId]
    objectId: NotRequired[Runtime.RemoteObjectId]
    depth: NotRequired[int]
    pierce: NotRequired[bool]


class DescribeNodeResult(TypedDict):
    node: Node


class ScrollIntoViewIfNeededParameters(TypedDict):
    nodeId: NotRequired[NodeId]
    backendNodeId: NotRequired[BackendNodeId]
    objectId: NotRequired[Runtime.RemoteObjectId]
    rect: NotRequired[Rect]


class DiscardSearchResultsParameters(TypedDict):
    searchId: str


class EnableParameters(TypedDict):
    includeWhitespace: NotRequired[Literal["none", "all"]]


class FocusParameters(TypedDict):
    nodeId: NotRequired[NodeId]
    backendNodeId: NotRequired[BackendNodeId]
    objectId: NotRequired[Runtime.RemoteObjectId]


class GetAttributesParameters(TypedDict):
    nodeId: NodeId


class GetAttributesResult(TypedDict):
    attributes: list[str]


class GetBoxModelParameters(TypedDict):
    nodeId: NotRequired[NodeId]
    backendNodeId: NotRequired[BackendNodeId]
    objectId: NotRequired[Runtime.RemoteObjectId]


class GetBoxModelResult(TypedDict):
    model: BoxModel


class GetContentQuadsParameters(TypedDict):
    nodeId: NotRequired[NodeId]
    backendNodeId: NotRequired[BackendNodeId]
    objectId: NotRequired[Runtime.RemoteObjectId]


class GetContentQuadsResult(TypedDict):
    quads: list[Quad]


class GetDocumentParameters(TypedDict):
    depth: NotRequired[int]
    pierce: NotRequired[bool]


class GetDocumentResult(TypedDict):
    root: Node


class GetFlattenedDocumentParameters(TypedDict):
    depth: NotRequired[int]
    pierce: NotRequired[bool]


class GetFlattenedDocumentResult(TypedDict):
    nodes: list[Node]


class GetNodesForSubtreeByStyleParameters(TypedDict):
    nodeId: NodeId
    computedStyles: list[CSSComputedStyleProperty]
    pierce: NotRequired[bool]


class GetNodesForSubtreeByStyleResult(TypedDict):
    nodeIds: list[NodeId]


class GetNodeForLocationParameters(TypedDict):
    x: int
    y: int
    includeUserAgentShadowDOM: NotRequired[bool]
    ignorePointerEventsNone: NotRequired[bool]


class GetNodeForLocationResult(TypedDict):
    backendNodeId: BackendNodeId
    frameId: Page.FrameId
    nodeId: NotRequired[NodeId]


class GetOuterHTMLParameters(TypedDict):
    nodeId: NotRequired[NodeId]
    backendNodeId: NotRequired[BackendNodeId]
    objectId: NotRequired[Runtime.RemoteObjectId]


class GetOuterHTMLResult(TypedDict):
    outerHTML: str


class GetRelayoutBoundaryParameters(TypedDict):
    nodeId: NodeId


class GetRelayoutBoundaryResult(TypedDict):
    nodeId: NodeId


class GetSearchResultsParameters(TypedDict):
    searchId: str
    fromIndex: int
    toIndex: int


class GetSearchResultsResult(TypedDict):
    nodeIds: list[NodeId]


class MoveToParameters(TypedDict):
    nodeId: NodeId
    targetNodeId: NodeId
    insertBeforeNodeId: NotRequired[NodeId]


class MoveToResult(TypedDict):
    nodeId: NodeId


class PerformSearchParameters(TypedDict):
    query: str
    includeUserAgentShadowDOM: NotRequired[bool]


class PerformSearchResult(TypedDict):
    searchId: str
    resultCount: int


class PushNodeByPathToFrontendParameters(TypedDict):
    path: str


class PushNodeByPathToFrontendResult(TypedDict):
    nodeId: NodeId


class PushNodesByBackendIdsToFrontendParameters(TypedDict):
    backendNodeIds: list[BackendNodeId]


class PushNodesByBackendIdsToFrontendResult(TypedDict):
    nodeIds: list[NodeId]


class QuerySelectorParameters(TypedDict):
    nodeId: NodeId
    selector: str


class QuerySelectorResult(TypedDict):
    nodeId: NodeId


class QuerySelectorAllParameters(TypedDict):
    nodeId: NodeId
    selector: str


class QuerySelectorAllResult(TypedDict):
    nodeIds: list[NodeId]


class GetTopLayerElementsResult(TypedDict):
    nodeIds: list[NodeId]


class RemoveAttributeParameters(TypedDict):
    nodeId: NodeId
    name: str


class RemoveNodeParameters(TypedDict):
    nodeId: NodeId


class RequestChildNodesParameters(TypedDict):
    nodeId: NodeId
    depth: NotRequired[int]
    pierce: NotRequired[bool]


class RequestNodeParameters(TypedDict):
    objectId: Runtime.RemoteObjectId


class RequestNodeResult(TypedDict):
    nodeId: NodeId


class ResolveNodeParameters(TypedDict):
    nodeId: NotRequired[NodeId]
    backendNodeId: NotRequired[BackendNodeId]
    objectGroup: NotRequired[str]
    executionContextId: NotRequired[Runtime.ExecutionContextId]


class ResolveNodeResult(TypedDict):
    object: Runtime.RemoteObject


class SetAttributeValueParameters(TypedDict):
    nodeId: NodeId
    name: str
    value: str


class SetAttributesAsTextParameters(TypedDict):
    nodeId: NodeId
    text: str
    name: NotRequired[str]


class SetFileInputFilesParameters(TypedDict):
    files: list[str]
    nodeId: NotRequired[NodeId]
    backendNodeId: NotRequired[BackendNodeId]
    objectId: NotRequired[Runtime.RemoteObjectId]


class SetNodeStackTracesEnabledParameters(TypedDict):
    enable: bool


class GetNodeStackTracesParameters(TypedDict):
    nodeId: NodeId


class GetNodeStackTracesResult(TypedDict):
    creation: NotRequired[Runtime.StackTrace]


class GetFileInfoParameters(TypedDict):
    objectId: Runtime.RemoteObjectId


class GetFileInfoResult(TypedDict):
    path: str


class SetInspectedNodeParameters(TypedDict):
    nodeId: NodeId


class SetNodeNameParameters(TypedDict):
    nodeId: NodeId
    name: str


class SetNodeNameResult(TypedDict):
    nodeId: NodeId


class SetNodeValueParameters(TypedDict):
    nodeId: NodeId
    value: str


class SetOuterHTMLParameters(TypedDict):
    nodeId: NodeId
    outerHTML: str


class GetFrameOwnerParameters(TypedDict):
    frameId: Page.FrameId


class GetFrameOwnerResult(TypedDict):
    backendNodeId: BackendNodeId
    nodeId: NotRequired[NodeId]


class GetContainerForNodeParameters(TypedDict):
    nodeId: NodeId
    containerName: NotRequired[str]
    physicalAxes: NotRequired[PhysicalAxes]
    logicalAxes: NotRequired[LogicalAxes]


class GetContainerForNodeResult(TypedDict):
    nodeId: NotRequired[NodeId]


class GetQueryingDescendantsForContainerParameters(TypedDict):
    nodeId: NodeId


class GetQueryingDescendantsForContainerResult(TypedDict):
    nodeIds: list[NodeId]


class AttributeModifiedEvent(TypedDict):
    nodeId: NodeId
    name: str
    value: str


class AttributeRemovedEvent(TypedDict):
    nodeId: NodeId
    name: str


class CharacterDataModifiedEvent(TypedDict):
    nodeId: NodeId
    characterData: str


class ChildNodeCountUpdatedEvent(TypedDict):
    nodeId: NodeId
    childNodeCount: int


class ChildNodeInsertedEvent(TypedDict):
    parentNodeId: NodeId
    previousNodeId: NodeId
    node: Node


class ChildNodeRemovedEvent(TypedDict):
    parentNodeId: NodeId
    nodeId: NodeId


class DistributedNodesUpdatedEvent(TypedDict):
    insertionPointId: NodeId
    distributedNodes: list[BackendNode]


class InlineStyleInvalidatedEvent(TypedDict):
    nodeIds: list[NodeId]


class PseudoElementAddedEvent(TypedDict):
    parentId: NodeId
    pseudoElement: Node


class PseudoElementRemovedEvent(TypedDict):
    parentId: NodeId
    pseudoElementId: NodeId


class SetChildNodesEvent(TypedDict):
    parentId: NodeId
    nodes: list[Node]


class ShadowRootPoppedEvent(TypedDict):
    hostId: NodeId
    rootId: NodeId


class ShadowRootPushedEvent(TypedDict):
    hostId: NodeId
    root: Node


class DOM(BaseDomain):
    """This domain exposes DOM read/write operations. Each DOM Node is represented with its mirror object that has an `id`. This `id` can be used to get additional information on the Node, resolve it into the JavaScript object wrapper, etc. It is important that client receives DOM events only for the nodes that are known to the client. Backend keeps track of the nodes that were sent to the client and never sends the same node twice. It is client's responsibility to collect information about the nodes that were sent to the client. Note that `iframe` owner elements will return corresponding document elements as their child nodes."""

    domain_name = "DOM"

    @overload
    async def collectClassNamesFromSubtree(
        self,
        params: CollectClassNamesFromSubtreeParameters,
        session_id: str | None = None,
    ) -> CollectClassNamesFromSubtreeResult: ...

    @overload
    async def collectClassNamesFromSubtree(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[CollectClassNamesFromSubtreeParameters],
    ) -> CollectClassNamesFromSubtreeResult: ...

    async def collectClassNamesFromSubtree(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> CollectClassNamesFromSubtreeResult:
        """Collects class names for the node with given id and all of it's child nodes."""

        return cast(
            CollectClassNamesFromSubtreeResult,
            await self._command(
                "collectClassNamesFromSubtree", params, session_id, kwargs
            ),
        )

    @overload
    async def copyTo(
        self,
        params: CopyToParameters,
        session_id: str | None = None,
    ) -> CopyToResult: ...

    @overload
    async def copyTo(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[CopyToParameters],
    ) -> CopyToResult: ...

    async def copyTo(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> CopyToResult:
        """Creates a deep copy of the specified node and places it into the target container before the given anchor."""

        return cast(
            CopyToResult, await self._command("copyTo", params, session_id, kwargs)
        )

    @overload
    async def describeNode(
        self,
        params: DescribeNodeParameters,
        session_id: str | None = None,
    ) -> DescribeNodeResult: ...

    @overload
    async def describeNode(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[DescribeNodeParameters],
    ) -> DescribeNodeResult: ...

    async def describeNode(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> DescribeNodeResult:
        """Describes node given its id, does not require domain to be enabled. Does not start tracking any objects, can be used for automation."""

        return cast(
            DescribeNodeResult,
            await self._command("describeNode", params, session_id, kwargs),
        )

    @overload
    async def scrollIntoViewIfNeeded(
        self,
        params: ScrollIntoViewIfNeededParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def scrollIntoViewIfNeeded(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[ScrollIntoViewIfNeededParameters],
    ) -> JsonObject: ...

    async def scrollIntoViewIfNeeded(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Scrolls the specified rect of the given node into view if not already visible. Note: exactly one between nodeId, backendNodeId and objectId should be passed to identify the node."""

        return await self._command("scrollIntoViewIfNeeded", params, session_id, kwargs)

    async def disable(
        self,
        session_id: str | None = None,
    ) -> JsonObject:
        """Disables DOM agent for the given page."""

        return await self._command("disable", None, session_id, {})

    @overload
    async def discardSearchResults(
        self,
        params: DiscardSearchResultsParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def discardSearchResults(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[DiscardSearchResultsParameters],
    ) -> JsonObject: ...

    async def discardSearchResults(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Discards search results from the session with the given id. `getSearchResults` should no longer be called for that search."""

        return await self._command("discardSearchResults", params, session_id, kwargs)

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
        """Enables DOM agent for the given page."""

        return await self._command("enable", params, session_id, kwargs)

    @overload
    async def focus(
        self,
        params: FocusParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def focus(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[FocusParameters],
    ) -> JsonObject: ...

    async def focus(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Focuses the given element."""

        return await self._command("focus", params, session_id, kwargs)

    @overload
    async def getAttributes(
        self,
        params: GetAttributesParameters,
        session_id: str | None = None,
    ) -> GetAttributesResult: ...

    @overload
    async def getAttributes(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[GetAttributesParameters],
    ) -> GetAttributesResult: ...

    async def getAttributes(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> GetAttributesResult:
        """Returns attributes for the specified node."""

        return cast(
            GetAttributesResult,
            await self._command("getAttributes", params, session_id, kwargs),
        )

    @overload
    async def getBoxModel(
        self,
        params: GetBoxModelParameters,
        session_id: str | None = None,
    ) -> GetBoxModelResult: ...

    @overload
    async def getBoxModel(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[GetBoxModelParameters],
    ) -> GetBoxModelResult: ...

    async def getBoxModel(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> GetBoxModelResult:
        """Returns boxes for the given node."""

        return cast(
            GetBoxModelResult,
            await self._command("getBoxModel", params, session_id, kwargs),
        )

    @overload
    async def getContentQuads(
        self,
        params: GetContentQuadsParameters,
        session_id: str | None = None,
    ) -> GetContentQuadsResult: ...

    @overload
    async def getContentQuads(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[GetContentQuadsParameters],
    ) -> GetContentQuadsResult: ...

    async def getContentQuads(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> GetContentQuadsResult:
        """Returns quads that describe node position on the page. This method might return multiple quads for inline nodes."""

        return cast(
            GetContentQuadsResult,
            await self._command("getContentQuads", params, session_id, kwargs),
        )

    @overload
    async def getDocument(
        self,
        params: GetDocumentParameters,
        session_id: str | None = None,
    ) -> GetDocumentResult: ...

    @overload
    async def getDocument(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[GetDocumentParameters],
    ) -> GetDocumentResult: ...

    async def getDocument(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> GetDocumentResult:
        """Returns the root DOM node (and optionally the subtree) to the caller. Implicitly enables the DOM domain events for the current target."""

        return cast(
            GetDocumentResult,
            await self._command("getDocument", params, session_id, kwargs),
        )

    @overload
    async def getFlattenedDocument(
        self,
        params: GetFlattenedDocumentParameters,
        session_id: str | None = None,
    ) -> GetFlattenedDocumentResult: ...

    @overload
    async def getFlattenedDocument(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[GetFlattenedDocumentParameters],
    ) -> GetFlattenedDocumentResult: ...

    async def getFlattenedDocument(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> GetFlattenedDocumentResult:
        """Returns the root DOM node (and optionally the subtree) to the caller. Deprecated, as it is not designed to work well with the rest of the DOM agent. Use DOMSnapshot.captureSnapshot instead."""

        return cast(
            GetFlattenedDocumentResult,
            await self._command("getFlattenedDocument", params, session_id, kwargs),
        )

    @overload
    async def getNodesForSubtreeByStyle(
        self,
        params: GetNodesForSubtreeByStyleParameters,
        session_id: str | None = None,
    ) -> GetNodesForSubtreeByStyleResult: ...

    @overload
    async def getNodesForSubtreeByStyle(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[GetNodesForSubtreeByStyleParameters],
    ) -> GetNodesForSubtreeByStyleResult: ...

    async def getNodesForSubtreeByStyle(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> GetNodesForSubtreeByStyleResult:
        """Finds nodes with a given computed style in a subtree."""

        return cast(
            GetNodesForSubtreeByStyleResult,
            await self._command(
                "getNodesForSubtreeByStyle", params, session_id, kwargs
            ),
        )

    @overload
    async def getNodeForLocation(
        self,
        params: GetNodeForLocationParameters,
        session_id: str | None = None,
    ) -> GetNodeForLocationResult: ...

    @overload
    async def getNodeForLocation(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[GetNodeForLocationParameters],
    ) -> GetNodeForLocationResult: ...

    async def getNodeForLocation(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> GetNodeForLocationResult:
        """Returns node id at given location. Depending on whether DOM domain is enabled, nodeId is either returned or not."""

        return cast(
            GetNodeForLocationResult,
            await self._command("getNodeForLocation", params, session_id, kwargs),
        )

    @overload
    async def getOuterHTML(
        self,
        params: GetOuterHTMLParameters,
        session_id: str | None = None,
    ) -> GetOuterHTMLResult: ...

    @overload
    async def getOuterHTML(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[GetOuterHTMLParameters],
    ) -> GetOuterHTMLResult: ...

    async def getOuterHTML(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> GetOuterHTMLResult:
        """Returns node's HTML markup."""

        return cast(
            GetOuterHTMLResult,
            await self._command("getOuterHTML", params, session_id, kwargs),
        )

    @overload
    async def getRelayoutBoundary(
        self,
        params: GetRelayoutBoundaryParameters,
        session_id: str | None = None,
    ) -> GetRelayoutBoundaryResult: ...

    @overload
    async def getRelayoutBoundary(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[GetRelayoutBoundaryParameters],
    ) -> GetRelayoutBoundaryResult: ...

    async def getRelayoutBoundary(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> GetRelayoutBoundaryResult:
        """Returns the id of the nearest ancestor that is a relayout boundary."""

        return cast(
            GetRelayoutBoundaryResult,
            await self._command("getRelayoutBoundary", params, session_id, kwargs),
        )

    @overload
    async def getSearchResults(
        self,
        params: GetSearchResultsParameters,
        session_id: str | None = None,
    ) -> GetSearchResultsResult: ...

    @overload
    async def getSearchResults(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[GetSearchResultsParameters],
    ) -> GetSearchResultsResult: ...

    async def getSearchResults(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> GetSearchResultsResult:
        """Returns search results from given `fromIndex` to given `toIndex` from the search with the given identifier."""

        return cast(
            GetSearchResultsResult,
            await self._command("getSearchResults", params, session_id, kwargs),
        )

    async def hideHighlight(
        self,
        session_id: str | None = None,
    ) -> JsonObject:
        """Hides any highlight."""

        return await self._command("hideHighlight", None, session_id, {})

    async def highlightNode(
        self,
        session_id: str | None = None,
    ) -> JsonObject:
        """Highlights DOM node."""

        return await self._command("highlightNode", None, session_id, {})

    async def highlightRect(
        self,
        session_id: str | None = None,
    ) -> JsonObject:
        """Highlights given rectangle."""

        return await self._command("highlightRect", None, session_id, {})

    async def markUndoableState(
        self,
        session_id: str | None = None,
    ) -> JsonObject:
        """Marks last undoable state."""

        return await self._command("markUndoableState", None, session_id, {})

    @overload
    async def moveTo(
        self,
        params: MoveToParameters,
        session_id: str | None = None,
    ) -> MoveToResult: ...

    @overload
    async def moveTo(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[MoveToParameters],
    ) -> MoveToResult: ...

    async def moveTo(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> MoveToResult:
        """Moves node into the new container, places it before the given anchor."""

        return cast(
            MoveToResult, await self._command("moveTo", params, session_id, kwargs)
        )

    @overload
    async def performSearch(
        self,
        params: PerformSearchParameters,
        session_id: str | None = None,
    ) -> PerformSearchResult: ...

    @overload
    async def performSearch(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[PerformSearchParameters],
    ) -> PerformSearchResult: ...

    async def performSearch(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> PerformSearchResult:
        """Searches for a given string in the DOM tree. Use `getSearchResults` to access search results or `cancelSearch` to end this search session."""

        return cast(
            PerformSearchResult,
            await self._command("performSearch", params, session_id, kwargs),
        )

    @overload
    async def pushNodeByPathToFrontend(
        self,
        params: PushNodeByPathToFrontendParameters,
        session_id: str | None = None,
    ) -> PushNodeByPathToFrontendResult: ...

    @overload
    async def pushNodeByPathToFrontend(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[PushNodeByPathToFrontendParameters],
    ) -> PushNodeByPathToFrontendResult: ...

    async def pushNodeByPathToFrontend(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> PushNodeByPathToFrontendResult:
        """Requests that the node is sent to the caller given its path. // FIXME, use XPath"""

        return cast(
            PushNodeByPathToFrontendResult,
            await self._command("pushNodeByPathToFrontend", params, session_id, kwargs),
        )

    @overload
    async def pushNodesByBackendIdsToFrontend(
        self,
        params: PushNodesByBackendIdsToFrontendParameters,
        session_id: str | None = None,
    ) -> PushNodesByBackendIdsToFrontendResult: ...

    @overload
    async def pushNodesByBackendIdsToFrontend(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[PushNodesByBackendIdsToFrontendParameters],
    ) -> PushNodesByBackendIdsToFrontendResult: ...

    async def pushNodesByBackendIdsToFrontend(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> PushNodesByBackendIdsToFrontendResult:
        """Requests that a batch of nodes is sent to the caller given their backend node ids."""

        return cast(
            PushNodesByBackendIdsToFrontendResult,
            await self._command(
                "pushNodesByBackendIdsToFrontend", params, session_id, kwargs
            ),
        )

    @overload
    async def querySelector(
        self,
        params: QuerySelectorParameters,
        session_id: str | None = None,
    ) -> QuerySelectorResult: ...

    @overload
    async def querySelector(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[QuerySelectorParameters],
    ) -> QuerySelectorResult: ...

    async def querySelector(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> QuerySelectorResult:
        """Executes `querySelector` on a given node."""

        return cast(
            QuerySelectorResult,
            await self._command("querySelector", params, session_id, kwargs),
        )

    @overload
    async def querySelectorAll(
        self,
        params: QuerySelectorAllParameters,
        session_id: str | None = None,
    ) -> QuerySelectorAllResult: ...

    @overload
    async def querySelectorAll(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[QuerySelectorAllParameters],
    ) -> QuerySelectorAllResult: ...

    async def querySelectorAll(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> QuerySelectorAllResult:
        """Executes `querySelectorAll` on a given node."""

        return cast(
            QuerySelectorAllResult,
            await self._command("querySelectorAll", params, session_id, kwargs),
        )

    async def getTopLayerElements(
        self,
        session_id: str | None = None,
    ) -> GetTopLayerElementsResult:
        """Returns NodeIds of current top layer elements. Top layer is rendered closest to the user within a viewport, therefore its elements always appear on top of all other content."""

        return cast(
            GetTopLayerElementsResult,
            await self._command("getTopLayerElements", None, session_id, {}),
        )

    async def redo(
        self,
        session_id: str | None = None,
    ) -> JsonObject:
        """Re-does the last undone action."""

        return await self._command("redo", None, session_id, {})

    @overload
    async def removeAttribute(
        self,
        params: RemoveAttributeParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def removeAttribute(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[RemoveAttributeParameters],
    ) -> JsonObject: ...

    async def removeAttribute(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Removes attribute with given name from an element with given id."""

        return await self._command("removeAttribute", params, session_id, kwargs)

    @overload
    async def removeNode(
        self,
        params: RemoveNodeParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def removeNode(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[RemoveNodeParameters],
    ) -> JsonObject: ...

    async def removeNode(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Removes node with given id."""

        return await self._command("removeNode", params, session_id, kwargs)

    @overload
    async def requestChildNodes(
        self,
        params: RequestChildNodesParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def requestChildNodes(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[RequestChildNodesParameters],
    ) -> JsonObject: ...

    async def requestChildNodes(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Requests that children of the node with given id are returned to the caller in form of `setChildNodes` events where not only immediate children are retrieved, but all children down to the specified depth."""

        return await self._command("requestChildNodes", params, session_id, kwargs)

    @overload
    async def requestNode(
        self,
        params: RequestNodeParameters,
        session_id: str | None = None,
    ) -> RequestNodeResult: ...

    @overload
    async def requestNode(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[RequestNodeParameters],
    ) -> RequestNodeResult: ...

    async def requestNode(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> RequestNodeResult:
        """Requests that the node is sent to the caller given the JavaScript node object reference. All nodes that form the path from the node to the root are also sent to the client as a series of `setChildNodes` notifications."""

        return cast(
            RequestNodeResult,
            await self._command("requestNode", params, session_id, kwargs),
        )

    @overload
    async def resolveNode(
        self,
        params: ResolveNodeParameters,
        session_id: str | None = None,
    ) -> ResolveNodeResult: ...

    @overload
    async def resolveNode(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[ResolveNodeParameters],
    ) -> ResolveNodeResult: ...

    async def resolveNode(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> ResolveNodeResult:
        """Resolves the JavaScript node object for a given NodeId or BackendNodeId."""

        return cast(
            ResolveNodeResult,
            await self._command("resolveNode", params, session_id, kwargs),
        )

    @overload
    async def setAttributeValue(
        self,
        params: SetAttributeValueParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def setAttributeValue(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetAttributeValueParameters],
    ) -> JsonObject: ...

    async def setAttributeValue(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Sets attribute for an element with given id."""

        return await self._command("setAttributeValue", params, session_id, kwargs)

    @overload
    async def setAttributesAsText(
        self,
        params: SetAttributesAsTextParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def setAttributesAsText(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetAttributesAsTextParameters],
    ) -> JsonObject: ...

    async def setAttributesAsText(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Sets attributes on element with given id. This method is useful when user edits some existing attribute value and types in several attribute name/value pairs."""

        return await self._command("setAttributesAsText", params, session_id, kwargs)

    @overload
    async def setFileInputFiles(
        self,
        params: SetFileInputFilesParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def setFileInputFiles(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetFileInputFilesParameters],
    ) -> JsonObject: ...

    async def setFileInputFiles(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Sets files for the given file input element."""

        return await self._command("setFileInputFiles", params, session_id, kwargs)

    @overload
    async def setNodeStackTracesEnabled(
        self,
        params: SetNodeStackTracesEnabledParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def setNodeStackTracesEnabled(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetNodeStackTracesEnabledParameters],
    ) -> JsonObject: ...

    async def setNodeStackTracesEnabled(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Sets if stack traces should be captured for Nodes. See `Node.getNodeStackTraces`. Default is disabled."""

        return await self._command(
            "setNodeStackTracesEnabled", params, session_id, kwargs
        )

    @overload
    async def getNodeStackTraces(
        self,
        params: GetNodeStackTracesParameters,
        session_id: str | None = None,
    ) -> GetNodeStackTracesResult: ...

    @overload
    async def getNodeStackTraces(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[GetNodeStackTracesParameters],
    ) -> GetNodeStackTracesResult: ...

    async def getNodeStackTraces(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> GetNodeStackTracesResult:
        """Gets stack traces associated with a Node. As of now, only provides stack trace for Node creation."""

        return cast(
            GetNodeStackTracesResult,
            await self._command("getNodeStackTraces", params, session_id, kwargs),
        )

    @overload
    async def getFileInfo(
        self,
        params: GetFileInfoParameters,
        session_id: str | None = None,
    ) -> GetFileInfoResult: ...

    @overload
    async def getFileInfo(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[GetFileInfoParameters],
    ) -> GetFileInfoResult: ...

    async def getFileInfo(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> GetFileInfoResult:
        """Returns file information for the given File wrapper."""

        return cast(
            GetFileInfoResult,
            await self._command("getFileInfo", params, session_id, kwargs),
        )

    @overload
    async def setInspectedNode(
        self,
        params: SetInspectedNodeParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def setInspectedNode(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetInspectedNodeParameters],
    ) -> JsonObject: ...

    async def setInspectedNode(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Enables console to refer to the node with given id via $x (see Command Line API for more details $x functions)."""

        return await self._command("setInspectedNode", params, session_id, kwargs)

    @overload
    async def setNodeName(
        self,
        params: SetNodeNameParameters,
        session_id: str | None = None,
    ) -> SetNodeNameResult: ...

    @overload
    async def setNodeName(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetNodeNameParameters],
    ) -> SetNodeNameResult: ...

    async def setNodeName(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> SetNodeNameResult:
        """Sets node name for a node with given id."""

        return cast(
            SetNodeNameResult,
            await self._command("setNodeName", params, session_id, kwargs),
        )

    @overload
    async def setNodeValue(
        self,
        params: SetNodeValueParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def setNodeValue(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetNodeValueParameters],
    ) -> JsonObject: ...

    async def setNodeValue(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Sets node value for a node with given id."""

        return await self._command("setNodeValue", params, session_id, kwargs)

    @overload
    async def setOuterHTML(
        self,
        params: SetOuterHTMLParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def setOuterHTML(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetOuterHTMLParameters],
    ) -> JsonObject: ...

    async def setOuterHTML(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Sets node HTML markup, returns new node id."""

        return await self._command("setOuterHTML", params, session_id, kwargs)

    async def undo(
        self,
        session_id: str | None = None,
    ) -> JsonObject:
        """Undoes the last performed action."""

        return await self._command("undo", None, session_id, {})

    @overload
    async def getFrameOwner(
        self,
        params: GetFrameOwnerParameters,
        session_id: str | None = None,
    ) -> GetFrameOwnerResult: ...

    @overload
    async def getFrameOwner(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[GetFrameOwnerParameters],
    ) -> GetFrameOwnerResult: ...

    async def getFrameOwner(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> GetFrameOwnerResult:
        """Returns iframe node that owns iframe with the given domain."""

        return cast(
            GetFrameOwnerResult,
            await self._command("getFrameOwner", params, session_id, kwargs),
        )

    @overload
    async def getContainerForNode(
        self,
        params: GetContainerForNodeParameters,
        session_id: str | None = None,
    ) -> GetContainerForNodeResult: ...

    @overload
    async def getContainerForNode(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[GetContainerForNodeParameters],
    ) -> GetContainerForNodeResult: ...

    async def getContainerForNode(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> GetContainerForNodeResult:
        """Returns the query container of the given node based on container query conditions: containerName, physical, and logical axes. If no axes are provided, the style container is returned, which is the direct parent or the closest element with a matching container-name."""

        return cast(
            GetContainerForNodeResult,
            await self._command("getContainerForNode", params, session_id, kwargs),
        )

    @overload
    async def getQueryingDescendantsForContainer(
        self,
        params: GetQueryingDescendantsForContainerParameters,
        session_id: str | None = None,
    ) -> GetQueryingDescendantsForContainerResult: ...

    @overload
    async def getQueryingDescendantsForContainer(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[GetQueryingDescendantsForContainerParameters],
    ) -> GetQueryingDescendantsForContainerResult: ...

    async def getQueryingDescendantsForContainer(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> GetQueryingDescendantsForContainerResult:
        """Returns the descendants of a container query container that have container queries against this container."""

        return cast(
            GetQueryingDescendantsForContainerResult,
            await self._command(
                "getQueryingDescendantsForContainer", params, session_id, kwargs
            ),
        )

    @overload
    def attributeModified(
        self,
        callback_or_session: EventCallback[AttributeModifiedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def attributeModified(
        self,
        callback_or_session: str,
        handler: EventCallback[AttributeModifiedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def attributeModified(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[AttributeModifiedEvent]: ...

    def attributeModified(
        self,
        callback_or_session: EventCallback[AttributeModifiedEvent] | str | None = None,
        handler: EventCallback[AttributeModifiedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[AttributeModifiedEvent] | Unsubscribe:
        """Fired when `Element`'s attribute is modified."""

        return cast(
            Awaitable[AttributeModifiedEvent] | Unsubscribe,
            self._event(
                "attributeModified",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def attributeRemoved(
        self,
        callback_or_session: EventCallback[AttributeRemovedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def attributeRemoved(
        self,
        callback_or_session: str,
        handler: EventCallback[AttributeRemovedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def attributeRemoved(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[AttributeRemovedEvent]: ...

    def attributeRemoved(
        self,
        callback_or_session: EventCallback[AttributeRemovedEvent] | str | None = None,
        handler: EventCallback[AttributeRemovedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[AttributeRemovedEvent] | Unsubscribe:
        """Fired when `Element`'s attribute is removed."""

        return cast(
            Awaitable[AttributeRemovedEvent] | Unsubscribe,
            self._event(
                "attributeRemoved",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def characterDataModified(
        self,
        callback_or_session: EventCallback[CharacterDataModifiedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def characterDataModified(
        self,
        callback_or_session: str,
        handler: EventCallback[CharacterDataModifiedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def characterDataModified(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[CharacterDataModifiedEvent]: ...

    def characterDataModified(
        self,
        callback_or_session: EventCallback[CharacterDataModifiedEvent]
        | str
        | None = None,
        handler: EventCallback[CharacterDataModifiedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[CharacterDataModifiedEvent] | Unsubscribe:
        """Mirrors `DOMCharacterDataModified` event."""

        return cast(
            Awaitable[CharacterDataModifiedEvent] | Unsubscribe,
            self._event(
                "characterDataModified",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def childNodeCountUpdated(
        self,
        callback_or_session: EventCallback[ChildNodeCountUpdatedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def childNodeCountUpdated(
        self,
        callback_or_session: str,
        handler: EventCallback[ChildNodeCountUpdatedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def childNodeCountUpdated(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[ChildNodeCountUpdatedEvent]: ...

    def childNodeCountUpdated(
        self,
        callback_or_session: EventCallback[ChildNodeCountUpdatedEvent]
        | str
        | None = None,
        handler: EventCallback[ChildNodeCountUpdatedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[ChildNodeCountUpdatedEvent] | Unsubscribe:
        """Fired when `Container`'s child node count has changed."""

        return cast(
            Awaitable[ChildNodeCountUpdatedEvent] | Unsubscribe,
            self._event(
                "childNodeCountUpdated",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def childNodeInserted(
        self,
        callback_or_session: EventCallback[ChildNodeInsertedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def childNodeInserted(
        self,
        callback_or_session: str,
        handler: EventCallback[ChildNodeInsertedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def childNodeInserted(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[ChildNodeInsertedEvent]: ...

    def childNodeInserted(
        self,
        callback_or_session: EventCallback[ChildNodeInsertedEvent] | str | None = None,
        handler: EventCallback[ChildNodeInsertedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[ChildNodeInsertedEvent] | Unsubscribe:
        """Mirrors `DOMNodeInserted` event."""

        return cast(
            Awaitable[ChildNodeInsertedEvent] | Unsubscribe,
            self._event(
                "childNodeInserted",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def childNodeRemoved(
        self,
        callback_or_session: EventCallback[ChildNodeRemovedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def childNodeRemoved(
        self,
        callback_or_session: str,
        handler: EventCallback[ChildNodeRemovedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def childNodeRemoved(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[ChildNodeRemovedEvent]: ...

    def childNodeRemoved(
        self,
        callback_or_session: EventCallback[ChildNodeRemovedEvent] | str | None = None,
        handler: EventCallback[ChildNodeRemovedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[ChildNodeRemovedEvent] | Unsubscribe:
        """Mirrors `DOMNodeRemoved` event."""

        return cast(
            Awaitable[ChildNodeRemovedEvent] | Unsubscribe,
            self._event(
                "childNodeRemoved",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def distributedNodesUpdated(
        self,
        callback_or_session: EventCallback[DistributedNodesUpdatedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def distributedNodesUpdated(
        self,
        callback_or_session: str,
        handler: EventCallback[DistributedNodesUpdatedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def distributedNodesUpdated(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[DistributedNodesUpdatedEvent]: ...

    def distributedNodesUpdated(
        self,
        callback_or_session: EventCallback[DistributedNodesUpdatedEvent]
        | str
        | None = None,
        handler: EventCallback[DistributedNodesUpdatedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[DistributedNodesUpdatedEvent] | Unsubscribe:
        """Called when distribution is changed."""

        return cast(
            Awaitable[DistributedNodesUpdatedEvent] | Unsubscribe,
            self._event(
                "distributedNodesUpdated",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def documentUpdated(
        self,
        callback_or_session: EventCallback[JsonObject],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def documentUpdated(
        self,
        callback_or_session: str,
        handler: EventCallback[JsonObject],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def documentUpdated(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[JsonObject]: ...

    def documentUpdated(
        self,
        callback_or_session: EventCallback[JsonObject] | str | None = None,
        handler: EventCallback[JsonObject] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[JsonObject] | Unsubscribe:
        """Fired when `Document` has been totally updated. Node ids are no longer valid."""

        return self._event(
            "documentUpdated",
            cast(EventCallback[Mapping[str, object]] | str | None, callback_or_session),
            cast(EventCallback[Mapping[str, object]] | None, handler),
            session_id,
        )

    @overload
    def inlineStyleInvalidated(
        self,
        callback_or_session: EventCallback[InlineStyleInvalidatedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def inlineStyleInvalidated(
        self,
        callback_or_session: str,
        handler: EventCallback[InlineStyleInvalidatedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def inlineStyleInvalidated(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[InlineStyleInvalidatedEvent]: ...

    def inlineStyleInvalidated(
        self,
        callback_or_session: EventCallback[InlineStyleInvalidatedEvent]
        | str
        | None = None,
        handler: EventCallback[InlineStyleInvalidatedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[InlineStyleInvalidatedEvent] | Unsubscribe:
        """Fired when `Element`'s inline style is modified via a CSS property modification."""

        return cast(
            Awaitable[InlineStyleInvalidatedEvent] | Unsubscribe,
            self._event(
                "inlineStyleInvalidated",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def pseudoElementAdded(
        self,
        callback_or_session: EventCallback[PseudoElementAddedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def pseudoElementAdded(
        self,
        callback_or_session: str,
        handler: EventCallback[PseudoElementAddedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def pseudoElementAdded(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[PseudoElementAddedEvent]: ...

    def pseudoElementAdded(
        self,
        callback_or_session: EventCallback[PseudoElementAddedEvent] | str | None = None,
        handler: EventCallback[PseudoElementAddedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[PseudoElementAddedEvent] | Unsubscribe:
        """Called when a pseudo element is added to an element."""

        return cast(
            Awaitable[PseudoElementAddedEvent] | Unsubscribe,
            self._event(
                "pseudoElementAdded",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def topLayerElementsUpdated(
        self,
        callback_or_session: EventCallback[JsonObject],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def topLayerElementsUpdated(
        self,
        callback_or_session: str,
        handler: EventCallback[JsonObject],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def topLayerElementsUpdated(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[JsonObject]: ...

    def topLayerElementsUpdated(
        self,
        callback_or_session: EventCallback[JsonObject] | str | None = None,
        handler: EventCallback[JsonObject] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[JsonObject] | Unsubscribe:
        """Called when top layer elements are changed."""

        return self._event(
            "topLayerElementsUpdated",
            cast(EventCallback[Mapping[str, object]] | str | None, callback_or_session),
            cast(EventCallback[Mapping[str, object]] | None, handler),
            session_id,
        )

    @overload
    def pseudoElementRemoved(
        self,
        callback_or_session: EventCallback[PseudoElementRemovedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def pseudoElementRemoved(
        self,
        callback_or_session: str,
        handler: EventCallback[PseudoElementRemovedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def pseudoElementRemoved(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[PseudoElementRemovedEvent]: ...

    def pseudoElementRemoved(
        self,
        callback_or_session: EventCallback[PseudoElementRemovedEvent]
        | str
        | None = None,
        handler: EventCallback[PseudoElementRemovedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[PseudoElementRemovedEvent] | Unsubscribe:
        """Called when a pseudo element is removed from an element."""

        return cast(
            Awaitable[PseudoElementRemovedEvent] | Unsubscribe,
            self._event(
                "pseudoElementRemoved",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def setChildNodes(
        self,
        callback_or_session: EventCallback[SetChildNodesEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def setChildNodes(
        self,
        callback_or_session: str,
        handler: EventCallback[SetChildNodesEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def setChildNodes(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[SetChildNodesEvent]: ...

    def setChildNodes(
        self,
        callback_or_session: EventCallback[SetChildNodesEvent] | str | None = None,
        handler: EventCallback[SetChildNodesEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[SetChildNodesEvent] | Unsubscribe:
        """Fired when backend wants to provide client with the missing DOM structure. This happens upon most of the calls requesting node ids."""

        return cast(
            Awaitable[SetChildNodesEvent] | Unsubscribe,
            self._event(
                "setChildNodes",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def shadowRootPopped(
        self,
        callback_or_session: EventCallback[ShadowRootPoppedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def shadowRootPopped(
        self,
        callback_or_session: str,
        handler: EventCallback[ShadowRootPoppedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def shadowRootPopped(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[ShadowRootPoppedEvent]: ...

    def shadowRootPopped(
        self,
        callback_or_session: EventCallback[ShadowRootPoppedEvent] | str | None = None,
        handler: EventCallback[ShadowRootPoppedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[ShadowRootPoppedEvent] | Unsubscribe:
        """Called when shadow root is popped from the element."""

        return cast(
            Awaitable[ShadowRootPoppedEvent] | Unsubscribe,
            self._event(
                "shadowRootPopped",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def shadowRootPushed(
        self,
        callback_or_session: EventCallback[ShadowRootPushedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def shadowRootPushed(
        self,
        callback_or_session: str,
        handler: EventCallback[ShadowRootPushedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def shadowRootPushed(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[ShadowRootPushedEvent]: ...

    def shadowRootPushed(
        self,
        callback_or_session: EventCallback[ShadowRootPushedEvent] | str | None = None,
        handler: EventCallback[ShadowRootPushedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[ShadowRootPushedEvent] | Unsubscribe:
        """Called when shadow root is pushed into the element."""

        return cast(
            Awaitable[ShadowRootPushedEvent] | Unsubscribe,
            self._event(
                "shadowRootPushed",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )


__all__ = [
    "DOM",
    "RGBA",
    "AttributeModifiedEvent",
    "AttributeRemovedEvent",
    "BackendNode",
    "BackendNodeId",
    "BoxModel",
    "CSSComputedStyleProperty",
    "CharacterDataModifiedEvent",
    "ChildNodeCountUpdatedEvent",
    "ChildNodeInsertedEvent",
    "ChildNodeRemovedEvent",
    "CollectClassNamesFromSubtreeParameters",
    "CollectClassNamesFromSubtreeResult",
    "CompatibilityMode",
    "CopyToParameters",
    "CopyToResult",
    "DescribeNodeParameters",
    "DescribeNodeResult",
    "DiscardSearchResultsParameters",
    "DistributedNodesUpdatedEvent",
    "EnableParameters",
    "FocusParameters",
    "GetAttributesParameters",
    "GetAttributesResult",
    "GetBoxModelParameters",
    "GetBoxModelResult",
    "GetContainerForNodeParameters",
    "GetContainerForNodeResult",
    "GetContentQuadsParameters",
    "GetContentQuadsResult",
    "GetDocumentParameters",
    "GetDocumentResult",
    "GetFileInfoParameters",
    "GetFileInfoResult",
    "GetFlattenedDocumentParameters",
    "GetFlattenedDocumentResult",
    "GetFrameOwnerParameters",
    "GetFrameOwnerResult",
    "GetNodeForLocationParameters",
    "GetNodeForLocationResult",
    "GetNodeStackTracesParameters",
    "GetNodeStackTracesResult",
    "GetNodesForSubtreeByStyleParameters",
    "GetNodesForSubtreeByStyleResult",
    "GetOuterHTMLParameters",
    "GetOuterHTMLResult",
    "GetQueryingDescendantsForContainerParameters",
    "GetQueryingDescendantsForContainerResult",
    "GetRelayoutBoundaryParameters",
    "GetRelayoutBoundaryResult",
    "GetSearchResultsParameters",
    "GetSearchResultsResult",
    "GetTopLayerElementsResult",
    "InlineStyleInvalidatedEvent",
    "LogicalAxes",
    "MoveToParameters",
    "MoveToResult",
    "Node",
    "NodeId",
    "PerformSearchParameters",
    "PerformSearchResult",
    "PhysicalAxes",
    "PseudoElementAddedEvent",
    "PseudoElementRemovedEvent",
    "PseudoType",
    "PushNodeByPathToFrontendParameters",
    "PushNodeByPathToFrontendResult",
    "PushNodesByBackendIdsToFrontendParameters",
    "PushNodesByBackendIdsToFrontendResult",
    "Quad",
    "QuerySelectorAllParameters",
    "QuerySelectorAllResult",
    "QuerySelectorParameters",
    "QuerySelectorResult",
    "Rect",
    "RemoveAttributeParameters",
    "RemoveNodeParameters",
    "RequestChildNodesParameters",
    "RequestNodeParameters",
    "RequestNodeResult",
    "ResolveNodeParameters",
    "ResolveNodeResult",
    "ScrollIntoViewIfNeededParameters",
    "SetAttributeValueParameters",
    "SetAttributesAsTextParameters",
    "SetChildNodesEvent",
    "SetFileInputFilesParameters",
    "SetInspectedNodeParameters",
    "SetNodeNameParameters",
    "SetNodeNameResult",
    "SetNodeStackTracesEnabledParameters",
    "SetNodeValueParameters",
    "SetOuterHTMLParameters",
    "ShadowRootPoppedEvent",
    "ShadowRootPushedEvent",
    "ShadowRootType",
    "ShapeOutsideInfo",
]
