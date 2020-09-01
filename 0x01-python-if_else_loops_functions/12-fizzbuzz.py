#!/usr/bin/python3
def fizzbuzz():
    for Number in range(1, 101):
        if (not (Number % 3)) and (not (Number % 5)):
            Message = 'FizzBuzz'
        elif  (not (Number % 3)):
            Message = 'Fizz'
        elif (not (Number % 5)):
            Message = 'Buzz'
        else:
            Message = ''
        if Number != 100:
            End = ' '
        print("{}".format(Message if Message else Number), end=End)
