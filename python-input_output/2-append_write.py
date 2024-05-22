#!/usr/bin/python3
"""Includes append_write function"""


def append_write(filename="", text=""):
    """Appends a string to the end of a text file (UTF-8)
    and returns the number of chars written"""

    with open(filename, 'a', encoding='utf-8') as file:
        chars = file.write(text)
    return chars
