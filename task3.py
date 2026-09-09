name = "Саша"
surname = "Тарасюк"
group = "ІТ-32"


def get_initials(name: str, surname: str) -> str:
    """Повертає ініціали імені та прізвища."""
    return f"{name[0]}.{surname[0]}."


def count_letters(text: str, letter: str = "a") -> int:
    """Рахує кількість входжень заданої літери без урахування регістру."""
    count = 0

    for char in text.lower():
        if char == letter.lower():
            count += 1

    return count


def count_vowels(text: str) -> int:
    """Рахує кількість голосних літер."""
    vowels = "aeiouy"
    count = 0

    for char in text.lower():
        if char in vowels:
            count += 1

    return count


def reverse_text(text: str) -> str:
    """Повертає текст у зворотному порядку без використання зрізів."""
    result = ""

    for char in text:
        result = char + result

    return result


def main():
    print(f"{name} {surname}, група {group}")

    print("\n1. Ініціали:")
    print(get_initials(name, surname))

    print("\n2. Довжина прізвища:")
    print(count_letters(surname, "а") +
          count_letters(surname, "б") +
          count_letters(surname, "в") +
          count_letters(surname, "г") +
          count_letters(surname, "д") +
          count_letters(surname, "е") +
          count_letters(surname, "ж") +
          count_letters(surname, "з") +
          count_letters(surname, "и") +
          count_letters(surname, "і") +
          count_letters(surname, "ї") +
          count_letters(surname, "й") +
          count_letters(surname, "к") +
          count_letters(surname, "л") +
          count_letters(surname, "м") +
          count_letters(surname, "н") +
          count_letters(surname, "о") +
          count_letters(surname, "п") +
          count_letters(surname, "р") +
          count_letters(surname, "с") +
          count_letters(surname, "т") +
          count_letters(surname, "у") +
          count_letters(surname, "ф") +
          count_letters(surname, "х") +
          count_letters(surname, "ц") +
          count_letters(surname, "ч") +
          count_letters(surname, "ш") +
          count_letters(surname, "щ") +
          count_letters(surname, "ь") +
          count_letters(surname, "ю") +
          count_letters(surname, "я"))

    vowels = count_vowels(surname)
    length = len(surname)

    print(f"Голосних: {vowels}")
    print(f"Приголосних: {length - vowels}")

    print("\n3. Кількість кожної голосної:")
    for letter in "aeiou":
        print(f"{letter}: {count_letters(surname, letter=letter)}")

    print("\n4. Значення літери за замовчуванням:")
    print(f"Літера 'a': {count_letters(surname)}")

    print("\n5. Прізвище навпаки:")
    print(reverse_text(surname))


if __name__ == "__main__":
    main()