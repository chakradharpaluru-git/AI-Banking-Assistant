# ==========================================================
# AI Banking Assistant
# Step 12 - Test Loan Prediction Model
# ==========================================================


import os
import pandas as pd
import joblib



# ==========================================================
# Project Paths
# ==========================================================


PROJECT_ROOT = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)


MODEL_PATH = os.path.join(
    PROJECT_ROOT,
    "models",
    "loan_model.pkl"
)


SCALER_PATH = os.path.join(
    PROJECT_ROOT,
    "models",
    "scaler.pkl"
)


DATA_PATH = os.path.join(
    PROJECT_ROOT,
    "datasets",
    "loan_data_encoded.csv"
)



# ==========================================================
# Load Model and Scaler
# ==========================================================


model = joblib.load(
    MODEL_PATH
)


scaler = joblib.load(
    SCALER_PATH
)



# ==========================================================
# Load Feature Names
# ==========================================================


data = pd.read_csv(
    DATA_PATH
)


feature_columns = data.drop(
    "Loan_Status",
    axis=1
).columns.tolist()



print("="*60)
print("MODEL LOADED SUCCESSFULLY")
print("="*60)


print("\nModel Features:")
print(len(feature_columns))

print(feature_columns)



# ==========================================================
# Prediction Function
# ==========================================================


def predict_loan(applicant):


    """
    Predict Loan Eligibility

    Input:
    Applicant dictionary

    Output:
    Approved / Rejected

    """



    # Convert input dictionary to dataframe

    input_df = pd.DataFrame(
        [applicant]
    )



    # Add missing features

    for feature in feature_columns:

        if feature not in input_df.columns:

            input_df[feature] = 0



    # Arrange same order as training

    input_df = input_df[
        feature_columns
    ]



    # Scale features

    input_scaled = scaler.transform(
        input_df
    )



    # Prediction

    prediction = model.predict(
        input_scaled
    )



    if prediction[0] == 1:

        return "Approved"

    else:

        return "Rejected"




# ==========================================================
# Test Model
# ==========================================================


if __name__ == "__main__":



    # Example Applicant

    applicant = {


        "Gender": 1,


        "Married": 1,


        "Education": 0,


        "Self_Employed": 0,


        "ApplicantIncome": 5000,


        "CoapplicantIncome": 0,


        "LoanAmount": 120,


        "Loan_Amount_Term": 360,


        "Credit_History": 1,


        "Dependents_1": 0,


        "Dependents_2": 0,


        "Dependents_3+": 0,


        "Property_Area_Semiurban": 0,


        "Property_Area_Urban": 1

    }



    result = predict_loan(
        applicant
    )



    print("\n")
    print("="*60)
    print("APPLICANT INPUT")
    print("="*60)

    print(applicant)



    print("\n")
    print("="*60)
    print("LOAN PREDICTION RESULT")
    print("="*60)


    print(result)