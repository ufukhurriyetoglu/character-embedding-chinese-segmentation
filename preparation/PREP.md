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

### Chinese Segmentation

###### [Chinese Word Segmentation as Character Tagging](https://pdfs.semanticscholar.org/67d0/e055b2de82743e2c9ea6eece65bf4a03b248.pdf), Computational Linguistics and Chinese Language Processing 2003

- Previous works
  - Purely dictionary-based
    - Maximum matching algorithm
      - Greedy search, walks through a sentence, find the longest matching entry in dictionary
    - Problems
      - Out-of-vocabulary words not dealt with
      - Completeness of the dictionary determines the successfulness of the segmentation
  - Purely statistical approach
    - Algorithm
      - Given a string of characters, the pair of adjacent characters with the largest mutual information greater than a pre-determined threshold is grouped as a word
      - \+ association measures
      - \+ expectation maximization methods
    - Advantages
      - No need dictionary or training data
      - Easily trained on any data source
    - Problems
      - Accuracy
  - Statistical dictionary-based
    - Algorithm 
      - Represents dictionary as weighted finite-state transducer
  - Supervised machine-learning
    - Transformation-based error-driven
      - Compares segmented & undersegmented corpus, finds the rule that achieves the maximum gain
    - Advantages
      - Learn the rules from a corpus
      - Not labor-intensive
    - Problems
      - Not efficient compared with statistical approaches
      
###### [HHMM-based Chinese lexical analyzer ICTCLAS](http://delivery.acm.org/10.1145/1120000/1119280/p184-zhang.pdf?ip=147.8.114.68&id=1119280&acc=OPEN&key=CDD1E79C27AC4E65%2EDE0A32330AE3471B%2E4D4702B0C3E38B35%2E6D218144511F3437&CFID=988281468&CFTOKEN=17668654&__acm__=1506508860_3634cbf323c612589ba39728adc9bfc5), SIGHAN '03 Proceedings of the second SIGHAN workshop on Chinese language processing

###### [Chinese Segmentation and New Word Detection using Conditional Random Fields](https://people.cs.umass.edu/~mccallum/papers/coling04.pdf), COLING '04 Proceedings of the 20th international conference on Computational Linguistics

- Treat Chinese word segmentation as binary decision task (labeled beginning of a word or the continuation of one)

###### [Character-Level Dependencies in Chinese: Usefulness and Learning](http://www.aclweb.org/anthology/E09-1100), EACL '09 Proceedings of the 12th Conference of the European Chapter of the Association for Computational Linguistics

To show that character-level dependency can be a good alternative to word boundary representation for Chinese. Annotated internal dependencies even bring performance enhancement.

1. Word segmentation task can be effectively re-formularized into character-level dependency parsing
2. Consider annotated character dependencies inside a word; a parser can still effectively capture both these annotated internal character dependencies & trivial external dependencies that are transformed from word boundaries
3. A full annotated character dependency tree can be constructed over all possible character pairs within a given sequence

###### [Parsing the Internal Structure of Words: A New Paradigm for Chinese Word Segmentation](http://www.aclweb.org/anthology/P11-1141), HLT '11 Proceedings of the 49th Annual Meeting of the Association for Computational Linguistics: Human Language Technologies

- Intro
  - Current word segmentation recognizes the word boundaries
    - Different annotation standards -> inconsistency
    - Applications have different requirements for granularity of words
    - Many phenomena in Chinese e.g. 大中小學, 游完泳
    - Head driven statistical parsers, dealing with out-of-vocabulary words easier with structure e.g. 英格蘭人
  - Cannot store all word structures in a dictionary -> need dynamic mechanism
- Model
  - Find `argmax` of `T` in joint probability `Pr(T, S)`, `T = parse tree`, `S = raw sentence`
  - Generate `S`
    - Generate constituent structures
    - Generate words with internal structures
    - Generate flat words
where T is a parse tree c
- Dataset
  - Training
    - [Penn Chinese Treebank (CTB) 5.0]()
- Conclusion
  - New paradigm: shift from flat word identification to structure parsing 
    - Statistical parsing technology
    - Development of large scale treebanks

###### [Chinese Parsing Exploiting Characters](http://ir.hit.edu.cn/~car/papers/acl13-chpar.pdf), ACL 2013

