import os

from supervised_learning import supervised

if __name__ == '__main__':

    path = os.getcwd()
    generate_file = open(path + '/icsi/svm.txt', 'w')


    generate_file.write("******5 labels*****POS*** not blind sampling ***" + '\n')
    model = supervised(corpus = 'icsi', text_to_vector_type = 'POS', n_taxonomy = 5, which_percentage = 0.5)
    generate_file.write(str(model.DA_SVM(sampling_times=5, blind_sampling= False, max_iter = 2000)) + '\n')
    generate_file.write('***********************************' + '\n')
    generate_file.flush()

    generate_file.write("******3 labels*****POS**blind sampling****" + '\n')
    model = supervised(corpus = 'icsi', text_to_vector_type = 'POS', n_taxonomy = 3, which_percentage = 0.50)
    generate_file.write(str(model.DA_SVM(sampling_times=5, blind_sampling= True,  max_iter = 2000)) + '\n')
    generate_file.write('***********************************'+ '\n')
    generate_file.flush()
