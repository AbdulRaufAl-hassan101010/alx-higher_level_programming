#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for row in matrix:
            column_length = len(row)
            for i in range(column_length):
                if column_length - 1 == i:
                    print("{:d}".format(row[i]), end='')
                else:
                    print("{:d}".format(row[i]), end=' ')
            print()
