#!/usr/bin/python3
"""This is a module for the rectangle class"""


class Rectangle():
    """This is a Rectangle class"""

    def __init__(self, width=0, height=0):
        """The __init__ method initializes an object of class Rectangle
        Args:
            width: the width of the rectangle
            height: the height of the rectangle
        Raises:
            TypeError: if width and height is not an integer
            ValueError: if width and height is less than zero
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """This function returns the width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """This functions sets the width attribute
        Return:
            int: rectangle width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """This functions returns the height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """This function sets the height attribute
        Return:
            int: rectangle height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
