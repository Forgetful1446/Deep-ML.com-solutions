import numpy as np

def accuracy_score(y_true, y_pred):
	# Your code here
	sum = 0
	for i in range(len(y_true)):
		if(y_true[i] == y_pred[i]):
			sum+= 1
	return sum / len(y_pred)
