def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    
    b = [[0 for i in range(len(a))] for i in range(len(a[0]))]

    for i in range(len(a)):
        for j in range(len(a[0])):
            b[j][i] = a[i][j]

    return b
