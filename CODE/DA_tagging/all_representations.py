
"""it genrates list of DA taggs from ../corpus-prep/ICSI_DialogueActs"""
# TODO: I removed bed009.C.txt and bed016.B.txt from the DA_icsi list. because for I do not know which reason, the code not generate their represent vectos properly! may be because they include a few number of utterances.
import collections
import os

from text_to_vector import adress_resume_ami

DA_icsi_list = ['../corpus-prep/ICSI_DialogueActs/Bdb001.A.txt', '../corpus-prep/ICSI_DialogueActs/Bdb001.B.txt', '../corpus-prep/ICSI_DialogueActs/Bdb001.C.txt', '../corpus-prep/ICSI_DialogueActs/Bdb001.D.txt', '../corpus-prep/ICSI_DialogueActs/Bdb001.E.txt', '../corpus-prep/ICSI_DialogueActs/Bdb001.F.txt', '../corpus-prep/ICSI_DialogueActs/Bed002.A.txt', '../corpus-prep/ICSI_DialogueActs/Bed002.B.txt', '../corpus-prep/ICSI_DialogueActs/Bed002.C.txt', '../corpus-prep/ICSI_DialogueActs/Bed002.D.txt', '../corpus-prep/ICSI_DialogueActs/Bed002.E.txt', '../corpus-prep/ICSI_DialogueActs/Bed002.F.txt', '../corpus-prep/ICSI_DialogueActs/Bed003.A.txt', '../corpus-prep/ICSI_DialogueActs/Bed003.B.txt', '../corpus-prep/ICSI_DialogueActs/Bed003.C.txt', '../corpus-prep/ICSI_DialogueActs/Bed003.D.txt', '../corpus-prep/ICSI_DialogueActs/Bed004.A.txt', '../corpus-prep/ICSI_DialogueActs/Bed004.B.txt', '../corpus-prep/ICSI_DialogueActs/Bed004.C.txt', '../corpus-prep/ICSI_DialogueActs/Bed004.D.txt', '../corpus-prep/ICSI_DialogueActs/Bed005.A.txt', '../corpus-prep/ICSI_DialogueActs/Bed005.B.txt', '../corpus-prep/ICSI_DialogueActs/Bed005.C.txt', '../corpus-prep/ICSI_DialogueActs/Bed005.D.txt', '../corpus-prep/ICSI_DialogueActs/Bed005.E.txt', '../corpus-prep/ICSI_DialogueActs/Bed005.F.txt', '../corpus-prep/ICSI_DialogueActs/Bed006.A.txt', '../corpus-prep/ICSI_DialogueActs/Bed006.B.txt', '../corpus-prep/ICSI_DialogueActs/Bed006.C.txt', '../corpus-prep/ICSI_DialogueActs/Bed006.D.txt', '../corpus-prep/ICSI_DialogueActs/Bed006.E.txt', '../corpus-prep/ICSI_DialogueActs/Bed006.F.txt', '../corpus-prep/ICSI_DialogueActs/Bed006.G.txt', '../corpus-prep/ICSI_DialogueActs/Bed008.A.txt', '../corpus-prep/ICSI_DialogueActs/Bed008.B.txt', '../corpus-prep/ICSI_DialogueActs/Bed008.C.txt', '../corpus-prep/ICSI_DialogueActs/Bed008.D.txt', '../corpus-prep/ICSI_DialogueActs/Bed008.E.txt', '../corpus-prep/ICSI_DialogueActs/Bed009.A.txt', '../corpus-prep/ICSI_DialogueActs/Bed009.B.txt', '../corpus-prep/ICSI_DialogueActs/Bed009.D.txt', '../corpus-prep/ICSI_DialogueActs/Bed009.E.txt', '../corpus-prep/ICSI_DialogueActs/Bed009.F.txt', '../corpus-prep/ICSI_DialogueActs/Bed009.G.txt', '../corpus-prep/ICSI_DialogueActs/Bed010.A.txt', '../corpus-prep/ICSI_DialogueActs/Bed010.B.txt', '../corpus-prep/ICSI_DialogueActs/Bed010.C.txt', '../corpus-prep/ICSI_DialogueActs/Bed010.D.txt', '../corpus-prep/ICSI_DialogueActs/Bed010.E.txt', '../corpus-prep/ICSI_DialogueActs/Bed010.F.txt', '../corpus-prep/ICSI_DialogueActs/Bed010.G.txt', '../corpus-prep/ICSI_DialogueActs/Bed011.A.txt', '../corpus-prep/ICSI_DialogueActs/Bed011.B.txt', '../corpus-prep/ICSI_DialogueActs/Bed011.C.txt', '../corpus-prep/ICSI_DialogueActs/Bed011.D.txt', '../corpus-prep/ICSI_DialogueActs/Bed011.E.txt', '../corpus-prep/ICSI_DialogueActs/Bed011.F.txt', '../corpus-prep/ICSI_DialogueActs/Bed011.G.txt', '../corpus-prep/ICSI_DialogueActs/Bed012.A.txt', '../corpus-prep/ICSI_DialogueActs/Bed012.B.txt', '../corpus-prep/ICSI_DialogueActs/Bed012.C.txt', '../corpus-prep/ICSI_DialogueActs/Bed012.D.txt', '../corpus-prep/ICSI_DialogueActs/Bed013.A.txt', '../corpus-prep/ICSI_DialogueActs/Bed013.B.txt', '../corpus-prep/ICSI_DialogueActs/Bed013.C.txt', '../corpus-prep/ICSI_DialogueActs/Bed013.D.txt', '../corpus-prep/ICSI_DialogueActs/Bed013.E.txt', '../corpus-prep/ICSI_DialogueActs/Bed014.A.txt', '../corpus-prep/ICSI_DialogueActs/Bed014.B.txt', '../corpus-prep/ICSI_DialogueActs/Bed014.C.txt', '../corpus-prep/ICSI_DialogueActs/Bed014.D.txt', '../corpus-prep/ICSI_DialogueActs/Bed014.E.txt', '../corpus-prep/ICSI_DialogueActs/Bed014.F.txt', '../corpus-prep/ICSI_DialogueActs/Bed015.A.txt', '../corpus-prep/ICSI_DialogueActs/Bed015.B.txt', '../corpus-prep/ICSI_DialogueActs/Bed015.C.txt', '../corpus-prep/ICSI_DialogueActs/Bed015.D.txt', '../corpus-prep/ICSI_DialogueActs/Bed015.E.txt', '../corpus-prep/ICSI_DialogueActs/Bed015.F.txt', '../corpus-prep/ICSI_DialogueActs/Bed016.A.txt', '../corpus-prep/ICSI_DialogueActs/Bed016.C.txt', '../corpus-prep/ICSI_DialogueActs/Bed016.D.txt', '../corpus-prep/ICSI_DialogueActs/Bed016.E.txt', '../corpus-prep/ICSI_DialogueActs/Bed016.F.txt', '../corpus-prep/ICSI_DialogueActs/Bed016.G.txt', '../corpus-prep/ICSI_DialogueActs/Bed016.H.txt', '../corpus-prep/ICSI_DialogueActs/Bed016.I.txt', '../corpus-prep/ICSI_DialogueActs/Bed016.J.txt', '../corpus-prep/ICSI_DialogueActs/Bed017.A.txt', '../corpus-prep/ICSI_DialogueActs/Bed017.B.txt', '../corpus-prep/ICSI_DialogueActs/Bed017.C.txt', '../corpus-prep/ICSI_DialogueActs/Bed017.D.txt', '../corpus-prep/ICSI_DialogueActs/Bed017.E.txt', '../corpus-prep/ICSI_DialogueActs/Bed017.F.txt', '../corpus-prep/ICSI_DialogueActs/Bmr001.A.txt', '../corpus-prep/ICSI_DialogueActs/Bmr001.B.txt', '../corpus-prep/ICSI_DialogueActs/Bmr001.C.txt', '../corpus-prep/ICSI_DialogueActs/Bmr002.A.txt', '../corpus-prep/ICSI_DialogueActs/Bmr002.B.txt', '../corpus-prep/ICSI_DialogueActs/Bmr002.C.txt', '../corpus-prep/ICSI_DialogueActs/Bmr002.D.txt', '../corpus-prep/ICSI_DialogueActs/Bmr003.A.txt', '../corpus-prep/ICSI_DialogueActs/Bmr003.B.txt', '../corpus-prep/ICSI_DialogueActs/Bmr003.C.txt', '../corpus-prep/ICSI_DialogueActs/Bmr003.D.txt', '../corpus-prep/ICSI_DialogueActs/Bmr003.E.txt', '../corpus-prep/ICSI_DialogueActs/Bmr003.F.txt', '../corpus-prep/ICSI_DialogueActs/Bmr005.A.txt', '../corpus-prep/ICSI_DialogueActs/Bmr005.B.txt', '../corpus-prep/ICSI_DialogueActs/Bmr005.C.txt', '../corpus-prep/ICSI_DialogueActs/Bmr005.D.txt', '../corpus-prep/ICSI_DialogueActs/Bmr005.E.txt', '../corpus-prep/ICSI_DialogueActs/Bmr005.F.txt', '../corpus-prep/ICSI_DialogueActs/Bmr005.G.txt', '../corpus-prep/ICSI_DialogueActs/Bmr005.H.txt', '../corpus-prep/ICSI_DialogueActs/Bmr006.A.txt', '../corpus-prep/ICSI_DialogueActs/Bmr006.B.txt', '../corpus-prep/ICSI_DialogueActs/Bmr006.C.txt', '../corpus-prep/ICSI_DialogueActs/Bmr006.D.txt', '../corpus-prep/ICSI_DialogueActs/Bmr006.E.txt', '../corpus-prep/ICSI_DialogueActs/Bmr006.F.txt', '../corpus-prep/ICSI_DialogueActs/Bmr007.A.txt', '../corpus-prep/ICSI_DialogueActs/Bmr007.B.txt', '../corpus-prep/ICSI_DialogueActs/Bmr007.C.txt', '../corpus-prep/ICSI_DialogueActs/Bmr007.D.txt', '../corpus-prep/ICSI_DialogueActs/Bmr007.E.txt', '../corpus-prep/ICSI_DialogueActs/Bmr007.F.txt', '../corpus-prep/ICSI_DialogueActs/Bmr007.G.txt', '../corpus-prep/ICSI_DialogueActs/Bmr007.H.txt', '../corpus-prep/ICSI_DialogueActs/Bmr008.A.txt', '../corpus-prep/ICSI_DialogueActs/Bmr008.B.txt', '../corpus-prep/ICSI_DialogueActs/Bmr008.C.txt', '../corpus-prep/ICSI_DialogueActs/Bmr008.D.txt', '../corpus-prep/ICSI_DialogueActs/Bmr008.E.txt', '../corpus-prep/ICSI_DialogueActs/Bmr008.F.txt', '../corpus-prep/ICSI_DialogueActs/Bmr009.A.txt', '../corpus-prep/ICSI_DialogueActs/Bmr009.B.txt', '../corpus-prep/ICSI_DialogueActs/Bmr009.C.txt', '../corpus-prep/ICSI_DialogueActs/Bmr009.D.txt', '../corpus-prep/ICSI_DialogueActs/Bmr009.E.txt', '../corpus-prep/ICSI_DialogueActs/Bmr010.A.txt', '../corpus-prep/ICSI_DialogueActs/Bmr010.B.txt', '../corpus-prep/ICSI_DialogueActs/Bmr010.C.txt', '../corpus-prep/ICSI_DialogueActs/Bmr010.D.txt', '../corpus-prep/ICSI_DialogueActs/Bmr010.E.txt', '../corpus-prep/ICSI_DialogueActs/Bmr010.F.txt', '../corpus-prep/ICSI_DialogueActs/Bmr010.G.txt', '../corpus-prep/ICSI_DialogueActs/Bmr010.H.txt', '../corpus-prep/ICSI_DialogueActs/Bmr011.A.txt', '../corpus-prep/ICSI_DialogueActs/Bmr011.B.txt', '../corpus-prep/ICSI_DialogueActs/Bmr011.C.txt', '../corpus-prep/ICSI_DialogueActs/Bmr011.D.txt', '../corpus-prep/ICSI_DialogueActs/Bmr011.E.txt', '../corpus-prep/ICSI_DialogueActs/Bmr011.F.txt', '../corpus-prep/ICSI_DialogueActs/Bmr011.G.txt', '../corpus-prep/ICSI_DialogueActs/Bmr011.H.txt', '../corpus-prep/ICSI_DialogueActs/Bmr012.A.txt', '../corpus-prep/ICSI_DialogueActs/Bmr012.B.txt', '../corpus-prep/ICSI_DialogueActs/Bmr012.C.txt', '../corpus-prep/ICSI_DialogueActs/Bmr012.D.txt', '../corpus-prep/ICSI_DialogueActs/Bmr012.E.txt', '../corpus-prep/ICSI_DialogueActs/Bmr012.F.txt', '../corpus-prep/ICSI_DialogueActs/Bmr012.G.txt', '../corpus-prep/ICSI_DialogueActs/Bmr012.H.txt', '../corpus-prep/ICSI_DialogueActs/Bmr012.J.txt', '../corpus-prep/ICSI_DialogueActs/Bmr013.A.txt', '../corpus-prep/ICSI_DialogueActs/Bmr013.B.txt', '../corpus-prep/ICSI_DialogueActs/Bmr013.C.txt', '../corpus-prep/ICSI_DialogueActs/Bmr013.D.txt', '../corpus-prep/ICSI_DialogueActs/Bmr013.E.txt', '../corpus-prep/ICSI_DialogueActs/Bmr013.F.txt', '../corpus-prep/ICSI_DialogueActs/Bmr013.G.txt', '../corpus-prep/ICSI_DialogueActs/Bmr014.A.txt', '../corpus-prep/ICSI_DialogueActs/Bmr014.B.txt', '../corpus-prep/ICSI_DialogueActs/Bmr014.C.txt', '../corpus-prep/ICSI_DialogueActs/Bmr014.D.txt', '../corpus-prep/ICSI_DialogueActs/Bmr014.E.txt', '../corpus-prep/ICSI_DialogueActs/Bmr014.F.txt', '../corpus-prep/ICSI_DialogueActs/Bmr015.A.txt', '../corpus-prep/ICSI_DialogueActs/Bmr015.B.txt', '../corpus-prep/ICSI_DialogueActs/Bmr015.C.txt', '../corpus-prep/ICSI_DialogueActs/Bmr015.D.txt', '../corpus-prep/ICSI_DialogueActs/Bmr015.E.txt', '../corpus-prep/ICSI_DialogueActs/Bmr015.F.txt', '../corpus-prep/ICSI_DialogueActs/Bmr015.G.txt', '../corpus-prep/ICSI_DialogueActs/Bmr016.A.txt', '../corpus-prep/ICSI_DialogueActs/Bmr016.B.txt', '../corpus-prep/ICSI_DialogueActs/Bmr016.C.txt', '../corpus-prep/ICSI_DialogueActs/Bmr016.D.txt', '../corpus-prep/ICSI_DialogueActs/Bmr016.E.txt', '../corpus-prep/ICSI_DialogueActs/Bmr016.F.txt', '../corpus-prep/ICSI_DialogueActs/Bmr016.G.txt', '../corpus-prep/ICSI_DialogueActs/Bmr018.A.txt', '../corpus-prep/ICSI_DialogueActs/Bmr018.B.txt', '../corpus-prep/ICSI_DialogueActs/Bmr018.C.txt', '../corpus-prep/ICSI_DialogueActs/Bmr018.D.txt', '../corpus-prep/ICSI_DialogueActs/Bmr018.E.txt', '../corpus-prep/ICSI_DialogueActs/Bmr018.F.txt', '../corpus-prep/ICSI_DialogueActs/Bmr018.G.txt', '../corpus-prep/ICSI_DialogueActs/Bmr019.A.txt', '../corpus-prep/ICSI_DialogueActs/Bmr019.B.txt', '../corpus-prep/ICSI_DialogueActs/Bmr019.C.txt', '../corpus-prep/ICSI_DialogueActs/Bmr019.D.txt', '../corpus-prep/ICSI_DialogueActs/Bmr019.E.txt', '../corpus-prep/ICSI_DialogueActs/Bmr019.F.txt', '../corpus-prep/ICSI_DialogueActs/Bmr019.G.txt', '../corpus-prep/ICSI_DialogueActs/Bmr019.H.txt', '../corpus-prep/ICSI_DialogueActs/Bmr019.I.txt', '../corpus-prep/ICSI_DialogueActs/Bmr020.A.txt', '../corpus-prep/ICSI_DialogueActs/Bmr020.B.txt', '../corpus-prep/ICSI_DialogueActs/Bmr020.C.txt', '../corpus-prep/ICSI_DialogueActs/Bmr020.D.txt', '../corpus-prep/ICSI_DialogueActs/Bmr020.E.txt', '../corpus-prep/ICSI_DialogueActs/Bmr020.F.txt', '../corpus-prep/ICSI_DialogueActs/Bmr020.G.txt', '../corpus-prep/ICSI_DialogueActs/Bmr021.A.txt', '../corpus-prep/ICSI_DialogueActs/Bmr021.B.txt', '../corpus-prep/ICSI_DialogueActs/Bmr021.C.txt', '../corpus-prep/ICSI_DialogueActs/Bmr021.D.txt', '../corpus-prep/ICSI_DialogueActs/Bmr021.E.txt', '../corpus-prep/ICSI_DialogueActs/Bmr021.F.txt', '../corpus-prep/ICSI_DialogueActs/Bmr022.A.txt', '../corpus-prep/ICSI_DialogueActs/Bmr022.B.txt', '../corpus-prep/ICSI_DialogueActs/Bmr022.C.txt', '../corpus-prep/ICSI_DialogueActs/Bmr022.D.txt', '../corpus-prep/ICSI_DialogueActs/Bmr022.E.txt', '../corpus-prep/ICSI_DialogueActs/Bmr022.F.txt', '../corpus-prep/ICSI_DialogueActs/Bmr023.A.txt', '../corpus-prep/ICSI_DialogueActs/Bmr023.B.txt', '../corpus-prep/ICSI_DialogueActs/Bmr023.C.txt', '../corpus-prep/ICSI_DialogueActs/Bmr023.D.txt', '../corpus-prep/ICSI_DialogueActs/Bmr023.E.txt', '../corpus-prep/ICSI_DialogueActs/Bmr023.F.txt', '../corpus-prep/ICSI_DialogueActs/Bmr023.G.txt', '../corpus-prep/ICSI_DialogueActs/Bmr024.A.txt', '../corpus-prep/ICSI_DialogueActs/Bmr024.B.txt', '../corpus-prep/ICSI_DialogueActs/Bmr024.C.txt', '../corpus-prep/ICSI_DialogueActs/Bmr024.D.txt', '../corpus-prep/ICSI_DialogueActs/Bmr024.E.txt', '../corpus-prep/ICSI_DialogueActs/Bmr024.F.txt', '../corpus-prep/ICSI_DialogueActs/Bmr024.G.txt', '../corpus-prep/ICSI_DialogueActs/Bmr024.H.txt', '../corpus-prep/ICSI_DialogueActs/Bmr024.I.txt', '../corpus-prep/ICSI_DialogueActs/Bmr025.A.txt', '../corpus-prep/ICSI_DialogueActs/Bmr025.B.txt', '../corpus-prep/ICSI_DialogueActs/Bmr025.C.txt', '../corpus-prep/ICSI_DialogueActs/Bmr025.D.txt', '../corpus-prep/ICSI_DialogueActs/Bmr025.E.txt', '../corpus-prep/ICSI_DialogueActs/Bmr025.F.txt', '../corpus-prep/ICSI_DialogueActs/Bmr025.G.txt', '../corpus-prep/ICSI_DialogueActs/Bmr025.H.txt', '../corpus-prep/ICSI_DialogueActs/Bmr026.A.txt', '../corpus-prep/ICSI_DialogueActs/Bmr026.B.txt', '../corpus-prep/ICSI_DialogueActs/Bmr026.C.txt', '../corpus-prep/ICSI_DialogueActs/Bmr026.D.txt', '../corpus-prep/ICSI_DialogueActs/Bmr026.E.txt', '../corpus-prep/ICSI_DialogueActs/Bmr026.F.txt', '../corpus-prep/ICSI_DialogueActs/Bmr027.A.txt', '../corpus-prep/ICSI_DialogueActs/Bmr027.B.txt', '../corpus-prep/ICSI_DialogueActs/Bmr027.C.txt', '../corpus-prep/ICSI_DialogueActs/Bmr027.D.txt', '../corpus-prep/ICSI_DialogueActs/Bmr027.E.txt', '../corpus-prep/ICSI_DialogueActs/Bmr027.F.txt', '../corpus-prep/ICSI_DialogueActs/Bmr027.G.txt', '../corpus-prep/ICSI_DialogueActs/Bmr027.H.txt', '../corpus-prep/ICSI_DialogueActs/Bmr028.A.txt', '../corpus-prep/ICSI_DialogueActs/Bmr028.B.txt', '../corpus-prep/ICSI_DialogueActs/Bmr028.C.txt', '../corpus-prep/ICSI_DialogueActs/Bmr028.D.txt', '../corpus-prep/ICSI_DialogueActs/Bmr028.E.txt', '../corpus-prep/ICSI_DialogueActs/Bmr028.F.txt', '../corpus-prep/ICSI_DialogueActs/Bmr028.H.txt', '../corpus-prep/ICSI_DialogueActs/Bmr028.I.txt', '../corpus-prep/ICSI_DialogueActs/Bmr029.A.txt', '../corpus-prep/ICSI_DialogueActs/Bmr029.B.txt', '../corpus-prep/ICSI_DialogueActs/Bmr029.C.txt', '../corpus-prep/ICSI_DialogueActs/Bmr029.E.txt', '../corpus-prep/ICSI_DialogueActs/Bmr029.F.txt', '../corpus-prep/ICSI_DialogueActs/Bmr030.A.txt', '../corpus-prep/ICSI_DialogueActs/Bmr030.B.txt', '../corpus-prep/ICSI_DialogueActs/Bmr030.C.txt', '../corpus-prep/ICSI_DialogueActs/Bmr030.D.txt', '../corpus-prep/ICSI_DialogueActs/Bmr030.E.txt', '../corpus-prep/ICSI_DialogueActs/Bns001.A.txt', '../corpus-prep/ICSI_DialogueActs/Bns001.B.txt', '../corpus-prep/ICSI_DialogueActs/Bns001.C.txt', '../corpus-prep/ICSI_DialogueActs/Bns001.D.txt', '../corpus-prep/ICSI_DialogueActs/Bns001.E.txt', '../corpus-prep/ICSI_DialogueActs/Bns001.F.txt', '../corpus-prep/ICSI_DialogueActs/Bns001.G.txt', '../corpus-prep/ICSI_DialogueActs/Bns002.A.txt', '../corpus-prep/ICSI_DialogueActs/Bns002.B.txt', '../corpus-prep/ICSI_DialogueActs/Bns002.C.txt', '../corpus-prep/ICSI_DialogueActs/Bns002.D.txt', '../corpus-prep/ICSI_DialogueActs/Bns002.E.txt', '../corpus-prep/ICSI_DialogueActs/Bns003.A.txt', '../corpus-prep/ICSI_DialogueActs/Bns003.B.txt', '../corpus-prep/ICSI_DialogueActs/Bns003.C.txt', '../corpus-prep/ICSI_DialogueActs/Bns003.D.txt', '../corpus-prep/ICSI_DialogueActs/Bns003.E.txt', '../corpus-prep/ICSI_DialogueActs/Bns003.F.txt', '../corpus-prep/ICSI_DialogueActs/Bro003.A.txt', '../corpus-prep/ICSI_DialogueActs/Bro003.B.txt', '../corpus-prep/ICSI_DialogueActs/Bro003.C.txt', '../corpus-prep/ICSI_DialogueActs/Bro003.D.txt', '../corpus-prep/ICSI_DialogueActs/Bro003.E.txt', '../corpus-prep/ICSI_DialogueActs/Bro003.F.txt', '../corpus-prep/ICSI_DialogueActs/Bro003.G.txt', '../corpus-prep/ICSI_DialogueActs/Bro004.A.txt', '../corpus-prep/ICSI_DialogueActs/Bro004.B.txt', '../corpus-prep/ICSI_DialogueActs/Bro004.C.txt', '../corpus-prep/ICSI_DialogueActs/Bro004.D.txt', '../corpus-prep/ICSI_DialogueActs/Bro004.E.txt', '../corpus-prep/ICSI_DialogueActs/Bro004.F.txt', '../corpus-prep/ICSI_DialogueActs/Bro004.G.txt', '../corpus-prep/ICSI_DialogueActs/Bro005.A.txt', '../corpus-prep/ICSI_DialogueActs/Bro005.B.txt', '../corpus-prep/ICSI_DialogueActs/Bro005.C.txt', '../corpus-prep/ICSI_DialogueActs/Bro005.D.txt', '../corpus-prep/ICSI_DialogueActs/Bro005.E.txt', '../corpus-prep/ICSI_DialogueActs/Bro007.A.txt', '../corpus-prep/ICSI_DialogueActs/Bro007.B.txt', '../corpus-prep/ICSI_DialogueActs/Bro007.C.txt', '../corpus-prep/ICSI_DialogueActs/Bro007.D.txt', '../corpus-prep/ICSI_DialogueActs/Bro008.A.txt', '../corpus-prep/ICSI_DialogueActs/Bro008.B.txt', '../corpus-prep/ICSI_DialogueActs/Bro008.C.txt', '../corpus-prep/ICSI_DialogueActs/Bro008.D.txt', '../corpus-prep/ICSI_DialogueActs/Bro008.E.txt', '../corpus-prep/ICSI_DialogueActs/Bro010.A.txt', '../corpus-prep/ICSI_DialogueActs/Bro010.B.txt', '../corpus-prep/ICSI_DialogueActs/Bro010.C.txt', '../corpus-prep/ICSI_DialogueActs/Bro010.D.txt', '../corpus-prep/ICSI_DialogueActs/Bro010.E.txt', '../corpus-prep/ICSI_DialogueActs/Bro010.F.txt', '../corpus-prep/ICSI_DialogueActs/Bro011.A.txt', '../corpus-prep/ICSI_DialogueActs/Bro011.B.txt', '../corpus-prep/ICSI_DialogueActs/Bro011.C.txt', '../corpus-prep/ICSI_DialogueActs/Bro011.D.txt', '../corpus-prep/ICSI_DialogueActs/Bro011.E.txt', '../corpus-prep/ICSI_DialogueActs/Bro011.F.txt', '../corpus-prep/ICSI_DialogueActs/Bro012.A.txt', '../corpus-prep/ICSI_DialogueActs/Bro012.B.txt', '../corpus-prep/ICSI_DialogueActs/Bro012.C.txt', '../corpus-prep/ICSI_DialogueActs/Bro012.D.txt', '../corpus-prep/ICSI_DialogueActs/Bro012.E.txt', '../corpus-prep/ICSI_DialogueActs/Bro012.F.txt', '../corpus-prep/ICSI_DialogueActs/Bro013.A.txt', '../corpus-prep/ICSI_DialogueActs/Bro013.B.txt', '../corpus-prep/ICSI_DialogueActs/Bro013.C.txt', '../corpus-prep/ICSI_DialogueActs/Bro013.D.txt', '../corpus-prep/ICSI_DialogueActs/Bro013.E.txt', '../corpus-prep/ICSI_DialogueActs/Bro014.A.txt', '../corpus-prep/ICSI_DialogueActs/Bro014.B.txt', '../corpus-prep/ICSI_DialogueActs/Bro014.C.txt', '../corpus-prep/ICSI_DialogueActs/Bro014.D.txt', '../corpus-prep/ICSI_DialogueActs/Bro014.E.txt', '../corpus-prep/ICSI_DialogueActs/Bro014.F.txt', '../corpus-prep/ICSI_DialogueActs/Bro015.A.txt', '../corpus-prep/ICSI_DialogueActs/Bro015.B.txt', '../corpus-prep/ICSI_DialogueActs/Bro015.C.txt', '../corpus-prep/ICSI_DialogueActs/Bro015.D.txt', '../corpus-prep/ICSI_DialogueActs/Bro015.E.txt', '../corpus-prep/ICSI_DialogueActs/Bro015.F.txt', '../corpus-prep/ICSI_DialogueActs/Bro016.A.txt', '../corpus-prep/ICSI_DialogueActs/Bro016.B.txt', '../corpus-prep/ICSI_DialogueActs/Bro016.C.txt', '../corpus-prep/ICSI_DialogueActs/Bro016.D.txt', '../corpus-prep/ICSI_DialogueActs/Bro016.E.txt', '../corpus-prep/ICSI_DialogueActs/Bro016.F.txt', '../corpus-prep/ICSI_DialogueActs/Bro017.A.txt', '../corpus-prep/ICSI_DialogueActs/Bro017.B.txt', '../corpus-prep/ICSI_DialogueActs/Bro017.C.txt', '../corpus-prep/ICSI_DialogueActs/Bro017.D.txt', '../corpus-prep/ICSI_DialogueActs/Bro017.E.txt', '../corpus-prep/ICSI_DialogueActs/Bro018.A.txt', '../corpus-prep/ICSI_DialogueActs/Bro018.B.txt', '../corpus-prep/ICSI_DialogueActs/Bro018.C.txt', '../corpus-prep/ICSI_DialogueActs/Bro018.D.txt', '../corpus-prep/ICSI_DialogueActs/Bro018.E.txt', '../corpus-prep/ICSI_DialogueActs/Bro019.A.txt', '../corpus-prep/ICSI_DialogueActs/Bro019.B.txt', '../corpus-prep/ICSI_DialogueActs/Bro019.C.txt', '../corpus-prep/ICSI_DialogueActs/Bro019.D.txt', '../corpus-prep/ICSI_DialogueActs/Bro019.E.txt', '../corpus-prep/ICSI_DialogueActs/Bro019.F.txt', '../corpus-prep/ICSI_DialogueActs/Bro019.G.txt', '../corpus-prep/ICSI_DialogueActs/Bro021.A.txt', '../corpus-prep/ICSI_DialogueActs/Bro021.B.txt', '../corpus-prep/ICSI_DialogueActs/Bro021.C.txt', '../corpus-prep/ICSI_DialogueActs/Bro021.D.txt', '../corpus-prep/ICSI_DialogueActs/Bro021.E.txt', '../corpus-prep/ICSI_DialogueActs/Bro021.F.txt', '../corpus-prep/ICSI_DialogueActs/Bro021.G.txt', '../corpus-prep/ICSI_DialogueActs/Bro022.A.txt', '../corpus-prep/ICSI_DialogueActs/Bro022.B.txt', '../corpus-prep/ICSI_DialogueActs/Bro022.C.txt', '../corpus-prep/ICSI_DialogueActs/Bro022.D.txt', '../corpus-prep/ICSI_DialogueActs/Bro022.E.txt', '../corpus-prep/ICSI_DialogueActs/Bro022.F.txt', '../corpus-prep/ICSI_DialogueActs/Bro022.G.txt', '../corpus-prep/ICSI_DialogueActs/Bro023.A.txt', '../corpus-prep/ICSI_DialogueActs/Bro023.B.txt', '../corpus-prep/ICSI_DialogueActs/Bro023.C.txt', '../corpus-prep/ICSI_DialogueActs/Bro023.D.txt', '../corpus-prep/ICSI_DialogueActs/Bro023.E.txt', '../corpus-prep/ICSI_DialogueActs/Bro024.A.txt', '../corpus-prep/ICSI_DialogueActs/Bro024.B.txt', '../corpus-prep/ICSI_DialogueActs/Bro024.C.txt', '../corpus-prep/ICSI_DialogueActs/Bro024.D.txt', '../corpus-prep/ICSI_DialogueActs/Bro024.E.txt', '../corpus-prep/ICSI_DialogueActs/Bro024.F.txt', '../corpus-prep/ICSI_DialogueActs/Bro024.G.txt', '../corpus-prep/ICSI_DialogueActs/Bro024.H.txt', '../corpus-prep/ICSI_DialogueActs/Bro025.A.txt', '../corpus-prep/ICSI_DialogueActs/Bro025.B.txt', '../corpus-prep/ICSI_DialogueActs/Bro025.C.txt', '../corpus-prep/ICSI_DialogueActs/Bro025.D.txt', '../corpus-prep/ICSI_DialogueActs/Bro025.E.txt', '../corpus-prep/ICSI_DialogueActs/Bro026.A.txt', '../corpus-prep/ICSI_DialogueActs/Bro026.B.txt', '../corpus-prep/ICSI_DialogueActs/Bro026.C.txt', '../corpus-prep/ICSI_DialogueActs/Bro026.D.txt', '../corpus-prep/ICSI_DialogueActs/Bro026.E.txt', '../corpus-prep/ICSI_DialogueActs/Bro027.A.txt', '../corpus-prep/ICSI_DialogueActs/Bro027.B.txt', '../corpus-prep/ICSI_DialogueActs/Bro027.C.txt', '../corpus-prep/ICSI_DialogueActs/Bro027.D.txt', '../corpus-prep/ICSI_DialogueActs/Bro028.A.txt', '../corpus-prep/ICSI_DialogueActs/Bro028.B.txt', '../corpus-prep/ICSI_DialogueActs/Bro028.C.txt', '../corpus-prep/ICSI_DialogueActs/Bro028.D.txt', '../corpus-prep/ICSI_DialogueActs/Bro028.E.txt', '../corpus-prep/ICSI_DialogueActs/Bsr001.A.txt', '../corpus-prep/ICSI_DialogueActs/Bsr001.B.txt', '../corpus-prep/ICSI_DialogueActs/Bsr001.C.txt', '../corpus-prep/ICSI_DialogueActs/Bsr001.D.txt', '../corpus-prep/ICSI_DialogueActs/Bsr001.E.txt', '../corpus-prep/ICSI_DialogueActs/Bsr001.F.txt', '../corpus-prep/ICSI_DialogueActs/Bsr001.G.txt', '../corpus-prep/ICSI_DialogueActs/Bsr001.H.txt', '../corpus-prep/ICSI_DialogueActs/Btr001.A.txt', '../corpus-prep/ICSI_DialogueActs/Btr001.B.txt', '../corpus-prep/ICSI_DialogueActs/Btr001.C.txt', '../corpus-prep/ICSI_DialogueActs/Btr001.D.txt', '../corpus-prep/ICSI_DialogueActs/Btr001.E.txt', '../corpus-prep/ICSI_DialogueActs/Btr001.F.txt', '../corpus-prep/ICSI_DialogueActs/Btr002.A.txt', '../corpus-prep/ICSI_DialogueActs/Btr002.B.txt', '../corpus-prep/ICSI_DialogueActs/Btr002.C.txt', '../corpus-prep/ICSI_DialogueActs/Btr002.D.txt', '../corpus-prep/ICSI_DialogueActs/Btr002.E.txt', '../corpus-prep/ICSI_DialogueActs/Btr002.F.txt', '../corpus-prep/ICSI_DialogueActs/Buw001.A.txt', '../corpus-prep/ICSI_DialogueActs/Buw001.B.txt', '../corpus-prep/ICSI_DialogueActs/Buw001.C.txt', '../corpus-prep/ICSI_DialogueActs/Buw001.D.txt', '../corpus-prep/ICSI_DialogueActs/Buw001.E.txt', '../corpus-prep/ICSI_DialogueActs/Buw001.F.txt', '../corpus-prep/ICSI_DialogueActs/Buw001.G.txt', '../corpus-prep/ICSI_DialogueActs/Buw001.H.txt']

