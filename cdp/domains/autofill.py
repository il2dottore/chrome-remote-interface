"""Generated bindings for the CDP Autofill domain. Do not edit manually."""

from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, overload

from typing_extensions import NotRequired, TypedDict, Unpack

from cdp.domain import Domain as BaseDomain
from cdp.types import JsonObject

if TYPE_CHECKING:
    from . import dom as DOM
    from . import page as Page


class CreditCard(TypedDict):
    number: str
    name: str
    expiryMonth: str
    expiryYear: str
    cvc: str


class AddressField(TypedDict):
    name: str
    value: str


class Address(TypedDict):
    fields: list[AddressField]


class TriggerParameters(TypedDict):
    fieldId: DOM.BackendNodeId
    frameId: NotRequired[Page.FrameId]
    card: CreditCard


class SetAddressesParameters(TypedDict):
    addresses: list[Address]


class Autofill(BaseDomain):
    """Defines commands and events for Autofill."""

    domain_name = "Autofill"

    @overload
    async def trigger(
        self,
        params: TriggerParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def trigger(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[TriggerParameters],
    ) -> JsonObject: ...

    async def trigger(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Trigger autofill on a form identified by the fieldId. If the field and related form cannot be autofilled, returns an error."""

        return await self._command("trigger", params, session_id, kwargs)

    @overload
    async def setAddresses(
        self,
        params: SetAddressesParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def setAddresses(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetAddressesParameters],
    ) -> JsonObject: ...

    async def setAddresses(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Set addresses so that developers can verify their forms implementation."""

        return await self._command("setAddresses", params, session_id, kwargs)


__all__ = [
    "Address",
    "AddressField",
    "Autofill",
    "CreditCard",
    "SetAddressesParameters",
    "TriggerParameters",
]
