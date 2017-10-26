#!/bin/bash

python3 -m src.clustering.char2clusters.py src/output/char2vec.bin -k 50 -o src/output/char2clusters.bin
