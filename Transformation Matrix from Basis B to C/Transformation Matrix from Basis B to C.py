def transform_basis(B, C):
    B = np.array(B)
    C = np.array(C)

    if np.linalg.det(C) == 0:
        raise ValueError("C is not invertible")

    return np.round(np.linalg.inv(C) @ B, 4)
