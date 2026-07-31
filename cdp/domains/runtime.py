"""Generated bindings for the CDP Runtime domain. Do not edit manually."""

from __future__ import annotations

from collections.abc import Awaitable, Mapping
from typing import Literal, TypeAlias, cast, overload

from typing_extensions import NotRequired, TypedDict, Unpack

from cdp.domain import Domain as BaseDomain, EventCallback, Unsubscribe
from cdp.types import JsonObject, JsonValue


ScriptId: TypeAlias = str


class SerializationOptions(TypedDict):
    serialization: Literal["deep", "json", "idOnly"]
    maxDepth: NotRequired[int]
    additionalParameters: NotRequired[JsonObject]


class DeepSerializedValue(TypedDict):
    type: Literal[
        "undefined",
        "null",
        "string",
        "number",
        "boolean",
        "bigint",
        "regexp",
        "date",
        "symbol",
        "array",
        "object",
        "function",
        "map",
        "set",
        "weakmap",
        "weakset",
        "error",
        "proxy",
        "promise",
        "typedarray",
        "arraybuffer",
        "node",
        "window",
    ]
    value: NotRequired[JsonValue]
    objectId: NotRequired[str]
    weakLocalObjectReference: NotRequired[int]


RemoteObjectId: TypeAlias = str

UnserializableValue: TypeAlias = str


class RemoteObject(TypedDict):
    type: Literal[
        "object",
        "function",
        "undefined",
        "string",
        "number",
        "boolean",
        "symbol",
        "bigint",
    ]
    subtype: NotRequired[
        Literal[
            "array",
            "null",
            "node",
            "regexp",
            "date",
            "map",
            "set",
            "weakmap",
            "weakset",
            "iterator",
            "generator",
            "error",
            "proxy",
            "promise",
            "typedarray",
            "arraybuffer",
            "dataview",
            "webassemblymemory",
            "wasmvalue",
        ]
    ]
    className: NotRequired[str]
    value: NotRequired[JsonValue]
    unserializableValue: NotRequired[UnserializableValue]
    description: NotRequired[str]
    webDriverValue: NotRequired[DeepSerializedValue]
    deepSerializedValue: NotRequired[DeepSerializedValue]
    objectId: NotRequired[RemoteObjectId]
    preview: NotRequired[ObjectPreview]
    customPreview: NotRequired[CustomPreview]


class CustomPreview(TypedDict):
    header: str
    bodyGetterId: NotRequired[RemoteObjectId]


class ObjectPreview(TypedDict):
    type: Literal[
        "object",
        "function",
        "undefined",
        "string",
        "number",
        "boolean",
        "symbol",
        "bigint",
    ]
    subtype: NotRequired[
        Literal[
            "array",
            "null",
            "node",
            "regexp",
            "date",
            "map",
            "set",
            "weakmap",
            "weakset",
            "iterator",
            "generator",
            "error",
            "proxy",
            "promise",
            "typedarray",
            "arraybuffer",
            "dataview",
            "webassemblymemory",
            "wasmvalue",
        ]
    ]
    description: NotRequired[str]
    overflow: bool
    properties: list[PropertyPreview]
    entries: NotRequired[list[EntryPreview]]


class PropertyPreview(TypedDict):
    name: str
    type: Literal[
        "object",
        "function",
        "undefined",
        "string",
        "number",
        "boolean",
        "symbol",
        "accessor",
        "bigint",
    ]
    value: NotRequired[str]
    valuePreview: NotRequired[ObjectPreview]
    subtype: NotRequired[
        Literal[
            "array",
            "null",
            "node",
            "regexp",
            "date",
            "map",
            "set",
            "weakmap",
            "weakset",
            "iterator",
            "generator",
            "error",
            "proxy",
            "promise",
            "typedarray",
            "arraybuffer",
            "dataview",
            "webassemblymemory",
            "wasmvalue",
        ]
    ]


class EntryPreview(TypedDict):
    key: NotRequired[ObjectPreview]
    value: ObjectPreview


class PropertyDescriptor(TypedDict):
    name: str
    value: NotRequired[RemoteObject]
    writable: NotRequired[bool]
    get: NotRequired[RemoteObject]
    set: NotRequired[RemoteObject]
    configurable: bool
    enumerable: bool
    wasThrown: NotRequired[bool]
    isOwn: NotRequired[bool]
    symbol: NotRequired[RemoteObject]


