from datetime import datetime

def get_days_from_today(given_date):

    try:
        given_date = datetime.strptime(given_date, '%Y-%m-%d')
        current_date = datetime.today()
        return current_date.toordinal() - given_date.toordinal()
    except ValueError:
        print("Incorrect data entered")

print(get_days_from_today("2021-10-09"))
