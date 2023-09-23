#!/usr/bin/python3
"""Module for class Rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Defines class REctangle"""

    def __init__(self, width, height):
        """Initialzes class Rectangle"""

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """returns area"""

        return self.__width * self.__height

    def __str__(self):
        """returns string representation of an instance of class Rectangle"""

        return f"[Rectangle] {self.__width}/{self.__height}"
