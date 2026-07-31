"""Generated bindings for the CDP WebAuthn domain. Do not edit manually."""

from __future__ import annotations

from collections.abc import Awaitable, Mapping
from typing import Literal, TypeAlias, cast, overload

from typing_extensions import NotRequired, TypedDict, Unpack

from cdp.domain import Domain as BaseDomain, EventCallback, Unsubscribe
from cdp.types import JsonObject


AuthenticatorId: TypeAlias = str

AuthenticatorProtocol: TypeAlias = Literal["u2f", "ctap2"]

Ctap2Version: TypeAlias = Literal["ctap2_0", "ctap2_1", "ctap2_2"]

AuthenticatorTransport: TypeAlias = Literal["usb", "nfc", "ble", "cable", "internal"]


class VirtualAuthenticatorOptions(TypedDict):
    protocol: AuthenticatorProtocol
    ctap2Version: NotRequired[Ctap2Version]
    transport: AuthenticatorTransport
    hasResidentKey: NotRequired[bool]
    hasUserVerification: NotRequired[bool]
    hasLargeBlob: NotRequired[bool]
    hasCredBlob: NotRequired[bool]
    hasMinPinLength: NotRequired[bool]
    hasPrf: NotRequired[bool]
    hasHmacSecret: NotRequired[bool]
    hasHmacSecretMc: NotRequired[bool]
    hasCmtgKey: NotRequired[bool]
    automaticPresenceSimulation: NotRequired[bool]
    isUserVerified: NotRequired[bool]
    defaultBackupEligibility: NotRequired[bool]
    defaultBackupState: NotRequired[bool]


class Credential(TypedDict):
    credentialId: str
    isResidentCredential: bool
    rpId: NotRequired[str]
    privateKey: str
    userHandle: NotRequired[str]
    signCount: NotRequired[int]
    largeBlob: NotRequired[str]
    backupEligibility: NotRequired[bool]
    backupState: NotRequired[bool]
    userName: NotRequired[str]
    userDisplayName: NotRequired[str]
    cmtgKeys: NotRequired[list[str]]
    activeCmtgKeyIndex: NotRequired[int]
    generateCmtgKeyOnNextOperation: NotRequired[bool]


class EnableParameters(TypedDict):
    enableUI: NotRequired[bool]


class AddVirtualAuthenticatorParameters(TypedDict):
    options: VirtualAuthenticatorOptions


class AddVirtualAuthenticatorResult(TypedDict):
    authenticatorId: AuthenticatorId


class SetResponseOverrideBitsParameters(TypedDict):
    authenticatorId: AuthenticatorId
    isBogusSignature: NotRequired[bool]
    isBadUV: NotRequired[bool]
    isBadUP: NotRequired[bool]


class RemoveVirtualAuthenticatorParameters(TypedDict):
    authenticatorId: AuthenticatorId


class AddCredentialParameters(TypedDict):
    authenticatorId: AuthenticatorId
    credential: Credential


class GetCredentialParameters(TypedDict):
    authenticatorId: AuthenticatorId
    credentialId: str


class GetCredentialResult(TypedDict):
    credential: Credential


class GetCredentialsParameters(TypedDict):
    authenticatorId: AuthenticatorId


class GetCredentialsResult(TypedDict):
    credentials: list[Credential]


class RemoveCredentialParameters(TypedDict):
    authenticatorId: AuthenticatorId
    credentialId: str


class ClearCredentialsParameters(TypedDict):
    authenticatorId: AuthenticatorId


class SetUserVerifiedParameters(TypedDict):
    authenticatorId: AuthenticatorId
    isUserVerified: bool


class SetAutomaticPresenceSimulationParameters(TypedDict):
    authenticatorId: AuthenticatorId
    enabled: bool


class SetCredentialPropertiesParameters(TypedDict):
    authenticatorId: AuthenticatorId
    credentialId: str
    backupEligibility: NotRequired[bool]
    backupState: NotRequired[bool]
    activeCmtgKeyIndex: NotRequired[int]
    generateCmtgKeyOnNextOperation: NotRequired[bool]
    signCount: NotRequired[int]


class CredentialAddedEvent(TypedDict):
    authenticatorId: AuthenticatorId
    credential: Credential


class CredentialDeletedEvent(TypedDict):
    authenticatorId: AuthenticatorId
    credentialId: str


class CredentialUpdatedEvent(TypedDict):
    authenticatorId: AuthenticatorId
    credential: Credential


class CredentialAssertedEvent(TypedDict):
    authenticatorId: AuthenticatorId
    credential: Credential


