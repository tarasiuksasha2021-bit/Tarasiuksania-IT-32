
import json
import sys
import os

print("Oleksandr Tarasiuk, IT-32")

settings_file = "settings.json"

default_settings = {
    "owner": "Oleksandr Tarasiuk",
    "group": "IT-32",
    "currency": "UAH",
    "monthly_limit": 6000,
    "categories": ["food", "transport", "coffee", "books", "internet"]
}

if not os.path.exists(settings_file):
    with open(settings_file, "w", encoding="utf-8") as file:
        json.dump(default_settings, file, indent=2, ensure_ascii=False)

    print("settings.json not found, default created")

else:
    try:
        with open(settings_file, "r", encoding="utf-8") as file:
            settings = json.load(file)

        print("owner:", settings["owner"])
        print("group:", settings["group"])
        print("currency:", settings["currency"])
        print("categories:", settings["categories"])

        total = 1203.00
        limit = settings["monthly_limit"]
        left = limit - total

        print(
            f"limit: {limit:.2f} UAH, "
            f"spent: {total:.2f} UAH, "
            f"left: {left:.2f} UAH"
        )

    except json.JSONDecodeError as error:
        print(
            f"JSON error at line {error.lineno}",
            file=sys.stderr
        )
        sys.exit(1)