#!/usr/bin/python3

for Character in range(97, 123, 1):
    if chr(Character) is not 'e' and chr(Character) is not 'q':
        print("{:s}".format(chr(Character)), end='')
