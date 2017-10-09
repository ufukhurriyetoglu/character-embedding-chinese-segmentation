#### Related Work

- Connected component analysis (statistical analysis)
  - Upward concavity
  - Horizontal projection profile
  - Vertical cuts of connected components
- Character segmentation
  - Shape of character
  - Challenges
    - Easy for Chinese, Japanese, etc.
    - Difficult for Arabic, Persian, etc.
- Texture analysis ([Script and Language Identification from Document Images](http://www.bmva.org/bmvc/1997/papers/050/), 1997)
  - Character density
  - Stroke orientation
  - Challenges
    - No results reported on full-page documents that involve variations in layouts and fonts
- Template matching
  - Probabilistic voting on matched templates
  - Challenges
    - Not flexible enough to generalize across large variations in fonts or handwriting styles
- Neural network
  - [Multi-font, Multi-size Large-set Character Recognition using Self-Organizing Neural Network](http://ieeexplore.ieee.org/document/598937/), 1995
    - Orientations of contours
- Linear discriminant analysis
  - Based on 5 simple features of connected component, including relative centroid locations and aspect ratio
  - Challenges
    - Sensitive to large variations across writers and diverse document content
- General challenges
  - Printed text
    - Require precise baseline alignment and word segmentation
    - Employ a combination of hand-picked and trainable features and a variety of decision rules -> hard to extend to new languages

#### Scope

- Source
  - Digital text
  - __Image text__
- Writing type
  - __Printed words__
  - Handwritten words
  - Mixed
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

###### [Language Identification for Handwritten Document Images Using A Shape Codebook](http://www.umiacs.umd.edu/~zhugy/HandwritingLanguageID_PR2009.pdf), 2009

A computational framework for language identification using low-level, segmentation-free, geometrically invariant shape features learned with little supervision.

- Introduction
  - Challenges
    - Handwriting variations due to style, cultural, and personalized differences are typica -> increased the diversity
    - Text lines in handwriting are curvilinear and the gaps between neighboring words and lines are not uniform
    - No well-defined baselines for handwritten text lines, even by linear or piecewise-linear approximation of shapes found in handwritten words
    - Automatic processing of off-line document image content needs to be robust in the presence of unconstrained document layouts, formatting, and image degradations
  - Approach
    - Utilize low-level segmentation-free shape features & structurally indexed shape descriptors
    - Utilize image descriptors built from a codebook of generic shape features that are translation, scale, and rotation invariant
    - Formulate feature partitioning as a graph cuts problem
    - Multi-class SVM classifier

###### [Language identification in document images](http://pagesperso.litislab.fr/cchatelain/wp-content/uploads/sites/8/2016/01/Bar15.pdf), Journal of Imaging Science and Technology 2016

#### Links

- [language-detection library (Java)](https://code.google.com/archive/p/language-detection/)

#### Glossary

- [Optical Character Recognition (OCR)]()
  - Software that can convert document images into electronic text files
- [Document Image Processing (DIP)]()
- [Gabor filters]()
- [Grey level co-occurrence matrices]()
