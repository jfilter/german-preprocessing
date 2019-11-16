from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

classifiers = [
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "License :: OSI Approved :: MIT License",
    "Topic :: Utilities",
]

setup(
    name="german",
    version="0.1.0",
    description="Preprocess German texts for serious NLP.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jfilter/german-preprocessing",
    author="Johannes Filter",
    author_email="hi@jfilter.de",
    license="MIT",
    packages=["german"],
    classifiers=classifiers,
    install_requires=["german-lemmatizer", "clean-text", "joblib", "tqdm", "unidecode"],
)

