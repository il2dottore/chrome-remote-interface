"""Generated bindings for the CDP Autofill domain. Do not edit manually."""

from __future__ import annotations

from collections.abc import Awaitable, Mapping
from typing import TYPE_CHECKING, Literal, TypeAlias, cast, overload

from typing_extensions import NotRequired, TypedDict, Unpack

from cdp.domain import Domain as BaseDomain, EventCallback, Unsubscribe
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


class AddressFields(TypedDict):
    fields: list[AddressField]


class Address(TypedDict):
    fields: list[AddressField]


class AddressUI(TypedDict):
    addressFields: list[AddressFields]


FillingStrategy: TypeAlias = Literal["autocompleteAttribute", "autofillInferred"]


class FilledField(TypedDict):
    htmlType: str
    id: str
    name: str
    value: str
    autofillType: str
    fillingStrategy: FillingStrategy
    frameId: Page.FrameId
    fieldId: DOM.BackendNodeId


class TriggerParameters(TypedDict):
    fieldId: DOM.BackendNodeId
    frameId: NotRequired[Page.FrameId]
    card: NotRequired[CreditCard]
    address: NotRequired[Address]


class SetAddressesParameters(TypedDict):
    addresses: list[Address]


class AddressFormFilledEvent(TypedDict):
    filledFields: list[FilledField]
    addressUi: AddressUI


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

    async def disable(
        self,
        session_id: str | None = None,
    ) -> JsonObject:
        """Disables autofill domain notifications."""

        return await self._command("disable", None, session_id, {})

    async def enable(
        self,
        session_id: str | None = None,
    ) -> JsonObject:
        """Enables autofill domain notifications."""

        return await self._command("enable", None, session_id, {})

    @overload
    def addressFormFilled(
        self,
        callback_or_session: EventCallback[AddressFormFilledEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def addressFormFilled(
        self,
        callback_or_session: str,
        handler: EventCallback[AddressFormFilledEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def addressFormFilled(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[AddressFormFilledEvent]: ...

    def addressFormFilled(
        self,
        callback_or_session: EventCallback[AddressFormFilledEvent] | str | None = None,
        handler: EventCallback[AddressFormFilledEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[AddressFormFilledEvent] | Unsubscribe:
        """Emitted when an address form is filled."""

        return cast(
            Awaitable[AddressFormFilledEvent] | Unsubscribe,
            self._event(
                "addressFormFilled",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )


__all__ = [
    "Address",
    "AddressField",
    "AddressFields",
    "AddressFormFilledEvent",
    "AddressUI",
    "Autofill",
    "CreditCard",
    "FilledField",
    "FillingStrategy",
    "SetAddressesParameters",
    "TriggerParameters",
]
