#!/usr/bin/python3
"""module for class BaseGeometry"""


class BaseGeometry():
    """Defines BaseGeometry"""

    def area(self):
        """returns area"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates integer"""

        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
