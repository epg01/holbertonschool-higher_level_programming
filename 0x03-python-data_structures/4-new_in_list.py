#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or (idx not in range(len(my_list))):
        pass
    else:
        copy_list_S = my_list.copy()
        copy_list_S[idx] = element
    return copy_list_S
