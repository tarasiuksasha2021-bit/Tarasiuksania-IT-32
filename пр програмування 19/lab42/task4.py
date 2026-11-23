
import csv


class Wallet:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __init__(self, owner, balance):
        if balance < 0:
            raise ValueError("Баланс не може бути від'ємним")
        self.owner = owner
        self.balance = round(balance, 2)

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Недостатньо коштів")
        self.balance = round(self.balance - amount, 2)


wallet = Wallet("Олександр Тарасюк", 5000)

print("Власник:", wallet.owner)
print("Початковий баланс:", wallet.balance, "грн")

total = 0

with open("data/expenses.csv", encoding="utf-8-sig", newline="") as file:
    reader = csv.DictReader(file)

    for expense in reader:
        amount = float(expense["amount"])

        try:
            wallet.withdraw(amount)
            total += amount
            print("Витрата:", expense, "| Залишок:", wallet.balance, "грн")
        except ValueError:
            print("Недостатньо коштів для витрати:", expense)
            break

print("Усього списано:", round(total, 2), "грн")
print("Кінцевий баланс:", wallet.balance, "грн")
