#!/usr/bin/python3
"""
From JSON string to Object module
"""

import json


def from_json_string(my_str):
    """
    a function that returns an object (python data structure)
    represented by JSON string.
    """
    return json.loads(my_str)
