#!/usr/bin/python3
"""This is module for Rectangle class"""

from models.base import Base


class Rectangle(Base):
    """This is the Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """This function initializes an instance of class Rectangle
            Args:
                width: rectangle width
                height: rectangle height
                x: rectangle attribute
                y: rectangle attribute
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """This function returns the rectangle width"""

        return self.__width

    @width.setter
    def width(self, value):
        """This function sets the rectangle width"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """This function returns the rectangle height"""

        return self.__height

    @height.setter
    def height(self, value):
        """sets the height attribute"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """returns the x attribute"""

        return self.__x

    @x.setter
    def x(self, value):
        """sets x attribute"""

        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """returns y attribute"""

        return self.__y

    @y.setter
    def y(self, value):
        """sets y attribute"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns area of rectangle object"""

        return self.width * self.height

    def display(self):
        """displays rectangle to stdout"""

        for y in range(self.y):
            print()
        for x in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """returns string representation of the object"""

        str1 = f"[Rectangle] ({self.id}) {self.x}/{self.y}"
        str2 = f" - {self.width}/{self.height}"
        return str1 + str2
