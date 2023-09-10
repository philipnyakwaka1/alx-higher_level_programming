#!/usr/bin/python3
"""THis is module for print_square"""


def print_square(size):
    """This functions prints a square using '#' character
    Args:
        size: size of the square
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
