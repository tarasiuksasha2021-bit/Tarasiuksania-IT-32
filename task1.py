full_name = "  oLEKSANDR   tARASIUK   oLEKSANDROVYCH  "

words = full_name.split()
full_name = " ".join(words).title()

print("Охайне ім'я:", full_name)
print("Довжина:", len(full_name))

name, surname, patronymic = full_name.split()

print("Перший символ прізвища:", surname[0])
print("Останній символ прізвища:", surname[-1])
print("Прізвище навпаки:", surname[::-1])

print("Формат:", f"{surname} {name[0]}. {patronymic[0]}.")
print("Ініціали:", f"{surname[0]}{name[0]}{patronymic[0]}")

vowels = "aeiou"
vowels_count = sum(1 for char in full_name.lower() if char in vowels)
print("Кількість голосних:", vowels_count)

group = "IT-32"
dash_position = group.find("-")

before_dash = group[:dash_position]
after_dash = group[dash_position + 1:]

print("До дефіса:", before_dash)
print("Після дефіса:", after_dash)
print("Після дефіса є числом:", after_dash.isdigit())

login = f"{name[0].lower()}.{surname.lower()}"
email = f"{login}@student.edu.ua"

print("Логін:", login)
print("Пошта:", email)