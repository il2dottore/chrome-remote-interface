"""Generated bindings for the CDP Extensions domain. Do not edit manually."""

from __future__ import annotations

from collections.abc import Mapping
from typing import Literal, TypeAlias, cast, overload

from typing_extensions import NotRequired, TypedDict, Unpack

from cdp.domain import Domain as BaseDomain
from cdp.types import JsonObject


StorageArea: TypeAlias = Literal["session", "local", "sync", "managed"]


class ExtensionInfo(TypedDict):
    id: str
    name: str
    version: str
    path: str
    enabled: bool


class TriggerActionParameters(TypedDict):
    id: str
    targetId: str


class LoadUnpackedParameters(TypedDict):
    path: str
    enableInIncognito: NotRequired[bool]


class LoadUnpackedResult(TypedDict):
    id: str


class GetExtensionsResult(TypedDict):
    extensions: list[ExtensionInfo]


class UninstallParameters(TypedDict):
    id: str


class GetStorageItemsParameters(TypedDict):
    id: str
    storageArea: StorageArea
    keys: NotRequired[list[str]]


class GetStorageItemsResult(TypedDict):
    data: JsonObject


class RemoveStorageItemsParameters(TypedDict):
    id: str
    storageArea: StorageArea
    keys: list[str]


class ClearStorageItemsParameters(TypedDict):
    id: str
    storageArea: StorageArea


class SetStorageItemsParameters(TypedDict):
    id: str
    storageArea: StorageArea
    values: JsonObject


class Extensions(BaseDomain):
    """Defines commands and events for browser extensions."""

    domain_name = "Extensions"

    @overload
    async def triggerAction(
        self,
        params: TriggerActionParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def triggerAction(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[TriggerActionParameters],
    ) -> JsonObject: ...

    async def triggerAction(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Runs an extension default action."""

        return await self._command("triggerAction", params, session_id, kwargs)

    @overload
    async def loadUnpacked(
        self,
        params: LoadUnpackedParameters,
        session_id: str | None = None,
    ) -> LoadUnpackedResult: ...

    @overload
    async def loadUnpacked(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[LoadUnpackedParameters],
    ) -> LoadUnpackedResult: ...

    async def loadUnpacked(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> LoadUnpackedResult:
        """Installs an unpacked extension from the filesystem similar to --load-extension CLI flags. Returns extension ID once the extension has been installed."""

        return cast(
            LoadUnpackedResult,
            await self._command("loadUnpacked", params, session_id, kwargs),
        )

    async def getExtensions(
        self,
        session_id: str | None = None,
    ) -> GetExtensionsResult:
        """Gets a list of all unpacked extensions."""

        return cast(
            GetExtensionsResult,
            await self._command("getExtensions", None, session_id, {}),
        )

    @overload
    async def uninstall(
        self,
        params: UninstallParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def uninstall(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[UninstallParameters],
    ) -> JsonObject: ...

    async def uninstall(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Uninstalls an unpacked extension (others not supported) from the profile."""

        return await self._command("uninstall", params, session_id, kwargs)

    @overload
    async def getStorageItems(
        self,
        params: GetStorageItemsParameters,
        session_id: str | None = None,
    ) -> GetStorageItemsResult: ...

    @overload
    async def getStorageItems(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[GetStorageItemsParameters],
    ) -> GetStorageItemsResult: ...

    async def getStorageItems(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> GetStorageItemsResult:
        """Gets data from extension storage in the given `storageArea`. If `keys` is specified, these are used to filter the result."""

        return cast(
            GetStorageItemsResult,
            await self._command("getStorageItems", params, session_id, kwargs),
        )

    @overload
    async def removeStorageItems(
        self,
        params: RemoveStorageItemsParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def removeStorageItems(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[RemoveStorageItemsParameters],
    ) -> JsonObject: ...

    async def removeStorageItems(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Removes `keys` from extension storage in the given `storageArea`."""

        return await self._command("removeStorageItems", params, session_id, kwargs)

    @overload
    async def clearStorageItems(
        self,
        params: ClearStorageItemsParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def clearStorageItems(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[ClearStorageItemsParameters],
    ) -> JsonObject: ...

    async def clearStorageItems(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Clears extension storage in the given `storageArea`."""

        return await self._command("clearStorageItems", params, session_id, kwargs)

    @overload
    async def setStorageItems(
        self,
        params: SetStorageItemsParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def setStorageItems(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetStorageItemsParameters],
    ) -> JsonObject: ...

    async def setStorageItems(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Sets `values` in extension storage in the given `storageArea`. The provided `values` will be merged with existing values in the storage area."""

        return await self._command("setStorageItems", params, session_id, kwargs)


__all__ = [
    "ClearStorageItemsParameters",
    "ExtensionInfo",
    "Extensions",
    "GetExtensionsResult",
    "GetStorageItemsParameters",
    "GetStorageItemsResult",
    "LoadUnpackedParameters",
    "LoadUnpackedResult",
    "RemoveStorageItemsParameters",
    "SetStorageItemsParameters",
    "StorageArea",
    "TriggerActionParameters",
    "UninstallParameters",
]
