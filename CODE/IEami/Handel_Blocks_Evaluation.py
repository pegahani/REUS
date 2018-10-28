import tools
import tf_idf
from evaluation import compare_with_AMI_results

scenario_based_classes = tools.classification_scenario_based

# m1 = {}
# m2 = {}
# m3 = {}
# m4 = {}
#
# for index in range(len(scenario_based_classes)):
#     m1[index] = scenario_based_classes[index][0]
#     m2[index] = scenario_based_classes[index][1]
#     m3[index] = scenario_based_classes[index][2]
#     if len(scenario_based_classes[index]) < 4:
#         m4[index] = None
#     else:
#         m4[index] = scenario_based_classes[index][3]


m1 = {0: 'meet_1', 1: 'meet_5', 2: 'meet_10', 3: 'meet_13', 4: 'meet_17', 5: 'meet_21', 6: 'meet_25', 7: 'meet_29', 8: 'meet_33', 9: 'meet_37', 10: 'meet_41', 11: 'meet_45', 12: 'meet_49', 13: 'meet_52', 14: 'meet_56', 15: 'meet_60', 16: 'meet_64', 17: 'meet_68', 18: 'meet_72', 19: 'meet_76', 20: 'meet_80', 21: 'meet_84', 22: 'meet_88', 23: 'meet_92', 24: 'meet_96', 25: 'meet_112', 26: 'meet_116', 27: 'meet_120', 28: 'meet_124', 29: 'meet_128', 30: 'meet_132', 31: 'meet_136', 32: 'meet_140', 33: 'meet_144', 34: 'meet_148'}
m2 = {0: 'meet_2', 1: 'meet_6', 2: 'meet_11', 3: 'meet_14', 4: 'meet_18', 5: 'meet_22', 6: 'meet_26', 7: 'meet_30', 8: 'meet_34', 9: 'meet_38', 10: 'meet_42', 11: 'meet_46', 12: 'meet_50', 13: 'meet_53', 14: 'meet_57', 15: 'meet_61', 16: 'meet_65', 17: 'meet_69', 18: 'meet_73', 19: 'meet_77', 20: 'meet_81', 21: 'meet_85', 22: 'meet_89', 23: 'meet_93', 24: 'meet_97', 25: 'meet_113', 26: 'meet_117', 27: 'meet_121', 28: 'meet_125', 29: 'meet_129', 30: 'meet_133', 31: 'meet_137', 32: 'meet_141', 33: 'meet_145', 34: 'meet_149'}
m3 = {0: 'meet_3', 1: 'meet_7', 2: 'meet_12', 3: 'meet_15', 4: 'meet_19', 5: 'meet_23', 6: 'meet_27', 7: 'meet_31', 8: 'meet_35', 9: 'meet_39', 10: 'meet_43', 11: 'meet_47', 12: 'meet_51', 13: 'meet_54', 14: 'meet_58', 15: 'meet_62', 16: 'meet_66', 17: 'meet_70', 18: 'meet_74', 19: 'meet_78', 20: 'meet_82', 21: 'meet_86', 22: 'meet_90', 23: 'meet_94', 24: 'meet_98', 25: 'meet_114', 26: 'meet_118', 27: 'meet_122', 28: 'meet_126', 29: 'meet_130', 30: 'meet_134', 31: 'meet_138', 32: 'meet_142', 33: 'meet_146', 34: 'meet_150'}
m4 = {0: 'meet_4', 1: 'meet_8', 2: None,      3: 'meet_16', 4: 'meet_20', 5: None,      6: 'meet_28', 7: 'meet_32', 8: 'meet_36', 9: 'meet_40', 10: 'meet_44', 11: 'meet_48', 12: 'meet_51b', 13: 'meet_55', 14: 'meet_59', 15: 'meet_63', 16: 'meet_67', 17: 'meet_71', 18: 'meet_75', 19: 'meet_79', 20: 'meet_83', 21: 'meet_87', 22: 'meet_91', 23: 'meet_95', 24: 'meet_99', 25: 'meet_115', 26: 'meet_119', 27: 'meet_123', 28: 'meet_127', 29: 'meet_131', 30: 'meet_135', 31: 'meet_139', 32: 'meet_143', 33: 'meet_147', 34: 'meet_151'}



# file = open('./result_huge_blocks_tf_idf.txt', 'w')
#
# meet_list = ["huge_"+str(i+1) for i in xrange(4)]
#
# adress_ = "./manual_huge_blocks/"
# all_documents = [tools.text_to_string(adress_ + i + '.txt') for i in meet_list]
#
# example = tf_idf.tf_idf_class(all_documents)
# tfidf_representation = example.tfidf()
#
# file.write('this file includes the tf-idf scores for 4 huge meeting blocks'+
#            '\n' +'The huge block1 contains all first meetings duing the day, the huge block2 contains all the second meetings during the day and so on ' +'\n')
#
# for meet in meet_list:
#
#     c = compare_with_AMI_results(meet)
#     candidate = c.get_best_k_tfidf(50, tfidf_representation[meet_list.index(meet)])
#     file.write('candidate = ' + str(candidate) + '\n')
#
#     file.flush()
#
# file.close()


file = open('./result/Row_results/result_relative_1.txt', 'w')
adress_ = "./manuel_corpus/"


file.write('this file includes the tf-idf scores for 138 scenario-based meetings'+
           '\n' +'For each meeting, the tf-idf scores are computed by comparing this meeting w.r.t other scenario-based '+ '\n'+
                 'meetings esxcept the meetins with the same order in their bloks.' +'\n')

all_documents_group_1 = [tools.text_to_string(adress_ + i + '.txt') for i in m1.itervalues()]
all_documents_group_2 = [tools.text_to_string(adress_ + i + '.txt') for i in m2.itervalues()]
all_documents_group_3 = [tools.text_to_string(adress_ + i + '.txt') for i in m3.itervalues()]
all_documents_group_4 = [tools.text_to_string(adress_ + i + '.txt') for i in m4.itervalues() if i is not None]


all_documents__1 = all_documents_group_2 + all_documents_group_3 + all_documents_group_4
all_documents__2 = all_documents_group_1 + all_documents_group_3 + all_documents_group_4
all_documents__3 = all_documents_group_2 + all_documents_group_1 + all_documents_group_4
all_documents__4 = all_documents_group_2 + all_documents_group_3 + all_documents_group_1

all_of_all_documents = [all_documents__1, all_documents__2, all_documents__3, all_documents__4]
all_of_all_meetings = [m1, m2, m3, m4]

length = len(m1)

for i in range(0,7):

    file.write('************************' + str([all_of_all_meetings[j][i] for j in range(4)]) + '*************************************\n')

    for j in range(4):

        _meet = all_of_all_meetings[j][i]

        if _meet != None:

            file.write(_meet + '\n')
            file.write('*****************' + '\n')

            doc = tools.text_to_string(adress_ + _meet + '.txt')

            tempo = all_of_all_documents[j] + [doc]
            example = tf_idf.tf_idf_class(tempo)
            idf = example.prep_idf()

            meet = tools.tokenize(doc)
            tfidf = example.tfidf_relative(meet, idf)

            c = compare_with_AMI_results(meet)
            candidate = c.get_best_k_tfidf(50, tfidf)
            file.write('candidate = ' + str(candidate) + '\n')

            file.flush()

        file.flush()

file.close()