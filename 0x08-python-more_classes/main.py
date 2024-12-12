#!/usr/bin/python3
"""Class rectangle"""

class Rectangle:
    """class Rectangle"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """instantiate"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1
    
    @property
    def width(self):
        """get width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set width"""
        if type(value) != int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """get height"""
        return self.__height

    @height.setter
    def height(self, value):
        """set height"""
        if type(value) != int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """return area"""
        return self.__width * self.__height

    def perimeter(self):
        """return perimeter"""
        return 2 * self.__height + 2 * self.__width

    def __str__(self):
        """print rectangle"""
        if self.__height == 0 or self.__width == 0:
            return ''
        _str = ''
        for _ in range(self.__height):
            _str += str(self.print_symbol) * self.__width + '\n'
        return _str

    def __repr__(self):
        """rep"""
        return f'Rectangle({self.__width}, {self.__height})'

    def __del__(self):
        """delete"""
        print('Bye rectangle...')
        Rectangle.number_of_instances -= 1

    def bigger_or_equal(rect_1, rect_2):
        """compare rectangles"""
        if not isinstance(rect_1, Rectangle):
            print('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            print('rect_2 must be an instance of Rectangle')
        if rect_1.area() >= rect_2.area():
            return rect_1
        elif rect_1.area() < rect_2.area():
            return rect_2
    
    @classmethod
    def square(cls, size=0):
        """return rectangle of equal sides"""
        return cls(size, size)

my_square = Rectangle.square(5)
print("Area: {} - Perimeter: {}".format(my_square.area(), my_square.perimeter()))
print(my_square)