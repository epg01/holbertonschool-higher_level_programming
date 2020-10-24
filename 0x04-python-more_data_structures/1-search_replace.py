#!/usr/bin/python3
def R(value_default, search, index, replace):
    if search == index:
        return replace
    else:
        return value_default


def search_replace(List, srch, replace):
    return [R(List[i], srch, i + 1, replace) for i in range(len(List))]
