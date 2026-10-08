from pathlib import Path

name = "Oleksandr"
surname = "Tarasiuk"
group = "IT-32"
year = 2009
language = "Python"

script_path = Path(__file__).resolve()
script_dir = script_path.parent
home = Path.home()
cwd = Path.cwd()

data_dir = script_dir / "data"
reports_dir = script_dir / "reports"
backups_dir = script_dir / "backups"

data_dir.mkdir(exist_ok=True)
reports_dir.mkdir(exist_ok=True)
backups_dir.mkdir(exist_ok=True)

profile_path = data_dir / "profile.txt"

profile_path.write_text(
    f"name: {name}\n"
    f"surname: {surname}\n"
    f"group: {group}\n"
    f"year: {year}\n"
    f"language: {language}\n",
    encoding="utf-8"
)

print(f"cwd:         {cwd}")
print(f"script:      {script_path}")
print(f"script dir:  {script_dir}")
print(f"home:        {home}")

print()
print(f"profile path: {profile_path}")
print(f"relative:     {profile_path.relative_to(script_dir)}")
print(f"name:         {profile_path.name}")
print(f"stem:         {profile_path.stem}")
print(f"suffix:       {profile_path.suffix}")
print(f"parent:       {profile_path.parent.name}")
print(f"size:         {profile_path.stat().st_size} bytes")

print()
print("project tree:")

for path in sorted(script_dir.rglob("*")):
    relative = path.relative_to(script_dir)
    level = len(relative.parts) - 1

    if path.is_dir():
        print("  " * level + path.name + "/")
    else:
        print("  " * level + path.name)