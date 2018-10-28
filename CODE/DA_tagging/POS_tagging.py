
# Tag 	Meaning 	            English Examples

# ADJ 	adjective 	            new, good, high, special, big, local
# ADP 	adposition 	            on, of, at, with, by, into, under
# ADV 	adverb 	                really, already, still, early, now
# CONJ 	conjunction 	        and, or, but, if, while, although
# DET 	determiner, article 	the, a, some, most, every, no, which
# NOUN 	noun 	                year, home, costs, time, Africa
# NUM 	numeral 	            twenty-four, fourth, 1991, 14:24
# PRT 	particle 	            at, on, out, over per, that, up, with
# PRON 	pronoun 	            he, their, her, its, my, I, us
# VERB 	verb 	                is, say, told, given, playing, would
# . 	punctuation marks 	    . , ; !
# X 	other 	                ersatz, esprit, dunno, gr8, univeristy

# vector representation of POS tagging. One hot representation for POS. [ADJ, ADP, ADV, CONJ, DET, NOUN, NUM, PRT, PRON, VERB, ., X]
import string

import nltk
from nltk import word_tokenize
from nltk.corpus import brown
from nltk.stem import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer

import pickle
import re


import numpy as np

"""if you have any problem in executing this code remove the CODE. at the begining of all imports"""
from text_to_vector import text_to_vector, adress_corpus_ami, adress_corpus_icsi

#necessary variables---------------------

suffixes_extractive_ami = [i + 1 for i in range(151)]
for j in [9, 24, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 150]:
    suffixes_extractive_ami.remove(j)


meeting_list_icsi = ['Bdb001'] + ['Bed00'+str(k) for k in range(2,10) if k != 7] +\
               ['Bed0'+str(k) for k in range(10,18) ]+\
               ['Bmr00' + str(j) for j in range(1,10) if j != 4]+['Bmr0' + str(j) for j in range(10,31) if j != 17]+\
               ['Bns00' + str(j) for j in range(1,4)]+\
               ['Bro00' + str(j) for j in range(3,10) if (j != 6 and j!= 9)]+['Bro0' + str(j) for j in range(10,29) if j != 20]+\
               ['Bsr001', 'Btr001', 'Btr002', 'Buw001']

