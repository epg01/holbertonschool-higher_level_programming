#!/usr/bin/python3


def safe_print_division(a, b):
    try:
        Result = a / b
    except ZeroDivisionError:
        Result = None
    finally:
        print("{0:s}: {1:}".format("Inside result", Result))
        return Result
