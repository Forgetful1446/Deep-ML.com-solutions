import numpy as np

def find_mean(data):
    mean = 0 
    for val in data:
        mean += val
    if len(data) > 0:
        mean /= len(data)
    return mean

def find_median(data):
    data_sorted = data.copy()
    data_sorted.sort()
    if(len(data) % 2 == 0):
        return (data_sorted[int (len(data) / 2) - 1] + data_sorted[int(len(data) / 2)]) / 2
    else:
        return (data_sorted[int (len(data) / 2)])
    
def find_mode(data):
    counts = {}
    for val in data:
        counts[val] = counts.get(val, 0) + 1 
        
    max_freq = max(counts.values())
    
    modes = [k for k, v in counts.items() if v == max_freq]
    
    return min(modes)

def find_variance(data):
    mean = find_mean(data)
    variance = 0
    for val in data:
        variance += (val - mean) ** 2
    return variance / len(data)

def find_variance_standard(data):
    return find_variance(data) ** 0.5

def find_25th(data):
    data.sort()
    return data[int(len(data) / 4)]

def find_75th(data):
    data.sort()
    return data[int(len(data) * 3 / 4)]

def find_interquartile_range(data):
    return find_75th(data) - find_25th(data)

def descriptive_statistics(data: list | np.ndarray) -> dict:
    """
    Calculate various descriptive statistics metrics for a given dataset.
    
    Args:
        data: List or numpy array of numerical values
    
    Returns:
        Dictionary containing mean, median, mode, variance, standard deviation,
        percentiles (25th, 50th, 75th), and interquartile range (IQR)
    """
    result = {
        "mean" : find_mean(data),
        "median" : find_median(data),
        "mode" : find_mode(data),
        "variance": find_variance(data),
        "standard_deviation": find_variance_standard(data),
        "25th_percentile": find_25th(data),
        "50th_percentile": find_median(data),
        "75th_percentile": find_75th(data),
        "interquartile_range":find_interquartile_range(data)
    }
        
    
    return result
