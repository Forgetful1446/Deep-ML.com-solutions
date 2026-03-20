import numpy as np

def kernel_function(x1, x2):
	# Your code here
	sum = 0
	for i in range(len(x1)):
		sum += x1[i] * x2[i]
	return sum
	pass
