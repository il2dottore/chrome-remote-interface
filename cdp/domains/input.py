"""Generated bindings for the CDP Input domain. Do not edit manually."""

from __future__ import annotations

from collections.abc import Awaitable, Mapping
from typing import Literal, TypeAlias, cast, overload

from typing_extensions import NotRequired, TypedDict, Unpack

from cdp.domain import Domain as BaseDomain, EventCallback, Unsubscribe
from cdp.types import JsonObject


class TouchPoint(TypedDict):
    x: float
    y: float
    radiusX: NotRequired[float]
    radiusY: NotRequired[float]
    rotationAngle: NotRequired[float]
    force: NotRequired[float]
    tangentialPressure: NotRequired[float]
    tiltX: NotRequired[int]
    tiltY: NotRequired[int]
    twist: NotRequired[int]
    id: NotRequired[float]


GestureSourceType: TypeAlias = Literal["default", "touch", "mouse"]

MouseButton: TypeAlias = Literal["none", "left", "middle", "right", "back", "forward"]

TimeSinceEpoch: TypeAlias = float


class DragDataItem(TypedDict):
    mimeType: str
    data: str
    title: NotRequired[str]
    baseURL: NotRequired[str]


class DragData(TypedDict):
    items: list[DragDataItem]
    files: NotRequired[list[str]]
    dragOperationsMask: int


class DispatchDragEventParameters(TypedDict):
    type: Literal["dragEnter", "dragOver", "drop", "dragCancel"]
    x: float
    y: float
    data: DragData
    modifiers: NotRequired[int]


class DispatchKeyEventParameters(TypedDict):
    type: Literal["keyDown", "keyUp", "rawKeyDown", "char"]
    modifiers: NotRequired[int]
    timestamp: NotRequired[TimeSinceEpoch]
    text: NotRequired[str]
    unmodifiedText: NotRequired[str]
    keyIdentifier: NotRequired[str]
    code: NotRequired[str]
    key: NotRequired[str]
    windowsVirtualKeyCode: NotRequired[int]
    nativeVirtualKeyCode: NotRequired[int]
    autoRepeat: NotRequired[bool]
    isKeypad: NotRequired[bool]
    isSystemKey: NotRequired[bool]
    location: NotRequired[int]
    commands: NotRequired[list[str]]


class InsertTextParameters(TypedDict):
    text: str


class ImeSetCompositionParameters(TypedDict):
    text: str
    selectionStart: int
    selectionEnd: int
    replacementStart: NotRequired[int]
    replacementEnd: NotRequired[int]


class DispatchMouseEventParameters(TypedDict):
    type: Literal["mousePressed", "mouseReleased", "mouseMoved", "mouseWheel"]
    x: float
    y: float
    modifiers: NotRequired[int]
    timestamp: NotRequired[TimeSinceEpoch]
    button: NotRequired[MouseButton]
    buttons: NotRequired[int]
    clickCount: NotRequired[int]
    force: NotRequired[float]
    tangentialPressure: NotRequired[float]
    tiltX: NotRequired[int]
    tiltY: NotRequired[int]
    twist: NotRequired[int]
    deltaX: NotRequired[float]
    deltaY: NotRequired[float]
    pointerType: NotRequired[Literal["mouse", "pen"]]


class DispatchTouchEventParameters(TypedDict):
    type: Literal["touchStart", "touchEnd", "touchMove", "touchCancel"]
    touchPoints: list[TouchPoint]
    modifiers: NotRequired[int]
    timestamp: NotRequired[TimeSinceEpoch]


class EmulateTouchFromMouseEventParameters(TypedDict):
    type: Literal["mousePressed", "mouseReleased", "mouseMoved", "mouseWheel"]
    x: int
    y: int
    button: MouseButton
    timestamp: NotRequired[TimeSinceEpoch]
    deltaX: NotRequired[float]
    deltaY: NotRequired[float]
    modifiers: NotRequired[int]
    clickCount: NotRequired[int]


class SetIgnoreInputEventsParameters(TypedDict):
    ignore: bool


class SetInterceptDragsParameters(TypedDict):
    enabled: bool


class SynthesizePinchGestureParameters(TypedDict):
    x: float
    y: float
    scaleFactor: float
    relativeSpeed: NotRequired[int]
    gestureSourceType: NotRequired[GestureSourceType]


class SynthesizeScrollGestureParameters(TypedDict):
    x: float
    y: float
    xDistance: NotRequired[float]
    yDistance: NotRequired[float]
    xOverscroll: NotRequired[float]
    yOverscroll: NotRequired[float]
    preventFling: NotRequired[bool]
    speed: NotRequired[int]
    gestureSourceType: NotRequired[GestureSourceType]
    repeatCount: NotRequired[int]
    repeatDelayMs: NotRequired[int]
    interactionMarkerName: NotRequired[str]


class SynthesizeTapGestureParameters(TypedDict):
    x: float
    y: float
    duration: NotRequired[int]
    tapCount: NotRequired[int]
    gestureSourceType: NotRequired[GestureSourceType]


class DragInterceptedEvent(TypedDict):
    data: DragData


