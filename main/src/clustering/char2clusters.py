# -*- coding: utf-8 -*-
import argparse
import pickle
from gensim.models import Word2Vec
import numpy as np
from sklearn import cluster


def parse_args():
    parser = argparse.ArgumentParser(description='Cluster char2cluster')
    parser.add_argument('model', metavar='M', type=str,
                        help='model file')
    parser.add_argument('--output', '-o', metavar='O', type=str, default='char2clusters.bin',
                    help='output cluster file name')
    parser.add_argument('--clusters', '-c', metavar='C', type=str,
                    help='pretrained cluster file name for interactive test')
    parser.add_argument('-k', metavar='K', type=int, default=50,
                        help='number of clusters')

    return parser.parse_args()

def save_clusters(cluster_idxs, output):
    with open(output, 'wb') as fout:
        pickle.dump(cluster_idxs, fout)

def load_pickle(f):
    with open(f, 'rb') as fin:
        data = pickle.load(fin)

    return data 

def interactive_test(model, cluster_idxs):
    while True:
        c = input('Input a Chinese character (q to quit):')
        if c == 'q':
            break
        else:
            try:
                char_idx = model.wv.index2word.index(c)
                char_cluster_idx = cluster_idxs[char_idx]

                cluster_chars = np.where(cluster_idxs == char_cluster_idx)[0]
                for cluster_char_idx in cluster_chars: 
                    cluster_char = model.wv.index2word[cluster_char_idx]
                    print('{}'.format(cluster_char), end=',')

                print('')

            except Exception as e:
                print('Error: {}'.format(e))

def get_clusters(model, k=50):
    vectors = model.wv.syn0
    kmeans = cluster.KMeans(n_clusters=k, n_jobs=-1, random_state=0)
    cluster_idxs = kmeans.fit_predict(vectors)

    return cluster_idxs

def main():
    args = parse_args()

    model = Word2Vec.load(args.model) 

    if not args.clusters:
        cluster_idxs = get_clusters(model, k=args.k)

        save_clusters(cluster_idxs, args.output)
    else:
        cluster_idxs = load_pickle(args.clusters)

        interactive_test(model, cluster_idxs)


if __name__ == "__main__":
    main()
