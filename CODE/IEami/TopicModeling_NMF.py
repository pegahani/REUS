"""https://de.dariah.eu/tatom/topic_model_python.html"""

import os
import numpy as np  # a conventional alias
import sklearn.feature_extraction.text as text
from sklearn import decomposition

class TM_NMF:
    def __init__(self, all_documents, num_topics, num_top_words, min_df, max_df, isblock):
        self.all_documents = all_documents
        self.num_topics = num_topics
        self.num_top_words = num_top_words
        self.min_df = min_df
        self.max_df = max_df

        path = os.getcwd() + '/' #'/IEami/'
        #self.file = open(path + 'Topic_huge.txt', 'w')

        if isblock:
            self.file = open(path + 'result_ami/' + 'Topic_modeling_nmf_block_' + str(num_topics) + '_topics.txt', 'w')
        else:
            self.file = open(path + 'result_ami/' + 'Topic_modeling_nmf_' + str(num_topics) + '_topic_scenario.txt', 'w')


    def find_NMF_topics(self):
        """
        :param num_topics:
        :param num_top_words: a list of top words for each topic
        :return:
        """

        vectorizer = text.CountVectorizer(input='filename', stop_words='english', min_df= self.min_df, max_df= self.max_df)
        dtm = vectorizer.fit_transform(self.all_documents).toarray()

        vocab = np.array(vectorizer.get_feature_names())
        clf = decomposition.NMF(n_components = self.num_topics, random_state=1)

        # it shows for how many proability each corpus is related to a word in topic results
        self.doctopic = clf.fit_transform(dtm)

        self.topic_words = []
        for topic in clf.components_:
            word_idx = np.argsort(topic)[::-1][0:self.num_top_words]
            self.topic_words.append([vocab[i] for i in word_idx])

        return

    def show_corpus_vs_topics(self):
        # ***************************************
        self.file.write('******************************************************\n')

        # they normaloze doctopic w.r.t its rows
        doctopic = (self.doctopic) / (np.sum(self.doctopic, axis=1, keepdims=True))
        corpus_names = []

        for fn in self.all_documents:
            name = os.path.basename(fn)
            # name = name.rstrip('0123456789')
            corpus_names.append(name)

        # turn this into an array so we can use NumPy functions
        novel_names = np.asarray(corpus_names)

        doctopic_orig = doctopic.copy()

        # use method described in preprocessing section
        doctopic_grouped = np.zeros((len(corpus_names), self.num_topics))

        # self.file.write('\t\t\t\t\t')
        # for i in range(self.num_topics):
        #     self.file.write( 'topic'+ str(i+1) +  '\t')

        self.file.write('\n')

        for i, name in enumerate(sorted(set(novel_names))):
            tempo = np.mean(doctopic[novel_names == name, :], axis=0)

            doctopic_grouped[i, :] = tempo
            #self.file.write(name + "  " + str(doctopic_grouped[i, :]) + '\n')

        self.file.write('\n')
        self.file.write("meetings\t\t\t\t\t")
        self.file.write("top topics\t\t\t\t\t\t")
        self.file.write("probabilities for top topics\n")
        corpus = corpus_names

        for i in range(len(doctopic)):
            top_topics = np.argsort(doctopic[i, :])[::-1][0:5]
            top_topics_str = ' '.join(str(t) for t in top_topics)

            top_probabilities = ' '.join(str(doctopic[i][t]) for t in top_topics)

            self.file.write("{}: {}  {}".format(corpus[i], top_topics_str, top_probabilities) + '\n')
            self.file.flush()
        return

    def show_topic_words(self):
        self.file.write('\n')
        for t in range(len(self.topic_words)):
            self.file.write("Topic {}: {}".format(t, ' '.join(self.topic_words[t][:self.num_top_words]) + '\n'))
            self.file.flush()
        return


