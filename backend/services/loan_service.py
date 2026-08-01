import os
import joblib
import pandas as pd



# =====================================================
# BASE DIRECTORY
# =====================================================

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.dirname(__file__)
    )
)



# =====================================================
# MODEL PATHS
# =====================================================

MODEL_PATH = os.path.join(
    BASE_DIR,
    "models",
    "loan_model.pkl"
)


SCALER_PATH = os.path.join(
    BASE_DIR,
    "models",
    "scaler.pkl"
)


DATA_PATH = os.path.join(
    BASE_DIR,
    "datasets",
    "loan_data_encoded.csv"
)



# =====================================================
# GLOBAL VARIABLES
# =====================================================

model = None

scaler = None

feature_columns = None



# =====================================================
# LOAD MODEL RESOURCES
# =====================================================

def load_resources():

    global model
    global scaler
    global feature_columns


    if model is None:


        model = joblib.load(
            MODEL_PATH
        )


        scaler = joblib.load(
            SCALER_PATH
        )


        data = pd.read_csv(
            DATA_PATH
        )


        feature_columns = (
            data
            .drop(
                "Loan_Status",
                axis=1
            )
            .columns
            .tolist()
        )


        print("Loan Model Loaded Successfully")



    return (
        model,
        scaler,
        feature_columns
    )



# =====================================================
# LOAN PREDICTION SERVICE
# =====================================================

def predict_loan(data):


    model, scaler, feature_columns = load_resources()



    # ==============================================
    # CREATE INPUT DATA
    # ==============================================

    applicant = {


        "Gender":
            data["gender"],


        "Married":
            data["married"],


        "Education":
            data["education"],


        "Self_Employed":
            data["self_employed"],


        "ApplicantIncome":
            data["applicant_income"],


        "CoapplicantIncome":
            data["coapplicant_income"],


        "LoanAmount":
            data["loan_amount"],


        "Loan_Amount_Term":
            data["loan_amount_term"],


        "Credit_History":
            data["credit_history"],


        "Dependents_1":
            data["dependents_1"],


        "Dependents_2":
            data["dependents_2"],


        "Dependents_3+":
            data["dependents_3_plus"],


        "Property_Area_Semiurban":
            data["property_area_semiurban"],


        "Property_Area_Urban":
            data["property_area_urban"],

    }



    input_df = pd.DataFrame(
        [applicant]
    )



    # ==============================================
    # MATCH TRAINING FEATURES
    # ==============================================

    for col in feature_columns:

        if col not in input_df.columns:

            input_df[col] = 0



    input_df = input_df[
        feature_columns
    ]



    # ==============================================
    # SCALE INPUT
    # ==============================================

    input_scaled = scaler.transform(
        input_df
    )



    # ==============================================
    # PREDICTION
    # ==============================================

    prediction = model.predict(
        input_scaled
    )[0]



    # ==============================================
    # CONFIDENCE
    # ==============================================

    confidence = None


    if hasattr(
        model,
        "predict_proba"
    ):


        probabilities = model.predict_proba(
            input_scaled
        )[0]


        confidence = float(
            max(probabilities)
        )



    # ==============================================
    # FINAL RESULT
    # ==============================================

    result = (

        "Loan Approved"

        if prediction == 1

        else

        "Loan Rejected"

    )



    return {

        "prediction": result,

        "confidence": confidence

    }