#!/usr/bin/python3
from sys import argv


def inf_add(argv):
    sum = 0
    for i in range(argv):
        sum += int(argv)
    print(sum)


if __name__ == "__main__":
    inf_add(argv)