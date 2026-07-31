"""Generated bindings for the CDP Ads domain. Do not edit manually."""

from __future__ import annotations

from typing import TYPE_CHECKING, cast

from typing_extensions import NotRequired, TypedDict

from cdp.domain import Domain as BaseDomain

if TYPE_CHECKING:
    from . import page as Page


class AdFrameData(TypedDict):
    frameId: Page.FrameId
    initialOrigin: NotRequired[str]
    networkBytes: float
    cpuTime: float


class AdMetrics(TypedDict):
    viewportAdDensityByArea: int
    averageViewportAdDensityByArea: float
    viewportAdCount: int
    averageViewportAdCount: float
    totalAdCpuTime: float
    totalAdNetworkBytes: float
    updateAdFrames: list[AdFrameData]
    removeAdFrames: list[Page.FrameId]


class GetAdMetricsResult(TypedDict):
    metrics: AdMetrics


class Ads(BaseDomain):
    """A domain for ad-related metrics and data."""

    domain_name = "Ads"

    async def getAdMetrics(
        self,
        session_id: str | None = None,
    ) -> GetAdMetricsResult:
        """Retrieves ad metrics for the current page."""

        return cast(
            GetAdMetricsResult,
            await self._command("getAdMetrics", None, session_id, {}),
        )


__all__ = ["AdFrameData", "AdMetrics", "Ads", "GetAdMetricsResult"]
