#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        Number_print = int()
        for times in range(x):
            hold_item = my_list.pop(times)
            print("{0}".format(hold_item), end='')
            my_list.insert(times, hold_item)
            Number_print += 1
        print()
    except:
        print()
        return Number_print
    return Number_print
