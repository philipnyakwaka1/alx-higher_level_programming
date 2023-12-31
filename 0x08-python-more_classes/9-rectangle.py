#!/usr/bin/python3
"""This is module for class Rectangle"""


class Rectangle(object):
    """Defines class Rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes class Rectangle"""

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
                my_string += str(self.print_symbol)
            my_string += "\n"
        return my_string[:-1]

    def __repr__(self):
        """return a string representation of the rectangle
        to be able to recreate a new instance by using eval()"""

        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """prints a string when deletion occurs"""

        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns bigger rectangle"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        return cls(size, size)
