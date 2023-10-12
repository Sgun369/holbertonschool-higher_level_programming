#!/usr/bin/python3
"""
a module that prints a square with "#"
"""


def print_square(size):
    """
    print a square of "#" characters with the specified size.

    Parameters:
        size(int or float): size of the square.
    Raises:
        TypeError: If size is not an integer or float
        ValueError if size is less than 0
    """

    if not isinstance(size, int) or (isinstance(size, float) and size < 0):
        if isinstance(size, float):
            raise TypeError("size must be an integer")
        raise ValueError("size must be >= 0")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
