from __future__ import annotations

import asyncio
import json
import unittest
from typing import cast

from cdp.client import Client
from cdp.domain import DynamicDomain
from cdp.domains.network import RequestWillBeSentEvent
from cdp.errors import ConnectionClosedError, ProtocolError
from cdp.types import JsonObject, ProtocolDescriptor, to_json_value


class FakeWebSocket:
    def __init__(self) -> None:
        self.incoming: asyncio.Queue[str] = asyncio.Queue()
        self.sent: asyncio.Queue[str] = asyncio.Queue()
        self.closed = False

    async def send(self, message: str) -> None:
        if self.closed:
            raise ConnectionClosedError("closed")
        await self.sent.put(message)

    async def recv(self) -> str:
        return await self.incoming.get()

    async def close(self) -> None:
        self.closed = True


DESCRIPTOR = cast(
    ProtocolDescriptor,
    {
        "version": {"major": "1", "minor": "3"},
        "domains": [
            {"domain": "Page"},
            {"domain": "Network"},
        ],
    },
)


class ClientTests(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self) -> None:
        self.websocket = FakeWebSocket()
        self.client = Client(
            self.websocket,
            "ws://localhost/devtools/page/test",
            DESCRIPTOR,
        )

    async def asyncTearDown(self) -> None:
        await self.client.close()

    async def _sent(self) -> JsonObject:
        raw: object = json.loads(await self.websocket.sent.get())
        value = to_json_value(raw)
        if not isinstance(value, dict):
            raise TypeError("sent WebSocket message was not an object")
        return value

    async def test_generated_command_shorthand(self) -> None:
        command = asyncio.create_task(
            self.client.Page.navigate(
                url="https://example.com",
                session_id="session-1",
            )
        )
        request = await self._sent()
        self.assertEqual(request["method"], "Page.navigate")
        self.assertEqual(request["params"], {"url": "https://example.com"})
        self.assertEqual(request["sessionId"], "session-1")
        await self.websocket.incoming.put(
            json.dumps(
                {
                    "id": request["id"],
                    "result": {"frameId": "frame-1"},
                }
            )
        )
        self.assertEqual(await command, {"frameId": "frame-1"})

    async def test_protocol_error_retains_request_and_response(self) -> None:
        command = asyncio.create_task(
            self.client.send("Network.getResponseBody", {"requestId": "missing"})
        )
        request = await self._sent()
        response = {"code": -32000, "message": "No resource"}
        await self.websocket.incoming.put(
            json.dumps({"id": request["id"], "error": response})
        )
        with self.assertRaises(ProtocolError) as caught:
            await command
        self.assertEqual(caught.exception.request["method"], "Network.getResponseBody")
        self.assertEqual(caught.exception.response, response)

    async def test_event_wait_callback_and_session_filter(self) -> None:
        callback_payloads: list[RequestWillBeSentEvent] = []
        unsubscribe = self.client.Network.requestWillBeSent(
            callback_payloads.append,
            session_id="session-1",
        )
        event = self.client.Network.requestWillBeSent(session_id="session-1")
        await self.websocket.incoming.put(
            json.dumps(
                {
                    "method": "Network.requestWillBeSent",
                    "params": {"requestId": "one"},
                    "sessionId": "another-session",
                }
            )
        )
        await asyncio.sleep(0)
        self.assertEqual(callback_payloads, [])
        await self.websocket.incoming.put(
            json.dumps(
                {
                    "method": "Network.requestWillBeSent",
                    "params": {"requestId": "two"},
                    "sessionId": "session-1",
                }
            )
        )
        self.assertEqual(await event, {"requestId": "two"})
        self.assertEqual(callback_payloads, [{"requestId": "two"}])
        unsubscribe()

    async def test_close_is_idempotent_and_rejects_send(self) -> None:
        await self.client.close()
        await self.client.close()
        with self.assertRaises(ConnectionClosedError):
            await self.client.send("Page.enable")

    async def test_remote_protocol_additions_are_available_dynamically(self) -> None:
        await self.client.close()
        descriptor = cast(
            ProtocolDescriptor,
            {
                "domains": [
                    {
                        "domain": "Future",
                        "commands": [{"name": "doThing"}],
                        "events": [{"name": "thingDone"}],
                    }
                ]
            },
        )
        websocket = FakeWebSocket()
        client = Client(websocket, "ws://localhost/future", descriptor)
        try:
            future_domain = cast(DynamicDomain, client["Future"])
            command = asyncio.create_task(future_domain.command("doThing", value=42))
            raw_request: object = json.loads(await websocket.sent.get())
            normalized_request = to_json_value(raw_request)
            if not isinstance(normalized_request, dict):
                raise TypeError("command request was not an object")
            request = normalized_request
            self.assertEqual(request["method"], "Future.doThing")
            self.assertEqual(request["params"], {"value": 42})
            await websocket.incoming.put(
                json.dumps({"id": request["id"], "result": {"ok": True}})
            )
            self.assertEqual(await command, {"ok": True})
        finally:
            await client.close()


if __name__ == "__main__":
    unittest.main()
