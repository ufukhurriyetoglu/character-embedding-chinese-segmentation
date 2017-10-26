#!/bin/bash

python3 -m src.clustering.char2clusters src/output/small_char2vec.bin -k 50 -o src/output/small_char2clusters.bin
