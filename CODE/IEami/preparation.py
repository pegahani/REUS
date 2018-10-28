import os

from TopicModeling_NMF import TM_NMF
from TopicModeling_LDA import TM_LDA
import tools
from evaluation import compare_with_AMI_results
from tf_idf import tf_idf_class

path = os.getcwd() + '/' #'+ '/IEami/'

classification_scenario_based = [['meet_1', 'meet_2', 'meet_3', 'meet_4'],
                                 ['meet_5', 'meet_6', 'meet_7', 'meet_8'],
                                 ['meet_10', 'meet_11', 'meet_12'],
                                 ['meet_13', 'meet_14', 'meet_15', 'meet_16'],
                                 ['meet_17', 'meet_18', 'meet_19', 'meet_20'],
                                 ['meet_21', 'meet_22', 'meet_23'],
                                 ['meet_25', 'meet_26', 'meet_27', 'meet_28'],
                                 ['meet_29', 'meet_30', 'meet_31', 'meet_32'],
                                 ['meet_33', 'meet_34', 'meet_35', 'meet_36'],
                                 ['meet_37', 'meet_38', 'meet_39','meet_40'],
                                 ['meet_41', 'meet_42', 'meet_43', 'meet_44'],
                                 ['meet_45', 'meet_46', 'meet_47', 'meet_48'],
                                 ['meet_49', 'meet_50', 'meet_51', 'meet_51b'],
                                 ['meet_52', 'meet_53', 'meet_54', 'meet_55'],
                                 ['meet_56', 'meet_57', 'meet_58', 'meet_59'],
                                 ['meet_60', 'meet_61', 'meet_62', 'meet_63'],
                                 ['meet_64', 'meet_65', 'meet_66', 'meet_67'],
                                 ['meet_68', 'meet_69', 'meet_70', 'meet_71'],
                                 ['meet_72', 'meet_73', 'meet_74', 'meet_75'],
                                 ['meet_76', 'meet_77', 'meet_78', 'meet_79'],
                                 ['meet_80', 'meet_81', 'meet_82', 'meet_83'],
                                 ['meet_84', 'meet_85', 'meet_86', 'meet_87'],
                                 ['meet_88', 'meet_89', 'meet_90', 'meet_91'],
                                 ['meet_92', 'meet_93', 'meet_94', 'meet_95'],
                                 ['meet_96', 'meet_97', 'meet_98', 'meet_99'],
                                 ['meet_112', 'meet_113', 'meet_114', 'meet_115'],
                                 ['meet_116', 'meet_117', 'meet_118', 'meet_119'],
                                 ['meet_120', 'meet_121', 'meet_122', 'meet_123'],
                                 ['meet_124', 'meet_125', 'meet_126', 'meet_127'],
                                 ['meet_128', 'meet_129', 'meet_130', 'meet_131'],
                                 ['meet_132', 'meet_133', 'meet_134', 'meet_135'],
                                 ['meet_136', 'meet_137', 'meet_138', 'meet_139'],
                                 ['meet_140', 'meet_141', 'meet_142', 'meet_143'],
                                 ['meet_144', 'meet_145', 'meet_146', 'meet_147'],
                                 ['meet_148', 'meet_149', 'meet_150', 'meet_151']]

def blocks_4_4_ami(n_words, length= None):
        """
        this function extracts the first
        :return:
        """
        file = open(path + 'result_ami/result_4_4.txt', 'w')
        adress = path + '/manual_corpus/'

        if length is None:
            for meet_list in classification_scenario_based:
                file.write('************************' + str(meet_list) + '*************************************\n')
                all_documents = [tools.text_to_string(adress + i + '.txt') for i in meet_list]
                example = tf_idf_class(all_documents)  # , document_0)
                tfidf_representation = example.tfidf()

                for meet in meet_list:
                    file.write(meet+ '\n')
                    file.write('*****************\n')

                    c = compare_with_AMI_results(meet)
                    c.get_resumes()

                    candidate = c.get_best_k_tfidf(n_words, tfidf_representation[meet_list.index(meet)])
                    file.write('candidate = ' + str(candidate)+ '\n')
                    file.flush()

                    bleu_measure = c.bleu_evaluation(candidate)

                    file.write('score_abstractive = ' + str(bleu_measure[0])+ '\n')
                    file.write('score_extractive = ' + str(bleu_measure[1])+ '\n')
                    file.flush()

                file.write('\n')
                file.flush()
        else:
            for meet_list in classification_scenario_based[0:length]:
                file.write('************************' + str(meet_list) + '*************************************\n')
                all_documents = [tools.text_to_string(adress + i + '.txt') for i in meet_list]
                example = tf_idf_class(all_documents)  # , document_0)
                tfidf_representation = example.tfidf(length)

                for meet in meet_list:
                    file.write(meet+ '\n')
                    file.write('*****************\n')

                    c = compare_with_AMI_results(meet)
                    c.get_resumes()

                    candidate = c.get_best_k_tfidf(n_words, tfidf_representation[meet_list.index(meet)])
                    file.write('candidate = ' + str(candidate)+ '\n')
                    file.flush()

                    bleu_measure = c.bleu_evaluation(candidate)

                    file.write('score_abstractive = ' + str(bleu_measure[0])+ '\n')
                    file.write('score_extractive = ' + str(bleu_measure[1])+ '\n')
                    file.flush()

                file.write('\n')
                file.flush()

        file.close()

        return

