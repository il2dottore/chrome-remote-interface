"""Generated bindings for the CDP DeviceAccess domain. Do not edit manually."""

from __future__ import annotations

from collections.abc import Awaitable, Mapping
from typing import TypeAlias, cast, overload

from typing_extensions import TypedDict, Unpack

from cdp.domain import Domain as BaseDomain, EventCallback, Unsubscribe
from cdp.types import JsonObject


RequestId: TypeAlias = str

DeviceId: TypeAlias = str


class PromptDevice(TypedDict):
    id: DeviceId
    name: str


class SelectPromptParameters(TypedDict):
    id: RequestId
    deviceId: DeviceId


class CancelPromptParameters(TypedDict):
    id: RequestId


class DeviceRequestPromptedEvent(TypedDict):
    id: RequestId
    devices: list[PromptDevice]


class DeviceAccess(BaseDomain):
    """The CDP DeviceAccess domain."""

    domain_name = "DeviceAccess"

    async def enable(
        self,
        session_id: str | None = None,
    ) -> JsonObject:
        """Enable events in this domain."""

        return await self._command("enable", None, session_id, {})

    async def disable(
        self,
        session_id: str | None = None,
    ) -> JsonObject:
        """Disable events in this domain."""

        return await self._command("disable", None, session_id, {})

    @overload
    async def selectPrompt(
        self,
        params: SelectPromptParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def selectPrompt(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SelectPromptParameters],
    ) -> JsonObject: ...

    async def selectPrompt(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Select a device in response to a DeviceAccess.deviceRequestPrompted event."""

        return await self._command("selectPrompt", params, session_id, kwargs)

    @overload
    async def cancelPrompt(
        self,
        params: CancelPromptParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def cancelPrompt(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[CancelPromptParameters],
    ) -> JsonObject: ...

    async def cancelPrompt(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Cancel a prompt in response to a DeviceAccess.deviceRequestPrompted event."""

        return await self._command("cancelPrompt", params, session_id, kwargs)

    @overload
    def deviceRequestPrompted(
        self,
        callback_or_session: EventCallback[DeviceRequestPromptedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def deviceRequestPrompted(
        self,
        callback_or_session: str,
        handler: EventCallback[DeviceRequestPromptedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def deviceRequestPrompted(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[DeviceRequestPromptedEvent]: ...

    def deviceRequestPrompted(
        self,
        callback_or_session: EventCallback[DeviceRequestPromptedEvent]
        | str
        | None = None,
        handler: EventCallback[DeviceRequestPromptedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[DeviceRequestPromptedEvent] | Unsubscribe:
        """A device request opened a user prompt to select a device. Respond with the selectPrompt or cancelPrompt command."""

        return cast(
            Awaitable[DeviceRequestPromptedEvent] | Unsubscribe,
            self._event(
                "deviceRequestPrompted",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )


__all__ = [
    "CancelPromptParameters",
    "DeviceAccess",
    "DeviceId",
    "DeviceRequestPromptedEvent",
    "PromptDevice",
    "RequestId",
    "SelectPromptParameters",
]
