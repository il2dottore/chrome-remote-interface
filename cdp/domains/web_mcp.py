"""Generated bindings for the CDP WebMCP domain. Do not edit manually."""

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


class Annotation(TypedDict):
    readOnly: NotRequired[bool]
    untrustedContent: NotRequired[bool]
    autosubmit: NotRequired[bool]


InvocationStatus: TypeAlias = Literal["Completed", "Canceled", "Error"]


class Tool(TypedDict):
    name: str
    description: str
    inputSchema: NotRequired[JsonObject]
    annotations: NotRequired[Annotation]
    frameId: Page.FrameId
    backendNodeId: NotRequired[DOM.BackendNodeId]
    stackTrace: NotRequired[Runtime.StackTrace]


class RemovedTool(TypedDict):
    name: str
    frameId: Page.FrameId


class InvokeToolParameters(TypedDict):
    frameId: Page.FrameId
    toolName: str
    input: JsonObject


class InvokeToolResult(TypedDict):
    invocationId: str


class CancelInvocationParameters(TypedDict):
    invocationId: str


class ToolsAddedEvent(TypedDict):
    tools: list[Tool]


class ToolsRemovedEvent(TypedDict):
    tools: list[RemovedTool]


class ToolInvokedEvent(TypedDict):
    toolName: str
    frameId: Page.FrameId
    invocationId: str
    input: str


class ToolRespondedEvent(TypedDict):
    invocationId: str
    status: InvocationStatus
    output: NotRequired[JsonValue]
    errorText: NotRequired[str]
    exception: NotRequired[Runtime.RemoteObject]


class WebMCP(BaseDomain):
    """The CDP WebMCP domain."""

    domain_name = "WebMCP"

    async def enable(
        self,
        session_id: str | None = None,
    ) -> JsonObject:
        """Enables the WebMCP domain, allowing events to be sent. Enabling the domain will trigger a toolsAdded event for all currently registered tools."""

        return await self._command("enable", None, session_id, {})

    async def disable(
        self,
        session_id: str | None = None,
    ) -> JsonObject:
        """Disables the WebMCP domain."""

        return await self._command("disable", None, session_id, {})

    @overload
    async def invokeTool(
        self,
        params: InvokeToolParameters,
        session_id: str | None = None,
    ) -> InvokeToolResult: ...

    @overload
    async def invokeTool(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[InvokeToolParameters],
    ) -> InvokeToolResult: ...

    async def invokeTool(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> InvokeToolResult:
        """Invokes a registered tool."""

        return cast(
            InvokeToolResult,
            await self._command("invokeTool", params, session_id, kwargs),
        )

    @overload
    async def cancelInvocation(
        self,
        params: CancelInvocationParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def cancelInvocation(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[CancelInvocationParameters],
    ) -> JsonObject: ...

    async def cancelInvocation(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Cancels a pending tool invocation."""

        return await self._command("cancelInvocation", params, session_id, kwargs)

    @overload
    def toolsAdded(
        self,
        callback_or_session: EventCallback[ToolsAddedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def toolsAdded(
        self,
        callback_or_session: str,
        handler: EventCallback[ToolsAddedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def toolsAdded(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[ToolsAddedEvent]: ...

    def toolsAdded(
        self,
        callback_or_session: EventCallback[ToolsAddedEvent] | str | None = None,
        handler: EventCallback[ToolsAddedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[ToolsAddedEvent] | Unsubscribe:
        """Event fired when new tools are added."""

        return cast(
            Awaitable[ToolsAddedEvent] | Unsubscribe,
            self._event(
                "toolsAdded",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def toolsRemoved(
        self,
        callback_or_session: EventCallback[ToolsRemovedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def toolsRemoved(
        self,
        callback_or_session: str,
        handler: EventCallback[ToolsRemovedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def toolsRemoved(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[ToolsRemovedEvent]: ...

    def toolsRemoved(
        self,
        callback_or_session: EventCallback[ToolsRemovedEvent] | str | None = None,
        handler: EventCallback[ToolsRemovedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[ToolsRemovedEvent] | Unsubscribe:
        """Event fired when tools are removed."""

        return cast(
            Awaitable[ToolsRemovedEvent] | Unsubscribe,
            self._event(
                "toolsRemoved",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def toolInvoked(
        self,
        callback_or_session: EventCallback[ToolInvokedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def toolInvoked(
        self,
        callback_or_session: str,
        handler: EventCallback[ToolInvokedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def toolInvoked(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[ToolInvokedEvent]: ...

    def toolInvoked(
        self,
        callback_or_session: EventCallback[ToolInvokedEvent] | str | None = None,
        handler: EventCallback[ToolInvokedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[ToolInvokedEvent] | Unsubscribe:
        """Event fired when a tool invocation starts."""

        return cast(
            Awaitable[ToolInvokedEvent] | Unsubscribe,
            self._event(
                "toolInvoked",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def toolResponded(
        self,
        callback_or_session: EventCallback[ToolRespondedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def toolResponded(
        self,
        callback_or_session: str,
        handler: EventCallback[ToolRespondedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def toolResponded(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[ToolRespondedEvent]: ...

    def toolResponded(
        self,
        callback_or_session: EventCallback[ToolRespondedEvent] | str | None = None,
        handler: EventCallback[ToolRespondedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[ToolRespondedEvent] | Unsubscribe:
        """Event fired when a tool invocation completes or fails."""

        return cast(
            Awaitable[ToolRespondedEvent] | Unsubscribe,
            self._event(
                "toolResponded",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )


__all__ = [
    "Annotation",
    "CancelInvocationParameters",
    "InvocationStatus",
    "InvokeToolParameters",
    "InvokeToolResult",
    "RemovedTool",
    "Tool",
    "ToolInvokedEvent",
    "ToolRespondedEvent",
    "ToolsAddedEvent",
    "ToolsRemovedEvent",
    "WebMCP",
]
