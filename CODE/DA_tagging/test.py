import numpy as np
from sklearn.metrics import *


def get_weighted_accuracy(y_pred, y_true):
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)

    w = np.ones(len(y_true))
    for idx, i in enumerate(np.bincount(y_true)):
        print(idx, i, i / float(len(y_true)))
        w[y_true == idx] *= (i / float(len(y_true)))

    print(w)

    result = accuracy_score(y_true, y_pred, sample_weight=w)
    return result

y_pred = [1, 2, 0, 1, 2, 0, 2, 0]
y_true = [1, 0, 2, 1, 2, 1, 1, 2]

print(get_weighted_accuracy(y_pred, y_true))