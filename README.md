[English](README.md) • [فارسی](README.fa.md)

# iran-national-id

Validate and decode Iranian national ID numbers (کد ملی) and map the first 3 digits to the **issuance province/city** using a JSON dataset.

* Clean, testable **functions only** (no scripts).
* Default data file: `src/iran_national_id/data/iran_codes.json` (based on your verified table).
* I/O keys are **English**; Persian labels are kept under `province_fa` / `city_fa`.

## Install (local)

```bash
pip install -e .
```

## Quick usage

```python
from iran_national_id import compute_check_digit, is_valid, describe

code = "1360000003"

print(is_valid(code))                 # True / False
print(compute_check_digit(code[:9]))  # check digit from first 9 digits

info = describe(code)                 # dict with details
import json
print(json.dumps(info, ensure_ascii=False, indent=2))
```

Sample `describe` output:

```json
{
  "input": "1360000003",
  "normalized": "1360000003",
  "is_valid": true,
  "math": {
    "weights": [10, 9, 8, 7, 6, 5, 4, 3, 2],
    "digits":  [1, 3, 6, 2, 9, 1, 9, 4, 1],
    "terms":   [10, 27, 48, 14, 54, 5, 36, 12, 2],
    "sum": 208,
    "mod": 10,
    "expected_digit": 1,
    "last_digit": 1
  },
  "first3": "136",
  "issuance": {
    "province_fa": "آذربایجان شرقی",
    "city_fa": "تبریز"
  }
}
```

> If you already have your finalized `iran_codes.json`, simply **replace**:
> `src/iran_national_id/data/iran_codes.json`
> The library reads from this path by default.

## API summary

* `is_valid(code: str) -> bool`
  Ensures `code` is exactly 10 digits, not all identical (e.g., `0000000000`), and the control digit matches the standard formula.

* `compute_check_digit(nine: str) -> int`
  Returns the 10th digit from the first 9 digits. Math:

  * Weights: 10..2 (left to right over the first 9 digits).
  * Weighted sum = Σ(digitᵢ × weightᵢ)
  * `r = sum % 11`
    If `r < 2` ⇒ check digit = `r`; else ⇒ `11 - r`.

* `describe(code: str) -> dict`
  Structured output including:

  * `input`, `normalized`, `is_valid`
  * `math` with `weights`, `digits`, `terms`, `sum`, `mod`, `expected_digit`, `last_digit`
  * `first3` (first three digits)
  * `issuance` with `province_fa`, `city_fa` (when mapping exists)

## About the data

* The JSON file contains an array of provinces; each province lists its 3-digit prefixes and cities with ranges/lists of codes.
* Internals cache the mapping and expand ranges (e.g., `149-150`) to enable fast lookups by the 3-digit key.

## Tests & code quality

* Run tests:

  ```bash
  python -m pytest
  ```

* Lint/style with Ruff:

  ```bash
  python -m ruff check .
  ```

* Coverage:

  ```bash
  pytest --cov
  ```

## License

MIT

[English](README.md) • [فارسی](README.fa.md)
