#!/bin/bash

if [ ! -f ../../corpus/wiki_texts.txt ]; then
    echo 'Extracting wiki corpus...'
    python3 wiki_to_text.py ../../corpus/zhwiki-latest-pages-articles.xml.bz2 ../../corpus/wiki_texts.txt
fi

echo 'Cleaning corpus...'
python3 clean_corpus.py ../../corpus/wiki_texts.txt > ../../corpus/clean_wiki_texts.txt

echo 'Converting to traditional Chinese...'
opencc -i ../../corpus/clean_wiki_texts.txt -o ../../corpus/corpus.txt -c s2t.conf

echo 'Segmenting characters...'
python3 seg_corpus.py ../../corpus/corpus.txt -o ../../corpus/corpus_seg.txt
