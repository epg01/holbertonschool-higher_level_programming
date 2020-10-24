#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return [replace
            if search - 1 == index
            else my_list[index]
            for index in range(len(my_list))]