- Intro
  - Given an input Chinese sentence, produces its character-level syntax trees
  - Allow word segmentation, part-of-speech (POS) tagging & parsing to be performed jointly using an CKY-style or shift-reduce algorithm
- Model
  - Based on the discriminative shift-reduce parser of [Zhang and Clark (2009; 2011)](), which is a transition-based model for lexicalized constituent parsing; use a beam-search decoder s.t. the transition action sequence can be globally optimized
    - Adding more transition actions
    - Defining novel features that capture character information
- Dataset
  - [CTB5]()
- Evaluation
  - Segmentation, POS tagging & parsing
    - Performed simultaneously
    - Significantly outperforms a pipelined baseline
- Conclusion
  - Annotated the internal structures of Chinese words; extend CTB-style constituent trees into character-level trees using their annotations
  - Developed a character-based parsing model that can produce character-level constituent trees; jointly performs word segmentation, POS tagging & syntactic parsing
  - Improved parsing accuracies compared to pipelined baseline

###### [Max-Margin Tensor Neural Network for Chinese Word Segmentation](http://www.aclweb.org/anthology/P14-1028), Proceedings of the 52nd Annual Meeting of the Association for Computational Linguistics 2014

- Intro
  - Previous work
    - Sequence labeling problem
      - Each character assigned a tag indicating its position in the word
      - Can incorporate a large body of handcrafted features into the models
      - Number of features too large -> models too large for practical use & prone to overfit on training corpus
  - Neural network models
    - Able to minimize the effort in feature engineering
    - Tag-tag, tag-character & character-character interaction not well modeled
    - Features based on linguistic intuition & statistical information can hardly be fully captured relying only on the simple transition score & the single non-linear transformation
- Model
  - Max-Margin Tensor Neural Network `MMTNN`
    - Explicitly models the interactions between tags & context characters by exploiting tag embeddings and tensor-based transformation
    - Tensor factorization
      - Improve efficiency
      - Prevent overfitting
  - Simple character bigram features
    - How far we can go without using feature engineering?
- Evaluation
  - Chinese word segmentation
    - [PKU (second International Chinese Word Segmentation)]() & [MSRA (second International Chinese Word Segmentation)]()
      - Outperform
      - Achieve competitive performance with minimal feature engineering
      
###### [Segmentation-Free Word Embedding for Unsegmented Languages](http://aclweb.org/anthology/D17-1081), EMNLP 2017

Training word embeddings considering __word co-occurrence statistics__ over all possible candidates of segmentations based on __frequent character n-grams__ instead of segmented sentences provided by conventional word segmenters.

### Character-based Word Embedding

#### English

###### [Better Word Representations with Recursive Neural Networks for Morphology](https://nlp.stanford.edu/~lmthang/data/papers/conll13_morpho.pdf), Conference on Computational Natural Language Learning (CoNLL 2013)

- Intro
  - Existing clusterings and embeddings represent well frequent words, but badly model rare ones
  - Treat each morpheme as a basic unit in the RNNs, construct representations for morphologically complex words on the fly from their morphemes
  - Able to build representations for new unseen words comprised of known morphemes
- Model
  - Morphological RNNs `morphoRNN`
    - Context-insensitive Morphological RNN `cimRNN`
    - Context-sensitive Morphological RNN `csmRNN`
      - Stack the `NLM` on top of `morphoRNN`
  - Initializing word representations
    - [C & W (Collobert et al., 2011)]()
    - [HSMN, (Huang et al., 2012)]()
- Dataset
  - Word Similarity Task
    - [WordSim-353 (Finkelstein et al., 2002)]()
    - [MC (Miller and Charles, 1991)]()
    - [RG (Rubenstein and Goodenough, 1965)]()
    - [SCWS*11 (Huang et al., 2012)]()
    - [Rare word (RW) dataset]()
- Evaluation
  - `csmRNN` consistently improves correlations over `cimRNN`
    - Effectiveness of using surrounding contexts in learning both morphological syntactics & semantics
  - Outperforms baselines by a good margin for all datasets (except SCWS*)
  - `cimRNN` 
    - Well enforce structural agreement among related words e.g. return `V-ing` words for `commenting`, `JJ-ness` words for “heartlessness
    - Cluster words sharing the same stem together e.g. `affected` & `unaffected`
  - `csmRNN`
    - Balance well between syntactic & semantic e.g. return `undesired` for `unaffected` but not `unaffected` for `affected`

