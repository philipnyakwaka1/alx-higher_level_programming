#!/usr/bin/python3
"""Module for class Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Defines class Square"""

    def __init__(self, size):
        """Initialzes class Rectangle"""

        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """returns area"""

        return self.__size ** 2

    def __str__(self):
        """returns string representation of an instance of class Rectangle"""

        return f"[Square] {self.__size}/{self.__size}"
