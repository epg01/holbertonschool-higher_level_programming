#!/usr/bin/python3


if __name__ == '__main__':
    import sys

    if (len(sys.argv)) == 2:
        print("{length} argument:".format(length=1))
        print("1: {name_argv}".format(name_argv=sys.argv[1]))
    elif (len(sys.argv)) > 1:
        print("{length} arguments:".format(length=len(sys.argv[1:])))
        for num_argv, argv in enumerate(sys.argv[1:], start=1):
            print("{num}: {argv}".format(num=num_argv, argv=argv))
    else:
        print("0 argument.")
