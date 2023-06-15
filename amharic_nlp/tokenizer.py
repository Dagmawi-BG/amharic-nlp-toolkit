# -*- coding: utf-8 -*-
from typing import List
import re

def tokenize_words(text: str) -> List[str]:
    """Splits Amharic text into a list of words."""
    text = text.replace('፡', ' ')
    words = text.split()
    return [w.strip() for w in words if w.strip()]

def tokenize_sentences(text: str) -> List[str]:
    """Splits Amharic text into sentences using traditional sentence delimiters."""
    # Delimiters: ። (four dots/period), ፧ (question mark), ፤ (semicolon)
    sentences = re.split(r'[።፧፤\n]', text)
    return [s.strip() for s in sentences if s.strip()]
