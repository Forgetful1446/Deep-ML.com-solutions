import numpy as np

def dice_score(y_true, y_pred):
    TP = 0
    FP = 0
    FN = 0
    for i in range(len(y_pred)):
        if(y_pred[i] == y_true[i] == 1):
            TP += 1
        elif(y_pred[i] == 1 and y_true[i] == 0):
            FP += 1
        elif(y_pred[i] == 0 and y_true[i] == 1):
            FN += 1
    if(TP + FP == 0 or TP + FN == 0 or TP == 0):
        return 0
    precision = TP / (TP + FP)
    recall = TP / (TP + FN)
    res = 2 * (precision * recall) / (precision + recall)
    return round(res, 3)
