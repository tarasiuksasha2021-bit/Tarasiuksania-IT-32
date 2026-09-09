print("Oleksandr Tarasiuk, IT-32")

score = int(input("Enter your expected score (integer 0-100): "))
missed = int(input("Enter missed classes (integer): "))

if score < 0 or score > 100:
    print("Error: score must be between 0 and 100")
else:
    if score >= 90:
        grade = "A"
    elif score >= 82:
        grade = "B"
    elif score >= 74:
        grade = "C"
    elif score >= 64:
        grade = "D"
    elif score >= 60:
        grade = "E"
    else:
        grade = "F"

    if missed > 16 * 0.30:
        print("Warning: not admitted because more than 30% of classes were missed")

    if grade == "F" or missed > 16 * 0.30:
        result = "failed"
    else:
        result = "passed"

    print(f"Score: {score}, Grade: {grade}, Result: {result}")