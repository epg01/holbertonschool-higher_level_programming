#!/bin/python3
def P_print_matrix_integer(matrix=[[]]):
    if matrix:
        for idx in range(len(matrix[0])):
            if idx != (len(matrix[0]) - 1):
                print("{:d}".format(matrix[0][idx]), end=' ')
            else:
                print("{:d}".format(matrix[0][idx]))
        return P_print_matrix_integer(matrix[1:])


def print_matrix_integer(matrix=[[]]):
    if [] not in matrix:
        return (P_print_matrix_integer(matrix))
    else:
        print()
