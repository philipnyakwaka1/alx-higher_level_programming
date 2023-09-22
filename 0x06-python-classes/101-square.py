#!/usr/bin/python3
"""module for class Square"""


class Square(object):
    """Defines class Square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes class square"""

        self.size = size
        self.position = position

    @property
    def size(self):
        """returns size"""

        return self.__size

    @size.setter
    def size(self, value):
        """sets size"""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """returns position"""

        return self.__position

    @position.setter
    def position(self, value):
        """sets size"""

        if (not isinstance(value, tuple) and (len(value) != 2 and
            all(not isinstance(i, int) for i in value)) and
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integer")

        self.__position = value

    def area(self):
        """returns area"""

        return self.__size ** 2

    def my_print(self):
        """prints square"""

        for _ in range(self.__position[1]):
            print()
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """string representation of square"""

        result = ""
        if self.__size == 0:
            return result
        else:
            for _ in range(self.__position[1]):
                result += "\n"
            for _ in range(self.__size):
                result += " " * self.__position[0] + "#" * self.__size + "\n"
            return result.rstrip("\n")
