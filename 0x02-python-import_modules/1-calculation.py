#!/usr/bin/python3


if __name__ == '__main__':
    from calculator_1 import add, sub, mul, div

    a = 10
    b = 5

    sing = tuple(['+', '-', '*', '/'])
    operator = tuple([add, sub, mul, div])

    for sing, oper in zip(sing, operator):
        print('{a:d} {sing:s} {b:d} = {result:d}'.format(a=a, b=b, sing= sing,
                                                         result=oper(a, b)))
