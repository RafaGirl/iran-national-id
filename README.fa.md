[English](README.md) • [فارسی](README.fa.md)

> <img src="icon.png" alt="Iran National ID icon" width="128" height="128">

# iran-national-id (فارسی)

اعتبارسنجی و تفسیر «کد ملی ایران» و نگاشت سه رقم اول به **استان/شهر صدور** با استفاده از یک دیتاست JSON.

* فقط **توابع** تمیز و قابل تست (اسکریپت مستقل ندارد).
* فایل دیتای پیش‌فرض: `src/iran_national_id/data/iran_codes.json` (بر اساس جدول تأییدشده‌ی شما).
* کلیدهای ورودی/خروجی **انگلیسی** هستند؛ معادل فارسی در `province_fa` و `city_fa` نگهداری می‌شود.

## نصب (محلی)

```
pip install -e .
```

## استفاده سریع

```
from iran_national_id import compute_check_digit, is_valid, describe

code = "1360000003"

print(is_valid(code))                 # True / False
print(compute_check_digit(code[:9]))  # رقم کنترل محاسبه‌شده

info = describe(code)                 # dict شامل جزئیات
import json
print(json.dumps(info, ensure_ascii=False, indent=2))
```

نمونه خروجی تابع `describe`:

```
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

> اگر نسخه‌ی نهایی و تأییدشده‌ی `iran_codes.json` را دارید، کافی است فایل را با مسیر زیر **جایگزین** کنید:
> `src/iran_national_id/data/iran_codes.json`
> کتابخانه به‌صورت پیش‌فرض از همین مسیر می‌خواند.

## API خلاصه

* `is_valid(code: str) -> bool`
  بررسی می‌کند `code` دقیقاً ۱۰ رقم باشد، همه ارقام یکسان نباشند (مثل `0000000000`)، و رقم کنترل با فرمول استاندارد **مطابقت** داشته باشد.

* `compute_check_digit(nine: str) -> int`
  رقم دهم را از روی ۹ رقم اول محاسبه می‌کند. فرمول دقیق:

  * وزن‌ها: ۲ تا ۱۰ از راست به چپ یا ۱۰ تا ۲ از چپ به راست برای ۹ رقم اول.
  * جمع وزن‌دار = Σ (رقمᵢ × وزنᵢ)
  * r = جمع وزن‌دار % 11
    اگر `r < 2` ⇒ رقم کنترل = `r`، در غیر این صورت ⇒ `11 - r`.

* `describe(code: str) -> dict`
  خروجی ساخت‌یافته شامل:

  * `input`، `normalized`، `is_valid`
  * بخش `math` با `weights`, `digits`, `terms`, `sum`, `mod`, `expected_digit`, `last_digit`
  * `first3` (سه رقم اول)
  * `issuance` با `province_fa`, `city_fa` (اگر نگاشت موجود باشد)

## دربارهٔ داده‌ها

* فایل JSON شامل آرایه‌ای از استان‌هاست که برای هر استان، کدهای سه‌رقمی و شهرها با بازه/لیست کدهایشان آمده است.
* تابع‌های داخلی، نگاشت را در حافظه کش می‌کنند و برای بازه‌ها (مثل `149-150`) تمامی کدهای ممکن را گسترش می‌دهند تا جستجوی سریع کلید سه‌رقمی فراهم شود.

## تست و کیفیت کد

* اجرای تست‌ها:

  ```
  python -m pytest
  ```

* بررسی استایل/لینت با Ruff:

  ```
  python -m ruff check .
  ```

## مجوز

MIT

[English](README.md) • [فارسی](README.fa.md)
