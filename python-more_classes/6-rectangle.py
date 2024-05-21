#!/usr/bin/python3
"""
    Defines a Rectangle class.
"""


class Rectangle:
    """
        Creates a rectangle
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((self.__height * 2) + (self.__width * 2))

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""

        rec_str = ""
        for i in range(self.__height):
            for j in range(self.__width):
                rec_str += "#"
            if i < self.__height - 1:
                rec_str += "\n"

        return rec_str

    def __repr__(self):
        rep = "Rectangle(" + str(self.__width) + ", "
        rep += str(self.__height) + ")"
        return rep

    def __del__(self):
        type(self).number_of_instances -= 1
        print("Bye rectangle...")