#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0 or (idx not in range(list(my_list))):
        pass
    else:
        my_list[idx] = element
    return my_list
