name = "Саша"
surname = "Тарасюк"
group = "ІТ-32"
year = 2009


def print_card():
    """Виводить інформаційну картку студента."""
    print(f"Ім'я: {name}")
    print(f"Прізвище: {surname}")
    print(f"Група: {group}")
    print(f"Рік народження: {year}")


def print_card_args(name, surname, group=group, year=year):
    """Виводить картку студента з використанням параметрів."""
    print(f"Ім'я: {name}")
    print(f"Прізвище: {surname}")
    print(f"Група: {group}")
    print(f"Рік народження: {year}")


def main():
    print(f"{name} {surname}, група {group}")
    print("\n1. Функція без параметрів:")

    print_card()
    print_card()
    print_card()

    print("\n2. Параметри функції:")

    # Позиційні аргументи
    print_card_args(name, surname, group, year)

    # Іменовані аргументи у довільному порядку
    print_card_args(year=year, group=group, surname=surname, name=name)

    # Змішані аргументи
    print_card_args(name, surname, group=group, year=year)

    print("\n3. Значення group за замовчуванням:")
    print_card_args(name, surname, year=year)

    print("\n4. Приклад помилки при недостатній кількості аргументів:")
    try:
        print_card_args("Ivan")
    except TypeError as error:
        print(type(error).__name__ + ":", error)


if __name__ == "__main__":
    main()