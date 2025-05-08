from datetime import datetime
import random
import re


# task 1
def get_days_from_today(date: str) -> int:
    try:
        date_time = datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        print('Invalid date')
        raise

    today = datetime.today()
    return (today - date_time).days


# task 2
def get_numbers_ticket(min_num: int, max_num: int, quantity: int) -> list[int]:
    if min_num < 1 or max_num > 1000:
        raise ValueError('Invalid min/max number')

    numbers = set()

    for i in range(quantity):
        numbers.add(random.randint(min_num, max_num))

    return sorted(numbers)


# task 3
def normalize_phone(num: str) -> str:
    pattern = r'[0-9]+'
    number = ''.join(re.findall(pattern, num))

    if not number.startswith('38'):
        number = '38' + number

    if not number.startswith('+'):
        number = '+' + number

    return number
