from pathlib import Path

import joblib
import pandas as pd

from backend.agents.state import AgentState


# =====================================================
# Paths
# =====================================================

BASE_DIR = Path(__file__).resolve().parents[2]

MODEL_PATH = BASE_DIR / "models" / "loan_model.pkl"
SCALER_PATH = BASE_DIR / "models" / "scaler.pkl"


# =====================================================
# Load Model
# =====================================================

loan_model = None
scaler = None


if MODEL_PATH.exists():

    loan_model = joblib.load(
        MODEL_PATH
    )

    scaler = joblib.load(
        SCALER_PATH
    )

    print("Loan Agent Model Loaded")

else:

    print("Loan Model Not Found")


# =====================================================
# Loan Agent
# =====================================================

def loan_agent(state: AgentState) -> AgentState:


    if loan_model is None:

        state["response"] = (
            "Loan model is not available."
        )

        state["final_answer"] = state["response"]

        return state



    # Demo customer input
    # Same 14 features used during training

    customer = {


        "Gender": 1,

        "Married": 1,

        "Education": 0,

        "Self_Employed": 0,


        "ApplicantIncome": 50000,

        "CoapplicantIncome": 10000,


        "LoanAmount": 300,

        "Loan_Amount_Term": 360,


        "Credit_History": 1,


        "Dependents_1": 0,

        "Dependents_2": 1,

        "Dependents_3+": 0,


        "Property_Area_Semiurban": 1,

        "Property_Area_Urban": 0

    }



    df = pd.DataFrame(
        [customer]
    )


    try:


        scaled = scaler.transform(
            df
        )


        prediction = loan_model.predict(
            scaled
        )[0]



        if prediction == 1:

            result = (
                "Loan Approved"
            )

        else:

            result = (
                "Loan Rejected"
            )



    except Exception as e:

        result = (
            f"Loan prediction failed: {e}"
        )



    state["response"] = result

    state["final_answer"] = result


    return state