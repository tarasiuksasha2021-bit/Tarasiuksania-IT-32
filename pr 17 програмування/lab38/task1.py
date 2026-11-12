
import requests
import sys

print("Oleksandr Tarasiuk, IT-32")

URL = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange"

try:
    response = requests.get(URL, params={"json": ""}, timeout=10)
    response.raise_for_status()

    rates = response.json()

    print("status:", response.status_code)
    print("Content-Type:", response.headers.get("Content-Type"))
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