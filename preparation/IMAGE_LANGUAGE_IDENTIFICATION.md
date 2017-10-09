#### Related Work

- Language features
  - Connected component analysis
    - Upward concavity
  - Character segmentation
    - Shape of character
  - Texture analysis ([Script and Language Identification from Document Images](http://www.bmva.org/bmvc/1997/papers/050/), 1997)
    - Character density
    - Stroke orientation
  - Challenges
    - Accurate character segmentation
      - Easy for Chinese, Japanese, etc.
      - Difficult for Arabic, Persian, etc.
- Neural network
  - [Multi-font, Multi-size Large-set Character Recognition using Self-Organizing Neural Network](http://ieeexplore.ieee.org/document/598937/), 1995
    - Orientations of contours

#### Scope

- Source
  - Digital text
  - __Image text__
- Writing type
  - __Printed words__
  - Handwritten words
- Length of text block
  - Words
  - __Sentences/lines__
  - __Paragraphs__
- Hierarchical classifiers
  - Script/language family classification
    - Shape of individual characters
  - Language classification
    - Language profile
      - Characters/n-gram distribution & sequences of characters/n-gram distribution

#### Papers

###### [Script and Language Identification from Document Images](http://www.bmva.org/bmvc/1997/papers/050/), 1997

- Introduction
  - Most existing work on OCR assumes that the language of the document to be processed is known beforehand
  - Individual OCR tools have been developed to deal best with only one specific language
- Algorithm
  - Gabor filters
  - Grey level co-occurrence matrices
- Advantage
  - No character segmentation or connected component analysis required
  - Small areas of foreign characters, numerals and italicized text in the document does not affect the overall texture of the block extracted
  - Simple, established texture classification techniques have been employed

###### [Language identification in document images](http://pagesperso.litislab.fr/cchatelain/wp-content/uploads/sites/8/2016/01/Bar15.pdf), Journal of Imaging Science and Technology 2016

#### Links

- [language-detection library (Java)](https://code.google.com/archive/p/language-detection/)

#### Glossary

- [Optical Character Recognition (OCR)]()
- [Document Image Processing (DIP)]()
- [Gabor filters]()
- [Grey level co-occurrence matrices]()
