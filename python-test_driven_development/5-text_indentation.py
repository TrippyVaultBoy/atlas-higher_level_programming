#!/usr/bin/python3
"""Includes text_indentation function"""


def text_indentation(text):
    """prints a text with 2 new lines after
    each of these characters: ., ? and :

    text must be a string, otherwise raise a
    TypeError exception with the message
    text must be a string

    There should be no space at the beginning
    or at the end of each printed line"""
    lines = text.split('\n')
    for line in lines:
        line = line.strip()
        for char in line:
            if ((char == '.') or (char == '?') or (char == ':')):
                print(char, end='')
                print()
                print()
            else:
                print(char, end='')
