#!/usr/bin/python3
"""Includes class_to_json function"""


def class_to_json(obj):
    """returns the dictionary description with
    simple data structure (list, dictionary, string,
    integer and boolean) for JSON serialization of an object"""

    if hasattr(obj, '__dict__') is False:
        raise ValueError("")

    json_dict = {}
    for key, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            json_dict[key] = value
    return json_dict
