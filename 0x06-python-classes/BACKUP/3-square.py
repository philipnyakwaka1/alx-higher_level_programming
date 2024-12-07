#!/usr/bin/python3
"""This module defines an class Square"""


class Square:
    """This is a class square"""

    def __init__(self, size=0):
        """__init__ method initializes the size of the new square

        Args:
            size: size of the square, which is initialized at 0

        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Calculates the area of an instance of class Square

        Returns:
            int: area of instance of class Square
        """
        return self.__size ** 2
