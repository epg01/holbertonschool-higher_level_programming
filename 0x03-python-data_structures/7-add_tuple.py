#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    LenA = len(tuple_a)
    LenB = len(tuple_b)
    if not LenA and LenB >= 2:
        return tuple_b
    elif not LenB and LenA >= 2:
        return tuple_a
    elif LenA >= 2 and LenB >=2:
        return tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1]
    elif LenA < 2 and LenB >= 2:
        return tuple_a[0] + tuple_b[0], tuple_b[1]
    elif LenA >= 2 and LenB < 2:
        return tuple_a[0] + tuple_b[0], tuple_a[1]
