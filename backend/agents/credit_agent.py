from pathlib import Path

import joblib
import pandas as pd

from backend.agents.state import AgentState


# =====================================================
# Project Root
# =====================================================

BASE_DIR = Path(__file__).resolve().parents[2]


MODEL_PATH = BASE_DIR / "models" / "credit_score_model.pkl"

SCALER_PATH = BASE_DIR / "models" / "credit_scaler.pkl"

ENCODER_PATH = BASE_DIR / "models" / "credit_target_encoder.pkl"

FEATURE_PATH = BASE_DIR / "models" / "credit_feature_names.pkl"



# =====================================================
# Lazy Loaded Resources
# =====================================================

model = None
scaler = None
encoder = None
feature_names = None



def load_credit_resources():

    global model
    global scaler
    global encoder
    global feature_names


    if model is None:


        if (
            MODEL_PATH.exists()
            and SCALER_PATH.exists()
            and ENCODER_PATH.exists()
            and FEATURE_PATH.exists()
        ):


            model = joblib.load(
                MODEL_PATH
            )


            scaler = joblib.load(
                SCALER_PATH
            )


            encoder = joblib.load(
                ENCODER_PATH
            )


            feature_names = joblib.load(
                FEATURE_PATH
            )


            print(
                "✅ Credit Model Loaded Successfully"
            )


        else:


            print(
                f"⚠️ Credit Model Files Not Found: {MODEL_PATH}"
            )



    return (
        model,
        scaler,
        encoder,
        feature_names
    )



# =====================================================
# Credit Agent
# =====================================================

def credit_agent(state: AgentState):


    model, scaler, encoder, feature_names = (
        load_credit_resources()
    )



    if model is None:


        state["response"] = (
            "Credit score model is not available."
        )


        state["final_answer"] = (
            state["response"]
        )


        return state




    customer = {


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



    df = pd.DataFrame(
        [customer]
    )



    for col in feature_names:

        if col not in df.columns:

            df[col] = 0



    df = df[
        feature_names
    ]



    scaled = scaler.transform(
        df
    )



    prediction = model.predict(
        scaled
    )



    label = encoder.inverse_transform(
        prediction
    )[0]



    response = (
        f"Predicted Credit Score: {label}"
    )


    state["response"] = response

    state["final_answer"] = response


    return state