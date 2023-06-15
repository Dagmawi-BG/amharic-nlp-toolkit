# -*- coding: utf-8 -*-
from typing import List

AMHARIC_STOPWORDS = {
    'እና', 'ግን', 'ወደ', 'ላይ', 'ታች', 'ውስጥ', 'ጋር', 'ስለ', 'ነገር', 'ምክንያት',
    'እንደ', 'ብቻ', 'ደግሞ', 'ነበር', 'በጣም', 'ሁሉ', 'አንድ', 'ይህ', 'ያ', 'እስከ',
    'ጋራ', 'ነበረ', 'ሆነ', 'ናቸው', 'ነው', 'አይደለም', 'በኩል', 'ጋር'
}

def remove_stopwords(words: List[str]) -> List[str]:
    """Filters out common Amharic stopwords from a list of words."""
    return [w for w in words if w not in AMHARIC_STOPWORDS]
