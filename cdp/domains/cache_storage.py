"""Generated bindings for the CDP CacheStorage domain. Do not edit manually."""

from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Literal, TypeAlias, cast, overload

from typing_extensions import NotRequired, TypedDict, Unpack

from cdp.domain import Domain as BaseDomain
from cdp.types import JsonObject

if TYPE_CHECKING:
    from . import storage as Storage


CacheId: TypeAlias = str

CachedResponseType: TypeAlias = Literal[
    "basic", "cors", "default", "error", "opaqueResponse", "opaqueRedirect"
]


class DataEntry(TypedDict):
    requestURL: str
    requestMethod: str
    requestHeaders: list[Header]
    responseTime: float
    responseStatus: int
    responseStatusText: str
    responseType: CachedResponseType
    responseHeaders: list[Header]


class Cache(TypedDict):
    cacheId: CacheId
    securityOrigin: str
    storageKey: str
    storageBucket: NotRequired[Storage.StorageBucket]
    cacheName: str


class Header(TypedDict):
    name: str
    value: str


class CachedResponse(TypedDict):
    body: str


class DeleteCacheParameters(TypedDict):
    cacheId: CacheId


class DeleteEntryParameters(TypedDict):
    cacheId: CacheId
    request: str


class RequestCacheNamesParameters(TypedDict):
    securityOrigin: NotRequired[str]
    storageKey: NotRequired[str]
    storageBucket: NotRequired[Storage.StorageBucket]


class RequestCacheNamesResult(TypedDict):
    caches: list[Cache]


class RequestCachedResponseParameters(TypedDict):
    cacheId: CacheId
    requestURL: str
    requestHeaders: list[Header]


class RequestCachedResponseResult(TypedDict):
    response: CachedResponse


class RequestEntriesParameters(TypedDict):
    cacheId: CacheId
    skipCount: NotRequired[int]
    pageSize: NotRequired[int]
    pathFilter: NotRequired[str]


class RequestEntriesResult(TypedDict):
    cacheDataEntries: list[DataEntry]
    returnCount: float


class CacheStorage(BaseDomain):
    """The CDP CacheStorage domain."""

    domain_name = "CacheStorage"

    @overload
    async def deleteCache(
        self,
        params: DeleteCacheParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def deleteCache(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[DeleteCacheParameters],
    ) -> JsonObject: ...

    async def deleteCache(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Deletes a cache."""

        return await self._command("deleteCache", params, session_id, kwargs)

    @overload
    async def deleteEntry(
        self,
        params: DeleteEntryParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def deleteEntry(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[DeleteEntryParameters],
    ) -> JsonObject: ...

    async def deleteEntry(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Deletes a cache entry."""

        return await self._command("deleteEntry", params, session_id, kwargs)

    @overload
    async def requestCacheNames(
        self,
        params: RequestCacheNamesParameters,
        session_id: str | None = None,
    ) -> RequestCacheNamesResult: ...

    @overload
    async def requestCacheNames(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[RequestCacheNamesParameters],
    ) -> RequestCacheNamesResult: ...

    async def requestCacheNames(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> RequestCacheNamesResult:
        """Requests cache names."""

        return cast(
            RequestCacheNamesResult,
            await self._command("requestCacheNames", params, session_id, kwargs),
        )

    @overload
    async def requestCachedResponse(
        self,
        params: RequestCachedResponseParameters,
        session_id: str | None = None,
    ) -> RequestCachedResponseResult: ...

    @overload
    async def requestCachedResponse(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[RequestCachedResponseParameters],
    ) -> RequestCachedResponseResult: ...

    async def requestCachedResponse(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> RequestCachedResponseResult:
        """Fetches cache entry."""

        return cast(
            RequestCachedResponseResult,
            await self._command("requestCachedResponse", params, session_id, kwargs),
        )

    @overload
    async def requestEntries(
        self,
        params: RequestEntriesParameters,
        session_id: str | None = None,
    ) -> RequestEntriesResult: ...

    @overload
    async def requestEntries(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[RequestEntriesParameters],
    ) -> RequestEntriesResult: ...

    async def requestEntries(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> RequestEntriesResult:
        """Requests data from cache."""

        return cast(
            RequestEntriesResult,
            await self._command("requestEntries", params, session_id, kwargs),
        )


__all__ = [
    "Cache",
    "CacheId",
    "CacheStorage",
    "CachedResponse",
    "CachedResponseType",
    "DataEntry",
    "DeleteCacheParameters",
    "DeleteEntryParameters",
    "Header",
    "RequestCacheNamesParameters",
    "RequestCacheNamesResult",
    "RequestCachedResponseParameters",
    "RequestCachedResponseResult",
    "RequestEntriesParameters",
    "RequestEntriesResult",
]
