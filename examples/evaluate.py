"""Evaluate JavaScript and handle an optional CDP result value."""

from __future__ import annotations

import asyncio

from cdp import connect


async def main() -> None:
    """Print the title of the currently open page."""

    client = await connect()
    try:
        result = await client.Runtime.evaluate(
            expression="document.title",
            returnByValue=True,
        )
        remote_object = result["result"]
        if "value" not in remote_object:
            description = remote_object.get("description")
            raise RuntimeError(description or "the expression returned no value")
        print(remote_object["value"])
    finally:
        await client.close()


if __name__ == "__main__":
    asyncio.run(main())
