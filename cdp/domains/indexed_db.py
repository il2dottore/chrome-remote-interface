"""Generated bindings for the CDP IndexedDB domain. Do not edit manually."""

from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Literal, cast, overload

from typing_extensions import NotRequired, TypedDict, Unpack

from cdp.domain import Domain as BaseDomain
from cdp.types import JsonObject

if TYPE_CHECKING:
    from . import runtime as Runtime
    from . import storage as Storage


class DatabaseWithObjectStores(TypedDict):
    name: str
    version: float
    objectStores: list[ObjectStore]


class ObjectStore(TypedDict):
    name: str
    keyPath: KeyPath
    autoIncrement: bool
    indexes: list[ObjectStoreIndex]


class ObjectStoreIndex(TypedDict):
    name: str
    keyPath: KeyPath
    unique: bool
    multiEntry: bool


class Key(TypedDict):
    type: Literal["number", "string", "date", "array"]
    number: NotRequired[float]
    string: NotRequired[str]
    date: NotRequired[float]
    array: NotRequired[list[Key]]


class KeyRange(TypedDict):
    lower: NotRequired[Key]
    upper: NotRequired[Key]
    lowerOpen: bool
    upperOpen: bool


class DataEntry(TypedDict):
    key: Runtime.RemoteObject
    primaryKey: Runtime.RemoteObject
    value: Runtime.RemoteObject


class KeyPath(TypedDict):
    type: Literal["null", "string", "array"]
    string: NotRequired[str]
    array: NotRequired[list[str]]


class ClearObjectStoreParameters(TypedDict):
    securityOrigin: NotRequired[str]
    storageKey: NotRequired[str]
    storageBucket: NotRequired[Storage.StorageBucket]
    databaseName: str
    objectStoreName: str


class DeleteDatabaseParameters(TypedDict):
    securityOrigin: NotRequired[str]
    storageKey: NotRequired[str]
    storageBucket: NotRequired[Storage.StorageBucket]
    databaseName: str


class DeleteObjectStoreEntriesParameters(TypedDict):
    securityOrigin: NotRequired[str]
    storageKey: NotRequired[str]
    storageBucket: NotRequired[Storage.StorageBucket]
    databaseName: str
    objectStoreName: str
    keyRange: KeyRange


class RequestDataParameters(TypedDict):
    securityOrigin: NotRequired[str]
    storageKey: NotRequired[str]
    storageBucket: NotRequired[Storage.StorageBucket]
    databaseName: str
    objectStoreName: str
    indexName: NotRequired[str]
    skipCount: int
    pageSize: int
    keyRange: NotRequired[KeyRange]


class RequestDataResult(TypedDict):
    objectStoreDataEntries: list[DataEntry]
    hasMore: bool


class GetMetadataParameters(TypedDict):
    securityOrigin: NotRequired[str]
    storageKey: NotRequired[str]
    storageBucket: NotRequired[Storage.StorageBucket]
    databaseName: str
    objectStoreName: str


class GetMetadataResult(TypedDict):
    entriesCount: float
    keyGeneratorValue: float


class RequestDatabaseParameters(TypedDict):
    securityOrigin: NotRequired[str]
    storageKey: NotRequired[str]
    storageBucket: NotRequired[Storage.StorageBucket]
    databaseName: str


class RequestDatabaseResult(TypedDict):
    databaseWithObjectStores: DatabaseWithObjectStores


class RequestDatabaseNamesParameters(TypedDict):
    securityOrigin: NotRequired[str]
    storageKey: NotRequired[str]
    storageBucket: NotRequired[Storage.StorageBucket]


class RequestDatabaseNamesResult(TypedDict):
    databaseNames: list[str]


