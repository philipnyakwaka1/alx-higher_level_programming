#!/usr/bin/python3
"""module for add_attribute"""


def add_attribute(obj, attr_name, attr_value):
    if hasattr(obj, '__dict__') is True:
        obj.__dict__[attr_name] = attr_value
    else:
        raise TypeError("can't add new attribute")
