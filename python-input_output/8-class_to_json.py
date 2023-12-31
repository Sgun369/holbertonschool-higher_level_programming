#!/usr/bin/python3
"""
Class to JSON module
"""


def class_to_json(obj):
    """"
    a function that returns the dictionary description
    with simple data structure
    (list,dictionary,string,integer and boolean)
    for JSON serialization of an object
    """
    if hasattr(obj, '__dict__'):
        return obj.__dict__
    else:
        raise TypeError("Object not serializable")
