#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    truth_list = ()
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            truth_list[i] = True
        else:
            truth_list[i] = False
    return truth_list
