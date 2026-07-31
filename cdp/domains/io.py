"""Generated bindings for the CDP IO domain. Do not edit manually."""

from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, TypeAlias, cast, overload

from typing_extensions import NotRequired, TypedDict, Unpack

from cdp.domain import Domain as BaseDomain
from cdp.types import JsonObject

if TYPE_CHECKING:
    from . import runtime as Runtime


StreamHandle: TypeAlias = str


class CloseParameters(TypedDict):
    handle: StreamHandle


class ReadParameters(TypedDict):
    handle: StreamHandle
    offset: NotRequired[int]
    size: NotRequired[int]


class ReadResult(TypedDict):
    base64Encoded: NotRequired[bool]
    data: str
    eof: bool


class ResolveBlobParameters(TypedDict):
    objectId: Runtime.RemoteObjectId


class ResolveBlobResult(TypedDict):
    uuid: str


class IO(BaseDomain):
    """Input/Output operations for streams produced by DevTools."""

    domain_name = "IO"

    @overload
    async def close(
        self,
        params: CloseParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def close(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[CloseParameters],
    ) -> JsonObject: ...

    async def close(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Close the stream, discard any temporary backing storage."""

        return await self._command("close", params, session_id, kwargs)

    @overload
    async def read(
        self,
        params: ReadParameters,
        session_id: str | None = None,
    ) -> ReadResult: ...

    @overload
    async def read(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[ReadParameters],
    ) -> ReadResult: ...

    async def read(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> ReadResult:
        """Read a chunk of the stream"""

        return cast(ReadResult, await self._command("read", params, session_id, kwargs))

    @overload
    async def resolveBlob(
        self,
        params: ResolveBlobParameters,
        session_id: str | None = None,
    ) -> ResolveBlobResult: ...

    @overload
    async def resolveBlob(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[ResolveBlobParameters],
    ) -> ResolveBlobResult: ...

    async def resolveBlob(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> ResolveBlobResult:
        """Return UUID of Blob object specified by a remote object id."""

        return cast(
            ResolveBlobResult,
            await self._command("resolveBlob", params, session_id, kwargs),
        )


__all__ = [
    "IO",
    "CloseParameters",
    "ReadParameters",
    "ReadResult",
    "ResolveBlobParameters",
    "ResolveBlobResult",
    "StreamHandle",
]
