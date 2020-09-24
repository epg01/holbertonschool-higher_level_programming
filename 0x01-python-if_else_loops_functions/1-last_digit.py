#!/usr/bin/python3
import random
Number = random.randint(-10000, 10000)

Message_Initial = "Last digit of"
if Number < 0:
    Last_Digit = (Number * (-1)) % 10
    Last_Digit *= (-1)
else:
    Last_Digit = Number % 10

if Last_Digit is 0:
    Message = "and is 0"
elif Last_Digit > 5:
    Message = "and is greater that 5"
else:
    Message = "and is less that 6 and not 0"

print("{:s} {Number:d} ".format(Message_Initial, Number=Number), end='')
print("is {:d} {Message:s}".format(Last_Digit, Message=Message))
