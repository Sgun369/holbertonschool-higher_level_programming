#!/usr/bin/python3
"""
module to check if an object is an instance of a_class
"""


def is_same_class(obj, a_class):
    """
    check if an object is exactly
    an instance of the specified class.
    """
    if type(obj) == a_class:
        return True
    else:
        return False
