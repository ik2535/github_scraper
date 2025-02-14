import os
from transformers import pipeline
from difflib import SequenceMatcher
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize similarity model
similarity_model = pipeline("feature-extraction", model="sentence-transformers/all-mpnet-base-v2")

def compute_similarity(code1, code2):
    """Computes similarity between two code snippets."""
    embedding1 = similarity_model(code1)[0][0]
    embedding2 = similarity_model(code2)[0][0]
    return SequenceMatcher(None, code1, code2).ratio()  # Alternative: Cosine similarity
