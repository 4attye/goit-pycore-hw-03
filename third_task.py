import re

raw_numbers = [
    "067\t123 4567",
    "(095) 234-5678\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ", ]


def normalize_phone(phone_number):
    # Видаляємо всі символи, крім цифр та символу '+'
    cleaned_number = re.sub(r'[^\d+]', '', phone_number)

    # Перевіряємо, чи номер починається з '+'
    if cleaned_number.startswith('+'):
        # Якщо номер починається з '+', то не змінюємо його
        normalized_number = cleaned_number
        # Якщо номер починається з '38', то додаємо тільки '+'
    elif cleaned_number.startswith('38'):
        normalized_number = '+' + cleaned_number
    else:
        # В інших випадках додаємо '+38'
        normalized_number = '+38' + cleaned_number

    return normalized_number


num = []
for nume in raw_numbers:
    num.append(normalize_phone(nume))

print("Нормалізовані номери телефонів для SMS-розсилки:", num)
