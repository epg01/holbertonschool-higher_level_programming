#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    Copy_List_Superficial = list(my_list)
    Copy_List_Superficial.reverse()
    for item in Copy_List_Superficial:
        print('{Number:d}'.format(Number=item))
