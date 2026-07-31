"""Generated bindings for the CDP WebAudio domain. Do not edit manually."""

from __future__ import annotations

from collections.abc import Awaitable, Mapping
from typing import Literal, TypeAlias, cast, overload

from typing_extensions import NotRequired, TypedDict, Unpack

from cdp.domain import Domain as BaseDomain, EventCallback, Unsubscribe
from cdp.types import JsonObject


GraphObjectId: TypeAlias = str

ContextType: TypeAlias = Literal["realtime", "offline"]

ContextState: TypeAlias = Literal["suspended", "running", "closed"]

NodeType: TypeAlias = str

ChannelCountMode: TypeAlias = Literal["clamped-max", "explicit", "max"]

ChannelInterpretation: TypeAlias = Literal["discrete", "speakers"]

ParamType: TypeAlias = str

AutomationRate: TypeAlias = Literal["a-rate", "k-rate"]


class ContextRealtimeData(TypedDict):
    currentTime: float
    renderCapacity: float
    callbackIntervalMean: float
    callbackIntervalVariance: float


class BaseAudioContext(TypedDict):
    contextId: GraphObjectId
    contextType: ContextType
    contextState: ContextState
    realtimeData: NotRequired[ContextRealtimeData]
    callbackBufferSize: float
    maxOutputChannelCount: float
    sampleRate: float


class AudioListener(TypedDict):
    listenerId: GraphObjectId
    contextId: GraphObjectId


class AudioNode(TypedDict):
    nodeId: GraphObjectId
    contextId: GraphObjectId
    nodeType: NodeType
    numberOfInputs: float
    numberOfOutputs: float
    channelCount: float
    channelCountMode: ChannelCountMode
    channelInterpretation: ChannelInterpretation


class AudioParam(TypedDict):
    paramId: GraphObjectId
    nodeId: GraphObjectId
    contextId: GraphObjectId
    paramType: ParamType
    rate: AutomationRate
    defaultValue: float
    minValue: float
    maxValue: float


class GetRealtimeDataParameters(TypedDict):
    contextId: GraphObjectId


class GetRealtimeDataResult(TypedDict):
    realtimeData: ContextRealtimeData


class ContextCreatedEvent(TypedDict):
    context: BaseAudioContext


class ContextWillBeDestroyedEvent(TypedDict):
    contextId: GraphObjectId


class ContextChangedEvent(TypedDict):
    context: BaseAudioContext


class AudioListenerCreatedEvent(TypedDict):
    listener: AudioListener


class AudioListenerWillBeDestroyedEvent(TypedDict):
    contextId: GraphObjectId
    listenerId: GraphObjectId


class AudioNodeCreatedEvent(TypedDict):
    node: AudioNode


class AudioNodeWillBeDestroyedEvent(TypedDict):
    contextId: GraphObjectId
    nodeId: GraphObjectId


class AudioParamCreatedEvent(TypedDict):
    param: AudioParam


class AudioParamWillBeDestroyedEvent(TypedDict):
    contextId: GraphObjectId
    nodeId: GraphObjectId
    paramId: GraphObjectId


class NodesConnectedEvent(TypedDict):
    contextId: GraphObjectId
    sourceId: GraphObjectId
    destinationId: GraphObjectId
    sourceOutputIndex: NotRequired[float]
    destinationInputIndex: NotRequired[float]


class NodesDisconnectedEvent(TypedDict):
    contextId: GraphObjectId
    sourceId: GraphObjectId
    destinationId: GraphObjectId
    sourceOutputIndex: NotRequired[float]
    destinationInputIndex: NotRequired[float]


class NodeParamConnectedEvent(TypedDict):
    contextId: GraphObjectId
    sourceId: GraphObjectId
    destinationId: GraphObjectId
    sourceOutputIndex: NotRequired[float]


class NodeParamDisconnectedEvent(TypedDict):
    contextId: GraphObjectId
    sourceId: GraphObjectId
    destinationId: GraphObjectId
    sourceOutputIndex: NotRequired[float]


