print("Oleksandr Tarasiuk, IT-32")

day = int(input("Enter your birth day (integer): "))
month = int(input("Enter your birth month (integer): "))
year = int(input("Enter your birth year (integer): "))

if year <= 0:
    print("Date is invalid: year must be positive")
elif month < 1 or month > 12:
    print("Date is invalid: month must be between 1 and 12")
else:
    if month in (1, 3, 5, 7, 8, 10, 12):
        days_in_month = 31
    elif month in (4, 6, 9, 11):
        days_in_month = 30
    else:
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            days_in_month = 29
        else:
            days_in_month = 28

    if day < 1 or day > days_in_month:
        print(f"Date is invalid: month {month} has only {days_in_month} days")
    else:
        print(f"Date is valid: {day:02d}.{month:02d}.{year}")