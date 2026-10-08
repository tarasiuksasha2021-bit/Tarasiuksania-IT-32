from pathlib import Path
from datetime import datetime

name = "Oleksandr"
surname = "Tarasiuk"

script_dir = Path(__file__).resolve().parent
data_dir = script_dir / "data"
data_dir.mkdir(exist_ok=True)

runs_path = data_dir / "runs.log"


def count_runs(path):
    if not path.exists():
        return 0

    with path.open("r", encoding="utf-8") as file:
        return sum(1 for line in file if line.strip())


def add_run(path, number):
    stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with path.open("a", encoding="utf-8") as file:
        file.write(f"{number};{stamp};{name} {surname}\n")


def show_history(path, last=3):
    with path.open("r", encoding="utf-8") as file:
        records = [line.strip() for line in file if line.strip()]

    print(f"runs so far: {len(records)}")
    print("last runs:")

    for record in records[-last:]:
        number, stamp, fullname = record.split(";", 2)
        print(f"  # {number}  {stamp}  {fullname}")

    if records:
        first = records[0].split(";", 2)
        print(f"first run was at {first[1]}")


def main():
    previous_runs = count_runs(runs_path)
    current_run = previous_runs + 1

    add_run(runs_path, current_run)

    print(f"Hello, {name} {surname}! This is run number {current_run}.")

    if current_run == 1:
        print("runs.log was just created.")

    show_history(runs_path)


main()