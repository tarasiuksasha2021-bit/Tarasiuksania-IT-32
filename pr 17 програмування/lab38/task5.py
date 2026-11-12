
import requests
import json
import os
import sys
from datetime import datetime

print("Oleksandr Tarasiuk, IT-32")

URL = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange"
CACHE_FILE = "cache/rates.json"

try:
    rates = None

    # Перевірка кешу
    if os.path.exists(CACHE_FILE):
        try:
            with open(CACHE_FILE, "r", encoding="utf-8") as file:
                cache = json.load(file)

            saved_time = datetime.fromisoformat(cache["fetched_at"])
            age = (datetime.now() - saved_time).total_seconds()

            if 0 <= age < 3600:
                rates = cache["rates"]
                print(f"source: cache (age {int(age)} seconds)")

        except (json.JSONDecodeError, KeyError, ValueError, TypeError):
            rates = None

    # Якщо кеш відсутній або застарілий
    if rates is None:
        response = requests.get(
            URL,
            params={"json": ""},
            timeout=10
        )
        response.raise_for_status()

        rates = response.json()

        os.makedirs("cache", exist_ok=True)

        cache = {
            "fetched_at": datetime.now().isoformat(),
            "rates": rates
        }

        with open(CACHE_FILE, "w", encoding="utf-8") as file:
            json.dump(cache, file, ensure_ascii=False, indent=4)

        print("source: API (cache saved)")

    print("currencies:", len(rates))

    for currency in rates:
        if currency["cc"] in ("USD", "EUR"):
            print(
                f'{currency["cc"]}: {currency["rate"]} UAH '
                f'({currency["exchangedate"]})'
            )

except requests.RequestException as error:
    print(f"Network error: {error}", file=sys.stderr)
    sys.exit(1)