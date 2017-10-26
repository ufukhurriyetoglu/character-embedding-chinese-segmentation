#!/bin/bash

if [ ! -f corpus/wiki_texts.txt ]; then
    echo 'Extracting wiki corpus...'
    python3 -m src.corpus_process.wiki_to_text corpus/zhwiki-latest-pages-articles.xml.bz2 corpus/wiki_texts.txt
fi

echo 'Cleaning corpus...'
python3 -m src.corpus_process.clean_corpus corpus/small_wiki_texts.txt > corpus/small_clean_wiki_texts.txt

echo 'Converting to traditional Chinese...'
opencc -i corpus/small_clean_wiki_texts.txt -o corpus/small_corpus.txt -c src/corpus_process/s2t.conf

echo 'Segmenting characters...'
python3 -m src.corpus_process.seg_corpus corpus/small_corpus.txt -o corpus/small_corpus_seg.txt
