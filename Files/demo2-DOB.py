from datetime import datetime, date, timedelta

dob = input("Enter your date of birth (DD-MM-YYYY): ")
try:
    birth_date = datetime.strptime(dob, "%d-%m-%Y")
    today = datetime.now()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    day_of_week = birth_date.strftime("%A")

    # Calculate next birthday
    next_birthday = birth_date.replace(year=today.year)
    if next_birthday < today:
        next_birthday = next_birthday.replace(year=today.year + 1)
    days_until_birthday = (next_birthday - today).days

    print(f"You are {age} years old. You were born on a {day_of_week}.")
    print(f"Days until your next birthday: {days_until_birthday}")
except ValueError:
    print("Invalid date format. Please use DD-MM-YYYY.")