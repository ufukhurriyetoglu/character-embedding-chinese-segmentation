#!/bin/bash

pre=""
vd=250

INFO="INFO"

while getopts "td:" opt; do
    case "$opt" in
        t)  pre="small_"
            ;;
        d)  vd=${OPTARG}
            ;;
    esac
done

echo -e "\t[$INFO] Vector dimension: $vd"

python3 -m src.char2vec.char2vec corpus/${pre}corpus_seg.txt -o src/output/${pre}char2vec.bin --vectordim ${vd}
