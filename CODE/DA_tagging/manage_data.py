from all_representations import DA_icsi_list, DA_ami_list

re_arrange_labels = {1: 0, 2: 1, 3: 2, 0: 10, 4: 11}

class manage_data:
    def __init__(self, corpus, n_taxonomy):

        self.n_taxonomy = n_taxonomy

        if corpus == 'icsi':
            self.meeting_group = DA_icsi_list
        elif corpus == 'ami':
            self.meeting_group = DA_ami_list

    def extract_train_test_minority(self, meeting_input, train_index = None, test_index = None):

        if (train_index is not None ) and (test_index is not None):
            output_train = {i: ([], []) for i in range(self.n_taxonomy)}
            output_test = {i: ([], []) for i in range(self.n_taxonomy)}

            for i in train_index:

                for j in range(len(meeting_input[i][1])):

                    label = meeting_input[i][1][j]
                    output_train[label][1].append(label)
                    output_train[label][0].append(meeting_input[i][0][j][1])


        # else:
        #
        #     #re_arrange_labels = {1: 0, 2: 1, 3: 2, 0: 10, 4: 11}
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
