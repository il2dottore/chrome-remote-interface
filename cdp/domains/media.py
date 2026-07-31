"""Generated bindings for the CDP Media domain. Do not edit manually."""

from __future__ import annotations

from collections.abc import Awaitable, Mapping
from typing import Literal, TypeAlias, cast, overload

from typing_extensions import TypedDict

from cdp.domain import Domain as BaseDomain, EventCallback, Unsubscribe
from cdp.types import JsonObject


PlayerId: TypeAlias = str

Timestamp: TypeAlias = float


class PlayerMessage(TypedDict):
    level: Literal["error", "warning", "info", "debug"]
    message: str


class PlayerProperty(TypedDict):
    name: str
    value: str


class PlayerEvent(TypedDict):
    timestamp: Timestamp
    value: str


class PlayerErrorSourceLocation(TypedDict):
    file: str
    line: int


class PlayerError(TypedDict):
    errorType: str
    code: int
    stack: list[PlayerErrorSourceLocation]
    cause: list[PlayerError]
    data: JsonObject


class PlayerPropertiesChangedEvent(TypedDict):
    playerId: PlayerId
    properties: list[PlayerProperty]


class PlayerEventsAddedEvent(TypedDict):
    playerId: PlayerId
    events: list[PlayerEvent]


class PlayerMessagesLoggedEvent(TypedDict):
    playerId: PlayerId
    messages: list[PlayerMessage]


class PlayerErrorsRaisedEvent(TypedDict):
    playerId: PlayerId
    errors: list[PlayerError]


class PlayersCreatedEvent(TypedDict):
    players: list[PlayerId]


class Media(BaseDomain):
    """This domain allows detailed inspection of media elements"""

    domain_name = "Media"

    async def enable(
        self,
        session_id: str | None = None,
    ) -> JsonObject:
        """Enables the Media domain"""

        return await self._command("enable", None, session_id, {})

    async def disable(
        self,
        session_id: str | None = None,
    ) -> JsonObject:
        """Disables the Media domain."""

        return await self._command("disable", None, session_id, {})

    @overload
    def playerPropertiesChanged(
        self,
        callback_or_session: EventCallback[PlayerPropertiesChangedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def playerPropertiesChanged(
        self,
        callback_or_session: str,
        handler: EventCallback[PlayerPropertiesChangedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def playerPropertiesChanged(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[PlayerPropertiesChangedEvent]: ...

    def playerPropertiesChanged(
        self,
        callback_or_session: EventCallback[PlayerPropertiesChangedEvent]
        | str
        | None = None,
        handler: EventCallback[PlayerPropertiesChangedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[PlayerPropertiesChangedEvent] | Unsubscribe:
        """This can be called multiple times, and can be used to set / override / remove player properties. A null propValue indicates removal."""

        return cast(
            Awaitable[PlayerPropertiesChangedEvent] | Unsubscribe,
            self._event(
                "playerPropertiesChanged",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def playerEventsAdded(
        self,
        callback_or_session: EventCallback[PlayerEventsAddedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def playerEventsAdded(
        self,
        callback_or_session: str,
        handler: EventCallback[PlayerEventsAddedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def playerEventsAdded(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[PlayerEventsAddedEvent]: ...

    def playerEventsAdded(
        self,
        callback_or_session: EventCallback[PlayerEventsAddedEvent] | str | None = None,
        handler: EventCallback[PlayerEventsAddedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[PlayerEventsAddedEvent] | Unsubscribe:
        """Send events as a list, allowing them to be batched on the browser for less congestion. If batched, events must ALWAYS be in chronological order."""

        return cast(
            Awaitable[PlayerEventsAddedEvent] | Unsubscribe,
            self._event(
                "playerEventsAdded",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def playerMessagesLogged(
        self,
        callback_or_session: EventCallback[PlayerMessagesLoggedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def playerMessagesLogged(
        self,
        callback_or_session: str,
        handler: EventCallback[PlayerMessagesLoggedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def playerMessagesLogged(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[PlayerMessagesLoggedEvent]: ...

    def playerMessagesLogged(
        self,
        callback_or_session: EventCallback[PlayerMessagesLoggedEvent]
        | str
        | None = None,
        handler: EventCallback[PlayerMessagesLoggedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[PlayerMessagesLoggedEvent] | Unsubscribe:
        """Send a list of any messages that need to be delivered."""

        return cast(
            Awaitable[PlayerMessagesLoggedEvent] | Unsubscribe,
            self._event(
                "playerMessagesLogged",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def playerErrorsRaised(
        self,
        callback_or_session: EventCallback[PlayerErrorsRaisedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def playerErrorsRaised(
        self,
        callback_or_session: str,
        handler: EventCallback[PlayerErrorsRaisedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def playerErrorsRaised(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[PlayerErrorsRaisedEvent]: ...

    def playerErrorsRaised(
        self,
        callback_or_session: EventCallback[PlayerErrorsRaisedEvent] | str | None = None,
        handler: EventCallback[PlayerErrorsRaisedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[PlayerErrorsRaisedEvent] | Unsubscribe:
        """Send a list of any errors that need to be delivered."""

        return cast(
            Awaitable[PlayerErrorsRaisedEvent] | Unsubscribe,
            self._event(
                "playerErrorsRaised",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def playersCreated(
        self,
        callback_or_session: EventCallback[PlayersCreatedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def playersCreated(
        self,
        callback_or_session: str,
        handler: EventCallback[PlayersCreatedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def playersCreated(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[PlayersCreatedEvent]: ...

    def playersCreated(
        self,
        callback_or_session: EventCallback[PlayersCreatedEvent] | str | None = None,
        handler: EventCallback[PlayersCreatedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[PlayersCreatedEvent] | Unsubscribe:
        """Called whenever a player is created, or when a new agent joins and receives a list of active players. If an agent is restored, it will receive the full list of player ids and all events again."""

        return cast(
            Awaitable[PlayersCreatedEvent] | Unsubscribe,
            self._event(
                "playersCreated",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )


__all__ = [
    "Media",
    "PlayerError",
    "PlayerErrorSourceLocation",
    "PlayerErrorsRaisedEvent",
    "PlayerEvent",
    "PlayerEventsAddedEvent",
    "PlayerId",
    "PlayerMessage",
    "PlayerMessagesLoggedEvent",
    "PlayerPropertiesChangedEvent",
    "PlayerProperty",
    "PlayersCreatedEvent",
    "Timestamp",
]
