"""Generated bindings for the CDP SmartCardEmulation domain. Do not edit manually."""

from __future__ import annotations

from collections.abc import Awaitable, Mapping
from typing import Literal, TypeAlias, cast, overload

from typing_extensions import NotRequired, TypedDict, Unpack

from cdp.domain import Domain as BaseDomain, EventCallback, Unsubscribe
from cdp.types import JsonObject


ResultCode: TypeAlias = Literal[
    "success",
    "removed-card",
    "reset-card",
    "unpowered-card",
    "unresponsive-card",
    "unsupported-card",
    "reader-unavailable",
    "sharing-violation",
    "not-transacted",
    "no-smartcard",
    "proto-mismatch",
    "system-cancelled",
    "not-ready",
    "cancelled",
    "insufficient-buffer",
    "invalid-handle",
    "invalid-parameter",
    "invalid-value",
    "no-memory",
    "timeout",
    "unknown-reader",
    "unsupported-feature",
    "no-readers-available",
    "service-stopped",
    "no-service",
    "comm-error",
    "internal-error",
    "server-too-busy",
    "unexpected",
    "shutdown",
    "unknown-card",
    "unknown",
]

ShareMode: TypeAlias = Literal["shared", "exclusive", "direct"]

Disposition: TypeAlias = Literal[
    "leave-card", "reset-card", "unpower-card", "eject-card"
]

ConnectionState: TypeAlias = Literal[
    "absent", "present", "swallowed", "powered", "negotiable", "specific"
]


class ReaderStateFlags(TypedDict):
    unaware: NotRequired[bool]
    ignore: NotRequired[bool]
    changed: NotRequired[bool]
    unknown: NotRequired[bool]
    unavailable: NotRequired[bool]
    empty: NotRequired[bool]
    present: NotRequired[bool]
    exclusive: NotRequired[bool]
    inuse: NotRequired[bool]
    mute: NotRequired[bool]
    unpowered: NotRequired[bool]


class ProtocolSet(TypedDict):
    t0: NotRequired[bool]
    t1: NotRequired[bool]
    raw: NotRequired[bool]


Protocol: TypeAlias = Literal["t0", "t1", "raw"]


class ReaderStateIn(TypedDict):
    reader: str
    currentState: ReaderStateFlags
    currentInsertionCount: int


class ReaderStateOut(TypedDict):
    reader: str
    eventState: ReaderStateFlags
    eventCount: int
    atr: str


class ReportEstablishContextResultParameters(TypedDict):
    requestId: str
    contextId: int


class ReportReleaseContextResultParameters(TypedDict):
    requestId: str


class ReportListReadersResultParameters(TypedDict):
    requestId: str
    readers: list[str]


class ReportGetStatusChangeResultParameters(TypedDict):
    requestId: str
    readerStates: list[ReaderStateOut]


class ReportBeginTransactionResultParameters(TypedDict):
    requestId: str
    handle: int


class ReportPlainResultParameters(TypedDict):
    requestId: str


class ReportConnectResultParameters(TypedDict):
    requestId: str
    handle: int
    activeProtocol: NotRequired[Protocol]


class ReportDataResultParameters(TypedDict):
    requestId: str
    data: str


class ReportStatusResultParameters(TypedDict):
    requestId: str
    readerName: str
    state: ConnectionState
    atr: str
    protocol: NotRequired[Protocol]


class ReportErrorParameters(TypedDict):
    requestId: str
    resultCode: ResultCode


class EstablishContextRequestedEvent(TypedDict):
    requestId: str


class ReleaseContextRequestedEvent(TypedDict):
    requestId: str
    contextId: int


class ListReadersRequestedEvent(TypedDict):
    requestId: str
    contextId: int


class GetStatusChangeRequestedEvent(TypedDict):
    requestId: str
    contextId: int
    readerStates: list[ReaderStateIn]
    timeout: NotRequired[int]


class CancelRequestedEvent(TypedDict):
    requestId: str
    contextId: int


class ConnectRequestedEvent(TypedDict):
    requestId: str
    contextId: int
    reader: str
    shareMode: ShareMode
    preferredProtocols: ProtocolSet


