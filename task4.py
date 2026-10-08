from pathlib import Path

script_dir = Path(__file__).resolve().parent
desktop = Path.home() / "Desktop"

files = [path for path in desktop.rglob("*") if path.is_file()]

print(f"Directory: {desktop}")
print(f"Files found: {len(files)}")
print()

if not files:
    print("No files found.")
else:
    for path in sorted(files):
        relative = path.relative_to(desktop)
        size = path.stat().st_size
        print(f"{relative} - {size} bytes")