class Input(BaseDomain):
    """The CDP Input domain."""

    domain_name = "Input"

    @overload
    async def dispatchDragEvent(
        self,
        params: DispatchDragEventParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def dispatchDragEvent(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[DispatchDragEventParameters],
    ) -> JsonObject: ...

    async def dispatchDragEvent(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Dispatches a drag event into the page."""

        return await self._command("dispatchDragEvent", params, session_id, kwargs)

    @overload
    async def dispatchKeyEvent(
        self,
        params: DispatchKeyEventParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def dispatchKeyEvent(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[DispatchKeyEventParameters],
    ) -> JsonObject: ...

    async def dispatchKeyEvent(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Dispatches a key event to the page."""

        return await self._command("dispatchKeyEvent", params, session_id, kwargs)

    @overload
    async def insertText(
        self,
        params: InsertTextParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def insertText(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[InsertTextParameters],
    ) -> JsonObject: ...

    async def insertText(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """This method emulates inserting text that doesn't come from a key press, for example an emoji keyboard or an IME."""

        return await self._command("insertText", params, session_id, kwargs)

    @overload
    async def imeSetComposition(
        self,
        params: ImeSetCompositionParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def imeSetComposition(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[ImeSetCompositionParameters],
    ) -> JsonObject: ...

    async def imeSetComposition(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """This method sets the current candidate text for ime. Use imeCommitComposition to commit the final text. Use imeSetComposition with empty string as text to cancel composition."""

        return await self._command("imeSetComposition", params, session_id, kwargs)

    @overload
    async def dispatchMouseEvent(
        self,
        params: DispatchMouseEventParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def dispatchMouseEvent(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[DispatchMouseEventParameters],
    ) -> JsonObject: ...

    async def dispatchMouseEvent(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Dispatches a mouse event to the page."""

        return await self._command("dispatchMouseEvent", params, session_id, kwargs)

    @overload
    async def dispatchTouchEvent(
        self,
        params: DispatchTouchEventParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def dispatchTouchEvent(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[DispatchTouchEventParameters],
    ) -> JsonObject: ...

    async def dispatchTouchEvent(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Dispatches a touch event to the page."""

        return await self._command("dispatchTouchEvent", params, session_id, kwargs)

    async def cancelDragging(
        self,
        session_id: str | None = None,
    ) -> JsonObject:
        """Cancels any active dragging in the page."""

        return await self._command("cancelDragging", None, session_id, {})

    @overload
    async def emulateTouchFromMouseEvent(
        self,
        params: EmulateTouchFromMouseEventParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def emulateTouchFromMouseEvent(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[EmulateTouchFromMouseEventParameters],
    ) -> JsonObject: ...

    async def emulateTouchFromMouseEvent(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Emulates touch event from the mouse event parameters."""

        return await self._command(
            "emulateTouchFromMouseEvent", params, session_id, kwargs
        )

    @overload
    async def setIgnoreInputEvents(
        self,
        params: SetIgnoreInputEventsParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def setIgnoreInputEvents(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetIgnoreInputEventsParameters],
    ) -> JsonObject: ...

    async def setIgnoreInputEvents(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Ignores input events (useful while auditing page)."""

        return await self._command("setIgnoreInputEvents", params, session_id, kwargs)

    @overload
    async def setInterceptDrags(
        self,
        params: SetInterceptDragsParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def setInterceptDrags(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetInterceptDragsParameters],
    ) -> JsonObject: ...

    async def setInterceptDrags(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Prevents default drag and drop behavior and instead emits `Input.dragIntercepted` events. Drag and drop behavior can be directly controlled via `Input.dispatchDragEvent`."""

        return await self._command("setInterceptDrags", params, session_id, kwargs)

    @overload
    async def synthesizePinchGesture(
        self,
        params: SynthesizePinchGestureParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def synthesizePinchGesture(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SynthesizePinchGestureParameters],
    ) -> JsonObject: ...

    async def synthesizePinchGesture(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Synthesizes a pinch gesture over a time period by issuing appropriate touch events."""

        return await self._command("synthesizePinchGesture", params, session_id, kwargs)

    @overload
    async def synthesizeScrollGesture(
        self,
        params: SynthesizeScrollGestureParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def synthesizeScrollGesture(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SynthesizeScrollGestureParameters],
    ) -> JsonObject: ...

    async def synthesizeScrollGesture(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Synthesizes a scroll gesture over a time period by issuing appropriate touch events."""

        return await self._command(
            "synthesizeScrollGesture", params, session_id, kwargs
        )

    @overload
    async def synthesizeTapGesture(
        self,
        params: SynthesizeTapGestureParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def synthesizeTapGesture(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SynthesizeTapGestureParameters],
    ) -> JsonObject: ...

    async def synthesizeTapGesture(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Synthesizes a tap gesture over a time period by issuing appropriate touch events."""

        return await self._command("synthesizeTapGesture", params, session_id, kwargs)

    @overload
    def dragIntercepted(
        self,
        callback_or_session: EventCallback[DragInterceptedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def dragIntercepted(
        self,
        callback_or_session: str,
        handler: EventCallback[DragInterceptedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def dragIntercepted(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[DragInterceptedEvent]: ...

    def dragIntercepted(
        self,
        callback_or_session: EventCallback[DragInterceptedEvent] | str | None = None,
        handler: EventCallback[DragInterceptedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[DragInterceptedEvent] | Unsubscribe:
        """Emitted only when `Input.setInterceptDrags` is enabled. Use this data with `Input.dispatchDragEvent` to restore normal drag and drop behavior."""

        return cast(
            Awaitable[DragInterceptedEvent] | Unsubscribe,
            self._event(
                "dragIntercepted",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )


__all__ = [
    "DispatchDragEventParameters",
    "DispatchKeyEventParameters",
    "DispatchMouseEventParameters",
    "DispatchTouchEventParameters",
    "DragData",
    "DragDataItem",
    "DragInterceptedEvent",
    "EmulateTouchFromMouseEventParameters",
    "GestureSourceType",
    "ImeSetCompositionParameters",
    "Input",
    "InsertTextParameters",
    "MouseButton",
    "SetIgnoreInputEventsParameters",
    "SetInterceptDragsParameters",
    "SynthesizePinchGestureParameters",
    "SynthesizeScrollGestureParameters",
    "SynthesizeTapGestureParameters",
    "TimeSinceEpoch",
    "TouchPoint",
]
