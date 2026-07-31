"""Generated bindings for the CDP ServiceWorker domain. Do not edit manually."""

from __future__ import annotations

from collections.abc import Awaitable, Mapping
from typing import TYPE_CHECKING, Literal, TypeAlias, cast, overload

from typing_extensions import NotRequired, TypedDict, Unpack

from cdp.domain import Domain as BaseDomain, EventCallback, Unsubscribe
from cdp.types import JsonObject

if TYPE_CHECKING:
    from . import target as Target


RegistrationID: TypeAlias = str


class ServiceWorkerRegistration(TypedDict):
    registrationId: RegistrationID
    scopeURL: str
    isDeleted: bool


ServiceWorkerVersionRunningStatus: TypeAlias = Literal[
    "stopped", "starting", "running", "stopping"
]

ServiceWorkerVersionStatus: TypeAlias = Literal[
    "new", "installing", "installed", "activating", "activated", "redundant"
]


class ServiceWorkerVersion(TypedDict):
    versionId: str
    registrationId: RegistrationID
    scriptURL: str
    runningStatus: ServiceWorkerVersionRunningStatus
    status: ServiceWorkerVersionStatus
    scriptLastModified: NotRequired[float]
    scriptResponseTime: NotRequired[float]
    controlledClients: NotRequired[list[Target.TargetID]]
    targetId: NotRequired[Target.TargetID]
    routerRules: NotRequired[str]


class ServiceWorkerErrorMessage(TypedDict):
    errorMessage: str
    registrationId: RegistrationID
    versionId: str
    sourceURL: str
    lineNumber: int
    columnNumber: int


class DeliverPushMessageParameters(TypedDict):
    origin: str
    registrationId: RegistrationID
    data: str


class DispatchSyncEventParameters(TypedDict):
    origin: str
    registrationId: RegistrationID
    tag: str
    lastChance: bool


class DispatchPeriodicSyncEventParameters(TypedDict):
    origin: str
    registrationId: RegistrationID
    tag: str


class SetForceUpdateOnPageLoadParameters(TypedDict):
    forceUpdateOnPageLoad: bool


class SkipWaitingParameters(TypedDict):
    scopeURL: str


class StartWorkerParameters(TypedDict):
    scopeURL: str


class StopWorkerParameters(TypedDict):
    versionId: str


class UnregisterParameters(TypedDict):
    scopeURL: str


class UpdateRegistrationParameters(TypedDict):
    scopeURL: str


class WorkerErrorReportedEvent(TypedDict):
    errorMessage: ServiceWorkerErrorMessage


class WorkerRegistrationUpdatedEvent(TypedDict):
    registrations: list[ServiceWorkerRegistration]


class WorkerVersionUpdatedEvent(TypedDict):
    versions: list[ServiceWorkerVersion]


