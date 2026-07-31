"""Generated bindings for the CDP DOMStorage domain. Do not edit manually."""

from __future__ import annotations

from collections.abc import Awaitable, Mapping
from typing import TypeAlias, cast, overload

from typing_extensions import NotRequired, TypedDict, Unpack

from cdp.domain import Domain as BaseDomain, EventCallback, Unsubscribe
from cdp.types import JsonObject


SerializedStorageKey: TypeAlias = str


class StorageId(TypedDict):
    securityOrigin: NotRequired[str]
    storageKey: NotRequired[SerializedStorageKey]
    isLocalStorage: bool


Item: TypeAlias = list[str]


class ClearParameters(TypedDict):
    storageId: StorageId


class GetDOMStorageItemsParameters(TypedDict):
    storageId: StorageId


class GetDOMStorageItemsResult(TypedDict):
    entries: list[Item]


class RemoveDOMStorageItemParameters(TypedDict):
    storageId: StorageId
    key: str


class SetDOMStorageItemParameters(TypedDict):
    storageId: StorageId
    key: str
    value: str


class DomStorageItemAddedEvent(TypedDict):
    storageId: StorageId
    key: str
    newValue: str


class DomStorageItemRemovedEvent(TypedDict):
    storageId: StorageId
    key: str


class DomStorageItemUpdatedEvent(TypedDict):
    storageId: StorageId
    key: str
    oldValue: str
    newValue: str


class DomStorageItemsClearedEvent(TypedDict):
    storageId: StorageId


class DOMStorage(BaseDomain):
    """Query and modify DOM storage."""

    domain_name = "DOMStorage"

    @overload
    async def clear(
        self,
        params: ClearParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def clear(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[ClearParameters],
    ) -> JsonObject: ...

    async def clear(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Send DOMStorage.clear."""

        return await self._command("clear", params, session_id, kwargs)

    async def disable(
        self,
        session_id: str | None = None,
    ) -> JsonObject:
        """Disables storage tracking, prevents storage events from being sent to the client."""

        return await self._command("disable", None, session_id, {})

    async def enable(
        self,
        session_id: str | None = None,
    ) -> JsonObject:
        """Enables storage tracking, storage events will now be delivered to the client."""

        return await self._command("enable", None, session_id, {})

    @overload
    async def getDOMStorageItems(
        self,
        params: GetDOMStorageItemsParameters,
        session_id: str | None = None,
    ) -> GetDOMStorageItemsResult: ...

    @overload
    async def getDOMStorageItems(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[GetDOMStorageItemsParameters],
    ) -> GetDOMStorageItemsResult: ...

    async def getDOMStorageItems(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> GetDOMStorageItemsResult:
        """Send DOMStorage.getDOMStorageItems."""

        return cast(
            GetDOMStorageItemsResult,
            await self._command("getDOMStorageItems", params, session_id, kwargs),
        )

    @overload
    async def removeDOMStorageItem(
        self,
        params: RemoveDOMStorageItemParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def removeDOMStorageItem(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[RemoveDOMStorageItemParameters],
    ) -> JsonObject: ...

    async def removeDOMStorageItem(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Send DOMStorage.removeDOMStorageItem."""

        return await self._command("removeDOMStorageItem", params, session_id, kwargs)

    @overload
    async def setDOMStorageItem(
        self,
        params: SetDOMStorageItemParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def setDOMStorageItem(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetDOMStorageItemParameters],
    ) -> JsonObject: ...

    async def setDOMStorageItem(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Send DOMStorage.setDOMStorageItem."""

        return await self._command("setDOMStorageItem", params, session_id, kwargs)

    @overload
    def domStorageItemAdded(
        self,
        callback_or_session: EventCallback[DomStorageItemAddedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def domStorageItemAdded(
        self,
        callback_or_session: str,
        handler: EventCallback[DomStorageItemAddedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def domStorageItemAdded(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[DomStorageItemAddedEvent]: ...

    def domStorageItemAdded(
        self,
        callback_or_session: EventCallback[DomStorageItemAddedEvent]
        | str
        | None = None,
        handler: EventCallback[DomStorageItemAddedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[DomStorageItemAddedEvent] | Unsubscribe:
        """Wait for or subscribe to DOMStorage.domStorageItemAdded."""

        return cast(
            Awaitable[DomStorageItemAddedEvent] | Unsubscribe,
            self._event(
                "domStorageItemAdded",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def domStorageItemRemoved(
        self,
        callback_or_session: EventCallback[DomStorageItemRemovedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def domStorageItemRemoved(
        self,
        callback_or_session: str,
        handler: EventCallback[DomStorageItemRemovedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def domStorageItemRemoved(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[DomStorageItemRemovedEvent]: ...

    def domStorageItemRemoved(
        self,
        callback_or_session: EventCallback[DomStorageItemRemovedEvent]
        | str
        | None = None,
        handler: EventCallback[DomStorageItemRemovedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[DomStorageItemRemovedEvent] | Unsubscribe:
        """Wait for or subscribe to DOMStorage.domStorageItemRemoved."""

        return cast(
            Awaitable[DomStorageItemRemovedEvent] | Unsubscribe,
            self._event(
                "domStorageItemRemoved",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def domStorageItemUpdated(
        self,
        callback_or_session: EventCallback[DomStorageItemUpdatedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def domStorageItemUpdated(
        self,
        callback_or_session: str,
        handler: EventCallback[DomStorageItemUpdatedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def domStorageItemUpdated(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[DomStorageItemUpdatedEvent]: ...

    def domStorageItemUpdated(
        self,
        callback_or_session: EventCallback[DomStorageItemUpdatedEvent]
        | str
        | None = None,
        handler: EventCallback[DomStorageItemUpdatedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[DomStorageItemUpdatedEvent] | Unsubscribe:
        """Wait for or subscribe to DOMStorage.domStorageItemUpdated."""

        return cast(
            Awaitable[DomStorageItemUpdatedEvent] | Unsubscribe,
            self._event(
                "domStorageItemUpdated",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def domStorageItemsCleared(
        self,
        callback_or_session: EventCallback[DomStorageItemsClearedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def domStorageItemsCleared(
        self,
        callback_or_session: str,
        handler: EventCallback[DomStorageItemsClearedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def domStorageItemsCleared(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[DomStorageItemsClearedEvent]: ...

    def domStorageItemsCleared(
        self,
        callback_or_session: EventCallback[DomStorageItemsClearedEvent]
        | str
        | None = None,
        handler: EventCallback[DomStorageItemsClearedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[DomStorageItemsClearedEvent] | Unsubscribe:
        """Wait for or subscribe to DOMStorage.domStorageItemsCleared."""

        return cast(
            Awaitable[DomStorageItemsClearedEvent] | Unsubscribe,
            self._event(
                "domStorageItemsCleared",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )


__all__ = [
    "ClearParameters",
    "DOMStorage",
    "DomStorageItemAddedEvent",
    "DomStorageItemRemovedEvent",
    "DomStorageItemUpdatedEvent",
    "DomStorageItemsClearedEvent",
    "GetDOMStorageItemsParameters",
    "GetDOMStorageItemsResult",
    "Item",
    "RemoveDOMStorageItemParameters",
    "SerializedStorageKey",
    "SetDOMStorageItemParameters",
    "StorageId",
]
