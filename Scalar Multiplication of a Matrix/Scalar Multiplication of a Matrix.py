def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
    result  = matrix

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            result[row][col] = scalar * matrix[row][col]
    return result
