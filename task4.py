name = "Саша"
surname = "Тарасюк"
group = "ІТ-32"


def read_grade(prompt):
    """Зчитує оцінку від 0 до 100."""
    while True:
        try:
            grade = int(input(prompt))

            if 0 <= grade <= 100:
                return grade

            print("Помилка: оцінка повинна бути від 0 до 100.")

        except ValueError:
            print("Помилка: введіть ціле число.")


def to_letter(grade):
    """Перетворює оцінку у літерну шкалу."""
    if grade >= 90:
        return "A"

    if grade >= 82:
        return "B"

    if grade >= 74:
        return "C"

    if grade >= 64:
        return "D"

    if grade >= 60:
        return "E"

    return "F"


def average(grades):
    """Обчислює середню оцінку."""
    return sum(grades) / len(grades)


def count_above(grades, limit):
    """Рахує кількість оцінок, які більші за задане значення."""
    count = 0

    for grade in grades:
        if grade > limit:
            count += 1

    return count


def print_report(name, group, grades):
    """Виводить підсумковий звіт про оцінки."""
    avg = average(grades)

    print("\n===== ЗВІТ =====")
    print(f"Студент: {name}")
    print(f"Група: {group}")
    print(f"Оцінки: {grades}")
    print(f"Середня оцінка: {avg:.2f}")
    print(f"Літера: {to_letter(avg)}")
    print(f"Найкраща оцінка: {max(grades)}")
    print(f"Найгірша оцінка: {min(grades)}")
    print(f"Оцінок вище середнього: {count_above(grades, avg)}")


def main():
    print(f"{name} {surname}, група {group}")

    grades = []

    # 5 оцінок, оскільки у імені "Саша" 5 літер
    for i in range(5):
        grade = read_grade(f"Введіть оцінку {i + 1}: ")
        grades.append(grade)

    print_report(name, group, grades)


if __name__ == "__main__":
    main()