###### [Compositional Morphology for Word Representations and Language Modelling](http://proceedings.mlr.press/v32/botha14.pdf), ICML'14 Proceedings of the 31st International Conference on International Conference on Machine Learning

- Intro
  - Focus on continuous space language models (CSLM)
  - Strikes a balance between probabilistic language modelling & morphology-based representation learning
  - Executed in the context of a log-bilinear (LBL) LM
  - Sped up by word classing 
- Model
  - Additive log-bilinear model (`LBL++`): additive word representations + log-bilinear language models
    - Vector: imperfection = im + perfect + ion
  - `LBL+o`: factorises output words and retains simple word vectors for the context
  - `LBL+c`: factorises context words
  - Class-based model (`CLBL`)
    - Brown clustering to partition the vocabulary into `|C|` classes
  - `CLBL++`
- Evaluation
  - Word Similarity Rating
    - Outperforming `csmRNN` for one set of embeddings for initialization
    - Simple linear probabilistic model suitable for integration directly into a decoder for translation
    - Trained from scratch on much less data
    - Directly applicable to languages which not yet having those initializations available
  - Machine Translation
    - Improved consistently across six language pairs when using CSLMs during decoding
    - Morphology-based representations led to further improvements beyond the level of optimiser variance only for `English → Czech`

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
- Evaluation
  - Word similarity & word analogy tasks
    - Slightly bette
  - Not betterenchmark by [Bojanowski et al.](https://arxiv.org/abs/1607.04606)
    - Not better
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
- Evaluation
  - Word relatedness computation & analogical reasoning
    - Enhanced performance
  
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
- Evaluation
  - Word similarity, word analogy, & document classification tasks
    - Outperforms baselines

###### [Learning Character-level Compositionality with Visual Features](http://www.aclweb.org/anthology/P/P17/P17-1188.pdf), ACL 2017

- Intro
  - Models calculating morphologysensitive word representations have been found effective
    - Learn more robust representations for rare words by exploiting morphological patterns
  - Compositionality of sub-character units can be found in logographic writing systems e.g. Han and Kanji characters used in Chinese and Japanese
  - Investigate the feasibility of modeling the compositionality of characters
- Model
  - Character Unicode representation -> its shape as an image
  - Calculate a representation of the image using CNNs
  - Fusion models
    - Early Fusion
    - Late Fusion
    - Fallback Fusion
- Dataset
  - Wikipedia article title in Chinese, Japanese, or Korean
- Evaluation
  - Downstream task: classifying Wikipedia titles for Chinese, Japanese, and Korean
    - Outperforms a baseline model that uses standard character embeddings for instances containing rare characters
- Conclusion
  - Representations effective under low-resource scenarios & complementary with standard character embeddings

## Uncomprehensable

- [Parsing with Compositional Vector Grammars](http://www.socher.org/uploads/Main/SocherBauerManningNg_ACL2013.pdf), ACL 2013

## Open Source Reference

- [Chinese word vectors](https://github.com/candlewill/Chinsese_word_vectors)
  - `Word2vec` and `GloVe` tools to train word vectors for Chinese using data from wikipedia dump
  
## Glossary

- [Out of Vocabulary (OOV)](http://www.festvox.org/bsv/x1407.html)
- [Morphologically Rich Languages (MRL)](https://www.quora.com/When-is-a-language-said-to-be-morphologically-rich)
- [Byte pair encoding](https://en.wikipedia.org/wiki/Byte_pair_encoding)
- Continuous Space Language Models (CSLM) - umbrella term for the LMs that represent words with real-valued vectors
- [Log Bi-linear Model (LBM)](http://blog.leanote.com/post/nanjiang/Log-biliearn-model)
- [Autoencoder](https://www.doc.ic.ac.uk/~js4416/163/website/nlp/)
- [Conditional random field (CRF)](http://www.aclweb.org/anthology/I05-3027) - a statistical sequence modeling framework

## Other Links

- [word2vec Explained: Deriving Mikolov et al.’s Negative-Sampling Word-Embedding Method](https://arxiv.org/pdf/1402.3722v1.pdf)
- [Word and Phrase Representations](https://www.doc.ic.ac.uk/~js4416/163/website/nlp/word-phrase.html)
