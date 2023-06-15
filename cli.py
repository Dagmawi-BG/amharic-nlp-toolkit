#!/usr/bin/env python3
import argparse
from amharic_nlp.normalizer import normalize_text
from amharic_nlp.tokenizer import tokenize_words, tokenize_sentences
from amharic_nlp.transliterator import transliterate

def main():
    parser = argparse.ArgumentParser(description="Amharic Natural Language Processing Toolkit CLI")
    parser.add_argument("action", choices=["normalize", "tokenize", "transliterate"], help="NLP action to perform")
    parser.add_argument("--text", required=True, help="Input Amharic text")
    args = parser.parse_args()
    
    if args.action == "normalize":
        print(normalize_text(args.text))
    elif args.action == "tokenize":
        words = tokenize_words(args.text)
        sentences = tokenize_sentences(args.text)
        print(f"Sentences ({len(sentences)}): {sentences}")
        print(f"Words ({len(words)}): {words}")
    elif args.action == "transliterate":
        print(transliterate(args.text))

if __name__ == "__main__":
    main()
