"""Generated bindings for the CDP Performance domain. Do not edit manually."""

from __future__ import annotations

from collections.abc import Awaitable, Mapping
from typing import Literal, cast, overload

from typing_extensions import NotRequired, TypedDict, Unpack

from cdp.domain import Domain as BaseDomain, EventCallback, Unsubscribe
from cdp.types import JsonObject


class Metric(TypedDict):
    name: str
    value: float


class EnableParameters(TypedDict):
    timeDomain: NotRequired[Literal["timeTicks", "threadTicks"]]


class SetTimeDomainParameters(TypedDict):
    timeDomain: Literal["timeTicks", "threadTicks"]


class GetMetricsResult(TypedDict):
    metrics: list[Metric]


class MetricsEvent(TypedDict):
    metrics: list[Metric]
    title: str


class Performance(BaseDomain):
    """The CDP Performance domain."""

    domain_name = "Performance"

    async def disable(
        self,
        session_id: str | None = None,
    ) -> JsonObject:
        """Disable collecting and reporting metrics."""

        return await self._command("disable", None, session_id, {})

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
        """Enable collecting and reporting metrics."""

        return await self._command("enable", params, session_id, kwargs)

    @overload
    async def setTimeDomain(
        self,
        params: SetTimeDomainParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def setTimeDomain(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetTimeDomainParameters],
    ) -> JsonObject: ...

    async def setTimeDomain(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Sets time domain to use for collecting and reporting duration metrics. Note that this must be called before enabling metrics collection. Calling this method while metrics collection is enabled returns an error."""

        return await self._command("setTimeDomain", params, session_id, kwargs)

    async def getMetrics(
        self,
        session_id: str | None = None,
    ) -> GetMetricsResult:
        """Retrieve current values of run-time metrics."""

        return cast(
            GetMetricsResult, await self._command("getMetrics", None, session_id, {})
        )

    @overload
    def metrics(
        self,
        callback_or_session: EventCallback[MetricsEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def metrics(
        self,
        callback_or_session: str,
        handler: EventCallback[MetricsEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def metrics(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[MetricsEvent]: ...

    def metrics(
        self,
        callback_or_session: EventCallback[MetricsEvent] | str | None = None,
        handler: EventCallback[MetricsEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[MetricsEvent] | Unsubscribe:
        """Current values of the metrics."""

        return cast(
            Awaitable[MetricsEvent] | Unsubscribe,
            self._event(
                "metrics",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )


__all__ = [
    "EnableParameters",
    "GetMetricsResult",
    "Metric",
    "MetricsEvent",
    "Performance",
    "SetTimeDomainParameters",
]
