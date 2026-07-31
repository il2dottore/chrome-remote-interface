"""Generated bindings for the CDP Accessibility domain. Do not edit manually."""

from __future__ import annotations

from collections.abc import Awaitable, Mapping
from typing import TYPE_CHECKING, Literal, TypeAlias, cast, overload

from typing_extensions import NotRequired, TypedDict, Unpack

from cdp.domain import Domain as BaseDomain, EventCallback, Unsubscribe
from cdp.types import JsonObject, JsonValue

if TYPE_CHECKING:
    from . import dom as DOM
    from . import page as Page
    from . import runtime as Runtime


AXNodeId: TypeAlias = str

AXValueType: TypeAlias = Literal[
    "boolean",
    "tristate",
    "booleanOrUndefined",
    "idref",
    "idrefList",
    "integer",
    "node",
    "nodeList",
    "number",
    "string",
    "computedString",
    "token",
    "tokenList",
    "domRelation",
    "role",
    "internalRole",
    "valueUndefined",
]

AXValueSourceType: TypeAlias = Literal[
    "attribute", "implicit", "style", "contents", "placeholder", "relatedElement"
]

AXValueNativeSourceType: TypeAlias = Literal[
    "description",
    "figcaption",
    "label",
    "labelfor",
    "labelwrapped",
    "legend",
    "rubyannotation",
    "tablecaption",
    "title",
    "other",
]


class AXValueSource(TypedDict):
    type: AXValueSourceType
    value: NotRequired[AXValue]
    attribute: NotRequired[str]
    attributeValue: NotRequired[AXValue]
    superseded: NotRequired[bool]
    nativeSource: NotRequired[AXValueNativeSourceType]
    nativeSourceValue: NotRequired[AXValue]
    invalid: NotRequired[bool]
    invalidReason: NotRequired[str]


class AXRelatedNode(TypedDict):
    backendDOMNodeId: DOM.BackendNodeId
    idref: NotRequired[str]
    text: NotRequired[str]


class AXProperty(TypedDict):
    name: AXPropertyName
    value: AXValue


class AXValue(TypedDict):
    type: AXValueType
    value: NotRequired[JsonValue]
    relatedNodes: NotRequired[list[AXRelatedNode]]
    sources: NotRequired[list[AXValueSource]]


AXPropertyName: TypeAlias = Literal[
    "actions",
    "busy",
    "disabled",
    "editable",
    "focusable",
    "focused",
    "hidden",
    "hiddenRoot",
    "invalid",
    "keyshortcuts",
    "settable",
    "roledescription",
    "live",
    "atomic",
    "relevant",
    "root",
    "autocomplete",
    "hasPopup",
    "level",
    "multiselectable",
    "orientation",
    "multiline",
    "readonly",
    "required",
    "valuemin",
    "valuemax",
    "valuetext",
    "checked",
    "expanded",
    "modal",
    "pressed",
    "selected",
    "activedescendant",
    "controls",
    "describedby",
    "details",
    "errormessage",
    "flowto",
    "labelledby",
    "owns",
    "url",
    "activeFullscreenElement",
    "activeModalDialog",
    "activeAriaModalDialog",
    "ariaHiddenElement",
    "ariaHiddenSubtree",
    "emptyAlt",
    "emptyText",
    "inertElement",
    "inertSubtree",
    "labelContainer",
    "labelFor",
    "notRendered",
    "notVisible",
    "presentationalRole",
    "probablyPresentational",
    "inactiveCarouselTabContent",
    "uninteresting",
]


class AXNode(TypedDict):
    nodeId: AXNodeId
    ignored: bool
    ignoredReasons: NotRequired[list[AXProperty]]
    role: NotRequired[AXValue]
    chromeRole: NotRequired[AXValue]
    name: NotRequired[AXValue]
    description: NotRequired[AXValue]
    value: NotRequired[AXValue]
    properties: NotRequired[list[AXProperty]]
    parentId: NotRequired[AXNodeId]
    childIds: NotRequired[list[AXNodeId]]
    backendDOMNodeId: NotRequired[DOM.BackendNodeId]
    frameId: NotRequired[Page.FrameId]


