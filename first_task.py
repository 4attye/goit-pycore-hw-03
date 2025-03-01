from datetime import datetime


def get_days_from_today(given_date):
    try:
        # Перетворення рядка дати у форматі 'YYYY-MM-DD'
        given_date = datetime.strptime(given_date, '%Y-%m-%d')
        # Отримання поточної дати
        current_date = datetime.today()
        # Розрахунок і повернення різниці між поточною датою та заданою датою
        return current_date.toordinal() - given_date.toordinal()
    except ValueError:
        # В разі помилки виводить "Incorrect data entered"
        print("Incorrect data entered")


print(get_days_from_today("2021-10-09"))
