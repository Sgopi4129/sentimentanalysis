import nltk
from spacy import spacy;
from nltk.stem import PorterStemmer
stemmer=PorterStemmer()
words=["eating","eats","eat","ate","adjustable","rafting","ability","meeting"]

for word in words:
    print(word,"|",stemmer.stem(word))
nlp=spacy.load("en_Core_web_sm")
doc=nlp("eating eats  eat ate adjustable rafting ability meeting better")
for token in doc:
    print(token,"|",token.lemma_)
