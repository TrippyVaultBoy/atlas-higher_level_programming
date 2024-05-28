#!/usr/bin/python3
"""Includes Square class that inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines class Square that inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

        self.__width = size
        self.__height = size

    def __str__(self):
        return "[{:s}] ({:d}) {:d}/{:d} - {:d}".format(
            type(self).__name__, self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """size getter"""
        return self.width

    @size.setter
    def size(self, value):
        """size setter"""
        self.attribute_validate(value, "width")

        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """updates class instance attributes"""
        for i in range(len(args)):
            if i == 0:
                self.id = args[i]
            if i == 1:
                self.height = args[i]
                self.width = args[i]
            if i == 2:
                self.x = args[i]
            if i == 3:
                self.y = args[i]

        if args is not None:
            for key in kwargs:
                if key == "id":
                    self.id = kwargs[key]
                if key == "size":
                    self.width = kwargs[key]
                    self.height = kwargs[key]
                if key == "x":
                    self.x = kwargs[key]
                if key == "y":
                    self.y = kwargs[key]
