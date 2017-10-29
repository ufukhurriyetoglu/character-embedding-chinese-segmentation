#!/bin/bash

pre=""

while getopts "t" opt; do
    case "$opt" in
        t)  pre="small_"
            ;;
    esac
done

python3 -m src.cooccur_matrix.cooccur_matrix --model src/output/${pre}char2vec.bin --corpus corpus/${pre}corpus.txt --clusters src/output/${pre}char2clusters.bin --output src/output/${pre}cooccur_matrix.bin
