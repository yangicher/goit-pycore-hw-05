import re
from typing import Callable

def generator_numbers(text: str):
    numbers = re.findall(r"\d+\.\d+|\d+", text)

    for n in numbers:
        yield float(n)

def sum_profit(text: str, func: Callable):
    sum = 0.0
    for n in func(text):
        sum += n
    return sum

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")