#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
    Last_Digit = (number * (-1)) % 10
    Last_Digit *= (-1)
else:
    Last_Digit = number % 10

if Last_Digit is 0:
    print("Last digit of {} is {} and is 0".format(number, Last_Digit))
elif Last_Digit > 5:
    Message = "and is greater that 5"
    print("Last digit of {} is {} {}".format(number, Last_Digit, Message))
else:
    Message = "and is less that 6 and not 0"
    print("Last digit of {} is {} {}".format(number, Last_Digit, Message))
