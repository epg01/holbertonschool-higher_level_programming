#!/usr/bin/python3
def no_c(my_string):
    if my_string is not None:
        String_Copy = "".join(my_string.split('C'))
        return "".join(String_Copy.split('c'))
