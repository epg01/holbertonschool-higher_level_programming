#!/usr/bin/python3
def uppercase(String):

    for Character in String:
        Number = ord(Character)
        if Number >= 97 and Number <= 122:
            print("{0:s}".format(chr(Number - 97 + 65)), end='')
        else:
            print("{0:s}".format(Character), end='')
    print()
