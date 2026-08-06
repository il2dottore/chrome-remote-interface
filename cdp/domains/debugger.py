"""Generated bindings for the CDP Debugger domain. Do not edit manually."""

from __future__ import annotations

from collections.abc import Awaitable, Mapping
from typing import TYPE_CHECKING, Literal, TypeAlias, cast, overload

from typing_extensions import NotRequired, TypedDict, Unpack

from cdp.domain import Domain as BaseDomain, EventCallback, Unsubscribe
from cdp.types import JsonObject

if TYPE_CHECKING:
    from . import runtime as Runtime


BreakpointId: TypeAlias = str

CallFrameId: TypeAlias = str


class Location(TypedDict):
    scriptId: Runtime.ScriptId
    lineNumber: int
    columnNumber: NotRequired[int]


class ScriptPosition(TypedDict):
    lineNumber: int
    columnNumber: int


class LocationRange(TypedDict):
    scriptId: Runtime.ScriptId
    start: ScriptPosition
    end: ScriptPosition


class CallFrame(TypedDict):
    callFrameId: CallFrameId
    functionName: str
    functionLocation: NotRequired[Location]
    location: Location
    url: str
    scopeChain: list[Scope]
    this: Runtime.RemoteObject
    returnValue: NotRequired[Runtime.RemoteObject]
    canBeRestarted: NotRequired[bool]


class Scope(TypedDict):
    type: Literal[
        "global",
        "local",
        "with",
        "closure",
        "catch",
        "block",
        "script",
        "eval",
        "module",
        "wasm-expression-stack",
    ]
    object: Runtime.RemoteObject
    name: NotRequired[str]
    startLocation: NotRequired[Location]
    endLocation: NotRequired[Location]


class SearchMatch(TypedDict):
    lineNumber: float
    lineContent: str


class BreakLocation(TypedDict):
    scriptId: Runtime.ScriptId
    lineNumber: int
    columnNumber: NotRequired[int]
    type: NotRequired[Literal["debuggerStatement", "call", "return"]]


class WasmDisassemblyChunk(TypedDict):
    lines: list[str]
    bytecodeOffsets: list[int]


ScriptLanguage: TypeAlias = Literal["JavaScript", "WebAssembly"]


class DebugSymbols(TypedDict):
    type: Literal["SourceMap", "EmbeddedDWARF", "ExternalDWARF"]
    externalURL: NotRequired[str]


class ResolvedBreakpoint(TypedDict):
    breakpointId: BreakpointId
    location: Location


class ContinueToLocationParameters(TypedDict):
    location: Location
    targetCallFrames: NotRequired[Literal["any", "current"]]


class EnableParameters(TypedDict):
    maxScriptsCacheSize: NotRequired[float]


class EnableResult(TypedDict):
    debuggerId: Runtime.UniqueDebuggerId


class EvaluateOnCallFrameParameters(TypedDict):
    callFrameId: CallFrameId
    expression: str
    objectGroup: NotRequired[str]
    includeCommandLineAPI: NotRequired[bool]
    silent: NotRequired[bool]
    returnByValue: NotRequired[bool]
    generatePreview: NotRequired[bool]
    throwOnSideEffect: NotRequired[bool]
    timeout: NotRequired[Runtime.TimeDelta]
    scopeNumber: NotRequired[int]


class EvaluateOnCallFrameResult(TypedDict):
    result: Runtime.RemoteObject
    exceptionDetails: NotRequired[Runtime.ExceptionDetails]


class GetPossibleBreakpointsParameters(TypedDict):
    start: Location
    end: NotRequired[Location]
    restrictToFunction: NotRequired[bool]


class GetPossibleBreakpointsResult(TypedDict):
    locations: list[BreakLocation]


class GetScriptSourceParameters(TypedDict):
    scriptId: Runtime.ScriptId


class GetScriptSourceResult(TypedDict):
    scriptSource: str
    bytecode: NotRequired[str]


class DisassembleWasmModuleParameters(TypedDict):
    scriptId: Runtime.ScriptId


class DisassembleWasmModuleResult(TypedDict):
    streamId: NotRequired[str]
    totalNumberOfLines: int
    functionBodyOffsets: list[int]
    chunk: WasmDisassemblyChunk


