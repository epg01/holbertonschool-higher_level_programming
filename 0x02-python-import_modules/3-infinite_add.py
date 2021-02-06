#!/usr/bin/python3


if __name__ == '__main__':
    import sys

    # Convert the str type to int type.

    try:

        List_Num = [int(item) for item in sys.argv[1:]]

    except:

        print('0')

    # Then Convert the list an iterable data type --> iter()

    Iter_Num = iter(List_Num)
    print("{result_sum}".format(result_sum=sum(Iter_Num)))
