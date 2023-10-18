#!/usr/bin/python3
"""
module write to a file
"""


def write_file(filename="", text=""):
    """"
    a function tha writes a string to a text file (UTF8)
    and returrns the number of characters
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return (f.write(text))
