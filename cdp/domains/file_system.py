"""Generated bindings for the CDP FileSystem domain. Do not edit manually."""

from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, cast, overload

from typing_extensions import NotRequired, TypedDict, Unpack

from cdp.domain import Domain as BaseDomain

if TYPE_CHECKING:
    from . import network as Network
    from . import storage as Storage


class File(TypedDict):
    name: str
    lastModified: Network.TimeSinceEpoch
    size: float
    type: str


class Directory(TypedDict):
    name: str
    nestedDirectories: list[str]
    nestedFiles: list[File]


class BucketFileSystemLocator(TypedDict):
    storageKey: Storage.SerializedStorageKey
    bucketName: NotRequired[str]
    pathComponents: list[str]


class GetDirectoryParameters(TypedDict):
    bucketFileSystemLocator: BucketFileSystemLocator


class GetDirectoryResult(TypedDict):
    directory: Directory


class FileSystem(BaseDomain):
    """The CDP FileSystem domain."""

    domain_name = "FileSystem"

    @overload
    async def getDirectory(
        self,
        params: GetDirectoryParameters,
        session_id: str | None = None,
    ) -> GetDirectoryResult: ...

    @overload
    async def getDirectory(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[GetDirectoryParameters],
    ) -> GetDirectoryResult: ...

    async def getDirectory(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> GetDirectoryResult:
        """Send FileSystem.getDirectory."""

        return cast(
            GetDirectoryResult,
            await self._command("getDirectory", params, session_id, kwargs),
        )


__all__ = [
    "BucketFileSystemLocator",
    "Directory",
    "File",
    "FileSystem",
    "GetDirectoryParameters",
    "GetDirectoryResult",
]
