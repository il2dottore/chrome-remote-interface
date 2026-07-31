"""Generated bindings for the CDP Storage domain. Do not edit manually."""

from __future__ import annotations

from collections.abc import Awaitable, Mapping
from typing import TYPE_CHECKING, Literal, TypeAlias, cast, overload

from typing_extensions import NotRequired, TypedDict, Unpack

from cdp.domain import Domain as BaseDomain, EventCallback, Unsubscribe
from cdp.types import JsonObject

if TYPE_CHECKING:
    from . import browser as Browser
    from . import network as Network
    from . import page as Page
    from . import target as Target


SerializedStorageKey: TypeAlias = str

StorageType: TypeAlias = Literal[
    "cookies",
    "file_systems",
    "indexeddb",
    "local_storage",
    "shader_cache",
    "websql",
    "service_workers",
    "cache_storage",
    "shared_storage",
    "storage_buckets",
    "all",
    "other",
]


class UsageForType(TypedDict):
    storageType: StorageType
    usage: float


class TrustTokens(TypedDict):
    issuerOrigin: str
    count: float


SharedStorageAccessScope: TypeAlias = Literal[
    "window", "sharedStorageWorklet", "header"
]

SharedStorageAccessMethod: TypeAlias = Literal[
    "addModule",
    "createWorklet",
    "selectURL",
    "run",
    "batchUpdate",
    "set",
    "append",
    "delete",
    "clear",
    "get",
    "keys",
    "values",
    "entries",
    "length",
    "remainingBudget",
]


class SharedStorageEntry(TypedDict):
    key: str
    value: str


class SharedStorageMetadata(TypedDict):
    creationTime: Network.TimeSinceEpoch
    length: int
    remainingBudget: float
    bytesUsed: int


class SharedStoragePrivateAggregationConfig(TypedDict):
    aggregationCoordinatorOrigin: NotRequired[str]
    contextId: NotRequired[str]
    filteringIdMaxBytes: int
    maxContributions: NotRequired[int]


class SharedStorageReportingMetadata(TypedDict):
    eventType: str
    reportingUrl: str


class SharedStorageUrlWithMetadata(TypedDict):
    url: str
    reportingMetadata: list[SharedStorageReportingMetadata]


class SharedStorageAccessParams(TypedDict):
    scriptSourceUrl: NotRequired[str]
    dataOrigin: NotRequired[str]
    operationName: NotRequired[str]
    operationId: NotRequired[str]
    keepAlive: NotRequired[bool]
    privateAggregationConfig: NotRequired[SharedStoragePrivateAggregationConfig]
    serializedData: NotRequired[str]
    urlsWithMetadata: NotRequired[list[SharedStorageUrlWithMetadata]]
    urnUuid: NotRequired[str]
    key: NotRequired[str]
    value: NotRequired[str]
    ignoreIfPresent: NotRequired[bool]
    workletOrdinal: NotRequired[int]
    workletTargetId: NotRequired[Target.TargetID]
    withLock: NotRequired[str]
    batchUpdateId: NotRequired[str]
    batchSize: NotRequired[int]


StorageBucketsDurability: TypeAlias = Literal["relaxed", "strict"]


class StorageBucket(TypedDict):
    storageKey: SerializedStorageKey
    name: NotRequired[str]


class StorageBucketInfo(TypedDict):
    bucket: StorageBucket
    id: str
    expiration: Network.TimeSinceEpoch
    quota: float
    persistent: bool
    durability: StorageBucketsDurability


class RelatedWebsiteSet(TypedDict):
    primarySites: list[str]
    associatedSites: list[str]
    serviceSites: list[str]


class GetStorageKeyForFrameParameters(TypedDict):
    frameId: Page.FrameId


class GetStorageKeyForFrameResult(TypedDict):
    storageKey: SerializedStorageKey


class GetStorageKeyParameters(TypedDict):
    frameId: NotRequired[Page.FrameId]


class GetStorageKeyResult(TypedDict):
    storageKey: SerializedStorageKey


