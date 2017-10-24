# -*- coding: utf-8 -*-
import argparse
from gensim.models.keyedvectors import KeyedVectors
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA


def parse_args():
    parser = argparse.ArgumentParser(description='Clean Chinese corpus')
    parser.add_argument('model', metavar='M', type=str,
                        help='model file')

    return parser.parse_args()

def minmax(vectors, padding=0.02):
    dim = np.shape(vectors)[-1]
    reshaped_vectors = np.reshape(vectors, (-1, dim))

    axis_min = np.amin(reshaped_vectors, axis=0) - padding
    axis_max = np.amax(reshaped_vectors, axis=0) + padding
    axis_minmax = [None] * (len(axis_min) + len(axis_max))
    axis_minmax[::2] = axis_min
    axis_minmax[1::2] = axis_max

    return axis_minmax

def pca(vectors):
    # store vector shape
    ori_shape = np.shape(vectors)
    dim = ori_shape[-1]

    # dimension reduction to reshaped vectors (d1*d2*...*d_n-1, 2)
    reduced_vectors = PCA(n_components=2).fit_transform(np.reshape(vectors, (-1, dim)))

    # restore vector shape to (d1, d2, ..., d_n-1, 2)
    new_shape = list(ori_shape)
    new_shape[-1] = 2
    new_shape = tuple(new_shape)
    return np.reshape(reduced_vectors, new_shape)

def pca_model(model):
    items = model.vocab
    keys = [item[0] for item in items] 
    vectors = [model[c] for c in keys] 

    reduced_vectors = pca(vectors)

    reduced_model = {}
    for i, c in enumerate(keys):
        reduced_model[c] = reduced_vectors[i]

    return reduced_model

def visualize(displays, vectors):
    # init plot
    zhfont = matplotlib.font_manager.FontProperties(fname='../../assets/fonts/wqy-microhei.ttc') # Chinese text display font
    ax = plt.subplot(1, 1, 1)
    ax.set_title('Char2Vec')
    ax.axis(minmax(vectors))

    print('-----------------------------------------------------------------------')

    # plot char2vec
    for i, group in enumerate(vectors):
        color = 'C{}'.format(i % 10)

        for j, v in enumerate(group): 
            ax.text(v[0], v[1], displays[i][j], fontproperties=zhfont, color=color)
            print('{}: {}'.format(displays[i][j], v))

    print('-----------------------------------------------------------------------')

    # show plot
    plt.show()

def interactive_test(model, reduced_model):
    # Keep vectors for visualization
    all_chars = []
    all_vectors = []

    while True:
        c = input('Input a Chinese character (q to quit):')
        if c == 'q':
            break
        else:
            try:
                sim_chars = model.similar_by_word(c)

                chars = [c]
                vectors = [reduced_model[c]]
                for sim_char, score in sim_chars:
                    # skip p special character
                    if sim_char == 'p':
                        continue

                    chars.append(sim_char)
                    vectors.append(reduced_model[sim_char])
                    print('{}:\t{}\t{}'.format(sim_char, score, reduced_model[sim_char]))

                all_chars.append(chars)
                all_vectors.append(vectors)

                visualize(all_chars, all_vectors)

            except Exception as e:
                print('Error: {}'.format(e))

def main():
    args = parse_args()

    model = KeyedVectors.load(args.model)
    reduced_model = pca_model(model)

    interactive_test(model, reduced_model)


if __name__ == "__main__":
    main()
