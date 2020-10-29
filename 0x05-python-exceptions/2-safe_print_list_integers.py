#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    try:
        Number_print = int()
        for index in range(x):
            hold_item = my_list[index]
            if type(int()) is type(hold_item):
                print("{0:d}".format(hold_item), end='')
                Number_print += 1
        print()
    except:
        raise

    return Number_print
