#!/usr/bin/python3
"""Module for class MyList"""


class MyList(list):
    """Defines class MyList"""
    def print_sorted(self):
        """prints sorted list"""

        print(sorted(self))
