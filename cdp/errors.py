"""Exceptions raised by :mod:`cdp`."""

from __future__ import annotations

from .types import JsonObject


class ProtocolError(Exception):
    """An error response returned by a CDP endpoint."""

    def __init__(self, request: JsonObject, response: JsonObject) -> None:
        message = str(response.get("message", "Chrome DevTools Protocol error"))
        data = response.get("data")
        if data is not None:
            message = f"{message} ({data})"
        super().__init__(message)
        self.request = request
        self.response = response


class ConnectionClosedError(ConnectionError):
    """Raised when a command cannot complete because the socket closed."""
