#!/usr/bin/python3
from models.base import Base


"""Module for class Rectangle()"""


class Rectangle(Base):
    """Defines class Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """constructor for class Rectangle()"""

        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """getter method for width"""

        return self.__width

    @width.setter
    def width(self, width):
        """setter method for width"""

        self.__width = width

    @property
    def y(self):
        """getter method for y"""

        return self.__y

    @y.setter
    def y(self, y):
        """setter method for y"""

        self.__y = y

    @property
    def height(self):
        """getter method for height"""

        return self.__height

    @height.setter
    def height(self, height):
        """setter method for height"""

        self.__height = height

    @property
    def x(self):
        """getter method for x"""

        return self.__x

    @x.setter
    def x(self, x):
        """setter method for x"""

        self.__x = x
