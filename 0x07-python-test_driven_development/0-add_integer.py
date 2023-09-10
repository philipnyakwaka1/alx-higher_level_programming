#!/usr/bin/python3
"""This module an add function"""


def add_integer(a, b=98):
    """This function adds two integers
    Args:
        a: an int or float
        b: an int or float
    Raises:
        TypeError: if an argument is not an int or a float
    Return:
        int: sum of two integers
    """
    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer")
    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return a + b
