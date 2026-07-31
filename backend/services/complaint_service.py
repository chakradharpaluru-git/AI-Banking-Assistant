# ==========================================================
# AI Banking Assistant
# Complaint Classification Service
# ==========================================================

import os
import re
import joblib

# ==========================================================
# Project Root
# ==========================================================

BASE_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..")
)

MODEL_PATH = os.path.join(
    BASE_DIR,
    "models",
    "complaint_classifier.pkl"
)

VECTORIZER_PATH = os.path.join(
    BASE_DIR,
    "models",
    "tfidf_vectorizer.pkl"
)

# ==========================================================
# Load Model
# ==========================================================

classifier = joblib.load(MODEL_PATH)
tfidf = joblib.load(VECTORIZER_PATH)

print("=" * 60)
print("COMPLAINT CLASSIFIER LOADED")
print("=" * 60)

# ==========================================================
# Text Cleaning
# ==========================================================

def preprocess_text(text: str):

    text = text.lower()

    text = re.sub(r"\d+", "", text)

    text = re.sub(r"[^a-zA-Z\s]", "", text)

    text = re.sub(r"\s+", " ", text).strip()

    return text


# ==========================================================
# Prediction Function
# ==========================================================

def classify_complaint(text: str) -> str:

    cleaned = preprocess_text(text)

    vector = tfidf.transform([cleaned])

    prediction = classifier.predict(vector)[0]

    return str(prediction)
