#!/usr/bin/python3
for i in range(10):
    if i == 9:
        print("{i:02}".format(i))
    else:
        print("{i:02}, ".format(i), end="")
