"""Generated bindings for the CDP Target domain. Do not edit manually."""

from __future__ import annotations

from collections.abc import Awaitable, Mapping
from typing import TYPE_CHECKING, TypeAlias, cast, overload

from typing_extensions import NotRequired, TypedDict, Unpack

from cdp.domain import Domain as BaseDomain, EventCallback, Unsubscribe
from cdp.types import JsonObject

if TYPE_CHECKING:
    from . import browser as Browser
    from . import page as Page


TargetID: TypeAlias = str

SessionID: TypeAlias = str


class TargetInfo(TypedDict):
    targetId: TargetID
    type: str
    title: str
    url: str
    attached: bool
    openerId: NotRequired[TargetID]
    canAccessOpener: bool
    openerFrameId: NotRequired[Page.FrameId]
    browserContextId: NotRequired[Browser.BrowserContextID]
    subtype: NotRequired[str]


class FilterEntry(TypedDict):
    exclude: NotRequired[bool]
    type: NotRequired[str]


TargetFilter: TypeAlias = list[FilterEntry]


class RemoteLocation(TypedDict):
    host: str
    port: int


class ActivateTargetParameters(TypedDict):
    targetId: TargetID


class AttachToTargetParameters(TypedDict):
    targetId: TargetID
    flatten: NotRequired[bool]


class AttachToTargetResult(TypedDict):
    sessionId: SessionID


class AttachToBrowserTargetResult(TypedDict):
    sessionId: SessionID


class CloseTargetParameters(TypedDict):
    targetId: TargetID


class CloseTargetResult(TypedDict):
    success: bool


class ExposeDevToolsProtocolParameters(TypedDict):
    targetId: TargetID
    bindingName: NotRequired[str]


class CreateBrowserContextParameters(TypedDict):
    disposeOnDetach: NotRequired[bool]
    proxyServer: NotRequired[str]
    proxyBypassList: NotRequired[str]
    originsWithUniversalNetworkAccess: NotRequired[list[str]]


class CreateBrowserContextResult(TypedDict):
    browserContextId: Browser.BrowserContextID


class GetBrowserContextsResult(TypedDict):
    browserContextIds: list[Browser.BrowserContextID]


class CreateTargetParameters(TypedDict):
    url: str
    width: NotRequired[int]
    height: NotRequired[int]
    browserContextId: NotRequired[Browser.BrowserContextID]
    enableBeginFrameControl: NotRequired[bool]
    newWindow: NotRequired[bool]
    background: NotRequired[bool]
    forTab: NotRequired[bool]


class CreateTargetResult(TypedDict):
    targetId: TargetID


class DetachFromTargetParameters(TypedDict):
    sessionId: NotRequired[SessionID]
    targetId: NotRequired[TargetID]


class DisposeBrowserContextParameters(TypedDict):
    browserContextId: Browser.BrowserContextID


class GetTargetInfoParameters(TypedDict):
    targetId: NotRequired[TargetID]


class GetTargetInfoResult(TypedDict):
    targetInfo: TargetInfo


class GetTargetsParameters(TypedDict):
    filter: NotRequired[TargetFilter]


class GetTargetsResult(TypedDict):
    targetInfos: list[TargetInfo]


class SendMessageToTargetParameters(TypedDict):
    message: str
    sessionId: NotRequired[SessionID]
    targetId: NotRequired[TargetID]


class SetAutoAttachParameters(TypedDict):
    autoAttach: bool
    waitForDebuggerOnStart: bool
    flatten: NotRequired[bool]
    filter: NotRequired[TargetFilter]


class AutoAttachRelatedParameters(TypedDict):
    targetId: TargetID
    waitForDebuggerOnStart: bool
    filter: NotRequired[TargetFilter]


class SetDiscoverTargetsParameters(TypedDict):
    discover: bool
    filter: NotRequired[TargetFilter]


class SetRemoteLocationsParameters(TypedDict):
    locations: list[RemoteLocation]


class AttachedToTargetEvent(TypedDict):
    sessionId: SessionID
    targetInfo: TargetInfo
    waitingForDebugger: bool


class DetachedFromTargetEvent(TypedDict):
    sessionId: SessionID
    targetId: NotRequired[TargetID]


class ReceivedMessageFromTargetEvent(TypedDict):
    sessionId: SessionID
    message: str
    targetId: NotRequired[TargetID]


class TargetCreatedEvent(TypedDict):
    targetInfo: TargetInfo


class TargetDestroyedEvent(TypedDict):
    targetId: TargetID


class TargetCrashedEvent(TypedDict):
    targetId: TargetID
    status: str
    errorCode: int


class TargetInfoChangedEvent(TypedDict):
    targetInfo: TargetInfo


