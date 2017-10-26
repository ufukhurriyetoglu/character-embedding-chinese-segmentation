#!/bin/bash

python3 -m src.cooccur_matrix.cooccur_matrix --model src/output/small_char2vec.bin --clusters src/output/small_char2clusters.bin --corpus corpus/small_corpus.txt -o src/output/small_cooccur_matrix.txt
