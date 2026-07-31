import os
import joblib
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

MODEL_PATH = os.path.join(BASE_DIR, "models", "loan_model.pkl")
SCALER_PATH = os.path.join(BASE_DIR, "models", "scaler.pkl")
DATA_PATH = os.path.join(BASE_DIR, "datasets", "loan_data_encoded.csv")

# Load model and scaler
model = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)

# Load feature names
data = pd.read_csv(DATA_PATH)
feature_columns = data.drop("Loan_Status", axis=1).columns.tolist()


def predict_loan(data):

    applicant = {
        "Gender": data["gender"],
        "Married": data["married"],
        "Education": data["education"],
        "Self_Employed": data["self_employed"],
        "ApplicantIncome": data["applicant_income"],
        "CoapplicantIncome": data["coapplicant_income"],
        "LoanAmount": data["loan_amount"],
        "Loan_Amount_Term": data["loan_amount_term"],
        "Credit_History": data["credit_history"],
        "Dependents_1": data["dependents_1"],
        "Dependents_2": data["dependents_2"],
        "Dependents_3+": data["dependents_3_plus"],
        "Property_Area_Semiurban": data["property_area_semiurban"],
        "Property_Area_Urban": data["property_area_urban"],
    }

    input_df = pd.DataFrame([applicant])

    for col in feature_columns:
        if col not in input_df.columns:
            input_df[col] = 0

    input_df = input_df[feature_columns]

    input_scaled = scaler.transform(input_df)

    prediction = model.predict(input_scaled)

    return "Approved" if prediction[0] == 1 else "Rejected"
