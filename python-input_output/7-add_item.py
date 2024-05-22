#!/usr/bin/python3
"""saves arguments to a json file"""
import sys

load = __import__('6-load_from_json_file').load_from_json_file
save = __import__('5-save_to_json_file').save_to_json_file

try:
    args = load("add_item.json")
except FileNotFoundError:
    args = []

for arg in sys.argv[1:]:
    args.append(arg)

save(args, "add_item.json")
