#!/usr/bin/python3

def uppercase(str):
    for char in str:
        if ord('a') <= ord(char) <= ord('z'):
            print("{}".format(chr(ord(char) - 32)))
        else:
            print("{}".format(char))
