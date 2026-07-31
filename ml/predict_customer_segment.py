# ==========================================================
# AI Banking Assistant
# Module 8 - Customer Segmentation
# Prediction Script
# ==========================================================

import joblib
import pandas as pd

print("=" * 70)
print("LOADING CUSTOMER SEGMENTATION MODEL")
print("=" * 70)

# ==========================================================
# Load Model
# ==========================================================

model = joblib.load("models/customer_segmentation_model.pkl")
scaler = joblib.load("models/customer_scaler.pkl")

print("Model Loaded Successfully")

# ==========================================================
# Feature Order
# MUST MATCH TRAINING
# ==========================================================

feature_order = [

    "Monthly_Inhand_Salary",
    "Num_Bank_Accounts",
    "Num_Credit_Card",
    "Interest_Rate",
    "Delay_from_due_date",
    "Num_Credit_Inquiries",
    "Credit_Utilization_Ratio",
    "Total_EMI_per_month"

]

# ==========================================================
# Cluster Mapping
# ==========================================================

segment_mapping = {

    0: "Premium Customer",

    1: "Regular Customer",

    2: "High Risk Customer",

    3: "Investment Customer"

}

# ==========================================================
# Prediction Function
# ==========================================================

def predict_customer_segment(customer):

    input_df = pd.DataFrame([customer])

    input_df = input_df[feature_order]

    scaled = scaler.transform(input_df)

    cluster = model.predict(scaled)[0]

    return segment_mapping.get(cluster, "Unknown Customer")

# ==========================================================
# Main
# ==========================================================

if __name__ == "__main__":

    customer = {}

    print("\nEnter Customer Details\n")

    for column in feature_order:

        value = float(input(f"{column}: "))

        customer[column] = value

    prediction = predict_customer_segment(customer)

    print("\n" + "="*40)
    print("Predicted Customer Segment")
    print("="*40)

    print(prediction)

    print("\n"+"="*70)
    print("PREDICTION COMPLETED")
    print("="*70)