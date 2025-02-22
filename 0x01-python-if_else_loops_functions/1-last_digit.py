#!/usr/bin/python3
"""Check for last digit"""

import random
number = random.randint(-10000, 10000)
if number < 0:
    last_digit = abs(number) % 10
    last_digit *= -1
else:
    last_digit = number % 10
string = f'Last digit of {number} is {last_digit}'
if last_digit == 0:
    print(f'{string} and is 0')
elif last_digit > 5:
    print(f'{string} and is greater than 5')
elif last_digit < 6 and last_digit != 0:
    print(f'{string} and is less than 6 and not 0')