class GetPartialAXTreeParameters(TypedDict):
    nodeId: NotRequired[DOM.NodeId]
    backendNodeId: NotRequired[DOM.BackendNodeId]
    objectId: NotRequired[Runtime.RemoteObjectId]
    fetchRelatives: NotRequired[bool]


class GetPartialAXTreeResult(TypedDict):
    nodes: list[AXNode]


class GetFullAXTreeParameters(TypedDict):
    depth: NotRequired[int]
    frameId: NotRequired[Page.FrameId]


class GetFullAXTreeResult(TypedDict):
    nodes: list[AXNode]


class GetRootAXNodeParameters(TypedDict):
    frameId: NotRequired[Page.FrameId]


class GetRootAXNodeResult(TypedDict):
    node: AXNode


class GetAXNodeAndAncestorsParameters(TypedDict):
    nodeId: NotRequired[DOM.NodeId]
    backendNodeId: NotRequired[DOM.BackendNodeId]
    objectId: NotRequired[Runtime.RemoteObjectId]


class GetAXNodeAndAncestorsResult(TypedDict):
    nodes: list[AXNode]


class GetChildAXNodesParameters(TypedDict):
    id: AXNodeId
    frameId: NotRequired[Page.FrameId]


class GetChildAXNodesResult(TypedDict):
    nodes: list[AXNode]


class QueryAXTreeParameters(TypedDict):
    nodeId: NotRequired[DOM.NodeId]
    backendNodeId: NotRequired[DOM.BackendNodeId]
    objectId: NotRequired[Runtime.RemoteObjectId]
    accessibleName: NotRequired[str]
    role: NotRequired[str]


class QueryAXTreeResult(TypedDict):
    nodes: list[AXNode]


class LoadCompleteEvent(TypedDict):
    root: AXNode


class NodesUpdatedEvent(TypedDict):
    nodes: list[AXNode]


