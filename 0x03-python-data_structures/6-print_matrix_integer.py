#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is not None:
        if matrix == [[]]:
            print()
        if len(matrix) == 1:
            Counter = int()
            for value in matrix[0]:
                print("{:d}".format(value), end='')

                Counter += 1
                if Counter != len(matrix[0]):
                    print("{0:s}".format(' '), end='')
                else:
                    print()
        else:
            Counter = int()
            for value in matrix[0]:
                print("{:d}".format(value), end='')

                Counter += 1
                if Counter != len(matrix[0]):
                    print("{0:s}".format(' '), end='')
                else:
                    print()
            return print_matrix_integer(matrix[1:])
