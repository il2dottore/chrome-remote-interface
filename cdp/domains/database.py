"""Generated bindings for the CDP Database domain. Do not edit manually."""

from __future__ import annotations

from collections.abc import Awaitable, Mapping
from typing import TypeAlias, cast, overload

from typing_extensions import NotRequired, TypedDict, Unpack

from cdp.domain import Domain as BaseDomain, EventCallback, Unsubscribe
from cdp.types import JsonObject, JsonValue


DatabaseId: TypeAlias = str


class Database(TypedDict):
    id: DatabaseId
    domain: str
    name: str
    version: str


class Error(TypedDict):
    message: str
    code: int


class ExecuteSQLParameters(TypedDict):
    databaseId: DatabaseId
    query: str


class ExecuteSQLResult(TypedDict):
    columnNames: NotRequired[list[str]]
    values: NotRequired[list[JsonValue]]
    sqlError: NotRequired[Error]


class GetDatabaseTableNamesParameters(TypedDict):
    databaseId: DatabaseId


class GetDatabaseTableNamesResult(TypedDict):
    tableNames: list[str]


class AddDatabaseEvent(TypedDict):
    database: Database


class DatabaseDomain(BaseDomain):
    """The CDP Database domain."""

    domain_name = "Database"

    async def disable(
        self,
        session_id: str | None = None,
    ) -> JsonObject:
        """Disables database tracking, prevents database events from being sent to the client."""

        return await self._command("disable", None, session_id, {})

    async def enable(
        self,
        session_id: str | None = None,
    ) -> JsonObject:
        """Enables database tracking, database events will now be delivered to the client."""

        return await self._command("enable", None, session_id, {})

    @overload
    async def executeSQL(
        self,
        params: ExecuteSQLParameters,
        session_id: str | None = None,
    ) -> ExecuteSQLResult: ...

    @overload
    async def executeSQL(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[ExecuteSQLParameters],
    ) -> ExecuteSQLResult: ...

    async def executeSQL(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> ExecuteSQLResult:
        """Send Database.executeSQL."""

        return cast(
            ExecuteSQLResult,
            await self._command("executeSQL", params, session_id, kwargs),
        )

    @overload
    async def getDatabaseTableNames(
        self,
        params: GetDatabaseTableNamesParameters,
        session_id: str | None = None,
    ) -> GetDatabaseTableNamesResult: ...

    @overload
    async def getDatabaseTableNames(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[GetDatabaseTableNamesParameters],
    ) -> GetDatabaseTableNamesResult: ...

    async def getDatabaseTableNames(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> GetDatabaseTableNamesResult:
        """Send Database.getDatabaseTableNames."""

        return cast(
            GetDatabaseTableNamesResult,
            await self._command("getDatabaseTableNames", params, session_id, kwargs),
        )

    @overload
    def addDatabase(
        self,
        callback_or_session: EventCallback[AddDatabaseEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def addDatabase(
        self,
        callback_or_session: str,
        handler: EventCallback[AddDatabaseEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def addDatabase(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[AddDatabaseEvent]: ...

    def addDatabase(
        self,
        callback_or_session: EventCallback[AddDatabaseEvent] | str | None = None,
        handler: EventCallback[AddDatabaseEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[AddDatabaseEvent] | Unsubscribe:
        """Wait for or subscribe to Database.addDatabase."""

        return cast(
            Awaitable[AddDatabaseEvent] | Unsubscribe,
            self._event(
                "addDatabase",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )


__all__ = [
    "AddDatabaseEvent",
    "Database",
    "DatabaseDomain",
    "DatabaseId",
    "Error",
    "ExecuteSQLParameters",
    "ExecuteSQLResult",
    "GetDatabaseTableNamesParameters",
    "GetDatabaseTableNamesResult",
]
