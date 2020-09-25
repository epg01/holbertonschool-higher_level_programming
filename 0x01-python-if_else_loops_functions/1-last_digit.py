#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

Message_Initial = "Last digit of"
if number < 0:
    Last_Digit = (number * (-1)) % 10
    Last_Digit *= (-1)
else:
    Last_Digit = number % 10

if Last_Digit is 0:
    Message = "and is 0"
elif Last_Digit > 5:
    Message = "and is greater that 5"
else:
    Message = "and is less that 6 and not 0"

print("{:s} {Number:d} ".format(Message_Initial, Number=number), end='')
print("is {:d} {Message:s}".format(Last_Digit, Message=Message))
