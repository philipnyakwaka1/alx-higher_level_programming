#!/usr/bin/python3
"""module for is_kind_of_class"""


def is_kind_of_class(obj, a_class):
    """Returns True if obj is an instance of a_class"""

    if isinstance(obj, a_class):
        return True
    else:
        return False
