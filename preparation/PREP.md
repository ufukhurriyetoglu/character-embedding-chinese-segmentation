## Content

1. Schedule
2. Related Works
3. Glossary

## Schedule

||Work|
|:-:|:-|
|Sep|* Background knowledge & related work study</br> * Detailed project plan & strategy|
|Oct - Dec|* work2vec implementation & result visualization</br> * Analysis of word vector relationships</br> * Chinese dictionary construction from vector relationships</br> * Evaluation & refinement|
|Jan - Mar|* Apply techniques to Chinese work segmentation</br> * Evaluation & refinement|
|Apr|* Report|

## Related Works

#### English

###### [Word2Vec using Character n-grams](https://web.stanford.edu/class/cs224n/reports/2761021.pdf), Student report for course CS224n in Stanford University

- Intro
  - `word2vec` difficult for good representations of rare words & dealing with `out of vocabulary` words (treated as `UNK`)
- Model
  - Converting words to n-grams  
  - Computation of word vector representation  
  - Model training & evaluation  
- Dataset
  - Training
    - [text8]()
  - Word similarity
    - [WordSimilarity-353 Test Collection]()
  - Word analogy
    - [Googles word2vec code archive]()
- Conclusion
  - Slightly better in word similarity & word analogy tasks
  - Not better than benchmark by [Bojanowski et al.](https://arxiv.org/abs/1607.04606)
    - Probably due to the amount of data trained on (50M v.s. 17M tokens)
    - `n-gram` can be useful for training over small amount of data

#### Chinese

###### [Joint Learning of Character and Word Embeddings](http://nlp.csai.tsinghua.edu.cn/~lzy/publications/ijcai2015_character.pdf), IJCAI'15 Proceedings of the 24th International Conference on Artificial Intelligence

- Intro
  - Internal characters + external contexts, joint learning of character & word embeddings
- Difficulties
  - Ambiguity of Chinese characters
    - Multiple-prototype: multiple vectors for the same character with different meanings
      - Position-based character embeddings
      - Cluster-based character embeddings
      - Nonparametric cluster-based character embeddings
  - Not semantically compositional Chinese words e.g. transliterated words, single-morpheme multi-character word, entity names
    - Prebuild a word list of those words, treat them as a whole when training
- Model
  - Character-enhanced word embedding model (CWE)
- Dataset
  - Embedding learning
    - [The People’s Daily]()
- Conclusion
  - Enhanced performance in word relatedness computation & analogical reasoning
  
###### [Improved Learning of Chinese Word Embeddings with Semantic Knowledge](https://www.google.com.hk/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&cad=rja&uact=8&ved=0ahUKEwjU946I2prWAhXBG5QKHfifDOkQFggkMAA&url=http%3A%2F%2Fwww.springer.com%2Fcda%2Fcontent%2Fdocument%2Fcda_downloaddocument%2F9783319258157-c2.pdf%3FSGWID%3D0-0-45-1544914-p177761955&usg=AFQjCNGC-pQUxrdY-zZWxk8Rwy9qf1HExw), 14th China National Conference, CCL 2015 and Third International Symposium, NLP-NABD 2015

- Intro
  - Previous morpheme- & character-based models used addition as composition function
  - Design new composition functions using the semantic relations between characters
  - Based on semantic categories and relations derived from `Tongyi Cilin` (a Chinese semantic thesaurus)
- Model
  - Compositional Chinese word embeddings (CCWE)
    - Category-based (C-CCWE)
      - What category the character is in?
    - Relation-based (R-CCWE)
      - What relationship (B biased, E biased, unbiased) is the word of?
- Dataset
  - Embedding learning
    - [The People’s Daily]()
  - Document classification
    - [Chinese Encyclopedia]()
- Conclusion
  - Outperforms baselines on word similarity, word analogy, & document classification tasks

## Open Source Reference

- [Chinese word vectors](https://github.com/candlewill/Chinsese_word_vectors)
  - `Word2vec` and `GloVe` tools to train word vectors for Chinese using data from wikipedia dump
  
## Glossary

- [Out of Vocabulary (OOV)](http://www.festvox.org/bsv/x1407.html)
- [Morphologically Rich Languages (MRL)](https://www.quora.com/When-is-a-language-said-to-be-morphologically-rich)
- [Byte pair encoding](https://en.wikipedia.org/wiki/Byte_pair_encoding)
