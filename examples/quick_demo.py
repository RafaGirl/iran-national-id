from iran_national_id import describe
import json

code = "1360000003"
info = describe(code)
print(json.dumps(info, ensure_ascii=False, indent=2))
