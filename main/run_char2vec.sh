#!/bin/bash

pre=""
k=50
vd=250
algo="k_means"

INFO="INFO"

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

echo -e "\t[$INFO] Vector dimension: $vd"

python3 -m src.char2vec.char2vec corpus/${pre}corpus_seg.txt -o output/d_${vd}_k_${k}_${algo}/${pre}char2vec.bin --vectordim ${vd}
