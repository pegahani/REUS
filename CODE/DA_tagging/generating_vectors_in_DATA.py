# this is a script for generating all text representaions in ./DATA file.
# This is for accelerating the code.
from all_representations import all_text_representation
from clusters import cluster, DA_icsi_list

# All scenario based extractive summaries in AMI


DA_ami_list = [i+1 for i in range(151)]
for j in [9, 24, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 150]:
    DA_ami_list.remove(j)

# you do not need to run this code until you add a new corpus.
if __name__ == '__main__':

    print('*****************************')


    for veci in [ "POS"]:#"word2vec", "POS+word2vec", "lexical", "POS"
        for num_taxonomy in [3]: #, 4, 5, 7]:
            for element in ['icsi']: #''ami']:

                text_rep =  all_text_representation(corpus=element, text_to_vector_type=veci,n_taxonomy=num_taxonomy, with_label= True )
                text_rep.save_abreviated_labels()