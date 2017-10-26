#!/bin/bash

python3 -m src.char2vec.char2vec corpus/small_corpus_seg.txt -o src/output/small_char2vec.bin --vectordim 250
