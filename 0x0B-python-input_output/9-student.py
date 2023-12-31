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

    def to_json(self, attrs=None):
        """
        retrieves dictionary representation
        of an instance of class Student
        Args:
            attrs(list): a list of attributes
        Return: If attrs is a list of strings, only attribute
        names contained in this list must be retrieved else a dict of
        all attributes is returned
        """

        if type(attrs) == list and all(type(item) == str for item in attrs):
            my_dict = {}
            return {item: getattr(self, item) for item in attrs if hasattr(self, item)}
        return self.__dict__
