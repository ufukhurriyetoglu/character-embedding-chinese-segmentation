# -*- coding: utf-8 -*-
import logging
import argparse
import word2vec


def parse_args():
    parser = argparse.ArgumentParser(description='Clean Chinese corpus')
    parser.add_argument('corpus', metavar='C', type=str, 
                    help='corpus file (line sentences)')
    parser.add_argument('--output', '-o', metavar='O', type=str, default='char2vec.bin',
                    help='output model file name')
    parser.add_argument('--vectordim', metavar='VD', type=int, default=250,
                    help='dimentionality of embedding vectors')

    return parser.parse_args()

def char2vec(corpus, output='char2vec.bin', dim=250):
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

    word2vec.word2vec(corpus, output, size=dim)

def main():
    args = parse_args()
    char2vec(args.corpus, output=args.output, dim=args.vectordim)    


if __name__ == "__main__":
    main()
