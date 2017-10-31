#!/bin/bash

pre=""
k=50

INFO="INFO"

while getopts "tk:" opt; do
    case "$opt" in
        t)  pre="small_"
            ;;
        k)  k=${OPTARG}
            ;;
    esac
done

echo -e "\t[$INFO] Number of clusters: $k"

python3 -m src.clustering.char2clusters src/output/${pre}char2vec.bin -k ${k} -o src/output/${pre}char2clusters.bin