def blocks_ami(n_words, length = None):

    #print('we are inside')

    file = open(path + 'result_ami/result_4_block_scen.txt', 'w')
    adress_ = path + "manual_blocks/"
    meet_list = ["block_" + str(i + 1) for i in xrange(34)]

    all_documents = [tools.text_to_string(adress_ + i + '.txt') for i in meet_list]

    example = tf_idf_class(all_documents)

    counter = 0

    if length is None:
        tfidf_representation = example.tfidf()
        for meet in meet_list:

            #print '***********'
            #print 'meet', meet

            meet_block = classification_scenario_based[counter]

            file.write(str(meet_block) + '\n')
            file.write('*****************' + '\n')
            file.flush()

            c = compare_with_AMI_results(meet_block)
            c.get_resumes()

            candidate = c.get_best_k_tfidf(n_words, tfidf_representation[counter])
            file.write('candidate = ' + str(candidate) + '\n')
            file.flush()

            bleu_measure = c.bleu_evaluation(candidate)

            file.write('score_abstractive = ' + str(bleu_measure[0]) + '\n')
            file.write('score_extractive = ' + str(bleu_measure[1]) + '\n')
            file.write('\n')

            file.flush()

            counter += 1
    else:
        #print('length is not none')
        tfidf_representation = example.tfidf(length)
        for meet in meet_list[0:length]:
            #print '***********'
            #print 'meet', meet

            meet_block = classification_scenario_based[counter]

            file.write(str(meet_block) + '\n')
            file.write('*****************' + '\n')
            file.flush()

            c = compare_with_AMI_results(meet_block)
            c.get_resumes()

            candidate = c.get_best_k_tfidf(n_words, tfidf_representation[counter])
            file.write('candidate = ' + str(candidate) + '\n')
            file.flush()

            bleu_measure = c.bleu_evaluation(candidate)

            file.write('score_abstractive = ' + str(bleu_measure[0]) + '\n')
            file.write('score_extractive = ' + str(bleu_measure[1]) + '\n')
            file.write('\n')

            file.flush()

            counter += 1

    file.close()

def non_scenario_ami(n_words):
    file = open(path + 'result_ami/result_non_scen.txt', 'w')

    meet_list = tools.non_scenario_based

    file.write('************************' + str(meet_list) + '*************************************' + '\n')
    all_documents = tools.all_nonscenario_based_documents
    example = tf_idf_class(all_documents)
    tfidf_representation = example.tfidf()

    for meet in meet_list:
        file.write(meet + '\n')
        file.write('*****************' + '\n')

        c = compare_with_AMI_results(meet)
        c.get_resumes()

        candidate = c.get_best_k_tfidf(n_words, tfidf_representation[tools.non_scenario_based.index(meet)])
        file.write('candidate = ' + str(candidate) + '\n')

        bleu_measure = c.bleu_evaluation(candidate)

        file.write('score_abstractive = ' + str(bleu_measure[0]) + '\n')
        file.write('score_extractive = ' + str(bleu_measure[1]) + '\n')
        file.flush()

        file.write('\n')

        file.flush()

    file.close()

def lda_ami(n_topics, n_words, length=None):
    # 138 scenario-based meetings
    # 33 non-scenario-based meetings

    if length is None:
        meet_list = tools.scenario_based  # + tools.non_scenario_based
        all_documents = tools.all_scenario_based_documents  # + tools.all_nonscenario_based_documents

    else:

        meet_list = tools.scenario_based[0:length]  # + tools.non_scenario_based
        all_documents = tools.all_scenario_based_documents[0:length]  # + tools.all_nonscenario_based_documents

    lda_instance = TM_LDA(all_documents, num_topics=n_topics, passes=500, num_words=n_words)
    lda_instance.find_lda_topics()

    lda_instance.show_documenrs_vs_topics(meet_list=meet_list)

def nmf_blocks_ami(n_topics, n_words):

    adress_ = path + "manual_blocks/"
    meet_list = ["block_" + str(i + 1) for i in xrange(34)]
    all_documents = [adress_ + i + '.txt' for i in meet_list]

    nmf_instance = TM_NMF(all_documents, num_topics= n_topics , num_top_words= n_words, min_df=0, max_df= 50, isblock = True)
    nmf_instance.find_NMF_topics()
    nmf_instance.show_corpus_vs_topics()
    nmf_instance.show_topic_words()

def nmf_ami(n_topics, n_words):

    adress_ = path + "manual_corpus/"
    meet_list = tools.scenario_based
    all_documents = [adress_ + i + '.txt' for i in meet_list]

    nmf_instance = TM_NMF(all_documents, num_topics= n_topics , num_top_words= n_words, min_df=0, max_df= 50, isblock = False)
    nmf_instance.find_NMF_topics()
    nmf_instance.show_corpus_vs_topics()
    nmf_instance.show_topic_words()

if __name__ == '__main__':
    #print('inside main')
    blocks_ami(5, 1)