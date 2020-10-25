#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is not None and a_dictionary:
        score = sorted(list((a_dictionary.values())))
        for keys in a_dictionary.keys():
            if a_dictionary.get(keys) == score[-1]:
                return keys
