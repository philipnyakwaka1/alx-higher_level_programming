#!/usr/bin/python3
"""This is module for class Square"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """This is class Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """initializes an instance of class Square"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """returns size"""

        return self.width

    @size.setter
    def size(self, value):
        """sets size"""

        self.width = value
        self.height = value

    def __str__(self):
        """returns string represenation of class Square"""

        str1 = f"[Square] ({self.id}) {self.x}/{self.y}"
        str2 = f" - {self.size}"
        return str1 + str2

    def update(self, *args, **kwargs):
        """updates class Square"""

        if args:
            try:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            except Exception as ex:
                pass
        else:
            for key, value in kwargs.items():
                self.__setattr__(key, value)

    def to_dictionary(self):
        """returns the dictionary representation of square object"""

        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
