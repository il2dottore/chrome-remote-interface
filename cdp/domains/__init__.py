"""Generated CDP domain registry. Do not edit manually."""

from __future__ import annotations

from typing import TYPE_CHECKING

from cdp.domain import Domain

from .accessibility import Accessibility
from .animation import AnimationDomain
from .audits import Audits
from .autofill import Autofill
from .background_service import BackgroundService
from .browser import Browser
from .css import CSS
from .cache_storage import CacheStorage
from .cast import Cast
from .dom import DOM
from .dom_debugger import DOMDebugger
from .event_breakpoints import EventBreakpoints
from .dom_snapshot import DOMSnapshot
from .dom_storage import DOMStorage
from .database import DatabaseDomain
from .device_orientation import DeviceOrientation
from .emulation import Emulation
from .headless_experimental import HeadlessExperimental
from .io import IO
from .indexed_db import IndexedDB
from .input import Input
from .inspector import Inspector
from .layer_tree import LayerTree
from .log import Log
from .memory import Memory
from .network import Network
from .overlay import Overlay
from .page import Page
from .performance import Performance
from .performance_timeline import PerformanceTimeline
from .security import Security
from .service_worker import ServiceWorker
from .storage import Storage
from .system_info import SystemInfo
from .target import Target
from .tethering import Tethering
from .tracing import Tracing
from .fetch import Fetch
from .web_audio import WebAudio
from .web_authn import WebAuthn
from .media import Media
from .device_access import DeviceAccess
from .preload import Preload
from .fed_cm import FedCm
from .console import Console
from .debugger import Debugger
from .heap_profiler import HeapProfiler
from .profiler import Profiler
from .runtime import Runtime
from .schema import Schema

DOMAIN_CLASSES: dict[str, type[Domain]] = {
    "Accessibility": Accessibility,
    "Animation": AnimationDomain,
    "Audits": Audits,
    "Autofill": Autofill,
    "BackgroundService": BackgroundService,
    "Browser": Browser,
    "CSS": CSS,
    "CacheStorage": CacheStorage,
    "Cast": Cast,
    "DOM": DOM,
    "DOMDebugger": DOMDebugger,
    "EventBreakpoints": EventBreakpoints,
    "DOMSnapshot": DOMSnapshot,
    "DOMStorage": DOMStorage,
    "Database": DatabaseDomain,
    "DeviceOrientation": DeviceOrientation,
    "Emulation": Emulation,
    "HeadlessExperimental": HeadlessExperimental,
    "IO": IO,
    "IndexedDB": IndexedDB,
    "Input": Input,
    "Inspector": Inspector,
    "LayerTree": LayerTree,
    "Log": Log,
    "Memory": Memory,
    "Network": Network,
    "Overlay": Overlay,
    "Page": Page,
    "Performance": Performance,
    "PerformanceTimeline": PerformanceTimeline,
    "Security": Security,
    "ServiceWorker": ServiceWorker,
    "Storage": Storage,
    "SystemInfo": SystemInfo,
    "Target": Target,
    "Tethering": Tethering,
    "Tracing": Tracing,
    "Fetch": Fetch,
    "WebAudio": WebAudio,
    "WebAuthn": WebAuthn,
    "Media": Media,
    "DeviceAccess": DeviceAccess,
    "Preload": Preload,
    "FedCm": FedCm,
    "Console": Console,
    "Debugger": Debugger,
    "HeapProfiler": HeapProfiler,
    "Profiler": Profiler,
    "Runtime": Runtime,
    "Schema": Schema,
}

if TYPE_CHECKING:
    _domain_count: int

__all__ = [
    "CSS",
    "DOM",
    "IO",
    "Accessibility",
    "AnimationDomain",
    "Audits",
    "Autofill",
    "BackgroundService",
    "Browser",
    "CacheStorage",
    "Cast",
    "Console",
    "DOMDebugger",
    "DOMSnapshot",
    "DOMStorage",
    "DatabaseDomain",
    "Debugger",
    "DeviceAccess",
    "DeviceOrientation",
    "Emulation",
    "EventBreakpoints",
    "FedCm",
    "Fetch",
    "HeadlessExperimental",
    "HeapProfiler",
    "IndexedDB",
    "Input",
    "Inspector",
    "LayerTree",
    "Log",
    "Media",
    "Memory",
    "Network",
    "Overlay",
    "Page",
    "Performance",
    "PerformanceTimeline",
    "Preload",
    "Profiler",
    "Runtime",
    "Schema",
    "Security",
    "ServiceWorker",
    "Storage",
    "SystemInfo",
    "Target",
    "Tethering",
    "Tracing",
    "WebAudio",
    "WebAuthn",
]
