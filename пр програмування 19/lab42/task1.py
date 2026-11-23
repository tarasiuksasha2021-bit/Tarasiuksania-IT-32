
class Wallet:
    def __init__(self, owner, balance):
        if not owner.strip():
            raise ValueError("Ім'я власника не може бути порожнім")

        if balance < 0:
            raise ValueError("Початковий баланс не може бути від'ємним")

        self.owner = owner
        self.balance = round(balance, 2)


wallet = Wallet("Олександр Тарасюк", 5000)
print("Власник:", wallet.owner)
print("Баланс:", wallet.balance, "грн")

try:
    wallet1 = Wallet("", 1000)
except ValueError as error:
    print("Помилка:", error)

try:
    wallet2 = Wallet("Олександр Тарасюк", -500)
except ValueError as error:
    print("Помилка:", error)
