# ==========================================================
# AI Banking Assistant
# Module 6 - Fraud Detection
# Step 13 - Test the Saved Fraud Detection Model
# ==========================================================

import os
import joblib
import pandas as pd

# ==========================================================
# Project Paths
# ==========================================================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MODEL_PATH = os.path.join(BASE_DIR, "models", "fraud_model.pkl")

# ==========================================================
# Check Model
# ==========================================================

if not os.path.exists(MODEL_PATH):

    print("=" * 60)
    print("ERROR")
    print("=" * 60)
    print("fraud_model.pkl not found.")
    print(MODEL_PATH)
    exit()

# ==========================================================
# Load Model
# ==========================================================

model = joblib.load(MODEL_PATH)

print("=" * 60)
print("FRAUD MODEL LOADED SUCCESSFULLY")
print("=" * 60)

print(model)

# ==========================================================
# Feature Names
# ==========================================================

feature_columns = [

    "Time",

    "V1","V2","V3","V4","V5","V6","V7","V8","V9",

    "V10","V11","V12","V13","V14","V15","V16",

    "V17","V18","V19","V20","V21","V22","V23",

    "V24","V25","V26","V27","V28",

    "Amount"

]

# ==========================================================
# Prediction Function
# ==========================================================

def predict_transaction(transaction):

    df = pd.DataFrame([transaction])

    df = df[feature_columns]

    prediction = model.predict(df)[0]

    if hasattr(model, "predict_proba"):

        probability = model.predict_proba(df)[0]

        genuine_prob = probability[0]

        fraud_prob = probability[1]

    else:

        genuine_prob = None

        fraud_prob = None

    return prediction, genuine_prob, fraud_prob


# ==========================================================
# Example 1
# Expected : Genuine
# ==========================================================

example1 = {

    "Time":12000,

    "V1":-1.359807,
    "V2":-0.072781,
    "V3":2.536346,
    "V4":1.378155,
    "V5":-0.338321,
    "V6":0.462388,
    "V7":0.239599,
    "V8":0.098698,
    "V9":0.363787,
    "V10":0.090794,
    "V11":-0.551600,
    "V12":-0.617801,
    "V13":-0.991390,
    "V14":-0.311169,
    "V15":1.468177,
    "V16":-0.470401,
    "V17":0.207971,
    "V18":0.025791,
    "V19":0.403993,
    "V20":0.251412,
    "V21":-0.018307,
    "V22":0.277838,
    "V23":-0.110474,
    "V24":0.066928,
    "V25":0.128539,
    "V26":-0.189115,
    "V27":0.133558,
    "V28":-0.021053,

    "Amount":120

}

prediction, genuine, fraud = predict_transaction(example1)

print("\n")
print("=" * 60)
print("TEST CASE 1")
print("=" * 60)

print("Expected : Genuine")

if prediction == 0:

    print("Prediction : Genuine")

else:

    print("Prediction : Fraud")

if genuine is not None:

    print(f"Genuine Probability : {genuine:.4f}")

    print(f"Fraud Probability    : {fraud:.4f}")

# ==========================================================
# Example 2
# Expected : Fraud
# ==========================================================

example2 = {

    "Time":230000,

    "V1":-15,
    "V2":12,
    "V3":-18,
    "V4":8,
    "V5":-12,
    "V6":6,
    "V7":-14,
    "V8":10,
    "V9":-9,
    "V10":12,
    "V11":-7,
    "V12":9,
    "V13":-5,
    "V14":-11,
    "V15":-6,
    "V16":8,
    "V17":-13,
    "V18":7,
    "V19":-5,
    "V20":9,
    "V21":-8,
    "V22":5,
    "V23":-4,
    "V24":2,
    "V25":-3,
    "V26":4,
    "V27":-5,
    "V28":2,

    "Amount":95000

}

prediction, genuine, fraud = predict_transaction(example2)

print("\n")
print("=" * 60)
print("TEST CASE 2")
print("=" * 60)

print("Expected : Fraud")

if prediction == 1:

    print("Prediction : Fraud")

else:

    print("Prediction : Genuine")

if genuine is not None:

    print(f"Genuine Probability : {genuine:.4f}")

    print(f"Fraud Probability    : {fraud:.4f}")

# ==========================================================
# Completed
# ==========================================================

print("\n")
print("=" * 60)
print("MODEL TEST COMPLETED SUCCESSFULLY")
print("=" * 60)