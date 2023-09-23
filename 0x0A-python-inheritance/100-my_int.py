#!/usr/bin/python3
"""module for MyInt"""


class MyInt(int):
    """Defines class MyInt"""
    def __eq__(self, val):
        """overide =="""

        return self.real != val

    def __ne__(self, val):
        """overide !="""

        return self.real == val
