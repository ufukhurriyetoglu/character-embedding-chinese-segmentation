# -*- coding: utf-8 -*-
import argparse
import word2vec
import numpy as np
from sklearn import cluster


def parse_args():
    parser = argparse.ArgumentParser(description='Cluster char2cluster')
    parser.add_argument('model', metavar='M', type=str,
                        help='model file')
    parser.add_argument('-k', metavar='K', type=int, default=50,
                        help='number of clusters')
    parser.add_argument('--all', default=False, action='store_true',
                        help='output all cluster information')

    return parser.parse_args()

def output_clusters(model, cluster_idxs):
    centroids = list(zip(model.vocab, cluster_idxs))
    centroids_sort = sorted(centroids, key=lambda e: e[1])
    
    for centroid in centroids_sort:
        print('{},{}'.format(centroid[0], centroid[1]))

def interactive_test(model, cluster_idxs):
    while True:
        c = input('Input a Chinese character (q to quit):')
        if c == 'q':
            break
        else:
            try:
                char_idx = model.ix(c)
                char_cluster_idx = cluster_idxs[char_idx]

                cluster_chars = np.where(cluster_idxs == char_cluster_idx)[0]
                for cluster_char_idx in cluster_chars: 
                    cluster_char = model.vocab[cluster_char_idx]
                    print('{}'.format(cluster_char), end=',')

                print('')

            except Exception as e:
                print('Error: {}'.format(e))

def get_clusters(model, k=50):
    vectors = model.vectors
    kmeans = cluster.KMeans(n_clusters=k, n_jobs=-1, random_state=0)
    cluster_idxs = kmeans.fit_predict(vectors)

    return cluster_idxs

def main():
    args = parse_args()

    model = word2vec.load(args.model) 
    vectors = model.vectors
    kmeans = cluster.KMeans(n_clusters=args.k, n_jobs=-1, random_state=0)
    cluster_idxs = kmeans.fit_predict(vectors)

    if args.all:
        output_clusters(model, cluster_idxs)
    else:
        interactive_test(model, cluster_idxs)


if __name__ == "__main__":
    main()
