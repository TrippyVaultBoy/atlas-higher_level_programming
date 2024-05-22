#!/usr/bin/python3
"""Includes class Student"""


class Student:
    """represents a student"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dictionary representation
        of a Student instance"""
        student_dict = {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age", self.age
        }
        return student_dict
