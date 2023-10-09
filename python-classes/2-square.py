#!/usr/bin/python3
"""writing a class Square based on 1-square.py"""


class Square:
    """create a Square"""
    def __init__(self, size=0):
        """intitilazing the square"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
