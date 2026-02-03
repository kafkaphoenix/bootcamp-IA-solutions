import string
import re

import nltk
from nltk.corpus import stopwords

import spacy
import spacy_spanish_lemmatizer

nltk.download("stopwords")
nltk.download("punkt")


def clean_query_txt(query: str) -> str:
    query = query.replace("El usuario busca ", "").strip()
    # In a real implementation, more complex cleaning could be done here
    # to remove stopwords, punctuation, etc.
    return query

def clean_query_txt_v2(query: str) -> str:
    # remove irrelevant phrases
    query = query.replace("El usuario busca ", "").strip()

    # # convert to lowercase
    # text = text.lower()

    # # # Remove special characters, numbers, punctuations (except for apostrophes)
    # text = re.sub(r"[^a-zA-Z']", ' ', text)
    
    # # remove extra spaces
    # text = re.sub(r'\s+', ' ', text).strip()
    
    # # Remove stop words (Stop words are common words that do not add much meaning to a sentence, such as "yo", "para mí", etc.)
    # stop_words = set(stopwords.words('spanish'))
    # text_tokens = nltk.word_tokenize(text, language='spanish')
    # filtered_words = [word for word in text_tokens if word not in stop_words]
    # text = ' '.join(filtered_words)

    # # lemmatization
    # nlp = spacy.load("es_core_news_sm")
    # nlp.replace_pipe("lemmatizer", "spanish_lemmatizer")
    # doc = nlp(text)
    # lemmatized_words = [token.lemma_ for token in doc]
    # text = ' '.join(lemmatized_words)

    return query