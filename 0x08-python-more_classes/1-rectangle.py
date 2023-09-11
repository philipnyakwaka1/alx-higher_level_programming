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
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """This function returns the width attribute"""
        return self.__width

    @width.setter
    def width(self, width):
        """This functions sets the width attribute
        Return:
            int: rectangle width
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        """This functions returns the height attribute"""
        return self.__height

    @height.setter
    def height(self, height):
        """This function sets the height attribute
        Return:
            int: rectangle height
        """
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
