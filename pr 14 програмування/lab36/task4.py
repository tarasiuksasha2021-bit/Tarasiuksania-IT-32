
import json
from datetime import date

print("Oleksandr Tarasiuk, IT-32")

today = date.today()

data = {
    "owner": "Oleksandr Tarasiuk",
    "group": "IT-32",
    "date": today
}

# Перша спроба без обробки дати
try:
    json.dumps(data)
except TypeError as error:
    print("TypeError:", error)

# Спосіб 1: використання default
def date_to_iso(obj):
    if isinstance(obj, date):
        return obj.isoformat()
    raise TypeError("Unsupported type")

json_text = json.dumps(data, default=date_to_iso, ensure_ascii=False)
restored = json.loads(json_text)
restored["date"] = date.fromisoformat(restored["date"])

print("default method:", restored == data)

# Спосіб 2: власне кодування та декодування
def encode_dates(obj):
    if isinstance(obj, date):
        return obj.isoformat()
    if isinstance(obj, dict):
        return {key: encode_dates(value) for key, value in obj.items()}
    if isinstance(obj, list):
        return [encode_dates(value) for value in obj]
    return obj

def decode_dates(obj):
    if isinstance(obj, dict):
        result = {}
        for key, value in obj.items():
            if key == "date" and isinstance(value, str):
                result[key] = date.fromisoformat(value)
            else:
                result[key] = decode_dates(value)
        return result
    if isinstance(obj, list):
        return [decode_dates(value) for value in obj]
    return obj

json_text = json.dumps(encode_dates(data), ensure_ascii=False)
restored = decode_dates(json.loads(json_text))

print("custom method:", restored == data)
print("date type:", type(restored["date"]).__name__)
