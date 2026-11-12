import csv
import math
from collections import defaultdict
from tabulate import tabulate

print("Oleksandr Tarasiuk, IT-32")

expenses = defaultdict(list)

with open("data/expenses.csv", "r", encoding="utf-8") as file:
    for line in file:
        if not line.strip() or line.lstrip().startswith("#"):
            continue

        parts = line.strip().split(";")

        if len(parts) != 4:
            continue

        date, category, amount, note = parts

        expenses[category].append(float(amount))

table = []
total_count = 0
total_sum = 0

for category, amounts in sorted(expenses.items()):
    count = len(amounts)
    total = math.fsum(amounts)

    total_count += count
    total_sum += total

    table.append([category, count, total])

table.append(["TOTAL", total_count, total_sum])

print(tabulate(
    table,
    headers=["category", "count", "total"],
    tablefmt="github",
    floatfmt=".2f"
))