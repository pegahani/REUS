import numpy as np
from sklearn.metrics import *
import collections


class evaluation:

    def __init__(self, n_clusters):
        self.number_of_clusters = n_clusters


    def get_total_occuracy(self, predicted, real, assigned_labels = None):

        real = np.array(real)
        predicted = np.array(predicted)

        result =  accuracy_score(real, predicted)

        return result

    def get_weighted_accuracy(self, y_pred, y_true):

        y_true = np.array(y_true)
        y_pred = np.array(y_pred)

        w = np.ones(len(y_true))
        for idx, i in enumerate(np.bincount(y_true)):
            w[y_true == idx] *= (i / float(len(y_true)))

        result = accuracy_score(y_true, y_pred, sample_weight=w)
        return result

    def get_predicted_error(self, predicted, real, assigned_labels = None):

        #predicted_to_real_assigned = self.predicted_to_real_assigned(predicted, assigned_labels)
        predicted_to_real_assigned = predicted

        accurancy_per_label = {key:0.0 for key in range(self.number_of_clusters)}
        total_real_per_label = collections.Counter(real)

        for label in range(self.number_of_clusters):
            count = 0
            for j in range(len(real)):
                if real[j] == label:
                    if predicted_to_real_assigned[j] == real[j]:
                        count += 1
            if total_real_per_label[label] != 0:
                accurancy_per_label[label] = float(count/total_real_per_label[label])
            else:
                accurancy_per_label[label] = 0.0

        return accurancy_per_label
        #return np.count_nonzero(predicted_to_real_assigned == real)/len(predicted_to_real_assigned)

    def predicted_to_real_assigned(self, predicted, assigned_labels):
        return [assigned_labels[j] for j in predicted]

    def prec_rec_fmeasure(self, predicted, real, assigned_labels, type):
        predicted_labels = self.predicted_to_real_assigned(predicted, assigned_labels)

        return list(precision_recall_fscore_support(real, predicted_labels,  average = type)[0:-1])
