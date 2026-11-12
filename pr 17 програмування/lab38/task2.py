
import requests
import sys
import time
from http.server import BaseHTTPRequestHandler, HTTPServer
from threading import Thread

print("Oleksandr Tarasiuk, IT-32")

URL = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange"


def get_rate(currency_code, url=URL, timeout=10):
    response = requests.get(
        url,
        params={"valcode": currency_code, "json": ""},
        timeout=timeout
    )
    response.raise_for_status()

    data = response.json()

    if not data:
        raise ValueError("Currency not found")

    return data[0]["rate"], data[0]["exchangedate"]


# Розрахунок витрат
try:
    total = 0

    with open("data/expenses.csv", "r", encoding="utf-8") as file:
        for line in file:
            if not line.strip() or line.lstrip().startswith("#"):
                continue

            total += float(line.strip().split(";")[2])

    usd_rate, usd_date = get_rate("USD")
    eur_rate, eur_date = get_rate("EUR")

    print("rate date:", usd_date)
    print(
        f"total: {total:.2f} UAH = "
        f"{total / usd_rate:.2f} USD = "
        f"{total / eur_rate:.2f} EUR"
    )

except (requests.RequestException, ValueError, OSError) as error:
    print(f"Error: {error}", file=sys.stderr)
    sys.exit(1)


# Функція перевірки помилок
def test_error(name, url=URL, timeout=10):
    try:
        get_rate("USD", url=url, timeout=timeout)
        print(name, ": no error")

    except requests.Timeout:
        print(name, ": Timeout")

    except requests.ConnectionError:
        print(name, ": ConnectionError")

    except requests.HTTPError as error:
        print(name, ": HTTPError", error)

    except requests.RequestException as error:
        print(name, ": RequestException", error)


# 1. Помилка з'єднання
test_error("Internet error", url="http://127.0.0.1:1")

# 2. Помилка 404
test_error(
    "404 error",
    url="https://bank.gov.ua/this-page-does-not-exist"
)


# 3. Локальний сервер для перевірки Timeout
class SlowHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        time.sleep(0.2)

        try:
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"[]")
        except (BrokenPipeError, ConnectionAbortedError):
            pass

    def log_message(self, *args):
        pass


server = HTTPServer(("127.0.0.1", 0), SlowHandler)

thread = Thread(target=server.serve_forever, daemon=True)
thread.start()

test_error(
    "Timeout error",
    url=f"http://127.0.0.1:{server.server_port}",
    timeout=0.01
)

server.shutdown()
server.server_close()
