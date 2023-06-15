import unittest
from amharic_nlp.normalizer import normalize_text
from amharic_nlp.tokenizer import tokenize_words, tokenize_sentences
from amharic_nlp.transliterator import transliterate

class TestAmharicNLP(unittest.TestCase):
    def test_normalize(self):
        self.assertEqual(normalize_text("ሐመልማል"), "ሀመልማል")
        self.assertEqual(normalize_text("ፀሀይ"), "ጸሀይ")
        
    def test_tokenize(self):
        words = tokenize_words("ሀመልማል፡በጣም፡ቆንጆ፡ነው።")
        self.assertEqual(len(words), 4)
        
    def test_transliterate(self):
        self.assertEqual(transliterate("ሰላም"), "selame")

if __name__ == '__main__':
    unittest.main()
