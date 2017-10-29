#!/bin/bash

pre=""

while getopts "t" opt; do
    case "$opt" in
        t)  pre="small_"
            ;;
    esac
done

python3 -m src.clustering.char2clusters src/output/${pre}char2vec.bin -k 50 -o src/output/${pre}char2clusters.bin
