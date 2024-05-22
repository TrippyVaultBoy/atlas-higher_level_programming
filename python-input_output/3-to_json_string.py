#!/usr/bin/python3
"""Includes to_json_string function"""
import json


def to_json_string(my_obj):
    """returns JSON rep of a string object"""
    return json.dumps(my_obj)
