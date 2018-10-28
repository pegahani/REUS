import os
from clusters import cluster

if __name__ == '__main__':

    path = os.getcwd()
    generate_file = open(path + '/ami/cluster.txt', 'w')

    for method in ["kmeans", "Agglomerative", "EM"]:
        for number_clusters in range(3,16):
            
            generate_file.write("****not blind *** 3 taxonomy***"+ method+ '****' + str(number_clusters) + '*****POS******'+ '\n')

            model = cluster(corpus='ami', method=method, text_to_vector_type='POS', with_label=True, n_taxonomy=3,
                        number_of_clusters= number_clusters, which_percentage=0.167)
            generate_file.write(str(model.DA_clustering(5, is_smote = False, smote_kind= None, blind_sampling=False)))

            generate_file.write('********************************************************************' + '\n')
            generate_file.flush()

    for method in ["kmeans", "Agglomerative", "EM"]:
        for number_clusters in range(3, 16):
            generate_file.write("****blind *** 3 taxonomy***" + method + '****' + str(number_clusters) + '*****POS******' + '\n')

            model = cluster(corpus='ami', method=method, text_to_vector_type='POS', with_label=True, n_taxonomy=3,
                            number_of_clusters=number_clusters, which_percentage=0.5)
            generate_file.write(str(model.DA_clustering(5, is_smote=False, smote_kind=None, blind_sampling=True)))

            generate_file.write('********************************************************************' + '\n')
            generate_file.flush()


