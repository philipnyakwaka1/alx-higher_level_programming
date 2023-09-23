#!/usr/bin/python3
"""module for add_attribute"""


def add_attribute(obj, attribute_name, attribute_value):
    """adds a new attribute to an object if it’s possible:"""
    if hasattr(obj, '__dict__') is True:
        setattr(obj, attribute_name, attribute_value)
    else:
        raise TypeError("can't add new attribute")
