import numpy as np

def to_categorical(x, n_col=None):
	if n_col is not None:
		result = [[0. for _ in range(n_col)] for _ in range(len(x))]
	else:
		result = [[0. for _ in range(max(x) + 1)] for _ in range(len(x))]
	
	for i in range(len(x)):
		result[i][x[i]] = 1.0
	return result
