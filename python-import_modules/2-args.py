#!/usr/bin/python3
from sys import argv

def args(argv):
    if len(argv) == 1:
        print("1 argument:", end="")
    elif len(argv) > 1:
        print("{} arguments:".format(len(argv) - 1), end="")
    elif len(argv) == 0:
        print("0 arguments.", end="")

    for i in range(1, len(argv)):
        print("{}: {}".format(i, argv[i]))

if __name__ == "__main__":
    print_arg()
