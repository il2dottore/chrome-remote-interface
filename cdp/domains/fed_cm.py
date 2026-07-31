"""Generated bindings for the CDP FedCm domain. Do not edit manually."""

from __future__ import annotations

from collections.abc import Awaitable, Mapping
from typing import Literal, TypeAlias, cast, overload

from typing_extensions import NotRequired, TypedDict, Unpack

from cdp.domain import Domain as BaseDomain, EventCallback, Unsubscribe
from cdp.types import JsonObject


LoginState: TypeAlias = Literal["SignIn", "SignUp"]

DialogType: TypeAlias = Literal["AccountChooser", "AutoReauthn"]


class Account(TypedDict):
    accountId: str
    email: str
    name: str
    givenName: str
    pictureUrl: str
    idpConfigUrl: str
    idpSigninUrl: str
    loginState: LoginState
    termsOfServiceUrl: NotRequired[str]
    privacyPolicyUrl: NotRequired[str]


class EnableParameters(TypedDict):
    disableRejectionDelay: NotRequired[bool]


class SelectAccountParameters(TypedDict):
    dialogId: str
    accountIndex: int


class DismissDialogParameters(TypedDict):
    dialogId: str
    triggerCooldown: NotRequired[bool]


class DialogShownEvent(TypedDict):
    dialogId: str
    dialogType: DialogType
    accounts: list[Account]
    title: str
    subtitle: NotRequired[str]


class FedCm(BaseDomain):
    """This domain allows interacting with the FedCM dialog."""

    domain_name = "FedCm"

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
        """Send FedCm.enable."""

        return await self._command("enable", params, session_id, kwargs)

    async def disable(
        self,
        session_id: str | None = None,
    ) -> JsonObject:
        """Send FedCm.disable."""

        return await self._command("disable", None, session_id, {})

    @overload
    async def selectAccount(
        self,
        params: SelectAccountParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def selectAccount(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SelectAccountParameters],
    ) -> JsonObject: ...

    async def selectAccount(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Send FedCm.selectAccount."""

        return await self._command("selectAccount", params, session_id, kwargs)

    @overload
    async def dismissDialog(
        self,
        params: DismissDialogParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def dismissDialog(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[DismissDialogParameters],
    ) -> JsonObject: ...

    async def dismissDialog(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Send FedCm.dismissDialog."""

        return await self._command("dismissDialog", params, session_id, kwargs)

    async def resetCooldown(
        self,
        session_id: str | None = None,
    ) -> JsonObject:
        """Resets the cooldown time, if any, to allow the next FedCM call to show a dialog even if one was recently dismissed by the user."""

        return await self._command("resetCooldown", None, session_id, {})

    @overload
    def dialogShown(
        self,
        callback_or_session: EventCallback[DialogShownEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def dialogShown(
        self,
        callback_or_session: str,
        handler: EventCallback[DialogShownEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def dialogShown(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[DialogShownEvent]: ...

    def dialogShown(
        self,
        callback_or_session: EventCallback[DialogShownEvent] | str | None = None,
        handler: EventCallback[DialogShownEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[DialogShownEvent] | Unsubscribe:
        """Wait for or subscribe to FedCm.dialogShown."""

        return cast(
            Awaitable[DialogShownEvent] | Unsubscribe,
            self._event(
                "dialogShown",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )


__all__ = [
    "Account",
    "DialogShownEvent",
    "DialogType",
    "DismissDialogParameters",
    "EnableParameters",
    "FedCm",
    "LoginState",
    "SelectAccountParameters",
]
