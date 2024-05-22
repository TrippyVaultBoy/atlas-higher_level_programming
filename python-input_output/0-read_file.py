#!/usr/bin/python3
"""Includes read_file function"""


def read_file(filename=""):
    """Reads a text file (UTF8) and prints to stdout"""
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
        print(content, end="")
