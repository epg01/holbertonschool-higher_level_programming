#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    my_list_copy = my_list[::-1]
    for value in my_list_copy:
        print("{0:d}".format(value))
