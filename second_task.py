import random

def get_numbers_ticket(min_num: int, max_num: int, quantity: int):
    if (not (1 <= min_num <= max_num <= 1000)
            or quantity >= max_num
            or quantity <= 0
            or (max_num - min_num + 1) < quantity):
        return []

    random_numbers = set()
    while len(random_numbers) < quantity:
        random_numbers.add(random.randint(min_num, max_num))
    return sorted(random_numbers)

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)
