"""Generated bindings for the CDP Inspector domain. Do not edit manually."""

from __future__ import annotations

from collections.abc import Awaitable, Mapping
from typing import cast, overload

from typing_extensions import TypedDict

from cdp.domain import Domain as BaseDomain, EventCallback, Unsubscribe
from cdp.types import JsonObject


class DetachedEvent(TypedDict):
    reason: str


class Inspector(BaseDomain):
    """The CDP Inspector domain."""

    domain_name = "Inspector"

    async def disable(
        self,
        session_id: str | None = None,
    ) -> JsonObject:
        """Disables inspector domain notifications."""

        return await self._command("disable", None, session_id, {})

    async def enable(
        self,
        session_id: str | None = None,
    ) -> JsonObject:
        """Enables inspector domain notifications."""

        return await self._command("enable", None, session_id, {})

    @overload
    def detached(
        self,
        callback_or_session: EventCallback[DetachedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def detached(
        self,
        callback_or_session: str,
        handler: EventCallback[DetachedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def detached(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[DetachedEvent]: ...

    def detached(
        self,
        callback_or_session: EventCallback[DetachedEvent] | str | None = None,
        handler: EventCallback[DetachedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[DetachedEvent] | Unsubscribe:
        """Fired when remote debugging connection is about to be terminated. Contains detach reason."""

        return cast(
            Awaitable[DetachedEvent] | Unsubscribe,
            self._event(
                "detached",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def targetCrashed(
        self,
        callback_or_session: EventCallback[JsonObject],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def targetCrashed(
        self,
        callback_or_session: str,
        handler: EventCallback[JsonObject],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def targetCrashed(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[JsonObject]: ...

    def targetCrashed(
        self,
        callback_or_session: EventCallback[JsonObject] | str | None = None,
        handler: EventCallback[JsonObject] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[JsonObject] | Unsubscribe:
        """Fired when debugging target has crashed"""

        return self._event(
            "targetCrashed",
            cast(EventCallback[Mapping[str, object]] | str | None, callback_or_session),
            cast(EventCallback[Mapping[str, object]] | None, handler),
            session_id,
        )

    @overload
    def targetReloadedAfterCrash(
        self,
        callback_or_session: EventCallback[JsonObject],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def targetReloadedAfterCrash(
        self,
        callback_or_session: str,
        handler: EventCallback[JsonObject],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def targetReloadedAfterCrash(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[JsonObject]: ...

    def targetReloadedAfterCrash(
        self,
        callback_or_session: EventCallback[JsonObject] | str | None = None,
        handler: EventCallback[JsonObject] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[JsonObject] | Unsubscribe:
        """Fired when debugging target has reloaded after crash"""

        return self._event(
            "targetReloadedAfterCrash",
            cast(EventCallback[Mapping[str, object]] | str | None, callback_or_session),
            cast(EventCallback[Mapping[str, object]] | None, handler),
            session_id,
        )


__all__ = ["DetachedEvent", "Inspector"]
