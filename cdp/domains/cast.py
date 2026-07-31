"""Generated bindings for the CDP Cast domain. Do not edit manually."""

from __future__ import annotations

from collections.abc import Awaitable, Mapping
from typing import cast, overload

from typing_extensions import NotRequired, TypedDict, Unpack

from cdp.domain import Domain as BaseDomain, EventCallback, Unsubscribe
from cdp.types import JsonObject


class Sink(TypedDict):
    name: str
    id: str
    session: NotRequired[str]


class EnableParameters(TypedDict):
    presentationUrl: NotRequired[str]


class SetSinkToUseParameters(TypedDict):
    sinkName: str


class StartDesktopMirroringParameters(TypedDict):
    sinkName: str


class StartTabMirroringParameters(TypedDict):
    sinkName: str


class StopCastingParameters(TypedDict):
    sinkName: str


class SinksUpdatedEvent(TypedDict):
    sinks: list[Sink]


class IssueUpdatedEvent(TypedDict):
    issueMessage: str


class Cast(BaseDomain):
    """A domain for interacting with Cast, Presentation API, and Remote Playback API functionalities."""

    domain_name = "Cast"

    @overload
    async def enable(
        self,
        params: EnableParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def enable(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[EnableParameters],
    ) -> JsonObject: ...

    async def enable(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Starts observing for sinks that can be used for tab mirroring, and if set, sinks compatible with |presentationUrl| as well. When sinks are found, a |sinksUpdated| event is fired. Also starts observing for issue messages. When an issue is added or removed, an |issueUpdated| event is fired."""

        return await self._command("enable", params, session_id, kwargs)

    async def disable(
        self,
        session_id: str | None = None,
    ) -> JsonObject:
        """Stops observing for sinks and issues."""

        return await self._command("disable", None, session_id, {})

    @overload
    async def setSinkToUse(
        self,
        params: SetSinkToUseParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def setSinkToUse(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetSinkToUseParameters],
    ) -> JsonObject: ...

    async def setSinkToUse(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Sets a sink to be used when the web page requests the browser to choose a sink via Presentation API, Remote Playback API, or Cast SDK."""

        return await self._command("setSinkToUse", params, session_id, kwargs)

    @overload
    async def startDesktopMirroring(
        self,
        params: StartDesktopMirroringParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def startDesktopMirroring(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[StartDesktopMirroringParameters],
    ) -> JsonObject: ...

    async def startDesktopMirroring(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Starts mirroring the desktop to the sink."""

        return await self._command("startDesktopMirroring", params, session_id, kwargs)

    @overload
    async def startTabMirroring(
        self,
        params: StartTabMirroringParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def startTabMirroring(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[StartTabMirroringParameters],
    ) -> JsonObject: ...

    async def startTabMirroring(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Starts mirroring the tab to the sink."""

        return await self._command("startTabMirroring", params, session_id, kwargs)

    @overload
    async def stopCasting(
        self,
        params: StopCastingParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def stopCasting(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[StopCastingParameters],
    ) -> JsonObject: ...

    async def stopCasting(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Stops the active Cast session on the sink."""

        return await self._command("stopCasting", params, session_id, kwargs)

    @overload
    def sinksUpdated(
        self,
        callback_or_session: EventCallback[SinksUpdatedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def sinksUpdated(
        self,
        callback_or_session: str,
        handler: EventCallback[SinksUpdatedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def sinksUpdated(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[SinksUpdatedEvent]: ...

    def sinksUpdated(
        self,
        callback_or_session: EventCallback[SinksUpdatedEvent] | str | None = None,
        handler: EventCallback[SinksUpdatedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[SinksUpdatedEvent] | Unsubscribe:
        """This is fired whenever the list of available sinks changes. A sink is a device or a software surface that you can cast to."""

        return cast(
            Awaitable[SinksUpdatedEvent] | Unsubscribe,
            self._event(
                "sinksUpdated",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def issueUpdated(
        self,
        callback_or_session: EventCallback[IssueUpdatedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def issueUpdated(
        self,
        callback_or_session: str,
        handler: EventCallback[IssueUpdatedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def issueUpdated(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[IssueUpdatedEvent]: ...

    def issueUpdated(
        self,
        callback_or_session: EventCallback[IssueUpdatedEvent] | str | None = None,
        handler: EventCallback[IssueUpdatedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[IssueUpdatedEvent] | Unsubscribe:
        """This is fired whenever the outstanding issue/error message changes. |issueMessage| is empty if there is no issue."""

        return cast(
            Awaitable[IssueUpdatedEvent] | Unsubscribe,
            self._event(
                "issueUpdated",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )


__all__ = [
    "Cast",
    "EnableParameters",
    "IssueUpdatedEvent",
    "SetSinkToUseParameters",
    "Sink",
    "SinksUpdatedEvent",
    "StartDesktopMirroringParameters",
    "StartTabMirroringParameters",
    "StopCastingParameters",
]
