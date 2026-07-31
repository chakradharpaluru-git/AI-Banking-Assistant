# ==========================================================
# AI Banking Assistant
# Module 9 - Complaint Classification
# Step 11 - Prediction Script
# ==========================================================

import os
import re
import joblib

# ==========================================================
# Model Paths
# ==========================================================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MODEL_PATH = os.path.join(BASE_DIR, "models", "complaint_classifier.pkl")
VECTORIZER_PATH = os.path.join(BASE_DIR, "models", "tfidf_vectorizer.pkl")

# ==========================================================
# Load Model
# ==========================================================

print("=" * 70)
print("LOADING COMPLAINT CLASSIFICATION MODEL")
print("=" * 70)

classifier = joblib.load(MODEL_PATH)
tfidf = joblib.load(VECTORIZER_PATH)

print("\nModel Loaded Successfully")

# ==========================================================
# Text Preprocessing
# ==========================================================

def preprocess_text(text):

    text = text.lower()

    text = re.sub(r"\d+", "", text)

    text = re.sub(r"[^a-zA-Z\s]", "", text)

    text = re.sub(r"\s+", " ", text).strip()

    return text

# ==========================================================
# Prediction Function
# ==========================================================

def predict_complaint(text):

    cleaned = preprocess_text(text)

    vector = tfidf.transform([cleaned])

    prediction = classifier.predict(vector)[0]

    return prediction

# ==========================================================
# User Input
# ==========================================================

print("\nEnter Your Complaint\n")

complaint = input("Complaint : ")

result = predict_complaint(complaint)

print("\n" + "=" * 70)
print("PREDICTED CATEGORY")
print("=" * 70)

print(result)

print("\n" + "=" * 70)
print("PREDICTION COMPLETED")
print("=" * 70)