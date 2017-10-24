# -*- coding: utf-8 -*-
import logging
import sys
from gensim.corpora import WikiCorpus


def main():
    if len(sys.argv) != 3:
        print('Usage: python3 {} <wiki-data-path> <output-file>'.format(sys.argv[0]))
        exit()

    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s', level=logging.INFO)
    wiki_corpus = WikiCorpus(sys.argv[1], dictionary={})

    i = 0
    fout_name = sys.argv[2]
    with open(fout_name, 'w', encoding='utf-8') as output:
        for text in wiki_corpus.get_texts():
            output.write(' '.join(text) + '\n')
            i += 1
            
            if i % 10000 == 0:
                logging.info('{} of the corpus has been processed'.format(i))


if __name__ == '__main__':
    main()
