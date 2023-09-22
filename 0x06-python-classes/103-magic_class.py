#!/usr/bin/python3
"""This module defines class MagicClass"""

import math


class MagicClass(object):
    """Defines magic class"""

    def __init__(self, radius=0):
        """initializes radius"""
        if not isinstance(radius, int) and not isinstance(radius, float):
            raise TypeError('radius needs to be a number')
        self.__radius = float(radius)

    def area(self):
        """returns area"""

        return self.__radius ** 2 * math.pi

    def circumference(self):
        """returns circumference"""

        return 2 * math.pi * self.__radius
