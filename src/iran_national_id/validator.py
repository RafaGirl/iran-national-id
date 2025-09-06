# SPDX-License-Identifier: MIT
from __future__ import annotations

import re

_DIGITS_RE_9 = re.compile(r"^\d{9}$")
_DIGITS_RE_10 = re.compile(r"^\d{10}$")


def compute_check_digit(nine: str) -> int:
    """
    Compute the Iranian national ID (کد ملی) check digit from the first 9 digits.

    Math:
        Let s = Σ_{i=0..8} d[i] * (10 - i)
        r = s mod 11
        check = r  if r < 2 else 11 - r

    Args:
        nine: A string of 9 ASCII digits.

    Returns:
        The check digit (0..9) as an integer.

    Raises:
        ValueError: If `nine` is not exactly 9 digits.
    """
    if not isinstance(nine, str) or not _DIGITS_RE_9.fullmatch(nine):
        raise ValueError("nine must be a 9-digit string")
    s = sum(int(nine[i]) * (10 - i) for i in range(9))
    r = s % 11
    return r if r < 2 else 11 - r


def is_valid(code: str) -> bool:
    """
    Validate a full 10-digit Iranian national ID.

    Rules:
    - Must be 10 digits.
    - Cannot be 10 identical digits (e.g., '0000000000').
    - The 10th digit must match the computed check digit of the first nine.

    Args:
        code: A string of 10 ASCII digits.

    Returns:
        True if valid, False otherwise.
    """
    if not isinstance(code, str) or not _DIGITS_RE_10.fullmatch(code):
        return False
    if code == code[0] * 10:
        return False
    return int(code[9]) == compute_check_digit(code[:9])
