#!/usr/bin/python3
"""Includes say_my_name function"""


def say_my_name(first_name, last_name=""):
    """prints My name is <first name> <last name>
    first_name and last_name must be strings otherwise,
    raise a TypeError exception with the message first_name
    must be a string or last_name must be a string"""

    if not isinstance(first_name, string):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, string):
        raise TypeError("last_name must be a string")

    print("My name is {:s} {:s}".format(first_name, last_name))