class WebAuthn(BaseDomain):
    """This domain allows configuring virtual authenticators to test the WebAuthn API."""

    domain_name = "WebAuthn"

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
        """Enable the WebAuthn domain and start intercepting credential storage and retrieval with a virtual authenticator."""

        return await self._command("enable", params, session_id, kwargs)

    async def disable(
        self,
        session_id: str | None = None,
    ) -> JsonObject:
        """Disable the WebAuthn domain."""

        return await self._command("disable", None, session_id, {})

    @overload
    async def addVirtualAuthenticator(
        self,
        params: AddVirtualAuthenticatorParameters,
        session_id: str | None = None,
    ) -> AddVirtualAuthenticatorResult: ...

    @overload
    async def addVirtualAuthenticator(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[AddVirtualAuthenticatorParameters],
    ) -> AddVirtualAuthenticatorResult: ...

    async def addVirtualAuthenticator(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> AddVirtualAuthenticatorResult:
        """Creates and adds a virtual authenticator."""

        return cast(
            AddVirtualAuthenticatorResult,
            await self._command("addVirtualAuthenticator", params, session_id, kwargs),
        )

    @overload
    async def setResponseOverrideBits(
        self,
        params: SetResponseOverrideBitsParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def setResponseOverrideBits(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetResponseOverrideBitsParameters],
    ) -> JsonObject: ...

    async def setResponseOverrideBits(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Resets parameters isBogusSignature, isBadUV, isBadUP to false if they are not present."""

        return await self._command(
            "setResponseOverrideBits", params, session_id, kwargs
        )

    @overload
    async def removeVirtualAuthenticator(
        self,
        params: RemoveVirtualAuthenticatorParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def removeVirtualAuthenticator(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[RemoveVirtualAuthenticatorParameters],
    ) -> JsonObject: ...

    async def removeVirtualAuthenticator(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Removes the given authenticator."""

        return await self._command(
            "removeVirtualAuthenticator", params, session_id, kwargs
        )

    @overload
    async def addCredential(
        self,
        params: AddCredentialParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def addCredential(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[AddCredentialParameters],
    ) -> JsonObject: ...

    async def addCredential(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Adds the credential to the specified authenticator."""

        return await self._command("addCredential", params, session_id, kwargs)

    @overload
    async def getCredential(
        self,
        params: GetCredentialParameters,
        session_id: str | None = None,
    ) -> GetCredentialResult: ...

    @overload
    async def getCredential(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[GetCredentialParameters],
    ) -> GetCredentialResult: ...

    async def getCredential(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> GetCredentialResult:
        """Returns a single credential stored in the given virtual authenticator that matches the credential ID."""

        return cast(
            GetCredentialResult,
            await self._command("getCredential", params, session_id, kwargs),
        )

    @overload
    async def getCredentials(
        self,
        params: GetCredentialsParameters,
        session_id: str | None = None,
    ) -> GetCredentialsResult: ...

    @overload
    async def getCredentials(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[GetCredentialsParameters],
    ) -> GetCredentialsResult: ...

    async def getCredentials(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> GetCredentialsResult:
        """Returns all the credentials stored in the given virtual authenticator."""

        return cast(
            GetCredentialsResult,
            await self._command("getCredentials", params, session_id, kwargs),
        )

    @overload
    async def removeCredential(
        self,
        params: RemoveCredentialParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def removeCredential(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[RemoveCredentialParameters],
    ) -> JsonObject: ...

    async def removeCredential(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Removes a credential from the authenticator."""

        return await self._command("removeCredential", params, session_id, kwargs)

    @overload
    async def clearCredentials(
        self,
        params: ClearCredentialsParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def clearCredentials(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[ClearCredentialsParameters],
    ) -> JsonObject: ...

    async def clearCredentials(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Clears all the credentials from the specified device."""

        return await self._command("clearCredentials", params, session_id, kwargs)

    @overload
    async def setUserVerified(
        self,
        params: SetUserVerifiedParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def setUserVerified(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetUserVerifiedParameters],
    ) -> JsonObject: ...

    async def setUserVerified(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Sets whether User Verification succeeds or fails for an authenticator. The default is true."""

        return await self._command("setUserVerified", params, session_id, kwargs)

    @overload
    async def setAutomaticPresenceSimulation(
        self,
        params: SetAutomaticPresenceSimulationParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def setAutomaticPresenceSimulation(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetAutomaticPresenceSimulationParameters],
    ) -> JsonObject: ...

    async def setAutomaticPresenceSimulation(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Sets whether tests of user presence will succeed immediately (if true) or fail to resolve (if false) for an authenticator. The default is true."""

        return await self._command(
            "setAutomaticPresenceSimulation", params, session_id, kwargs
        )

    @overload
    async def setCredentialProperties(
        self,
        params: SetCredentialPropertiesParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def setCredentialProperties(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetCredentialPropertiesParameters],
    ) -> JsonObject: ...

    async def setCredentialProperties(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Allows setting credential properties. https://w3c.github.io/webauthn/#sctn-automation-set-credential-properties"""

        return await self._command(
            "setCredentialProperties", params, session_id, kwargs
        )

    @overload
    def credentialAdded(
        self,
        callback_or_session: EventCallback[CredentialAddedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def credentialAdded(
        self,
        callback_or_session: str,
        handler: EventCallback[CredentialAddedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def credentialAdded(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[CredentialAddedEvent]: ...

    def credentialAdded(
        self,
        callback_or_session: EventCallback[CredentialAddedEvent] | str | None = None,
        handler: EventCallback[CredentialAddedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[CredentialAddedEvent] | Unsubscribe:
        """Triggered when a credential is added to an authenticator."""

        return cast(
            Awaitable[CredentialAddedEvent] | Unsubscribe,
            self._event(
                "credentialAdded",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def credentialDeleted(
        self,
        callback_or_session: EventCallback[CredentialDeletedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def credentialDeleted(
        self,
        callback_or_session: str,
        handler: EventCallback[CredentialDeletedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def credentialDeleted(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[CredentialDeletedEvent]: ...

    def credentialDeleted(
        self,
        callback_or_session: EventCallback[CredentialDeletedEvent] | str | None = None,
        handler: EventCallback[CredentialDeletedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[CredentialDeletedEvent] | Unsubscribe:
        """Triggered when a credential is deleted, e.g. through PublicKeyCredential.signalUnknownCredential()."""

        return cast(
            Awaitable[CredentialDeletedEvent] | Unsubscribe,
            self._event(
                "credentialDeleted",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def credentialUpdated(
        self,
        callback_or_session: EventCallback[CredentialUpdatedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def credentialUpdated(
        self,
        callback_or_session: str,
        handler: EventCallback[CredentialUpdatedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def credentialUpdated(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[CredentialUpdatedEvent]: ...

    def credentialUpdated(
        self,
        callback_or_session: EventCallback[CredentialUpdatedEvent] | str | None = None,
        handler: EventCallback[CredentialUpdatedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[CredentialUpdatedEvent] | Unsubscribe:
        """Triggered when a credential is updated, e.g. through PublicKeyCredential.signalCurrentUserDetails()."""

        return cast(
            Awaitable[CredentialUpdatedEvent] | Unsubscribe,
            self._event(
                "credentialUpdated",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def credentialAsserted(
        self,
        callback_or_session: EventCallback[CredentialAssertedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def credentialAsserted(
        self,
        callback_or_session: str,
        handler: EventCallback[CredentialAssertedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def credentialAsserted(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[CredentialAssertedEvent]: ...

    def credentialAsserted(
        self,
        callback_or_session: EventCallback[CredentialAssertedEvent] | str | None = None,
        handler: EventCallback[CredentialAssertedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[CredentialAssertedEvent] | Unsubscribe:
        """Triggered when a credential is used in a webauthn assertion."""

        return cast(
            Awaitable[CredentialAssertedEvent] | Unsubscribe,
            self._event(
                "credentialAsserted",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )


__all__ = [
    "AddCredentialParameters",
    "AddVirtualAuthenticatorParameters",
    "AddVirtualAuthenticatorResult",
    "AuthenticatorId",
    "AuthenticatorProtocol",
    "AuthenticatorTransport",
    "ClearCredentialsParameters",
    "Credential",
    "CredentialAddedEvent",
    "CredentialAssertedEvent",
    "CredentialDeletedEvent",
    "CredentialUpdatedEvent",
    "Ctap2Version",
    "EnableParameters",
    "GetCredentialParameters",
    "GetCredentialResult",
    "GetCredentialsParameters",
    "GetCredentialsResult",
    "RemoveCredentialParameters",
    "RemoveVirtualAuthenticatorParameters",
    "SetAutomaticPresenceSimulationParameters",
    "SetCredentialPropertiesParameters",
    "SetResponseOverrideBitsParameters",
    "SetUserVerifiedParameters",
    "VirtualAuthenticatorOptions",
    "WebAuthn",
]
