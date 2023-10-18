#!/usr/bin/python3
""""
Read file module
"""


def read_file(filename=""):
    """
    a function that reads a text file (UTF8) and
    prints to stdout
    """
    with open('my_file_0.txt', mode='r', encoding="utf-8", ) as f:
        print(f.read(), end="")
