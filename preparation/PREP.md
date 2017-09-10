## Content

1. Schedule
2. Related Works
3. Glossary

## Schedule

## Related Works

###### [Improved Learning of Chinese Word Embeddings with Semantic Knowledge](https://www.google.com.hk/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&cad=rja&uact=8&ved=0ahUKEwjU946I2prWAhXBG5QKHfifDOkQFggkMAA&url=http%3A%2F%2Fwww.springer.com%2Fcda%2Fcontent%2Fdocument%2Fcda_downloaddocument%2F9783319258157-c2.pdf%3FSGWID%3D0-0-45-1544914-p177761955&usg=AFQjCNGC-pQUxrdY-zZWxk8Rwy9qf1HExw)

_* 14th China National Conference, CCL 2015 and Third International Symposium, NLP-NABD 2015_

###### [Word2Vec using Character n-grams](https://web.stanford.edu/class/cs224n/reports/2761021.pdf)

_* Student report for course CS224n in Stanford University_

1. Intro
  - __Issues__ of the current `word2vec` model
    - Difficult for good representations of rare words
    - Dealing with `out of vocabulary` words (treated as `UNK`)
      - Especially important in morphologically rich languages
  - Proposed __experiment__
    - `n-grams` enhanced `word2vec` using `skip-gram` approach for English words
  - __Advantages__ of n-gram model
    - Takes into account structure of words
  - __Evaluation method__
    - Compared with conventional skip-gram model baseline
2. Work
  - Model
    - Converting words to n-grams  
      ![](https://github.com/pyliaorachel/word2vec-chinese-dictionary/blob/master/preparation/img/Word2Vec_using_Character_n-grams_1.png?raw=true)
      
    - Computation of word vector representation  
      ![](https://github.com/pyliaorachel/word2vec-chinese-dictionary/blob/master/preparation/img/Word2Vec_using%20Character_n-grams_2.png?raw=true)
      
    - Model training & evaluation  
      ![](https://github.com/pyliaorachel/word2vec-chinese-dictionary/blob/master/preparation/img/Word2Vec_using%20Character_n-grams_3.png?raw=true)
  - Dataset
    - Training
      - `text8`
    - Word similarity
      - `WordSimilarity-353 Test Collection`
    - Word analogy
      - `Googles word2vec code archive`
3. Conclusion
  - Slightly better in word similarity & word analogy tasks
  - Not better than benchmark by [Bojanowski et al.](https://arxiv.org/abs/1607.04606)
    - Probably due to the amount of data trained on (50M v.s. 17M tokens)
    - `n-gram` can be useful for training over small amount of data
4. Future Work
  - Dataset size
  - Languages
  - Extrinsic evaluation

## Glossary

- [Out of Vocabulary (OOV)](http://www.festvox.org/bsv/x1407.html)
- [Morphologically Rich Languages (MRL)](https://www.quora.com/When-is-a-language-said-to-be-morphologically-rich)
- [Byte pair encoding](https://en.wikipedia.org/wiki/Byte_pair_encoding)
