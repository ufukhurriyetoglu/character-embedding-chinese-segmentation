#!/bin/bash

pre=""
k=50
vd=250

while getopts "td:k:" opt; do
    case "$opt" in
        t)  pre="small_"
            ;;
        d)  vd=${OPTARG}
            ;;
        k)  k=${OPTARG}
            ;;
    esac
done

python3 -m src.cooccur_matrix.cooccur_matrix --model src/output/d_${vd}_k_${k}/${pre}char2vec.bin --corpus corpus/${pre}corpus.txt --clusters src/output/d_${vd}_k_${k}/${pre}char2clusters.bin --output src/output/d_${vd}_k_${k}/${pre}cooccur_matrix.bin
