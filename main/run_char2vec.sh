#!/bin/bash

pre=""
k=50
vd=250

INFO="INFO"

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

echo -e "\t[$INFO] Vector dimension: $vd"

python3 -m src.char2vec.char2vec corpus/${pre}corpus_seg.txt -o src/output/d_${vd}_k_${k}/${pre}char2vec.bin --vectordim ${vd}
