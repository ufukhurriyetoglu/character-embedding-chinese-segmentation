# -*- coding: utf-8 -*-
import argparse
from gensim.models import Word2Vec
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA


def parse_args():
    parser = argparse.ArgumentParser(description='Visualize char2vec')
    parser.add_argument('model', metavar='M', type=str,
                        help='model file')
    parser.add_argument('-n', metavar='N', type=int, default=5,
                        help='number of closest vectors to display')

    return parser.parse_args()

def minmax(vectors, padding_scale=0.1):
    dim = np.shape(vectors)[-1]
    reshaped_vectors = np.reshape(vectors, (-1, dim))

    peak_to_peak = np.ptp(reshaped_vectors, axis=0)
    axis_min = np.amin(reshaped_vectors, axis=0)
    axis_max = np.amax(reshaped_vectors, axis=0)
    axis_minmax = [None] * (len(axis_min) + len(axis_max))
    axis_minmax[::2] = axis_min
    axis_minmax[1::2] = axis_max

    axis_minmax[0] -= padding_scale * peak_to_peak[0]
    axis_minmax[1] += padding_scale * peak_to_peak[0]
    axis_minmax[2] -= padding_scale * peak_to_peak[1]
    axis_minmax[3] += padding_scale * peak_to_peak[1]

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
    return pca(model.wv.syn0)

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

def interactive_test(model, reduced_vectors, n=5):
    # Keep vectors for visualization
    all_chars = []
    all_vectors = []

    while True:
        c = input('Input a Chinese character (q to quit):')
        if c == 'q':
            break
        else:
            try:
                sim_chars, metrics = zip(*model.wv.similar_by_word(c))
                char_idx = model.wv.index2word.index(c) 

                chars = [c]
                vectors = [list(reduced_vectors[char_idx])]
                for i in range(n): 
                    sim_char = sim_chars[i] 
                    sim_char_idx = model.wv.index2word.index(sim_char)
                    metric = metrics[i]
                    reduced_vector = reduced_vectors[sim_char_idx]

                    chars.append(sim_char)
                    vectors.append(list(reduced_vector))
                    print('{}:\t{}\t{}'.format(sim_char, metric, reduced_vector))

                all_chars.append(chars)
                all_vectors.append(list(vectors))

                visualize(all_chars, all_vectors)

            except Exception as e:
                print('Error: {}'.format(e))

def main():
    args = parse_args()

    model = Word2Vec.load(args.model) 
    reduced_vectors = pca_model(model)

    interactive_test(model, reduced_vectors, n=args.n)


if __name__ == "__main__":
    main()
