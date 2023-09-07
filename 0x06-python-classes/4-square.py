#!/usr/bin/python3
"""This module defines an class Square"""


class Square:
    """This is a class square"""

    def __init__(self, size=0):
        """__init__ method initializes the size of the new square

        Args:
            size: size of the square, which is initialized at 0
        """
        self.__size = size

    @property
    def size(self):
        """getter method to get the current size of the square

            Returns:
            int: current size of square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """setter method to set size of square

        Args:


A
A
A
D
D
D
C
            value: size of square to be set
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Calculates the area of an instance of class Square

        Returns:
            int: area of instance of class Square
        """
        return self.__size ** 2
