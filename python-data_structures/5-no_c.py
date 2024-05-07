#!/usr/bin/python3

def no_c(my_string):
    str_copy = my_string[:]
    for i in range(len(str_copy)):
        if str_copy[i] == 'c' or str_copy[i] == 'C':
            str_copy[i] = ""
    return str_copy
