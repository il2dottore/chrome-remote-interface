"""Generated bindings for the CDP Security domain. Do not edit manually."""

from __future__ import annotations

from collections.abc import Awaitable, Mapping
from typing import TYPE_CHECKING, Literal, TypeAlias, cast, overload

from typing_extensions import NotRequired, TypedDict, Unpack

from cdp.domain import Domain as BaseDomain, EventCallback, Unsubscribe
from cdp.types import JsonObject

if TYPE_CHECKING:
    from . import network as Network


CertificateId: TypeAlias = int

MixedContentType: TypeAlias = Literal["blockable", "optionally-blockable", "none"]

SecurityState: TypeAlias = Literal[
    "unknown", "neutral", "insecure", "secure", "info", "insecure-broken"
]


class CertificateSecurityState(TypedDict):
    protocol: str
    keyExchange: str
    keyExchangeGroup: NotRequired[str]
    cipher: str
    mac: NotRequired[str]
    certificate: list[str]
    subjectName: str
    issuer: str
    validFrom: Network.TimeSinceEpoch
    validTo: Network.TimeSinceEpoch
    certificateNetworkError: NotRequired[str]
    certificateHasWeakSignature: bool
    certificateHasSha1Signature: bool
    modernSSL: bool
    obsoleteSslProtocol: bool
    obsoleteSslKeyExchange: bool
    obsoleteSslCipher: bool
    obsoleteSslSignature: bool


SafetyTipStatus: TypeAlias = Literal["badReputation", "lookalike"]


class SafetyTipInfo(TypedDict):
    safetyTipStatus: SafetyTipStatus
    safeUrl: NotRequired[str]


class VisibleSecurityState(TypedDict):
    securityState: SecurityState
    certificateSecurityState: NotRequired[CertificateSecurityState]
    safetyTipInfo: NotRequired[SafetyTipInfo]
    securityStateIssueIds: list[str]


class SecurityStateExplanation(TypedDict):
    securityState: SecurityState
    title: str
    summary: str
    description: str
    mixedContentType: MixedContentType
    certificate: list[str]
    recommendations: NotRequired[list[str]]


class InsecureContentStatus(TypedDict):
    ranMixedContent: bool
    displayedMixedContent: bool
    containedMixedForm: bool
    ranContentWithCertErrors: bool
    displayedContentWithCertErrors: bool
    ranInsecureContentStyle: SecurityState
    displayedInsecureContentStyle: SecurityState


CertificateErrorAction: TypeAlias = Literal["continue", "cancel"]


class SetIgnoreCertificateErrorsParameters(TypedDict):
    ignore: bool


class HandleCertificateErrorParameters(TypedDict):
    eventId: int
    action: CertificateErrorAction


class SetOverrideCertificateErrorsParameters(TypedDict):
    override: bool


class CertificateErrorEvent(TypedDict):
    eventId: int
    errorType: str
    requestURL: str


class VisibleSecurityStateChangedEvent(TypedDict):
    visibleSecurityState: VisibleSecurityState


class SecurityStateChangedEvent(TypedDict):
    securityState: SecurityState
    schemeIsCryptographic: bool
    explanations: list[SecurityStateExplanation]
    insecureContentStatus: InsecureContentStatus
    summary: NotRequired[str]


