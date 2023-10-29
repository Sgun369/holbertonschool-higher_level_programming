#!/usr/bin/python3
""""the Suare module"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square that inherits from Recttangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Class constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """returns a string representation of the class"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)

    @property
    def size(self):
        """"zize getter"""
        return self.width

    @size.setter
    def size(self, size):
        """size setter"""
        if not isinstance(size, int):
            raise TypeError("width must be an integer")
        if size <= 0:
            raise ValueError("width must be > 0")
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """assigns attributes:"""
        i = 0
        for arg in args:
            if i == 0:
                self.id = arg
            if i == 1:
                self.size = arg
            if i == 2:
                self.x = arg
            if i == 3:
                self.y = arg
            i += 1
        if not args:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """returns the dictionary representation of quare"""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }
