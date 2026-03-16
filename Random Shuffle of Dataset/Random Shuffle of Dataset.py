import numpy as np

def shuffle_data(X, y, seed=None):
    np.random.seed(seed)

    idx = np.random.permutation(len(X))

    X = X[idx]
    y = y[idx]

    return X, y
