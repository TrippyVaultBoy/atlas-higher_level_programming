#!/usr/bin/python3
"""Includes save_to_json_file function"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file with json representation"""
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)
