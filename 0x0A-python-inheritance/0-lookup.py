#!/usr/bin/python3
"""This is module for lookup function"""


def lookup(obj):
    """returns list of available attributes and
    method in an object
    """
    return dir(obj)
