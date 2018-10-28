# coding: utf-8

#existed proportion labels for number of DAs in AMI
# total = 18,908
#Counter({0: 82, 1: 11359, 2: 4229, 3: 3131, 4: 71, 5: 36})
#----------------------------------------------
#existed proportion labels for number of DAs in ICSI
# total = 142,544
#Counter({0: 23444, 1: 65914,2: 6135, 3: 16840,, 4: 4029, 5: 17900, -1: 8282})

#----------------------------------------------

#4926 vector size for lexical presentation
import collections
import os
import os.path
import random
import time
import numpy as np
from collections import Counter

from imblearn.over_sampling import SMOTE

import sys
from sklearn.metrics import pairwise_distances_argmin_min

from all_representations import DA_ami_list, DA_icsi_list, all_text_representation

"""if any problem in executing the code, remove CODE.DA_tagging. from the begining of the two bellow imports"""
from Sampling_data import sampling_data,train_test_prep
from text_to_vector import *
from Evaluation import evaluation


from sklearn.cluster import KMeans
from sklearn.cluster import AgglomerativeClustering
from sklearn.model_selection import LeaveOneOut, KFold
from sklearn import datasets, mixture

from itertools import groupby as g
from sklearn.metrics import precision_recall_fscore_support
from sklearn.decomposition import TruncatedSVD


#-------------some variables for AMI---------------------------

# All scenario based manual corpus in AMI
suffixes_manual_corpus = [i+1 for i in range(188) ] + [str(51)+'b']
for j in [9, 24, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 149, 152, 153, 154, 155]:
        suffixes_manual_corpus.remove(j)

# All scenario based extractive summaries in AMI
suffixes_extractive_sum = [i+1 for i in range(151)]
for j in [9, 24, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 150]:
    suffixes_extractive_sum.remove(j)

random.seed(314159)
re_arrange_labels = {1: 0, 2: 1, 3: 2, 0: 10, 4: 11}

