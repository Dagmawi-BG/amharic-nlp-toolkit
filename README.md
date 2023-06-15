# 🐍 Amharic NLP Toolkit

A lightweight Python toolkit for processing, normalizing, and transliterating Amharic (Ge'ez script) text. Designed for preprocessing text in machine learning pipelines and linguistic applications.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)

## Features

- **Text Normalization:** Replaces homophones (sound-alike characters such as `ሐ`, `ኅ`, `ሠ` with standard equivalents `ሀ`, `ሀ`, `ሰ`) to eliminate spelling variations.
- **Word & Sentence Tokenization:** Tokenizes text based on traditional Amharic punctuation marks like `፡` (word separator) and `።` (sentence ender).
- **Stopwords Filter:** Built-in list of common Amharic stopwords for text filtering.
- **Transliteration:** Phonetically maps Ge'ez characters to Latin characters.
- **CLI Utility:** Quick command-line interface for common operations.

## Structure

```
├── amharic_nlp/
│   ├── __init__.py
│   ├── normalizer.py
│   ├── stopwords.py
│   ├── tokenizer.py
│   └── transliterator.py
├── tests/
│   └── test_nlp.py
├── cli.py
├── setup.py
└── requirements.txt
```

## Installation

```bash
git clone https://github.com/Dagmawi-BG/amharic-nlp-toolkit.git
cd amharic-nlp-toolkit
pip install -e .
```

## Usage

### Python API

```python
from amharic_nlp.normalizer import normalize_text
from amharic_nlp.transliterator import transliterate

text = "ፀሀይ፡በጣም፡ሙቅ፡ናት።"
normalized = normalize_text(text)
print(normalized)  # Output: ጸሀይ በጣም ሙቅ ናት።

trans = transliterate("ሰላም")
print(trans)  # Output: selame
```

### CLI

```bash
python3 cli.py normalize --text "ሐመልማል"
# Output: ሀመልማል
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
