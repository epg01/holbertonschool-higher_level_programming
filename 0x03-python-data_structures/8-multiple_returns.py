#!/bin/usr/python3
def multiple_returns(sentence):
    if sentence is None:
        return 0, None
    elif not len(sentence):
        return 0, None
    else:
        return len(sentence), sentence[0]
