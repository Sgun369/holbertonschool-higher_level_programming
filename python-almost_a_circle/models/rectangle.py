#!/usr/bin/python3
"""First Rectangle module"""

from models.base import Base


class Rectangle(Base):
    """class Rectangle that inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initializes the rectangle"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)


@property
def width(self):
    """getter method for width"""
    return self.__width


@width.setter
def width(self, value):
    """setter method for width"""
    if not isinstance(value, int):
        raise TypeError("width must be an integer")
    if value <= 0:
        raise ValueError("width must be > 0")
    self.__width = value


@property
def height(self):
    """gette method for height"""
    return self.__height


@height.setter
def height(self, value):
    """setter method for height"""
    if not isinstance(value, int):
        raise TypeError("height must be an integer")
    if value <= 0:
        raise ValueError("height must be > 0")
    self.__height = value


@property
def x(self):
    """getter method for x"""
    return self.__x


@x.setter
def x(self, value):
    """setter method for x"""
    if not isinstance(value, int):
        raise TypeError("x must be an integer")
    if value < 0:
        raise ValueError("x mst be >= 0")
    self.__x = value


@property
def y(self):
    """getter method for y"""
    return self.__y


@y.setter
def y(self, value):
    """setter method for y"""
    if not isinstance(value, int):
        raise TypeError("y must e an integer")
    if y < 0:
        raise ValueError("y must be >= 0")
    self.__y = value
