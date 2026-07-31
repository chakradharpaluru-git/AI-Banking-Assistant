import os
from pathlib import Path

import joblib
import pandas as pd

from backend.agents.state import AgentState


# ======================================
# Base Directory
# ======================================

BASE_DIR = Path(__file__).resolve().parents[2]

MODEL_PATH = BASE_DIR / "models" / "fraud_model.pkl"


# ======================================
# Load Fraud Model
# ======================================

if MODEL_PATH.exists():
    fraud_model = joblib.load(MODEL_PATH)
    print("Fraud Model Loaded Successfully")
else:
    fraud_model = None
    print(f"Fraud Model Not Found: {MODEL_PATH}")


# ======================================
# Fraud Agent
# ======================================

def fraud_agent(state: AgentState) -> AgentState:

    if fraud_model is None:
        state["response"] = "Fraud model is not available."
        state["final_answer"] = state["response"]
        return state

    # Dummy input (replace later with frontend values)
    customer = {
        "Amount": 25000,
        "OldBalance": 50000,
        "NewBalance": 25000
    }

    df = pd.DataFrame([customer])

    try:
        prediction = fraud_model.predict(df)[0]

        if prediction == 1:
            result = "Fraud Transaction Detected"
        else:
            result = "Transaction is Genuine"

    except Exception as e:
        result = f"Prediction Error: {e}"

    state["response"] = result
    state["final_answer"] = result

    return state
