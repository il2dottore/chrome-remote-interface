"""Generated bindings for the CDP DigitalCredentials domain. Do not edit manually."""

from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Literal, TypeAlias, overload

from typing_extensions import NotRequired, TypedDict, Unpack

from cdp.domain import Domain as BaseDomain
from cdp.types import JsonObject

if TYPE_CHECKING:
    from . import page as Page


VirtualWalletAction: TypeAlias = Literal["respond", "decline", "wait", "clear"]


class SetVirtualWalletBehaviorParameters(TypedDict):
    action: VirtualWalletAction
    protocol: NotRequired[str]
    response: NotRequired[JsonObject]
    frameId: NotRequired[Page.FrameId]


class DigitalCredentials(BaseDomain):
    """This domain allows interacting with the Digital Credentials API for automation."""

    domain_name = "DigitalCredentials"

    @overload
    async def setVirtualWalletBehavior(
        self,
        params: SetVirtualWalletBehaviorParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def setVirtualWalletBehavior(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetVirtualWalletBehaviorParameters],
    ) -> JsonObject: ...

    async def setVirtualWalletBehavior(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Sets the behavior of the virtual wallet for digital credential requests issued from this frame."""

        return await self._command(
            "setVirtualWalletBehavior", params, session_id, kwargs
        )


__all__ = [
    "DigitalCredentials",
    "SetVirtualWalletBehaviorParameters",
    "VirtualWalletAction",
]
