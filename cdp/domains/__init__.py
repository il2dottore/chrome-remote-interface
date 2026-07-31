"""Generated CDP domain registry. Do not edit manually."""

from __future__ import annotations

from typing import TYPE_CHECKING

from cdp.domain import Domain

from .accessibility import Accessibility
from .ads import Ads
from .animation import AnimationDomain
from .audits import Audits
from .autofill import Autofill
from .background_service import BackgroundService
from .bluetooth_emulation import BluetoothEmulation
from .browser import Browser
from .css import CSS
from .cache_storage import CacheStorage
from .cast import Cast
from .crash_report_context import CrashReportContext
from .dom import DOM
from .dom_debugger import DOMDebugger
from .dom_snapshot import DOMSnapshot
from .dom_storage import DOMStorage
from .device_access import DeviceAccess
from .device_orientation import DeviceOrientation
from .digital_credentials import DigitalCredentials
from .emulation import Emulation
from .event_breakpoints import EventBreakpoints
from .extensions import Extensions
from .fed_cm import FedCm
from .fetch import Fetch
from .file_system import FileSystem
from .headless_experimental import HeadlessExperimental
from .io import IO
from .indexed_db import IndexedDB
from .input import Input
from .inspector import Inspector
from .layer_tree import LayerTree
from .log import Log
from .media import Media
from .memory import Memory
from .network import Network
from .overlay import Overlay
from .pwa import PWA
from .page import Page
from .performance import Performance
from .performance_timeline import PerformanceTimeline
from .preload import Preload
from .security import Security
from .service_worker import ServiceWorker
from .smart_card_emulation import SmartCardEmulation
from .storage import Storage
from .system_info import SystemInfo
from .target import Target
from .tethering import Tethering
from .tracing import Tracing
from .web_audio import WebAudio
from .web_authn import WebAuthn
from .web_mcp import WebMCP
from .console import Console
from .debugger import Debugger
from .heap_profiler import HeapProfiler
from .profiler import Profiler
from .runtime import Runtime
from .schema import Schema

DOMAIN_CLASSES: dict[str, type[Domain]] = {
    "Accessibility": Accessibility,
    "Ads": Ads,
    "Animation": AnimationDomain,
    "Audits": Audits,
    "Autofill": Autofill,
    "BackgroundService": BackgroundService,
    "BluetoothEmulation": BluetoothEmulation,
    "Browser": Browser,
    "CSS": CSS,
    "CacheStorage": CacheStorage,
    "Cast": Cast,
    "CrashReportContext": CrashReportContext,
    "DOM": DOM,
    "DOMDebugger": DOMDebugger,
    "DOMSnapshot": DOMSnapshot,
    "DOMStorage": DOMStorage,
    "DeviceAccess": DeviceAccess,
    "DeviceOrientation": DeviceOrientation,
    "DigitalCredentials": DigitalCredentials,
    "Emulation": Emulation,
    "EventBreakpoints": EventBreakpoints,
    "Extensions": Extensions,
    "FedCm": FedCm,
    "Fetch": Fetch,
    "FileSystem": FileSystem,
    "HeadlessExperimental": HeadlessExperimental,
    "IO": IO,
    "IndexedDB": IndexedDB,
    "Input": Input,
    "Inspector": Inspector,
    "LayerTree": LayerTree,
    "Log": Log,
    "Media": Media,
    "Memory": Memory,
    "Network": Network,
    "Overlay": Overlay,
    "PWA": PWA,
    "Page": Page,
    "Performance": Performance,
    "PerformanceTimeline": PerformanceTimeline,
    "Preload": Preload,
    "Security": Security,
    "ServiceWorker": ServiceWorker,
    "SmartCardEmulation": SmartCardEmulation,
    "Storage": Storage,
    "SystemInfo": SystemInfo,
    "Target": Target,
    "Tethering": Tethering,
    "Tracing": Tracing,
    "WebAudio": WebAudio,
    "WebAuthn": WebAuthn,
    "WebMCP": WebMCP,
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
    "PWA",
    "Accessibility",
    "Ads",
    "AnimationDomain",
    "Audits",
    "Autofill",
    "BackgroundService",
    "BluetoothEmulation",
    "Browser",
    "CacheStorage",
    "Cast",
    "Console",
    "CrashReportContext",
    "DOMDebugger",
    "DOMSnapshot",
    "DOMStorage",
    "Debugger",
    "DeviceAccess",
    "DeviceOrientation",
    "DigitalCredentials",
    "Emulation",
    "EventBreakpoints",
    "Extensions",
    "FedCm",
    "Fetch",
    "FileSystem",
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
    "SmartCardEmulation",
    "Storage",
    "SystemInfo",
    "Target",
    "Tethering",
    "Tracing",
    "WebAudio",
    "WebAuthn",
    "WebMCP",
]
