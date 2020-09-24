#!/usr/bin/python3
import random
Number = random.randint(-10, 10)
Message = ""
if Number is 0:
    Message = "is zero"
elif Number > 0:
    Message = "is positive"
else:
    Message = "is negative"
print("{Number:d} {Message:s}".format(Number=Number, Message=Message))
