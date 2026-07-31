"""Create a target and send Page commands through its session."""

from __future__ import annotations

import asyncio

from cdp import Version, connect


async def main() -> None:
    """Create, attach to, navigate, and close a temporary target."""

    version = await Version()
    browser_url = version.get("webSocketDebuggerUrl")
    if browser_url is None:
        raise RuntimeError("Chrome did not provide a browser websocket URL")

    browser = await connect(browser_url)
    target_id: str | None = None
    try:
        created = await browser.Target.createTarget(url="about:blank")
        target_id = created["targetId"]
        attached = await browser.Target.attachToTarget(
            targetId=target_id,
            flatten=True,
        )
        session_id = attached["sessionId"]

        await browser.Page.enable(session_id=session_id)
        load_event = browser.Page.loadEventFired(session_id=session_id)
        await browser.Page.navigate(
            url="https://example.com",
            session_id=session_id,
        )
        await load_event
        print(f"Loaded target {target_id} in session {session_id}")
    finally:
        try:
            if target_id is not None:
                await browser.Target.closeTarget(targetId=target_id)
        finally:
            await browser.close()


if __name__ == "__main__":
    asyncio.run(main())
