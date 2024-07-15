import re

text_str = '''Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, 
        доповнений додатковими надходженнями 27.45 I 324.00 доларів.'''


def generator_numbers(text: str) -> float:
    text = text.strip()
    text = re.findall(r'(\d+\.\d+|\d+)', text_str)
    print(text)
    for number in text:
        number = float(number)
        yield number

def sum_profit(text: str, func: callable):
    sum_prof = 0
    for num_1 in func(text):
        sum_prof += num_1
    return sum_prof

profit = sum_profit(text_str, generator_numbers)

print(profit)
