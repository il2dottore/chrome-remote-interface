"""Observe requests emitted by the Network domain."""

from __future__ import annotations

import asyncio

from cdp import connect
from cdp.domains.network import RequestWillBeSentEvent


def print_request(event: RequestWillBeSentEvent) -> None:
    """Print the URL from a typed ``Network.requestWillBeSent`` event."""

    print(f"request: {event['request']['method']} {event['request']['url']}")


async def main() -> None:
    """Subscribe to requests, navigate, then unsubscribe."""

    client = await connect()
    try:
        await client.Network.enable()
        unsubscribe = client.Network.requestWillBeSent(print_request)
        try:
            await client.Page.enable()
            await client.Page.navigate(url="https://example.com")
            await asyncio.sleep(2)
        finally:
            unsubscribe()
    finally:
        await client.close()


if __name__ == "__main__":
    asyncio.run(main())