class InternalPropertyDescriptor(TypedDict):
    name: str
    value: NotRequired[RemoteObject]


class PrivatePropertyDescriptor(TypedDict):
    name: str
    value: NotRequired[RemoteObject]
    get: NotRequired[RemoteObject]
    set: NotRequired[RemoteObject]


class CallArgument(TypedDict):
    value: NotRequired[JsonValue]
    unserializableValue: NotRequired[UnserializableValue]
    objectId: NotRequired[RemoteObjectId]


ExecutionContextId: TypeAlias = int


class ExecutionContextDescription(TypedDict):
    id: ExecutionContextId
    origin: str
    name: str
    uniqueId: str
    auxData: NotRequired[JsonObject]


class ExceptionDetails(TypedDict):
    exceptionId: int
    text: str
    lineNumber: int
    columnNumber: int
    scriptId: NotRequired[ScriptId]
    url: NotRequired[str]
    stackTrace: NotRequired[StackTrace]
    exception: NotRequired[RemoteObject]
    executionContextId: NotRequired[ExecutionContextId]
    exceptionMetaData: NotRequired[JsonObject]


Timestamp: TypeAlias = float

TimeDelta: TypeAlias = float


class CallFrame(TypedDict):
    functionName: str
    scriptId: ScriptId
    url: str
    lineNumber: int
    columnNumber: int


class StackTrace(TypedDict):
    description: NotRequired[str]
    callFrames: list[CallFrame]
    parent: NotRequired[StackTrace]
    parentId: NotRequired[StackTraceId]


UniqueDebuggerId: TypeAlias = str


class StackTraceId(TypedDict):
    id: str
    debuggerId: NotRequired[UniqueDebuggerId]


class AwaitPromiseParameters(TypedDict):
    promiseObjectId: RemoteObjectId
    returnByValue: NotRequired[bool]
    generatePreview: NotRequired[bool]


class AwaitPromiseResult(TypedDict):
    result: RemoteObject
    exceptionDetails: NotRequired[ExceptionDetails]


class CallFunctionOnParameters(TypedDict):
    functionDeclaration: str
    objectId: NotRequired[RemoteObjectId]
    arguments: NotRequired[list[CallArgument]]
    silent: NotRequired[bool]
    returnByValue: NotRequired[bool]
    generatePreview: NotRequired[bool]
    userGesture: NotRequired[bool]
    awaitPromise: NotRequired[bool]
    executionContextId: NotRequired[ExecutionContextId]
    objectGroup: NotRequired[str]
    throwOnSideEffect: NotRequired[bool]
    uniqueContextId: NotRequired[str]
    generateWebDriverValue: NotRequired[bool]
    serializationOptions: NotRequired[SerializationOptions]


class CallFunctionOnResult(TypedDict):
    result: RemoteObject
    exceptionDetails: NotRequired[ExceptionDetails]


class CompileScriptParameters(TypedDict):
    expression: str
    sourceURL: str
    persistScript: bool
    executionContextId: NotRequired[ExecutionContextId]


class CompileScriptResult(TypedDict):
    scriptId: NotRequired[ScriptId]
    exceptionDetails: NotRequired[ExceptionDetails]


class EvaluateParameters(TypedDict):
    expression: str
    objectGroup: NotRequired[str]
    includeCommandLineAPI: NotRequired[bool]
    silent: NotRequired[bool]
    contextId: NotRequired[ExecutionContextId]
    returnByValue: NotRequired[bool]
    generatePreview: NotRequired[bool]
    userGesture: NotRequired[bool]
    awaitPromise: NotRequired[bool]
    throwOnSideEffect: NotRequired[bool]
    timeout: NotRequired[TimeDelta]
    disableBreaks: NotRequired[bool]
    replMode: NotRequired[bool]
    allowUnsafeEvalBlockedByCSP: NotRequired[bool]
    uniqueContextId: NotRequired[str]
    generateWebDriverValue: NotRequired[bool]
    serializationOptions: NotRequired[SerializationOptions]


class EvaluateResult(TypedDict):
    result: RemoteObject
    exceptionDetails: NotRequired[ExceptionDetails]


