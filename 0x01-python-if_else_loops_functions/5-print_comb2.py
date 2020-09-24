#!/usr/bin/python3

Separator = ', '
for Number in range(0, 100, 1):
    if Number < 10:
        print("{0:d}{1:d}".format(0, Number), end=Separator)
    else:
        if Number is 99:
            Separator = '\n'
        print("{0:d}".format(Number), end=Separator)
