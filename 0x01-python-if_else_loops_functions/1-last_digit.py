#!/usr/bin/python3
import random
Number = random.randint(-10000, 10000)
Last_Number = str(Number)[len(str(Number)) - 1]
print("Last digit of ", Number, " is ", Last_Number, end=' ')
Last_Number = int(Last_Number)
if Last_Number > 5:
    print("{}".format("greater than 5"))
elif Last_Number < 6 and not Number:
    print("{}".format("less than 6 and not 0"))
else:
    print("{}".format("and is 0"))
