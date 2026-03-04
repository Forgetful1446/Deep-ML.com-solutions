def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
    """
    Reshape a 2D matrix into a new shape if the total number of elements matches.

    Parameters:
    a (list[list[int | float]]): Original 2D matrix.
    new_shape (tuple[int, int]): Target shape in the form (rows, cols).

    Returns:
    list[list[int | float]]: Reshaped matrix with dimensions specified by new_shape.
    Returns an empty list if reshaping is not possible.
    """
    if (len(a) * len(a[0]) != new_shape[0] * new_shape[1]):
        return [] 
    
    temp = []
    reshaped_matrix = [[0 for _ in range(new_shape[1])] for _ in range(new_shape[0])]
    
    for i in range(len(a)):
        for j in range(len(a[0])):
            temp.append(a[i][j])
    
    idx = 0

    for i in range(len(reshaped_matrix)):
        for j in range(len(reshaped_matrix[0])):
            reshaped_matrix[i][j] = temp[idx]
            idx += 1
    
    return reshaped_matrix
