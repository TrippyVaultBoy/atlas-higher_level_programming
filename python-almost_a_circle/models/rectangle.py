#!/usr/bin/python3
"""Includes class Rectangle"""
from models.base import Base


class Rectangle(Base):
    """defines the class Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)

        self.attribute_validate(width, "width")
        self.attribute_validate(height, "height")
        self.attribute_validate(x, "x")
        self.attribute_validate(y, "y")

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        self.attribute_validate(value, "width")

        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        self.attribute_validate(value, "height")

        self.__height = value

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter"""
        self.attribute_validate(value, "x")

        self.__x = value

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter"""
        self.attribute_validate(value, "y")

        self.__y = value

    def area(self):
        """returns area if the rectangle instance"""
        return self.__width * self.__height

    def attribute_validate(self, attr, var):
        """validates attribute type and value"""
        if type(attr) is not int:
            raise TypeError(var + " must be an integer")

        if attr <= 0 and var in ("width", "height"):
            raise ValueError(var + " must be > 0")

        if attr < 0 and var in ("x", "y"):
            raise ValueError(var + " must be >= 0")
