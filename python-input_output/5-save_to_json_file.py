#!/usr/bin/python3
"""Includes save_to_json_file function"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file with json representation"""
    if isinstance(my_obj, set):
        raise TypeError("Object of type set is not JSON serializable")
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)
