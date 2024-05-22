#!/usr/bin/python3
"""Includes from_json_string function"""
import json


def from_json_string(my_str):
    """returns an object rep by a json string"""
    return json.loads(my_str)
