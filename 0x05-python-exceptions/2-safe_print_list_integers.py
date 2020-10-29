#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    Number_print = int()
    for index in range(x):
        try:
            print("{0:d}".format(my_list[index]), end='')
            Number_print += 1
        except (ValueError, TypeError):
            pass
    print()
    return Number_print
