import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from spacy.tokens import Doc

# Load English language model
nlp = spacy.load("en_core_web_sm", disable=["ner"])

# Custom tokenization pipeline
def custom_tokenizer(text):
    doc = nlp(text)
    tokens = [token.lemma_.lower() for token in doc if token.text.lower() not in STOP_WORDS and not token.is_punct]
    return tokens

# Preprocess text
def preprocess_text(text):
    # Custom tokenization
    tokens = custom_tokenizer(text)
    return " ".join(tokens)