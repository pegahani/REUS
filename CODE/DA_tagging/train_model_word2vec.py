#this script is for training the word2vec vector on a given corpus. Because word2vec should train on a text database.
# here we learn on all corpora to make our experiments coherent. The generated model is saved in ./DATA

from text_to_vector import text_to_vector
from clusters import cluster, DA_icsi_list


meeting_list_icsi = ['Bdb001'] + ['Bed00'+str(k) for k in range(2,10) if k != 7] +\
               ['Bed0'+str(k) for k in range(10,18) ]+\
               ['Bmr00' + str(j) for j in range(1,10) if j != 4]+['Bmr0' + str(j) for j in range(10,31) if j != 17]+\
               ['Bns00' + str(j) for j in range(1,4)]+\
               ['Bro00' + str(j) for j in range(3,10) if (j != 6 and j!= 9)]+['Bro0' + str(j) for j in range(10,29) if j != 20]+\
               ['Bsr001', 'Btr001', 'Btr002', 'Buw001']


#NOTICE : If you want add a new corpus retrain the models on union of all corpora!!
def train_mode(with_punctuation):
    """
    this function trains a word2vev model on all AMI meetings.
    with_punctuation: it says if the punctuations should be taken into account for word2vec model or not.
    :return:
    """

    word2vec_prep = text_to_vector()

    "texts in AMI corpus"
    suffixes = [str(51)+'b']+[str(i+1) for i in range(188) ]
    for j in ['9', '24', '100', '101', '102', '103', '104', '105', '106', '107', '108', '109', '110', '111', '152', '153',
              '154', '155']:
        suffixes.remove(j)

    filenames_ = [word2vec_prep.adress+'meet_'+ i +'.txt' for i in suffixes]

    "add texts of icsi"
    for meet in meeting_list_icsi:
        filenames_.append('../corpus-prep/ICSI_corpus/'+ meet + '.txt')

    for da in DA_icsi_list:
        filenames_.append(da)


    #the generated model can be with or without considering the punctuations in the utterances.
    sentences = word2vec_prep.generate_sentences(filenames_, with_punctuations = with_punctuation)
    word2vec_prep.word2vec_make_model(sentences, with_punctuations = with_punctuation)

    pass

train_mode(with_punctuation= True)
train_mode(with_punctuation= False)