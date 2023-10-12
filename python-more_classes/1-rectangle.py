#!/usr/bin/python3
class Rectangle:
    def __init__(self, width=0, height=0):
        """
        Initialize a Rectangle instance.

        args:
            width(init, optional):The width Defaults to 0
            height (init, optional):The eight Defaults to 0
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Retrieve the width of the rectangle.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        set the width of the rectangle.

        args:
        value (int): The new width value.

        Raises:
            TypeError: If the width is not an integer.
            ValueError: If the width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

        @property
        def height(self):
            """
            Retrieve the height of the rectangle.

            Returns:
            int: The height of the rectangle.
            """
            return self.__height

        @height.setter
        def height(self, value):
            """
            set the height of the rectangle.

            args:
                value (int):The new height value.

            Raises:
                TypeError: If the height is not an integer.
                ValueError: IF the height is less than 0.
            """
            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            if value < 0:
                raise ValueError("height must be >= 0")
            self.__height = value
