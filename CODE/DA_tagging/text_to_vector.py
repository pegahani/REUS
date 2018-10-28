# coding: utf-8
#-----------------------------------------------
#class gensim.models.word2vec.Word2Vec(sentences=None, size=100, alpha=0.025, window=5, min_count=5, max_vocab_size=None,
#                                      sample=0.001, seed=1, workers=3, min_alpha=0.0001, sg=0, hs=0, negative=5, cbow_mean=1,
#                                      hashfxn= < built- in function hash >, iter=5, null_word=0, trim_rule=None, sorted_vocab=1,
#                                      batch_words=10000, compute_loss=False, callbacks=())

# size (int) – Dimensionality of the feature vectors.
# alpha (float) – The initial learning rate.
# window (int) – The maximum distance between the current and predicted word within a sentence.
# sg (int {1, 0}) – Defines the training algorithm. If 1, skip-gram is employed; otherwise, CBOW(continuous bag-of-words) is used.

"""CBOW is faster while skip-gram is slower but does a better job for infrequent words."""

# min_alpha (float) – Learning rate will linearly drop to min_alpha as training progresses.
# seed (int) – Seed for the random number generator. Initial vectors for each word are seeded with a hash of the concatenation of word + str(seed). Note that for a fully deterministically-reproducible run, you must also limit the model to a single worker thread (workers=1), to eliminate ordering jitter from OS thread scheduling. (In Python 3, reproducibility between interpreter launches also requires use of the PYTHONHASHSEED environment variable to control hash randomization).
# min_count (int) – Ignores all words with total frequency lower than this.
# max_vocab_size (int) – Limits the RAM during vocabulary building; if there are more unique words than this, then prune the infrequent ones. Every 10 million word types need about 1GB of RAM. Set to None for no limit.
# sample (float) – The threshold for configuring which higher-frequency words are randomly downsampled, useful range is (0, 1e-5).
# workers (int) – Use these many worker threads to train the model (=faster training with multicore machines).
# hs (int {1,0}) – If 1, hierarchical softmax will be used for model training. If set to 0, and negative is non-zero, negative sampling will be used.
# negative (int) – If > 0, negative sampling will be used, the int for negative specifies how many “noise words” should be drawn (usually between 5-20). If set to 0, no negative sampling is used.
# cbow_mean (int {1,0}) – If 0, use the sum of the context word vectors. If 1, use the mean, only applies when cbow is used.
# hashfxn (function) – Hash function to use to randomly initialize weights, for increased training reproducibility.
# iter (int) – Number of iterations (epochs) over the corpus.
# trim_rule (function) – Vocabulary trimming rule, specifies whether certain words should remain in the vocabulary, be trimmed away, or handled using the default (discard if word count < min_count). Can be None (min_count will be used, look to keep_vocab_item()), or a callable that accepts parameters (word, count, min_count) and returns either gensim.utils.RULE_DISCARD, gensim.utils.RULE_KEEP or gensim.utils.RULE_DEFAULT. Note: The rule, if given, is only used to prune vocabulary during build_vocab() and is not stored as part of the model.
# sorted_vocab (int {1,0}) – If 1, sort the vocabulary by descending frequency before assigning word indexes.
# batch_words (int) – Target size (in words) for batches of examples passed to worker threads (and thus cython routines).(Larger batches will be passed if individual texts are longer than 10000 words, but the standard cython code truncates to that maximum.)
# compute_loss (bool) – If True, computes and stores loss value which can be retrieved using model.get_latest_training_loss().
# callbacks – List of callbacks that need to be executed/run at specific stages during training.
# -----------------------------------------------


#in word2vec, Word vectors are positioned in the vector space such that words that share common contexts in the corpus
# are located in close proximity to one another in the space

from __future__ import print_function

from gensim.models import Word2Vec
from nltk.stem import *
from nltk.stem import WordNetLemmatizer
from nltk.stem.porter import *
import string
import numpy as np

from stop_words import get_stop_words
from nltk.corpus import stopwords

import gensim, logging

adress_corpus_ami = '../corpus-prep/manuel_corpus/'
adress_corpus_icsi = '../corpus-prep/ICSI_corpus/'
adress_resume_ami = '../corpus-prep/manual_resume_extractive/extsumm/'
adress_resume_icsi = '../corpus-prep/ICSI_DialogueActs/'

