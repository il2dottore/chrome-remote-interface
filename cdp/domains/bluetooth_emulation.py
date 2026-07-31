"""Generated bindings for the CDP BluetoothEmulation domain. Do not edit manually."""

from __future__ import annotations

from collections.abc import Awaitable, Mapping
from typing import Literal, TypeAlias, cast, overload

from typing_extensions import NotRequired, TypedDict, Unpack

from cdp.domain import Domain as BaseDomain, EventCallback, Unsubscribe
from cdp.types import JsonObject


CentralState: TypeAlias = Literal["absent", "powered-off", "powered-on"]

GATTOperationType: TypeAlias = Literal["connection", "discovery"]

CharacteristicWriteType: TypeAlias = Literal[
    "write-default-deprecated", "write-with-response", "write-without-response"
]

CharacteristicOperationType: TypeAlias = Literal[
    "read", "write", "subscribe-to-notifications", "unsubscribe-from-notifications"
]

DescriptorOperationType: TypeAlias = Literal["read", "write"]


class ManufacturerData(TypedDict):
    key: int
    data: str


class ScanRecord(TypedDict):
    name: NotRequired[str]
    uuids: NotRequired[list[str]]
    appearance: NotRequired[int]
    txPower: NotRequired[int]
    manufacturerData: NotRequired[list[ManufacturerData]]


class ScanEntry(TypedDict):
    deviceAddress: str
    rssi: int
    scanRecord: ScanRecord


class CharacteristicProperties(TypedDict):
    broadcast: NotRequired[bool]
    read: NotRequired[bool]
    writeWithoutResponse: NotRequired[bool]
    write: NotRequired[bool]
    notify: NotRequired[bool]
    indicate: NotRequired[bool]
    authenticatedSignedWrites: NotRequired[bool]
    extendedProperties: NotRequired[bool]


class EnableParameters(TypedDict):
    state: CentralState
    leSupported: bool


class SetSimulatedCentralStateParameters(TypedDict):
    state: CentralState


class SimulatePreconnectedPeripheralParameters(TypedDict):
    address: str
    name: str
    manufacturerData: list[ManufacturerData]
    knownServiceUuids: list[str]


class SimulateAdvertisementParameters(TypedDict):
    entry: ScanEntry


class SimulateGATTOperationResponseParameters(TypedDict):
    address: str
    type: GATTOperationType
    code: int


class SimulateCharacteristicOperationResponseParameters(TypedDict):
    characteristicId: str
    type: CharacteristicOperationType
    code: int
    data: NotRequired[str]


class SimulateDescriptorOperationResponseParameters(TypedDict):
    descriptorId: str
    type: DescriptorOperationType
    code: int
    data: NotRequired[str]


class AddServiceParameters(TypedDict):
    address: str
    serviceUuid: str


class AddServiceResult(TypedDict):
    serviceId: str


class RemoveServiceParameters(TypedDict):
    serviceId: str


class AddCharacteristicParameters(TypedDict):
    serviceId: str
    characteristicUuid: str
    properties: CharacteristicProperties


class AddCharacteristicResult(TypedDict):
    characteristicId: str


class RemoveCharacteristicParameters(TypedDict):
    characteristicId: str


class AddDescriptorParameters(TypedDict):
    characteristicId: str
    descriptorUuid: str


class AddDescriptorResult(TypedDict):
    descriptorId: str


class RemoveDescriptorParameters(TypedDict):
    descriptorId: str


class SimulateGATTDisconnectionParameters(TypedDict):
    address: str


class GattOperationReceivedEvent(TypedDict):
    address: str
    type: GATTOperationType


class CharacteristicOperationReceivedEvent(TypedDict):
    characteristicId: str
    type: CharacteristicOperationType
    data: NotRequired[str]
    writeType: NotRequired[CharacteristicWriteType]


class DescriptorOperationReceivedEvent(TypedDict):
    descriptorId: str
    type: DescriptorOperationType
    data: NotRequired[str]


