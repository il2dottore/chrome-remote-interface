"""Generated bindings for the CDP Tethering domain. Do not edit manually."""

from __future__ import annotations

from collections.abc import Awaitable, Mapping
from typing import cast, overload

from typing_extensions import TypedDict, Unpack

from cdp.domain import Domain as BaseDomain, EventCallback, Unsubscribe
from cdp.types import JsonObject


class BindParameters(TypedDict):
    port: int


class UnbindParameters(TypedDict):
    port: int


class AcceptedEvent(TypedDict):
    port: int
    connectionId: str


class Tethering(BaseDomain):
    """The Tethering domain defines methods and events for browser port binding."""

    domain_name = "Tethering"

    @overload
    async def bind(
        self,
        params: BindParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def bind(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[BindParameters],
    ) -> JsonObject: ...

    async def bind(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Request browser port binding."""

        return await self._command("bind", params, session_id, kwargs)

    @overload
    async def unbind(
        self,
        params: UnbindParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def unbind(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[UnbindParameters],
    ) -> JsonObject: ...

    async def unbind(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Request browser port unbinding."""

        return await self._command("unbind", params, session_id, kwargs)

    @overload
    def accepted(
        self,
        callback_or_session: EventCallback[AcceptedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def accepted(
        self,
        callback_or_session: str,
        handler: EventCallback[AcceptedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def accepted(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[AcceptedEvent]: ...

    def accepted(
        self,
        callback_or_session: EventCallback[AcceptedEvent] | str | None = None,
        handler: EventCallback[AcceptedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[AcceptedEvent] | Unsubscribe:
        """Informs that port was successfully bound and got a specified connection id."""

        return cast(
            Awaitable[AcceptedEvent] | Unsubscribe,
            self._event(
                "accepted",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )


__all__ = ["AcceptedEvent", "BindParameters", "Tethering", "UnbindParameters"]
