#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if my_list and (idx < len(my_list)):
        copy_list = []
        for index in range(len(my_list)):
            if (index != idx):
                copy_list.append(my_list[index])
            else:
                copy_list.append(element)
        return copy_list
    else:
        return my_list
