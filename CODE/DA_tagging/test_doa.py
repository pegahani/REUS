import os

from Domain_Adaptation import domain_adptation

len_icsi_3 = 18872
len_icsi_5 = 116362
len_ami_3 = 18719
len_ami_5 = 18872

if __name__ == '__main__':
    # classifier types: TCA, SCL

    path = os.getcwd()
    generate_file = open(path + '/ami/doa_scl_3.txt', 'w')

    #generate_file.write("******5 taxonomy*****ICSI to AMI*** not blind sampling ***" + '\n')

    # for percentage in [0.001, 0.002, 0.003, 0.004, 0.005, 0.006, 0.007, 0.008, 0.009, 0.01, 0.02, 0.03]: #, 0.4, 0.6, 0.8, 1.0]:
    #     generate_file.write("************* " + str(percentage) + " *******************"+ '\n')
    #     doap = domain_adptation(text_to_vector_type= 'POS', corpus_source ='icsi', n_taxonomy_source = 5, which_percentage_source = percentage,
    #                                                     corpus_target = 'ami', n_taxonomy_target = 5, classifier_type = 'SCL')
    #
    #
    #
    #     generate_file.write(str(doap.TransferComponent(sampling_times= 5 , blind_sampling= False) ) + "\n")
    #     generate_file.flush()

    # generate_file.write('**********************' + '\n')
    # generate_file.flush()

    generate_file.write("******3 taxonomy*****ICSI to AMI*** blind sampling ***" + '\n')

    for percentage in [0.001, 0.002, 0.003, 0.004, 0.005, 0.006, 0.007, 0.008, 0.009]:
        generate_file.write("************* " + str(percentage) + " *******************"+ '\n')

        doap = domain_adptation(text_to_vector_type= 'POS', corpus_source ='icsi', n_taxonomy_source = 3, which_percentage_source = percentage,
                                corpus_target = 'ami', n_taxonomy_target = 3, classifier_type = 'SCL')
        generate_file.flush()

        generate_file.write(str(doap.TransferComponent(sampling_times= 5 , blind_sampling= False)))

    generate_file.write('**********************' + '\n')
    generate_file.flush()


    #
    # print("******3 taxonomy*****ICSI to AMI*** not blind sampling ***" + '\n')
    # doap = domain_adptation(text_to_vector_type= 'POS', corpus_source ='icsi', n_taxonomy_source = 3, which_percentage_source =0.01,
    #     corpus_target = 'ami', n_taxonomy_target = 3)
    # generate_file.flush()
    #
    # doap.TransferComponent(sampling_times= 5 , blind_sampling= False)
    # print('**********************' + '\n')
    # # generate_file.flush()
    # #
    # print("******3 taxonomy*****ICSI to AMI*** blind sampling ***" + '\n')
    # doap = domain_adptation(text_to_vector_type= 'POS', corpus_source ='icsi', n_taxonomy_source = 3, which_percentage_source = 0.5,
    #     corpus_target = 'ami', n_taxonomy_target = 3 )
    # # generate_file.flush()
    # #
    # doap.TransferComponent(sampling_times= 5 , blind_sampling= True)
    # print('**********************' + '\n')
    # generate_file.flush()