
import csv
import json
import os

print("Oleksandr Tarasiuk, IT-32")

records = []

with open("data/expenses.csv", "r", encoding="utf-8") as file:
    for line in file:
        if not line.strip() or line.lstrip().startswith("#"):
            continue

        date, category, amount, comment = line.strip().split(";")

        records.append({
            "date": date,
            "category": category,
            "amount": float(amount),
            "comment": comment
        })

with open("data/expenses.json", "w", encoding="utf-8") as file:
    json.dump(records, file, indent=2, ensure_ascii=False)

size = os.path.getsize("data/expenses.json")

print(f"records: {len(records)}")
print(f"saved: data/expenses.json ({size} bytes)")
