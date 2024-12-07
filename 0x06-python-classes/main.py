#!/usr/bin/env python3

"""Class Square"""

class Square:
    """Class Square"""
    def __init__(self, size=0, position=(0, 0)):
        """initialize"""
        self.size = size
        self.position = position
    
    @property
    def position(self):
        """get position"""
        return self.__position

    @position.setter
    def position(self, value):
        """set position"""
        if type(value) == tuple and type(value[0]) == int and type(value[1]) == int and value[0] >= 0 and value[1] >= 0:
            self.__position = value
        else:
            raise TypeError('position must be a tuple of 2 positive integers')

    @property
    def size(self):
        """get size"""
        return self.__size

    @size.setter
    def size(self, value):
        """set size"""
        if type(value) != int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        "return area"
        return self.__size ** 2

    def my_print(self):
        """print square"""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(' ' * self.__position[0] + '#' * self.__size)

my_square_1 = Square(3)
my_square_1.my_print()

print("--")

my_square_2 = Square(3, (1, 1))
my_square_2.my_print()

print("--")

my_square_3 = Square(3, (3, 0))
my_square_3.my_print()

print("--")