class text_to_vector:

    def __init__(self):

        self.adress = '../corpus-prep/manuel_corpus/'
        self.lemmatizer = WordNetLemmatizer()
        self.stemmer = PorterStemmer()

    def remove_punctuation(self, words):
        table = str.maketrans('', '', string.punctuation)
        non_punctuation_words = [w.translate(table) for w in words]

        return non_punctuation_words

    def to_lowercase(self, words):

        words = [word.lower() for word in words]
        return words

    # #--------------------
    # load text
    def generate_sentences(self, filenames, with_punctuations):

        sentences = []

        for filename in filenames:
            with open(filename, 'rt') as f:
                for line in f:
                    text = line[5:]
                    words = text.split(' ')

                    # remove punctuation from each word
                    #TODO: Not sure the punctuation should be removed from utterances

                    "with punctuations"
                    if with_punctuations:
                        words_no_punctuation = words
                    #without punctuations
                    else:
                        words_no_punctuation = self.remove_punctuation(words)
                    #plurals = plurals_

                    #remove \n from the end of each utterances
                    words_no_punctuation[-1] = words_no_punctuation[-1][0:-1]
                    words_lower = self.to_lowercase(words_no_punctuation)

                    #lemmatization
                    #TODO: the w!= '' condition should be modified better in word preparation part
                    word_lematized = [self.lemmatizer.lemmatize(w) for w in words_lower if w!= '']

                    sentences.append(word_lematized)

                    # TODO: not sure about stemming or lemmatization order.
                    # lemmatization
                    #singles = [lemmatizer.lemmatize(plural) for plural in plurals]

                    # TODO: stemming gives strange results
                    # stemming
                    #singles_stemming = [stemmer.stem(w) for w in singles]

        return sentences
    # #-----------------------------------

    def remove_stopwords(self, word_list):

        stop_words = list(get_stop_words('en'))  # About 900 stopwords
        nltk_words = list(stopwords.words('english'))  # About 150 stopwords
        stop_words.extend(nltk_words)
        punctuation = list(string.punctuation)

        output = []
        for w in word_list:
            if (len(w) > 1) and (w[-1] in punctuation):
                tempo = w[:-1]
                #if w[-2] in punctuation:
                #    tempo = w[:-2]
            else:
                tempo = w
            if tempo not in stop_words:
                output.append(tempo)

        #output = [w for w in word_list if not w in stop_words]

        return output

    #TODO: word2vec train on which sentences?
    #TODO: the default length for word2vec is 100 for each word. which is long. what can we do to solve it?
    def word2vec_make_model(self, sentences, with_punctuations):
        logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

        # train model
        # TODO word2vec parametrs will change
        """the smaller the window, it is more grammatical and the bigger the window the vectors are more semantic."""
        model = Word2Vec(sentences, size=20, window=5, min_count=1, workers=4)
        #model = Word2Vec(sentences, min_count=1)

        # summarize vocabulary
        #words = list(model.wv.vocab)

        #print(words)
        # access vector for one word

        #print(model['sentence'])
        # save model

        "if with puntuation"
        if with_punctuations:
            model.save('./model/model_word2vec.bin')
        else:
            #if without punctuation
            model.save('./model/model_no_punctuation_word2vec.bin')


        # load model
        #new_model = Word2Vec.load('model.bin')

        pass

    def text_preparation(self, utterance):

        #text = utterance[5:]
        words = utterance.split(' ')

        words_no_punctuation = self.remove_stopwords(words) #self.remove_punctuation(words)

        # remove \n from the end of each utterances
        #words_no_punctuation[-1] = words_no_punctuation[-1][0:-1]
        words_lower = self.to_lowercase(words_no_punctuation)

        # lemmatization
        word_lematized = [self.lemmatizer.lemmatize(w) for w in words_lower]

        return word_lematized

    def retrain_model(self, new_sentences, with_punctiations):
        """
        this is supposed to be a function that continue training on new input to the system. Since we learn on all corpora in
        one shot, we do not need this function anymore.
        :param new_sentences:
        :return:
        """
        if with_punctiations:
            model_ = Word2Vec.load('./model/model_word2vec.bin')
        else:
            model_ = Word2Vec.load('./model/model_no_punctuation_word2vec.bin')

        model_.build_vocab(new_sentences, update=True)
        model_.train(new_sentences, total_examples=model_.corpus_count, epochs=model_.iter)

        if with_punctiations:
            model_.save('./model/model_word2vec.bin')
        else:
            model_.save('./model/model_no_punctuation_word2vec.bin')


        pass

    def is_word_in_word2vec_vocabulary(self, sentence_list, model_):
        words_model = model_.wv.vocab
        for w in sentence_list:
            if w not in words_model:
                return False

        return True

    def word2vec_generation(self, utterance, with_punctuations):
        """
        a method that gets an utterance and gives back its word2vec vector representation by taking the punctuations or not.
        :param utterance:
        :param with_punctuations:
        :return:
        """
        vector = []

        #words = self.text_preparation(utterance)

        words = utterance

        #model_ = Word2Vec.load('model.bin')
        #if not self.is_word_in_word2vec_vocabulary(utterance, model_):
        #    self.retrain_model([words])

        if with_punctuations:
            new_model = Word2Vec.load('./model/model_word2vec.bin')
        else:
            new_model = Word2Vec.load('./model/model_no_punctuation_word2vec.bin')



        # TODO: how generate word2vec vectors for each utterance using the vocabularies in Word2vec model?

        #First: average of Word2Vec vectors in each utterance
        for w in words:
            vector.append(new_model.wv[w])

        return np.mean(vector, axis=0)
