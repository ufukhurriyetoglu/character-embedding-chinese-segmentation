#!/bin/bash

pre=""

while getopts "t" opt; do
    case "$opt" in
        t)  pre="small_"
            ;;
    esac
done

if [ ! -f corpus/wiki_texts.txt ]; then
    echo 'Extracting wiki corpus...'
    python3 -m src.corpus_process.wiki_to_text corpus/zhwiki-latest-pages-articles.xml.bz2 corpus/wiki_texts.txt
fi

echo 'Cleaning corpus...'
python3 -m src.corpus_process.clean_corpus corpus/${pre}wiki_texts.txt > corpus/${pre}clean_wiki_texts.txt

echo 'Converting to traditional Chinese...'
opencc -i corpus/${pre}clean_wiki_texts.txt -o corpus/${pre}corpus.txt -c src/corpus_process/s2t.conf

echo 'Segmenting characters...'
python3 -m src.corpus_process.seg_corpus corpus/${pre}corpus.txt -o corpus/${pre}corpus_seg.txt
