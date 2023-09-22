#!/usr/bin/python3
"""This is module for class Square"""


class Square(object):
    """Defines class Square"""

    def __init__(self, size=0):
        """initializes square"""
        self.size = size

    @property
    def size(self):
        """returns self"""

        return self.__size

    @size.setter
    def size(self, value):
        """sets size"""

        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """returns area"""
        return self.__size ** 2

    def __eq__(self, other):
        """equal comparison"""

        return self.area() == other.area()

    def __ne__(self, other):
        """not equal comparison"""

        return self.area() != other.area()

    def __lt__(self, other):
        """less than comparison"""

        return self.area() < other.area()

    def __le__(self, other):
        """less or equal to comparison"""

        return self.area() <= other.area()

    def __gt__(self, other):
        """greater than comparison"""

        return self.area() > other.area()

    def __ge__(self, other):
        """greater than or equal to comparison"""

        return self.area() >= other.area()
