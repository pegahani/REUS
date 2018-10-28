import heapq
import os.path

from nltk.translate.bleu_score import corpus_bleu
from nltk.translate.bleu_score import sentence_bleu

import tools
from tf_idf import tf_idf_class
from heapq import nlargest

class compare_with_AMI_results:

    def __init__(self, corpus_list):

        if not isinstance(corpus_list, (list,)):
            self.corpus_list = [corpus_list]
        else:
            self.corpus_list = corpus_list

    def get_resumes(self):

        self.resume_abstractive = []
        self.resume_extractive = []

        for meet in self.corpus_list:
            if os.path.exists('./manual_resume_abstractive/' + meet+ '.txt') == True:
                self.resume_abstractive.append(meet)
            if os.path.exists('./manual_resume_extractive/extsumm/' + meet + '.txt') == True:
                self.resume_extractive.append(meet)
        return


    def get_best_k_tfidf(self,k, tf_idf):
        """
        it finds the first K biggest tf-idf in list of computed tf-idf scores
        :param k:
        :param input:
        :return:
        """

        #indexes = heapq.nlargest(k, range(len(tf_idf)), tf_idf.__getitem__)
        top_k = heapq.nlargest(k, tf_idf, key= tf_idf.get)

        return top_k

    def clean_extractive(self, file):

        out = open('./axilaury_extractive/' + file + '.txt', 'w')

        myfile = open('./manual_resume_extractive/extsumm/' + file + '.txt', 'r')
        array = []

        for data in myfile:
            if ('to -->' not in data) and ('dialogue type :' not in data):
                array.append(data)
                data = tools.clean_line(data)

                out.write(data + '\n')

        return

    def bleu_evaluation(self, candidate):

        abstractive_score = None
        extractive_score = None

        """first elemnt in refrences is the abstractive resume and the second one is the extractive resume"""

        # if the list is not empty
        if self.resume_abstractive:

            abstractive_score = sentence_bleu([tools.tokenize(tools.text_to_string('./manual_resume_abstractive/'+text + '.txt', is_resume_abstract=True))
                                               for text in self.resume_abstractive], candidate)
        # if the list is not empty
        if self.resume_extractive:
            #self.clean_extractive(self.corpus)
            extractive_score = sentence_bleu([tools.tokenize(tools.text_to_string('./axilaury_extractive/' + text + '.txt'))
                                              for text in self.resume_extractive], candidate)

        return (abstractive_score, extractive_score)


# adress = './test/'
# document_0 = tools.text_to_string(adress + 'meet_1.txt')
# document_1 = tools.text_to_string(adress + 'meet_2.txt')
# document_2 = tools.text_to_string(adress + 'meet_3.txt')
# document_3 = tools.text_to_string(adress + 'meet_4.txt')
#
# all_documents = [document_0 , document_1, document_2, document_3]
# example = tf_idf_class(all_documents)
# tfidf_representation = example.tfidf()
# print(tfidf_representation)
#
# print('for meeting 1')
# print(document_0)
# print(tfidf_representation[0])
#
# c = compare_with_AMI_results('meet_1')
#
# candidate = c.get_best_k_tfidf(10, tfidf_representation[0])
#
# refrences = [tools.tokenize(tools.text_to_string('./test/refrence_1_meet_1.txt')),
#              tools.tokenize(tools.text_to_string('./test/refrence_2_meet_1.txt'))]
# print 'candidate', candidate
# c.bleu_evaluation(refrences, candidate)




# adress = './manuel_corpus/'
#
# all_documents = all_scenario_based_documents[0:4]
# example = tf_idf_class(all_documents)
# tfidf_representation = example.tfidf()
#
# for meet in scenario_based[0:4]:
#     file.write(meet)
#     file.write('*****************')
#
#     c = compare_with_AMI_results(meet)
#     c.get_resumes()
#     refrences = [c.resume_abstractive, c.resume_extractive]
#
#     candidate = c.get_best_k_tfidf(20, tfidf_representation[scenario_based.index(meet)])
#     file.write('candidate = '+ candidate)
#
#     bleu_measure = c.bleu_evaluation(refrences, candidate)
#
#     file.write('score_abstractive = ' + bleu_measure[0])
#     file.write(' score_extractive = ' + bleu_measure[1])
#
# file.flush()
#
# file.close()


