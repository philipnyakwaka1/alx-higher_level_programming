#!/usr/bin/env python3
"""Print alphabet"""

for c in range(97, 123):
    char = chr(c)
    if char != 'q' and char != 'e':
        print(char, end=" ")
