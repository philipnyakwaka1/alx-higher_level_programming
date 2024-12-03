#!/usr/bin/python3
def print_last_digit(number):
    temp = number
    if temp < 0:
        temp *= -1
    last_digit = temp % 10
    print("{}".format(last_digit), end="")
    return last_digit
