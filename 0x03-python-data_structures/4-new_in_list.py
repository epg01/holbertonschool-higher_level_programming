#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if my_list is not None and idx in range(len(my_list)):
        my_list_clone = list(my_list)
        my_list_clone[idx] = element
        return my_list_clone
    else:
        return list(my_list)