class NextWasmDisassemblyChunkParameters(TypedDict):
    streamId: str


class NextWasmDisassemblyChunkResult(TypedDict):
    chunk: WasmDisassemblyChunk


class GetWasmBytecodeParameters(TypedDict):
    scriptId: Runtime.ScriptId


class GetWasmBytecodeResult(TypedDict):
    bytecode: str


class GetStackTraceParameters(TypedDict):
    stackTraceId: Runtime.StackTraceId


class GetStackTraceResult(TypedDict):
    stackTrace: Runtime.StackTrace


class PauseOnAsyncCallParameters(TypedDict):
    parentStackTraceId: Runtime.StackTraceId


class RemoveBreakpointParameters(TypedDict):
    breakpointId: BreakpointId


class RestartFrameParameters(TypedDict):
    callFrameId: CallFrameId
    mode: NotRequired[Literal["StepInto"]]


class RestartFrameResult(TypedDict):
    callFrames: list[CallFrame]
    asyncStackTrace: NotRequired[Runtime.StackTrace]
    asyncStackTraceId: NotRequired[Runtime.StackTraceId]


class ResumeParameters(TypedDict):
    terminateOnResume: NotRequired[bool]


class SearchInContentParameters(TypedDict):
    scriptId: Runtime.ScriptId
    query: str
    caseSensitive: NotRequired[bool]
    isRegex: NotRequired[bool]


class SearchInContentResult(TypedDict):
    result: list[SearchMatch]


class SetAsyncCallStackDepthParameters(TypedDict):
    maxDepth: int


class SetBlackboxExecutionContextsParameters(TypedDict):
    uniqueIds: list[str]


class SetBlackboxPatternsParameters(TypedDict):
    patterns: list[str]
    skipAnonymous: NotRequired[bool]


class SetBlackboxedRangesParameters(TypedDict):
    scriptId: Runtime.ScriptId
    positions: list[ScriptPosition]


class SetBreakpointParameters(TypedDict):
    location: Location
    condition: NotRequired[str]


class SetBreakpointResult(TypedDict):
    breakpointId: BreakpointId
    actualLocation: Location


class SetInstrumentationBreakpointParameters(TypedDict):
    instrumentation: Literal[
        "beforeScriptExecution", "beforeScriptWithSourceMapExecution"
    ]


class SetInstrumentationBreakpointResult(TypedDict):
    breakpointId: BreakpointId


class SetBreakpointByUrlParameters(TypedDict):
    lineNumber: int
    url: NotRequired[str]
    urlRegex: NotRequired[str]
    scriptHash: NotRequired[str]
    columnNumber: NotRequired[int]
    condition: NotRequired[str]


class SetBreakpointByUrlResult(TypedDict):
    breakpointId: BreakpointId
    locations: list[Location]


class SetBreakpointOnFunctionCallParameters(TypedDict):
    objectId: Runtime.RemoteObjectId
    condition: NotRequired[str]


class SetBreakpointOnFunctionCallResult(TypedDict):
    breakpointId: BreakpointId


class SetBreakpointsActiveParameters(TypedDict):
    active: bool


class SetPauseOnExceptionsParameters(TypedDict):
    state: Literal["none", "caught", "uncaught", "all"]


class SetReturnValueParameters(TypedDict):
    newValue: Runtime.CallArgument


class SetScriptSourceParameters(TypedDict):
    scriptId: Runtime.ScriptId
    scriptSource: str
    dryRun: NotRequired[bool]
    allowTopFrameEditing: NotRequired[bool]


class SetScriptSourceResult(TypedDict):
    callFrames: NotRequired[list[CallFrame]]
    stackChanged: NotRequired[bool]
    asyncStackTrace: NotRequired[Runtime.StackTrace]
    asyncStackTraceId: NotRequired[Runtime.StackTraceId]
    status: Literal[
        "Ok",
        "CompileError",
        "BlockedByActiveGenerator",
        "BlockedByActiveFunction",
        "BlockedByTopLevelEsModuleChange",
    ]
    exceptionDetails: NotRequired[Runtime.ExceptionDetails]


