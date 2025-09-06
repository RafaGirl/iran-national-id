# SPDX-License-Identifier: MIT
# (c) 2025 - iran-national-id
"""Utilities for validating and decoding Iranian national ID numbers (کد ملی).

Public API (functions):
- compute_check_digit(nine: str) -> int
- is_valid(code: str) -> bool
- describe(code: str, *, codes: dict | None = None) -> dict

The default province/city mapping is loaded from the embedded JSON file (data/iran_codes.json).
You can override by passing a parsed mapping (same schema as the JSON) to `describe`.
"""

from .validator import compute_check_digit, is_valid
from .codes import describe

__all__ = [
    "compute_check_digit",
    "is_valid",
    "describe",
]
