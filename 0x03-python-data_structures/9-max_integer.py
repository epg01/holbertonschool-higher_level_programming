#!/usr/bin/python3
def search_max(my_list, max_value, length):
    if not length:
        if max_value < my_list[0]:
            return my_list[0]
        else:
            return max_value
    else:
        if max_value < my_list[0]:
            max_value = my_list[0]
        return search_max(my_list[1:], max_value, length - 1)


def max_integer(my_list=[]):
    if my_list is not None and my_list:
        return (search_max(my_list, my_list[0], len(my_list) - 1))
