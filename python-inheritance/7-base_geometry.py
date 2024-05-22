#!/usr/bin/python3
"""Includes BaseGeometry class"""


class BaseGeometry:
    """BaseGeometry class"""
    
    def area(self):
        """method to calculate area"""
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """validates value"""
        if isinstance(value, int) == False:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