class Target(BaseDomain):
    """Supports additional targets discovery and allows to attach to them."""

    domain_name = "Target"

    @overload
    async def activateTarget(
        self,
        params: ActivateTargetParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def activateTarget(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[ActivateTargetParameters],
    ) -> JsonObject: ...

    async def activateTarget(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Activates (focuses) the target."""

        return await self._command("activateTarget", params, session_id, kwargs)

    @overload
    async def attachToTarget(
        self,
        params: AttachToTargetParameters,
        session_id: str | None = None,
    ) -> AttachToTargetResult: ...

    @overload
    async def attachToTarget(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[AttachToTargetParameters],
    ) -> AttachToTargetResult: ...

    async def attachToTarget(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> AttachToTargetResult:
        """Attaches to the target with given id."""

        return cast(
            AttachToTargetResult,
            await self._command("attachToTarget", params, session_id, kwargs),
        )

    async def attachToBrowserTarget(
        self,
        session_id: str | None = None,
    ) -> AttachToBrowserTargetResult:
        """Attaches to the browser target, only uses flat sessionId mode."""

        return cast(
            AttachToBrowserTargetResult,
            await self._command("attachToBrowserTarget", None, session_id, {}),
        )

    @overload
    async def closeTarget(
        self,
        params: CloseTargetParameters,
        session_id: str | None = None,
    ) -> CloseTargetResult: ...

    @overload
    async def closeTarget(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[CloseTargetParameters],
    ) -> CloseTargetResult: ...

    async def closeTarget(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> CloseTargetResult:
        """Closes the target. If the target is a page that gets closed too."""

        return cast(
            CloseTargetResult,
            await self._command("closeTarget", params, session_id, kwargs),
        )

    @overload
    async def exposeDevToolsProtocol(
        self,
        params: ExposeDevToolsProtocolParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def exposeDevToolsProtocol(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[ExposeDevToolsProtocolParameters],
    ) -> JsonObject: ...

    async def exposeDevToolsProtocol(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Inject object to the target's main frame that provides a communication channel with browser target. Injected object will be available as `window[bindingName]`. The object has the follwing API: - `binding.send(json)` - a method to send messages over the remote debugging protocol - `binding.onmessage = json => handleMessage(json)` - a callback that will be called for the protocol notifications and command responses."""

        return await self._command("exposeDevToolsProtocol", params, session_id, kwargs)

    @overload
    async def createBrowserContext(
        self,
        params: CreateBrowserContextParameters,
        session_id: str | None = None,
    ) -> CreateBrowserContextResult: ...

    @overload
    async def createBrowserContext(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[CreateBrowserContextParameters],
    ) -> CreateBrowserContextResult: ...

    async def createBrowserContext(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> CreateBrowserContextResult:
        """Creates a new empty BrowserContext. Similar to an incognito profile but you can have more than one."""

        return cast(
            CreateBrowserContextResult,
            await self._command("createBrowserContext", params, session_id, kwargs),
        )

    async def getBrowserContexts(
        self,
        session_id: str | None = None,
    ) -> GetBrowserContextsResult:
        """Returns all browser contexts created with `Target.createBrowserContext` method."""

        return cast(
            GetBrowserContextsResult,
            await self._command("getBrowserContexts", None, session_id, {}),
        )

    @overload
    async def createTarget(
        self,
        params: CreateTargetParameters,
        session_id: str | None = None,
    ) -> CreateTargetResult: ...

    @overload
    async def createTarget(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[CreateTargetParameters],
    ) -> CreateTargetResult: ...

    async def createTarget(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> CreateTargetResult:
        """Creates a new page."""

        return cast(
            CreateTargetResult,
            await self._command("createTarget", params, session_id, kwargs),
        )

    @overload
    async def detachFromTarget(
        self,
        params: DetachFromTargetParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def detachFromTarget(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[DetachFromTargetParameters],
    ) -> JsonObject: ...

    async def detachFromTarget(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Detaches session with given id."""

        return await self._command("detachFromTarget", params, session_id, kwargs)

    @overload
    async def disposeBrowserContext(
        self,
        params: DisposeBrowserContextParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def disposeBrowserContext(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[DisposeBrowserContextParameters],
    ) -> JsonObject: ...

    async def disposeBrowserContext(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Deletes a BrowserContext. All the belonging pages will be closed without calling their beforeunload hooks."""

        return await self._command("disposeBrowserContext", params, session_id, kwargs)

    @overload
    async def getTargetInfo(
        self,
        params: GetTargetInfoParameters,
        session_id: str | None = None,
    ) -> GetTargetInfoResult: ...

    @overload
    async def getTargetInfo(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[GetTargetInfoParameters],
    ) -> GetTargetInfoResult: ...

    async def getTargetInfo(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> GetTargetInfoResult:
        """Returns information about a target."""

        return cast(
            GetTargetInfoResult,
            await self._command("getTargetInfo", params, session_id, kwargs),
        )

    @overload
    async def getTargets(
        self,
        params: GetTargetsParameters,
        session_id: str | None = None,
    ) -> GetTargetsResult: ...

    @overload
    async def getTargets(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[GetTargetsParameters],
    ) -> GetTargetsResult: ...

    async def getTargets(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> GetTargetsResult:
        """Retrieves a list of available targets."""

        return cast(
            GetTargetsResult,
            await self._command("getTargets", params, session_id, kwargs),
        )

    @overload
    async def sendMessageToTarget(
        self,
        params: SendMessageToTargetParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def sendMessageToTarget(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SendMessageToTargetParameters],
    ) -> JsonObject: ...

    async def sendMessageToTarget(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Sends protocol message over session with given id. Consider using flat mode instead; see commands attachToTarget, setAutoAttach, and crbug.com/991325."""

        return await self._command("sendMessageToTarget", params, session_id, kwargs)

    @overload
    async def setAutoAttach(
        self,
        params: SetAutoAttachParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def setAutoAttach(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetAutoAttachParameters],
    ) -> JsonObject: ...

    async def setAutoAttach(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Controls whether to automatically attach to new targets which are considered to be related to this one. When turned on, attaches to all existing related targets as well. When turned off, automatically detaches from all currently attached targets. This also clears all targets added by `autoAttachRelated` from the list of targets to watch for creation of related targets."""

        return await self._command("setAutoAttach", params, session_id, kwargs)

    @overload
    async def autoAttachRelated(
        self,
        params: AutoAttachRelatedParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def autoAttachRelated(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[AutoAttachRelatedParameters],
    ) -> JsonObject: ...

    async def autoAttachRelated(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Adds the specified target to the list of targets that will be monitored for any related target creation (such as child frames, child workers and new versions of service worker) and reported through `attachedToTarget`. The specified target is also auto-attached. This cancels the effect of any previous `setAutoAttach` and is also cancelled by subsequent `setAutoAttach`. Only available at the Browser target."""

        return await self._command("autoAttachRelated", params, session_id, kwargs)

    @overload
    async def setDiscoverTargets(
        self,
        params: SetDiscoverTargetsParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def setDiscoverTargets(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetDiscoverTargetsParameters],
    ) -> JsonObject: ...

    async def setDiscoverTargets(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Controls whether to discover available targets and notify via `targetCreated/targetInfoChanged/targetDestroyed` events."""

        return await self._command("setDiscoverTargets", params, session_id, kwargs)

    @overload
    async def setRemoteLocations(
        self,
        params: SetRemoteLocationsParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def setRemoteLocations(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetRemoteLocationsParameters],
    ) -> JsonObject: ...

    async def setRemoteLocations(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Enables target discovery for the specified locations, when `setDiscoverTargets` was set to `true`."""

        return await self._command("setRemoteLocations", params, session_id, kwargs)

    @overload
    def attachedToTarget(
        self,
        callback_or_session: EventCallback[AttachedToTargetEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def attachedToTarget(
        self,
        callback_or_session: str,
        handler: EventCallback[AttachedToTargetEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def attachedToTarget(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[AttachedToTargetEvent]: ...

    def attachedToTarget(
        self,
        callback_or_session: EventCallback[AttachedToTargetEvent] | str | None = None,
        handler: EventCallback[AttachedToTargetEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[AttachedToTargetEvent] | Unsubscribe:
        """Issued when attached to target because of auto-attach or `attachToTarget` command."""

        return cast(
            Awaitable[AttachedToTargetEvent] | Unsubscribe,
            self._event(
                "attachedToTarget",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def detachedFromTarget(
        self,
        callback_or_session: EventCallback[DetachedFromTargetEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def detachedFromTarget(
        self,
        callback_or_session: str,
        handler: EventCallback[DetachedFromTargetEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def detachedFromTarget(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[DetachedFromTargetEvent]: ...

    def detachedFromTarget(
        self,
        callback_or_session: EventCallback[DetachedFromTargetEvent] | str | None = None,
        handler: EventCallback[DetachedFromTargetEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[DetachedFromTargetEvent] | Unsubscribe:
        """Issued when detached from target for any reason (including `detachFromTarget` command). Can be issued multiple times per target if multiple sessions have been attached to it."""

        return cast(
            Awaitable[DetachedFromTargetEvent] | Unsubscribe,
            self._event(
                "detachedFromTarget",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def receivedMessageFromTarget(
        self,
        callback_or_session: EventCallback[ReceivedMessageFromTargetEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def receivedMessageFromTarget(
        self,
        callback_or_session: str,
        handler: EventCallback[ReceivedMessageFromTargetEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def receivedMessageFromTarget(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[ReceivedMessageFromTargetEvent]: ...

    def receivedMessageFromTarget(
        self,
        callback_or_session: EventCallback[ReceivedMessageFromTargetEvent]
        | str
        | None = None,
        handler: EventCallback[ReceivedMessageFromTargetEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[ReceivedMessageFromTargetEvent] | Unsubscribe:
        """Notifies about a new protocol message received from the session (as reported in `attachedToTarget` event)."""

        return cast(
            Awaitable[ReceivedMessageFromTargetEvent] | Unsubscribe,
            self._event(
                "receivedMessageFromTarget",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def targetCreated(
        self,
        callback_or_session: EventCallback[TargetCreatedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def targetCreated(
        self,
        callback_or_session: str,
        handler: EventCallback[TargetCreatedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def targetCreated(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[TargetCreatedEvent]: ...

    def targetCreated(
        self,
        callback_or_session: EventCallback[TargetCreatedEvent] | str | None = None,
        handler: EventCallback[TargetCreatedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[TargetCreatedEvent] | Unsubscribe:
        """Issued when a possible inspection target is created."""

        return cast(
            Awaitable[TargetCreatedEvent] | Unsubscribe,
            self._event(
                "targetCreated",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def targetDestroyed(
        self,
        callback_or_session: EventCallback[TargetDestroyedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def targetDestroyed(
        self,
        callback_or_session: str,
        handler: EventCallback[TargetDestroyedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def targetDestroyed(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[TargetDestroyedEvent]: ...

    def targetDestroyed(
        self,
        callback_or_session: EventCallback[TargetDestroyedEvent] | str | None = None,
        handler: EventCallback[TargetDestroyedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[TargetDestroyedEvent] | Unsubscribe:
        """Issued when a target is destroyed."""

        return cast(
            Awaitable[TargetDestroyedEvent] | Unsubscribe,
            self._event(
                "targetDestroyed",
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
        callback_or_session: EventCallback[TargetCrashedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def targetCrashed(
        self,
        callback_or_session: str,
        handler: EventCallback[TargetCrashedEvent],
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
    ) -> Awaitable[TargetCrashedEvent]: ...

    def targetCrashed(
        self,
        callback_or_session: EventCallback[TargetCrashedEvent] | str | None = None,
        handler: EventCallback[TargetCrashedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[TargetCrashedEvent] | Unsubscribe:
        """Issued when a target has crashed."""

        return cast(
            Awaitable[TargetCrashedEvent] | Unsubscribe,
            self._event(
                "targetCrashed",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def targetInfoChanged(
        self,
        callback_or_session: EventCallback[TargetInfoChangedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def targetInfoChanged(
        self,
        callback_or_session: str,
        handler: EventCallback[TargetInfoChangedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def targetInfoChanged(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[TargetInfoChangedEvent]: ...

    def targetInfoChanged(
        self,
        callback_or_session: EventCallback[TargetInfoChangedEvent] | str | None = None,
        handler: EventCallback[TargetInfoChangedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[TargetInfoChangedEvent] | Unsubscribe:
        """Issued when some information about a target has changed. This only happens between `targetCreated` and `targetDestroyed`."""

        return cast(
            Awaitable[TargetInfoChangedEvent] | Unsubscribe,
            self._event(
                "targetInfoChanged",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )


__all__ = [
    "ActivateTargetParameters",
    "AttachToBrowserTargetResult",
    "AttachToTargetParameters",
    "AttachToTargetResult",
    "AttachedToTargetEvent",
    "AutoAttachRelatedParameters",
    "CloseTargetParameters",
    "CloseTargetResult",
    "CreateBrowserContextParameters",
    "CreateBrowserContextResult",
    "CreateTargetParameters",
    "CreateTargetResult",
    "DetachFromTargetParameters",
    "DetachedFromTargetEvent",
    "DisposeBrowserContextParameters",
    "ExposeDevToolsProtocolParameters",
    "FilterEntry",
    "GetBrowserContextsResult",
    "GetTargetInfoParameters",
    "GetTargetInfoResult",
    "GetTargetsParameters",
    "GetTargetsResult",
    "ReceivedMessageFromTargetEvent",
    "RemoteLocation",
    "SendMessageToTargetParameters",
    "SessionID",
    "SetAutoAttachParameters",
    "SetDiscoverTargetsParameters",
    "SetRemoteLocationsParameters",
    "Target",
    "TargetCrashedEvent",
    "TargetCreatedEvent",
    "TargetDestroyedEvent",
    "TargetFilter",
    "TargetID",
    "TargetInfo",
    "TargetInfoChangedEvent",
]
