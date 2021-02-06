#!/usr/bin/python3


if __name__ == '__main__':
    from add_0 import add

    a, b = (1, 2)

    print("{a:d} + {b:d} = {result:d}".format(a=a, b=b, result=add(a, b)))
