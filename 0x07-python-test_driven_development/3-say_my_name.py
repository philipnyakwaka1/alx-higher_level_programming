#!/usr/bin/python3
"""This modules defines say_my_name"""


def say_my_name(first_name, last_name=""):
    """This function prints the first name and last name
    Args:
        first_name: a person's first name
        last_name: a users last name
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f'My name is {first_name} {last_name}')
