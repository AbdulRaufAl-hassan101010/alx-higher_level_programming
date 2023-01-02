#!/usr/bin/python3
def matrix_divided(matrix, div):
    new_matrix = []

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if isinstance(div, int) != True and isinstance(div, float) != True:
        raise TypeError("div must be a number")

    if isinstance(matrix, list) is not True:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    for row in matrix:
        new_row = []
        if not isinstance(row, list):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")

        valid_length = len(matrix[0])

        if len(row) is not valid_length:
            raise TypeError(
                "Each row of the matrix must have the same size")

        for column in row:
            if isinstance(column, int) != True and isinstance(column, float) != True:
                raise TypeError(
                    "matrix must be a matrix (list of lists) of integers/floats")
            division_sum = round(column / div, 2)
            new_row.append(division_sum)

        new_matrix.append(new_row)

    return new_matrix


# matrix = [1,2,3]

# print(matrix_divided(matrix, 3))
