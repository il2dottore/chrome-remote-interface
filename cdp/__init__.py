"""Low-level asynchronous Python client for Chrome DevTools Protocol."""

from .client import CDP, Chrome, Client, connect
from .devtools import (
    Activate,
    Close,
    List,
    New,
    Protocol,
    Version,
    activate_target,
    close_target,
    list_targets,
    new_target,
    protocol,
    version,
)
from .errors import ConnectionClosedError, ProtocolError
from .types import JsonObject, JsonValue, ProtocolDescriptor, Target, VersionInfo

__all__ = [
    "CDP",
    "Activate",
    "Chrome",
    "Client",
    "Close",
    "ConnectionClosedError",
    "JsonObject",
    "JsonValue",
    "List",
    "New",
    "Protocol",
    "ProtocolDescriptor",
    "ProtocolError",
    "Target",
    "Version",
    "VersionInfo",
    "activate_target",
    "close_target",
    "connect",
    "list_targets",
    "new_target",
    "protocol",
    "version",
]
