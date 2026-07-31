"""Generated bindings for the CDP EventBreakpoints domain. Do not edit manually."""

from __future__ import annotations

from collections.abc import Mapping
from typing import overload

from typing_extensions import TypedDict, Unpack

from cdp.domain import Domain as BaseDomain
from cdp.types import JsonObject


class SetInstrumentationBreakpointParameters(TypedDict):
    eventName: str


class RemoveInstrumentationBreakpointParameters(TypedDict):
    eventName: str


class EventBreakpoints(BaseDomain):
    """EventBreakpoints permits setting JavaScript breakpoints on operations and events occurring in native code invoked from JavaScript. Once breakpoint is hit, it is reported through Debugger domain, similarly to regular breakpoints being hit."""

    domain_name = "EventBreakpoints"

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

    async def disable(
        self,
        session_id: str | None = None,
    ) -> JsonObject:
        """Removes all breakpoints"""

        return await self._command("disable", None, session_id, {})


__all__ = [
    "EventBreakpoints",
    "RemoveInstrumentationBreakpointParameters",
    "SetInstrumentationBreakpointParameters",
]
