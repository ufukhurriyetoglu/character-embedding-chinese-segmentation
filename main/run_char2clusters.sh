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

echo -e "\t[$INFO] Number of clusters: $k"

python3 -m src.clustering.char2clusters src/output/d_${vd}_k_${k}/${pre}char2vec.bin -k ${k} -o src/output/d_${vd}_k_${k}/${pre}char2clusters.bin
