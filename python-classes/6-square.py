#!/usr/bin/python3
"""writing a class Square that defines a square by:
private instance attribute size
instantiation with optional size: def __init__(self, size=0)"""


class Square:
    """create a Square"""
    def __init__(self, size=0, position=(0, 0)):
        """intitilazing the square"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """property def size(self): to retrieve it"""
        return self.__size

    @size.setter
    def size(self, value):
        """sets the value"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """
        pisition getter
        """
        return self.position

    @position.setter
    def position(self, value):
        """
        to set the position
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(i, int) for i in value) or
                not all(i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Public instance method:
        def area(self):
        that returns the current square area"""
        return (self.__size ** 2)

    def my_print(self):
        """prints in stdout the square
        with the character #:"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.size)
