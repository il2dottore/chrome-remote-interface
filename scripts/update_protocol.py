"""Fetch, merge, and generate the Chrome DevTools Protocol bindings."""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import TypeAlias, cast
from urllib.request import urlopen

JsonValue: TypeAlias = (
    bool | int | float | str | list["JsonValue"] | dict[str, "JsonValue"] | None
)
JsonObject: TypeAlias = dict[str, JsonValue]

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_PROTOCOL = ROOT / "chrome-remote-interface" / "lib" / "protocol.json"
DEFAULT_BASE_URL = (
    "https://raw.githubusercontent.com/ChromeDevTools/devtools-protocol/master/json"
)
GENERATOR = ROOT / "tools" / "generate_domains.py"


def normalize_json(value: object) -> JsonValue:
    """Convert a decoded JSON value into a bounded recursive type."""

    if value is None or isinstance(value, bool | int | float | str):
        return value
    if isinstance(value, list):
        return [normalize_json(item) for item in cast(list[object], value)]
    if isinstance(value, dict):
        result: JsonObject = {}
        for key, item in cast(dict[object, object], value).items():
            if not isinstance(key, str):
                raise ValueError("JSON object key is not a string")
            result[key] = normalize_json(item)
        return result
    raise ValueError(f"Unsupported JSON value: {type(value).__name__}")


def fetch_descriptor(base_url: str, name: str) -> JsonObject:
    """Fetch one protocol descriptor from ``base_url``."""

    with urlopen(f"{base_url.rstrip('/')}/{name}", timeout=30) as response:
        raw: object = json.load(response)
    value = normalize_json(raw)
    if not isinstance(value, dict):
        raise ValueError(f"{name} does not contain a JSON object")
    return value


def merge_descriptors(
    browser_protocol: JsonObject, js_protocol: JsonObject
) -> JsonObject:
    """Merge the browser and JavaScript protocol domain lists."""

    browser_domains = browser_protocol.get("domains")
    js_domains = js_protocol.get("domains")
    if not isinstance(browser_domains, list) or not isinstance(js_domains, list):
        raise ValueError("protocol descriptors must contain a domains array")
    merged_protocol = dict(browser_protocol)
    merged_protocol["domains"] = [*browser_domains, *js_domains]
    return merged_protocol


def update_protocol(
    protocol_path: Path,
    base_url: str,
    generator_path: Path = GENERATOR,
) -> None:
    """Update ``protocol_path`` and regenerate the Python domain bindings."""

    protocol_path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(
        prefix=".update-protocol-", dir=protocol_path.parent
    ) as temporary_directory:
        temporary_path = Path(temporary_directory) / "protocol.json"
        browser_protocol = fetch_descriptor(base_url, "browser_protocol.json")
        js_protocol = fetch_descriptor(base_url, "js_protocol.json")
        merged_protocol = merge_descriptors(browser_protocol, js_protocol)
        temporary_path.write_text(
            json.dumps(merged_protocol, indent=4, ensure_ascii=False) + "\n",
            encoding="utf-8",
            newline="\n",
        )
        temporary_path.replace(protocol_path)

    subprocess.run(
        [sys.executable, str(generator_path), str(protocol_path)],
        check=True,
        cwd=ROOT,
    )


def main() -> None:
    """Run the protocol update command."""

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--base-url",
        default=os.environ.get("CDP_PROTOCOL_BASE_URL", DEFAULT_BASE_URL),
        help="base URL containing browser_protocol.json and js_protocol.json",
    )
    arguments = parser.parse_args()
    update_protocol(DEFAULT_PROTOCOL, arguments.base_url)


if __name__ == "__main__":
    main()
