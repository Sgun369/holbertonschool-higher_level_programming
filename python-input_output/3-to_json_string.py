#!/usr/bin/python3
"""
To Json module
"""

import json


def to_json_string(my_obj):
    """"
    a function that returs the JSON representation
    of an object(string).
    """
    return json.dumps(my_obj)
