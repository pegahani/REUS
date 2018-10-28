import time
from collections import Counter

from libtlda.scl import StructuralCorrespondenceClassifier
from libtlda.suba import SubspaceAlignedClassifier
from libtlda.tca import TransferComponentClassifier

from Evaluation import evaluation
from Sampling_data import sampling_data, train_test_prep
from all_representations import DA_icsi_list, DA_ami_list, all_text_representation
from manage_data import manage_data


import numpy as np

class domain_adptation:

    def __init__(self, text_to_vector_type, corpus_source, n_taxonomy_source, which_percentage_source,
        corpus_target, n_taxonomy_target, classifier_type):

        "variables for the source corpus"
        self.corpus_source = corpus_source
        self.which_percentage_source = which_percentage_source

        if corpus_source == 'icsi':
            self.meeting_group_source = DA_icsi_list
        elif corpus_source == 'ami':
            self.meeting_group_source = DA_ami_list
        self.n_taxonomy_source = n_taxonomy_source
        self.text_represent_source = all_text_representation(self.corpus_source, text_to_vector_type, n_taxonomy_source)
        self.manage_dat_source = manage_data(corpus_source, n_taxonomy_source)
        self.sampling_source = sampling_data(n_taxonomies=n_taxonomy_source, meeting_group=self.meeting_group_source)

        #self.eval = evaluation(self.n_taxonomy_source)

        "variables for the target corpus"

        self.corpus_target = corpus_target
        if corpus_target == 'icsi':
            self.meeting_group_target = DA_icsi_list
        elif corpus_target == 'ami':
            self.meeting_group_target = DA_ami_list
        self.n_taxonomy_target = n_taxonomy_target
        self.text_represent_target = all_text_representation(self.corpus_target, text_to_vector_type, n_taxonomy_target)
        self.manage_dat_target = manage_data(corpus_target, n_taxonomy_target)
        self.sampling_target = sampling_data(n_taxonomies=n_taxonomy_target, meeting_group=self.meeting_group_target)

        self.eval = evaluation(self.n_taxonomy_target)

        self.classifier_type = classifier_type

    def DoA(self, sampling_times, blind_sampling):

        #************************************
        accuracy_majority = {label: 0.0 for label in range(self.n_taxonomy_target)}
        total_accuracy = 0.0
        total_accuracy_weighted = 0.0
        accuracy_majority_list = {label:[] for label in range(self.n_taxonomy_target)}
        total_accuracy_list = []
        total_accuracy_weighted_list = []
        counter_loop = 0
        #************************************

        (all_meeting_input_source, meeting_input_source) = self.text_represent_source.reload_abreviated_labels()
        (all_meeting_input_target, meeting_input_target) = self.text_represent_target.reload_abreviated_labels()

        train_test_data_source = train_test_prep(meeting_input = meeting_input_source, meeting_group=self.meeting_group_source, n_taxonomy=self.n_taxonomy_source,
                                          blind_samling=blind_sampling, sampling=self.sampling_source, text_represent=self.text_represent_source,
                                          which_percentage=self.which_percentage_source)

        train_test_data_target = train_test_prep(meeting_input = meeting_input_target, meeting_group=self.meeting_group_target, n_taxonomy=self.n_taxonomy_target,
                                          blind_samling=True, sampling=self.sampling_target, text_represent=self.text_represent_target,
                                          which_percentage= None)

        train_index_source = [i for i in range(len(self.meeting_group_source))]
        train_index_target = [i for i in range(len(self.meeting_group_target))]

        (train_source, real_label_train_source, test_source, num_sample_source) = train_test_data_source.prepare_train_test_data \
            (train_index=train_index_source, test_index=None, is_smote=False, smote_kind=None, num_sample = None )

        (train_target, real_label_train_target, test_target, num_sample_target) = train_test_data_target.prepare_train_test_data(
            train_index=train_index_target, test_index=None, is_smote=False,
            smote_kind=None, num_sample = num_sample_source)

        X_train_sorce = [self.meeting_group_source[p] for p in train_index_source]
        X_train_target = [self.meeting_group_target[p] for p in train_index_target]


        real_label_target = sum([meeting_input_target[i][1] for i in X_train_target], [])
        predicted_labels_ = [[] for i in real_label_train_target]

        classifier = None
        "learning part"
        start = time.time()
        if self.classifier_type == 'TCA':
            classifier = TransferComponentClassifier()
        elif self.classifier_type == 'SCL':
            classifier = StructuralCorrespondenceClassifier(loss='logistic', l2=1.0, num_pivots=6,
                 num_components=6)

        train_source_array = np.asarray(train_source)
        train_target_array = np.asarray(train_target)

        classifier.fit(train_source_array, real_label_train_source, train_target_array)
        target_predict = classifier.predict(train_target_array)

        finish = time.time()
        print(finish - start)

        counter_loop += 1

        for j in range(len(target_predict)):
            predicted_labels_[j].append(target_predict[j])

        predicted_labels = [max(set(item), key=item.count) for item in predicted_labels_]
        accuracy_majority = dict(Counter(accuracy_majority) + Counter(
            self.eval.get_predicted_error(predicted_labels, real_label_train_target)))

        real_vs_predicted = self.eval.get_predicted_error(predicted_labels, real_label_train_target)
        for i in accuracy_majority_list.keys():
            accuracy_majority_list[i].append(real_vs_predicted[i])

        accuracy = self.eval.get_total_occuracy(predicted_labels, real_label_train_target)
        accuracy_weighted = self.eval.get_weighted_accuracy(predicted_labels, real_label_train_target)
        total_accuracy_weighted_list.append(accuracy_weighted)

        total_accuracy_weighted += accuracy_weighted
        total_accuracy += accuracy
        total_accuracy_list.append(accuracy)

        #print(self.n_taxonomy_target, ";", num_sample_target, ";", counter_loop, ";", accuracy_weighted, ";",
        #      accuracy, ";", accuracy_majority)

        for sampling in range(sampling_times-1):

            (train_source, real_label_train_source, test_source, num_sample_source) = train_test_data_source.prepare_train_test_data\
                (train_index= train_index_source, test_index= None, is_smote=False, smote_kind=None, num_sample= None)

            (train_target, real_label_train_target, test_target, num_sample_target) = train_test_data_target.prepare_train_test_data(
                train_index=train_index_target, test_index=None, is_smote=False,
                smote_kind=None, num_sample = num_sample_source)

            "learning part"
            start = time.time()

            if self.classifier_type == 'TCA':
                classifier = TransferComponentClassifier()
            elif self.classifier_type == 'SCL':
                classifier = StructuralCorrespondenceClassifier(loss='logistic', l2=1.0, num_pivots=6,
                 num_components=6)

            train_source_array = np.asarray(train_source)
            train_target_array = np.asarray(train_target)

            classifier.fit(train_source_array, real_label_train_source, train_target_array)
            target_predict = classifier.predict(train_target_array)

            finish = time.time()
            print(finish - start)

            for j in range(len(target_predict)):
                predicted_labels_[j].append(target_predict[j])


            predicted_labels = [max(set(item), key=item.count) for item in predicted_labels_]
            accuracy_majority = dict(Counter(accuracy_majority) + Counter(self.eval.get_predicted_error(predicted_labels, real_label_train_target)))

            real_vs_predicted = self.eval.get_predicted_error(predicted_labels, real_label_train_target)
            for i in accuracy_majority_list.keys():
                accuracy_majority_list[i].append(real_vs_predicted[i])

            accuracy = self.eval.get_total_occuracy(predicted_labels, real_label_train_target)
            accuracy_weighted = self.eval.get_weighted_accuracy(predicted_labels, real_label_train_target)
            total_accuracy_weighted_list.append(accuracy_weighted)

            total_accuracy_weighted += accuracy_weighted
            total_accuracy += accuracy
            total_accuracy_list.append(accuracy)

            # print(self.n_taxonomy_target, ";", num_sample_target, ";", counter_loop, ";", accuracy_weighted, ";",
            #       accuracy,";", accuracy_majority)


            counter_loop += 1

        accurancy_majority_ = {key: accuracy_majority[key] / counter_loop for key in accuracy_majority.keys()}

        print('*************************************')

        print(self.n_taxonomy_target, ";", num_sample_target, ";", total_accuracy_weighted / counter_loop, ";",
              total_accuracy / counter_loop, ";", accurancy_majority_)

        return self.n_taxonomy_target, ";", num_sample_target, ";", total_accuracy_weighted / counter_loop, ";",\
               total_accuracy / counter_loop, ";", accurancy_majority_
