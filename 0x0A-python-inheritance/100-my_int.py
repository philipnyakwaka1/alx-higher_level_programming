#!/usr/bin/python3


class MyInt(int):
    """Defines class MyInt"""
    def __eq__(self, other):
        """overide =="""

        return super().__ne__(other)

    def __ne__(self, other):
        """overide !="""

        return super().__eq__(other)
