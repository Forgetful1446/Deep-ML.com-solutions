def confusion_matrix(datas):
    TP = 0
    FN = 0
    FP = 0
    TN = 0
    
    for data in datas:
        y_true = data[0]
        y_pred = data[1]
        
        if y_pred == 1 and y_true == 1:
            TP += 1
        elif y_pred == 0 and y_true == 0:
            TN += 1
        elif y_pred == 1 and y_true == 0:
            FP += 1
        elif y_pred == 0 and y_true == 1:
            FN += 1
    
    return [[TP, FN], [FP, TN]]
