#!/usr/bin/python3
from add_0 import add


if __name__ == '__main__':

    a, b = (1, 2)

    print("{a:d} + {b:d} = {result:d}".format(a=a, b=b, result=add(a, b)))
