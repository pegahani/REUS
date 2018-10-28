
# LinearSVC(penalty=’l2’, loss=’squared_hinge’, dual=True, tol=0.0001, C=1.0, multi_class=’ovr’, fit_intercept=True,
#           intercept_scaling=1, class_weight=None, verbose=0, random_state=None, max_iter=1000)[source]
import time

from sklearn.svm import LinearSVC
from sklearn.datasets import make_classification
from sklearn.model_selection import LeaveOneOut
from collections import Counter


import numpy as np

from Evaluation import evaluation
from Sampling_data import sampling_data, train_test_prep
from all_representations import all_text_representation, DA_icsi_list, DA_ami_list
from manage_data import manage_data


class supervised:

    def __init__(self, corpus, text_to_vector_type, n_taxonomy, which_percentage):

        self.corpus = corpus
        self.which_percentage = which_percentage

        if corpus == 'icsi':
            self.meeting_group = DA_icsi_list
        elif corpus == 'ami':
            self.meeting_group = DA_ami_list
        self.n_taxonomy = n_taxonomy
        self.text_represent = all_text_representation(self.corpus, text_to_vector_type, n_taxonomy)
        self.manage_dat = manage_data(corpus, n_taxonomy)
        self.sampling = sampling_data(n_taxonomies = n_taxonomy, meeting_group= self.meeting_group)

        self.eval = evaluation(self.n_taxonomy)

    def DA_SVM(self, sampling_times, blind_sampling, max_iter):

        "the real data for clustering are in meet_input variable"
        (all_meeting_input, meeting_input) = self.text_represent.reload_abreviated_labels()

        train_test_data = train_test_prep(meeting_input = meeting_input, meeting_group=self.meeting_group, n_taxonomy=self.n_taxonomy,
                                          blind_samling=blind_sampling, sampling=self.sampling, text_represent=self.text_represent,
                                          which_percentage=self.which_percentage)

        #*******************variables for accuracy calculation**********************************
        accuracy_majority = {label:0.0 for label in range(self.n_taxonomy)}
        total_accuracy = 0.0
        total_accuracy_weighted = 0.0
        accuracy_majority_list = {label:[] for label in range(self.n_taxonomy)}
        total_accuracy_list = []
        total_accuracy_weighted_list = []
        counter_loop = 0
        # *****************************************************

        loo = LeaveOneOut()
        for train_index, test_index in loo.split(self.meeting_group): #kf.split(self.meeting_group):

            X_test = [self.meeting_group[p] for p in test_index]
            real_label_for_test = sum([meeting_input[i][1] for i in X_test], [])
            predicted_labels_ = [[] for i in real_label_for_test]

            for sampling in range(sampling_times):

                (_input_for_train, real_label_train, test_prep, num_sampling) = \
                    train_test_data.prepare_train_test_data(train_index=train_index, test_index=test_index,
                                                            is_smote=False, smote_kind=None, num_sample= None)

                start = time.time()
                svm_train = LinearSVC(random_state=0, tol=1e-5, max_iter = max_iter)
                svm_train.fit(_input_for_train, real_label_train)
                fin = time.time()
                #print("training time", fin - start)

                predicted_ = svm_train.predict(test_prep)
                for j in range(len(predicted_)):
                    predicted_labels_[j].append(predicted_[j])

            predicted_labels = [max(set(item), key = item.count) for item in predicted_labels_]

            real_vs_predicted = self.eval.get_predicted_error(predicted_labels, real_label_for_test)
            accuracy_majority = dict(Counter(accuracy_majority) + Counter(real_vs_predicted))

            for i in accuracy_majority_list.keys():
                accuracy_majority_list[i].append(real_vs_predicted[i])

            accuracy = self.eval.get_total_occuracy(predicted_labels, real_label_for_test)
            accuracy_weighted = self.eval.get_weighted_accuracy(predicted_labels, real_label_for_test)

            total_accuracy_weighted += accuracy_weighted
            total_accuracy_weighted_list.append(accuracy_weighted)

            total_accuracy += accuracy
            total_accuracy_list.append(accuracy)


            counter_loop += 1

        accurancy_majority_ = {key: accuracy_majority[key]/counter_loop for key in accuracy_majority.keys()}
        #print(self.n_taxonomy, ";", num_sampling, ";", counter_loop, ";",total_accuracy_weighted_list, ";", total_accuracy_list, ";", accuracy_majority_list)
        #print("****************************************")
        return  self.n_taxonomy, ";", num_sampling , ";", total_accuracy_weighted / counter_loop, ";", total_accuracy / counter_loop, ";", accurancy_majority_

