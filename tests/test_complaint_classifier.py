# ==========================================================
# AI Banking Assistant
# Module 9 - Complaint Classification
# Step 12 - Test the Model
# ==========================================================

import os
import re
import joblib

# ==========================================================
# Paths
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

print("Model Loaded Successfully")

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
# Test Cases
# ==========================================================

test_cases = [

    {
        "Complaint": "My ATM card has been blocked.",
        "Expected": "Account"
    },

    {
        "Complaint": "Unable to complete KYC verification.",
        "Expected": "KYC"
    },

    {
        "Complaint": "My home loan has not been approved.",
        "Expected": "Loan"
    },

    {
        "Complaint": "Internet banking login is not working.",
        "Expected": "Internet Banking"
    }

]

# ==========================================================
# Run Tests
# ==========================================================

print("\n" + "=" * 70)
print("TESTING MODEL")
print("=" * 70)

correct = 0

for i, test in enumerate(test_cases, start=1):

    prediction = predict_complaint(test["Complaint"])

    print(f"\nExample {i}")
    print("-" * 70)
    print("Input      :", test["Complaint"])
    print("Expected   :", test["Expected"])
    print("Predicted  :", prediction)

    if prediction == test["Expected"]:
        print("Status     : PASS")
        correct += 1
    else:
        print("Status     : FAIL")

# ==========================================================
# Summary
# ==========================================================

print("\n" + "=" * 70)
print("TEST SUMMARY")
print("=" * 70)

print(f"Passed : {correct}/{len(test_cases)}")
print(f"Failed : {len(test_cases) - correct}/{len(test_cases)}")

accuracy = (correct / len(test_cases)) * 100

print(f"Accuracy on Test Cases : {accuracy:.2f}%")

print("\n" + "=" * 70)
print("STEP 12 COMPLETED SUCCESSFULLY")
print("=" * 70)