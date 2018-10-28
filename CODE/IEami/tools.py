import os
import re

scenario_based = ['meet_1', 'meet_2', 'meet_3', 'meet_4', 'meet_5', 'meet_6', 'meet_7', 'meet_8', 'meet_10', 'meet_11',
                  'meet_12', 'meet_13', 'meet_14', 'meet_15', 'meet_16', 'meet_17', 'meet_18', 'meet_19', 'meet_20',
                  'meet_21', 'meet_22', 'meet_23', 'meet_25', 'meet_26', 'meet_27', 'meet_28', 'meet_29', 'meet_30',
                  'meet_31', 'meet_32', 'meet_33', 'meet_34', 'meet_35', 'meet_36', 'meet_37', 'meet_38', 'meet_39',
                  'meet_40', 'meet_41', 'meet_42', 'meet_43', 'meet_44', 'meet_45', 'meet_46', 'meet_47', 'meet_48',
                  'meet_49', 'meet_50', 'meet_51', 'meet_51b', 'meet_52', 'meet_53', 'meet_54','meet_55', 'meet_56',
                  'meet_57', 'meet_58', 'meet_59', 'meet_60', 'meet_61', 'meet_62', 'meet_63', 'meet_64', 'meet_65',
                  'meet_66', 'meet_67', 'meet_68', 'meet_69', 'meet_70', 'meet_71', 'meet_72', 'meet_73', 'meet_74',
                  'meet_75', 'meet_76', 'meet_77', 'meet_78', 'meet_79', 'meet_80', 'meet_81', 'meet_82', 'meet_83',
                  'meet_84', 'meet_85', 'meet_86', 'meet_87', 'meet_88', 'meet_89', 'meet_90', 'meet_91', 'meet_92',
                  'meet_93', 'meet_94', 'meet_95', 'meet_96', 'meet_97', 'meet_98', 'meet_99', 'meet_112', 'meet_113',
                  'meet_114', 'meet_115', 'meet_116', 'meet_117', 'meet_118', 'meet_119', 'meet_120', 'meet_121',
                  'meet_122', 'meet_123', 'meet_124', 'meet_125', 'meet_126', 'meet_127', 'meet_128', 'meet_129',
                  'meet_130', 'meet_131', 'meet_132', 'meet_133', 'meet_134', 'meet_135', 'meet_136', 'meet_137',
                  'meet_138', 'meet_139', 'meet_140', 'meet_141', 'meet_142', 'meet_143', 'meet_144', 'meet_145',
                  'meet_146', 'meet_147', 'meet_148', 'meet_149', 'meet_150', 'meet_151']

non_scenario_based = ['meet_156', 'meet_157', 'meet_158', 'meet_159', 'meet_160', 'meet_161', 'meet_162', 'meet_163',
                      'meet_164', 'meet_165', 'meet_166', 'meet_167', 'meet_168', 'meet_169', 'meet_170', 'meet_171',
                      'meet_172', 'meet_188', 'meet_173', 'meet_174', 'meet_175', 'meet_176', 'meet_177', 'meet_178',
                      'meet_179', 'meet_180', 'meet_181', 'meet_182', 'meet_183', 'meet_184', 'meet_185', 'meet_186',
                      'meet_187']


classification_scenario_based = [['meet_1', 'meet_2', 'meet_3', 'meet_4'], ['meet_5', 'meet_6', 'meet_7', 'meet_8'], ['meet_10', 'meet_11',
                  'meet_12'], ['meet_13', 'meet_14', 'meet_15', 'meet_16'], ['meet_17', 'meet_18', 'meet_19', 'meet_20'],
                  ['meet_21', 'meet_22', 'meet_23'], ['meet_25', 'meet_26', 'meet_27', 'meet_28'], ['meet_29', 'meet_30',
                  'meet_31', 'meet_32'], ['meet_33', 'meet_34', 'meet_35', 'meet_36'], ['meet_37', 'meet_38', 'meet_39',
                  'meet_40'], ['meet_41', 'meet_42', 'meet_43', 'meet_44'], ['meet_45', 'meet_46', 'meet_47', 'meet_48'],
                  ['meet_49', 'meet_50', 'meet_51', 'meet_51b'], ['meet_52', 'meet_53', 'meet_54', 'meet_55'], ['meet_56',
                  'meet_57', 'meet_58', 'meet_59'], ['meet_60', 'meet_61', 'meet_62', 'meet_63'], ['meet_64', 'meet_65',
                  'meet_66', 'meet_67'], ['meet_68', 'meet_69', 'meet_70', 'meet_71'], ['meet_72', 'meet_73', 'meet_74',
                  'meet_75'], ['meet_76', 'meet_77', 'meet_78', 'meet_79'], ['meet_80', 'meet_81', 'meet_82', 'meet_83'],
                  ['meet_84', 'meet_85', 'meet_86', 'meet_87'], ['meet_88', 'meet_89', 'meet_90', 'meet_91'], ['meet_92',
                  'meet_93', 'meet_94', 'meet_95'], ['meet_96', 'meet_97', 'meet_98', 'meet_99'], ['meet_112', 'meet_113',
                  'meet_114', 'meet_115'], ['meet_116', 'meet_117', 'meet_118', 'meet_119'], ['meet_120', 'meet_121',
                  'meet_122', 'meet_123'], ['meet_124', 'meet_125', 'meet_126', 'meet_127'], ['meet_128', 'meet_129',
                  'meet_130', 'meet_131'], ['meet_132', 'meet_133', 'meet_134', 'meet_135'], ['meet_136', 'meet_137',
                  'meet_138', 'meet_139'], ['meet_140', 'meet_141', 'meet_142', 'meet_143'], ['meet_144', 'meet_145',
                  'meet_146', 'meet_147'], ['meet_148', 'meet_149', 'meet_150', 'meet_151']]



tokenize = lambda doc: [d for d in doc.lower().split(" ") if d != '']

def clean_line(data):

    data = data.replace('A : ', '')
    data = data.replace('B : ', '')
    data = data.replace('C : ', '')
    data = data.replace('D : ', '')

    data = re.sub(r'[^a-zA-Z0-9 ]',r'', data)

    return data

def text_to_string(input_file, is_resume_abstract = None, is_resume_extractive = None):  # meet_1

        data = ''

        if is_resume_extractive == None and is_resume_abstract == None:
            with open(input_file, 'r') as myfile:
                data = myfile.read().replace('\n', '')
                data = clean_line(data)

        if is_resume_abstract == True:
            with open(input_file, 'r') as myfile:
                data = myfile.read().replace('\n', ' ')

                data = data.replace('abstract : ', '')
                data = data.replace('actions : ', '')
                data = data.replace('decisions: ', '')
                data = data.replace('problems: ', '')

                data = clean_line(data)

        return data


path = os.getcwd() + '/' #'/IEami/'
adress = path + 'manual_corpus/'

all_scenario_based_documents = [text_to_string(adress + i + '.txt') for i in scenario_based]
all_nonscenario_based_documents = [text_to_string(adress + i + '.txt') for i in non_scenario_based]
