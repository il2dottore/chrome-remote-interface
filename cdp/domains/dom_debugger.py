"""Generated bindings for the CDP DOMDebugger domain. Do not edit manually."""

from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Literal, TypeAlias, cast, overload

from typing_extensions import NotRequired, TypedDict, Unpack

from cdp.domain import Domain as BaseDomain
from cdp.types import JsonObject

if TYPE_CHECKING:
    from . import dom as DOM
    from . import runtime as Runtime


DOMBreakpointType: TypeAlias = Literal[
    "subtree-modified", "attribute-modified", "node-removed"
]

CSPViolationType: TypeAlias = Literal[
    "trustedtype-sink-violation", "trustedtype-policy-violation"
]


class EventListener(TypedDict):
    type: str
    useCapture: bool
    passive: bool
    once: bool
    scriptId: Runtime.ScriptId
    lineNumber: int
    columnNumber: int
    handler: NotRequired[Runtime.RemoteObject]
    originalHandler: NotRequired[Runtime.RemoteObject]
    backendNodeId: NotRequired[DOM.BackendNodeId]


class GetEventListenersParameters(TypedDict):
    objectId: Runtime.RemoteObjectId
    depth: NotRequired[int]
    pierce: NotRequired[bool]


class GetEventListenersResult(TypedDict):
    listeners: list[EventListener]


class RemoveDOMBreakpointParameters(TypedDict):
    nodeId: DOM.NodeId
    type: DOMBreakpointType


class RemoveEventListenerBreakpointParameters(TypedDict):
    eventName: str
    targetName: NotRequired[str]


class RemoveInstrumentationBreakpointParameters(TypedDict):
    eventName: str


class RemoveXHRBreakpointParameters(TypedDict):
    url: str


class SetBreakOnCSPViolationParameters(TypedDict):
    violationTypes: list[CSPViolationType]


class SetDOMBreakpointParameters(TypedDict):
    nodeId: DOM.NodeId
    type: DOMBreakpointType


class SetEventListenerBreakpointParameters(TypedDict):
    eventName: str
    targetName: NotRequired[str]


class SetInstrumentationBreakpointParameters(TypedDict):
    eventName: str


class SetXHRBreakpointParameters(TypedDict):
    url: str


class DOMDebugger(BaseDomain):
    """DOM debugging allows setting breakpoints on particular DOM operations and events. JavaScript execution will stop on these operations as if there was a regular breakpoint set."""

    domain_name = "DOMDebugger"

    @overload
    async def getEventListeners(
        self,
        params: GetEventListenersParameters,
        session_id: str | None = None,
    ) -> GetEventListenersResult: ...

    @overload
    async def getEventListeners(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[GetEventListenersParameters],
    ) -> GetEventListenersResult: ...

    async def getEventListeners(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> GetEventListenersResult:
        """Returns event listeners of the given object."""

        return cast(
            GetEventListenersResult,
            await self._command("getEventListeners", params, session_id, kwargs),
        )

    @overload
    async def removeDOMBreakpoint(
        self,
        params: RemoveDOMBreakpointParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def removeDOMBreakpoint(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[RemoveDOMBreakpointParameters],
    ) -> JsonObject: ...

    async def removeDOMBreakpoint(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Removes DOM breakpoint that was set using `setDOMBreakpoint`."""

        return await self._command("removeDOMBreakpoint", params, session_id, kwargs)

    @overload
    async def removeEventListenerBreakpoint(
        self,
        params: RemoveEventListenerBreakpointParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def removeEventListenerBreakpoint(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[RemoveEventListenerBreakpointParameters],
    ) -> JsonObject: ...

    async def removeEventListenerBreakpoint(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Removes breakpoint on particular DOM event."""

        return await self._command(
            "removeEventListenerBreakpoint", params, session_id, kwargs
        )

    @overload
    async def removeInstrumentationBreakpoint(
        self,
        params: RemoveInstrumentationBreakpointParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def removeInstrumentationBreakpoint(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[RemoveInstrumentationBreakpointParameters],
    ) -> JsonObject: ...

    async def removeInstrumentationBreakpoint(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Removes breakpoint on particular native event."""

        return await self._command(
            "removeInstrumentationBreakpoint", params, session_id, kwargs
        )

    @overload
    async def removeXHRBreakpoint(
        self,
        params: RemoveXHRBreakpointParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def removeXHRBreakpoint(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[RemoveXHRBreakpointParameters],
    ) -> JsonObject: ...

    async def removeXHRBreakpoint(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Removes breakpoint from XMLHttpRequest."""

        return await self._command("removeXHRBreakpoint", params, session_id, kwargs)

    @overload
    async def setBreakOnCSPViolation(
        self,
        params: SetBreakOnCSPViolationParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def setBreakOnCSPViolation(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetBreakOnCSPViolationParameters],
    ) -> JsonObject: ...

    async def setBreakOnCSPViolation(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Sets breakpoint on particular CSP violations."""

        return await self._command("setBreakOnCSPViolation", params, session_id, kwargs)

    @overload
    async def setDOMBreakpoint(
        self,
        params: SetDOMBreakpointParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def setDOMBreakpoint(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetDOMBreakpointParameters],
    ) -> JsonObject: ...

    async def setDOMBreakpoint(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Sets breakpoint on particular operation with DOM."""

        return await self._command("setDOMBreakpoint", params, session_id, kwargs)

    @overload
    async def setEventListenerBreakpoint(
        self,
        params: SetEventListenerBreakpointParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def setEventListenerBreakpoint(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetEventListenerBreakpointParameters],
    ) -> JsonObject: ...

    async def setEventListenerBreakpoint(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Sets breakpoint on particular DOM event."""

        return await self._command(
            "setEventListenerBreakpoint", params, session_id, kwargs
        )

    @overload
    async def setInstrumentationBreakpoint(
        self,
        params: SetInstrumentationBreakpointParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def setInstrumentationBreakpoint(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetInstrumentationBreakpointParameters],
    ) -> JsonObject: ...

    async def setInstrumentationBreakpoint(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Sets breakpoint on particular native event."""

        return await self._command(
            "setInstrumentationBreakpoint", params, session_id, kwargs
        )

    @overload
    async def setXHRBreakpoint(
        self,
        params: SetXHRBreakpointParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def setXHRBreakpoint(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetXHRBreakpointParameters],
    ) -> JsonObject: ...

    async def setXHRBreakpoint(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Sets breakpoint on XMLHttpRequest."""

        return await self._command("setXHRBreakpoint", params, session_id, kwargs)


__all__ = [
    "CSPViolationType",
    "DOMBreakpointType",
    "DOMDebugger",
    "EventListener",
    "GetEventListenersParameters",
    "GetEventListenersResult",
    "RemoveDOMBreakpointParameters",
    "RemoveEventListenerBreakpointParameters",
    "RemoveInstrumentationBreakpointParameters",
    "RemoveXHRBreakpointParameters",
    "SetBreakOnCSPViolationParameters",
    "SetDOMBreakpointParameters",
    "SetEventListenerBreakpointParameters",
    "SetInstrumentationBreakpointParameters",
    "SetXHRBreakpointParameters",
]
