#!/usr/bin/python3
"""module for class_to_json"""


def class_to_json(obj):
    """
    returns the dictionary description with simple
    data structure (list, dictionary, string, integer
    and boolean) for JSON serialization of an object

    Args:
        obj: instance of the class
    """

    my_dict = {}
    for key, value in obj.__dict__.items():
        if type(value) in (list, dict, str, int, bool):
            my_dict[key] = value
    return my_dict
