#!/usr/bin/python3
"""
module to print first name and last name
"""

def say_my_name(first_name, last_name =""):
    """
    Print a message with the first name and last name

    parameters:
        first_name (str)
        last_name (str)
    Raises:
        TypeError: IF either first_name or last_name
        is not a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last name must be a string")
    
    print("My name is {:s} {:s}".format(first_name, last_name))
    