#!/usr/bin/python3


if __name__ == '__main__':
    import add_0

    a, b = (1, 2)

    print("{a} + {b} = {result}".format(a=a, b=b, result=add_0.add(a, b)))
