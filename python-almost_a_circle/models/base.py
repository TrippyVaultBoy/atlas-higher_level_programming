#!/usr/bin/python3
"""Includes class Base"""
import json


class Base:
    """base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        list_obj = []
        filename = "{:s}.json".format(cls.__name__)

        if list_objs is not None:
            for i in range(len(list_objs)):
                list_obj.append(cls.to_dictionary(list_objs[i]))

        with open(filename, mode="w", encoding="utf-8") as file:
            file.write(cls.to_json_string(list_obj))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        json_to_list = []

        if json_string is not None and json_string != "":
            json_to_list = json.loads(json_string)

        return json_to_list

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
        if cls.__name__ == "Square":
            dummy_instance = cls(1)
        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = "{:s}.json" .format(cls.__name__)

        try:
            with open(filename, "r") as file:
                file_content = file.read()
                obj_list = cls.from_json_string(file_content)
                return [cls.create(**obj) for obj in obj_list]

        except FileNotFoundError:
            return []
