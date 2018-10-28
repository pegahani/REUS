import random
from collections import Counter
import numpy as np

from imblearn.over_sampling import SMOTE
from sklearn.decomposition import TruncatedSVD


class sampling_data:

    def __init__(self, n_taxonomies, meeting_group):

        self.n_taxonomies = n_taxonomies
        self.meeting_group = meeting_group

    def blind_sampling(self, data_input, percentage, number_sample):

        """
        it returns which_percentage samples of _data
        :param data_:
        :param which_percent:
        :return:
        """

        samples = []
        real_label = []

        sum_ = sum(len(value) for value in data_input.values())

        if number_sample== None:
            number_sample = round(percentage * sum_)
        else:
            number_sample = number_sample

        blind_data = []
        for key in data_input.keys():
            for i in data_input[key]:
                blind_data.append((i, key))

        random.shuffle(blind_data)

        print(number_sample)
        print(len(blind_data))
        for i in range(number_sample):
            element = blind_data.pop()
            samples.append(element[0])
            real_label.append(element[1])

        #print(Counter(real_label))

        return (samples, real_label, number_sample)

    def sampling_wrt_taxonomy(self, all_for_train_clustering, which_percent):
        "sampling data by taking their real labels into the account. It is not just a blind sampling."

        my_dict = {j: 0 for j in range(self.n_taxonomies)}
        label_positions = {j: [] for j in range(self.n_taxonomies)}

        for i in all_for_train_clustering.keys():
            tempo = all_for_train_clustering[i][1]

            my_dict_tempo = {m: tempo.count(m) for m in tempo}
            my_dict = dict(Counter(my_dict) + Counter(my_dict_tempo))

            place_counter = 0
            for k in tempo:
                label_positions[k].append(
                    (i, place_counter))  # i is meeting number, place_counter is its position in meeting
                place_counter += 1

        sum_ = sum(my_dict.values())
        percentage = {key: float("{0:.3f}".format(my_dict[key] / sum_)) for key in my_dict.keys()}
        # print('percentage', percentage)

        "number of sampled data of classes with higher number of samples"
        total_sum = round(which_percent * sum_)

        #number_sample = round(total_sum /self.n_taxonomies)
        number_sample = total_sum
        # print("number_sample for each label", number_sample)

        samples = {j: None for j in self.meeting_group}
        indexes = {l: [] for l in self.meeting_group}

        # choose indexes randomly
        for i in range(self.n_taxonomies):
            if i in my_dict.keys():
                if my_dict[i] <= number_sample:
                    for element in label_positions[i]:
                        indexes[element[0]].append(element[1])
                else:
                    select_random = random.sample(label_positions[i], number_sample)
                    for element in select_random:
                        indexes[element[0]].append(element[1])

        for _meet in self.meeting_group:
            samples[_meet] = ([all_for_train_clustering[_meet][0][t] for t in indexes[_meet]],
                              [all_for_train_clustering[_meet][1][t] for t in indexes[_meet]])

        t = []
        for i in samples.keys():
            if samples[i][1] != []:
                for j in samples[i][1]:
                    t.append(j)

        #print(Counter(t))
        return (samples, total_sum*self.n_taxonomies)