class WebAudio(BaseDomain):
    """This domain allows inspection of Web Audio API. https://webaudio.github.io/web-audio-api/"""

    domain_name = "WebAudio"

    async def enable(
        self,
        session_id: str | None = None,
    ) -> JsonObject:
        """Enables the WebAudio domain and starts sending context lifetime events."""

        return await self._command("enable", None, session_id, {})

    async def disable(
        self,
        session_id: str | None = None,
    ) -> JsonObject:
        """Disables the WebAudio domain."""

        return await self._command("disable", None, session_id, {})

    @overload
    async def getRealtimeData(
        self,
        params: GetRealtimeDataParameters,
        session_id: str | None = None,
    ) -> GetRealtimeDataResult: ...

    @overload
    async def getRealtimeData(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[GetRealtimeDataParameters],
    ) -> GetRealtimeDataResult: ...

    async def getRealtimeData(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> GetRealtimeDataResult:
        """Fetch the realtime data from the registered contexts."""

        return cast(
            GetRealtimeDataResult,
            await self._command("getRealtimeData", params, session_id, kwargs),
        )

    @overload
    def contextCreated(
        self,
        callback_or_session: EventCallback[ContextCreatedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def contextCreated(
        self,
        callback_or_session: str,
        handler: EventCallback[ContextCreatedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def contextCreated(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[ContextCreatedEvent]: ...

    def contextCreated(
        self,
        callback_or_session: EventCallback[ContextCreatedEvent] | str | None = None,
        handler: EventCallback[ContextCreatedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[ContextCreatedEvent] | Unsubscribe:
        """Notifies that a new BaseAudioContext has been created."""

        return cast(
            Awaitable[ContextCreatedEvent] | Unsubscribe,
            self._event(
                "contextCreated",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def contextWillBeDestroyed(
        self,
        callback_or_session: EventCallback[ContextWillBeDestroyedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def contextWillBeDestroyed(
        self,
        callback_or_session: str,
        handler: EventCallback[ContextWillBeDestroyedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def contextWillBeDestroyed(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[ContextWillBeDestroyedEvent]: ...

    def contextWillBeDestroyed(
        self,
        callback_or_session: EventCallback[ContextWillBeDestroyedEvent]
        | str
        | None = None,
        handler: EventCallback[ContextWillBeDestroyedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[ContextWillBeDestroyedEvent] | Unsubscribe:
        """Notifies that an existing BaseAudioContext will be destroyed."""

        return cast(
            Awaitable[ContextWillBeDestroyedEvent] | Unsubscribe,
            self._event(
                "contextWillBeDestroyed",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def contextChanged(
        self,
        callback_or_session: EventCallback[ContextChangedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def contextChanged(
        self,
        callback_or_session: str,
        handler: EventCallback[ContextChangedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def contextChanged(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[ContextChangedEvent]: ...

    def contextChanged(
        self,
        callback_or_session: EventCallback[ContextChangedEvent] | str | None = None,
        handler: EventCallback[ContextChangedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[ContextChangedEvent] | Unsubscribe:
        """Notifies that existing BaseAudioContext has changed some properties (id stays the same).."""

        return cast(
            Awaitable[ContextChangedEvent] | Unsubscribe,
            self._event(
                "contextChanged",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def audioListenerCreated(
        self,
        callback_or_session: EventCallback[AudioListenerCreatedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def audioListenerCreated(
        self,
        callback_or_session: str,
        handler: EventCallback[AudioListenerCreatedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def audioListenerCreated(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[AudioListenerCreatedEvent]: ...

    def audioListenerCreated(
        self,
        callback_or_session: EventCallback[AudioListenerCreatedEvent]
        | str
        | None = None,
        handler: EventCallback[AudioListenerCreatedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[AudioListenerCreatedEvent] | Unsubscribe:
        """Notifies that the construction of an AudioListener has finished."""

        return cast(
            Awaitable[AudioListenerCreatedEvent] | Unsubscribe,
            self._event(
                "audioListenerCreated",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def audioListenerWillBeDestroyed(
        self,
        callback_or_session: EventCallback[AudioListenerWillBeDestroyedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def audioListenerWillBeDestroyed(
        self,
        callback_or_session: str,
        handler: EventCallback[AudioListenerWillBeDestroyedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def audioListenerWillBeDestroyed(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[AudioListenerWillBeDestroyedEvent]: ...

    def audioListenerWillBeDestroyed(
        self,
        callback_or_session: EventCallback[AudioListenerWillBeDestroyedEvent]
        | str
        | None = None,
        handler: EventCallback[AudioListenerWillBeDestroyedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[AudioListenerWillBeDestroyedEvent] | Unsubscribe:
        """Notifies that a new AudioListener has been created."""

        return cast(
            Awaitable[AudioListenerWillBeDestroyedEvent] | Unsubscribe,
            self._event(
                "audioListenerWillBeDestroyed",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def audioNodeCreated(
        self,
        callback_or_session: EventCallback[AudioNodeCreatedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def audioNodeCreated(
        self,
        callback_or_session: str,
        handler: EventCallback[AudioNodeCreatedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def audioNodeCreated(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[AudioNodeCreatedEvent]: ...

    def audioNodeCreated(
        self,
        callback_or_session: EventCallback[AudioNodeCreatedEvent] | str | None = None,
        handler: EventCallback[AudioNodeCreatedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[AudioNodeCreatedEvent] | Unsubscribe:
        """Notifies that a new AudioNode has been created."""

        return cast(
            Awaitable[AudioNodeCreatedEvent] | Unsubscribe,
            self._event(
                "audioNodeCreated",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def audioNodeWillBeDestroyed(
        self,
        callback_or_session: EventCallback[AudioNodeWillBeDestroyedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def audioNodeWillBeDestroyed(
        self,
        callback_or_session: str,
        handler: EventCallback[AudioNodeWillBeDestroyedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def audioNodeWillBeDestroyed(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[AudioNodeWillBeDestroyedEvent]: ...

    def audioNodeWillBeDestroyed(
        self,
        callback_or_session: EventCallback[AudioNodeWillBeDestroyedEvent]
        | str
        | None = None,
        handler: EventCallback[AudioNodeWillBeDestroyedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[AudioNodeWillBeDestroyedEvent] | Unsubscribe:
        """Notifies that an existing AudioNode has been destroyed."""

        return cast(
            Awaitable[AudioNodeWillBeDestroyedEvent] | Unsubscribe,
            self._event(
                "audioNodeWillBeDestroyed",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def audioParamCreated(
        self,
        callback_or_session: EventCallback[AudioParamCreatedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def audioParamCreated(
        self,
        callback_or_session: str,
        handler: EventCallback[AudioParamCreatedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def audioParamCreated(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[AudioParamCreatedEvent]: ...

    def audioParamCreated(
        self,
        callback_or_session: EventCallback[AudioParamCreatedEvent] | str | None = None,
        handler: EventCallback[AudioParamCreatedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[AudioParamCreatedEvent] | Unsubscribe:
        """Notifies that a new AudioParam has been created."""

        return cast(
            Awaitable[AudioParamCreatedEvent] | Unsubscribe,
            self._event(
                "audioParamCreated",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def audioParamWillBeDestroyed(
        self,
        callback_or_session: EventCallback[AudioParamWillBeDestroyedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def audioParamWillBeDestroyed(
        self,
        callback_or_session: str,
        handler: EventCallback[AudioParamWillBeDestroyedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def audioParamWillBeDestroyed(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[AudioParamWillBeDestroyedEvent]: ...

    def audioParamWillBeDestroyed(
        self,
        callback_or_session: EventCallback[AudioParamWillBeDestroyedEvent]
        | str
        | None = None,
        handler: EventCallback[AudioParamWillBeDestroyedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[AudioParamWillBeDestroyedEvent] | Unsubscribe:
        """Notifies that an existing AudioParam has been destroyed."""

        return cast(
            Awaitable[AudioParamWillBeDestroyedEvent] | Unsubscribe,
            self._event(
                "audioParamWillBeDestroyed",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def nodesConnected(
        self,
        callback_or_session: EventCallback[NodesConnectedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def nodesConnected(
        self,
        callback_or_session: str,
        handler: EventCallback[NodesConnectedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def nodesConnected(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[NodesConnectedEvent]: ...

    def nodesConnected(
        self,
        callback_or_session: EventCallback[NodesConnectedEvent] | str | None = None,
        handler: EventCallback[NodesConnectedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[NodesConnectedEvent] | Unsubscribe:
        """Notifies that two AudioNodes are connected."""

        return cast(
            Awaitable[NodesConnectedEvent] | Unsubscribe,
            self._event(
                "nodesConnected",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def nodesDisconnected(
        self,
        callback_or_session: EventCallback[NodesDisconnectedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def nodesDisconnected(
        self,
        callback_or_session: str,
        handler: EventCallback[NodesDisconnectedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def nodesDisconnected(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[NodesDisconnectedEvent]: ...

    def nodesDisconnected(
        self,
        callback_or_session: EventCallback[NodesDisconnectedEvent] | str | None = None,
        handler: EventCallback[NodesDisconnectedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[NodesDisconnectedEvent] | Unsubscribe:
        """Notifies that AudioNodes are disconnected. The destination can be null, and it means all the outgoing connections from the source are disconnected."""

        return cast(
            Awaitable[NodesDisconnectedEvent] | Unsubscribe,
            self._event(
                "nodesDisconnected",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def nodeParamConnected(
        self,
        callback_or_session: EventCallback[NodeParamConnectedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def nodeParamConnected(
        self,
        callback_or_session: str,
        handler: EventCallback[NodeParamConnectedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def nodeParamConnected(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[NodeParamConnectedEvent]: ...

    def nodeParamConnected(
        self,
        callback_or_session: EventCallback[NodeParamConnectedEvent] | str | None = None,
        handler: EventCallback[NodeParamConnectedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[NodeParamConnectedEvent] | Unsubscribe:
        """Notifies that an AudioNode is connected to an AudioParam."""

        return cast(
            Awaitable[NodeParamConnectedEvent] | Unsubscribe,
            self._event(
                "nodeParamConnected",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def nodeParamDisconnected(
        self,
        callback_or_session: EventCallback[NodeParamDisconnectedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def nodeParamDisconnected(
        self,
        callback_or_session: str,
        handler: EventCallback[NodeParamDisconnectedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def nodeParamDisconnected(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[NodeParamDisconnectedEvent]: ...

    def nodeParamDisconnected(
        self,
        callback_or_session: EventCallback[NodeParamDisconnectedEvent]
        | str
        | None = None,
        handler: EventCallback[NodeParamDisconnectedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[NodeParamDisconnectedEvent] | Unsubscribe:
        """Notifies that an AudioNode is disconnected to an AudioParam."""

        return cast(
            Awaitable[NodeParamDisconnectedEvent] | Unsubscribe,
            self._event(
                "nodeParamDisconnected",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )


__all__ = [
    "AudioListener",
    "AudioListenerCreatedEvent",
    "AudioListenerWillBeDestroyedEvent",
    "AudioNode",
    "AudioNodeCreatedEvent",
    "AudioNodeWillBeDestroyedEvent",
    "AudioParam",
    "AudioParamCreatedEvent",
    "AudioParamWillBeDestroyedEvent",
    "AutomationRate",
    "BaseAudioContext",
    "ChannelCountMode",
    "ChannelInterpretation",
    "ContextChangedEvent",
    "ContextCreatedEvent",
    "ContextRealtimeData",
    "ContextState",
    "ContextType",
    "ContextWillBeDestroyedEvent",
    "GetRealtimeDataParameters",
    "GetRealtimeDataResult",
    "GraphObjectId",
    "NodeParamConnectedEvent",
    "NodeParamDisconnectedEvent",
    "NodeType",
    "NodesConnectedEvent",
    "NodesDisconnectedEvent",
    "ParamType",
    "WebAudio",
]
