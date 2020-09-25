#!/usr/bin/python3
def uppercase(String):
    Separator = ''
    Counter_Length_String = 1
    for Character in String:
        Number = ord(Character)
        if Counter_Length_String == len(String):
            Separator = '\n'

        if Number >= 97 and Number <= 122:
            print("{0:s}".format(chr(Number - 97 + 65)), end=Separator)
        else:
            print("{0:s}".format(Character), end=Separator)
        Counter_Length_String += 1
