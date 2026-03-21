def calculate_brightness(img):
	if(len(img) == 0):
		return -1

	matrixSum = 0

	rowCheck = len(img[0])
	for row in img:
		if len(row) != rowCheck:
			return -1
		for i in row:
			if i < 0 or i > 255:
				return -1
			matrixSum += i
	
	return matrixSum/(len(img) * len(img[0]))
