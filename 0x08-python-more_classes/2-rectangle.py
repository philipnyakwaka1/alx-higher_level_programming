#!/usr/bin/python3
"This module defines class Rectangle()"


class Rectangle():
    """Defines class Recyangle"""

    def __init__(self, width=0, height=0):
        """
        Initializes an instance of class Rectangle()
        Args:
            width: rectangle width
            height: rectangle height
        Raises:
            TypeError: if width and height is not an integer
            ValueError: if width and height is less than zero
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """property decorator for retrieving rectangle width"""

        return self.__width

    @width.setter
    def width(self, width):
        """sets rectangle width"""

        if type(width) != int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        """property decorator for retrieving rectangle height"""

        return self.__height

    @height.setter
    def height(self, height):
        """sets rectangle height"""

        if type(height) != int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    def area(self):
        """returns area of rectangle object"""

        return self.__width * self.__height

    def area(self):
        """returns perimeter of rectangle object"""

        return (2 * self.__width) + (2 * self.__height)
