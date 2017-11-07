#!/bin/bash

pre=""
k=50
vd=250
algo="k_means"
seg_algo="naive_threshold"

while getopts "td:k:a:s:" opt; do
    case "$opt" in
        t)  pre="small_"
            ;;
        d)  vd=${OPTARG}
            ;;
        k)  k=${OPTARG}
            ;;
        a)  algo=${OPTARG}
            ;;
        s)  seg_algo=${OPTARG}
            ;;
    esac
done

if [ ! -f output/segmentation/${seg_algo}/d_${vd}_k_${k}_${algo}/${pre}seg.txt ]; then
    if [ ! -d output/segmentation/${seg_algo}/d_${vd}_k_${k}_${algo} ]; then
        mkdir output/segmentation/${seg_algo}/d_${vd}_k_${k}_${algo}
    fi

    touch output/segmentation/${seg_algo}/d_${vd}_k_${k}_${algo}/${pre}seg.txt
fi

python3 -m src.segment.${seg_algo} corpus/segmentation/${pre}test.txt --model output/d_${vd}_k_${k}_${algo}/${pre}char2vec.bin --clusters output/d_${vd}_k_${k}_${algo}/${pre}char2clusters.bin --comatrix output/d_${vd}_k_${k}_${algo}/${pre}cooccur_matrix.bin --output output/segmentation/${seg_algo}/d_${vd}_k_${k}_${algo}/${pre}seg.txt
