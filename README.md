# German Preprocessing [![Build Status](https://travis-ci.com/jfilter/german-preprocessing.svg?branch=master)](https://travis-ci.com/jfilter/german-preprocessing) [![PyPI](https://img.shields.io/pypi/v/german.svg)](https://pypi.org/project/german/) [![PyPI - Python Version](https://img.shields.io/pypi/pyversions/german.svg)](https://pypi.org/project/german/)

Preprocess German texts to do some serious natural-language processing.

-   [clean texts](https://github.com/jfilter/clean-text)
-   remove stopwords (as defined by [spaCy](https://github.com/explosion/spaCy/blob/master/spacy/lang/de/stop_words.py))
-   [lemmatize](https://github.com/jfilter/german-lemmatizer)
-   lower-case, and remove all punctions, digits are replaced with "0"

## Installation

`pip install german`

## Usage

```python
from german import preprocess

preprocess(['Johannes war einer von vielen guten Schülern.', 'Julia trinkt gern Tee.'], remove_stop=True)
# ['johannes gut schüler', 'julia trinken tee']
```

## License

MIT.

## Sponsoring

This work was created as part of a [project](https://github.com/jfilter/ptf) that was funded by the German [Federal Ministry of Education and Research](https://www.bmbf.de/en/index.html).

<img src="./bmbf_funded.svg">
