#!/usr/bin/python3
import random
Number = random.randint(-10, 10)
if Number is 0:
    Message = "is zero"
elif Number > 0:
    Message = "is positive"
else:
    Message = "is negative"
print("{:d} {:s}".format(Number, Message))