class Security(BaseDomain):
    """The CDP Security domain."""

    domain_name = "Security"

    async def disable(
        self,
        session_id: str | None = None,
    ) -> JsonObject:
        """Disables tracking security state changes."""

        return await self._command("disable", None, session_id, {})

    async def enable(
        self,
        session_id: str | None = None,
    ) -> JsonObject:
        """Enables tracking security state changes."""

        return await self._command("enable", None, session_id, {})

    @overload
    async def setIgnoreCertificateErrors(
        self,
        params: SetIgnoreCertificateErrorsParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def setIgnoreCertificateErrors(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetIgnoreCertificateErrorsParameters],
    ) -> JsonObject: ...

    async def setIgnoreCertificateErrors(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Enable/disable whether all certificate errors should be ignored."""

        return await self._command(
            "setIgnoreCertificateErrors", params, session_id, kwargs
        )

    @overload
    async def handleCertificateError(
        self,
        params: HandleCertificateErrorParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def handleCertificateError(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[HandleCertificateErrorParameters],
    ) -> JsonObject: ...

    async def handleCertificateError(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Handles a certificate error that fired a certificateError event."""

        return await self._command("handleCertificateError", params, session_id, kwargs)

    @overload
    async def setOverrideCertificateErrors(
        self,
        params: SetOverrideCertificateErrorsParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def setOverrideCertificateErrors(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetOverrideCertificateErrorsParameters],
    ) -> JsonObject: ...

    async def setOverrideCertificateErrors(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Enable/disable overriding certificate errors. If enabled, all certificate error events need to be handled by the DevTools client and should be answered with `handleCertificateError` commands."""

        return await self._command(
            "setOverrideCertificateErrors", params, session_id, kwargs
        )

    @overload
    def certificateError(
        self,
        callback_or_session: EventCallback[CertificateErrorEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def certificateError(
        self,
        callback_or_session: str,
        handler: EventCallback[CertificateErrorEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def certificateError(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[CertificateErrorEvent]: ...

    def certificateError(
        self,
        callback_or_session: EventCallback[CertificateErrorEvent] | str | None = None,
        handler: EventCallback[CertificateErrorEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[CertificateErrorEvent] | Unsubscribe:
        """There is a certificate error. If overriding certificate errors is enabled, then it should be handled with the `handleCertificateError` command. Note: this event does not fire if the certificate error has been allowed internally. Only one client per target should override certificate errors at the same time."""

        return cast(
            Awaitable[CertificateErrorEvent] | Unsubscribe,
            self._event(
                "certificateError",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def visibleSecurityStateChanged(
        self,
        callback_or_session: EventCallback[VisibleSecurityStateChangedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def visibleSecurityStateChanged(
        self,
        callback_or_session: str,
        handler: EventCallback[VisibleSecurityStateChangedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def visibleSecurityStateChanged(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[VisibleSecurityStateChangedEvent]: ...

    def visibleSecurityStateChanged(
        self,
        callback_or_session: EventCallback[VisibleSecurityStateChangedEvent]
        | str
        | None = None,
        handler: EventCallback[VisibleSecurityStateChangedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[VisibleSecurityStateChangedEvent] | Unsubscribe:
        """The security state of the page changed."""

        return cast(
            Awaitable[VisibleSecurityStateChangedEvent] | Unsubscribe,
            self._event(
                "visibleSecurityStateChanged",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def securityStateChanged(
        self,
        callback_or_session: EventCallback[SecurityStateChangedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def securityStateChanged(
        self,
        callback_or_session: str,
        handler: EventCallback[SecurityStateChangedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def securityStateChanged(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[SecurityStateChangedEvent]: ...

    def securityStateChanged(
        self,
        callback_or_session: EventCallback[SecurityStateChangedEvent]
        | str
        | None = None,
        handler: EventCallback[SecurityStateChangedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[SecurityStateChangedEvent] | Unsubscribe:
        """The security state of the page changed. No longer being sent."""

        return cast(
            Awaitable[SecurityStateChangedEvent] | Unsubscribe,
            self._event(
                "securityStateChanged",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )


__all__ = [
    "CertificateErrorAction",
    "CertificateErrorEvent",
    "CertificateId",
    "CertificateSecurityState",
    "HandleCertificateErrorParameters",
    "InsecureContentStatus",
    "MixedContentType",
    "SafetyTipInfo",
    "SafetyTipStatus",
    "Security",
    "SecurityState",
    "SecurityStateChangedEvent",
    "SecurityStateExplanation",
    "SetIgnoreCertificateErrorsParameters",
    "SetOverrideCertificateErrorsParameters",
    "VisibleSecurityState",
    "VisibleSecurityStateChangedEvent",
]
