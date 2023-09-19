 #!/usr/bin/python3
"""This is module for class Square"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """This is class Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """initializes an instance of class Square"""
        super().__init__(size, size, x, y, id=None)

    @property
    def size(self):
        """returns size"""

        return self.height

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
