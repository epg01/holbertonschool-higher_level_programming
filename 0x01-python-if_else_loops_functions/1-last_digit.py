#!/usr/bin/python3
import random
Number = random.randint(-10000, 10000)

if Number >= 0:
    Last_Number = int(str(Number)[-1])
else:
    Last_Number = int('-' + str(Number)[-1])

if not Last_Number:
    Mess_End = "and is 0"
elif Last_Number > 6 and Last_Number:
    Mess_End = 'and is less than 6 and not 0'
else:
    Mess_End = 'and is greater than 5'

print("Last digit of {} is {} and is {}".format(Number, Last_Number, Mess_End))
