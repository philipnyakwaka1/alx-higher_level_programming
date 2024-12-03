#!/usr/bin/python3
"""Show whether the randonmly assigned number is +ve or -ve"""

import random
number = random.randint(-10, 10)
if number > 0:
    print(f'{number} is positive')
elif number < 0:
    print(f'{number} is negative')
else:
    print(f'{number} is zero')
