
import math
import random
import csv
from pathlib import Path
from datetime import datetime

print("Oleksandr Tarasiuk, ІТ-32")

YEAR = 2009

random.seed(YEAR)

questions = []

# Корінь
number = random.randint(5, 20)
square = number ** 2
questions.append((f"sqrt({square})", math.isqrt(square)))

# Факторіал
number = random.randint(3, 6)
questions.append((f"{number}!", math.factorial(number)))

# НСД
a = random.randint(24, 90)
b = random.randint(12, 60)
questions.append((f"gcd({a}, {b})", math.gcd(a, b)))

# Комбінації
n = random.randint(6, 10)
k = random.randint(2, n - 2)
questions.append((f"comb({n}, {k})", math.comb(n, k)))

# Відсотки
percent = random.choice([5, 10, 15, 20])
amount = random.randint(10, 50) * 20
questions.append(
    (f"{percent}% of {amount}", percent * amount // 100)
)

start = datetime.now()
score = 0

for i, (question, correct) in enumerate(questions, 1):
    answer = input(f"{i}) {question} = ")

    try:
        if answer.strip() != "" and int(answer) == correct:
            print("   correct")
            score += 1
        else:
            print(f"   wrong, answer: {correct}")
    except ValueError:
        print(f"   wrong, answer: {correct}")

end = datetime.now()
seconds = (end - start).total_seconds()

history = Path(__file__).parent / "results" / "history.csv"
history.parent.mkdir(exist_ok=True)

new_file = not history.exists()

with history.open("a", newline="", encoding="utf-8") as file:
    if new_file:
        file.write("# datetime;score;seconds\n")

    writer = csv.writer(file, delimiter=";")
    writer.writerow([
        end.strftime("%Y-%m-%d %H:%M:%S"),
        score,
        f"{seconds:.1f}"
    ])

attempts = []

with history.open(encoding="utf-8") as file:
    for row in csv.reader(file, delimiter=";"):
        if not row or row[0].startswith("#"):
            continue

        try:
            attempts.append((
                datetime.strptime(row[0], "%Y-%m-%d %H:%M:%S"),
                int(row[1]),
                float(row[2])
            ))
        except (ValueError, IndexError):
            continue

best = min(attempts, key=lambda x: (-x[1], x[2]))

print(f"score: {score}/5, time: {seconds:.1f} s")
print(
    f"attempts: {len(attempts)}, best: "
    f"{best[1]}/5 in {best[2]:.1f} s "
    f"({best[0]:%Y-%m-%d %H:%M})"
)
