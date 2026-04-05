import numpy as np

def rmse(y_true, y_pred):
    if y_pred.shape != y_true.shape or len(y_pred) == 0:
        return -1
    return np.round(np.sqrt(np.mean((y_pred - y_true) ** 2)), 3)
