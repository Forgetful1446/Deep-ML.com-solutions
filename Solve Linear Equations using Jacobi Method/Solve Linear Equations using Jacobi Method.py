import numpy as np

def solve_jacobi(A: np.ndarray, b: np.ndarray, n: int) -> list:
    size = len(b)
    
    x = np.zeros(size)
    
    for step in range(n):
        x_new = np.zeros(size)
        
        for i in range(size):
            sum_ = 0
            
            for j in range(size):
                if j != i:
                    sum_ += A[i][j] * x[j]
            
            x_new[i] = (b[i] - sum_) / A[i][i]
        
        x = x_new
    
    return x
