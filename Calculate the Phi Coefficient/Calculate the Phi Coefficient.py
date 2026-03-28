import math

def phi_corr(x: list[int], y: list[int]) -> float:
    if len(x) != len(y):
        raise ValueError("x and y must have same length")
    
    x00 = x01 = x10 = x11 = 0
    
    for i in range(len(x)):
        if x[i] == 0 and y[i] == 0:
            x00 += 1
        elif x[i] == 0 and y[i] == 1:
            x01 += 1
        elif x[i] == 1 and y[i] == 0:
            x10 += 1
        else:
            x11 += 1
    
    denominator = (x00 + x01)*(x10 + x11)*(x00 + x10)*(x01 + x11)
    
    if denominator == 0:
        return 0.0
    
    val = ((x00 * x11) - (x01 * x10)) / math.sqrt(denominator)
    
    return round(val, 4)
