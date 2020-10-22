#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    if my_list is not None:
        for value in reversed(my_list):
            print("{0:d}".format(value))
