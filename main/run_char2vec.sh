#!/bin/bash

python3 -m src.char2vec.char2vec corpus/corpus_seg.txt -o src/output/char2vec.bin --vectordim 250
