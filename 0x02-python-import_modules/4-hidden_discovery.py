#!/usr/bin/python3


if __name__ == '__main__':
    import hidden_4

    List_Method = dir(hidden_4)

    for item in List_Method:
        if item.startswith('__'):
            pass
        else:
            print("{method}".format(method=item))
