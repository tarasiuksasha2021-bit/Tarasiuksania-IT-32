from pathlib import Path
import sys

name = "Oleksandr"
surname = "Tarasiuk"
group = "IT-32"

script_dir = Path(__file__).resolve().parent
data_dir = script_dir / "data"
reports_dir = script_dir / "reports"

data_dir.mkdir(exist_ok=True)
reports_dir.mkdir(exist_ok=True)

expenses_path = data_dir / "expenses.csv"


def usage():
    print("usage: python task3.py add <date> <category> <amount> <note>")
    print("       python task3.py list")
    print("       python task3.py report")


def ensure_file():
    if not expenses_path.exists():
        expenses_path.write_text(
            "# date;category;amount;note\n",
            encoding="utf-8"
        )


def read_expenses():
    ensure_file()
    expenses = []

    with expenses_path.open("r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            if not line or line.startswith("#"):
                continue

            parts = line.split(";", 3)

            if len(parts) != 4:
                continue

            date, category, amount, note = parts

            try:
                amount = float(amount)
            except ValueError:
                continue

            expenses.append({
                "date": date,
                "category": category,
                "amount": amount,
                "note": note
            })

    return expenses


def add_expense(args):
    if len(args) < 4:
        print("error: add needs date, category, amount and note")
        usage()
        return

    date = args[0]
    category = args[1]

    try:
        amount = float(args[2])
    except ValueError:
        print("error: amount must be a number")
        return

    note = " ".join(args[3:])

    ensure_file()

    with expenses_path.open("a", encoding="utf-8") as file:
        file.write(f"{date};{category};{amount:.2f};{note}\n")

    print(f"added: {date} {category} {amount:.2f} ({note})")


def list_expenses():
    expenses = read_expenses()

    if not expenses:
        print("No expenses.")
        return

    print(f"{'date':<12} {'category':<15} {'amount':>8}  note")

    for expense in expenses:
        print(
            f"{expense['date']:<12} "
            f"{expense['category']:<15} "
            f"{expense['amount']:>8.2f}  "
            f"{expense['note']}"
        )

    total = sum(expense["amount"] for expense in expenses)

    print()
    print(f"{len(expenses)} records, total {total:.2f}")


def make_report():
    expenses = read_expenses()

    if not expenses:
        print("No expenses.")
        return

    total = sum(expense["amount"] for expense in expenses)

    categories = {}

    for expense in expenses:
        category = expense["category"]

        if category not in categories:
            categories[category] = {
                "count": 0,
                "total": 0
            }

        categories[category]["count"] += 1
        categories[category]["total"] += expense["amount"]

    days = {}

    for expense in expenses:
        date = expense["date"]
        days[date] = days.get(date, 0) + expense["amount"]

    top_day = max(days, key=days.get)
    most_expensive = max(expenses, key=lambda expense: expense["amount"])

    dates = sorted(expense["date"] for expense in expenses)
    first_date = dates[0]
    last_date = dates[-1]

    average_per_day = total / len(days)

    lines = []

    lines.append(f"Expenses report for {name} {surname} ({group})")
    lines.append(f"Period: {first_date} .. {last_date}")
    lines.append(f"Records: {len(expenses)}")
    lines.append("")
    lines.append(
        f"{'category':<12} {'count':>5} {'total':>10} "
        f"{'share':>8}  chart"
    )
    lines.append("-" * 52)

    sorted_categories = sorted(
        categories.items(),
        key=lambda item: item[1]["total"],
        reverse=True
    )

    for category, data in sorted_categories:
        share = data["total"] / total * 100
        chart = "#" * int(share / 5)

        lines.append(
            f"{category:<12} "
            f"{data['count']:>5} "
            f"{data['total']:>10.2f} "
            f"{share:>7.1f}%  "
            f"{chart}"
        )

    lines.append("-" * 52)
    lines.append(
        f"{'total':<12} "
        f"{len(expenses):>5} "
        f"{total:>10.2f} "
        f"{100:>7.1f}%"
    )
    lines.append("")
    lines.append(f"Top day: {top_day} ({days[top_day]:.2f})")
    lines.append(
        f"Most expensive: "
        f"{most_expensive['category']} "
        f"{most_expensive['amount']:.2f} "
        f"({most_expensive['note']})"
    )
    lines.append(f"Average per day: {average_per_day:.2f}")

    report_path = reports_dir / "expenses_report.txt"
    report_text = "\n".join(lines)

    report_path.write_text(report_text + "\n", encoding="utf-8")

    print(report_text)
    print()
    print(f"report saved to: {report_path}")


def main():
    if len(sys.argv) < 2:
        usage()
        return

    command = sys.argv[1]

    if command == "add":
        add_expense(sys.argv[2:])
    elif command == "list":
        list_expenses()
    elif command == "report":
        make_report()
    else:
        print(f"error: unknown command {command}")
        usage()


main()