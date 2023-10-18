#!/usr/bin/python3
""""
module Only sub class of
"""


def inherits_from(obj, a_class):
    """"
    a function that returns True if the object is an instance of a class
    that inherited (directly or inde=irectly) from the specified class
    ptherwise False
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
