#!/usr/bin/python3
"""Check for lowercase"""


def islower(c):
    """Check for lowercase"""
    if type(c) == str:
        n = ord(c)
        if n >= 97 and n <= 122:
            return True
        return False
    return False
