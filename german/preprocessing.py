import os

from tqdm import tqdm

import cleantext
from german_lemmatizer import lemmatize
from joblib import Parallel, delayed


def clean(x, **kwargs):
    return cleantext.clean(x, lang="de", **kwargs)


def first_clean(x):
    return clean(x, lower=False, no_line_breaks=True)


def second_clean(x):
    return clean(
        x,
        fix_unicode=False,
        to_ascii=False,
        no_urls=True,
        no_emails=True,
        no_digits=True,
        no_punct=True,
    )


def preprocess(texts, n_jobs=None, remove_stop=True):
    if n_jobs is None:
        n_jobs = os.cpu_count()

    texts = Parallel(n_jobs=n_jobs)(delayed(first_clean)(row) for row in tqdm(texts))
    texts = lemmatize(texts, n_jobs=n_jobs, remove_stop=remove_stop)
    texts = Parallel(n_jobs=n_jobs)(delayed(second_clean)(row) for row in tqdm(texts))
    return texts