class DisconnectRequestedEvent(TypedDict):
    requestId: str
    handle: int
    disposition: Disposition


class TransmitRequestedEvent(TypedDict):
    requestId: str
    handle: int
    data: str
    protocol: NotRequired[Protocol]


class ControlRequestedEvent(TypedDict):
    requestId: str
    handle: int
    controlCode: int
    data: str


class GetAttribRequestedEvent(TypedDict):
    requestId: str
    handle: int
    attribId: int


class SetAttribRequestedEvent(TypedDict):
    requestId: str
    handle: int
    attribId: int
    data: str


class StatusRequestedEvent(TypedDict):
    requestId: str
    handle: int


class BeginTransactionRequestedEvent(TypedDict):
    requestId: str
    handle: int


class EndTransactionRequestedEvent(TypedDict):
    requestId: str
    handle: int
    disposition: Disposition


class SmartCardEmulation(BaseDomain):
    """The CDP SmartCardEmulation domain."""

    domain_name = "SmartCardEmulation"

    async def enable(
        self,
        session_id: str | None = None,
    ) -> JsonObject:
        """Enables the |SmartCardEmulation| domain."""

        return await self._command("enable", None, session_id, {})

    async def disable(
        self,
        session_id: str | None = None,
    ) -> JsonObject:
        """Disables the |SmartCardEmulation| domain."""

        return await self._command("disable", None, session_id, {})

    @overload
    async def reportEstablishContextResult(
        self,
        params: ReportEstablishContextResultParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def reportEstablishContextResult(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[ReportEstablishContextResultParameters],
    ) -> JsonObject: ...

    async def reportEstablishContextResult(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Reports the successful result of a |SCardEstablishContext| call. This maps to: PC/SC Lite: https://pcsclite.apdu.fr/api/group__API.html#gaa1b8970169fd4883a6dc4a8f43f19b67 Microsoft: https://learn.microsoft.com/en-us/windows/win32/api/winscard/nf-winscard-scardestablishcontext"""

        return await self._command(
            "reportEstablishContextResult", params, session_id, kwargs
        )

    @overload
    async def reportReleaseContextResult(
        self,
        params: ReportReleaseContextResultParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def reportReleaseContextResult(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[ReportReleaseContextResultParameters],
    ) -> JsonObject: ...

    async def reportReleaseContextResult(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Reports the successful result of a |SCardReleaseContext| call. This maps to: PC/SC Lite: https://pcsclite.apdu.fr/api/group__API.html#ga6aabcba7744c5c9419fdd6404f73a934 Microsoft: https://learn.microsoft.com/en-us/windows/win32/api/winscard/nf-winscard-scardreleasecontext"""

        return await self._command(
            "reportReleaseContextResult", params, session_id, kwargs
        )

    @overload
    async def reportListReadersResult(
        self,
        params: ReportListReadersResultParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def reportListReadersResult(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[ReportListReadersResultParameters],
    ) -> JsonObject: ...

    async def reportListReadersResult(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Reports the successful result of a |SCardListReaders| call. This maps to: PC/SC Lite: https://pcsclite.apdu.fr/api/group__API.html#ga93b07815789b3cf2629d439ecf20f0d9 Microsoft: https://learn.microsoft.com/en-us/windows/win32/api/winscard/nf-winscard-scardlistreadersa"""

        return await self._command(
            "reportListReadersResult", params, session_id, kwargs
        )

    @overload
    async def reportGetStatusChangeResult(
        self,
        params: ReportGetStatusChangeResultParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def reportGetStatusChangeResult(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[ReportGetStatusChangeResultParameters],
    ) -> JsonObject: ...

    async def reportGetStatusChangeResult(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Reports the successful result of a |SCardGetStatusChange| call. This maps to: PC/SC Lite: https://pcsclite.apdu.fr/api/group__API.html#ga33247d5d1257d59e55647c3bb717db24 Microsoft: https://learn.microsoft.com/en-us/windows/win32/api/winscard/nf-winscard-scardgetstatuschangea"""

        return await self._command(
            "reportGetStatusChangeResult", params, session_id, kwargs
        )

    @overload
    async def reportBeginTransactionResult(
        self,
        params: ReportBeginTransactionResultParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def reportBeginTransactionResult(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[ReportBeginTransactionResultParameters],
    ) -> JsonObject: ...

    async def reportBeginTransactionResult(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Reports the result of a |SCardBeginTransaction| call. On success, this creates a new transaction object. This maps to: PC/SC Lite: https://pcsclite.apdu.fr/api/group__API.html#gaddb835dce01a0da1d6ca02d33ee7d861 Microsoft: https://learn.microsoft.com/en-us/windows/win32/api/winscard/nf-winscard-scardbegintransaction"""

        return await self._command(
            "reportBeginTransactionResult", params, session_id, kwargs
        )

    @overload
    async def reportPlainResult(
        self,
        params: ReportPlainResultParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def reportPlainResult(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[ReportPlainResultParameters],
    ) -> JsonObject: ...

    async def reportPlainResult(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Reports the successful result of a call that returns only a result code. Used for: |SCardCancel|, |SCardDisconnect|, |SCardSetAttrib|, |SCardEndTransaction|. This maps to: 1. SCardCancel PC/SC Lite: https://pcsclite.apdu.fr/api/group__API.html#gaacbbc0c6d6c0cbbeb4f4debf6fbeeee6 Microsoft: https://learn.microsoft.com/en-us/windows/win32/api/winscard/nf-winscard-scardcancel 2. SCardDisconnect PC/SC Lite: https://pcsclite.apdu.fr/api/group__API.html#ga4be198045c73ec0deb79e66c0ca1738a Microsoft: https://learn.microsoft.com/en-us/windows/win32/api/winscard/nf-winscard-scarddisconnect 3. SCardSetAttrib PC/SC Lite: https://pcsclite.apdu.fr/api/group__API.html#ga060f0038a4ddfd5dd2b8fadf3c3a2e4f Microsoft: https://learn.microsoft.com/en-us/windows/win32/api/winscard/nf-winscard-scardsetattrib 4. SCardEndTransaction PC/SC Lite: https://pcsclite.apdu.fr/api/group__API.html#gae8742473b404363e5c587f570d7e2f3b Microsoft: https://learn.microsoft.com/en-us/windows/win32/api/winscard/nf-winscard-scardendtransaction"""

        return await self._command("reportPlainResult", params, session_id, kwargs)

    @overload
    async def reportConnectResult(
        self,
        params: ReportConnectResultParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def reportConnectResult(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[ReportConnectResultParameters],
    ) -> JsonObject: ...

    async def reportConnectResult(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Reports the successful result of a |SCardConnect| call. This maps to: PC/SC Lite: https://pcsclite.apdu.fr/api/group__API.html#ga4e515829752e0a8dbc4d630696a8d6a5 Microsoft: https://learn.microsoft.com/en-us/windows/win32/api/winscard/nf-winscard-scardconnecta"""

        return await self._command("reportConnectResult", params, session_id, kwargs)

    @overload
    async def reportDataResult(
        self,
        params: ReportDataResultParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def reportDataResult(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[ReportDataResultParameters],
    ) -> JsonObject: ...

    async def reportDataResult(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Reports the successful result of a call that sends back data on success. Used for |SCardTransmit|, |SCardControl|, and |SCardGetAttrib|. This maps to: 1. SCardTransmit PC/SC Lite: https://pcsclite.apdu.fr/api/group__API.html#ga9a2d77242a271310269065e64633ab99 Microsoft: https://learn.microsoft.com/en-us/windows/win32/api/winscard/nf-winscard-scardtransmit 2. SCardControl PC/SC Lite: https://pcsclite.apdu.fr/api/group__API.html#gac3454d4657110fd7f753b2d3d8f4e32f Microsoft: https://learn.microsoft.com/en-us/windows/win32/api/winscard/nf-winscard-scardcontrol 3. SCardGetAttrib PC/SC Lite: https://pcsclite.apdu.fr/api/group__API.html#gaacfec51917255b7a25b94c5104961602 Microsoft: https://learn.microsoft.com/en-us/windows/win32/api/winscard/nf-winscard-scardgetattrib"""

        return await self._command("reportDataResult", params, session_id, kwargs)

    @overload
    async def reportStatusResult(
        self,
        params: ReportStatusResultParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def reportStatusResult(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[ReportStatusResultParameters],
    ) -> JsonObject: ...

    async def reportStatusResult(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Reports the successful result of a |SCardStatus| call. This maps to: PC/SC Lite: https://pcsclite.apdu.fr/api/group__API.html#gae49c3c894ad7ac12a5b896bde70d0382 Microsoft: https://learn.microsoft.com/en-us/windows/win32/api/winscard/nf-winscard-scardstatusa"""

        return await self._command("reportStatusResult", params, session_id, kwargs)

    @overload
    async def reportError(
        self,
        params: ReportErrorParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def reportError(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[ReportErrorParameters],
    ) -> JsonObject: ...

    async def reportError(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Reports an error result for the given request."""

        return await self._command("reportError", params, session_id, kwargs)

    @overload
    def establishContextRequested(
        self,
        callback_or_session: EventCallback[EstablishContextRequestedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def establishContextRequested(
        self,
        callback_or_session: str,
        handler: EventCallback[EstablishContextRequestedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def establishContextRequested(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[EstablishContextRequestedEvent]: ...

    def establishContextRequested(
        self,
        callback_or_session: EventCallback[EstablishContextRequestedEvent]
        | str
        | None = None,
        handler: EventCallback[EstablishContextRequestedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[EstablishContextRequestedEvent] | Unsubscribe:
        """Fired when |SCardEstablishContext| is called. This maps to: PC/SC Lite: https://pcsclite.apdu.fr/api/group__API.html#gaa1b8970169fd4883a6dc4a8f43f19b67 Microsoft: https://learn.microsoft.com/en-us/windows/win32/api/winscard/nf-winscard-scardestablishcontext"""

        return cast(
            Awaitable[EstablishContextRequestedEvent] | Unsubscribe,
            self._event(
                "establishContextRequested",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def releaseContextRequested(
        self,
        callback_or_session: EventCallback[ReleaseContextRequestedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def releaseContextRequested(
        self,
        callback_or_session: str,
        handler: EventCallback[ReleaseContextRequestedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def releaseContextRequested(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[ReleaseContextRequestedEvent]: ...

    def releaseContextRequested(
        self,
        callback_or_session: EventCallback[ReleaseContextRequestedEvent]
        | str
        | None = None,
        handler: EventCallback[ReleaseContextRequestedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[ReleaseContextRequestedEvent] | Unsubscribe:
        """Fired when |SCardReleaseContext| is called. This maps to: PC/SC Lite: https://pcsclite.apdu.fr/api/group__API.html#ga6aabcba7744c5c9419fdd6404f73a934 Microsoft: https://learn.microsoft.com/en-us/windows/win32/api/winscard/nf-winscard-scardreleasecontext"""

        return cast(
            Awaitable[ReleaseContextRequestedEvent] | Unsubscribe,
            self._event(
                "releaseContextRequested",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def listReadersRequested(
        self,
        callback_or_session: EventCallback[ListReadersRequestedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def listReadersRequested(
        self,
        callback_or_session: str,
        handler: EventCallback[ListReadersRequestedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def listReadersRequested(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[ListReadersRequestedEvent]: ...

    def listReadersRequested(
        self,
        callback_or_session: EventCallback[ListReadersRequestedEvent]
        | str
        | None = None,
        handler: EventCallback[ListReadersRequestedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[ListReadersRequestedEvent] | Unsubscribe:
        """Fired when |SCardListReaders| is called. This maps to: PC/SC Lite: https://pcsclite.apdu.fr/api/group__API.html#ga93b07815789b3cf2629d439ecf20f0d9 Microsoft: https://learn.microsoft.com/en-us/windows/win32/api/winscard/nf-winscard-scardlistreadersa"""

        return cast(
            Awaitable[ListReadersRequestedEvent] | Unsubscribe,
            self._event(
                "listReadersRequested",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def getStatusChangeRequested(
        self,
        callback_or_session: EventCallback[GetStatusChangeRequestedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def getStatusChangeRequested(
        self,
        callback_or_session: str,
        handler: EventCallback[GetStatusChangeRequestedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def getStatusChangeRequested(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[GetStatusChangeRequestedEvent]: ...

    def getStatusChangeRequested(
        self,
        callback_or_session: EventCallback[GetStatusChangeRequestedEvent]
        | str
        | None = None,
        handler: EventCallback[GetStatusChangeRequestedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[GetStatusChangeRequestedEvent] | Unsubscribe:
        """Fired when |SCardGetStatusChange| is called. Timeout is specified in milliseconds. This maps to: PC/SC Lite: https://pcsclite.apdu.fr/api/group__API.html#ga33247d5d1257d59e55647c3bb717db24 Microsoft: https://learn.microsoft.com/en-us/windows/win32/api/winscard/nf-winscard-scardgetstatuschangea"""

        return cast(
            Awaitable[GetStatusChangeRequestedEvent] | Unsubscribe,
            self._event(
                "getStatusChangeRequested",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def cancelRequested(
        self,
        callback_or_session: EventCallback[CancelRequestedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def cancelRequested(
        self,
        callback_or_session: str,
        handler: EventCallback[CancelRequestedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def cancelRequested(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[CancelRequestedEvent]: ...

    def cancelRequested(
        self,
        callback_or_session: EventCallback[CancelRequestedEvent] | str | None = None,
        handler: EventCallback[CancelRequestedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[CancelRequestedEvent] | Unsubscribe:
        """Fired when |SCardCancel| is called. This maps to: PC/SC Lite: https://pcsclite.apdu.fr/api/group__API.html#gaacbbc0c6d6c0cbbeb4f4debf6fbeeee6 Microsoft: https://learn.microsoft.com/en-us/windows/win32/api/winscard/nf-winscard-scardcancel"""

        return cast(
            Awaitable[CancelRequestedEvent] | Unsubscribe,
            self._event(
                "cancelRequested",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def connectRequested(
        self,
        callback_or_session: EventCallback[ConnectRequestedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def connectRequested(
        self,
        callback_or_session: str,
        handler: EventCallback[ConnectRequestedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def connectRequested(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[ConnectRequestedEvent]: ...

    def connectRequested(
        self,
        callback_or_session: EventCallback[ConnectRequestedEvent] | str | None = None,
        handler: EventCallback[ConnectRequestedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[ConnectRequestedEvent] | Unsubscribe:
        """Fired when |SCardConnect| is called. This maps to: PC/SC Lite: https://pcsclite.apdu.fr/api/group__API.html#ga4e515829752e0a8dbc4d630696a8d6a5 Microsoft: https://learn.microsoft.com/en-us/windows/win32/api/winscard/nf-winscard-scardconnecta"""

        return cast(
            Awaitable[ConnectRequestedEvent] | Unsubscribe,
            self._event(
                "connectRequested",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def disconnectRequested(
        self,
        callback_or_session: EventCallback[DisconnectRequestedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def disconnectRequested(
        self,
        callback_or_session: str,
        handler: EventCallback[DisconnectRequestedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def disconnectRequested(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[DisconnectRequestedEvent]: ...

    def disconnectRequested(
        self,
        callback_or_session: EventCallback[DisconnectRequestedEvent]
        | str
        | None = None,
        handler: EventCallback[DisconnectRequestedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[DisconnectRequestedEvent] | Unsubscribe:
        """Fired when |SCardDisconnect| is called. This maps to: PC/SC Lite: https://pcsclite.apdu.fr/api/group__API.html#ga4be198045c73ec0deb79e66c0ca1738a Microsoft: https://learn.microsoft.com/en-us/windows/win32/api/winscard/nf-winscard-scarddisconnect"""

        return cast(
            Awaitable[DisconnectRequestedEvent] | Unsubscribe,
            self._event(
                "disconnectRequested",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def transmitRequested(
        self,
        callback_or_session: EventCallback[TransmitRequestedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def transmitRequested(
        self,
        callback_or_session: str,
        handler: EventCallback[TransmitRequestedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def transmitRequested(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[TransmitRequestedEvent]: ...

    def transmitRequested(
        self,
        callback_or_session: EventCallback[TransmitRequestedEvent] | str | None = None,
        handler: EventCallback[TransmitRequestedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[TransmitRequestedEvent] | Unsubscribe:
        """Fired when |SCardTransmit| is called. This maps to: PC/SC Lite: https://pcsclite.apdu.fr/api/group__API.html#ga9a2d77242a271310269065e64633ab99 Microsoft: https://learn.microsoft.com/en-us/windows/win32/api/winscard/nf-winscard-scardtransmit"""

        return cast(
            Awaitable[TransmitRequestedEvent] | Unsubscribe,
            self._event(
                "transmitRequested",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def controlRequested(
        self,
        callback_or_session: EventCallback[ControlRequestedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def controlRequested(
        self,
        callback_or_session: str,
        handler: EventCallback[ControlRequestedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def controlRequested(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[ControlRequestedEvent]: ...

    def controlRequested(
        self,
        callback_or_session: EventCallback[ControlRequestedEvent] | str | None = None,
        handler: EventCallback[ControlRequestedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[ControlRequestedEvent] | Unsubscribe:
        """Fired when |SCardControl| is called. This maps to: PC/SC Lite: https://pcsclite.apdu.fr/api/group__API.html#gac3454d4657110fd7f753b2d3d8f4e32f Microsoft: https://learn.microsoft.com/en-us/windows/win32/api/winscard/nf-winscard-scardcontrol"""

        return cast(
            Awaitable[ControlRequestedEvent] | Unsubscribe,
            self._event(
                "controlRequested",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def getAttribRequested(
        self,
        callback_or_session: EventCallback[GetAttribRequestedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def getAttribRequested(
        self,
        callback_or_session: str,
        handler: EventCallback[GetAttribRequestedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def getAttribRequested(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[GetAttribRequestedEvent]: ...

    def getAttribRequested(
        self,
        callback_or_session: EventCallback[GetAttribRequestedEvent] | str | None = None,
        handler: EventCallback[GetAttribRequestedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[GetAttribRequestedEvent] | Unsubscribe:
        """Fired when |SCardGetAttrib| is called. This maps to: PC/SC Lite: https://pcsclite.apdu.fr/api/group__API.html#gaacfec51917255b7a25b94c5104961602 Microsoft: https://learn.microsoft.com/en-us/windows/win32/api/winscard/nf-winscard-scardgetattrib"""

        return cast(
            Awaitable[GetAttribRequestedEvent] | Unsubscribe,
            self._event(
                "getAttribRequested",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def setAttribRequested(
        self,
        callback_or_session: EventCallback[SetAttribRequestedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def setAttribRequested(
        self,
        callback_or_session: str,
        handler: EventCallback[SetAttribRequestedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def setAttribRequested(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[SetAttribRequestedEvent]: ...

    def setAttribRequested(
        self,
        callback_or_session: EventCallback[SetAttribRequestedEvent] | str | None = None,
        handler: EventCallback[SetAttribRequestedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[SetAttribRequestedEvent] | Unsubscribe:
        """Fired when |SCardSetAttrib| is called. This maps to: PC/SC Lite: https://pcsclite.apdu.fr/api/group__API.html#ga060f0038a4ddfd5dd2b8fadf3c3a2e4f Microsoft: https://learn.microsoft.com/en-us/windows/win32/api/winscard/nf-winscard-scardsetattrib"""

        return cast(
            Awaitable[SetAttribRequestedEvent] | Unsubscribe,
            self._event(
                "setAttribRequested",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def statusRequested(
        self,
        callback_or_session: EventCallback[StatusRequestedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def statusRequested(
        self,
        callback_or_session: str,
        handler: EventCallback[StatusRequestedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def statusRequested(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[StatusRequestedEvent]: ...

    def statusRequested(
        self,
        callback_or_session: EventCallback[StatusRequestedEvent] | str | None = None,
        handler: EventCallback[StatusRequestedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[StatusRequestedEvent] | Unsubscribe:
        """Fired when |SCardStatus| is called. This maps to: PC/SC Lite: https://pcsclite.apdu.fr/api/group__API.html#gae49c3c894ad7ac12a5b896bde70d0382 Microsoft: https://learn.microsoft.com/en-us/windows/win32/api/winscard/nf-winscard-scardstatusa"""

        return cast(
            Awaitable[StatusRequestedEvent] | Unsubscribe,
            self._event(
                "statusRequested",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def beginTransactionRequested(
        self,
        callback_or_session: EventCallback[BeginTransactionRequestedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def beginTransactionRequested(
        self,
        callback_or_session: str,
        handler: EventCallback[BeginTransactionRequestedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def beginTransactionRequested(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[BeginTransactionRequestedEvent]: ...

    def beginTransactionRequested(
        self,
        callback_or_session: EventCallback[BeginTransactionRequestedEvent]
        | str
        | None = None,
        handler: EventCallback[BeginTransactionRequestedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[BeginTransactionRequestedEvent] | Unsubscribe:
        """Fired when |SCardBeginTransaction| is called. This maps to: PC/SC Lite: https://pcsclite.apdu.fr/api/group__API.html#gaddb835dce01a0da1d6ca02d33ee7d861 Microsoft: https://learn.microsoft.com/en-us/windows/win32/api/winscard/nf-winscard-scardbegintransaction"""

        return cast(
            Awaitable[BeginTransactionRequestedEvent] | Unsubscribe,
            self._event(
                "beginTransactionRequested",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def endTransactionRequested(
        self,
        callback_or_session: EventCallback[EndTransactionRequestedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def endTransactionRequested(
        self,
        callback_or_session: str,
        handler: EventCallback[EndTransactionRequestedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def endTransactionRequested(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[EndTransactionRequestedEvent]: ...

    def endTransactionRequested(
        self,
        callback_or_session: EventCallback[EndTransactionRequestedEvent]
        | str
        | None = None,
        handler: EventCallback[EndTransactionRequestedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[EndTransactionRequestedEvent] | Unsubscribe:
        """Fired when |SCardEndTransaction| is called. This maps to: PC/SC Lite: https://pcsclite.apdu.fr/api/group__API.html#gae8742473b404363e5c587f570d7e2f3b Microsoft: https://learn.microsoft.com/en-us/windows/win32/api/winscard/nf-winscard-scardendtransaction"""

        return cast(
            Awaitable[EndTransactionRequestedEvent] | Unsubscribe,
            self._event(
                "endTransactionRequested",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )


__all__ = [
    "BeginTransactionRequestedEvent",
    "CancelRequestedEvent",
    "ConnectRequestedEvent",
    "ConnectionState",
    "ControlRequestedEvent",
    "DisconnectRequestedEvent",
    "Disposition",
    "EndTransactionRequestedEvent",
    "EstablishContextRequestedEvent",
    "GetAttribRequestedEvent",
    "GetStatusChangeRequestedEvent",
    "ListReadersRequestedEvent",
    "Protocol",
    "ProtocolSet",
    "ReaderStateFlags",
    "ReaderStateIn",
    "ReaderStateOut",
    "ReleaseContextRequestedEvent",
    "ReportBeginTransactionResultParameters",
    "ReportConnectResultParameters",
    "ReportDataResultParameters",
    "ReportErrorParameters",
    "ReportEstablishContextResultParameters",
    "ReportGetStatusChangeResultParameters",
    "ReportListReadersResultParameters",
    "ReportPlainResultParameters",
    "ReportReleaseContextResultParameters",
    "ReportStatusResultParameters",
    "ResultCode",
    "SetAttribRequestedEvent",
    "ShareMode",
    "SmartCardEmulation",
    "StatusRequestedEvent",
    "TransmitRequestedEvent",
]
