name = input("Enter your name: ")
age = int(input("Enter your age: "))

age_in_range = 18 <= age <= 60
age_even = age % 2 == 0
both_conditions = age_in_range and age_even
at_least_one = age_in_range or age_even
years_until_60 = 60 - age

print(f"\nName: {name}")
print(f"Age: {age}")
print(f"Age is from 18 to 60: {age_in_range}")
print(f"Age is even: {age_even}")
print(f"Age is from 18 to 60 and even: {both_conditions}")
print(f"At least one condition is true: {at_least_one}")
print(f"Years until 60: {years_until_60}")