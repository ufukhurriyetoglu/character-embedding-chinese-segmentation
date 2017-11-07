#!/bin/bash

pre=""
algo="k_means"
k=50
vd=250

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

echo -e "\t[$INFO] Number of clusters: $k, clustering method: $algo"

python3 -m src.clustering.char2clusters_${algo} output/d_${vd}_k_${k}_${algo}/${pre}char2vec.bin -k ${k} -o output/d_${vd}_k_${k}_${algo}/${pre}char2clusters.bin