class train_test_prep:

    def __init__(self, meeting_input, meeting_group, n_taxonomy, blind_samling, sampling, text_represent, which_percentage):

        self.meeting_group = meeting_group
        self.n_taxonomy = n_taxonomy

        self.blind_samling = blind_samling
        if which_percentage != None:
            self.which_percentage = which_percentage
        else:
            self.which_percentage = None
        self.text_represent = text_represent

        self.meeting_input =  meeting_input
        self.sampling = sampling

        self.svd = TruncatedSVD(n_components=50, n_iter=5, random_state= None)

    def extract_train_test_minority(self, meeting_input, train_index = None, test_index = None):

        output_train = None
        output_test = None


        if train_index is not None:
            output_train = {i: ([], []) for i in range(self.n_taxonomy)}

        if test_index is not None:
            output_test = {i: ([], []) for i in range(self.n_taxonomy)}

        for i in train_index:
            for j in range(len(meeting_input[i][1])):
                label = meeting_input[i][1][j]
                output_train[label][1].append(label)
                output_train[label][0].append(meeting_input[i][0][j][1])

        # else:
        #
        #     re_arrange_labels = {1: 0, 2: 1, 3: 2, 0: 10, 4: 11}
        #     output_train = {i: ([], []) for i in [0,1,2]}
        #     output_test = {i: ([], []) for i in [10,11]}
        #
        #     for i in self.meeting_group:
        #
        #         for j in range(len(meeting_input[i][1])):
        #
        #             if meeting_input[i][1][j] in [1, 2, 3]:
        #                 label = re_arrange_labels[ meeting_input[i][1][j] ]
        #                 output_train[label][1].append(label)
        #                 output_train[label][0].append(meeting_input[i][0][j][1])
        #
        #             elif meeting_input[i][1][j] in [0,4]:
        #                 label = re_arrange_labels[ meeting_input[i][1][j] ]
        #                 output_test[label][1].append(label)
        #                 output_test[label][0].append(meeting_input[i][0][j][1])

        return (output_train, output_test)

    def prepare_train_test_data(self, train_index, test_index, is_smote, smote_kind, num_sample):

        if num_sample != None:
            number_sample = num_sample
        else:
            number_sample = None

        if self.text_represent == 'lexical':
            _input_for_clustering = np.concatenate(tuple(
                [item[1] for item in self.meeting_input[i][0]] for i in self.meeting_input.keys() if self.meeting_input[i] != ([], [])), axis=0)
            self.svd.fit(_input_for_clustering)

        _input_for_train_clustering = None
        real_label_train_clustering = None
        _train_blind = None

        test_prep = None
        #real_label_for_test_clustering = None
        #predicted_labels_ = None

        if test_index is not None:
            X_test = [self.meeting_group[p] for p in test_index]
            _input_for_test_clustering = np.concatenate(tuple([item[1] for item in self.meeting_input[i][0]] for i in X_test if self.meeting_input[i] != ([], [])), axis=0)
            test_prep = [item.tolist() for item in _input_for_test_clustering]
            # real_label_for_test_clustering = sum([self.meeting_input[i][1] for i in X_test], [])
            # predicted_labels_ = [[] for i in real_label_for_test_clustering]
            if self.text_represent == 'lexical':
                test_prep = self.svd.transform(test_prep)
        else:
            X_test = None

        X_train = [self.meeting_group[k] for k in train_index]
        train_ = {key: self.meeting_input[key] for key in self.meeting_input.keys()}

        if self.blind_samling:
            (_train_blind, _test_blind) = self.extract_train_test_minority(self.meeting_input, X_train, X_test)

        """for NOT blind sampling case"""
        if not self.blind_samling:
            (meeting_input_train, number_sample) = self.sampling.sampling_wrt_taxonomy(train_, self.which_percentage)
            _input_for_train_clustering = np.concatenate(tuple(
                [item[1] for item in meeting_input_train[i][0]] for i in X_train if meeting_input_train[i] != ([], [])), axis=0)
            real_label_train_clustering = np.concatenate(tuple(meeting_input_train[i][1] for i in X_train if meeting_input_train[i] != ([], [])), axis=0)

        """for blind sampling case"""
        if self.blind_samling:
            meeting_input_train_ = {key: _train_blind[key][0] for key in _train_blind.keys()}
            (_input_for_train_clustering, real_label_train_clustering, number_sample) = self.sampling.blind_sampling(meeting_input_train_, self.which_percentage, number_sample)

        if is_smote:
            """do over sampling on minority classes background noise and Social Acts"""
            sm = SMOTE(kind=smote_kind)
            _input_for_train_clustering, real_label_train_clustering = sm.fit_sample(_input_for_train_clustering,
                                                                                     real_label_train_clustering)

        return (_input_for_train_clustering, real_label_train_clustering, test_prep, number_sample) #, real_label_for_test_clustering, predicted_labels_)