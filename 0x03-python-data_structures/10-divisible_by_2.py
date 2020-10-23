#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list is not None and my_list:
        new_list = list()
        for value in my_list:
            if not value % 2:
                new_list.append(True)
            else:
                new_list.append(False)
        return new_list
