#!/bin/bash

python3 -m src.cooccur_matrix.cooccur_matrix --model src/output/char2vec.bin --clusters src/output/char2clusters.bin --corpus corpus/corpus.txt -o src/output/cooccur_matrix.txt
