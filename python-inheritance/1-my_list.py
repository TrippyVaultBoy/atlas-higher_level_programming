#!/usr/bin/python3
"""Includes definition of the
    MyList class"""


class MyList(list):
    def print_sorted(self):
        """Sorts and prints a list"""
        sorted_list = sorted(self)
        print(sorted_list)
