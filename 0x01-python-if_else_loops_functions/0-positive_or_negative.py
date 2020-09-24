#!/usr/bin/python3
import random
Number = random.randint(-10, 10)
if Number is 0:
    print("{0:d} is zero".format(Number))
elif Number > 0:
    print("{0:d} is positive".format(Number))
else:
    print("{0:d} is negative".format(Number))