class SetSkipAllPausesParameters(TypedDict):
    skip: bool


class SetVariableValueParameters(TypedDict):
    scopeNumber: int
    variableName: str
    newValue: Runtime.CallArgument
    callFrameId: CallFrameId


class StepIntoParameters(TypedDict):
    breakOnAsyncCall: NotRequired[bool]
    skipList: NotRequired[list[LocationRange]]


class StepOverParameters(TypedDict):
    skipList: NotRequired[list[LocationRange]]


class BreakpointResolvedEvent(TypedDict):
    breakpointId: BreakpointId
    location: Location


class PausedEvent(TypedDict):
    callFrames: list[CallFrame]
    reason: Literal[
        "ambiguous",
        "assert",
        "CSPViolation",
        "debugCommand",
        "DOM",
        "EventListener",
        "exception",
        "instrumentation",
        "OOM",
        "other",
        "promiseRejection",
        "XHR",
        "step",
    ]
    data: NotRequired[JsonObject]
    hitBreakpoints: NotRequired[list[str]]
    asyncStackTrace: NotRequired[Runtime.StackTrace]
    asyncStackTraceId: NotRequired[Runtime.StackTraceId]
    asyncCallStackTraceId: NotRequired[Runtime.StackTraceId]


class ScriptFailedToParseEvent(TypedDict):
    scriptId: Runtime.ScriptId
    url: str
    startLine: int
    startColumn: int
    endLine: int
    endColumn: int
    executionContextId: Runtime.ExecutionContextId
    hash: str
    buildId: str
    executionContextAuxData: NotRequired[JsonObject]
    sourceMapURL: NotRequired[str]
    hasSourceURL: NotRequired[bool]
    isModule: NotRequired[bool]
    length: NotRequired[int]
    stackTrace: NotRequired[Runtime.StackTrace]
    codeOffset: NotRequired[int]
    scriptLanguage: NotRequired[ScriptLanguage]
    embedderName: NotRequired[str]


class ScriptParsedEvent(TypedDict):
    scriptId: Runtime.ScriptId
    url: str
    startLine: int
    startColumn: int
    endLine: int
    endColumn: int
    executionContextId: Runtime.ExecutionContextId
    hash: str
    buildId: str
    executionContextAuxData: NotRequired[JsonObject]
    isLiveEdit: NotRequired[bool]
    sourceMapURL: NotRequired[str]
    hasSourceURL: NotRequired[bool]
    isModule: NotRequired[bool]
    length: NotRequired[int]
    stackTrace: NotRequired[Runtime.StackTrace]
    codeOffset: NotRequired[int]
    scriptLanguage: NotRequired[ScriptLanguage]
    debugSymbols: NotRequired[list[DebugSymbols]]
    embedderName: NotRequired[str]
    resolvedBreakpoints: NotRequired[list[ResolvedBreakpoint]]


