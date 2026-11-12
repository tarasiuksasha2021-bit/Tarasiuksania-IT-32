
import json
from datetime import date

print("Oleksandr Tarasiuk, IT-32")

with open("data/expenses.json", "r", encoding="utf-8") as file:
    records = json.load(file)

new_record = {
    "date": date.today().isoformat(),
    "category": "food",
    "amount": 50.0,
    "comment": "new expense"
}

records.append(new_record)
added = 1

old_count = len(records)

records = [record for record in records if record["amount"] >= 10]

deleted = old_count - len(records)

with open("data/expenses_updated.json", "w", encoding="utf-8") as file:
    json.dump(records, file, indent=2, ensure_ascii=False)

print(f"added: {added}")
print(f"deleted: {deleted}")
print(f"records: {len(records)}")
print("saved: data/expenses_updated.json")