class ServiceWorker(BaseDomain):
    """The CDP ServiceWorker domain."""

    domain_name = "ServiceWorker"

    @overload
    async def deliverPushMessage(
        self,
        params: DeliverPushMessageParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def deliverPushMessage(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[DeliverPushMessageParameters],
    ) -> JsonObject: ...

    async def deliverPushMessage(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Send ServiceWorker.deliverPushMessage."""

        return await self._command("deliverPushMessage", params, session_id, kwargs)

    async def disable(
        self,
        session_id: str | None = None,
    ) -> JsonObject:
        """Send ServiceWorker.disable."""

        return await self._command("disable", None, session_id, {})

    @overload
    async def dispatchSyncEvent(
        self,
        params: DispatchSyncEventParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def dispatchSyncEvent(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[DispatchSyncEventParameters],
    ) -> JsonObject: ...

    async def dispatchSyncEvent(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Send ServiceWorker.dispatchSyncEvent."""

        return await self._command("dispatchSyncEvent", params, session_id, kwargs)

    @overload
    async def dispatchPeriodicSyncEvent(
        self,
        params: DispatchPeriodicSyncEventParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def dispatchPeriodicSyncEvent(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[DispatchPeriodicSyncEventParameters],
    ) -> JsonObject: ...

    async def dispatchPeriodicSyncEvent(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Send ServiceWorker.dispatchPeriodicSyncEvent."""

        return await self._command(
            "dispatchPeriodicSyncEvent", params, session_id, kwargs
        )

    async def enable(
        self,
        session_id: str | None = None,
    ) -> JsonObject:
        """Send ServiceWorker.enable."""

        return await self._command("enable", None, session_id, {})

    @overload
    async def setForceUpdateOnPageLoad(
        self,
        params: SetForceUpdateOnPageLoadParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def setForceUpdateOnPageLoad(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetForceUpdateOnPageLoadParameters],
    ) -> JsonObject: ...

    async def setForceUpdateOnPageLoad(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Send ServiceWorker.setForceUpdateOnPageLoad."""

        return await self._command(
            "setForceUpdateOnPageLoad", params, session_id, kwargs
        )

    @overload
    async def skipWaiting(
        self,
        params: SkipWaitingParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def skipWaiting(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SkipWaitingParameters],
    ) -> JsonObject: ...

    async def skipWaiting(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Send ServiceWorker.skipWaiting."""

        return await self._command("skipWaiting", params, session_id, kwargs)

    @overload
    async def startWorker(
        self,
        params: StartWorkerParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def startWorker(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[StartWorkerParameters],
    ) -> JsonObject: ...

    async def startWorker(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Send ServiceWorker.startWorker."""

        return await self._command("startWorker", params, session_id, kwargs)

    async def stopAllWorkers(
        self,
        session_id: str | None = None,
    ) -> JsonObject:
        """Send ServiceWorker.stopAllWorkers."""

        return await self._command("stopAllWorkers", None, session_id, {})

    @overload
    async def stopWorker(
        self,
        params: StopWorkerParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def stopWorker(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[StopWorkerParameters],
    ) -> JsonObject: ...

    async def stopWorker(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Send ServiceWorker.stopWorker."""

        return await self._command("stopWorker", params, session_id, kwargs)

    @overload
    async def unregister(
        self,
        params: UnregisterParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def unregister(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[UnregisterParameters],
    ) -> JsonObject: ...

    async def unregister(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Send ServiceWorker.unregister."""

        return await self._command("unregister", params, session_id, kwargs)

    @overload
    async def updateRegistration(
        self,
        params: UpdateRegistrationParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def updateRegistration(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[UpdateRegistrationParameters],
    ) -> JsonObject: ...

    async def updateRegistration(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Send ServiceWorker.updateRegistration."""

        return await self._command("updateRegistration", params, session_id, kwargs)

    @overload
    def workerErrorReported(
        self,
        callback_or_session: EventCallback[WorkerErrorReportedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def workerErrorReported(
        self,
        callback_or_session: str,
        handler: EventCallback[WorkerErrorReportedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def workerErrorReported(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[WorkerErrorReportedEvent]: ...

    def workerErrorReported(
        self,
        callback_or_session: EventCallback[WorkerErrorReportedEvent]
        | str
        | None = None,
        handler: EventCallback[WorkerErrorReportedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[WorkerErrorReportedEvent] | Unsubscribe:
        """Wait for or subscribe to ServiceWorker.workerErrorReported."""

        return cast(
            Awaitable[WorkerErrorReportedEvent] | Unsubscribe,
            self._event(
                "workerErrorReported",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def workerRegistrationUpdated(
        self,
        callback_or_session: EventCallback[WorkerRegistrationUpdatedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def workerRegistrationUpdated(
        self,
        callback_or_session: str,
        handler: EventCallback[WorkerRegistrationUpdatedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def workerRegistrationUpdated(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[WorkerRegistrationUpdatedEvent]: ...

    def workerRegistrationUpdated(
        self,
        callback_or_session: EventCallback[WorkerRegistrationUpdatedEvent]
        | str
        | None = None,
        handler: EventCallback[WorkerRegistrationUpdatedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[WorkerRegistrationUpdatedEvent] | Unsubscribe:
        """Wait for or subscribe to ServiceWorker.workerRegistrationUpdated."""

        return cast(
            Awaitable[WorkerRegistrationUpdatedEvent] | Unsubscribe,
            self._event(
                "workerRegistrationUpdated",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def workerVersionUpdated(
        self,
        callback_or_session: EventCallback[WorkerVersionUpdatedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def workerVersionUpdated(
        self,
        callback_or_session: str,
        handler: EventCallback[WorkerVersionUpdatedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def workerVersionUpdated(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[WorkerVersionUpdatedEvent]: ...

    def workerVersionUpdated(
        self,
        callback_or_session: EventCallback[WorkerVersionUpdatedEvent]
        | str
        | None = None,
        handler: EventCallback[WorkerVersionUpdatedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[WorkerVersionUpdatedEvent] | Unsubscribe:
        """Wait for or subscribe to ServiceWorker.workerVersionUpdated."""

        return cast(
            Awaitable[WorkerVersionUpdatedEvent] | Unsubscribe,
            self._event(
                "workerVersionUpdated",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )


__all__ = [
    "DeliverPushMessageParameters",
    "DispatchPeriodicSyncEventParameters",
    "DispatchSyncEventParameters",
    "RegistrationID",
    "ServiceWorker",
    "ServiceWorkerErrorMessage",
    "ServiceWorkerRegistration",
    "ServiceWorkerVersion",
    "ServiceWorkerVersionRunningStatus",
    "ServiceWorkerVersionStatus",
    "SetForceUpdateOnPageLoadParameters",
    "SkipWaitingParameters",
    "StartWorkerParameters",
    "StopWorkerParameters",
    "UnregisterParameters",
    "UpdateRegistrationParameters",
    "WorkerErrorReportedEvent",
    "WorkerRegistrationUpdatedEvent",
    "WorkerVersionUpdatedEvent",
]