#--------------------------------------------------



import pickle
from POS_tagging import initialisation, word_embedding

DA_tag_ami_abreviation = {0: 0, 1:0, 2:0,
                      3:1, 4:1,
                      5:2, 6:2, 7:2,
                      8:3, 9:3, 10:3, 11:3,
                      12:4, 13:4}

#with four clusters
DA_tag_ami_abreviation_ = {3:0, 4:0,
                       5:1, 6:1, 7:1,
                       8:2, 9:2, 10:2, 11:2,
                       0: 3, 1: 3, 2: 3, 12: 3, 13: 3}


DA_tag_icsi_abreviation = {1:0, 2:1, 3:2}

#-------------some variables for ICSI-----------------------

meeting_list_icsi = ['Bdb001'] + ['Bed00'+str(k) for k in range(2,10) if k != 7] +\
               ['Bed0'+str(k) for k in range(10,18) ]+\
               ['Bmr00' + str(j) for j in range(1,10) if j != 4]+['Bmr0' + str(j) for j in range(10,31) if j != 17]+\
               ['Bns00' + str(j) for j in range(1,4)]+\
               ['Bro00' + str(j) for j in range(3,10) if (j != 6 and j!= 9)]+['Bro0' + str(j) for j in range(10,29) if j != 20]+\
               ['Bsr001', 'Btr001', 'Btr002', 'Buw001']

