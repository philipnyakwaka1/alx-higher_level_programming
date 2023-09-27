#!/usr/bin/python3
"""module for class Student"""


class Student():
    """Defines class Student"""

    def __init__(self, first_name, last_name, age):
        """
        initializes the class
        Args:
            first_name(str): student's first name
            last_name(str): student's last name
            age(int): student's age
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves dictionary representation
        of an instance of class Student"""

        return self.__dict__