class BluetoothEmulation(BaseDomain):
    """This domain allows configuring virtual Bluetooth devices to test the web-bluetooth API."""

    domain_name = "BluetoothEmulation"

    @overload
    async def enable(
        self,
        params: EnableParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def enable(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[EnableParameters],
    ) -> JsonObject: ...

    async def enable(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Enable the BluetoothEmulation domain."""

        return await self._command("enable", params, session_id, kwargs)

    @overload
    async def setSimulatedCentralState(
        self,
        params: SetSimulatedCentralStateParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def setSimulatedCentralState(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetSimulatedCentralStateParameters],
    ) -> JsonObject: ...

    async def setSimulatedCentralState(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Set the state of the simulated central."""

        return await self._command(
            "setSimulatedCentralState", params, session_id, kwargs
        )

    async def disable(
        self,
        session_id: str | None = None,
    ) -> JsonObject:
        """Disable the BluetoothEmulation domain."""

        return await self._command("disable", None, session_id, {})

    @overload
    async def simulatePreconnectedPeripheral(
        self,
        params: SimulatePreconnectedPeripheralParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def simulatePreconnectedPeripheral(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SimulatePreconnectedPeripheralParameters],
    ) -> JsonObject: ...

    async def simulatePreconnectedPeripheral(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Simulates a peripheral with |address|, |name| and |knownServiceUuids| that has already been connected to the system."""

        return await self._command(
            "simulatePreconnectedPeripheral", params, session_id, kwargs
        )

    @overload
    async def simulateAdvertisement(
        self,
        params: SimulateAdvertisementParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def simulateAdvertisement(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SimulateAdvertisementParameters],
    ) -> JsonObject: ...

    async def simulateAdvertisement(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Simulates an advertisement packet described in |entry| being received by the central."""

        return await self._command("simulateAdvertisement", params, session_id, kwargs)

    @overload
    async def simulateGATTOperationResponse(
        self,
        params: SimulateGATTOperationResponseParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def simulateGATTOperationResponse(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SimulateGATTOperationResponseParameters],
    ) -> JsonObject: ...

    async def simulateGATTOperationResponse(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Simulates the response code from the peripheral with |address| for a GATT operation of |type|. The |code| value follows the HCI Error Codes from Bluetooth Core Specification Vol 2 Part D 1.3 List Of Error Codes."""

        return await self._command(
            "simulateGATTOperationResponse", params, session_id, kwargs
        )

    @overload
    async def simulateCharacteristicOperationResponse(
        self,
        params: SimulateCharacteristicOperationResponseParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def simulateCharacteristicOperationResponse(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SimulateCharacteristicOperationResponseParameters],
    ) -> JsonObject: ...

    async def simulateCharacteristicOperationResponse(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Simulates the response from the characteristic with |characteristicId| for a characteristic operation of |type|. The |code| value follows the Error Codes from Bluetooth Core Specification Vol 3 Part F 3.4.1.1 Error Response. The |data| is expected to exist when simulating a successful read operation response."""

        return await self._command(
            "simulateCharacteristicOperationResponse", params, session_id, kwargs
        )

    @overload
    async def simulateDescriptorOperationResponse(
        self,
        params: SimulateDescriptorOperationResponseParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def simulateDescriptorOperationResponse(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SimulateDescriptorOperationResponseParameters],
    ) -> JsonObject: ...

    async def simulateDescriptorOperationResponse(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Simulates the response from the descriptor with |descriptorId| for a descriptor operation of |type|. The |code| value follows the Error Codes from Bluetooth Core Specification Vol 3 Part F 3.4.1.1 Error Response. The |data| is expected to exist when simulating a successful read operation response."""

        return await self._command(
            "simulateDescriptorOperationResponse", params, session_id, kwargs
        )

    @overload
    async def addService(
        self,
        params: AddServiceParameters,
        session_id: str | None = None,
    ) -> AddServiceResult: ...

    @overload
    async def addService(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[AddServiceParameters],
    ) -> AddServiceResult: ...

    async def addService(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> AddServiceResult:
        """Adds a service with |serviceUuid| to the peripheral with |address|."""

        return cast(
            AddServiceResult,
            await self._command("addService", params, session_id, kwargs),
        )

    @overload
    async def removeService(
        self,
        params: RemoveServiceParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def removeService(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[RemoveServiceParameters],
    ) -> JsonObject: ...

    async def removeService(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Removes the service respresented by |serviceId| from the simulated central."""

        return await self._command("removeService", params, session_id, kwargs)

    @overload
    async def addCharacteristic(
        self,
        params: AddCharacteristicParameters,
        session_id: str | None = None,
    ) -> AddCharacteristicResult: ...

    @overload
    async def addCharacteristic(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[AddCharacteristicParameters],
    ) -> AddCharacteristicResult: ...

    async def addCharacteristic(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> AddCharacteristicResult:
        """Adds a characteristic with |characteristicUuid| and |properties| to the service represented by |serviceId|."""

        return cast(
            AddCharacteristicResult,
            await self._command("addCharacteristic", params, session_id, kwargs),
        )

    @overload
    async def removeCharacteristic(
        self,
        params: RemoveCharacteristicParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def removeCharacteristic(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[RemoveCharacteristicParameters],
    ) -> JsonObject: ...

    async def removeCharacteristic(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Removes the characteristic respresented by |characteristicId| from the simulated central."""

        return await self._command("removeCharacteristic", params, session_id, kwargs)

    @overload
    async def addDescriptor(
        self,
        params: AddDescriptorParameters,
        session_id: str | None = None,
    ) -> AddDescriptorResult: ...

    @overload
    async def addDescriptor(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[AddDescriptorParameters],
    ) -> AddDescriptorResult: ...

    async def addDescriptor(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> AddDescriptorResult:
        """Adds a descriptor with |descriptorUuid| to the characteristic respresented by |characteristicId|."""

        return cast(
            AddDescriptorResult,
            await self._command("addDescriptor", params, session_id, kwargs),
        )

    @overload
    async def removeDescriptor(
        self,
        params: RemoveDescriptorParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def removeDescriptor(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[RemoveDescriptorParameters],
    ) -> JsonObject: ...

    async def removeDescriptor(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Removes the descriptor with |descriptorId| from the simulated central."""

        return await self._command("removeDescriptor", params, session_id, kwargs)

    @overload
    async def simulateGATTDisconnection(
        self,
        params: SimulateGATTDisconnectionParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def simulateGATTDisconnection(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SimulateGATTDisconnectionParameters],
    ) -> JsonObject: ...

    async def simulateGATTDisconnection(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Simulates a GATT disconnection from the peripheral with |address|."""

        return await self._command(
            "simulateGATTDisconnection", params, session_id, kwargs
        )

    @overload
    def gattOperationReceived(
        self,
        callback_or_session: EventCallback[GattOperationReceivedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def gattOperationReceived(
        self,
        callback_or_session: str,
        handler: EventCallback[GattOperationReceivedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def gattOperationReceived(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[GattOperationReceivedEvent]: ...

    def gattOperationReceived(
        self,
        callback_or_session: EventCallback[GattOperationReceivedEvent]
        | str
        | None = None,
        handler: EventCallback[GattOperationReceivedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[GattOperationReceivedEvent] | Unsubscribe:
        """Event for when a GATT operation of |type| to the peripheral with |address| happened."""

        return cast(
            Awaitable[GattOperationReceivedEvent] | Unsubscribe,
            self._event(
                "gattOperationReceived",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def characteristicOperationReceived(
        self,
        callback_or_session: EventCallback[CharacteristicOperationReceivedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def characteristicOperationReceived(
        self,
        callback_or_session: str,
        handler: EventCallback[CharacteristicOperationReceivedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def characteristicOperationReceived(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[CharacteristicOperationReceivedEvent]: ...

    def characteristicOperationReceived(
        self,
        callback_or_session: EventCallback[CharacteristicOperationReceivedEvent]
        | str
        | None = None,
        handler: EventCallback[CharacteristicOperationReceivedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[CharacteristicOperationReceivedEvent] | Unsubscribe:
        """Event for when a characteristic operation of |type| to the characteristic respresented by |characteristicId| happened. |data| and |writeType| is expected to exist when |type| is write."""

        return cast(
            Awaitable[CharacteristicOperationReceivedEvent] | Unsubscribe,
            self._event(
                "characteristicOperationReceived",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def descriptorOperationReceived(
        self,
        callback_or_session: EventCallback[DescriptorOperationReceivedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def descriptorOperationReceived(
        self,
        callback_or_session: str,
        handler: EventCallback[DescriptorOperationReceivedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def descriptorOperationReceived(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[DescriptorOperationReceivedEvent]: ...

    def descriptorOperationReceived(
        self,
        callback_or_session: EventCallback[DescriptorOperationReceivedEvent]
        | str
        | None = None,
        handler: EventCallback[DescriptorOperationReceivedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[DescriptorOperationReceivedEvent] | Unsubscribe:
        """Event for when a descriptor operation of |type| to the descriptor respresented by |descriptorId| happened. |data| is expected to exist when |type| is write."""

        return cast(
            Awaitable[DescriptorOperationReceivedEvent] | Unsubscribe,
            self._event(
                "descriptorOperationReceived",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )


__all__ = [
    "AddCharacteristicParameters",
    "AddCharacteristicResult",
    "AddDescriptorParameters",
    "AddDescriptorResult",
    "AddServiceParameters",
    "AddServiceResult",
    "BluetoothEmulation",
    "CentralState",
    "CharacteristicOperationReceivedEvent",
    "CharacteristicOperationType",
    "CharacteristicProperties",
    "CharacteristicWriteType",
    "DescriptorOperationReceivedEvent",
    "DescriptorOperationType",
    "EnableParameters",
    "GATTOperationType",
    "GattOperationReceivedEvent",
    "ManufacturerData",
    "RemoveCharacteristicParameters",
    "RemoveDescriptorParameters",
    "RemoveServiceParameters",
    "ScanEntry",
    "ScanRecord",
    "SetSimulatedCentralStateParameters",
    "SimulateAdvertisementParameters",
    "SimulateCharacteristicOperationResponseParameters",
    "SimulateDescriptorOperationResponseParameters",
    "SimulateGATTDisconnectionParameters",
    "SimulateGATTOperationResponseParameters",
    "SimulatePreconnectedPeripheralParameters",
]
