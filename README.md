## Chinese Dictionary Construction using word2vec

###### Abstract

The aim is to construct a Chinese dictionary from large Chinese corpora using character-based word2vec technique.  

The motivation of this project is to avoid maintaining a dictionary by man power, and to catch more slangs that are unlikely to be included in those dictionaries.  

The dictionary is useful in various further NLP tasks such as Chinese word segmentation. A variation of this project is to directly use the vectors learned to segment Chinese words without intermediate dictionaries. An extension of this project is to find out some interesting language features in Chinese from the result of word2vec.

###### Description

_* Brief intro to `word2vec`: [word2vec](https://deeplearning4j.org/word2vec) is a kind of model that takes a corpus as input and outputs a set of feature vectors that can be projected in a latent space of N dimensions. It is extremely useful since vectors that have smaller cosine distance tend to have higher similarities, and hence word2vec is being used in various NLP deep learning tasks. The classical task using word2vec is to predict target word given some context, or predict context given a target word. Also, interesting relationships e.g. 'man' - 'woman' = 'king' - 'queen' can be identified in the space._
    
As compared to English, NLP in Chinese requires an additional preprocessing stage, i.e. segment the text into sequence of words, before they can be used in subsequent NLP tasks, including input into word2vec. There are various ways for Chinese word segmentation, but all of them need a dictionary beforehand. Maintaining the dictionary requires additional man power, and the dictionary tend not to be exhaustive enough, for example, it tend to miss some internet slangs.  

This project is to actually build a Chinese dictionary from some known Chinese corpora using `word2vec` technique. Almost all `word2vec` application targeting on Chinese text tend to segment them into words first, however, Chinese in character unit also can have meanings. If we segment the text into characters, which is an extremely easy task, and feed them into word2vec, there would definitely be something interesting in the output space. Then maybe we can slice the text into 2-character units, and find out valid 2-character words from the frequency information, then based on the individual characters in the words and their position in the space, some cluster-to-cluster relationship may be found, and we can use it to construct possible dictionary words. For example, we have 校 in a cluster, 狗 in a cluster, and 校狗 is found to be a valid word; then we can somehow imply that if 貓 is in the same cluster as 狗, 校貓 is probably a valid word as well and can be included the dictionary, even though it doesn’t appear in the input corpus. This way some informal but reasonable words can be better catched.  
    
As we play with character-based chinese word2vec space, some more interesting features may be identified as well, e.g. 徘 and 徊 should be almost overlapping in the space, since they are indivisible words.

## About This Repo

```
/preparation    # pre-work information e.g. schedule, related work research, etc.
/main           # main project e.g. source code, report, etc.
```
