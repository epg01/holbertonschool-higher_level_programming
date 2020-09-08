#!/usr/bin/python3

def element_at(my_list, idx):
    if idx < len(my_list):
        if not idx:
            return my_list[0]
        else:
            idx -= 1
            return element_at(my_list[1:], idx)