class ClearDataForOriginParameters(TypedDict):
    origin: str
    storageTypes: str


class ClearDataForStorageKeyParameters(TypedDict):
    storageKey: str
    storageTypes: str


class GetCookiesParameters(TypedDict):
    browserContextId: NotRequired[Browser.BrowserContextID]


class GetCookiesResult(TypedDict):
    cookies: list[Network.Cookie]


class SetCookiesParameters(TypedDict):
    cookies: list[Network.CookieParam]
    browserContextId: NotRequired[Browser.BrowserContextID]


class ClearCookiesParameters(TypedDict):
    browserContextId: NotRequired[Browser.BrowserContextID]


class GetUsageAndQuotaParameters(TypedDict):
    origin: str


class GetUsageAndQuotaResult(TypedDict):
    usage: float
    quota: float
    overrideActive: bool
    usageBreakdown: list[UsageForType]


class OverrideQuotaForOriginParameters(TypedDict):
    origin: str
    quotaSize: NotRequired[float]


class TrackCacheStorageForOriginParameters(TypedDict):
    origin: str


class TrackCacheStorageForStorageKeyParameters(TypedDict):
    storageKey: str


class TrackIndexedDBForOriginParameters(TypedDict):
    origin: str


class TrackIndexedDBForStorageKeyParameters(TypedDict):
    storageKey: str


class UntrackCacheStorageForOriginParameters(TypedDict):
    origin: str


class UntrackCacheStorageForStorageKeyParameters(TypedDict):
    storageKey: str


class UntrackIndexedDBForOriginParameters(TypedDict):
    origin: str


class UntrackIndexedDBForStorageKeyParameters(TypedDict):
    storageKey: str


class GetTrustTokensResult(TypedDict):
    tokens: list[TrustTokens]


class ClearTrustTokensParameters(TypedDict):
    issuerOrigin: str


class ClearTrustTokensResult(TypedDict):
    didDeleteTokens: bool


class GetSharedStorageMetadataParameters(TypedDict):
    ownerOrigin: str


class GetSharedStorageMetadataResult(TypedDict):
    metadata: SharedStorageMetadata


class GetSharedStorageEntriesParameters(TypedDict):
    ownerOrigin: str


class GetSharedStorageEntriesResult(TypedDict):
    entries: list[SharedStorageEntry]


class SetSharedStorageEntryParameters(TypedDict):
    ownerOrigin: str
    key: str
    value: str
    ignoreIfPresent: NotRequired[bool]


class DeleteSharedStorageEntryParameters(TypedDict):
    ownerOrigin: str
    key: str


class ClearSharedStorageEntriesParameters(TypedDict):
    ownerOrigin: str


class ResetSharedStorageBudgetParameters(TypedDict):
    ownerOrigin: str


class SetSharedStorageTrackingParameters(TypedDict):
    enable: bool


class SetStorageBucketTrackingParameters(TypedDict):
    storageKey: str
    enable: bool


class DeleteStorageBucketParameters(TypedDict):
    bucket: StorageBucket


class RunBounceTrackingMitigationsResult(TypedDict):
    deletedSites: list[str]


class GetRelatedWebsiteSetsResult(TypedDict):
    sets: list[RelatedWebsiteSet]


class CacheStorageContentUpdatedEvent(TypedDict):
    origin: str
    storageKey: str
    bucketId: str
    cacheName: str


class CacheStorageListUpdatedEvent(TypedDict):
    origin: str
    storageKey: str
    bucketId: str


class IndexedDBContentUpdatedEvent(TypedDict):
    origin: str
    storageKey: str
    bucketId: str
    databaseName: str
    objectStoreName: str


class IndexedDBListUpdatedEvent(TypedDict):
    origin: str
    storageKey: str
    bucketId: str


class SharedStorageAccessedEvent(TypedDict):
    accessTime: Network.TimeSinceEpoch
    scope: SharedStorageAccessScope
    method: SharedStorageAccessMethod
    mainFrameId: Page.FrameId
    ownerOrigin: str
    ownerSite: str
    params: SharedStorageAccessParams


