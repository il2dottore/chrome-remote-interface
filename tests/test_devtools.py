from __future__ import annotations

import unittest
from unittest.mock import AsyncMock, patch

from cdp.devtools import Activate, Close, List, New, Protocol, Version


class DevtoolsTests(unittest.IsolatedAsyncioTestCase):
    async def test_local_protocol_does_not_make_an_http_request(self) -> None:
        with patch("cdp.devtools._request", new_callable=AsyncMock) as request:
            descriptor = await Protocol({"local": True, "port": 1})
        request.assert_not_awaited()
        self.assertEqual(descriptor["version"], {"major": "1", "minor": "3"})
        domains = descriptor["domains"]
        if not isinstance(domains, list):
            self.fail("local descriptor domains must be an array")
        self.assertGreater(len(domains), 40)

    async def test_discovery_helpers_use_node_compatible_endpoints(self) -> None:
        responses = [
            b"[]",
            b'{"id":"new","type":"page","title":"","url":"about:blank"}',
            b"",
            b"",
            b'{"Browser":"Chrome"}',
        ]
        request = AsyncMock(side_effect=responses)
        with patch("cdp.devtools._request", request):
            self.assertEqual(await List(), [])
            target = await New({"url": "about:blank"})
            await Activate("new")
            await Close({"id": "new"})
            info = await Version()
        self.assertEqual(target["id"], "new")
        self.assertEqual(info.get("Browser"), "Chrome")
        self.assertEqual(request.await_args_list[0].args[0], "/json/list")
        self.assertEqual(request.await_args_list[1].args[0], "/json/new?about:blank")
        self.assertEqual(request.await_args_list[1].args[1]["method"], "PUT")
        self.assertEqual(request.await_args_list[2].args[0], "/json/activate/new")
        self.assertEqual(request.await_args_list[3].args[0], "/json/close/new")
        self.assertEqual(request.await_args_list[4].args[0], "/json/version")


if __name__ == "__main__":
    unittest.main()
