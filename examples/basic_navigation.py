"""Navigate a page and wait for its load event."""

from __future__ import annotations

import asyncio

from cdp import connect


async def main() -> None:
    """Open example.com in the first page exposed by Chrome."""

    client = await connect()
    try:
        await client.Page.enable()
        load_event = client.Page.loadEventFired()
        navigation = await client.Page.navigate(url="https://example.com")
        await load_event
        print(f"Navigated frame: {navigation['frameId']}")
    finally:
        await client.close()


if __name__ == "__main__":
    asyncio.run(main())
