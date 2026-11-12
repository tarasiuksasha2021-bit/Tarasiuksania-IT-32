
import math
import sys
from pathlib import Path
from datetime import date, timedelta
from collections import defaultdict

print("Oleksandr Tarasiuk, ІТ-32")

file_path = Path(__file__).parent / "data" / "expenses.csv"

if not file_path.exists():
    print("Помилка: файл expenses.csv не знайдено", file=sys.stderr)
    sys.exit(1)

expenses = defaultdict(list)

with file_path.open(encoding="utf-8-sig") as file:
    for number, line in enumerate(file, 1):
        line = line.strip()

        if not line or line.startswith("#"):
            continue

        try:
            parts = line.split(";")
            day = date.fromisoformat(parts[0])
            amount = float(parts[2].replace(",", "."))

            if amount < 0 or not math.isfinite(amount):
                raise ValueError

            expenses[day].append(amount)

        except (ValueError, IndexError):
            print(
                f"Попередження: рядок {number} пропущено",
                file=sys.stderr
            )

if not expenses:
    print("Немає даних про витрати")
    sys.exit(0)

first = min(expenses)
last = max(expenses)

days = (last - first).days + 1

daily = {}
current = first

while current <= last:
    daily[current] = math.fsum(expenses.get(current, []))
    current += timedelta(days=1)

weekdays = [
    "Monday", "Tuesday", "Wednesday",
    "Thursday", "Friday", "Saturday", "Sunday"
]

totals = [0.0] * 7

for day, amount in daily.items():
    totals[day.weekday()] += amount

total = math.fsum(
    amount
    for values in expenses.values()
    for amount in values
)

average = total / days

variance = math.fsum(
    (value - average) ** 2
    for value in daily.values()
) / days

deviation = math.sqrt(variance)

top_day = max(daily, key=daily.get)
no_spend = sum(value == 0 for value in daily.values())

month_start = date(last.year, last.month, 1)

if last.month == 12:
    next_month = date(last.year + 1, 1, 1)
else:
    next_month = date(last.year, last.month + 1, 1)

month_days = (next_month - month_start).days
days_left = (next_month - last).days
forecast = average * month_days

print(
    f"period: {first:%d.%m.%Y} ({first:%A}) - "
    f"{last:%d.%m.%Y} ({last:%A}), {days} days"
)

print("\nweekday      total")

for i, name in enumerate(weekdays):
    print(f"{name:<12} {totals[i]:.2f}")

print(f"\ntotal: {total:.2f}")
print(f"per day: {average:.2f} +- {deviation:.2f}")
print(
    f"top day: {top_day:%d.%m.%Y} "
    f"({top_day:%A}), {daily[top_day]:.2f}"
)
print(f"no-spend days: {no_spend}")
print(f"days in {last:%B}: {month_days}")
print(f"days left: {days_left}")
print(f"month forecast: {forecast:.2f}")

# Перевірка дат
for check in [date(2026, 12, 15), date(2028, 2, 10)]:
    start = date(check.year, check.month, 1)

    if check.month == 12:
        end = date(check.year + 1, 1, 1)
    else:
        end = date(check.year, check.month + 1, 1)

    print(f"{check}: {(end - start).days} days")
