"""Generated bindings for the CDP DeviceOrientation domain. Do not edit manually."""

from __future__ import annotations

from collections.abc import Mapping
from typing import overload

from typing_extensions import TypedDict, Unpack

from cdp.domain import Domain as BaseDomain
from cdp.types import JsonObject


class SetDeviceOrientationOverrideParameters(TypedDict):
    alpha: float
    beta: float
    gamma: float


class DeviceOrientation(BaseDomain):
    """The CDP DeviceOrientation domain."""

    domain_name = "DeviceOrientation"

    async def clearDeviceOrientationOverride(
        self,
        session_id: str | None = None,
    ) -> JsonObject:
        """Clears the overridden Device Orientation."""

        return await self._command(
            "clearDeviceOrientationOverride", None, session_id, {}
        )

    @overload
    async def setDeviceOrientationOverride(
        self,
        params: SetDeviceOrientationOverrideParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def setDeviceOrientationOverride(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetDeviceOrientationOverrideParameters],
    ) -> JsonObject: ...

    async def setDeviceOrientationOverride(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Overrides the Device Orientation."""

        return await self._command(
            "setDeviceOrientationOverride", params, session_id, kwargs
        )


__all__ = ["DeviceOrientation", "SetDeviceOrientationOverrideParameters"]
