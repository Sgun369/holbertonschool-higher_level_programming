#!/usr/bin/python3
"""writing a class Square that defines a square by:
private instance attribute size
instantiation with optional size: def __init__(self, size=0)"""


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

    def area(self):
        """Public instance method:
        def area(self):
        that returns the current square area"""
        return (self.__size ** 2)
