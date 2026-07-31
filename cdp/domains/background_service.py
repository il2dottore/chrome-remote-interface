"""Generated bindings for the CDP BackgroundService domain. Do not edit manually."""

from __future__ import annotations

from collections.abc import Awaitable, Mapping
from typing import TYPE_CHECKING, Literal, TypeAlias, cast, overload

from typing_extensions import TypedDict, Unpack

from cdp.domain import Domain as BaseDomain, EventCallback, Unsubscribe
from cdp.types import JsonObject

if TYPE_CHECKING:
    from . import network as Network
    from . import service_worker as ServiceWorker


ServiceName: TypeAlias = Literal[
    "backgroundFetch",
    "backgroundSync",
    "pushMessaging",
    "notifications",
    "paymentHandler",
    "periodicBackgroundSync",
]


class EventMetadata(TypedDict):
    key: str
    value: str


class BackgroundServiceEvent(TypedDict):
    timestamp: Network.TimeSinceEpoch
    origin: str
    serviceWorkerRegistrationId: ServiceWorker.RegistrationID
    service: ServiceName
    eventName: str
    instanceId: str
    eventMetadata: list[EventMetadata]
    storageKey: str


class StartObservingParameters(TypedDict):
    service: ServiceName


class StopObservingParameters(TypedDict):
    service: ServiceName


class SetRecordingParameters(TypedDict):
    shouldRecord: bool
    service: ServiceName


class ClearEventsParameters(TypedDict):
    service: ServiceName


class RecordingStateChangedEvent(TypedDict):
    isRecording: bool
    service: ServiceName


class BackgroundServiceEventReceivedEvent(TypedDict):
    backgroundServiceEvent: BackgroundServiceEvent


class BackgroundService(BaseDomain):
    """Defines events for background web platform features."""

    domain_name = "BackgroundService"

    @overload
    async def startObserving(
        self,
        params: StartObservingParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def startObserving(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[StartObservingParameters],
    ) -> JsonObject: ...

    async def startObserving(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Enables event updates for the service."""

        return await self._command("startObserving", params, session_id, kwargs)

    @overload
    async def stopObserving(
        self,
        params: StopObservingParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def stopObserving(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[StopObservingParameters],
    ) -> JsonObject: ...

    async def stopObserving(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Disables event updates for the service."""

        return await self._command("stopObserving", params, session_id, kwargs)

    @overload
    async def setRecording(
        self,
        params: SetRecordingParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def setRecording(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetRecordingParameters],
    ) -> JsonObject: ...

    async def setRecording(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Set the recording state for the service."""

        return await self._command("setRecording", params, session_id, kwargs)

    @overload
    async def clearEvents(
        self,
        params: ClearEventsParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def clearEvents(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[ClearEventsParameters],
    ) -> JsonObject: ...

    async def clearEvents(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Clears all stored data for the service."""

        return await self._command("clearEvents", params, session_id, kwargs)

    @overload
    def recordingStateChanged(
        self,
        callback_or_session: EventCallback[RecordingStateChangedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def recordingStateChanged(
        self,
        callback_or_session: str,
        handler: EventCallback[RecordingStateChangedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def recordingStateChanged(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[RecordingStateChangedEvent]: ...

    def recordingStateChanged(
        self,
        callback_or_session: EventCallback[RecordingStateChangedEvent]
        | str
        | None = None,
        handler: EventCallback[RecordingStateChangedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[RecordingStateChangedEvent] | Unsubscribe:
        """Called when the recording state for the service has been updated."""

        return cast(
            Awaitable[RecordingStateChangedEvent] | Unsubscribe,
            self._event(
                "recordingStateChanged",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def backgroundServiceEventReceived(
        self,
        callback_or_session: EventCallback[BackgroundServiceEventReceivedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def backgroundServiceEventReceived(
        self,
        callback_or_session: str,
        handler: EventCallback[BackgroundServiceEventReceivedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def backgroundServiceEventReceived(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[BackgroundServiceEventReceivedEvent]: ...

    def backgroundServiceEventReceived(
        self,
        callback_or_session: EventCallback[BackgroundServiceEventReceivedEvent]
        | str
        | None = None,
        handler: EventCallback[BackgroundServiceEventReceivedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[BackgroundServiceEventReceivedEvent] | Unsubscribe:
        """Called with all existing backgroundServiceEvents when enabled, and all new events afterwards if enabled and recording."""

        return cast(
            Awaitable[BackgroundServiceEventReceivedEvent] | Unsubscribe,
            self._event(
                "backgroundServiceEventReceived",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )


__all__ = [
    "BackgroundService",
    "BackgroundServiceEvent",
    "BackgroundServiceEventReceivedEvent",
    "ClearEventsParameters",
    "EventMetadata",
    "RecordingStateChangedEvent",
    "ServiceName",
    "SetRecordingParameters",
    "StartObservingParameters",
    "StopObservingParameters",
]
