# ==========================================================
# AI Banking Assistant
# Module 7 - Credit Score Prediction
# Step 11 & 12 - Prediction Script
# ==========================================================

import os
import joblib
import pandas as pd

# ==========================================================
# Model Paths
# ==========================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(
    BASE_DIR,
    "models",
    "credit_score_model.pkl"
)

SCALER_PATH = os.path.join(
    BASE_DIR,
    "models",
    "credit_scaler.pkl"
)

ENCODER_PATH = os.path.join(
    BASE_DIR,
    "models",
    "credit_target_encoder.pkl"
)

FEATURE_PATH = os.path.join(
    BASE_DIR,
    "models",
    "credit_feature_names.pkl"
)

# ==========================================================
# Load Saved Objects
# ==========================================================

model = joblib.load(MODEL_PATH)

scaler = joblib.load(SCALER_PATH)

target_encoder = joblib.load(ENCODER_PATH)

feature_names = joblib.load(FEATURE_PATH)

print("=" * 60)
print("CREDIT SCORE MODEL LOADED SUCCESSFULLY")
print("=" * 60)

# ==========================================================
# Prediction Function
# ==========================================================

def predict_credit_score(customer):

    # --------------------------------------
    # Convert Dictionary to DataFrame
    # --------------------------------------

    input_df = pd.DataFrame([customer])

    # --------------------------------------
    # Add Missing Columns
    # --------------------------------------

    for column in feature_names:

        if column not in input_df.columns:

            input_df[column] = 0

    # --------------------------------------
    # Arrange Columns
    # --------------------------------------

    input_df = input_df[feature_names]

    # --------------------------------------
    # Scale Features
    # --------------------------------------

    input_scaled = scaler.transform(input_df)

    # --------------------------------------
    # Predict
    # --------------------------------------

    prediction = model.predict(input_scaled)

    # --------------------------------------
    # Decode Label
    # --------------------------------------

    label = target_encoder.inverse_transform(prediction)[0]

    return label


# ==========================================================
# Test Case 1
# Expected : Good
# ==========================================================

customer_1 = {

    "Age": 30,

    "Annual_Income": 1200000,

    "Monthly_Inhand_Salary": 100000,

    "Num_Bank_Accounts": 2,

    "Num_Credit_Card": 2,

    "Interest_Rate": 8,

    "Num_of_Loan": 1,

    "Delay_from_due_date": 0,

    "Num_of_Delayed_Payment": 0,

    "Changed_Credit_Limit": 5,

    "Outstanding_Debt": 50000,

    "Credit_Utilization_Ratio": 22,

    "Monthly_Balance": 70000

}

# ==========================================================
# Test Case 2
# Expected : Poor
# ==========================================================

customer_2 = {

    "Age": 45,

    "Annual_Income": 300000,

    "Monthly_Inhand_Salary": 25000,

    "Num_Bank_Accounts": 8,

    "Num_Credit_Card": 9,

    "Interest_Rate": 28,

    "Num_of_Loan": 6,

    "Delay_from_due_date": 45,

    "Num_of_Delayed_Payment": 18,

    "Changed_Credit_Limit": -15,

    "Outstanding_Debt": 450000,

    "Credit_Utilization_Ratio": 92,

    "Monthly_Balance": 1000

}

# ==========================================================
# Predict Customer 1
# ==========================================================

result = predict_credit_score(customer_1)

print("\n" + "=" * 60)
print("TEST CASE 1")
print("=" * 60)

print("Annual Income          : ₹12,00,000")
print("Outstanding Debt       : ₹50,000")
print("Credit Utilization     : 22%")
print("Delayed Payments       : 0")

print("\nPredicted Credit Score :", result)

# ==========================================================
# Predict Customer 2
# ==========================================================

result = predict_credit_score(customer_2)

print("\n" + "=" * 60)
print("TEST CASE 2")
print("=" * 60)

print("Annual Income          : ₹3,00,000")
print("Outstanding Debt       : ₹4,50,000")
print("Credit Utilization     : 92%")
print("Delayed Payments       : 18")

print("\nPredicted Credit Score :", result)

print("\n" + "=" * 60)
print("PREDICTION COMPLETED")
print("=" * 60)