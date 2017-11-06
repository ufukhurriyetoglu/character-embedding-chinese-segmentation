## Usage

#### `corpus_process`

- `wiki_to_text.py`: extract wiki corpus from XML
    ```bash
    $ python3 wiki_to_text.py <raw-dump> <output-file-name> 
    ```

- `clean_corpus.py`: clean corpus, remove non-chinese characters & replace spaces with 'p's 
    ```bash
    $ python3 clean_corpus.py <extracted-wiki-file> > <output-file-name> 
    ```

- `seg_corpus.py`: segment corpus into characters separated by space (for word2vec to process) 
    ```bash
    $ python3 seg_corpus.py <corpus-file-name> -o <output-file-name> 
    ```

#### `char2vec`   

- `char2vec.py`: char2vec trainer
    ```bash
    $ python3 char2vec.py <corpus-file> -o <output-model-name> [--vectordim <vector-dimension>]
    ```

- `visualize.py`: char2vec visualization
    ```bash
    $ python3 visualize_vec.py <model-name>

    # interactive interface
    >>> Input a Chinese character (q to quit):
    的

    >>>
    數: 0.999819815158844   [ 0.72170001 -0.00357776]
    學: 0.9997885823249817  [ 0.63855296  0.00435965]
    基: 0.999778687953949   [  4.49367970e-01  -8.63740788e-05]
    中: 0.9997752904891968  [ 0.53253031 -0.00289603]
    不: 0.999743640422821   [ 0.41746774 -0.0021561 ]
    為: 0.9997429847717285  [ 0.50866777 -0.00120577]
    以: 0.9997390508651733  [ 0.36837152 -0.00215767]
    究: 0.9997353553771973  [ 0.41495565  0.0049392 ]
    爾: 0.9997234344482422  [ 0.48267803  0.00375513]
    -----------------------------------------------------------------------
    的: [ 1.02621961 -0.00103056]
    數: [ 0.72170001 -0.00357776]
    學: [ 0.63855296  0.00435965]
    基: [  4.49367970e-01  -8.63740788e-05]
    中: [ 0.53253031 -0.00289603]
    不: [ 0.41746774 -0.0021561 ]
    為: [ 0.50866777 -0.00120577]
    以: [ 0.36837152 -0.00215767]
    究: [ 0.41495565  0.0049392 ]
    爾: [ 0.48267803  0.00375513]
    -----------------------------------------------------------------------    
    >>> 
    ```

#### `clustering`

- `char2clusters.py`: clustering char vectors
    ```bash
    $ python3 char2clusters.py <model-file> -k <num-of-clusters> --all >> <output-file-name>

    # or interactive interface

    $ python3 char2clusters.py <model-file> -k <num-of-clusters>

    >>> Input a Chinese character (q to quit):
    工

    >>>
    學,論,研,和,大,上,實,其,現,構,領,亦,念,幾,使,許,種,析,自,詞,今,文,書,成,得,德,確,與,加,開,源,斯,系,美,臘,重,曼,通,全,抽,天,致,向,程,工,
    >>>
    ```

#### `cooccur_matrix`

- `cooccur_matrix.py`: building cluster-to-cluster cooccurrence matrix
    ```bash
    $ python3 cooccur_matrix.py --model <model-file> --clusters <cluster-file> --corpus <corpus-file> -o <output-file-name> 
    ``` 

- `visualize.py`: connection strength visualization
    ```bash
    $ python3 visualize.py --model <model-name> --clusters <cluster-f-name> --comatrix <cooccur-matrix-f-name>

    # interactive interface
    >>> Input a Chinese sentence (q to quit):
    今天天氣真好
    ```

## Notes

Interchanging between `gensim` and `word2vec`:

|gensim|word2vec|
|-|-|
|`from gensim.models import Word2Vec`|`import word2vec`|
|`model.wv.index2word.index(char)`|`model.ix(char)`|
|`model.syn0`|`model.vectors`|
|`model.wv.index2word(char_idx)`|`model.vocab[char_idx]`|
