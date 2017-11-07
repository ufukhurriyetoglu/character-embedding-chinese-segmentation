# -*- coding: utf-8 -*-
import argparse
import logging
from gensim.models import Word2Vec
import pickle
import re


def parse_args():
    parser = argparse.ArgumentParser(description='Naive threshold method')
    parser.add_argument('file', metavar='F', type=str,
                    help='Text file to segment')
    parser.add_argument('--model', metavar='M', type=str,
                    help='model file')
    parser.add_argument('--clusters', metavar='CL', type=str,
                    help='cluster file')
    parser.add_argument('--comatrix', metavar='CM', type=str,
                    help='cooccurrence matrix file')
    parser.add_argument('--output', metavar='OF', type=str, default='seg_file.txt',
                    help='Segmented text file')

    return parser.parse_args()

def load_pickle(f):
    with open(f, 'rb') as fin:
        data = pickle.load(fin)

    return data 

def is_ch_char(c):
    return re.match(r'[\u4e00-\u9fff]', c) != None

def connection_strength(c1, c2, step, model, clusters, cooccur_matrix):
    if is_ch_char(c1) and is_ch_char(c2):
        try:
            c1_idx = model.wv.index2word.index(c1)
            c2_idx = model.wv.index2word.index(c2)
            cluster1 = clusters[c1_idx]
            cluster2 = clusters[c2_idx]

            return cooccur_matrix[step-1][cluster1][cluster2]
        except Exception as e:
            return 0

    return 0

def segment(fin_name, fout_name, model, clusters, cooccur_matrix): 
    with open(fout_name, 'w') as fout:
        with open(fin_name, 'r') as fin:
            for l_no, line in enumerate(fin):
                if l_no % 1000 == 0:
                    logging.info('Processing line {}...'.format(l_no))

                # segment
                split_line = list(line)

                connection_strengths = [0] + [connection_strength(c1, c2, 1, model, clusters, cooccur_matrix) for c1, c2 in zip(split_line, split_line[1:])] + [0]
                mid_points = [(a + b) / 2 for a, b in zip(connection_strengths, connection_strengths[2:])]
                seg = [s <= mp for s, mp in zip(connection_strengths[1:-1], mid_points)]

                # results in word list
                results = []
                last = ''
                for i, char in enumerate(split_line[:-1]):
                    last += char
                    if seg[i]:
                        results.append(last)
                        last = ''

                if last != '':
                    results.append(last)

                # write to file
                fout.write('　'.join(results) + '\n') 

def main():
    args = parse_args()

    model = Word2Vec.load(args.model) 
    clusters = load_pickle(args.clusters) 
    cooccur_matrix = load_pickle(args.comatrix)

    segment(args.file, args.output, model, clusters, cooccur_matrix)

if __name__ == "__main__":
    main()
