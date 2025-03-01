from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:

        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        delta_days = (birthday_this_year - today).days

        if 0 <= delta_days <= 7:

            congratulation_date = birthday_this_year

            if congratulation_date.weekday() in [5, 6]:
                congratulation_date += timedelta(days=(7 - congratulation_date.weekday()))

            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d"),
            })

    return upcoming_birthdays

users = [
    {"name": "John Doe", "birthday": "1985.03.01"},
    {"name": "Jane Smith", "birthday": "1990.03.05"}
]

print(get_upcoming_birthdays(users))