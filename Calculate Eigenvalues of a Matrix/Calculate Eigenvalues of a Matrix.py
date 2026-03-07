import numpy as np

def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:

    a = matrix[0][0]
    b = matrix[0][1]
    c = matrix[1][0]
    d = matrix[1][1]
    
    trace = a + d
    det = a * d - b * c

    delta = (- trace) ** 2 - 4 * det

    lambda1 = (trace + np.sqrt(delta)) / 2
    lambda2 = (trace - np.sqrt(delta)) / 2
    
    return [lambda1, lambda2]
