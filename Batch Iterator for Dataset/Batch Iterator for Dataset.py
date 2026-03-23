import numpy as np

def batch_iterator(X, y=None, batch_size=64):
	# Your code here
	n_sample = len(X)
	result = []

	for i in range(0, n_sample, batch_size):
		X_batch = X[i:i+batch_size]

		if y is not None:
			y_batch = y[i:i+batch_size]
			result.append([X_batch,y_batch])
			continue
		result.append(X_batch)
	
	return result
			
