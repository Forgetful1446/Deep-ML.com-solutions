def to_categorical(x, n_col=None):
	if n_col is None:
		n_col = max(x) + 1
	
	if max(x) >= n_col:
		raise ValueError("n_col must be greater than max value in x")
	
	result = [[0. for _ in range(n_col)] for _ in range(len(x))]
	
	for i in range(len(x)):
		result[i][x[i]] = 1.0
	
	return result
