"""Generated bindings for the CDP PWA domain. Do not edit manually."""

from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Literal, TypeAlias, cast, overload

from typing_extensions import NotRequired, TypedDict, Unpack

from cdp.domain import Domain as BaseDomain
from cdp.types import JsonObject

if TYPE_CHECKING:
    from . import target as Target


class FileHandlerAccept(TypedDict):
    mediaType: str
    fileExtensions: list[str]


class FileHandler(TypedDict):
    action: str
    accepts: list[FileHandlerAccept]
    displayName: str


DisplayMode: TypeAlias = Literal["standalone", "browser"]


class GetOsAppStateParameters(TypedDict):
    manifestId: str


class GetOsAppStateResult(TypedDict):
    badgeCount: int
    fileHandlers: list[FileHandler]


class InstallParameters(TypedDict):
    manifestId: str
    installUrlOrBundleUrl: NotRequired[str]


class UninstallParameters(TypedDict):
    manifestId: str


class LaunchParameters(TypedDict):
    manifestId: str
    url: NotRequired[str]


class LaunchResult(TypedDict):
    targetId: Target.TargetID


class LaunchFilesInAppParameters(TypedDict):
    manifestId: str
    files: list[str]


class LaunchFilesInAppResult(TypedDict):
    targetIds: list[Target.TargetID]


class OpenCurrentPageInAppParameters(TypedDict):
    manifestId: str


class ChangeAppUserSettingsParameters(TypedDict):
    manifestId: str
    linkCapturing: NotRequired[bool]
    displayMode: NotRequired[DisplayMode]


class PWA(BaseDomain):
    """This domain allows interacting with the browser to control PWAs."""

    domain_name = "PWA"

    @overload
    async def getOsAppState(
        self,
        params: GetOsAppStateParameters,
        session_id: str | None = None,
    ) -> GetOsAppStateResult: ...

    @overload
    async def getOsAppState(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[GetOsAppStateParameters],
    ) -> GetOsAppStateResult: ...

    async def getOsAppState(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> GetOsAppStateResult:
        """Returns the following OS state for the given manifest id."""

        return cast(
            GetOsAppStateResult,
            await self._command("getOsAppState", params, session_id, kwargs),
        )

    @overload
    async def install(
        self,
        params: InstallParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def install(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[InstallParameters],
    ) -> JsonObject: ...

    async def install(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Installs the given manifest identity, optionally using the given installUrlOrBundleUrl IWA-specific install description: manifestId corresponds to isolated-app:// + web_package::SignedWebBundleId File installation mode: The installUrlOrBundleUrl can be either file:// or http(s):// pointing to a signed web bundle (.swbn). In this case SignedWebBundleId must correspond to The .swbn file's signing key. Dev proxy installation mode: installUrlOrBundleUrl must be http(s):// that serves dev mode IWA. web_package::SignedWebBundleId must be of type dev proxy. The advantage of dev proxy mode is that all changes to IWA automatically will be reflected in the running app without reinstallation. To generate bundle id for proxy mode: 1. Generate 32 random bytes. 2. Add a specific suffix at the end following the documentation https://github.com/WICG/isolated-web-apps/blob/main/Scheme.md#suffix 3. Encode the entire sequence using Base32 without padding. If Chrome is not in IWA dev mode, the installation will fail, regardless of the state of the allowlist."""

        return await self._command("install", params, session_id, kwargs)

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
        """Uninstalls the given manifest_id and closes any opened app windows."""

        return await self._command("uninstall", params, session_id, kwargs)

    @overload
    async def launch(
        self,
        params: LaunchParameters,
        session_id: str | None = None,
    ) -> LaunchResult: ...

    @overload
    async def launch(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[LaunchParameters],
    ) -> LaunchResult: ...

    async def launch(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> LaunchResult:
        """Launches the installed web app, or an url in the same web app instead of the default start url if it is provided. Returns a page Target.TargetID which can be used to attach to via Target.attachToTarget or similar APIs."""

        return cast(
            LaunchResult, await self._command("launch", params, session_id, kwargs)
        )

    @overload
    async def launchFilesInApp(
        self,
        params: LaunchFilesInAppParameters,
        session_id: str | None = None,
    ) -> LaunchFilesInAppResult: ...

    @overload
    async def launchFilesInApp(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[LaunchFilesInAppParameters],
    ) -> LaunchFilesInAppResult: ...

    async def launchFilesInApp(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> LaunchFilesInAppResult:
        """Opens one or more local files from an installed web app identified by its manifestId. The web app needs to have file handlers registered to process the files. The API returns one or more page Target.TargetIDs which can be used to attach to via Target.attachToTarget or similar APIs. If some files in the parameters cannot be handled by the web app, they will be ignored. If none of the files can be handled, this API returns an error. If no files are provided as the parameter, this API also returns an error. According to the definition of the file handlers in the manifest file, one Target.TargetID may represent a page handling one or more files. The order of the returned Target.TargetIDs is not guaranteed. TODO(crbug.com/339454034): Check the existences of the input files."""

        return cast(
            LaunchFilesInAppResult,
            await self._command("launchFilesInApp", params, session_id, kwargs),
        )

    @overload
    async def openCurrentPageInApp(
        self,
        params: OpenCurrentPageInAppParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def openCurrentPageInApp(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[OpenCurrentPageInAppParameters],
    ) -> JsonObject: ...

    async def openCurrentPageInApp(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Opens the current page in its web app identified by the manifest id, needs to be called on a page target. This function returns immediately without waiting for the app to finish loading."""

        return await self._command("openCurrentPageInApp", params, session_id, kwargs)

    @overload
    async def changeAppUserSettings(
        self,
        params: ChangeAppUserSettingsParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def changeAppUserSettings(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[ChangeAppUserSettingsParameters],
    ) -> JsonObject: ...

    async def changeAppUserSettings(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Changes user settings of the web app identified by its manifestId. If the app was not installed, this command returns an error. Unset parameters will be ignored; unrecognized values will cause an error. Unlike the ones defined in the manifest files of the web apps, these settings are provided by the browser and controlled by the users, they impact the way the browser handling the web apps. See the comment of each parameter."""

        return await self._command("changeAppUserSettings", params, session_id, kwargs)


__all__ = [
    "PWA",
    "ChangeAppUserSettingsParameters",
    "DisplayMode",
    "FileHandler",
    "FileHandlerAccept",
    "GetOsAppStateParameters",
    "GetOsAppStateResult",
    "InstallParameters",
    "LaunchFilesInAppParameters",
    "LaunchFilesInAppResult",
    "LaunchParameters",
    "LaunchResult",
    "OpenCurrentPageInAppParameters",
    "UninstallParameters",
]
