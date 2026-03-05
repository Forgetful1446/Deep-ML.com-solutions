  def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    b = [[0 for i in range(len(a))] for i in range(len(a[0]))]

    for i in range(len(a)):
        for j in range(len(a[0])):
            b[j][i] = a[i][j]

    return b

def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    """
    Calculate the mean values of a matrix by row or by column.

    Args:
        matrix (list[list[float]]): A 2D list representing the matrix.
        mode (str): Determines how the mean is calculated.
            - 'row': compute the mean of each row.
            - 'column': compute the mean of each column.

    Returns:
        list[float]: A list containing the mean values according to the selected mode.
            - If mode == 'row', the result length equals the number of rows.
            - If mode == 'column', the result length equals the number of columns.
    """
    if mode == 'column':
        matrix = transpose_matrix(matrix)
    means = [sum(row) / len(row) for row in matrix]
    return means
    
