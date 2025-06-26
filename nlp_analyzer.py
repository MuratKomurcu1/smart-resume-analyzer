import spacy # Natural Language Processing (NLP) library
from keybert import KeyBERT # Keyword extraction library
import yake # Yet Another Keyword Extractor (YAKE) library
import subprocess
import importlib

# en_core_web_sm modeli kurulu değilse yükle
try:
    spacy.load("en_core_web_sm")
except OSError:
    subprocess.run(["python", "-m", "spacy", "download", "en_core_web_sm"])
    
    
nlp = spacy.load("en_core_web_sm") # Load the English NLP model from spaCy
kw_model = KeyBERT() # Initialize KeyBERT model

# Named Entity Recognition (NER)
def extract_named_entities(text):
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    return entities

# Keyword Extraction - YAKE
def extract_keywords_yake(text, top_k=10):
    yake_kw_extractor = yake.KeywordExtractor()
    keywords = yake_kw_extractor.extract_keywords(text)
    return [kw[0] for kw in keywords[:top_k]]

# Keyword Extraction - KeyBERT
def extract_keywords_keybert(text, top_k=10):
    keywords = kw_model.extract_keywords(text, top_n=top_k)
    return [kw[0] for kw in keywords]

# Basit skillset extraction (ön tanımlı kelimeler üzerinden)
def extract_skills(text):
    skill_list = ["Python", "TensorFlow", "Pandas", "SQL", "NLP", "Machine Learning", "Deep Learning", "Git"]
    found_skills = [skill for skill in skill_list if skill.lower() in text.lower()]
    return found_skills
