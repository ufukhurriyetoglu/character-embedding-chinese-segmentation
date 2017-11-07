#!/bin/bash


#
# Get opts
#

test=""
vd=250
k=50
preprocess=0
char2vec=0
algo="k_means"
seg_algo="naive_threshold"

while getopts "tpcd:k:a:s:" opt; do
    case "$opt" in
        t)  test="-t"
            ;;
        p)  preprocess=1
            ;;
        c)  char2vec=1
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

start=`date +%s`
end_0=`date +%s`
end_1=$end_0

MAIN="MAIN"
TIME="TIME"

#
# Preprocess
#

if [ $preprocess -eq 1 ]; then
    echo "[$MAIN] Preprocessing..."
    ./run_corpus_process.sh $test
    
    end_0=`date +%s`
    end_1=$end_0
    echo "[$TIME] Duration for preprocessing: $(((end_0 - start) / 60)) min"
fi

if [ ! -d output/d_${vd}_k_${k}_${algo} ]; then
    mkdir output/d_${vd}_k_${k}_${algo}
fi

# Char2vec

if [ $char2vec -eq 1 ]; then
    echo "[$MAIN] Char2vec training..."
    ./run_char2vec.sh $test -d $vd -k $k -a $algo

    end_1=`date +%s`
    echo "[$TIME] Duration for char2vec: $(((end_1 - end_0) / 60)) min"
fi

# Char2clusters

echo "[$MAIN] Char2clusters training..."
end_2=`date +%s`
./run_char2clusters.sh $test -d $vd -k $k -a $algo

echo "[$TIME] Duration for char2clusters: $(((end_2 - end_1) / 60)) min"

# Cooccurrence matrix

echo "[$MAIN] Cooccurrence matrix calculating..."
./run_cooccur_matrix.sh $test -d $vd -k $k -a $algo

end_3=`date +%s`
echo "[$TIME] Duration for cooccurrence matrix: $(((end_3 - end_2) / 60)) min"


end=`date +%s`

echo "[$TIME] Total duration: $(((end-start) / 60)) min"