class IndexedDB(BaseDomain):
    """The CDP IndexedDB domain."""

    domain_name = "IndexedDB"

    @overload
    async def clearObjectStore(
        self,
        params: ClearObjectStoreParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def clearObjectStore(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[ClearObjectStoreParameters],
    ) -> JsonObject: ...

    async def clearObjectStore(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Clears all entries from an object store."""

        return await self._command("clearObjectStore", params, session_id, kwargs)

    @overload
    async def deleteDatabase(
        self,
        params: DeleteDatabaseParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def deleteDatabase(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[DeleteDatabaseParameters],
    ) -> JsonObject: ...

    async def deleteDatabase(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Deletes a database."""

        return await self._command("deleteDatabase", params, session_id, kwargs)

    @overload
    async def deleteObjectStoreEntries(
        self,
        params: DeleteObjectStoreEntriesParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def deleteObjectStoreEntries(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[DeleteObjectStoreEntriesParameters],
    ) -> JsonObject: ...

    async def deleteObjectStoreEntries(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Delete a range of entries from an object store"""

        return await self._command(
            "deleteObjectStoreEntries", params, session_id, kwargs
        )

    async def disable(
        self,
        session_id: str | None = None,
    ) -> JsonObject:
        """Disables events from backend."""

        return await self._command("disable", None, session_id, {})

    async def enable(
        self,
        session_id: str | None = None,
    ) -> JsonObject:
        """Enables events from backend."""

        return await self._command("enable", None, session_id, {})

    @overload
    async def requestData(
        self,
        params: RequestDataParameters,
        session_id: str | None = None,
    ) -> RequestDataResult: ...

    @overload
    async def requestData(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[RequestDataParameters],
    ) -> RequestDataResult: ...

    async def requestData(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> RequestDataResult:
        """Requests data from object store or index."""

        return cast(
            RequestDataResult,
            await self._command("requestData", params, session_id, kwargs),
        )

    @overload
    async def getMetadata(
        self,
        params: GetMetadataParameters,
        session_id: str | None = None,
    ) -> GetMetadataResult: ...

    @overload
    async def getMetadata(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[GetMetadataParameters],
    ) -> GetMetadataResult: ...

    async def getMetadata(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> GetMetadataResult:
        """Gets metadata of an object store."""

        return cast(
            GetMetadataResult,
            await self._command("getMetadata", params, session_id, kwargs),
        )

    @overload
    async def requestDatabase(
        self,
        params: RequestDatabaseParameters,
        session_id: str | None = None,
    ) -> RequestDatabaseResult: ...

    @overload
    async def requestDatabase(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[RequestDatabaseParameters],
    ) -> RequestDatabaseResult: ...

    async def requestDatabase(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> RequestDatabaseResult:
        """Requests database with given name in given frame."""

        return cast(
            RequestDatabaseResult,
            await self._command("requestDatabase", params, session_id, kwargs),
        )

    @overload
    async def requestDatabaseNames(
        self,
        params: RequestDatabaseNamesParameters,
        session_id: str | None = None,
    ) -> RequestDatabaseNamesResult: ...

    @overload
    async def requestDatabaseNames(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[RequestDatabaseNamesParameters],
    ) -> RequestDatabaseNamesResult: ...

    async def requestDatabaseNames(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> RequestDatabaseNamesResult:
        """Requests database names for given security origin."""

        return cast(
            RequestDatabaseNamesResult,
            await self._command("requestDatabaseNames", params, session_id, kwargs),
        )


__all__ = [
    "ClearObjectStoreParameters",
    "DataEntry",
    "DatabaseWithObjectStores",
    "DeleteDatabaseParameters",
    "DeleteObjectStoreEntriesParameters",
    "GetMetadataParameters",
    "GetMetadataResult",
    "IndexedDB",
    "Key",
    "KeyPath",
    "KeyRange",
    "ObjectStore",
    "ObjectStoreIndex",
    "RequestDataParameters",
    "RequestDataResult",
    "RequestDatabaseNamesParameters",
    "RequestDatabaseNamesResult",
    "RequestDatabaseParameters",
    "RequestDatabaseResult",
]
