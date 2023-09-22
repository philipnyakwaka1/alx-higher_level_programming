#!/usr/bin/python3
"""module for is_same_class"""


def is_same_class(obj, a_class):
    """Returns True if obj is an instance of a_class"""

    if type(obj) is a_class:
        return True
    else:
        return False
