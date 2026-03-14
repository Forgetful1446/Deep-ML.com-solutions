import numpy as np

def feature_scaling(data: np.ndarray):

    standardized_data = np.round((data - np.mean(data, axis=0)) / np.std(data, axis=0),4)

    normalized_data = np.round((data - data.min(axis=0)) /(data.max(axis=0) - data.min(axis=0)),4)

    return standardized_data.tolist(), normalized_data.tolist()
