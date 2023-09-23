#!/usr/bin/python3
"""module for to_json_string"""
import json


def from_json_string(my_obj):
    """returns the JSON representation of an object (string)"""

    return json.loads(my_obj)
