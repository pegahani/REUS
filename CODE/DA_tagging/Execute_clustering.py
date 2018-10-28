import sys

from clusters import cluster

if __name__ == '__main__':

    original_n_clusters = 3
    percentage = 0.167
    sampling_repetition = 1
    is_smote = False
    smote_type = None
    sampling_blind = False

    print(sys.argv)

    corpus_name = sys.argv[1]  # Corpus name
    clusterign_method = sys.argv[2]  # clustering methods: at the moment we have these options: kmeans, Agglomerative, EM
    text_representation = sys.argv[3]  # text representations. The available options: POS, Word2vec, lexical
    n_cluster = int(sys.argv[4])  # number of clusters for the clustering
    #if len(sys.argv) < 5:
    #    original_n_clusters = 3
    if len(sys.argv) > 5 :
        original_n_clusters = int(sys.argv[5])  # original number of clusters, which is 3 for the best case.
    elif len(sys.argv) > 6 :
        percentage = int(sys.argv[6]) # which percentage of the whole data should be sampled for the clustering
    elif len(sys.argv) > 7:
        sampling_repetition = int(sys.argv[7]) # number of iterations for repeating the LEAVE ONE OUT and clustering iterations.
    elif len(sys.argv) > 8:
        is_smote = sys.argv[8] # this parament defines, if we use SMOTE method or not.
    elif len(sys.argv) > 9:
        smote_type = sys.argv[9] # this parament defines the SMOTE method.
    elif len(sys.argv) > 10:
        sampling_blind = sys.argv[10] # if True, sampling data from DAs is with out considering their real lables imblance.

    model = cluster(corpus = corpus_name, method =clusterign_method, text_to_vector_type = text_representation,
                    with_label = True, original_number_clusters = original_n_clusters, number_of_clusters = n_cluster,
                    which_percentage = percentage)

    model.average_sampling_train(sampling_times = sampling_repetition, is_smote = is_smote, smote_kind=smote_type,
                                 blind_samling= sampling_repetition)
