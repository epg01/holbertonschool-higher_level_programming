#!/usr/bin/python3
def no_c(my_string):
    if 'C' in my_string:
        my_string = list(my_string)
        my_string.remove('C')
        return no_c(''.join(my_string))
    elif 'c' in my_string:
        my_string = list(my_string)
        my_string.remove('c')
        return (''.join(my_string))
    else:
        return (my_string)
