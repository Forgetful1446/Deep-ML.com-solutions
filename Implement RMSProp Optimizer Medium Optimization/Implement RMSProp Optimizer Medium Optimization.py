import numpy as np
def rmsprop_update(params: list[float], grads: list[float], cache: list[float], lr: float = 0.01, beta: float = 0.9, epsilon: float = 1e-8) -> tuple[list[float], list[float]]:
    """
    Perform RMSProp optimization update.
    
    Args:
        params: List of parameter values
        grads: List of gradients for each parameter
        cache: List of cache values (moving average of squared gradients)
        lr: Learning rate
        beta: Decay rate for moving average
        epsilon: Small constant for numerical stability
    
    Returns:
        Tuple of (updated_params, updated_cache)
    """
    params = np.array(params)
    grads = np.array(grads)
    cache = np.array(cache)
    
    v_new = beta * cache +  (1 -  beta)* grads ** 2
    for i in range(len(params)):
        params[i] = params[i] - (lr * grads[i]) / (np.sqrt(v_new[i]) + epsilon)
        
    return (params.tolist(), v_new.tolist())
