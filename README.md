# chrome-remote-interface

`chrome-remote-interface` is a low-level, asynchronous Python client for the
[Chrome DevTools Protocol (CDP)](https://chromedevtools.github.io/devtools-protocol/).
It is a Python port of the Node.js
[chrome-remote-interface](https://github.com/cyrus-and/chrome-remote-interface)
package.

The library gives you direct access to Chrome and Chromium debugging domains
over WebSocket. It intentionally stays close to CDP: it does not add browser
automation concepts such as locators, page objects, or selectors.

## Features

- Async WebSocket client built for `asyncio`.
- One generated, typed Python module for every CDP domain.
- Typed commands, parameters, results, events, payloads, aliases, and enums.
- Event listeners with either callbacks or awaitable one-shot waits.
- Flattened CDP sessions through the `session_id` argument.
- Chrome discovery helpers compatible with the Node.js package.
- Raw `client.send(...)` access for protocol additions not in the bundled schema.
- Command-line tools for listing targets, creating targets, and inspecting a
  running browser.

## Requirements

- Python 3.10 or newer.
- Chrome or Chromium started with remote debugging enabled.

Install the package from PyPI:

```console
python -m pip install chrome-remote-interface
```

Start a debugging browser on the default endpoint (`localhost:9222`):

```console
chrome --remote-debugging-port=9222
```

For a separate profile, add `--user-data-dir` so that the command can run next
to an existing Chrome instance. See [`examples/README.md`](examples/README.md)
for a complete setup and runnable examples.

## Publishing a release

The workflow in [`.github/workflows/publish.yml`](.github/workflows/publish.yml)
validates and publishes a package to PyPI whenever a tag matching `v*` is
pushed. It uses PyPI Trusted Publishing (GitHub Actions OIDC), so no API token
is stored in the repository.

Before the first release, configure a PyPI Trusted Publisher for this GitHub
repository with workflow `publish.yml` and environment `pypi`. Then bump the
version in `pyproject.toml`, commit it, and push a matching unique tag:

```console
git tag v1.0.2
git push origin v1.0.2
```

The workflow rejects tags whose version does not match `pyproject.toml`.

## Quick start

The package is installed as `chrome-remote-interface` but imported as `cdp`:

```python
import asyncio

from cdp import connect


async def main() -> None:
    client = await connect()
    try:
        await client.Page.enable()

        loaded = client.Page.loadEventFired()
        navigation = await client.Page.navigate(url="https://example.com")
        await loaded
        print(f"Loaded frame: {navigation['frameId']}")
    finally:
        await client.close()


asyncio.run(main())
```

`connect()` applies its `timeout` to discovery and the WebSocket handshake.
For long-running commands, set `command_timeout` to bound how long a command
may wait for a response. A timed-out command is cancelled and removed from the
pending-request table:

```python
client = await connect(command_timeout=10)
try:
    await client.Page.enable()
finally:
    await client.close()
```

The connection close handshake is bounded by `close_timeout` (five seconds by
default). You can also use the async context manager to guarantee cleanup:

```python
client = await connect()
async with client:
    await client.Page.enable()
```

Every command can use keyword arguments or a parameter mapping. Generated
domain methods return typed dictionaries, so editors can provide completion
and report incorrect fields before runtime.

## Events and JavaScript

Subscribe to a typed event with a callback and keep the unsubscribe function:

```python
from cdp.domains.network import RequestWillBeSentEvent


def on_request(event: RequestWillBeSentEvent) -> None:
    print(event["request"]["url"])


unsubscribe = client.Network.requestWillBeSent(on_request)
await client.Network.enable()

# Later:
unsubscribe()
```

Listeners registered with a `session_id` are removed automatically when Chrome
emits `Target.detachedFromTarget`. They can also be removed explicitly with
`client.remove_session_listeners(session_id)`.

CDP values can be optional according to the protocol schema. Narrow them
before indexing them:

```python
result = await client.Runtime.evaluate(
    expression="document.title",
    returnByValue=True,
)
remote_object = result["result"]
if "value" in remote_object:
    print(remote_object["value"])
```

## Targets and sessions

The HTTP helpers can list inspectable targets and connect to a specific page:

```python
from cdp import List, connect


targets = await List()
page = next(target for target in targets if target["type"] == "page")
client = await connect(page["id"])
```

For browser-level connections, attach to a target and pass its session ID to
subsequent domain commands:

```python
from cdp import Version, connect


version = await Version()
browser = await connect(version["webSocketDebuggerUrl"])
created = await browser.Target.createTarget(url="about:blank")
attached = await browser.Target.attachToTarget(
    targetId=created["targetId"],
    flatten=True,
)
await browser.Page.enable(session_id=attached["sessionId"])
```

## Discovery helpers

The following async helpers use Chrome's `/json` endpoints and default to
`localhost:9222`:

| Helper | Purpose |
| --- | --- |
| `Version()` | Browser version and browser WebSocket URL |
| `List()` | List inspectable targets |
| `New()` | Create a new target |
| `Activate()` | Activate a target |
| `Close()` | Close a target |
| `Protocol()` | Fetch the browser's protocol descriptor |

Each helper accepts options such as `host`, `port`, `secure`, and `timeout`.
The Node-compatible aliases (`Chrome`, `CDP`, `list_targets`, and so on) are
also exported.

## Generated CDP domains

### Where `protocol.json` comes from

The source descriptor is
[`chrome-remote-interface/lib/protocol.json`](chrome-remote-interface/lib/protocol.json).
It is the merged Chrome DevTools Protocol schema: Chrome's browser domains
plus the JavaScript/runtime domains from the upstream
[`devtools-protocol`](https://github.com/ChromeDevTools/devtools-protocol)
repository. The copy at `cdp/protocol.json` is generated automatically for
`Protocol({"local": True})`; do not edit that copy by hand.

### Updating the schema

To use the exact protocol supported by a running Chrome, first start Chrome
with remote debugging and download its descriptor:

```powershell
Invoke-WebRequest `
    -Uri http://localhost:9222/json/protocol `
    -OutFile chrome-remote-interface/lib/protocol.json
```

Or, from Git Bash, run the repository's update script to fetch and merge the
latest upstream schema used by the original Node.js project:

```bash
bash scripts/update-protocol.sh
```

The script writes the source descriptor and regenerates the Python bindings
automatically. If you only replace the source file manually, regenerate from
the repository root with:

```console
python tools/generate_domains.py
```

The generator validates the descriptor, copies it to `cdp/protocol.json`, and
writes one module per domain under [`cdp/domains/`](cdp/domains/):

```python
from cdp.domains.page import NavigateParameters, NavigateResult
from cdp.domains.runtime import RemoteObject
```

`tools/generate_stubs.py` remains available as a compatibility entry point.
When a connected browser advertises newer protocol members, use
`client.send("Domain.command", ...)` as a typed-safe raw fallback.

## Examples

The [`examples/`](examples/) directory contains small, runnable programs:

- `basic_navigation.py` — `Page.enable`, `Page.navigate`, and load events.
- `evaluate.py` — `Runtime.evaluate` and optional result values.
- `network_events.py` — typed `Network` request events.
- `target_sessions.py` — `Target` creation, attachment, and sessions.

Run them from the repository root with:

```console
python -m examples.basic_navigation
```

## Command-line interface

The package also installs a `chrome-remote-interface` command:

```console
chrome-remote-interface list
chrome-remote-interface new https://example.com
chrome-remote-interface protocol --local
chrome-remote-interface inspect
```

## Development

Install development dependencies and run the full validation suite:

```console
python -m pip install -e ".[dev]"
python tools/generate_domains.py
python -m unittest discover -s tests
ruff format --check .
ruff check .
pyright
python -m build
```

## License

This project is distributed under the [MIT License](LICENSE).
