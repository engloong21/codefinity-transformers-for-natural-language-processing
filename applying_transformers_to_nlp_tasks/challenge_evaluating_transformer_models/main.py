# Correct confusion matrix
TP = 4
TN = 3
FP = 1
FN = 2

# Total
total_predictions = TP + TN + FP + FN  # = 10

# Compute and round metrics
accuracy  = round((TP + TN) / total_predictions,  2)  # (4+3)/10 = 0.7
precision = round(TP / (TP + FP),                2)  # 4/(4+1) = 0.8
recall    = round(TP / (TP + FN),                2)  # 4/(4+2) ≈ 0.67
f1_score  = round(2 * (precision * recall) / (precision + recall), 2)  # ≈0.73

print(accuracy, precision, recall, f1_score)