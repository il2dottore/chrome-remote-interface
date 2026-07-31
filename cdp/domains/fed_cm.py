"""Generated bindings for the CDP FedCm domain. Do not edit manually."""

from __future__ import annotations

from collections.abc import Awaitable, Mapping
from typing import Literal, TypeAlias, cast, overload

from typing_extensions import NotRequired, TypedDict, Unpack

from cdp.domain import Domain as BaseDomain, EventCallback, Unsubscribe
from cdp.types import JsonObject


LoginState: TypeAlias = Literal["SignIn", "SignUp"]

DialogType: TypeAlias = Literal[
    "AccountChooser", "AutoReauthn", "ConfirmIdpLogin", "Error"
]

DialogButton: TypeAlias = Literal[
    "ConfirmIdpLoginContinue", "ErrorGotIt", "ErrorMoreDetails"
]

AccountUrlType: TypeAlias = Literal["TermsOfService", "PrivacyPolicy"]


class Account(TypedDict):
    accountId: str
    email: str
    name: str
    givenName: str
    pictureUrl: str
    idpConfigUrl: str
    idpLoginUrl: str
    loginState: LoginState
    termsOfServiceUrl: NotRequired[str]
    privacyPolicyUrl: NotRequired[str]


class EnableParameters(TypedDict):
    disableRejectionDelay: NotRequired[bool]


class SelectAccountParameters(TypedDict):
    dialogId: str
    accountIndex: int


class ClickDialogButtonParameters(TypedDict):
    dialogId: str
    dialogButton: DialogButton


class OpenUrlParameters(TypedDict):
    dialogId: str
    accountIndex: int
    accountUrlType: AccountUrlType


class DismissDialogParameters(TypedDict):
    dialogId: str
    triggerCooldown: NotRequired[bool]


class DialogShownEvent(TypedDict):
    dialogId: str
    dialogType: DialogType
    accounts: list[Account]
    title: str
    subtitle: NotRequired[str]


class DialogClosedEvent(TypedDict):
    dialogId: str


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
    async def clickDialogButton(
        self,
        params: ClickDialogButtonParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def clickDialogButton(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[ClickDialogButtonParameters],
    ) -> JsonObject: ...

    async def clickDialogButton(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Send FedCm.clickDialogButton."""

        return await self._command("clickDialogButton", params, session_id, kwargs)

    @overload
    async def openUrl(
        self,
        params: OpenUrlParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def openUrl(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[OpenUrlParameters],
    ) -> JsonObject: ...

    async def openUrl(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Send FedCm.openUrl."""

        return await self._command("openUrl", params, session_id, kwargs)

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

    @overload
    def dialogClosed(
        self,
        callback_or_session: EventCallback[DialogClosedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def dialogClosed(
        self,
        callback_or_session: str,
        handler: EventCallback[DialogClosedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def dialogClosed(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[DialogClosedEvent]: ...

    def dialogClosed(
        self,
        callback_or_session: EventCallback[DialogClosedEvent] | str | None = None,
        handler: EventCallback[DialogClosedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[DialogClosedEvent] | Unsubscribe:
        """Triggered when a dialog is closed, either by user action, JS abort, or a command below."""

        return cast(
            Awaitable[DialogClosedEvent] | Unsubscribe,
            self._event(
                "dialogClosed",
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
    "AccountUrlType",
    "ClickDialogButtonParameters",
    "DialogButton",
    "DialogClosedEvent",
    "DialogShownEvent",
    "DialogType",
    "DismissDialogParameters",
    "EnableParameters",
    "FedCm",
    "LoginState",
    "OpenUrlParameters",
    "SelectAccountParameters",
]