class GetIsolateIdResult(TypedDict):
    id: str


class GetHeapUsageResult(TypedDict):
    usedSize: float
    totalSize: float


class GetPropertiesParameters(TypedDict):
    objectId: RemoteObjectId
    ownProperties: NotRequired[bool]
    accessorPropertiesOnly: NotRequired[bool]
    generatePreview: NotRequired[bool]
    nonIndexedPropertiesOnly: NotRequired[bool]


class GetPropertiesResult(TypedDict):
    result: list[PropertyDescriptor]
    internalProperties: NotRequired[list[InternalPropertyDescriptor]]
    privateProperties: NotRequired[list[PrivatePropertyDescriptor]]
    exceptionDetails: NotRequired[ExceptionDetails]


class GlobalLexicalScopeNamesParameters(TypedDict):
    executionContextId: NotRequired[ExecutionContextId]


class GlobalLexicalScopeNamesResult(TypedDict):
    names: list[str]


class QueryObjectsParameters(TypedDict):
    prototypeObjectId: RemoteObjectId
    objectGroup: NotRequired[str]


class QueryObjectsResult(TypedDict):
    objects: RemoteObject


class ReleaseObjectParameters(TypedDict):
    objectId: RemoteObjectId


class ReleaseObjectGroupParameters(TypedDict):
    objectGroup: str


class RunScriptParameters(TypedDict):
    scriptId: ScriptId
    executionContextId: NotRequired[ExecutionContextId]
    objectGroup: NotRequired[str]
    silent: NotRequired[bool]
    includeCommandLineAPI: NotRequired[bool]
    returnByValue: NotRequired[bool]
    generatePreview: NotRequired[bool]
    awaitPromise: NotRequired[bool]


class RunScriptResult(TypedDict):
    result: RemoteObject
    exceptionDetails: NotRequired[ExceptionDetails]


class SetAsyncCallStackDepthParameters(TypedDict):
    maxDepth: int


class SetCustomObjectFormatterEnabledParameters(TypedDict):
    enabled: bool


class SetMaxCallStackSizeToCaptureParameters(TypedDict):
    size: int


class AddBindingParameters(TypedDict):
    name: str
    executionContextId: NotRequired[ExecutionContextId]
    executionContextName: NotRequired[str]


class RemoveBindingParameters(TypedDict):
    name: str


class GetExceptionDetailsParameters(TypedDict):
    errorObjectId: RemoteObjectId


class GetExceptionDetailsResult(TypedDict):
    exceptionDetails: NotRequired[ExceptionDetails]


class BindingCalledEvent(TypedDict):
    name: str
    payload: str
    executionContextId: ExecutionContextId


class ConsoleAPICalledEvent(TypedDict):
    type: Literal[
        "log",
        "debug",
        "info",
        "error",
        "warning",
        "dir",
        "dirxml",
        "table",
        "trace",
        "clear",
        "startGroup",
        "startGroupCollapsed",
        "endGroup",
        "assert",
        "profile",
        "profileEnd",
        "count",
        "timeEnd",
    ]
    args: list[RemoteObject]
    executionContextId: ExecutionContextId
    timestamp: Timestamp
    stackTrace: NotRequired[StackTrace]
    context: NotRequired[str]


class ExceptionRevokedEvent(TypedDict):
    reason: str
    exceptionId: int


class ExceptionThrownEvent(TypedDict):
    timestamp: Timestamp
    exceptionDetails: ExceptionDetails


class ExecutionContextCreatedEvent(TypedDict):
    context: ExecutionContextDescription


class ExecutionContextDestroyedEvent(TypedDict):
    executionContextId: ExecutionContextId
    executionContextUniqueId: str


class InspectRequestedEvent(TypedDict):
    object: RemoteObject
    hints: JsonObject
    executionContextId: NotRequired[ExecutionContextId]


