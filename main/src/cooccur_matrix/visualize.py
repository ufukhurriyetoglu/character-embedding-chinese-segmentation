# -*- coding: utf-8 -*-
import argparse
import word2vec
import numpy as np
import pickle
import matplotlib
import matplotlib.pyplot as plt


def parse_args():
    parser = argparse.ArgumentParser(description='Visualize cooccurrence matrix')
    parser.add_argument('--model', metavar='M', type=str,
                    help='model file')
    parser.add_argument('--clusters', metavar='CL', type=str,
                    help='cluster file')
    parser.add_argument('--comatrix', metavar='CM', type=str,
                    help='cooccurrence matrix file')

    return parser.parse_args()

def load_pickle(f):
    with open(f, 'rb') as fin:
        data = pickle.load(fin)

    return data 

def visualize(chars, connection_strength, n=2):
    # init data
    m = len(chars) * 2 - 1
    x_labels = [''] * m
    x_labels[::2] = chars
    x = range(m)
    ys = [[0 for _ in range(m)] for _ in range(n-1)]
    for step in range(1, n):
        for i in range(len(chars) - step):
            for j in range(i + step, len(chars), step):
                center = i + j 
                ys[step-1][center] = connection_strength[i][j]

    # init plot
    zhfont = matplotlib.font_manager.FontProperties(fname='../../assets/fonts/wqy-microhei.ttc') # Chinese text display font
    plt.title('Connection Strength')
    plt.xticks(x, x_labels, fontproperties=zhfont) 

    # plot strengths at different step sizes
    for i, y in enumerate(ys):
        plt.plot(x, y, label='Step {}'.format(i+1))

    # show plot
    plt.show()

def interactive_test(model, clusters, cooccur_matrix, n=2): 
    while True:
        sen = input('Input a Chinese sentence (q to quit):')
        if sen == 'q':
            break
        else:
            try:
                chars = list(sen)
                char_idxs = [-1 for _ in range(len(chars))]
                cluster_idxs= [-1 for _ in range(len(chars))]
                connection_strength = [[0 for _ in range(len(chars))] for _ in range(len(chars))]

                for i, char in enumerate(chars):
                    try:
                        char_idxs[i] = model.ix(char)
                        cluster_idxs[i] = clusters[char_idxs[i]]

                    except Exception as e:
                        continue

                for step in range(1, n):
                    for i in range(len(chars) - step):
                        for j in range(i + step, len(chars), step):
                            if cluster_idxs[i] != -1 and cluster_idxs[j] != -1:
                                connection_strength[i][j] = cooccur_matrix[step-1][cluster_idxs[i]][cluster_idxs[j]]

                visualize(chars, connection_strength)

            except Exception as e:
                print('Error: {}'.format(e))

def main():
    args = parse_args()

    model = word2vec.load(args.model) 
    clusters = load_pickle(args.clusters) 
    cooccur_matrix = load_pickle(args.comatrix)

    interactive_test(model, clusters, cooccur_matrix)


if __name__ == "__main__":
    main()