#------------------------------
Tag_ = {   'ADJ' :  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           'ADP' :  [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           'ADV' :  [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           'CONJ':  [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
           'DET' :  [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
           'NOUN':  [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
           'NUM' :  [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
           'PRT' :  [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
           'PRON':  [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
           'VERB':  [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
           '.'   :  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
           'X'   :  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
}


DA_tag = {'Backchannel\n':0, 'Stall\n': 1,'Fragment\n':2,
          'Inform\n':3, 'Elicit-Inform\n':4,
          'Suggest\n':5, 'Offer\n':6, 'Elicit-Offer-Or-Suggestion\n':7,
          'Assess\n':8, 'Comment-About-Understanding\n': 9, 'Elicit-Assessment\n':10, 'Elicit-Comment-Understanding\n': 11,
          'Be-Positive\n':12, 'Be-Negative\n':13,
          'Other\n':14 }


tempo = {0:['%', '%--', '%-', 'x', 'bd', 'bc', 'bh', 'b', 't1', 't3', 'nd'], #background noise
                  1: ['s', 'na', 'ng', 'no', 'bk', '2'],  # information exchange
                  2: ['cs', 'co', 'tc', 'na', 'ng'], #acts about possible actions
                  3: ['cc', 'aa', 'bu', 'r', 'bs', 'aap', 'arp', 'am', 'ar', 'br', 'df', 'e'], #comment on previous discussions
                  4: ['fe', 'ft', 'fw', 'fa', 'ba', 'by', 'j'], #socila acts (+, -)
                  5: ['z', 'h', 'm', 'f', 'fh', 'fg', 'bsc', 'rt', 't', 'sj'], # other
                 -1: ['qw', 'qy', 'qo', 'qr', 'qrr', 'qh', 'd', 'g'] # questions
}

# DA_icsi_2_AMI = {}
# for key,val in tempo.items():
#     for item in val:
#         DA_icsi_2_AMI[item] = key

#TODO the coherency between icsi and AMI may be changed later. We used this paper to find it:
#The ICSI Meeting Recorder Dialog Act (MRDA) Corpus, Shriberg, Dhillon, Bhagat, Ang and Carvey

DA_icsi_2_AMI = {'%': 0, '%--': 0, '%-': 0, 'x': 0, 'bd': 0, 'bc': 0, 'bh': 0, 'b': 0, 't1': 0, 't3': 0, 'nd': 0,'s': 1, 'na': 2, 'ng': 2, 'no': 1, 'bk': 1, '2': 1, 'cs': 2, 'co': 2, 'tc': 2, 'cc': 3, 'aa': 3, 'bu': 3, 'r': 3, 'bs': 3, 'aap': 3, 'arp': 3, 'am': 3, 'ar': 3, 'br': 3, 'df': 3, 'e': 3, 'fe': 4, 'ft': 4, 'fw': 4, 'fa': 4, 'ba': 4, 'by': 4, 'j': 4, 'z': 5, 'h': 5, 'm': 5, 'f': 5, 'fh': 5, 'fg': 5, 'bsc': 5, 'rt':5, 't':5, 'sj':5, 'qw': -1, 'qy': -1, 'qo': -1, 'qr': -1, 'qrr': -1, 'qh': -1, 'd': -1, 'g': -1}


#backchannel, stall, fragment
#INFORMATION EXCHANGE: inform, elicit inform
#ACT ABOUT POSSIBLE ACTIONS: suggest, offer, elicit-offer-or-suggest
#COMMENTING ON PREVIOUS DISCUSSION: assses, comment-about-understanding, elicit-assesment, elicit-comment-about-understanding
#SOCIAL ACTS: be-positive, be-negative
#OTHER

# other: fragment : unfinished utterances

class initialisation:

    def __init__(self, corpus_name):

        global lem
        global stem
        global w2vec
        global corpus

        lem = WordNetLemmatizer()
        stem = PorterStemmer()
        w2vec = text_to_vector()
        corpus = corpus_name

# ----------- analyse words in corpus-------------------------
class dictionary:

    def get_meeting_index(self, filename):
        return re.search(r'\d+', filename).group()

    def load_dictionary(self, filenames, with_lable):
        """
        this function gets dictionary of words from all meetings plain texts and save them in "Dictionary/dictionary_no_stop_words"
        :param filenames:
        :param with_lable:
        :return:
        """

        #output_ = []
        #output_lematize = []
        output_stem_all = {}

        if with_lable:
            output_stem = []

            for filename in filenames:
                with open(filename, 'rt') as f:
                    for line in f:
                        text = (line[5:]).split()

                        #output_ = list(set(output_ + text))
                        #output_lematize = list(set(output_lematize + [lem.lemmatize(word) for word in text]))

                        """remove stop words"""
                        sent_vector = w2vec.remove_stopwords([stem.stem(word) for word in text])
                        output_stem = list(set(output_stem + sent_vector))


            filehandler = None
            if corpus == 'ami':
                filehandler = open('Dictionary/dictionary_no_stop_words'+'_ami', 'wb')
            elif corpus == 'icsi':
                filehandler = open('Dictionary/dictionary_no_stop_words' + '_icsi', 'wb')

            pickle.dump(output_stem, filehandler)

        pass

    def reload_dictionary(self):

        filehandler = None
        
        if corpus == 'ami':
            filehandler = open('Dictionary/dictionary_no_stop_words'+'_ami', 'rb')
        elif corpus == 'icsi':
            filehandler = open('Dictionary/dictionary_no_stop_words'+'_icsi', 'rb')

        dictionary = pickle.load(filehandler)

        return dictionary

#-------------POS tagging preparation---------------------
class word_embedding:
    def __init__(self):
        self.dictionary = dictionary().reload_dictionary()


    def one_hot_POS(self, tag):
        return Tag_[tag]

    def sentence_2_pos(self, sent):

        porter = PorterStemmer()
        #without stemming
        #text = nltk.word_tokenize(sent)

        #with stemming
        text = [porter.stem(word) for word in word_tokenize(sent)]
        posTagged = nltk.pos_tag(text)
        words_tags = [(word, nltk.map_tag('en-ptb', 'universal', tag)) for word, tag in posTagged]

        words = [item[0] for item in words_tags]
        tags  = [item_[1] for item_ in words_tags]

        pos_onehot = [self.one_hot_POS(i) for i in tags]
        pos = list(np.sum(np.array(pos_onehot), axis=0))

        return (words, pos)

    def sentence_2_word2vec(self, text):

        words = text.split(' ')

        # remove punctuation from each word
        # TODO: Not sure the punctuation should be removed from utterances
        #words_no_punctuation = w2vec.remove_punctuation(words)

        # keep the punctuation
        #words_no_punctuation = w2vec.remove_stopwords(words)
        words_no_punctuation = words

        # plurals = plurals_

        # remove \n from the end of each utterances
        words_no_punctuation[-1] = words_no_punctuation[-1][0:-1]
        words_lower = w2vec.to_lowercase(words_no_punctuation)

        # lemmatization
        # TODO: the w!= '' condition should be modified better in word preparation part
        word_lematized = [w2vec.lemmatizer.lemmatize(w) for w in words_lower if w != '']

        return (words, (w2vec.word2vec_generation(word_lematized, with_punctuations= True)).tolist())

    # ---- generate vectors with tags --------------------

    def sentence_2_lexical(self, sent, dictionary):

        word = [stem.stem(word) for word in sent]
        vect = [1 if item in word else 0 for item in dictionary]
        return(word, vect)


    def find_icsi_label(self, param):
        "it finds the correct label for DAs w.r.t the DAs in icsi."
        pipe_index = param.rfind('|')
        #TODO: since that I didn't understand what the DA types before the |, I receive the DA types only after the | if there is one with |
        if pipe_index != -1:
            param = param[pipe_index+1:]

        "separate strings by . and ^"
        DAs = re.split(r'[.^:]', param[:-1])
        DA_ami_based = list(set([DA_icsi_2_AMI[i] for i in DAs]))

        return DA_ami_based

    def generate_tag(self, corpus, filenames, representation, with_tag):
        "it gets the sentences and tags from the supported text files."
        output_ = []
        tags_ = []

        # files_indexes = [get_meeting_index(file) for file in filenames]
        # print(files_indexes)

        #for j in tempo.keys():
        # keys = [str(i+1) for i in range(8)] + ['10', '11', '12', '13', '14', '15']
        # for j in keys :
        #      dictionary = list(set(dictionary + tempo[j]))


        #if we use the extractive summaries with their given tags
        if with_tag:
            for filename in filenames:
                with open(filename, 'rt') as f:
                    for line in f:
                        #if it is dialogue type
                        saved_line = line
                        if saved_line[0:13] == 'dialogue type':
                            if corpus == 'ami':
                                # each utterance has only one dialogue act, but to make the code coherent with ICSI, we put a dialogue act type in a list.
                                tags_.append(DA_tag[saved_line[16:]])
                            elif corpus == 'icsi':
                                # each utterance may have several DA types.
                                tags_.append(self.find_icsi_label(saved_line[16:]))

                        elif saved_line[0:4] in ['A : ', 'B : ', 'C : ', 'D : ', 'E : ', 'F : ', 'G : ', 'H : ', 'I : ', 'J : ', 'K : ']:
                            #if there is a word in DA in the specified line of the text. Because some DAs are empty.

                            if len(saved_line[4:-1]) > 1:
                                if representation == 'POS':
                                    output_.append(self.sentence_2_pos(saved_line[4:]))
                                elif representation == 'word2vec':
                                    output_.append(self.sentence_2_word2vec(saved_line[4:]))
                                elif representation == 'POS+word2vec':
                                    output_.append(self.sentence_2_pos(saved_line[4:])+self.sentence_2_word2vec(saved_line[4:]))
                                elif representation == 'lexical':
                                    output_.append(self.sentence_2_lexical(saved_line[4:], self.dictionary))
                                    #output_.append(sentence_2_lexical(saved_line[4:]))
                            else:
                                del tags_[-1]

        return (output_, tags_)

    def vector_representation(self, text, representation):

        # preparer dictionary of words in corpus
        dictionary = []
        tempo = self.dictionary

        # All scenario based extractive summaries in AMI
        # for j in tempo.keys():
        keys = [str(i + 1) for i in range(8)] + ['10', '11', '12', '13', '14', '15']
        for j in keys:
            dictionary = list(set(dictionary + tempo[j]))

        if representation == 'POS':
            return self.sentence_2_pos(text)
        elif representation == 'word2vec':
            return self.sentence_2_word2vec(text)
        elif representation == 'lexical':
            return self.sentence_2_lexical(text, dictionary)

        pass


#---------------some tools------------------------
# the vocabulary of AMI words has been intialised already
# TODO: the vocabulary are extracted with punctuations at the end of each word such as: mind. recording.
def load_ami_dictionary_words():
    "this should be initiated every time"
    initialisation('ami')

    # load dictionary of words for AMI corpus
    files = [adress_corpus_ami + 'meet_' + str(num) + '.txt' for num in suffixes_extractive_ami]
    dic = dictionary()
    dic.load_dictionary(files, True)

# the vocabulary of ICSI words has been intialised already.
def load_icsi_dictionary_words():
    "this should be initiated every time"
    initialisation('icsi')

    # load dictionary of words for AMI corpus
    files = [adress_corpus_icsi + i +'.txt' for i in meeting_list_icsi]
    dic = dictionary()
    dic.load_dictionary(files, True)


#------------------------------------------------------

