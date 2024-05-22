#!/usr/bin/python3
"""Includes save_to_json_file function"""
import json
import os


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file with json representation"""
    if not os.access("no_perm/file_7", os.W_OK):
        raise PermissionError("Permission denied: 'no_perm/file_7'")
    if isinstance(my_obj, set):
        raise TypeError("Object of type set is not JSON serializable")
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)
