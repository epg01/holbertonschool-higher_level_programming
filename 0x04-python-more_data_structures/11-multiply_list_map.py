#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    number = [number for item in my_list]
    return list(map(lambda x, number: x * number, my_list, number))
