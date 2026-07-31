"""Generated bindings for the CDP HeadlessExperimental domain. Do not edit manually."""

from __future__ import annotations

from collections.abc import Mapping
from typing import Literal, cast, overload

from typing_extensions import NotRequired, TypedDict, Unpack

from cdp.domain import Domain as BaseDomain
from cdp.types import JsonObject


class ScreenshotParams(TypedDict):
    format: NotRequired[Literal["jpeg", "png", "webp"]]
    quality: NotRequired[int]
    optimizeForSpeed: NotRequired[bool]


class BeginFrameParameters(TypedDict):
    frameTimeTicks: NotRequired[float]
    interval: NotRequired[float]
    noDisplayUpdates: NotRequired[bool]
    screenshot: NotRequired[ScreenshotParams]


class BeginFrameResult(TypedDict):
    hasDamage: bool
    screenshotData: NotRequired[str]


class HeadlessExperimental(BaseDomain):
    """This domain provides experimental commands only supported in headless mode."""

    domain_name = "HeadlessExperimental"

    @overload
    async def beginFrame(
        self,
        params: BeginFrameParameters,
        session_id: str | None = None,
    ) -> BeginFrameResult: ...

    @overload
    async def beginFrame(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[BeginFrameParameters],
    ) -> BeginFrameResult: ...

    async def beginFrame(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> BeginFrameResult:
        """Sends a BeginFrame to the target and returns when the frame was completed. Optionally captures a screenshot from the resulting frame. Requires that the target was created with enabled BeginFrameControl. Designed for use with --run-all-compositor-stages-before-draw, see also https://goo.gle/chrome-headless-rendering for more background."""

        return cast(
            BeginFrameResult,
            await self._command("beginFrame", params, session_id, kwargs),
        )

    async def disable(
        self,
        session_id: str | None = None,
    ) -> JsonObject:
        """Disables headless events for the target."""

        return await self._command("disable", None, session_id, {})

    async def enable(
        self,
        session_id: str | None = None,
    ) -> JsonObject:
        """Enables headless events for the target."""

        return await self._command("enable", None, session_id, {})


__all__ = [
    "BeginFrameParameters",
    "BeginFrameResult",
    "HeadlessExperimental",
    "ScreenshotParams",
]
