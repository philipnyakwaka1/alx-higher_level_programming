#!/usr/bin/python3
"""This is module for class Rectangle"""


class Rectangle(object):
    """Defines class Rectangle"""

    def __init__(self, width=0, height=0):
        """Initializes class Rectangle"""

        self.width = width
        self.height = height

    @property
    def width(self):
        """returns width"""

        return self.__width

    @width.setter
    def width(self, value):
        """sets width"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """returns width"""

        return self.__height

    @height.setter
    def height(self, value):
        """sets width"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns area"""

        return self.__width * self.__height

    def perimeter(self):
        """returns perimeter"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * self.__width + 2 * self.__height

    def __str__(self):
        """print representation"""

        if self.__height == 0 or self.__width == 0:
            return ""
        my_string = ""
        for i in range(self.__height):
            for j in range(self.__width):
                my_string += "#"
            my_string += "\n"
        return my_string[:-1]
