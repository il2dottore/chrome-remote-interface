# Examples

These examples use the asynchronous `cdp` client and the generated domain
modules. Run them from the repository root with Python 3.10 or newer:

```console
python -m examples.basic_navigation
python -m examples.evaluate
python -m examples.network_events
python -m examples.target_sessions
```

Start Chrome with the remote debugging endpoint enabled before running an
example. On Windows, for example:

```console
chrome.exe --remote-debugging-port=9222 --user-data-dir=%TEMP%\cdp-example
```

The scripts demonstrate these domains and client features:

- `basic_navigation.py` uses the `Page` domain to enable page events,
  navigate, and wait for `Page.loadEventFired`.
- `evaluate.py` uses `Runtime.evaluate` and shows how to narrow the optional
  `RemoteObject.value` field safely.
- `network_events.py` enables the `Network` domain and subscribes to the
  typed `Network.requestWillBeSent` event.
- `target_sessions.py` uses the browser websocket, then creates and attaches
  to a target through the `Target` domain. Commands are sent to that target by
  passing its `session_id`.

The examples intentionally keep the API calls small. For the complete list of
generated domains, commands, events, and types, see [`cdp/domains/`](../cdp/domains/)
and the [project README](../README.md).
