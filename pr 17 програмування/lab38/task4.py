
import requests

print("Oleksandr Tarasiuk, IT-32")

def check_error(name, url, timeout=10):
    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
        print(name, ": no error")

    except requests.Timeout:
        print(name, ": Timeout")

    except requests.ConnectionError:
        print(name, ": ConnectionError")

    except requests.HTTPError:
        print(name, ": HTTPError 404")

check_error("Internet error", "http://127.0.0.1:1")

check_error(
    "404 error",
    "https://bank.gov.ua/this-page-does-not-exist"
)

check_error(
    "Timeout error",
    "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange",
    timeout=0.0000001
)