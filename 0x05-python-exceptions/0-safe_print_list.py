#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    if my_list != []:
        try:
            number_of_element_print = int()
            for item_print in range(x):
                print("{0}".format(item_print), end='')
                number_of_element_print += 1
            print()
        except:
            return number_of_element_print
        return number_of_element_print
