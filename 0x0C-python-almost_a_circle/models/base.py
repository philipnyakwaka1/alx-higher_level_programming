#!usr/bin/python3
"""This is a module for the Base clase"""


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
