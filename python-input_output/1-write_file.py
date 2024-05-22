#!/usr/bin/python3
"""Includes the write_file function"""


def write_file(filename="", text=""):
    """writes a string to a text file (UTF-8)
    and returns the number of chars written"""

    with open(filename, 'w', encoding='utf-8') as file:
        chars = file.write(text)
    return chars