class SharedStorageWorkletOperationExecutionFinishedEvent(TypedDict):
    finishedTime: Network.TimeSinceEpoch
    executionTime: int
    method: SharedStorageAccessMethod
    operationId: str
    workletTargetId: Target.TargetID
    mainFrameId: Page.FrameId
    ownerOrigin: str


class StorageBucketCreatedOrUpdatedEvent(TypedDict):
    bucketInfo: StorageBucketInfo


class StorageBucketDeletedEvent(TypedDict):
    bucketId: str


class Storage(BaseDomain):
    """The CDP Storage domain."""

    domain_name = "Storage"

    @overload
    async def getStorageKeyForFrame(
        self,
        params: GetStorageKeyForFrameParameters,
        session_id: str | None = None,
    ) -> GetStorageKeyForFrameResult: ...

    @overload
    async def getStorageKeyForFrame(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[GetStorageKeyForFrameParameters],
    ) -> GetStorageKeyForFrameResult: ...

    async def getStorageKeyForFrame(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> GetStorageKeyForFrameResult:
        """Returns a storage key given a frame id. Deprecated. Please use Storage.getStorageKey instead."""

        return cast(
            GetStorageKeyForFrameResult,
            await self._command("getStorageKeyForFrame", params, session_id, kwargs),
        )

    @overload
    async def getStorageKey(
        self,
        params: GetStorageKeyParameters,
        session_id: str | None = None,
    ) -> GetStorageKeyResult: ...

    @overload
    async def getStorageKey(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[GetStorageKeyParameters],
    ) -> GetStorageKeyResult: ...

    async def getStorageKey(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> GetStorageKeyResult:
        """Returns storage key for the given frame. If no frame ID is provided, the storage key of the target executing this command is returned."""

        return cast(
            GetStorageKeyResult,
            await self._command("getStorageKey", params, session_id, kwargs),
        )

    @overload
    async def clearDataForOrigin(
        self,
        params: ClearDataForOriginParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def clearDataForOrigin(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[ClearDataForOriginParameters],
    ) -> JsonObject: ...

    async def clearDataForOrigin(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Clears storage for origin."""

        return await self._command("clearDataForOrigin", params, session_id, kwargs)

    @overload
    async def clearDataForStorageKey(
        self,
        params: ClearDataForStorageKeyParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def clearDataForStorageKey(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[ClearDataForStorageKeyParameters],
    ) -> JsonObject: ...

    async def clearDataForStorageKey(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Clears storage for storage key."""

        return await self._command("clearDataForStorageKey", params, session_id, kwargs)

    @overload
    async def getCookies(
        self,
        params: GetCookiesParameters,
        session_id: str | None = None,
    ) -> GetCookiesResult: ...

    @overload
    async def getCookies(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[GetCookiesParameters],
    ) -> GetCookiesResult: ...

    async def getCookies(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> GetCookiesResult:
        """Returns all browser cookies."""

        return cast(
            GetCookiesResult,
            await self._command("getCookies", params, session_id, kwargs),
        )

    @overload
    async def setCookies(
        self,
        params: SetCookiesParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def setCookies(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetCookiesParameters],
    ) -> JsonObject: ...

    async def setCookies(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Sets given cookies."""

        return await self._command("setCookies", params, session_id, kwargs)

    @overload
    async def clearCookies(
        self,
        params: ClearCookiesParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def clearCookies(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[ClearCookiesParameters],
    ) -> JsonObject: ...

    async def clearCookies(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Clears cookies."""

        return await self._command("clearCookies", params, session_id, kwargs)

    @overload
    async def getUsageAndQuota(
        self,
        params: GetUsageAndQuotaParameters,
        session_id: str | None = None,
    ) -> GetUsageAndQuotaResult: ...

    @overload
    async def getUsageAndQuota(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[GetUsageAndQuotaParameters],
    ) -> GetUsageAndQuotaResult: ...

    async def getUsageAndQuota(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> GetUsageAndQuotaResult:
        """Returns usage and quota in bytes."""

        return cast(
            GetUsageAndQuotaResult,
            await self._command("getUsageAndQuota", params, session_id, kwargs),
        )

    @overload
    async def overrideQuotaForOrigin(
        self,
        params: OverrideQuotaForOriginParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def overrideQuotaForOrigin(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[OverrideQuotaForOriginParameters],
    ) -> JsonObject: ...

    async def overrideQuotaForOrigin(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Override quota for the specified origin"""

        return await self._command("overrideQuotaForOrigin", params, session_id, kwargs)

    @overload
    async def trackCacheStorageForOrigin(
        self,
        params: TrackCacheStorageForOriginParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def trackCacheStorageForOrigin(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[TrackCacheStorageForOriginParameters],
    ) -> JsonObject: ...

    async def trackCacheStorageForOrigin(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Registers origin to be notified when an update occurs to its cache storage list."""

        return await self._command(
            "trackCacheStorageForOrigin", params, session_id, kwargs
        )

    @overload
    async def trackCacheStorageForStorageKey(
        self,
        params: TrackCacheStorageForStorageKeyParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def trackCacheStorageForStorageKey(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[TrackCacheStorageForStorageKeyParameters],
    ) -> JsonObject: ...

    async def trackCacheStorageForStorageKey(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Registers storage key to be notified when an update occurs to its cache storage list."""

        return await self._command(
            "trackCacheStorageForStorageKey", params, session_id, kwargs
        )

    @overload
    async def trackIndexedDBForOrigin(
        self,
        params: TrackIndexedDBForOriginParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def trackIndexedDBForOrigin(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[TrackIndexedDBForOriginParameters],
    ) -> JsonObject: ...

    async def trackIndexedDBForOrigin(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Registers origin to be notified when an update occurs to its IndexedDB."""

        return await self._command(
            "trackIndexedDBForOrigin", params, session_id, kwargs
        )

    @overload
    async def trackIndexedDBForStorageKey(
        self,
        params: TrackIndexedDBForStorageKeyParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def trackIndexedDBForStorageKey(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[TrackIndexedDBForStorageKeyParameters],
    ) -> JsonObject: ...

    async def trackIndexedDBForStorageKey(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Registers storage key to be notified when an update occurs to its IndexedDB."""

        return await self._command(
            "trackIndexedDBForStorageKey", params, session_id, kwargs
        )

    @overload
    async def untrackCacheStorageForOrigin(
        self,
        params: UntrackCacheStorageForOriginParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def untrackCacheStorageForOrigin(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[UntrackCacheStorageForOriginParameters],
    ) -> JsonObject: ...

    async def untrackCacheStorageForOrigin(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Unregisters origin from receiving notifications for cache storage."""

        return await self._command(
            "untrackCacheStorageForOrigin", params, session_id, kwargs
        )

    @overload
    async def untrackCacheStorageForStorageKey(
        self,
        params: UntrackCacheStorageForStorageKeyParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def untrackCacheStorageForStorageKey(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[UntrackCacheStorageForStorageKeyParameters],
    ) -> JsonObject: ...

    async def untrackCacheStorageForStorageKey(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Unregisters storage key from receiving notifications for cache storage."""

        return await self._command(
            "untrackCacheStorageForStorageKey", params, session_id, kwargs
        )

    @overload
    async def untrackIndexedDBForOrigin(
        self,
        params: UntrackIndexedDBForOriginParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def untrackIndexedDBForOrigin(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[UntrackIndexedDBForOriginParameters],
    ) -> JsonObject: ...

    async def untrackIndexedDBForOrigin(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Unregisters origin from receiving notifications for IndexedDB."""

        return await self._command(
            "untrackIndexedDBForOrigin", params, session_id, kwargs
        )

    @overload
    async def untrackIndexedDBForStorageKey(
        self,
        params: UntrackIndexedDBForStorageKeyParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def untrackIndexedDBForStorageKey(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[UntrackIndexedDBForStorageKeyParameters],
    ) -> JsonObject: ...

    async def untrackIndexedDBForStorageKey(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Unregisters storage key from receiving notifications for IndexedDB."""

        return await self._command(
            "untrackIndexedDBForStorageKey", params, session_id, kwargs
        )

    async def getTrustTokens(
        self,
        session_id: str | None = None,
    ) -> GetTrustTokensResult:
        """Returns the number of stored Trust Tokens per issuer for the current browsing context."""

        return cast(
            GetTrustTokensResult,
            await self._command("getTrustTokens", None, session_id, {}),
        )

    @overload
    async def clearTrustTokens(
        self,
        params: ClearTrustTokensParameters,
        session_id: str | None = None,
    ) -> ClearTrustTokensResult: ...

    @overload
    async def clearTrustTokens(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[ClearTrustTokensParameters],
    ) -> ClearTrustTokensResult: ...

    async def clearTrustTokens(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> ClearTrustTokensResult:
        """Removes all Trust Tokens issued by the provided issuerOrigin. Leaves other stored data, including the issuer's Redemption Records, intact."""

        return cast(
            ClearTrustTokensResult,
            await self._command("clearTrustTokens", params, session_id, kwargs),
        )

    @overload
    async def getSharedStorageMetadata(
        self,
        params: GetSharedStorageMetadataParameters,
        session_id: str | None = None,
    ) -> GetSharedStorageMetadataResult: ...

    @overload
    async def getSharedStorageMetadata(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[GetSharedStorageMetadataParameters],
    ) -> GetSharedStorageMetadataResult: ...

    async def getSharedStorageMetadata(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> GetSharedStorageMetadataResult:
        """Gets metadata for an origin's shared storage."""

        return cast(
            GetSharedStorageMetadataResult,
            await self._command("getSharedStorageMetadata", params, session_id, kwargs),
        )

    @overload
    async def getSharedStorageEntries(
        self,
        params: GetSharedStorageEntriesParameters,
        session_id: str | None = None,
    ) -> GetSharedStorageEntriesResult: ...

    @overload
    async def getSharedStorageEntries(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[GetSharedStorageEntriesParameters],
    ) -> GetSharedStorageEntriesResult: ...

    async def getSharedStorageEntries(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> GetSharedStorageEntriesResult:
        """Gets the entries in an given origin's shared storage."""

        return cast(
            GetSharedStorageEntriesResult,
            await self._command("getSharedStorageEntries", params, session_id, kwargs),
        )

    @overload
    async def setSharedStorageEntry(
        self,
        params: SetSharedStorageEntryParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def setSharedStorageEntry(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetSharedStorageEntryParameters],
    ) -> JsonObject: ...

    async def setSharedStorageEntry(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Sets entry with `key` and `value` for a given origin's shared storage."""

        return await self._command("setSharedStorageEntry", params, session_id, kwargs)

    @overload
    async def deleteSharedStorageEntry(
        self,
        params: DeleteSharedStorageEntryParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def deleteSharedStorageEntry(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[DeleteSharedStorageEntryParameters],
    ) -> JsonObject: ...

    async def deleteSharedStorageEntry(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Deletes entry for `key` (if it exists) for a given origin's shared storage."""

        return await self._command(
            "deleteSharedStorageEntry", params, session_id, kwargs
        )

    @overload
    async def clearSharedStorageEntries(
        self,
        params: ClearSharedStorageEntriesParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def clearSharedStorageEntries(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[ClearSharedStorageEntriesParameters],
    ) -> JsonObject: ...

    async def clearSharedStorageEntries(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Clears all entries for a given origin's shared storage."""

        return await self._command(
            "clearSharedStorageEntries", params, session_id, kwargs
        )

    @overload
    async def resetSharedStorageBudget(
        self,
        params: ResetSharedStorageBudgetParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def resetSharedStorageBudget(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[ResetSharedStorageBudgetParameters],
    ) -> JsonObject: ...

    async def resetSharedStorageBudget(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Resets the budget for `ownerOrigin` by clearing all budget withdrawals."""

        return await self._command(
            "resetSharedStorageBudget", params, session_id, kwargs
        )

    @overload
    async def setSharedStorageTracking(
        self,
        params: SetSharedStorageTrackingParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def setSharedStorageTracking(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetSharedStorageTrackingParameters],
    ) -> JsonObject: ...

    async def setSharedStorageTracking(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Enables/disables issuing of sharedStorageAccessed events."""

        return await self._command(
            "setSharedStorageTracking", params, session_id, kwargs
        )

    @overload
    async def setStorageBucketTracking(
        self,
        params: SetStorageBucketTrackingParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def setStorageBucketTracking(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetStorageBucketTrackingParameters],
    ) -> JsonObject: ...

    async def setStorageBucketTracking(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Set tracking for a storage key's buckets."""

        return await self._command(
            "setStorageBucketTracking", params, session_id, kwargs
        )

    @overload
    async def deleteStorageBucket(
        self,
        params: DeleteStorageBucketParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def deleteStorageBucket(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[DeleteStorageBucketParameters],
    ) -> JsonObject: ...

    async def deleteStorageBucket(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Deletes the Storage Bucket with the given storage key and bucket name."""

        return await self._command("deleteStorageBucket", params, session_id, kwargs)

    async def runBounceTrackingMitigations(
        self,
        session_id: str | None = None,
    ) -> RunBounceTrackingMitigationsResult:
        """Deletes state for sites identified as potential bounce trackers, immediately."""

        return cast(
            RunBounceTrackingMitigationsResult,
            await self._command("runBounceTrackingMitigations", None, session_id, {}),
        )

    async def getRelatedWebsiteSets(
        self,
        session_id: str | None = None,
    ) -> GetRelatedWebsiteSetsResult:
        """Returns the effective Related Website Sets in use by this profile for the browser session. The effective Related Website Sets will not change during a browser session."""

        return cast(
            GetRelatedWebsiteSetsResult,
            await self._command("getRelatedWebsiteSets", None, session_id, {}),
        )

    @overload
    def cacheStorageContentUpdated(
        self,
        callback_or_session: EventCallback[CacheStorageContentUpdatedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def cacheStorageContentUpdated(
        self,
        callback_or_session: str,
        handler: EventCallback[CacheStorageContentUpdatedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def cacheStorageContentUpdated(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[CacheStorageContentUpdatedEvent]: ...

    def cacheStorageContentUpdated(
        self,
        callback_or_session: EventCallback[CacheStorageContentUpdatedEvent]
        | str
        | None = None,
        handler: EventCallback[CacheStorageContentUpdatedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[CacheStorageContentUpdatedEvent] | Unsubscribe:
        """A cache's contents have been modified."""

        return cast(
            Awaitable[CacheStorageContentUpdatedEvent] | Unsubscribe,
            self._event(
                "cacheStorageContentUpdated",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def cacheStorageListUpdated(
        self,
        callback_or_session: EventCallback[CacheStorageListUpdatedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def cacheStorageListUpdated(
        self,
        callback_or_session: str,
        handler: EventCallback[CacheStorageListUpdatedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def cacheStorageListUpdated(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[CacheStorageListUpdatedEvent]: ...

    def cacheStorageListUpdated(
        self,
        callback_or_session: EventCallback[CacheStorageListUpdatedEvent]
        | str
        | None = None,
        handler: EventCallback[CacheStorageListUpdatedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[CacheStorageListUpdatedEvent] | Unsubscribe:
        """A cache has been added/deleted."""

        return cast(
            Awaitable[CacheStorageListUpdatedEvent] | Unsubscribe,
            self._event(
                "cacheStorageListUpdated",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def indexedDBContentUpdated(
        self,
        callback_or_session: EventCallback[IndexedDBContentUpdatedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def indexedDBContentUpdated(
        self,
        callback_or_session: str,
        handler: EventCallback[IndexedDBContentUpdatedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def indexedDBContentUpdated(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[IndexedDBContentUpdatedEvent]: ...

    def indexedDBContentUpdated(
        self,
        callback_or_session: EventCallback[IndexedDBContentUpdatedEvent]
        | str
        | None = None,
        handler: EventCallback[IndexedDBContentUpdatedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[IndexedDBContentUpdatedEvent] | Unsubscribe:
        """The origin's IndexedDB object store has been modified."""

        return cast(
            Awaitable[IndexedDBContentUpdatedEvent] | Unsubscribe,
            self._event(
                "indexedDBContentUpdated",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def indexedDBListUpdated(
        self,
        callback_or_session: EventCallback[IndexedDBListUpdatedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def indexedDBListUpdated(
        self,
        callback_or_session: str,
        handler: EventCallback[IndexedDBListUpdatedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def indexedDBListUpdated(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[IndexedDBListUpdatedEvent]: ...

    def indexedDBListUpdated(
        self,
        callback_or_session: EventCallback[IndexedDBListUpdatedEvent]
        | str
        | None = None,
        handler: EventCallback[IndexedDBListUpdatedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[IndexedDBListUpdatedEvent] | Unsubscribe:
        """The origin's IndexedDB database list has been modified."""

        return cast(
            Awaitable[IndexedDBListUpdatedEvent] | Unsubscribe,
            self._event(
                "indexedDBListUpdated",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def sharedStorageAccessed(
        self,
        callback_or_session: EventCallback[SharedStorageAccessedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def sharedStorageAccessed(
        self,
        callback_or_session: str,
        handler: EventCallback[SharedStorageAccessedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def sharedStorageAccessed(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[SharedStorageAccessedEvent]: ...

    def sharedStorageAccessed(
        self,
        callback_or_session: EventCallback[SharedStorageAccessedEvent]
        | str
        | None = None,
        handler: EventCallback[SharedStorageAccessedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[SharedStorageAccessedEvent] | Unsubscribe:
        """Shared storage was accessed by the associated page. The following parameters are included in all events."""

        return cast(
            Awaitable[SharedStorageAccessedEvent] | Unsubscribe,
            self._event(
                "sharedStorageAccessed",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def sharedStorageWorkletOperationExecutionFinished(
        self,
        callback_or_session: EventCallback[
            SharedStorageWorkletOperationExecutionFinishedEvent
        ],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def sharedStorageWorkletOperationExecutionFinished(
        self,
        callback_or_session: str,
        handler: EventCallback[SharedStorageWorkletOperationExecutionFinishedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def sharedStorageWorkletOperationExecutionFinished(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[SharedStorageWorkletOperationExecutionFinishedEvent]: ...

    def sharedStorageWorkletOperationExecutionFinished(
        self,
        callback_or_session: EventCallback[
            SharedStorageWorkletOperationExecutionFinishedEvent
        ]
        | str
        | None = None,
        handler: EventCallback[SharedStorageWorkletOperationExecutionFinishedEvent]
        | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[SharedStorageWorkletOperationExecutionFinishedEvent] | Unsubscribe:
        """A shared storage run or selectURL operation finished its execution. The following parameters are included in all events."""

        return cast(
            Awaitable[SharedStorageWorkletOperationExecutionFinishedEvent]
            | Unsubscribe,
            self._event(
                "sharedStorageWorkletOperationExecutionFinished",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def storageBucketCreatedOrUpdated(
        self,
        callback_or_session: EventCallback[StorageBucketCreatedOrUpdatedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def storageBucketCreatedOrUpdated(
        self,
        callback_or_session: str,
        handler: EventCallback[StorageBucketCreatedOrUpdatedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def storageBucketCreatedOrUpdated(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[StorageBucketCreatedOrUpdatedEvent]: ...

    def storageBucketCreatedOrUpdated(
        self,
        callback_or_session: EventCallback[StorageBucketCreatedOrUpdatedEvent]
        | str
        | None = None,
        handler: EventCallback[StorageBucketCreatedOrUpdatedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[StorageBucketCreatedOrUpdatedEvent] | Unsubscribe:
        """Wait for or subscribe to Storage.storageBucketCreatedOrUpdated."""

        return cast(
            Awaitable[StorageBucketCreatedOrUpdatedEvent] | Unsubscribe,
            self._event(
                "storageBucketCreatedOrUpdated",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def storageBucketDeleted(
        self,
        callback_or_session: EventCallback[StorageBucketDeletedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def storageBucketDeleted(
        self,
        callback_or_session: str,
        handler: EventCallback[StorageBucketDeletedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def storageBucketDeleted(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[StorageBucketDeletedEvent]: ...

    def storageBucketDeleted(
        self,
        callback_or_session: EventCallback[StorageBucketDeletedEvent]
        | str
        | None = None,
        handler: EventCallback[StorageBucketDeletedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[StorageBucketDeletedEvent] | Unsubscribe:
        """Wait for or subscribe to Storage.storageBucketDeleted."""

        return cast(
            Awaitable[StorageBucketDeletedEvent] | Unsubscribe,
            self._event(
                "storageBucketDeleted",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )


__all__ = [
    "CacheStorageContentUpdatedEvent",
    "CacheStorageListUpdatedEvent",
    "ClearCookiesParameters",
    "ClearDataForOriginParameters",
    "ClearDataForStorageKeyParameters",
    "ClearSharedStorageEntriesParameters",
    "ClearTrustTokensParameters",
    "ClearTrustTokensResult",
    "DeleteSharedStorageEntryParameters",
    "DeleteStorageBucketParameters",
    "GetCookiesParameters",
    "GetCookiesResult",
    "GetRelatedWebsiteSetsResult",
    "GetSharedStorageEntriesParameters",
    "GetSharedStorageEntriesResult",
    "GetSharedStorageMetadataParameters",
    "GetSharedStorageMetadataResult",
    "GetStorageKeyForFrameParameters",
    "GetStorageKeyForFrameResult",
    "GetStorageKeyParameters",
    "GetStorageKeyResult",
    "GetTrustTokensResult",
    "GetUsageAndQuotaParameters",
    "GetUsageAndQuotaResult",
    "IndexedDBContentUpdatedEvent",
    "IndexedDBListUpdatedEvent",
    "OverrideQuotaForOriginParameters",
    "RelatedWebsiteSet",
    "ResetSharedStorageBudgetParameters",
    "RunBounceTrackingMitigationsResult",
    "SerializedStorageKey",
    "SetCookiesParameters",
    "SetSharedStorageEntryParameters",
    "SetSharedStorageTrackingParameters",
    "SetStorageBucketTrackingParameters",
    "SharedStorageAccessMethod",
    "SharedStorageAccessParams",
    "SharedStorageAccessScope",
    "SharedStorageAccessedEvent",
    "SharedStorageEntry",
    "SharedStorageMetadata",
    "SharedStoragePrivateAggregationConfig",
    "SharedStorageReportingMetadata",
    "SharedStorageUrlWithMetadata",
    "SharedStorageWorkletOperationExecutionFinishedEvent",
    "Storage",
    "StorageBucket",
    "StorageBucketCreatedOrUpdatedEvent",
    "StorageBucketDeletedEvent",
    "StorageBucketInfo",
    "StorageBucketsDurability",
    "StorageType",
    "TrackCacheStorageForOriginParameters",
    "TrackCacheStorageForStorageKeyParameters",
    "TrackIndexedDBForOriginParameters",
    "TrackIndexedDBForStorageKeyParameters",
    "TrustTokens",
    "UntrackCacheStorageForOriginParameters",
    "UntrackCacheStorageForStorageKeyParameters",
    "UntrackIndexedDBForOriginParameters",
    "UntrackIndexedDBForStorageKeyParameters",
    "UsageForType",
]
