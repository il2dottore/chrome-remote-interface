"""Generated client domain annotations. Do not edit manually."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .domains.accessibility import Accessibility
    from .domains.animation import AnimationDomain
    from .domains.audits import Audits
    from .domains.autofill import Autofill
    from .domains.background_service import BackgroundService
    from .domains.browser import Browser
    from .domains.cache_storage import CacheStorage
    from .domains.cast import Cast
    from .domains.console import Console
    from .domains.css import CSS
    from .domains.database import DatabaseDomain
    from .domains.debugger import Debugger
    from .domains.device_access import DeviceAccess
    from .domains.device_orientation import DeviceOrientation
    from .domains.dom import DOM
    from .domains.dom_debugger import DOMDebugger
    from .domains.dom_snapshot import DOMSnapshot
    from .domains.dom_storage import DOMStorage
    from .domains.emulation import Emulation
    from .domains.event_breakpoints import EventBreakpoints
    from .domains.fed_cm import FedCm
    from .domains.fetch import Fetch
    from .domains.headless_experimental import HeadlessExperimental
    from .domains.heap_profiler import HeapProfiler
    from .domains.indexed_db import IndexedDB
    from .domains.input import Input
    from .domains.inspector import Inspector
    from .domains.io import IO
    from .domains.layer_tree import LayerTree
    from .domains.log import Log
    from .domains.media import Media
    from .domains.memory import Memory
    from .domains.network import Network
    from .domains.overlay import Overlay
    from .domains.page import Page
    from .domains.performance import Performance
    from .domains.performance_timeline import PerformanceTimeline
    from .domains.preload import Preload
    from .domains.profiler import Profiler
    from .domains.runtime import Runtime
    from .domains.schema import Schema
    from .domains.security import Security
    from .domains.service_worker import ServiceWorker
    from .domains.storage import Storage
    from .domains.system_info import SystemInfo
    from .domains.target import Target
    from .domains.tethering import Tethering
    from .domains.tracing import Tracing
    from .domains.web_audio import WebAudio
    from .domains.web_authn import WebAuthn


class DomainHints:
    Accessibility: Accessibility
    Animation: AnimationDomain
    Audits: Audits
    Autofill: Autofill
    BackgroundService: BackgroundService
    Browser: Browser
    CSS: CSS
    CacheStorage: CacheStorage
    Cast: Cast
    DOM: DOM
    DOMDebugger: DOMDebugger
    EventBreakpoints: EventBreakpoints
    DOMSnapshot: DOMSnapshot
    DOMStorage: DOMStorage
    Database: DatabaseDomain
    DeviceOrientation: DeviceOrientation
    Emulation: Emulation
    HeadlessExperimental: HeadlessExperimental
    IO: IO
    IndexedDB: IndexedDB
    Input: Input
    Inspector: Inspector
    LayerTree: LayerTree
    Log: Log
    Memory: Memory
    Network: Network
    Overlay: Overlay
    Page: Page
    Performance: Performance
    PerformanceTimeline: PerformanceTimeline
    Security: Security
    ServiceWorker: ServiceWorker
    Storage: Storage
    SystemInfo: SystemInfo
    Target: Target
    Tethering: Tethering
    Tracing: Tracing
    Fetch: Fetch
    WebAudio: WebAudio
    WebAuthn: WebAuthn
    Media: Media
    DeviceAccess: DeviceAccess
    Preload: Preload
    FedCm: FedCm
    Console: Console
    Debugger: Debugger
    HeapProfiler: HeapProfiler
    Profiler: Profiler
    Runtime: Runtime
    Schema: Schema
