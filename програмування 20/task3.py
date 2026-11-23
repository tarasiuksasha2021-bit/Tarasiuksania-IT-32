
class Expense:
    def __init__(self, date, category, amount):
        self.date = date
        self.category = category
        self.amount = amount

    def monthly_cost(self):
        return self.amount


class RecurringExpense(Expense):
    def __init__(self, date, category, amount, times_per_month):
        super().__init__(date, category, amount)
        self.times_per_month = times_per_month

    def monthly_cost(self):
        return self.amount * self.times_per_month


class SharedExpense(Expense):
    def __init__(self, date, category, amount, people):
        super().__init__(date, category, amount)
        self.people = people

    def monthly_cost(self):
        return self.amount / self.people


expenses = [
    RecurringExpense("01.11.2026", "Transport", 20, 20),
    RecurringExpense("01.11.2026", "Mobile", 150, 1),
    SharedExpense("01.11.2026", "Rent", 6000, 3),
    SharedExpense("01.11.2026", "Internet", 300, 2)
]

total = 0

for expense in expenses:
    cost = expense.monthly_cost()
    print(f"{expense.category}: {cost:.2f} грн")
    total += cost

print(f"Total monthly cost: {total:.2f} грн")
