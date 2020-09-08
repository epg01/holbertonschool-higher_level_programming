#!/usr/bin/python3
def print_list_integer(my_list=[]):
    if my_list:
        print("{:d}".format(my_list[0]))
        print_list_integer(my_list[1:])
