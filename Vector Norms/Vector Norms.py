import numpy as np

def compute_norm(arr: np.ndarray, norm_type: str) -> float:
    """
    Compute the specified norm of the input array.
    
    Args:
        arr: Input numpy array (1D or 2D)
        norm_type: Type of norm ('l1', 'l2', or 'frobenius')
    
    Returns:
        The computed norm as a float
    """
    result = 0
    if(norm_type == 'l1'):
        result = np.sum(np.abs(arr))
    elif(norm_type == 'l2'):
        if arr.ndim == 1: 
            result = np.sqrt(np.sum(arr ** 2))
        else:
            result = np.linalg.norm(arr,2)
    elif(norm_type == 'frobenius'):
        result = np.sqrt(np.sum(arr ** 2))
    else:
        raise ValueError("Invalid norm_type")
    return result
