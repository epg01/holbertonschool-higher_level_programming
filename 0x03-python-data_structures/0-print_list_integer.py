#!/usr/bin/python3


def print_list_integer(my_list=[]):
    try:
        for item in my_list:
            print("{Number}".format(Number=item))
    except:
        pass
