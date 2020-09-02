#!/usr/bin/python3
def uppercase(str):
    if not str:
        return None
    for Index in range(len(str)):
        Character = str[Index]
        Solve_Character = Character
        if ord(Character) >= 97 and ord(Character) <= 122:
            Character = chr(ord(Character) - 97 + 65)
        if Index < (len(str) - 1):
            print("{}".format(Character if ord(Character) >= 65 and
                              ord(Character) <= 90 else Character), end='')
        else:
            print("{}".format(Character if ord(Character) >= 65 and
                              ord(Character) <= 90 else Character))