class Accessibility(BaseDomain):
    """The CDP Accessibility domain."""

    domain_name = "Accessibility"

    async def disable(
        self,
        session_id: str | None = None,
    ) -> JsonObject:
        """Disables the accessibility domain."""

        return await self._command("disable", None, session_id, {})

    async def enable(
        self,
        session_id: str | None = None,
    ) -> JsonObject:
        """Enables the accessibility domain which causes `AXNodeId`s to remain consistent between method calls. This turns on accessibility for the page, which can impact performance until accessibility is disabled."""

        return await self._command("enable", None, session_id, {})

    @overload
    async def getPartialAXTree(
        self,
        params: GetPartialAXTreeParameters,
        session_id: str | None = None,
    ) -> GetPartialAXTreeResult: ...

    @overload
    async def getPartialAXTree(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[GetPartialAXTreeParameters],
    ) -> GetPartialAXTreeResult: ...

    async def getPartialAXTree(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> GetPartialAXTreeResult:
        """Fetches the accessibility node and partial accessibility tree for this DOM node, if it exists."""

        return cast(
            GetPartialAXTreeResult,
            await self._command("getPartialAXTree", params, session_id, kwargs),
        )

    @overload
    async def getFullAXTree(
        self,
        params: GetFullAXTreeParameters,
        session_id: str | None = None,
    ) -> GetFullAXTreeResult: ...

    @overload
    async def getFullAXTree(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[GetFullAXTreeParameters],
    ) -> GetFullAXTreeResult: ...

    async def getFullAXTree(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> GetFullAXTreeResult:
        """Fetches the entire accessibility tree for the root Document"""

        return cast(
            GetFullAXTreeResult,
            await self._command("getFullAXTree", params, session_id, kwargs),
        )

    @overload
    async def getRootAXNode(
        self,
        params: GetRootAXNodeParameters,
        session_id: str | None = None,
    ) -> GetRootAXNodeResult: ...

    @overload
    async def getRootAXNode(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[GetRootAXNodeParameters],
    ) -> GetRootAXNodeResult: ...

    async def getRootAXNode(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> GetRootAXNodeResult:
        """Fetches the root node. Requires `enable()` to have been called previously."""

        return cast(
            GetRootAXNodeResult,
            await self._command("getRootAXNode", params, session_id, kwargs),
        )

    @overload
    async def getAXNodeAndAncestors(
        self,
        params: GetAXNodeAndAncestorsParameters,
        session_id: str | None = None,
    ) -> GetAXNodeAndAncestorsResult: ...

    @overload
    async def getAXNodeAndAncestors(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[GetAXNodeAndAncestorsParameters],
    ) -> GetAXNodeAndAncestorsResult: ...

    async def getAXNodeAndAncestors(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> GetAXNodeAndAncestorsResult:
        """Fetches a node and all ancestors up to and including the root. Requires `enable()` to have been called previously."""

        return cast(
            GetAXNodeAndAncestorsResult,
            await self._command("getAXNodeAndAncestors", params, session_id, kwargs),
        )

    @overload
    async def getChildAXNodes(
        self,
        params: GetChildAXNodesParameters,
        session_id: str | None = None,
    ) -> GetChildAXNodesResult: ...

    @overload
    async def getChildAXNodes(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[GetChildAXNodesParameters],
    ) -> GetChildAXNodesResult: ...

    async def getChildAXNodes(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> GetChildAXNodesResult:
        """Fetches a particular accessibility node by AXNodeId. Requires `enable()` to have been called previously."""

        return cast(
            GetChildAXNodesResult,
            await self._command("getChildAXNodes", params, session_id, kwargs),
        )

    @overload
    async def queryAXTree(
        self,
        params: QueryAXTreeParameters,
        session_id: str | None = None,
    ) -> QueryAXTreeResult: ...

    @overload
    async def queryAXTree(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[QueryAXTreeParameters],
    ) -> QueryAXTreeResult: ...

    async def queryAXTree(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> QueryAXTreeResult:
        """Query a DOM node's accessibility subtree for accessible name and role. This command computes the name and role for all nodes in the subtree, including those that are ignored for accessibility, and returns those that match the specified name and role. If no DOM node is specified, or the DOM node does not exist, the command returns an error. If neither `accessibleName` or `role` is specified, it returns all the accessibility nodes in the subtree."""

        return cast(
            QueryAXTreeResult,
            await self._command("queryAXTree", params, session_id, kwargs),
        )

    @overload
    def loadComplete(
        self,
        callback_or_session: EventCallback[LoadCompleteEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def loadComplete(
        self,
        callback_or_session: str,
        handler: EventCallback[LoadCompleteEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def loadComplete(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[LoadCompleteEvent]: ...

    def loadComplete(
        self,
        callback_or_session: EventCallback[LoadCompleteEvent] | str | None = None,
        handler: EventCallback[LoadCompleteEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[LoadCompleteEvent] | Unsubscribe:
        """The loadComplete event mirrors the load complete event sent by the browser to assistive technology when the web page has finished loading."""

        return cast(
            Awaitable[LoadCompleteEvent] | Unsubscribe,
            self._event(
                "loadComplete",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def nodesUpdated(
        self,
        callback_or_session: EventCallback[NodesUpdatedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def nodesUpdated(
        self,
        callback_or_session: str,
        handler: EventCallback[NodesUpdatedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def nodesUpdated(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[NodesUpdatedEvent]: ...

    def nodesUpdated(
        self,
        callback_or_session: EventCallback[NodesUpdatedEvent] | str | None = None,
        handler: EventCallback[NodesUpdatedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[NodesUpdatedEvent] | Unsubscribe:
        """The nodesUpdated event is sent every time a previously requested node has changed the in tree."""

        return cast(
            Awaitable[NodesUpdatedEvent] | Unsubscribe,
            self._event(
                "nodesUpdated",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )


__all__ = [
    "AXNode",
    "AXNodeId",
    "AXProperty",
    "AXPropertyName",
    "AXRelatedNode",
    "AXValue",
    "AXValueNativeSourceType",
    "AXValueSource",
    "AXValueSourceType",
    "AXValueType",
    "Accessibility",
    "GetAXNodeAndAncestorsParameters",
    "GetAXNodeAndAncestorsResult",
    "GetChildAXNodesParameters",
    "GetChildAXNodesResult",
    "GetFullAXTreeParameters",
    "GetFullAXTreeResult",
    "GetPartialAXTreeParameters",
    "GetPartialAXTreeResult",
    "GetRootAXNodeParameters",
    "GetRootAXNodeResult",
    "LoadCompleteEvent",
    "NodesUpdatedEvent",
    "QueryAXTreeParameters",
    "QueryAXTreeResult",
]
