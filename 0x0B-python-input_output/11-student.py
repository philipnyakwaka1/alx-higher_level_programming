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
            return {i: getattr(self, i) for i in attrs if hasattr(self, i)}
        return self.__dict__

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""

        for attr, val in self.__dict__.items():
            for key, value in json.items():
                if attr == key:
                    self.__dict__[attr] = value
