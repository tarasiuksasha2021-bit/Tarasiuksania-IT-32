birth_day = 7
birth_month = 2

day_positive = birth_day > 0
day_even = birth_day % 2 == 0
day_positive_and_even = day_positive and day_even

print(f"Birth day: {birth_day}")
print(f"Positive: {day_positive}")
print(f"Even: {day_even}")
print(f"Positive and even: {day_positive_and_even}")

birth_product = birth_day * birth_month

product_positive = birth_product > 0
product_even = birth_product % 2 == 0
product_positive_and_even = product_positive and product_even

print(f"\nBirth day * birth month: {birth_product}")
print(f"Positive: {product_positive}")
print(f"Even: {product_even}")
print(f"Positive and even: {product_positive_and_even}")