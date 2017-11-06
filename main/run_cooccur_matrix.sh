#!/bin/bash

pre=""
k=50
vd=250
algo="k_means"

while getopts "td:k:a:" opt; do
    case "$opt" in
        t)  pre="small_"
            ;;
        d)  vd=${OPTARG}
            ;;
        k)  k=${OPTARG}
            ;;
        a)  algo=${OPTARG}
            ;;
    esac
done

python3 -m src.cooccur_matrix.cooccur_matrix --model src/output/d_${vd}_k_${k}_${algo}/${pre}char2vec.bin --corpus corpus/${pre}corpus.txt --clusters src/output/d_${vd}_k_${k}_${algo}/${pre}char2clusters.bin --output src/output/d_${vd}_k_${k}_${algo}/${pre}cooccur_matrix.bin