#-------------some variables for AMI-----------------------

# All scenario based extractive summaries in AMI
DA_ami_list = [i+1 for i in range(151)]
for j in [9, 24, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 150]:
    DA_ami_list.remove(j)

#TODO: I do ot understad why pickle not working. It doen't matter, I wrote them directly in DA_icsi_list variable.
def load_DA_icsi_list():

    DA_icsi_list = []
    for meet in meeting_list_icsi:
        for parti in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']:
            mm = meet + '.' + parti
            adress = '../corpus-prep/ICSI_DialogueActs/' + mm + '.txt'
            # if a file exists
            if os.path.isfile(adress):
                DA_icsi_list.append(adress)

    #print(DA_icsi_list)
    #pickle.dump(DA_icsi_list, 'Data/DA_icsi_list.pkl')

    pickle_out = open("Data/DA_icsi_list.pkl", "wb")
    pickle.dump(DA_icsi_list, pickle_out)
    pickle_out.close()

    pass


class all_text_representation:

    def __init__(self, corpus, text_to_vector_type, n_taxonomy, with_label = None):

        self.corpus = corpus
        self.text_to_vector_type = text_to_vector_type

        if corpus == 'icsi':
            self.meeting_group = DA_icsi_list
        elif corpus == 'ami':
            self.meeting_group = DA_ami_list

        self.n_taxonomy = n_taxonomy
        if with_label is None:
            self.with_label = True
        else:
            self.with_label = with_label

        pass

    def represent_texts_as_vectors(self):

        word_emb = word_embedding()
        all_meeting_input = {i:[] for i in self.meeting_group}

        #if the labels of DAs are given
        file_name = []
        if self.with_label == True:
            if self.corpus == 'ami':
                file_name = [adress_resume_ami + 'meet_' + str(i) + '.txt' for i in self.meeting_group]

            elif self.corpus == 'icsi':
                file_name = self.meeting_group #DA_icsi_list


            for l in range(len(file_name)):
                file_ = file_name[l]
                _input_words_tags = word_emb.generate_tag(self.corpus, [file_], self.text_to_vector_type, self.with_label)
                all_meeting_input[file_name[l]] = _input_words_tags

        "each text of dialogue acts has a tuple ([(sentence_1, equivalent vector_1), (sentence_2, equivalent vector_2), (sentence_3, equivalent vector_3)], [DA_1, DA_2, DA_3]) in all_meeting_input. For AMI DA_1, DA_2 and .. are integer reals while in icsi they are list of integers."
        return all_meeting_input


    def which_label_eliminate(self, all_for_train_clustering, eliminate_list, which_taggig):

        output = {i: (None, None) for i in self.meeting_group}
        count_all = 0

        for i in self.meeting_group:

            text_vector_list = []
            DA_list = []

            tempo = all_for_train_clustering[i][1]
            count_all += len(tempo)
            for k in range(len(tempo)):
                if tempo[k] not in eliminate_list:
                    text_vector_list.append(all_for_train_clustering[i][0][k])
                    DA_list.append(which_taggig[tempo[k]])

            output[i] = (text_vector_list, DA_list)

        #this is for computing percentage of each label in the AMI corpus.
        print("count_all", count_all)

        return output

    def abreviate_labels_ami(self, all_for_train_clustering):
        "For AMI corpus: it gets list of utterances plus their DAs and generalise them accoring to the selected number of DA tags."

        output = None

        if self.n_taxonomy == 5:
            output = self.which_label_eliminate(all_for_train_clustering, [14], DA_tag_ami_abreviation)

        elif self.n_taxonomy == 4:
            output = self.which_label_eliminate(all_for_train_clustering, [0, 1, 2, 14], DA_tag_ami_abreviation_)

        elif self.n_taxonomy == 3:
            output = self.which_label_eliminate(all_for_train_clustering, [0, 1, 2, 12, 13, 14], DA_tag_ami_abreviation_)

        print("*****text representation for " + self.corpus + ' with ' + str(self.n_taxonomy) + ' labesl finished ****')

        return output

    def abreviate_labels_icsi(self, all_for_train_clustering):

        "for ICSI"
        output = {i: (None, None) for i in self.meeting_group}

        for i in self.meeting_group:

            text_vector_list = []
            DA_list = []

            for j in range(len(all_for_train_clustering[i][1])):
                "because of several DAs for each utterance, here we have a list of labels."
                da = all_for_train_clustering[i][1][j]
                for k in range(len(da)):

                    # for counting total number of DAs in the ICSI corpus.
                    if self.n_taxonomy == 7:
                        DA_list.append(da[k])
                        text_vector_list.append(all_for_train_clustering[i][0][j])

                    if self.n_taxonomy == 5:
                        if da[k] not in [-1, 5]:
                            DA_list.append(da[k])
                            text_vector_list.append(all_for_train_clustering[i][0][j])

                    elif self.n_taxonomy == 4:
                        if da[k] not in [-1, 0, 5]:
                            DA_list.append(da[k])
                            text_vector_list.append(all_for_train_clustering[i][0][j])

                    elif self.n_taxonomy == 3:
                        if da[k] not in [-1, 0, 4, 5]:
                            DA_list.append(DA_tag_icsi_abreviation[da[k]])
                            text_vector_list.append(all_for_train_clustering[i][0][j])

            output[i] = (text_vector_list, DA_list)


        print("*****text representation for " + self.corpus + ' with ' + str(self.n_taxonomy) + ' labesl finished ****')
        return output

    def save_abreviated_labels(self):

        meeting_input = None

        "here we save first sentences, their represented vectors and their real data. "
        "second we add their abreviated labels. It seems unnecessary to keep all_meeting_input at the moment, but we save them anyway. "
        "they might be usefull in the future specially for the AMI corpus. "

        initialisation(self.corpus)
        all_meeting_input = self.represent_texts_as_vectors()
        if self.corpus == 'ami':
            meeting_input = self.abreviate_labels_ami(all_meeting_input)
        elif self.corpus == 'icsi':
            meeting_input = self.abreviate_labels_icsi(all_meeting_input)

        filehandler = open('Data/data_'+ str(self.n_taxonomy) + '_label_' + self.corpus + '_' + self.text_to_vector_type, 'wb')
        pickle.dump(all_meeting_input, filehandler)
        pickle.dump(meeting_input, filehandler)

        return

    def reload_abreviated_labels(self):
        """load represented texts of database as numerical vectors."""
        #path = os.getcwd()+'/DA_tagging/'
        path = ""
        filehandler = open(path+ 'Data/data_'+ str(self.n_taxonomy) + '_label_' + self.corpus+ '_'+ self.text_to_vector_type, 'rb')
        all_meeting_input = pickle.load(filehandler)
        meeting_input = pickle.load(filehandler)

        return (all_meeting_input, meeting_input)

def count_DAs_proportion_in_corpus(corpus_name):

    """this is just for counting proportation of DAs for each given corpus."""

    text_rep = None

    if corpus_name == 'icsi':
        text_rep = all_text_representation(corpus_name, 'POS', 7)
    elif corpus_name == 'ami':
        text_rep = all_text_representation(corpus_name, 'POS', 5)

    (a, b) = text_rep.reload_abreviated_labels()
    all_das = []
    count = 0
    for key in b.keys():
        count += len(b[key][1])
        for j in [item for item in b[key][1]]:
            all_das.append(j)

    countersss = collections.Counter(all_das)
    if corpus_name == 'ami':
        "for the *other* DA in ami the information are not available in the countersss "
        countersss[5] = 36
        count += 36

    print("total number of DAs for "+ corpus_name + ": "+ str(count))
    print(countersss)
    print("percentage of each tag for " +  corpus_name + ": " )
    print({key: countersss[key]/count for key in countersss.keys()})

    pass

#count_DAs_proportion_in_corpus('ami')