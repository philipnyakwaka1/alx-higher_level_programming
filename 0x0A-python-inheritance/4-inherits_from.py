#!/usr/bin/python3
"""module for inherits_from"""


def inherits_from(obj, a_class):
    """Returns True if obj is an inherits from a subclass of a_class"""

    if type(obj) is not a_class and issubclass(type(obj), a_class):
        return True
    else:
        return False
