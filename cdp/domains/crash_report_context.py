"""Generated bindings for the CDP CrashReportContext domain. Do not edit manually."""

from __future__ import annotations

from typing import TYPE_CHECKING, cast

from typing_extensions import TypedDict

from cdp.domain import Domain as BaseDomain

if TYPE_CHECKING:
    from . import page as Page


class CrashReportContextEntry(TypedDict):
    key: str
    value: str
    frameId: Page.FrameId


class GetEntriesResult(TypedDict):
    entries: list[CrashReportContextEntry]


class CrashReportContext(BaseDomain):
    """This domain exposes the current state of the CrashReportContext API."""

    domain_name = "CrashReportContext"

    async def getEntries(
        self,
        session_id: str | None = None,
    ) -> GetEntriesResult:
        """Returns all entries in the CrashReportContext across all frames in the page."""

        return cast(
            GetEntriesResult, await self._command("getEntries", None, session_id, {})
        )


__all__ = ["CrashReportContext", "CrashReportContextEntry", "GetEntriesResult"]
