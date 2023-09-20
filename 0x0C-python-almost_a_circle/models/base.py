#!/usr/bin/python3
"""This is a module for the Base clase"""

import json


class Base():
    """This is the base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """The __init__ method initializes the class
        Args:
            id: id attribute of the class
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """converts a list of dictionaries"""

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)
