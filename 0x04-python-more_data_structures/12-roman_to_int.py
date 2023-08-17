#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None:
        return 0
    a = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = 0
    val = 0
    for i in roman_string:
        if a[i] <= val:
            num += a[i]
        else:
            num += a[i] - 2 * val
        val = a[i]
    return num
