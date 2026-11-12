import pytest

from expenses import parse_line, load_expenses, total_by_category


# Завдання 2. Перші тести з assert

def test_parse_line_valid():
    record = parse_line("2026-10-02;food;85.50;lunch")
    assert record["category"] == "food"
    assert record["amount"] == 85.5


def test_parse_line_date():
    record = parse_line("2026-10-03;food;120.00;groceries")
    assert record["date"] == "2026-10-03"


def test_parse_line_comment():
    record = parse_line("2026-10-04;transport;32.00;bus")
    assert record["comment"] == "bus"


# Завдання 3. Перевірка винятків

def test_parse_line_bad_amount():
    with pytest.raises(ValueError):
        parse_line("2026-10-02;food;abc;lunch")


def test_parse_line_wrong_fields():
    with pytest.raises(ValueError):
        parse_line("2026-10-02;food;85.50")


# Завдання 4. Параметризований тест

@pytest.mark.parametrize(
    "line, expected_category, expected_amount",
    [
        ("2026-10-02;food;85.50;lunch", "food", 85.50),
        ("2026-10-02;transport;32.00;bus", "transport", 32.00),
        ("2026-10-03;food;120.00;groceries", "food", 120.00),
        ("2026-10-03;coffee;65.00;coffee", "coffee", 65.00),
        ("2026-10-04;transport;32.00;bus", "transport", 32.00),
    ]
)
def test_parse_line_parametrize(line, expected_category, expected_amount):
    record = parse_line(line)
    assert record["category"] == expected_category
    assert record["amount"] == expected_amount


# Завдання 5. Тимчасовий файл

def test_total_by_category_tmp_path(tmp_path):
    path = tmp_path / "expenses.csv"

    path.write_text(
        "# date;category;amount;comment\n"
        "2026-09-21;food;85.50;lunch\n"
        "\n"
        "2026-09-22;food;14.50;coffee\n",
        encoding="utf-8"
    )

    totals = total_by_category(load_expenses(path))

    assert totals == {"food": 100.0}


# Перевірка справжнього файлу з роботи №22

def test_total_by_category_real_file():
    records = load_expenses("data/expenses.csv")
    totals = total_by_category(records)

    assert totals == {
        "food": 507.0,
        "transport": 96.0,
        "coffee": 130.0,
        "internet": 250.0,
        "books": 220.0
    }