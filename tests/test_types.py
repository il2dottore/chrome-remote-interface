from __future__ import annotations

import math
import unittest

from cdp.types import to_json_value


class JsonValueTests(unittest.TestCase):
    def test_non_finite_numbers_are_rejected(self) -> None:
        for value in (math.nan, math.inf, -math.inf):
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    to_json_value(value)


if __name__ == "__main__":
    unittest.main()
