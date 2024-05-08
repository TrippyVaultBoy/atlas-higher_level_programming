#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    print_count = 0

    try:
        for element in my_list:
            if print_count >= x:
                break
            try:
                print("{:d}".format(element), end="")
                print_count += 1
            except ValueError:
                pass
    except TypeError:
        pass
    print()
    return print_count