class cluster:

    def __init__(self, corpus, method, text_to_vector_type, with_label, n_taxonomy, number_of_clusters, which_percentage):
        """

        :param corpus: name of the corpus. At this level, we have two options: AMI and ICSI
        :param method: clustering method
        :param text_to_vector_type: text representation method
        :param with_label: keep real labels of DAs or not
        :param n_taxonomy:
        :param number_of_clusters:
        :param which_percentage:
        """

        self.corpus = corpus
        self.w2vec = text_to_vector()

        if corpus == 'icsi':
            self.meeting_group = DA_icsi_list
        elif corpus == 'ami':
            self.meeting_group = DA_ami_list

        #self.meeting_group = meeting_group
        self.method = method
        self.text_to_vector_type = text_to_vector_type
        self.with_label = with_label
        self.n_taxonomy = n_taxonomy
        self.number_of_clusters = number_of_clusters
        self.which_percentage = which_percentage

        self.sampling = sampling_data(n_taxonomies = n_taxonomy, meeting_group= self.meeting_group)
        self.eval = evaluation(self.number_of_clusters)
        self.text_represent = all_text_representation(self.corpus, self.text_to_vector_type, self.n_taxonomy, with_label= True)

        self.svd = TruncatedSVD(n_components=50, n_iter=5, random_state= None)

    # it recieves a list and gives back the most repeated element in the list.
    def most_common(self, lst):
        return max(set(lst), key=lst.count)

    """it gets label of the closest point to centroid of each clster """
    def get_menoids(self, clustering, Data):
        closest, _ = pairwise_distances_argmin_min(clustering.cluster_centers_, Data)
        return closest

    def modify_labels(self, lables):

        new_labels = {key:[] for key in lables.keys()}
        average_labels = []
        if(self.with_label):
            for k in lables.keys():
                label_equiv = self.most_common(lables[k])

                try:
                    assert label_equiv not in average_labels
                except AssertionError:
                    sys.exit('ERROR: the clustering should have a problem. Having several clusters with the same label is not possible.')
                    #print('the clustering should have a problem. Having several clusters with the same label is not possible.')

                average_labels.append(label_equiv)
                new_labels[label_equiv] = lables[k]

            return new_labels

    # def get_dictionary(self):
    #
    #     if self.with_label:
    #         file_name = [adress_resume_ami + 'meet_' + str(i) + '.txt' for i in self.meeting_group]
    #     else:
    #         file_name = [adress_corpus_ami + 'meet_' + str(i) + '.txt' for i in self.meeting_group]
    #
    #     #load_dictionary(file_name, self.with_label)
    #     return reload_dictionary()

    def predict_Agglomerative(self, centers_, test_prep):
        closest, _ = pairwise_distances_argmin_min(test_prep, centers_)
        return closest

    def assign_labels_centroid(self, kmeans_train, _input_for_train_clustering, real_label_train_clustering ):

        closest = self.get_menoids(kmeans_train, _input_for_train_clustering)
        vect = [real_label_train_clustering[i] for i in closest]
        return {i:vect[i] for i in range(len(vect))}

    def assign_majority(self, labels_real):
        return {key:self.most_common(labels_real[key]) for key in labels_real.keys()}

    def print_proportion(self, pred):

        text = ''
        for i in range(self.number_of_clusters):
            text = text + str(pred[i]) + ';'

        return text

    def get_predicted_proportion(self, real, pred):
        predicted_prop = Counter(pred)
        return predicted_prop

    def simpler_sampling_data_for_clustering(self, data_, which_percent):

        samples = []

        sum_ = sum(len(value) for value in data_.values())
        #print(sum_)
        percentage = {key:float("{0:.3f}".format(len(data_[key])/sum_)) for key in data_.keys()}

        #print("percentage", percentage)

        number_sample = round(which_percent * sum_)

        for key in data_:
            if percentage[key] >= which_percent:
                samples = samples + random.sample(data_[key], number_sample)
            else:
                samples = samples + data_[key]

        return(samples, number_sample)

    def predict_with_std(self, test_prep, centers_std):

        #print('************')
        #print(centers_std)
        test = test_prep[1]

        length = len(centers_std[0][0])
        output = [None]*len(test_prep)


        for key in centers_std.keys():
            print(key)
            check = True
            for i in range(length):
                if not( centers_std[key][0][i] <= test[i] and test[i] <= centers_std[key][1][i]):
                    print('False')
                    check = False
            if check == True:
                print('----------------------------')
                print(key)


        pass

    def clean(self, meeting_input_samples):
        meeting = dict()
        print(meeting_input_samples)
        for i in meeting_input_samples.keys():
            if meeting_input_samples[i] == ([],[]):
                pass
            else:
                meeting[i] = meeting_input_samples[i]
        print(meeting)
        return meeting

    def prepare_data_real_labels(self, meeting_input_test_):

        test_prep = []
        real_label_for_test_clustering = []
        for key in meeting_input_test_.keys():
            test_prep = test_prep +  meeting_input_test_[key]
            real_label_for_test_clustering = real_label_for_test_clustering + [key]*len(meeting_input_test_[key])

        return(test_prep, real_label_for_test_clustering)

    def DA_clustering(self, sampling_times, is_smote, smote_kind, blind_sampling):
        """
        :param sampling_times:
        :param is_smote:
        :param smote_kind:
        :param blind_samling: if True, the method samples data without taing their imblance into account.
        in the best case clustering, this variable is "False"
        :return:
        """

        "the real data for clustering are in meet_input variable"
        (all_meeting_input, meeting_input) = self.text_represent.reload_abreviated_labels()

        train_test_data = train_test_prep(meeting_input = meeting_input, meeting_group=self.meeting_group, n_taxonomy=self.n_taxonomy,
                                          blind_samling=blind_sampling, sampling=self.sampling, text_represent=self.text_represent,
                                          which_percentage=self.which_percentage)

        #*******************variables for accuracy calculation**********************************
        accuracy_majority = {label:0.0 for label in range(self.number_of_clusters)}
        total_accuracy = 0.0
        total_accuracy_weighted = 0.0
        accuracy_majority_list = {label:[] for label in range(self.number_of_clusters)}
        total_accuracy_list = []
        total_accuracy_weighted_list = []
        counter_loop = 0
        # *****************************************************

        loo = LeaveOneOut()
        #kf = KFold(n_splits=50)
        for train_index, test_index in loo.split(self.meeting_group): #kf.split(self.meeting_group):

            X_test = [self.meeting_group[p] for p in test_index]
            real_label_for_test_clustering = sum([meeting_input[i][1] for i in X_test], [])
            predicted_labels_ = [[] for i in real_label_for_test_clustering]

            for sampling in range(sampling_times):

                (_input_for_train_clustering, real_label_train_clustering, test_prep, num_sampling) = \
                    train_test_data.prepare_train_test_data(train_index = train_index, test_index = test_index, is_smote = is_smote, smote_kind= smote_kind)

                # some variables for the clustering results
                labels = {i: [] for i in range(self.number_of_clusters)}
                labels_real = {i: [] for i in range(self.number_of_clusters)}
                values_for_clusters = {i: [] for i in range(self.number_of_clusters)}

                # if selected clustering method is k-means
                if self.method == 'kmeans':

                    if self.text_to_vector_type == 'lexical':
                        """reduce space size using PCA (principal component analysis)"""
                        _input_for_train_clustering = self.svd.transform(_input_for_train_clustering)

                    start = time.time()

                    kmeans_train = KMeans(n_clusters=self.number_of_clusters, random_state=0).fit(_input_for_train_clustering)
                    k_mean_labels = kmeans_train.labels_
                    fin = time.time()
                    #print('training time', fin-start)

                    length_ = len(k_mean_labels)
                    for k in range(length_):
                        labels[k_mean_labels[k]].append(k)

                    for i in range(self.number_of_clusters):
                        for j in labels[i]:
                            labels_real[i].append(real_label_train_clustering[j])

                    # dominated labels in each cluster
                    assigned_labels_to_clusters_majority_labels = self.assign_majority(labels_real)

                    predicted_ = self.eval.predicted_to_real_assigned(kmeans_train.predict(test_prep), assigned_labels_to_clusters_majority_labels)
                    for j in range(len(predicted_)):
                        predicted_labels_[j].append(predicted_[j])

                # if selected clustering method is hierarchical
                elif self.method == 'Agglomerative':
                    agglomerative_train = AgglomerativeClustering(n_clusters=self.number_of_clusters, affinity='euclidean', linkage ='complete')

                    if self.text_to_vector_type == 'lexical':
                        start = time.time()
                        """reduce space size using PCA (principal component analysis)"""
                        _input_for_train_clustering = self.svd.transform(_input_for_train_clustering)
                        fin = time.time()
                        #print("transform lexical", fin - start)

                    start = time.time()
                    agglomerative_train.fit(_input_for_train_clustering)
                    fin = time.time()
                    #print("training time", fin - start)

                    Agglomerative_labels = agglomerative_train.labels_

                    length_ = len(Agglomerative_labels)
                    for k in range(length_):
                        labels[Agglomerative_labels[k]].append(k)

                    for i in range(self.number_of_clusters):
                        for j in labels[i]:
                            labels_real[i].append(real_label_train_clustering[j])
                            values_for_clusters[i].append(_input_for_train_clustering[j])

                    #dominated labels in each cluster
                    assigned_labels_to_clusters_majority_labels = self.assign_majority(labels_real)

                    centers_ = [] #{i:None for i in range(self.number_of_clusters)}
                    for k in values_for_clusters.keys():
                        mean_ = np.mean(values_for_clusters[k], axis = 0)
                        centers_.append(mean_)

                    predicted_ = self.eval.predicted_to_real_assigned(self.predict_Agglomerative(centers_, test_prep), assigned_labels_to_clusters_majority_labels)
                    for j in range(len(predicted_)):
                        predicted_labels_[j].append(predicted_[j])

                if self.method == 'EM':

                    if self.text_to_vector_type == 'lexical':
                        """reduce space size using PCA (principal component analysis)"""
                        _input_for_train_clustering = self.svd.transform(_input_for_train_clustering)

                    em_train = mixture.GaussianMixture(n_components =self.number_of_clusters, covariance_type="full", tol=0.001).fit(_input_for_train_clustering)
                    em_labels = em_train.predict(_input_for_train_clustering)

                    length_ = len(em_labels)
                    for k in range(length_):
                        labels[em_labels[k]].append(k)

                    for i in range(self.number_of_clusters):
                        for j in labels[i]:
                            labels_real[i].append(real_label_train_clustering[j])
                            values_for_clusters[i].append(_input_for_train_clustering[j])

                    #dominated labels in each cluster
                    assigned_labels_to_clusters_majority_labels = self.assign_majority(labels_real)

                    predicted_ = self.eval.predicted_to_real_assigned(em_train.predict(test_prep), assigned_labels_to_clusters_majority_labels)
                    for j in range(len(predicted_)):
                        predicted_labels_[j].append(predicted_[j])

            predicted_labels = [max(set(item), key = item.count) for item in predicted_labels_]

            real_vs_predicted = self.eval.get_predicted_error(predicted_labels, real_label_for_test_clustering)
            accuracy_majority = dict(Counter(accuracy_majority) + Counter(real_vs_predicted))

            for i in accuracy_majority_list.keys():
                accuracy_majority_list[i].append(real_vs_predicted[i])

            accuracy = self.eval.get_total_occuracy(predicted_labels, real_label_for_test_clustering)
            accuracy_weighted = self.eval.get_weighted_accuracy(predicted_labels, real_label_for_test_clustering)

            total_accuracy_weighted += accuracy_weighted
            total_accuracy_weighted_list.append(accuracy_weighted)
            #print("weighted accuracy", total_accuracy_weighted)
            total_accuracy += accuracy
            total_accuracy_list.append(accuracy)

            counter_loop += 1

        accurancy_majority_ = {key: accuracy_majority[key]/counter_loop for key in accuracy_majority.keys()}
        #print(self.number_of_clusters, ";", num_sampling, ";", counter_loop, ";",total_accuracy_weighted_list, ";", total_accuracy_list, ";", accuracy_majority_list)
        #print("****************************************")
        return  self.number_of_clusters, ";", num_sampling, ";", total_accuracy_weighted / counter_loop, ";", total_accuracy / counter_loop, ";", accurancy_majority_

    def minor_average_sampling(self, sampling_times):
        (all_meeting_input,meeting_input) = self.text_represent.reload_abreviated_labels()
        #print("first", sum(len(value[1]) for value in meeting_infput.values()))

        (_train, _test) = self.extract_train_test_minority(meeting_input)

        meeting_input_train_ = {key: _train[key][0] for key in _train.keys()}
        meeting_input_test_ = {key: _test[key][0] for key in _test.keys()}

        if self.text_to_vector_type == 'lexical':
            _input_for_clustering = []

            for key in meeting_input_train_:
                _input_for_clustering = _input_for_clustering + meeting_input_train_[key]

            for key in meeting_input_test_:
                _input_for_clustering = _input_for_clustering + meeting_input_test_[key]

            self.svd.fit(_input_for_clustering)

        if self.text_to_vector_type == 'lexical':
            """reduce space size using PCA (principal component analysis)"""
            meeting_input_test_ = {key: (self.svd.transform(meeting_input_test_[key])).tolist() for key in meeting_input_test_.keys() }
            meeting_input_train_ = {key: (self.svd.transform(meeting_input_train_[key])).tolist() for key in meeting_input_train_.keys() }

        (test_prep, real_label_for_test_clustering) = self.prepare_data_real_labels(meeting_input_test_)
        (train_prep, real_label_for_train_clustering) = self.prepare_data_real_labels(meeting_input_train_)

        predicted_labels_test = [[] for i in real_label_for_test_clustering]
        predicted_labels_train = [[] for i in real_label_for_train_clustering]
        _labels_test = [[] for i in real_label_for_test_clustering]
        _labels_train = [[] for i in real_label_for_train_clustering]

        for sampling in range(sampling_times):

            (_input_for_train_clustering, number_samples) = self.simpler_sampling_data_for_clustering(meeting_input_train_, self.which_percentage)

            real_label_train_clustering = []
            for label in [0,1,2]:
                real_label_train_clustering = real_label_train_clustering + [label]*number_samples


            # some variables for the clustering results
            labels = {i: [] for i in range(self.number_of_clusters)}
            labels_real = {i: [] for i in range(self.number_of_clusters)}
            values_for_clusters = {i: [] for i in range(self.number_of_clusters)}

            # if selected clustering method is k-means
            if self.method == 'kmeans':

                kmeans_train = KMeans(n_clusters=self.number_of_clusters, random_state=0).fit(_input_for_train_clustering)
                k_mean_labels = kmeans_train.labels_

                length_ = len(k_mean_labels)
                for k in range(length_):
                    labels[k_mean_labels[k]].append(k)

                for i in range(self.number_of_clusters):
                    for j in labels[i]:
                        labels_real[i].append(real_label_train_clustering[j])

                # dominated labels in each cluster
                assigned_labels_to_clusters_majority_labels = self.assign_majority(labels_real)

                test_labels = kmeans_train.predict(test_prep)
                predicted_test = self.eval.predicted_to_real_assigned(test_labels, assigned_labels_to_clusters_majority_labels)
                for j in range(len(predicted_test)):
                    predicted_labels_test[j].append(predicted_test[j])
                    _labels_test[j].append(test_labels[j])


                trained_labels = kmeans_train.predict(train_prep)
                predicted_train = self.eval.predicted_to_real_assigned(trained_labels, assigned_labels_to_clusters_majority_labels)
                for j in range(len(predicted_train)):
                    predicted_labels_train[j].append(predicted_train[j])
                    _labels_train[j].append(trained_labels[j])

            # if selected clustering method is hierarchical
            elif self.method == 'Agglomerative':
                agglomerative_train = AgglomerativeClustering(n_clusters=self.number_of_clusters, affinity='euclidean', linkage='complete')

                agglomerative_train.fit(_input_for_train_clustering)
                Agglomerative_labels = agglomerative_train.labels_

                length_ = len(Agglomerative_labels)
                for k in range(length_):
                    labels[Agglomerative_labels[k]].append(k)

                for i in range(self.number_of_clusters):
                    for j in labels[i]:
                        labels_real[i].append(real_label_train_clustering[j])
                        values_for_clusters[i].append(_input_for_train_clustering[j])

                # dominated labels in each cluster
                assigned_labels_to_clusters_majority_labels = self.assign_majority(labels_real)

                centers_ = []  # {i:None for i in range(self.number_of_clusters)}
                for k in values_for_clusters.keys():
                    mean_ = np.mean(values_for_clusters[k], axis=0)
                    centers_.append(mean_)


                test_labels = self.predict_Agglomerative(centers_, test_prep)
                predicted_test = self.eval.predicted_to_real_assigned(test_labels,
                                                             assigned_labels_to_clusters_majority_labels)
                for j in range(len(predicted_test)):
                    predicted_labels_test[j].append(predicted_test[j])
                    _labels_test[j].append(test_labels[j])


                trained_labels = self.predict_Agglomerative(centers_, train_prep)
                predicted_train = self.eval.predicted_to_real_assigned(trained_labels, assigned_labels_to_clusters_majority_labels)
                for j in range(len(predicted_train)):
                    predicted_labels_train[j].append(predicted_train[j])
                    _labels_train[j].append(trained_labels[j])

            if self.method == 'EM':

                em_train = mixture.GaussianMixture(n_components=self.number_of_clusters, covariance_type="full",
                                                   tol=0.001).fit(_input_for_train_clustering)
                em_labels = em_train.predict(_input_for_train_clustering)

                length_ = len(em_labels)
                for k in range(length_):
                    labels[em_labels[k]].append(k)

                for i in range(self.number_of_clusters):
                    for j in labels[i]:
                        labels_real[i].append(real_label_train_clustering[j])
                        #values_for_clusters[i].append(_input_for_train_clustering[j])

                # dominated labels in each cluster
                assigned_labels_to_clusters_majority_labels = self.assign_majority(labels_real)

                test_labels = em_train.predict(test_prep)
                predicted_test = self.eval.predicted_to_real_assigned(test_labels, assigned_labels_to_clusters_majority_labels)
                for j in range(len(predicted_test)):
                    predicted_labels_test[j].append(predicted_test[j])
                    _labels_test[j].append(test_labels[j])


                trained_labels = em_train.predict(train_prep)
                predicted_train = self.eval.predicted_to_real_assigned(trained_labels, assigned_labels_to_clusters_majority_labels)
                for j in range(len(predicted_train)):
                    predicted_labels_train[j].append(predicted_train[j])
                    _labels_train[j].append(trained_labels[j])


        final_predicted_labels_test = [max(set(item), key = item.count) for item in predicted_labels_test ]
        final_predicted_labels_train = [max(set(item), key = item.count) for item in predicted_labels_train ]

        final_labels_test = [max(set(item), key = item.count) for item in _labels_test ]
        final_labels_train = [max(set(item), key = item.count) for item in _labels_train ]

        #           10                  0                       1                           2                           11
        print(";","Background noise;Information Exchange;Acts about possible actions;Commenting on previous discussions;Social Acts")
        print(";",len(meeting_input_test_[10]), ";", len(meeting_input_train_[0]), ";", len(meeting_input_train_[1]) , ";", len(meeting_input_train_[2]) , ";", len(meeting_input_test_[11]))

        predicted_prop = self.get_predicted_proportion(real_label_for_test_clustering[0:82], final_predicted_labels_test[0:82])
        print("Background noise",";",";", predicted_prop[0], ";", predicted_prop[1], ";", predicted_prop[2], ";")

        # predicted_prop = self.get_predicted_proportion(real_label_for_train_clustering[0:11359], final_predicted_labels_train[0:11359])
        # print("Information Exchange", ";",";", predicted_prop[0], ";", predicted_prop[1], ";", predicted_prop[2], ";")
        #
        # predicted_prop = self.get_predicted_proportion(real_label_for_train_clustering[11359:11359+4229], final_predicted_labels_train[11359:11359+4229])
        # print("Acts about possible actions", ";",";", predicted_prop[0], ";", predicted_prop[1], ";", predicted_prop[2], ";")
        #
        # predicted_prop = self.get_predicted_proportion(real_label_for_train_clustering[11359+4229:], final_predicted_labels_train[11359+4229:])
        # print("Commenting on previous discussions",";",";", predicted_prop[0], ";", predicted_prop[1], ";", predicted_prop[2], ";")
        #
        #
        # predicted_prop = self.get_predicted_proportion(real_label_for_test_clustering[82:], final_predicted_labels_test[82:])
        # print("Social Acts", ";",";", predicted_prop[0],";", predicted_prop[1], ";", predicted_prop[2], ";")

        print("************************")

        text = ''
        for i in range(self.number_of_clusters):
            text = text + ";" + str(i)

        print(text)

        predicted_prop = self.get_predicted_proportion(real_label_for_test_clustering[0:82], final_labels_test[0:82])
        print("Background noise;", self.print_proportion(predicted_prop))

        # predicted_prop = self.get_predicted_proportion(real_label_for_train_clustering[0:11359], final_labels_train[0:11359])
        # print("Information Exchange;", self.print_proportion(predicted_prop))
        #
        # predicted_prop = self.get_predicted_proportion(real_label_for_train_clustering[11359:11359+4229], final_labels_train[11359:11359+4229])
        # print("Acts about possible actions;", self.print_proportion(predicted_prop))
        #
        # predicted_prop = self.get_predicted_proportion(real_label_for_train_clustering[11359+4229:], final_labels_train[11359+4229:])
        # print("Commenting on previous discussions;", self.print_proportion(predicted_prop))
        #
        # predicted_prop = self.get_predicted_proportion(real_label_for_test_clustering[82:], final_labels_test[82:])
        # print("Social Acts;", self.print_proportion(predicted_prop))

        return

tag_to_DA = {0: 'sounds and noises', 1: 'information exchange',2: 'acts about possible actions',3: 'commenting on previous discussion' ,4: 'social acts'}

#label percentages for 5 classes: {0: 0.004, 1: 0.601, 2: 0.224, 3: 0.166, 4: 0.006}
#8%  1513 for each label: 5*1513 total number of samples for clustering
#label percentges for 3 classes: {0: 0.607, 1: 0.226, 2: 0.167} total elements: 18719 total sampling: 10619
#20%  3744 for each label: 3*3744 total number of samples for clustering

