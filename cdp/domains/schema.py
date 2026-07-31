"""Generated bindings for the CDP Schema domain. Do not edit manually."""

from __future__ import annotations

from typing import cast

from typing_extensions import TypedDict

from cdp.domain import Domain as BaseDomain


class Domain(TypedDict):
    name: str
    version: str


class GetDomainsResult(TypedDict):
    domains: list[Domain]


class Schema(BaseDomain):
    """This domain is deprecated."""

    domain_name = "Schema"

    async def getDomains(
        self,
        session_id: str | None = None,
    ) -> GetDomainsResult:
        """Returns supported domains."""

        return cast(
            GetDomainsResult, await self._command("getDomains", None, session_id, {})
        )


__all__ = ["Domain", "GetDomainsResult", "Schema"]
