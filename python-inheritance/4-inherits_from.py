#!/usr/bin/python3
"""Includes inherites_from function"""


def inherits_from(obj, a_class):
    """Checks if obj is an instance of an inhertited class"""
    if type(obj) is a_class:
        return False
    else:
        return isinstance(obj, a_class)
