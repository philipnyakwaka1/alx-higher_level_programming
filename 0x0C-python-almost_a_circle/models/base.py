#!/usr/bin/python3
"""Module for class Base()"""


class Base():
    """Defines class Base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor"""
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
