#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    number = list(map(lambda Number: Number, my_list))
    return list(map(lambda x, number: x * number, my_list, number))
