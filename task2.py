name = "Саша"
surname = "Тарасюк"
group = "ІТ-32"
year = 2009


def print_age(year):
    """Виводить вік людини, але нічого не повертає."""
    age = 2026 - year
    print(f"Вік: {age}")


def get_age(year, current_year=2026):
    """Повертає вік людини."""
    if year > current_year or year < 0:
        return -1

    return current_year - year


def main():
    print(f"{name} {surname}, група {group}")

    print("\n1. print_age():")
    print_age(year)

    print("\n2. Результат print(print_age()):")
    result = print_age(year)
    print(result)

    print("\n3. Вік у місяцях і тижнях:")
    age = get_age(year)

    print(f"Вік у роках: {age}")
    print(f"Вік у місяцях: {age * 12}")
    print(f"Вік у тижнях: {age * 52}")

    print("\n4. Вік у 2030 році:")
    age_2030 = get_age(year, current_year=2030)
    print(f"Вік у 2030 році: {age_2030}")

    print("\n5. Спроба помножити результат print_age():")
    try:
        print_age(year) * 12
    except TypeError as error:
        print(type(error).__name__ + ":", error)

    print("\n6. Перевірка неправильного року:")
    wrong_age = get_age(3000)
    print(f"Результат для 3000 року: {wrong_age}")

    print("\n7. Код після return:")
    print("Код після return не виконується.")


if __name__ == "__main__":
    main()