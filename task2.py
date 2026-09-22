grades_string = "92, 85, 95, 78, 88"

grades = [int(grade) for grade in grades_string.split(", ")]

print("Оцінки:", grades)

average = sum(grades) / len(grades)

print(f"Середня оцінка: {average:.2f}")
print("Найвища оцінка:", max(grades))
print("Найнижча оцінка:", min(grades))

print("Оцінки через |:", " | ".join(map(str, grades)))

subjects_string = "Programming, Mathematics, Databases, Web Development, English"
subjects = subjects_string.split(", ")

print()
print(f"{'№':<5}{'Предмет':<22}{'Оцінка':>8}")
print("-" * 35)

for number, (subject, grade) in enumerate(zip(subjects, grades), start=1):
    print(f"{number:<5}{subject:<22}{grade:>8}")

longest_subject = max(subjects, key=len)

print()
print("Найдовший предмет:", longest_subject)
print("Кількість символів:", len(longest_subject))