
import math
import sys
import shutil
from pathlib import Path
from datetime import datetime

print("Oleksandr Tarasiuk, ІТ-32")

def size_format(size):
    units = ["B", "KB", "MB", "GB"]

    if size == 0:
        return "0 B"

    index = min(int(math.log(size, 1024)), 3)
    value = size / (1024 ** index)

    return f"{value:.1f} {units[index]}"


args = sys.argv[1:]
dry_run = False

if "--dry-run" in args:
    dry_run = True
    args.remove("--dry-run")

if len(args) != 1:
    print("usage: python task3.py [--dry-run] <dir>")
    sys.exit(2)

directory = Path(args[0]).expanduser()

if not directory.exists() or not directory.is_dir():
    print("error: це не каталог", file=sys.stderr)
    sys.exit(1)

files = [p for p in directory.iterdir() if p.is_file()]

if not files:
    print("У каталозі немає файлів")
    sys.exit(0)

records = []

for file in files:
    stat = file.stat()
    modified = datetime.fromtimestamp(stat.st_mtime)
    folder = modified.strftime("%Y-%m")
    destination = directory / folder / file.name

    records.append(
        (file, stat.st_size, modified, destination)
    )

records.sort(key=lambda x: x[2])

# Перевірка конфліктів до переміщення
for file, size, modified, destination in records:
    if destination.exists():
        print(
            f"error: {destination} already exists, nothing was moved",
            file=sys.stderr
        )
        sys.exit(1)

folders = set()

for file, size, modified, destination in records:
    folders.add(destination.parent)

    print(
        f"{file.name:<22} {size_format(size):>9} "
        f"{modified:%d.%m.%Y %H:%M} "
        f" -> {destination.parent.name}/"
    )

if dry_run:
    print(
        f"{len(records)} files, {len(folders)} folders "
        "(dry run, nothing moved)"
    )
    sys.exit(0)

for file, size, modified, destination in records:
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.move(str(file), str(destination))

report_dir = Path(__file__).parent / "reports"
report_dir.mkdir(exist_ok=True)

now = datetime.now()
report = report_dir / f"organize_{now:%Y%m%d_%H%M}.txt"

with report.open("w", encoding="utf-8") as output:
    output.write("Oleksandr Tarasiuk, ІТ-32\n")

    for file, size, modified, destination in records:
        output.write(
            f"{file.name}; {size_format(size)}; "
            f"{modified}; {destination}\n"
        )

print(f"{len(records)} files, {len(folders)} folders")
print(f"report saved to: {report}")
