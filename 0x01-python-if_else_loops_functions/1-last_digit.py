#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
Initial_M = "Last digit of"
if number < 0:
    Last_Digit = (number * (-1)) % 10
    Last_Digit *= (-1)
else:
    Last_Digit = number % 10

if Last_Digit is 0:
    Message = "is zero"
    print("{} {} is {} {}".format(Initial_M, number, Last_Digit, Message))
elif Last_Digit > 5:
    Message = "and is greater that 5"
    print("{} {} is {} {}".format(Initial_M, number, Last_Digit, Message))
else:
    Message = "and is less that 6 and not 0"
    print("{} {} is {} {}".format(Initial_M, number, Last_Digit, Message))
