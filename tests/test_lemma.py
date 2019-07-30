import os
import pathlib
import shutil

import pytest

import german


def test_lemma():
    res = german.lemmatize(["Johannes war einer von vielen guten Schülern."])
    assert list(res) == ["Johannes sein einer von vielen gut Schüler."]


def test_preproc():
    res = german.preprocess(
        [
            "Johannes war einer von vielen guten Schülern.",
            "Johannes war einer von vielen guten Schülern.",
        ]
    )
    assert list(res) == ["johannes gut schüler"] * 2
