import numpy as np

def phi_transform(data: list[float], degree: int) -> list[list[float]]:
    """
    Perform a Phi Transformation to map input features into a higher-dimensional space by generating polynomial features.

    Args:
        data (list[float]): A list of numerical values to transform.
        degree (int): The degree of the polynomial expansion.

    """
    if(degree < 0):
        return []
    result  = [[1,i] for i in data]
    
    for i in range(len(result)):
        for j in range(degree - 1):
            result[i] = np.append(result[i], result[i][j + 1] * result[i][1])
    
    result = np.array(result)
    return result.tolist()
