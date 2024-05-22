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
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
