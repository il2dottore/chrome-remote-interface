from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from tools.generate_domains import generate


class GeneratorTests(unittest.TestCase):
    def test_writes_one_module_per_domain_and_removes_stale_modules(self) -> None:
        descriptor = {
            "version": {"major": "1", "minor": "0"},
            "domains": [
                {
                    "domain": "Alpha",
                    "types": [
                        {
                            "id": "Identifier",
                            "type": "string",
                        }
                    ],
                    "commands": [
                        {
                            "name": "lookup",
                            "parameters": [
                                {"name": "id", "$ref": "Identifier"},
                            ],
                            "returns": [
                                {"name": "found", "type": "boolean"},
                            ],
                        }
                    ],
                },
                {
                    "domain": "BetaDomain",
                    "events": [
                        {
                            "name": "changed",
                            "parameters": [
                                {"name": "id", "$ref": "Alpha.Identifier"},
                            ],
                        }
                    ],
                },
            ],
        }
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            protocol = root / "protocol.json"
            package = root / "cdp"
            domains = package / "domains"
            domains.mkdir(parents=True)
            (domains / "stale.py").write_text("stale", encoding="utf-8")
            protocol.write_text(json.dumps(descriptor), encoding="utf-8")
            generate(protocol, package)
            self.assertTrue((domains / "alpha.py").is_file())
            self.assertTrue((domains / "beta_domain.py").is_file())
            self.assertFalse((domains / "stale.py").exists())
            self.assertIn(
                "class Alpha(BaseDomain)",
                (domains / "alpha.py").read_text(encoding="utf-8"),
            )
            self.assertIn(
                "from .alpha import Alpha",
                (domains / "__init__.py").read_text(encoding="utf-8"),
            )
            self.assertEqual(
                json.loads((package / "protocol.json").read_text(encoding="utf-8")),
                descriptor,
            )


if __name__ == "__main__":
    unittest.main()
