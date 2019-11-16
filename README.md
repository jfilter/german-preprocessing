# German Preprocessing

Preprocess German texts to do some serious natural-language processing.

-   [clean texts](https://github.com/jfilter/clean-text)
-   remove stopwords (as defined by [spaCy](https://github.com/explosion/spaCy/blob/master/spacy/lang/de/stop_words.py))
-   [lemmatize](https://github.com/jfilter/german-lemmatizer)
-   lower-case, and remove all punctions, digits are replaced with "0"

## Installation

`pip install git+https://github.com/jfilter/german-preprocessing#egg=german`

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
