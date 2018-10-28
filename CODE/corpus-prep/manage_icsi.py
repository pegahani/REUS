"""
this code is for geenrating the original ICSI corpus from their supported XML version.
"""

import os
import random
import string
import xml.etree.ElementTree as ET

meeting_list = ['Bdb001'] + ['Bed00'+str(k) for k in range(2,10) if k != 7] +\
               ['Bed0'+str(k) for k in range(10,18) ]+\
               ['Bmr00' + str(j) for j in range(1,10) if j != 4]+['Bmr0' + str(j) for j in range(10,31) if j != 17]+\
               ['Bns00' + str(j) for j in range(1,4)]+\
               ['Bro00' + str(j) for j in range(3,10) if (j != 6 and j!= 9)]+['Bro0' + str(j) for j in range(10,29) if j != 20]+\
               ['Bsr001', 'Btr001', 'Btr002', 'Buw001']

class manage_meet_icsi:
    def __init__(self, corpus_name, which_part):

        self.corpus_name = corpus_name
        # There are two options: corpus or DA
        self.which_part = which_part

        self.file = None
        self.root_resources = None
        self.participants = None

    def initialization(self):
        if self.corpus_name == "ICSI":
            if self.which_part == 'corpus':
                self.file = "../../DATA/ICSI/ICSI_original_transcripts/transcripts/"
            elif self.which_part == 'DA':
                self.file = "../../DATA/ICSI/ICSI/DialogueActs/"
        pass

    def get_root(self, meet):

        schema = None

        if self.which_part == 'corpus':
            schema = self.file + meet + '.mrt'
        elif self.which_part == 'DA':
            schema = self.file + meet + '.dialogue-acts.xml'

        if self.file != None:
            if os.path.exists(schema):
                self.tree_resource = ET.parse(schema)
                self.root_resources = self.tree_resource.getroot()
                #self.participants = self.get_participants(self.root_resources)

    def get_participants(self, meet):

        schema = "../../DATA/ICSI/ICSI_original_transcripts/transcripts/"
        tree_resource = ET.parse(schema + meet + '.mrt')
        root_resources = tree_resource.getroot()

        participants_list = []
        participants = root_resources[0].getchildren()[-1].getchildren()
        for participant in participants:
            participants_list.append(participant.attrib['Name'])

        """assign A B C D .. to the participants names to make them coherent with AMI corpora"""
        alaphabetical_participants = {participants_list[i]: string.uppercase[i] for i in range(len(participants_list))}

        return alaphabetical_participants

    def generate_text(self, meet):

        generate_file = open('./ICSI_corpus/'+ meet+'.txt', 'w')
        self.get_root(meet)

        texts = self.root_resources[1].getchildren()

        for segment in texts:
            str = ''
            if segment.text not in [None, '\n']:
                str += segment.text.strip()
            children = segment.getchildren()
            if children != []:
                tempo = segment.getchildren()
                for child in tempo:
                    if child.text not in [None, '\n    ']:
                        str += child.text
                    last = child
                if (last.tail) is not None:
                    str += last.tail
            if str not in ['\n    ', None, ' ', '\n']:
                if str[-5:] == '\n    ':
                    if 'Participant' in segment.attrib:
                        generate_file.write(self.participants[segment.attrib['Participant']] + ' : ' + str[0:-5] + '\n')
                    else:
                        generate_file.write(random.choice(self.participants.values()) + ' : ' + str[0:-5] + '\n')

        return

    def get_sentence(self, xml_file, start_word, end_word):
        """
        a method for getting sentences from xml files including their words.
        :param xml_file:
        :param start_word:
        :param end_word:
        :return:
        """

        file_address = "../../DATA/ICSI/ICSI/Words/"+ xml_file
        str = ""

        start = start_word[3:-1]
        poiny_w_poin_index_for_start = start.find('.w.')
        start_number_real = int(start[poiny_w_poin_index_for_start + 3:].replace(',', ''))
        if 'disfmarker' in end_word:
            end = 'disfmarker'
        else:
            end = end_word[3:-1]

        tree_resource = ET.parse(file_address)
        root_resources = tree_resource.getroot()
        for word in root_resources.getchildren():

            if word.tag == 'w':
                word_complete = word.attrib['{http://nite.sourceforge.net/}id'][:len(start) + 1]
                poiny_w_poin_index = word_complete.find('.w.')
                start_number = int(word_complete[poiny_w_poin_index+3:].replace(',', ''))

                if start_number >= int(start_number_real):
                    str = str + ' '+ word.text

            if end == 'disfmarker':
                if end in word.attrib['{http://nite.sourceforge.net/}id']:
                    break
            else:
                if word.attrib['{http://nite.sourceforge.net/}id'][:len(end)+1] == end:
                    break

        return str

    def generate_DAs(self, meet, partcipants):
        """
        it gets phrases + their dialogue acts from the source XML files.
        :param meet: meeting name coming from meeting_list file.
        :return:
        """
        generate_file = open('./ICSI_DialogueActs/'+ meet+'.txt', 'w')

        self.get_root(meet)

        start_word = None
        end_word = None

        for child in self.root_resources.getchildren():
            tempo_child = child.getchildren()
            if  tempo_child != []:
                if 'href' in tempo_child[0].attrib:
                    words = tempo_child[0].attrib['href']
                    hashtag_index = words.find('#')
                    points_index = words.find('..')

                    xml_file = words[:hashtag_index]
                    if points_index == -1:
                        start_word = words[hashtag_index + 1:]
                        end_word = start_word
                    else:
                        start_word = words[hashtag_index+1:points_index]
                        end_word = words[points_index+2:]

                else:
                    xml_file = meet + '.words'

                sentence = self.get_sentence(xml_file, start_word, end_word)
                generate_file.write("dialogue type : " + child.attrib['original-type'] + '\n')
                generate_file.write(partcipants[child.attrib['participant']] + ' : ' + sentence + '\n\n')

        pass



if __name__ == '__main__':

    # print(meeting_list.index('Bmr011'))

    for meet in meeting_list[26:]:
        ex = manage_meet_icsi("ICSI", 'DA')
        ex.initialization()
        partcipants = ex.get_participants(meet)
        for parti in partcipants.values():
            mm = meet + '.' + parti
            print(mm)
            if os.path.exists('../../DATA/ICSI/ICSI/DialogueActs/' + mm + '.dialogue-acts.xml'):
                ex.generate_DAs(mm, partcipants)


