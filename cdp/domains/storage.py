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


SerializedStorageKey: TypeAlias = str

StorageType: TypeAlias = Literal[
    "appcache",
    "cookies",
    "file_systems",
    "indexeddb",
    "local_storage",
    "shader_cache",
    "websql",
    "service_workers",
    "cache_storage",
    "interest_groups",
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


InterestGroupAccessType: TypeAlias = Literal[
    "join", "leave", "update", "loaded", "bid", "win"
]


class InterestGroupAd(TypedDict):
    renderUrl: str
    metadata: NotRequired[str]


class InterestGroupDetails(TypedDict):
    ownerOrigin: str
    name: str
    expirationTime: Network.TimeSinceEpoch
    joiningOrigin: str
    biddingUrl: NotRequired[str]
    biddingWasmHelperUrl: NotRequired[str]
    updateUrl: NotRequired[str]
    trustedBiddingSignalsUrl: NotRequired[str]
    trustedBiddingSignalsKeys: list[str]
    userBiddingSignals: NotRequired[str]
    ads: list[InterestGroupAd]
    adComponents: list[InterestGroupAd]


SharedStorageAccessType: TypeAlias = Literal[
    "documentAddModule",
    "documentSelectURL",
    "documentRun",
    "documentSet",
    "documentAppend",
    "documentDelete",
    "documentClear",
    "workletSet",
    "workletAppend",
    "workletDelete",
    "workletClear",
    "workletGet",
    "workletKeys",
    "workletEntries",
    "workletLength",
    "workletRemainingBudget",
]


class SharedStorageEntry(TypedDict):
    key: str
    value: str


class SharedStorageMetadata(TypedDict):
    creationTime: Network.TimeSinceEpoch
    length: int
    remainingBudget: float


class SharedStorageReportingMetadata(TypedDict):
    eventType: str
    reportingUrl: str


class SharedStorageUrlWithMetadata(TypedDict):
    url: str
    reportingMetadata: list[SharedStorageReportingMetadata]


class SharedStorageAccessParams(TypedDict):
    scriptSourceUrl: NotRequired[str]
    operationName: NotRequired[str]
    serializedData: NotRequired[str]
    urlsWithMetadata: NotRequired[list[SharedStorageUrlWithMetadata]]
    key: NotRequired[str]
    value: NotRequired[str]
    ignoreIfPresent: NotRequired[bool]


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


AttributionReportingSourceType: TypeAlias = Literal["navigation", "event"]

UnsignedInt64AsBase10: TypeAlias = str

UnsignedInt128AsBase16: TypeAlias = str

SignedInt64AsBase10: TypeAlias = str


class AttributionReportingFilterDataEntry(TypedDict):
    key: str
    values: list[str]


class AttributionReportingAggregationKeysEntry(TypedDict):
    key: str
    value: UnsignedInt128AsBase16


class AttributionReportingSourceRegistration(TypedDict):
    time: Network.TimeSinceEpoch
    expiry: NotRequired[int]
    eventReportWindow: NotRequired[int]
    aggregatableReportWindow: NotRequired[int]
    type: AttributionReportingSourceType
    sourceOrigin: str
    reportingOrigin: str
    destinationSites: list[str]
    eventId: UnsignedInt64AsBase10
    priority: SignedInt64AsBase10
    filterData: list[AttributionReportingFilterDataEntry]
    aggregationKeys: list[AttributionReportingAggregationKeysEntry]
    debugKey: NotRequired[UnsignedInt64AsBase10]


AttributionReportingSourceRegistrationResult: TypeAlias = Literal[
    "success",
    "internalError",
    "insufficientSourceCapacity",
    "insufficientUniqueDestinationCapacity",
    "excessiveReportingOrigins",
    "prohibitedByBrowserPolicy",
    "successNoised",
    "destinationReportingLimitReached",
    "destinationGlobalLimitReached",
    "destinationBothLimitsReached",
    "reportingOriginsPerSiteLimitReached",
]


class GetStorageKeyForFrameParameters(TypedDict):
    frameId: Page.FrameId


class GetStorageKeyForFrameResult(TypedDict):
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


class GetInterestGroupDetailsParameters(TypedDict):
    ownerOrigin: str
    name: str


class GetInterestGroupDetailsResult(TypedDict):
    details: InterestGroupDetails


class SetInterestGroupTrackingParameters(TypedDict):
    enable: bool


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


class SetAttributionReportingLocalTestingModeParameters(TypedDict):
    enabled: bool


class SetAttributionReportingTrackingParameters(TypedDict):
    enable: bool


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


class InterestGroupAccessedEvent(TypedDict):
    accessTime: Network.TimeSinceEpoch
    type: InterestGroupAccessType
    ownerOrigin: str
    name: str


class SharedStorageAccessedEvent(TypedDict):
    accessTime: Network.TimeSinceEpoch
    type: SharedStorageAccessType
    mainFrameId: Page.FrameId
    ownerOrigin: str
    params: SharedStorageAccessParams


class StorageBucketCreatedOrUpdatedEvent(TypedDict):
    bucketInfo: StorageBucketInfo


class StorageBucketDeletedEvent(TypedDict):
    bucketId: str


class AttributionReportingSourceRegisteredEvent(TypedDict):
    registration: AttributionReportingSourceRegistration
    result: AttributionReportingSourceRegistrationResult


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
        """Returns a storage key given a frame id."""

        return cast(
            GetStorageKeyForFrameResult,
            await self._command("getStorageKeyForFrame", params, session_id, kwargs),
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
    async def getInterestGroupDetails(
        self,
        params: GetInterestGroupDetailsParameters,
        session_id: str | None = None,
    ) -> GetInterestGroupDetailsResult: ...

    @overload
    async def getInterestGroupDetails(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[GetInterestGroupDetailsParameters],
    ) -> GetInterestGroupDetailsResult: ...

    async def getInterestGroupDetails(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> GetInterestGroupDetailsResult:
        """Gets details for a named interest group."""

        return cast(
            GetInterestGroupDetailsResult,
            await self._command("getInterestGroupDetails", params, session_id, kwargs),
        )

    @overload
    async def setInterestGroupTracking(
        self,
        params: SetInterestGroupTrackingParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def setInterestGroupTracking(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetInterestGroupTrackingParameters],
    ) -> JsonObject: ...

    async def setInterestGroupTracking(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Enables/Disables issuing of interestGroupAccessed events."""

        return await self._command(
            "setInterestGroupTracking", params, session_id, kwargs
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

    @overload
    async def setAttributionReportingLocalTestingMode(
        self,
        params: SetAttributionReportingLocalTestingModeParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def setAttributionReportingLocalTestingMode(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetAttributionReportingLocalTestingModeParameters],
    ) -> JsonObject: ...

    async def setAttributionReportingLocalTestingMode(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """https://wicg.github.io/attribution-reporting-api/"""

        return await self._command(
            "setAttributionReportingLocalTestingMode", params, session_id, kwargs
        )

    @overload
    async def setAttributionReportingTracking(
        self,
        params: SetAttributionReportingTrackingParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def setAttributionReportingTracking(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetAttributionReportingTrackingParameters],
    ) -> JsonObject: ...

    async def setAttributionReportingTracking(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Enables/disables issuing of Attribution Reporting events."""

        return await self._command(
            "setAttributionReportingTracking", params, session_id, kwargs
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
    def interestGroupAccessed(
        self,
        callback_or_session: EventCallback[InterestGroupAccessedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def interestGroupAccessed(
        self,
        callback_or_session: str,
        handler: EventCallback[InterestGroupAccessedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def interestGroupAccessed(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[InterestGroupAccessedEvent]: ...

    def interestGroupAccessed(
        self,
        callback_or_session: EventCallback[InterestGroupAccessedEvent]
        | str
        | None = None,
        handler: EventCallback[InterestGroupAccessedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[InterestGroupAccessedEvent] | Unsubscribe:
        """One of the interest groups was accessed by the associated page."""

        return cast(
            Awaitable[InterestGroupAccessedEvent] | Unsubscribe,
            self._event(
                "interestGroupAccessed",
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

    @overload
    def attributionReportingSourceRegistered(
        self,
        callback_or_session: EventCallback[AttributionReportingSourceRegisteredEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def attributionReportingSourceRegistered(
        self,
        callback_or_session: str,
        handler: EventCallback[AttributionReportingSourceRegisteredEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def attributionReportingSourceRegistered(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[AttributionReportingSourceRegisteredEvent]: ...

    def attributionReportingSourceRegistered(
        self,
        callback_or_session: EventCallback[AttributionReportingSourceRegisteredEvent]
        | str
        | None = None,
        handler: EventCallback[AttributionReportingSourceRegisteredEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[AttributionReportingSourceRegisteredEvent] | Unsubscribe:
        """TODO(crbug.com/1458532): Add other Attribution Reporting events, e.g. trigger registration."""

        return cast(
            Awaitable[AttributionReportingSourceRegisteredEvent] | Unsubscribe,
            self._event(
                "attributionReportingSourceRegistered",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )


__all__ = [
    "AttributionReportingAggregationKeysEntry",
    "AttributionReportingFilterDataEntry",
    "AttributionReportingSourceRegisteredEvent",
    "AttributionReportingSourceRegistration",
    "AttributionReportingSourceRegistrationResult",
    "AttributionReportingSourceType",
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
    "GetInterestGroupDetailsParameters",
    "GetInterestGroupDetailsResult",
    "GetSharedStorageEntriesParameters",
    "GetSharedStorageEntriesResult",
    "GetSharedStorageMetadataParameters",
    "GetSharedStorageMetadataResult",
    "GetStorageKeyForFrameParameters",
    "GetStorageKeyForFrameResult",
    "GetTrustTokensResult",
    "GetUsageAndQuotaParameters",
    "GetUsageAndQuotaResult",
    "IndexedDBContentUpdatedEvent",
    "IndexedDBListUpdatedEvent",
    "InterestGroupAccessType",
    "InterestGroupAccessedEvent",
    "InterestGroupAd",
    "InterestGroupDetails",
    "OverrideQuotaForOriginParameters",
    "ResetSharedStorageBudgetParameters",
    "RunBounceTrackingMitigationsResult",
    "SerializedStorageKey",
    "SetAttributionReportingLocalTestingModeParameters",
    "SetAttributionReportingTrackingParameters",
    "SetCookiesParameters",
    "SetInterestGroupTrackingParameters",
    "SetSharedStorageEntryParameters",
    "SetSharedStorageTrackingParameters",
    "SetStorageBucketTrackingParameters",
    "SharedStorageAccessParams",
    "SharedStorageAccessType",
    "SharedStorageAccessedEvent",
    "SharedStorageEntry",
    "SharedStorageMetadata",
    "SharedStorageReportingMetadata",
    "SharedStorageUrlWithMetadata",
    "SignedInt64AsBase10",
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
    "UnsignedInt64AsBase10",
    "UnsignedInt128AsBase16",
    "UntrackCacheStorageForOriginParameters",
    "UntrackCacheStorageForStorageKeyParameters",
    "UntrackIndexedDBForOriginParameters",
    "UntrackIndexedDBForStorageKeyParameters",
    "UsageForType",
]
