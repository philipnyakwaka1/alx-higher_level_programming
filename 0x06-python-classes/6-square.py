#!/usr/bin/python3
"""This module defines a class Square"""


class Square:
    """This is a class square"""

    def __init__(self, size=0, position=(0, 0)):
        """__init__ method initializes the size of the new square

        Args:
            size: size of the square, which is initialized at 0
        """
        self.__size = size
        self.__position = position

    @property
    def position(self):
        """getter method to get the current position

        Returns:
            int: tuple of two integers
        """
        return self.__position

    @position.setter
    def position(self, value):
        """setter method to set the position value

        Args:
            value: value of position to be set
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(i, int) for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        if any(i < 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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

    def my_print(self):
        """prints an instance of class Square"""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
