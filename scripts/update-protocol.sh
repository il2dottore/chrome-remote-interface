#!/usr/bin/env bash

set -euo pipefail

root="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
protocol="$root/chrome-remote-interface/lib/protocol.json"
base="${CDP_PROTOCOL_BASE_URL:-https://raw.githubusercontent.com/ChromeDevTools/devtools-protocol/master/json}"
python_cmd="${PYTHON:-}"
if [[ -z "$python_cmd" ]]; then
    if command -v python >/dev/null 2>&1; then
        python_cmd=python
    else
        python_cmd=python3
    fi
fi
temporary_directory="$(mktemp -d)"
trap 'rm -rf "$temporary_directory"' EXIT

"$python_cmd" - "$base" "$temporary_directory/protocol.json" <<'PY'
from __future__ import annotations

import json
import sys
from pathlib import Path
from urllib.request import urlopen


base_url = sys.argv[1].rstrip("/")
output_path = Path(sys.argv[2])


def fetch(name: str) -> dict[str, object]:
    with urlopen(f"{base_url}/{name}", timeout=30) as response:
        value: object = json.load(response)
    if not isinstance(value, dict):
        raise ValueError(f"{name} does not contain a JSON object")
    return value


browser_protocol = fetch("browser_protocol.json")
js_protocol = fetch("js_protocol.json")
browser_domains = browser_protocol.get("domains")
js_domains = js_protocol.get("domains")
if not isinstance(browser_domains, list) or not isinstance(js_domains, list):
    raise ValueError("protocol descriptors must contain a domains array")

merged_protocol = dict(browser_protocol)
merged_protocol["domains"] = [*browser_domains, *js_domains]
output_path.write_text(
    json.dumps(merged_protocol, indent=4, ensure_ascii=False) + "\n",
    encoding="utf-8",
)
PY

mv "$temporary_directory/protocol.json" "$protocol"
"$python_cmd" "$root/tools/generate_domains.py" "$protocol"
