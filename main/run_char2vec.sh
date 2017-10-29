#!/bin/bash

pre=""

while getopts "t" opt; do
    case "$opt" in
        t)  pre="small_"
            ;;
    esac
done

python3 -m src.char2vec.char2vec corpus/${pre}corpus_seg.txt -o src/output/${pre}char2vec.bin --vectordim 250
