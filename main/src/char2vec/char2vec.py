# -*- coding: utf-8 -*-
import logging
import argparse
from gensim.models import word2vec


def parse_args():
    parser = argparse.ArgumentParser(description='Clean Chinese corpus')
    parser.add_argument('corpus', metavar='C', type=str, 
                    help='corpus file (line sentences)')
    parser.add_argument('--output', '-o', metavar='O', type=str, default='char2vec.bin',
                    help='output model file name')
    parser.add_argument('--vectordim', metavar='VD', type=int, default=250,
                    help='dimentionality of embedding vectors')

    return parser.parse_args()

def char2vec(corpus, dim=250):
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

    sentences = ''
    model = None
    with open(corpus, 'r') as c:
        sentences = word2vec.LineSentence(c)
    
        model = word2vec.Word2Vec(sentences, size=dim)

    return model

def main():
    args = parse_args()

    model = char2vec(args.corpus, dim=args.vectordim)    

    model.wv.save(args.output)


if __name__ == "__main__":
    main()