class Runtime(BaseDomain):
    """Runtime domain exposes JavaScript runtime by means of remote evaluation and mirror objects. Evaluation results are returned as mirror object that expose object type, string representation and unique identifier that can be used for further object reference. Original objects are maintained in memory unless they are either explicitly released or are released along with the other objects in their object group."""

    domain_name = "Runtime"

    @overload
    async def awaitPromise(
        self,
        params: AwaitPromiseParameters,
        session_id: str | None = None,
    ) -> AwaitPromiseResult: ...

    @overload
    async def awaitPromise(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[AwaitPromiseParameters],
    ) -> AwaitPromiseResult: ...

    async def awaitPromise(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> AwaitPromiseResult:
        """Add handler to promise with given promise object id."""

        return cast(
            AwaitPromiseResult,
            await self._command("awaitPromise", params, session_id, kwargs),
        )

    @overload
    async def callFunctionOn(
        self,
        params: CallFunctionOnParameters,
        session_id: str | None = None,
    ) -> CallFunctionOnResult: ...

    @overload
    async def callFunctionOn(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[CallFunctionOnParameters],
    ) -> CallFunctionOnResult: ...

    async def callFunctionOn(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> CallFunctionOnResult:
        """Calls function with given declaration on the given object. Object group of the result is inherited from the target object."""

        return cast(
            CallFunctionOnResult,
            await self._command("callFunctionOn", params, session_id, kwargs),
        )

    @overload
    async def compileScript(
        self,
        params: CompileScriptParameters,
        session_id: str | None = None,
    ) -> CompileScriptResult: ...

    @overload
    async def compileScript(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[CompileScriptParameters],
    ) -> CompileScriptResult: ...

    async def compileScript(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> CompileScriptResult:
        """Compiles expression."""

        return cast(
            CompileScriptResult,
            await self._command("compileScript", params, session_id, kwargs),
        )

    async def disable(
        self,
        session_id: str | None = None,
    ) -> JsonObject:
        """Disables reporting of execution contexts creation."""

        return await self._command("disable", None, session_id, {})

    async def discardConsoleEntries(
        self,
        session_id: str | None = None,
    ) -> JsonObject:
        """Discards collected exceptions and console API calls."""

        return await self._command("discardConsoleEntries", None, session_id, {})

    async def enable(
        self,
        session_id: str | None = None,
    ) -> JsonObject:
        """Enables reporting of execution contexts creation by means of `executionContextCreated` event. When the reporting gets enabled the event will be sent immediately for each existing execution context."""

        return await self._command("enable", None, session_id, {})

    @overload
    async def evaluate(
        self,
        params: EvaluateParameters,
        session_id: str | None = None,
    ) -> EvaluateResult: ...

    @overload
    async def evaluate(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[EvaluateParameters],
    ) -> EvaluateResult: ...

    async def evaluate(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> EvaluateResult:
        """Evaluates expression on global object."""

        return cast(
            EvaluateResult, await self._command("evaluate", params, session_id, kwargs)
        )

    async def getIsolateId(
        self,
        session_id: str | None = None,
    ) -> GetIsolateIdResult:
        """Returns the isolate id."""

        return cast(
            GetIsolateIdResult,
            await self._command("getIsolateId", None, session_id, {}),
        )

    async def getHeapUsage(
        self,
        session_id: str | None = None,
    ) -> GetHeapUsageResult:
        """Returns the JavaScript heap usage. It is the total usage of the corresponding isolate not scoped to a particular Runtime."""

        return cast(
            GetHeapUsageResult,
            await self._command("getHeapUsage", None, session_id, {}),
        )

    @overload
    async def getProperties(
        self,
        params: GetPropertiesParameters,
        session_id: str | None = None,
    ) -> GetPropertiesResult: ...

    @overload
    async def getProperties(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[GetPropertiesParameters],
    ) -> GetPropertiesResult: ...

    async def getProperties(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> GetPropertiesResult:
        """Returns properties of a given object. Object group of the result is inherited from the target object."""

        return cast(
            GetPropertiesResult,
            await self._command("getProperties", params, session_id, kwargs),
        )

    @overload
    async def globalLexicalScopeNames(
        self,
        params: GlobalLexicalScopeNamesParameters,
        session_id: str | None = None,
    ) -> GlobalLexicalScopeNamesResult: ...

    @overload
    async def globalLexicalScopeNames(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[GlobalLexicalScopeNamesParameters],
    ) -> GlobalLexicalScopeNamesResult: ...

    async def globalLexicalScopeNames(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> GlobalLexicalScopeNamesResult:
        """Returns all let, const and class variables from global scope."""

        return cast(
            GlobalLexicalScopeNamesResult,
            await self._command("globalLexicalScopeNames", params, session_id, kwargs),
        )

    @overload
    async def queryObjects(
        self,
        params: QueryObjectsParameters,
        session_id: str | None = None,
    ) -> QueryObjectsResult: ...

    @overload
    async def queryObjects(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[QueryObjectsParameters],
    ) -> QueryObjectsResult: ...

    async def queryObjects(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> QueryObjectsResult:
        """Send Runtime.queryObjects."""

        return cast(
            QueryObjectsResult,
            await self._command("queryObjects", params, session_id, kwargs),
        )

    @overload
    async def releaseObject(
        self,
        params: ReleaseObjectParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def releaseObject(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[ReleaseObjectParameters],
    ) -> JsonObject: ...

    async def releaseObject(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Releases remote object with given id."""

        return await self._command("releaseObject", params, session_id, kwargs)

    @overload
    async def releaseObjectGroup(
        self,
        params: ReleaseObjectGroupParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def releaseObjectGroup(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[ReleaseObjectGroupParameters],
    ) -> JsonObject: ...

    async def releaseObjectGroup(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Releases all remote objects that belong to a given group."""

        return await self._command("releaseObjectGroup", params, session_id, kwargs)

    async def runIfWaitingForDebugger(
        self,
        session_id: str | None = None,
    ) -> JsonObject:
        """Tells inspected instance to run if it was waiting for debugger to attach."""

        return await self._command("runIfWaitingForDebugger", None, session_id, {})

    @overload
    async def runScript(
        self,
        params: RunScriptParameters,
        session_id: str | None = None,
    ) -> RunScriptResult: ...

    @overload
    async def runScript(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[RunScriptParameters],
    ) -> RunScriptResult: ...

    async def runScript(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> RunScriptResult:
        """Runs script with given id in a given context."""

        return cast(
            RunScriptResult,
            await self._command("runScript", params, session_id, kwargs),
        )

    @overload
    async def setAsyncCallStackDepth(
        self,
        params: SetAsyncCallStackDepthParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def setAsyncCallStackDepth(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetAsyncCallStackDepthParameters],
    ) -> JsonObject: ...

    async def setAsyncCallStackDepth(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Enables or disables async call stacks tracking."""

        return await self._command("setAsyncCallStackDepth", params, session_id, kwargs)

    @overload
    async def setCustomObjectFormatterEnabled(
        self,
        params: SetCustomObjectFormatterEnabledParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def setCustomObjectFormatterEnabled(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetCustomObjectFormatterEnabledParameters],
    ) -> JsonObject: ...

    async def setCustomObjectFormatterEnabled(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Send Runtime.setCustomObjectFormatterEnabled."""

        return await self._command(
            "setCustomObjectFormatterEnabled", params, session_id, kwargs
        )

    @overload
    async def setMaxCallStackSizeToCapture(
        self,
        params: SetMaxCallStackSizeToCaptureParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def setMaxCallStackSizeToCapture(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetMaxCallStackSizeToCaptureParameters],
    ) -> JsonObject: ...

    async def setMaxCallStackSizeToCapture(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Send Runtime.setMaxCallStackSizeToCapture."""

        return await self._command(
            "setMaxCallStackSizeToCapture", params, session_id, kwargs
        )

    async def terminateExecution(
        self,
        session_id: str | None = None,
    ) -> JsonObject:
        """Terminate current or next JavaScript execution. Will cancel the termination when the outer-most script execution ends."""

        return await self._command("terminateExecution", None, session_id, {})

    @overload
    async def addBinding(
        self,
        params: AddBindingParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def addBinding(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[AddBindingParameters],
    ) -> JsonObject: ...

    async def addBinding(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """If executionContextId is empty, adds binding with the given name on the global objects of all inspected contexts, including those created later, bindings survive reloads. Binding function takes exactly one argument, this argument should be string, in case of any other input, function throws an exception. Each binding function call produces Runtime.bindingCalled notification."""

        return await self._command("addBinding", params, session_id, kwargs)

    @overload
    async def removeBinding(
        self,
        params: RemoveBindingParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def removeBinding(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[RemoveBindingParameters],
    ) -> JsonObject: ...

    async def removeBinding(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """This method does not remove binding function from global object but unsubscribes current runtime agent from Runtime.bindingCalled notifications."""

        return await self._command("removeBinding", params, session_id, kwargs)

    @overload
    async def getExceptionDetails(
        self,
        params: GetExceptionDetailsParameters,
        session_id: str | None = None,
    ) -> GetExceptionDetailsResult: ...

    @overload
    async def getExceptionDetails(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[GetExceptionDetailsParameters],
    ) -> GetExceptionDetailsResult: ...

    async def getExceptionDetails(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> GetExceptionDetailsResult:
        """This method tries to lookup and populate exception details for a JavaScript Error object. Note that the stackTrace portion of the resulting exceptionDetails will only be populated if the Runtime domain was enabled at the time when the Error was thrown."""

        return cast(
            GetExceptionDetailsResult,
            await self._command("getExceptionDetails", params, session_id, kwargs),
        )

    @overload
    def bindingCalled(
        self,
        callback_or_session: EventCallback[BindingCalledEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def bindingCalled(
        self,
        callback_or_session: str,
        handler: EventCallback[BindingCalledEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def bindingCalled(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[BindingCalledEvent]: ...

    def bindingCalled(
        self,
        callback_or_session: EventCallback[BindingCalledEvent] | str | None = None,
        handler: EventCallback[BindingCalledEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[BindingCalledEvent] | Unsubscribe:
        """Notification is issued every time when binding is called."""

        return cast(
            Awaitable[BindingCalledEvent] | Unsubscribe,
            self._event(
                "bindingCalled",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def consoleAPICalled(
        self,
        callback_or_session: EventCallback[ConsoleAPICalledEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def consoleAPICalled(
        self,
        callback_or_session: str,
        handler: EventCallback[ConsoleAPICalledEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def consoleAPICalled(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[ConsoleAPICalledEvent]: ...

    def consoleAPICalled(
        self,
        callback_or_session: EventCallback[ConsoleAPICalledEvent] | str | None = None,
        handler: EventCallback[ConsoleAPICalledEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[ConsoleAPICalledEvent] | Unsubscribe:
        """Issued when console API was called."""

        return cast(
            Awaitable[ConsoleAPICalledEvent] | Unsubscribe,
            self._event(
                "consoleAPICalled",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def exceptionRevoked(
        self,
        callback_or_session: EventCallback[ExceptionRevokedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def exceptionRevoked(
        self,
        callback_or_session: str,
        handler: EventCallback[ExceptionRevokedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def exceptionRevoked(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[ExceptionRevokedEvent]: ...

    def exceptionRevoked(
        self,
        callback_or_session: EventCallback[ExceptionRevokedEvent] | str | None = None,
        handler: EventCallback[ExceptionRevokedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[ExceptionRevokedEvent] | Unsubscribe:
        """Issued when unhandled exception was revoked."""

        return cast(
            Awaitable[ExceptionRevokedEvent] | Unsubscribe,
            self._event(
                "exceptionRevoked",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def exceptionThrown(
        self,
        callback_or_session: EventCallback[ExceptionThrownEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def exceptionThrown(
        self,
        callback_or_session: str,
        handler: EventCallback[ExceptionThrownEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def exceptionThrown(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[ExceptionThrownEvent]: ...

    def exceptionThrown(
        self,
        callback_or_session: EventCallback[ExceptionThrownEvent] | str | None = None,
        handler: EventCallback[ExceptionThrownEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[ExceptionThrownEvent] | Unsubscribe:
        """Issued when exception was thrown and unhandled."""

        return cast(
            Awaitable[ExceptionThrownEvent] | Unsubscribe,
            self._event(
                "exceptionThrown",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def executionContextCreated(
        self,
        callback_or_session: EventCallback[ExecutionContextCreatedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def executionContextCreated(
        self,
        callback_or_session: str,
        handler: EventCallback[ExecutionContextCreatedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def executionContextCreated(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[ExecutionContextCreatedEvent]: ...

    def executionContextCreated(
        self,
        callback_or_session: EventCallback[ExecutionContextCreatedEvent]
        | str
        | None = None,
        handler: EventCallback[ExecutionContextCreatedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[ExecutionContextCreatedEvent] | Unsubscribe:
        """Issued when new execution context is created."""

        return cast(
            Awaitable[ExecutionContextCreatedEvent] | Unsubscribe,
            self._event(
                "executionContextCreated",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def executionContextDestroyed(
        self,
        callback_or_session: EventCallback[ExecutionContextDestroyedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def executionContextDestroyed(
        self,
        callback_or_session: str,
        handler: EventCallback[ExecutionContextDestroyedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def executionContextDestroyed(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[ExecutionContextDestroyedEvent]: ...

    def executionContextDestroyed(
        self,
        callback_or_session: EventCallback[ExecutionContextDestroyedEvent]
        | str
        | None = None,
        handler: EventCallback[ExecutionContextDestroyedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[ExecutionContextDestroyedEvent] | Unsubscribe:
        """Issued when execution context is destroyed."""

        return cast(
            Awaitable[ExecutionContextDestroyedEvent] | Unsubscribe,
            self._event(
                "executionContextDestroyed",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def executionContextsCleared(
        self,
        callback_or_session: EventCallback[JsonObject],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def executionContextsCleared(
        self,
        callback_or_session: str,
        handler: EventCallback[JsonObject],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def executionContextsCleared(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[JsonObject]: ...

    def executionContextsCleared(
        self,
        callback_or_session: EventCallback[JsonObject] | str | None = None,
        handler: EventCallback[JsonObject] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[JsonObject] | Unsubscribe:
        """Issued when all executionContexts were cleared in browser"""

        return self._event(
            "executionContextsCleared",
            cast(EventCallback[Mapping[str, object]] | str | None, callback_or_session),
            cast(EventCallback[Mapping[str, object]] | None, handler),
            session_id,
        )

    @overload
    def inspectRequested(
        self,
        callback_or_session: EventCallback[InspectRequestedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def inspectRequested(
        self,
        callback_or_session: str,
        handler: EventCallback[InspectRequestedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def inspectRequested(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[InspectRequestedEvent]: ...

    def inspectRequested(
        self,
        callback_or_session: EventCallback[InspectRequestedEvent] | str | None = None,
        handler: EventCallback[InspectRequestedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[InspectRequestedEvent] | Unsubscribe:
        """Issued when object should be inspected (for example, as a result of inspect() command line API call)."""

        return cast(
            Awaitable[InspectRequestedEvent] | Unsubscribe,
            self._event(
                "inspectRequested",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )


__all__ = [
    "AddBindingParameters",
    "AwaitPromiseParameters",
    "AwaitPromiseResult",
    "BindingCalledEvent",
    "CallArgument",
    "CallFrame",
    "CallFunctionOnParameters",
    "CallFunctionOnResult",
    "CompileScriptParameters",
    "CompileScriptResult",
    "ConsoleAPICalledEvent",
    "CustomPreview",
    "DeepSerializedValue",
    "EntryPreview",
    "EvaluateParameters",
    "EvaluateResult",
    "ExceptionDetails",
    "ExceptionRevokedEvent",
    "ExceptionThrownEvent",
    "ExecutionContextCreatedEvent",
    "ExecutionContextDescription",
    "ExecutionContextDestroyedEvent",
    "ExecutionContextId",
    "GetExceptionDetailsParameters",
    "GetExceptionDetailsResult",
    "GetHeapUsageResult",
    "GetIsolateIdResult",
    "GetPropertiesParameters",
    "GetPropertiesResult",
    "GlobalLexicalScopeNamesParameters",
    "GlobalLexicalScopeNamesResult",
    "InspectRequestedEvent",
    "InternalPropertyDescriptor",
    "ObjectPreview",
    "PrivatePropertyDescriptor",
    "PropertyDescriptor",
    "PropertyPreview",
    "QueryObjectsParameters",
    "QueryObjectsResult",
    "ReleaseObjectGroupParameters",
    "ReleaseObjectParameters",
    "RemoteObject",
    "RemoteObjectId",
    "RemoveBindingParameters",
    "RunScriptParameters",
    "RunScriptResult",
    "Runtime",
    "ScriptId",
    "SerializationOptions",
    "SetAsyncCallStackDepthParameters",
    "SetCustomObjectFormatterEnabledParameters",
    "SetMaxCallStackSizeToCaptureParameters",
    "StackTrace",
    "StackTraceId",
    "TimeDelta",
    "Timestamp",
    "UniqueDebuggerId",
    "UnserializableValue",
]
