#!/usr/bin/python3
for Number in range(0, 100):
    if Number != 99:
        print("{}{}".format(Number // 10, Number % 10), end=", ")
    else:
        print("{}{}".format(Number // 10, Number % 10))
