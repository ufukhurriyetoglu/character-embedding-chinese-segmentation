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
    parser.add_argument('-k', metavar='K', type=int, default=10,
                        help='number of nearest vectors in a cluster')

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

                cluster_chars = np.where(np.array(cluster_idxs) == char_cluster_idx)[0]
                for cluster_char_idx in cluster_chars: 
                    cluster_char = model.wv.index2word[cluster_char_idx]
                    print('{}'.format(cluster_char), end=',')

                print('')

            except Exception as e:
                print('Error: {}'.format(e))

def get_clusters(model, k=10, threshold=0):
    words = model.wv.index2word
    cluster_idxs = [-1 for _ in range(len(words))]
    metrics = [-1 for _ in range(len(words))]
    cluster_idx = 0

    for word in words:
        char_idx = words.index(word)

        # skip already asigned vectors
        if cluster_idxs[char_idx] != -1:
            continue

        # find similar characters
        sim_chars, sim_metrics = zip(*model.wv.similar_by_word(word, topn=k))
        sim_char_idxs = [words.index(sim_char) for sim_char in sim_chars]

        # find the max similarity metric with all other characters in the cluster
        max_sim_metrics = [max([model.wv.similarity(c, other) if c != other else 0 for other in sim_chars] + [sim_metrics[i]]) for i, c in enumerate(sim_chars)]

        # assign cluster to center character
        cluster_idxs[char_idx] = cluster_idx
        metrics[char_idx] = max(sim_metrics)

        # assign cluster to nearest characters
        for sim_char in sim_chars:
            sim_char_idx = words.index(sim_char)
            sim_metric = max_sim_metrics[sim_chars.index(sim_char)]

            # if some charaters are already in a cluster, compare and keep the one with larger metric
            if cluster_idxs[sim_char_idx] != -1 and metrics[sim_char_idx] > sim_metric:
                continue

            # similarity must be >= threshold
            if sim_metric >= threshold:
                cluster_idxs[sim_char_idx] = cluster_idx
                metrics[sim_char_idx] = sim_metric

        cluster_idx += 1

    # cluster special pause character 'p' by itself
    p_idx = model.wv.index2word.index('p')
    cluster_idxs[p_idx] = cluster_idx + 1 

    print('Number of clusters: {}'.format(cluster_idx + 1))

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
