name = "Sasha"
surname = "Tarasiuk"
group = "IT-32"

print(f"{name} {surname}, {group}")

number = int(input("Enter an integer: "))

if number < 0:
    print("Please enter a non-negative integer.")
elif number == 0:
    print("Digits: 1")
    print("Sum of digits: 0")
    print("Max digit: 0, min digit: 0")
    print("Reversed: 0")
else:
    temp = number

    count = 0
    digit_sum = 0
    max_digit = 0
    min_digit = 9
    reversed_number = 0

    while temp > 0:
        digit = temp % 10

        count += 1
        digit_sum += digit

        if digit > max_digit:
            max_digit = digit

        if digit < min_digit:
            min_digit = digit

        reversed_number = reversed_number * 10 + digit

        temp //= 10

    print(f"Digits: {count}")
    print(f"Sum of digits: {digit_sum}")
    print(f"Max digit: {max_digit}, min digit: {min_digit}")
    print(f"Reversed: {reversed_number}")