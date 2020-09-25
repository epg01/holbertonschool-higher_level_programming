#!/usr/bin/python3

Counter = 1
Counter_To_Limit = 1
Number_Limit = 9
Number = 1
Separator = ', '
while Number is not 100:
    if Number is 89:
        Separator = '\n'

    if Number < 10:
        print("{0:d}{1:d}".format(0, Number), end=Separator)
    else:
        print("{0:d}".format(Number), end=Separator)

    if Counter_To_Limit == Number_Limit:
        Counter += 1
        Number += Counter
        Number_Limit -= (1)
        Counter_To_Limit = 0
    Number += 1
    Counter_To_Limit += 1
