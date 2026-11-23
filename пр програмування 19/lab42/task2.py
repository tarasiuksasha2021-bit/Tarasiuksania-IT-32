
class Wallet:
    def __init__(self, owner, balance):
        if not owner.strip():
            raise ValueError("Ім'я не може бути порожнім")
        if balance < 0:
            raise ValueError("Баланс не може бути від'ємним")

        self.owner = owner
        self.__balance = round(balance, 2)

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Сума поповнення має бути більшою за 0")
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Сума зняття має бути більшою за 0")
        if amount > self.__balance:
            raise ValueError("Недостатньо коштів")
        self.__balance -= amount


wallet = Wallet("Олександр Тарасюк", 5000)

wallet.deposit(500)
wallet.withdraw(300)

print("Власник:", wallet.owner)

try:
    print(wallet.__balance)
except AttributeError as error:
    print("Помилка:", error)

print("Баланс через name mangling:", wallet._Wallet__balance)

try:
    wallet.withdraw(10000)
except ValueError as error:
    print("Помилка:", error)
