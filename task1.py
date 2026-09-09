print("Oleksandr Tarasiuk, IT-32")

name = input("Enter your full name (text): ").strip()
age = int(input("Enter your age (integer): "))

if not name:
    print("Name was not entered")
    name = "Anonymous"

if age < 0:
    category = "invalid age"
elif age <= 6:
    category = "child"
elif age <= 17:
    category = "schoolchild"
elif age <= 64:
    category = "adult"
else:
    category = "senior"

print(f"Hello, {name}! Your age category is {category}.")