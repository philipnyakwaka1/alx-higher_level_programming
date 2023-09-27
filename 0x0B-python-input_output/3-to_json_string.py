#!/usr/bin/python3
"""module for from_json_string"""
import json


def to_json_string(my_str):
    """returns an object (Python data structure)
    represented by a JSON string"""

    return json.dumps(my_str)