class Debugger(BaseDomain):
    """Debugger domain exposes JavaScript debugging capabilities. It allows setting and removing breakpoints, stepping through execution, exploring stack traces, etc."""

    domain_name = "Debugger"

    @overload
    async def continueToLocation(
        self,
        params: ContinueToLocationParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def continueToLocation(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[ContinueToLocationParameters],
    ) -> JsonObject: ...

    async def continueToLocation(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Continues execution until specific location is reached."""

        return await self._command("continueToLocation", params, session_id, kwargs)

    async def disable(
        self,
        session_id: str | None = None,
    ) -> JsonObject:
        """Disables debugger for given page."""

        return await self._command("disable", None, session_id, {})

    @overload
    async def enable(
        self,
        params: EnableParameters,
        session_id: str | None = None,
    ) -> EnableResult: ...

    @overload
    async def enable(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[EnableParameters],
    ) -> EnableResult: ...

    async def enable(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> EnableResult:
        """Enables debugger for the given page. Clients should not assume that the debugging has been enabled until the result for this command is received."""

        return cast(
            EnableResult, await self._command("enable", params, session_id, kwargs)
        )

    @overload
    async def evaluateOnCallFrame(
        self,
        params: EvaluateOnCallFrameParameters,
        session_id: str | None = None,
    ) -> EvaluateOnCallFrameResult: ...

    @overload
    async def evaluateOnCallFrame(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[EvaluateOnCallFrameParameters],
    ) -> EvaluateOnCallFrameResult: ...

    async def evaluateOnCallFrame(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> EvaluateOnCallFrameResult:
        """Evaluates expression on a given call frame."""

        return cast(
            EvaluateOnCallFrameResult,
            await self._command("evaluateOnCallFrame", params, session_id, kwargs),
        )

    @overload
    async def getPossibleBreakpoints(
        self,
        params: GetPossibleBreakpointsParameters,
        session_id: str | None = None,
    ) -> GetPossibleBreakpointsResult: ...

    @overload
    async def getPossibleBreakpoints(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[GetPossibleBreakpointsParameters],
    ) -> GetPossibleBreakpointsResult: ...

    async def getPossibleBreakpoints(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> GetPossibleBreakpointsResult:
        """Returns possible locations for breakpoint. scriptId in start and end range locations should be the same."""

        return cast(
            GetPossibleBreakpointsResult,
            await self._command("getPossibleBreakpoints", params, session_id, kwargs),
        )

    @overload
    async def getScriptSource(
        self,
        params: GetScriptSourceParameters,
        session_id: str | None = None,
    ) -> GetScriptSourceResult: ...

    @overload
    async def getScriptSource(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[GetScriptSourceParameters],
    ) -> GetScriptSourceResult: ...

    async def getScriptSource(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> GetScriptSourceResult:
        """Returns source for the script with given id."""

        return cast(
            GetScriptSourceResult,
            await self._command("getScriptSource", params, session_id, kwargs),
        )

    @overload
    async def disassembleWasmModule(
        self,
        params: DisassembleWasmModuleParameters,
        session_id: str | None = None,
    ) -> DisassembleWasmModuleResult: ...

    @overload
    async def disassembleWasmModule(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[DisassembleWasmModuleParameters],
    ) -> DisassembleWasmModuleResult: ...

    async def disassembleWasmModule(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> DisassembleWasmModuleResult:
        """Send Debugger.disassembleWasmModule."""

        return cast(
            DisassembleWasmModuleResult,
            await self._command("disassembleWasmModule", params, session_id, kwargs),
        )

    @overload
    async def nextWasmDisassemblyChunk(
        self,
        params: NextWasmDisassemblyChunkParameters,
        session_id: str | None = None,
    ) -> NextWasmDisassemblyChunkResult: ...

    @overload
    async def nextWasmDisassemblyChunk(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[NextWasmDisassemblyChunkParameters],
    ) -> NextWasmDisassemblyChunkResult: ...

    async def nextWasmDisassemblyChunk(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> NextWasmDisassemblyChunkResult:
        """Disassemble the next chunk of lines for the module corresponding to the stream. If disassembly is complete, this API will invalidate the streamId and return an empty chunk. Any subsequent calls for the now invalid stream will return errors."""

        return cast(
            NextWasmDisassemblyChunkResult,
            await self._command("nextWasmDisassemblyChunk", params, session_id, kwargs),
        )

    @overload
    async def getWasmBytecode(
        self,
        params: GetWasmBytecodeParameters,
        session_id: str | None = None,
    ) -> GetWasmBytecodeResult: ...

    @overload
    async def getWasmBytecode(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[GetWasmBytecodeParameters],
    ) -> GetWasmBytecodeResult: ...

    async def getWasmBytecode(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> GetWasmBytecodeResult:
        """This command is deprecated. Use getScriptSource instead."""

        return cast(
            GetWasmBytecodeResult,
            await self._command("getWasmBytecode", params, session_id, kwargs),
        )

    @overload
    async def getStackTrace(
        self,
        params: GetStackTraceParameters,
        session_id: str | None = None,
    ) -> GetStackTraceResult: ...

    @overload
    async def getStackTrace(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[GetStackTraceParameters],
    ) -> GetStackTraceResult: ...

    async def getStackTrace(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> GetStackTraceResult:
        """Returns stack trace with given `stackTraceId`."""

        return cast(
            GetStackTraceResult,
            await self._command("getStackTrace", params, session_id, kwargs),
        )

    async def pause(
        self,
        session_id: str | None = None,
    ) -> JsonObject:
        """Stops on the next JavaScript statement."""

        return await self._command("pause", None, session_id, {})

    @overload
    async def pauseOnAsyncCall(
        self,
        params: PauseOnAsyncCallParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def pauseOnAsyncCall(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[PauseOnAsyncCallParameters],
    ) -> JsonObject: ...

    async def pauseOnAsyncCall(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Send Debugger.pauseOnAsyncCall."""

        return await self._command("pauseOnAsyncCall", params, session_id, kwargs)

    @overload
    async def removeBreakpoint(
        self,
        params: RemoveBreakpointParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def removeBreakpoint(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[RemoveBreakpointParameters],
    ) -> JsonObject: ...

    async def removeBreakpoint(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Removes JavaScript breakpoint."""

        return await self._command("removeBreakpoint", params, session_id, kwargs)

    @overload
    async def restartFrame(
        self,
        params: RestartFrameParameters,
        session_id: str | None = None,
    ) -> RestartFrameResult: ...

    @overload
    async def restartFrame(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[RestartFrameParameters],
    ) -> RestartFrameResult: ...

    async def restartFrame(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> RestartFrameResult:
        """Restarts particular call frame from the beginning. The old, deprecated behavior of `restartFrame` is to stay paused and allow further CDP commands after a restart was scheduled. This can cause problems with restarting, so we now continue execution immediatly after it has been scheduled until we reach the beginning of the restarted frame. To stay back-wards compatible, `restartFrame` now expects a `mode` parameter to be present. If the `mode` parameter is missing, `restartFrame` errors out. The various return values are deprecated and `callFrames` is always empty. Use the call frames from the `Debugger#paused` events instead, that fires once V8 pauses at the beginning of the restarted function."""

        return cast(
            RestartFrameResult,
            await self._command("restartFrame", params, session_id, kwargs),
        )

    @overload
    async def resume(
        self,
        params: ResumeParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def resume(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[ResumeParameters],
    ) -> JsonObject: ...

    async def resume(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Resumes JavaScript execution."""

        return await self._command("resume", params, session_id, kwargs)

    @overload
    async def searchInContent(
        self,
        params: SearchInContentParameters,
        session_id: str | None = None,
    ) -> SearchInContentResult: ...

    @overload
    async def searchInContent(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SearchInContentParameters],
    ) -> SearchInContentResult: ...

    async def searchInContent(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> SearchInContentResult:
        """Searches for given string in script content."""

        return cast(
            SearchInContentResult,
            await self._command("searchInContent", params, session_id, kwargs),
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
    async def setBlackboxExecutionContexts(
        self,
        params: SetBlackboxExecutionContextsParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def setBlackboxExecutionContexts(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetBlackboxExecutionContextsParameters],
    ) -> JsonObject: ...

    async def setBlackboxExecutionContexts(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Replace previous blackbox execution contexts with passed ones. Forces backend to skip stepping/pausing in scripts in these execution contexts. VM will try to leave blackboxed script by performing 'step in' several times, finally resorting to 'step out' if unsuccessful."""

        return await self._command(
            "setBlackboxExecutionContexts", params, session_id, kwargs
        )

    @overload
    async def setBlackboxPatterns(
        self,
        params: SetBlackboxPatternsParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def setBlackboxPatterns(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetBlackboxPatternsParameters],
    ) -> JsonObject: ...

    async def setBlackboxPatterns(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Replace previous blackbox patterns with passed ones. Forces backend to skip stepping/pausing in scripts with url matching one of the patterns. VM will try to leave blackboxed script by performing 'step in' several times, finally resorting to 'step out' if unsuccessful."""

        return await self._command("setBlackboxPatterns", params, session_id, kwargs)

    @overload
    async def setBlackboxedRanges(
        self,
        params: SetBlackboxedRangesParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def setBlackboxedRanges(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetBlackboxedRangesParameters],
    ) -> JsonObject: ...

    async def setBlackboxedRanges(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Makes backend skip steps in the script in blackboxed ranges. VM will try leave blacklisted scripts by performing 'step in' several times, finally resorting to 'step out' if unsuccessful. Positions array contains positions where blackbox state is changed. First interval isn't blackboxed. Array should be sorted."""

        return await self._command("setBlackboxedRanges", params, session_id, kwargs)

    @overload
    async def setBreakpoint(
        self,
        params: SetBreakpointParameters,
        session_id: str | None = None,
    ) -> SetBreakpointResult: ...

    @overload
    async def setBreakpoint(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetBreakpointParameters],
    ) -> SetBreakpointResult: ...

    async def setBreakpoint(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> SetBreakpointResult:
        """Sets JavaScript breakpoint at a given location."""

        return cast(
            SetBreakpointResult,
            await self._command("setBreakpoint", params, session_id, kwargs),
        )

    @overload
    async def setInstrumentationBreakpoint(
        self,
        params: SetInstrumentationBreakpointParameters,
        session_id: str | None = None,
    ) -> SetInstrumentationBreakpointResult: ...

    @overload
    async def setInstrumentationBreakpoint(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetInstrumentationBreakpointParameters],
    ) -> SetInstrumentationBreakpointResult: ...

    async def setInstrumentationBreakpoint(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> SetInstrumentationBreakpointResult:
        """Sets instrumentation breakpoint."""

        return cast(
            SetInstrumentationBreakpointResult,
            await self._command(
                "setInstrumentationBreakpoint", params, session_id, kwargs
            ),
        )

    @overload
    async def setBreakpointByUrl(
        self,
        params: SetBreakpointByUrlParameters,
        session_id: str | None = None,
    ) -> SetBreakpointByUrlResult: ...

    @overload
    async def setBreakpointByUrl(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetBreakpointByUrlParameters],
    ) -> SetBreakpointByUrlResult: ...

    async def setBreakpointByUrl(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> SetBreakpointByUrlResult:
        """Sets JavaScript breakpoint at given location specified either by URL or URL regex. Once this command is issued, all existing parsed scripts will have breakpoints resolved and returned in `locations` property. Further matching script parsing will result in subsequent `breakpointResolved` events issued. This logical breakpoint will survive page reloads."""

        return cast(
            SetBreakpointByUrlResult,
            await self._command("setBreakpointByUrl", params, session_id, kwargs),
        )

    @overload
    async def setBreakpointOnFunctionCall(
        self,
        params: SetBreakpointOnFunctionCallParameters,
        session_id: str | None = None,
    ) -> SetBreakpointOnFunctionCallResult: ...

    @overload
    async def setBreakpointOnFunctionCall(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetBreakpointOnFunctionCallParameters],
    ) -> SetBreakpointOnFunctionCallResult: ...

    async def setBreakpointOnFunctionCall(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> SetBreakpointOnFunctionCallResult:
        """Sets JavaScript breakpoint before each call to the given function. If another function was created from the same source as a given one, calling it will also trigger the breakpoint."""

        return cast(
            SetBreakpointOnFunctionCallResult,
            await self._command(
                "setBreakpointOnFunctionCall", params, session_id, kwargs
            ),
        )

    @overload
    async def setBreakpointsActive(
        self,
        params: SetBreakpointsActiveParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def setBreakpointsActive(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetBreakpointsActiveParameters],
    ) -> JsonObject: ...

    async def setBreakpointsActive(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Activates / deactivates all breakpoints on the page."""

        return await self._command("setBreakpointsActive", params, session_id, kwargs)

    @overload
    async def setPauseOnExceptions(
        self,
        params: SetPauseOnExceptionsParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def setPauseOnExceptions(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetPauseOnExceptionsParameters],
    ) -> JsonObject: ...

    async def setPauseOnExceptions(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Defines pause on exceptions state. Can be set to stop on all exceptions, uncaught exceptions, or caught exceptions, no exceptions. Initial pause on exceptions state is `none`."""

        return await self._command("setPauseOnExceptions", params, session_id, kwargs)

    @overload
    async def setReturnValue(
        self,
        params: SetReturnValueParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def setReturnValue(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetReturnValueParameters],
    ) -> JsonObject: ...

    async def setReturnValue(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Changes return value in top frame. Available only at return break position."""

        return await self._command("setReturnValue", params, session_id, kwargs)

    @overload
    async def setScriptSource(
        self,
        params: SetScriptSourceParameters,
        session_id: str | None = None,
    ) -> SetScriptSourceResult: ...

    @overload
    async def setScriptSource(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetScriptSourceParameters],
    ) -> SetScriptSourceResult: ...

    async def setScriptSource(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> SetScriptSourceResult:
        """Edits JavaScript source live. In general, functions that are currently on the stack can not be edited with a single exception: If the edited function is the top-most stack frame and that is the only activation of that function on the stack. In this case the live edit will be successful and a `Debugger.restartFrame` for the top-most function is automatically triggered."""

        return cast(
            SetScriptSourceResult,
            await self._command("setScriptSource", params, session_id, kwargs),
        )

    @overload
    async def setSkipAllPauses(
        self,
        params: SetSkipAllPausesParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def setSkipAllPauses(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetSkipAllPausesParameters],
    ) -> JsonObject: ...

    async def setSkipAllPauses(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Makes page not interrupt on any pauses (breakpoint, exception, dom exception etc)."""

        return await self._command("setSkipAllPauses", params, session_id, kwargs)

    @overload
    async def setVariableValue(
        self,
        params: SetVariableValueParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def setVariableValue(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetVariableValueParameters],
    ) -> JsonObject: ...

    async def setVariableValue(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Changes value of variable in a callframe. Object-based scopes are not supported and must be mutated manually."""

        return await self._command("setVariableValue", params, session_id, kwargs)

    @overload
    async def stepInto(
        self,
        params: StepIntoParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def stepInto(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[StepIntoParameters],
    ) -> JsonObject: ...

    async def stepInto(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Steps into the function call."""

        return await self._command("stepInto", params, session_id, kwargs)

    async def stepOut(
        self,
        session_id: str | None = None,
    ) -> JsonObject:
        """Steps out of the function call."""

        return await self._command("stepOut", None, session_id, {})

    @overload
    async def stepOver(
        self,
        params: StepOverParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def stepOver(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[StepOverParameters],
    ) -> JsonObject: ...

    async def stepOver(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Steps over the statement."""

        return await self._command("stepOver", params, session_id, kwargs)

    @overload
    def breakpointResolved(
        self,
        callback_or_session: EventCallback[BreakpointResolvedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def breakpointResolved(
        self,
        callback_or_session: str,
        handler: EventCallback[BreakpointResolvedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def breakpointResolved(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[BreakpointResolvedEvent]: ...

    def breakpointResolved(
        self,
        callback_or_session: EventCallback[BreakpointResolvedEvent] | str | None = None,
        handler: EventCallback[BreakpointResolvedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[BreakpointResolvedEvent] | Unsubscribe:
        """Fired when breakpoint is resolved to an actual script and location. Deprecated in favor of `resolvedBreakpoints` in the `scriptParsed` event."""

        return cast(
            Awaitable[BreakpointResolvedEvent] | Unsubscribe,
            self._event(
                "breakpointResolved",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def paused(
        self,
        callback_or_session: EventCallback[PausedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def paused(
        self,
        callback_or_session: str,
        handler: EventCallback[PausedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def paused(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[PausedEvent]: ...

    def paused(
        self,
        callback_or_session: EventCallback[PausedEvent] | str | None = None,
        handler: EventCallback[PausedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[PausedEvent] | Unsubscribe:
        """Fired when the virtual machine stopped on breakpoint or exception or any other stop criteria."""

        return cast(
            Awaitable[PausedEvent] | Unsubscribe,
            self._event(
                "paused",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def resumed(
        self,
        callback_or_session: EventCallback[JsonObject],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def resumed(
        self,
        callback_or_session: str,
        handler: EventCallback[JsonObject],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def resumed(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[JsonObject]: ...

    def resumed(
        self,
        callback_or_session: EventCallback[JsonObject] | str | None = None,
        handler: EventCallback[JsonObject] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[JsonObject] | Unsubscribe:
        """Fired when the virtual machine resumed execution."""

        return self._event(
            "resumed",
            cast(EventCallback[Mapping[str, object]] | str | None, callback_or_session),
            cast(EventCallback[Mapping[str, object]] | None, handler),
            session_id,
        )

    @overload
    def scriptFailedToParse(
        self,
        callback_or_session: EventCallback[ScriptFailedToParseEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def scriptFailedToParse(
        self,
        callback_or_session: str,
        handler: EventCallback[ScriptFailedToParseEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def scriptFailedToParse(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[ScriptFailedToParseEvent]: ...

    def scriptFailedToParse(
        self,
        callback_or_session: EventCallback[ScriptFailedToParseEvent]
        | str
        | None = None,
        handler: EventCallback[ScriptFailedToParseEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[ScriptFailedToParseEvent] | Unsubscribe:
        """Fired when virtual machine fails to parse the script."""

        return cast(
            Awaitable[ScriptFailedToParseEvent] | Unsubscribe,
            self._event(
                "scriptFailedToParse",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def scriptParsed(
        self,
        callback_or_session: EventCallback[ScriptParsedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def scriptParsed(
        self,
        callback_or_session: str,
        handler: EventCallback[ScriptParsedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def scriptParsed(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[ScriptParsedEvent]: ...

    def scriptParsed(
        self,
        callback_or_session: EventCallback[ScriptParsedEvent] | str | None = None,
        handler: EventCallback[ScriptParsedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[ScriptParsedEvent] | Unsubscribe:
        """Fired when virtual machine parses script. This event is also fired for all known and uncollected scripts upon enabling debugger."""

        return cast(
            Awaitable[ScriptParsedEvent] | Unsubscribe,
            self._event(
                "scriptParsed",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )


__all__ = [
    "BreakLocation",
    "BreakpointId",
    "BreakpointResolvedEvent",
    "CallFrame",
    "CallFrameId",
    "ContinueToLocationParameters",
    "DebugSymbols",
    "Debugger",
    "DisassembleWasmModuleParameters",
    "DisassembleWasmModuleResult",
    "EnableParameters",
    "EnableResult",
    "EvaluateOnCallFrameParameters",
    "EvaluateOnCallFrameResult",
    "GetPossibleBreakpointsParameters",
    "GetPossibleBreakpointsResult",
    "GetScriptSourceParameters",
    "GetScriptSourceResult",
    "GetStackTraceParameters",
    "GetStackTraceResult",
    "GetWasmBytecodeParameters",
    "GetWasmBytecodeResult",
    "Location",
    "LocationRange",
    "NextWasmDisassemblyChunkParameters",
    "NextWasmDisassemblyChunkResult",
    "PauseOnAsyncCallParameters",
    "PausedEvent",
    "RemoveBreakpointParameters",
    "ResolvedBreakpoint",
    "RestartFrameParameters",
    "RestartFrameResult",
    "ResumeParameters",
    "Scope",
    "ScriptFailedToParseEvent",
    "ScriptLanguage",
    "ScriptParsedEvent",
    "ScriptPosition",
    "SearchInContentParameters",
    "SearchInContentResult",
    "SearchMatch",
    "SetAsyncCallStackDepthParameters",
    "SetBlackboxExecutionContextsParameters",
    "SetBlackboxPatternsParameters",
    "SetBlackboxedRangesParameters",
    "SetBreakpointByUrlParameters",
    "SetBreakpointByUrlResult",
    "SetBreakpointOnFunctionCallParameters",
    "SetBreakpointOnFunctionCallResult",
    "SetBreakpointParameters",
    "SetBreakpointResult",
    "SetBreakpointsActiveParameters",
    "SetInstrumentationBreakpointParameters",
    "SetInstrumentationBreakpointResult",
    "SetPauseOnExceptionsParameters",
    "SetReturnValueParameters",
    "SetScriptSourceParameters",
    "SetScriptSourceResult",
    "SetSkipAllPausesParameters",
    "SetVariableValueParameters",
    "StepIntoParameters",
    "StepOverParameters",
    "WasmDisassemblyChunk",
]
