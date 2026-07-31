import os
from pathlib import Path

import joblib
import pandas as pd

from backend.agents.state import AgentState


# ======================================
# Base Directory
# ======================================

BASE_DIR = Path(__file__).resolve().parents[2]

# Change this path if your model is elsewhere
MODEL_PATH = BASE_DIR / "models" / "loan_model.pkl"

# ======================================
# Load Loan Model
# ======================================

if MODEL_PATH.exists():
    loan_model = joblib.load(MODEL_PATH)
    print("Loan Model Loaded Successfully")
else:
    loan_model = None
    print(f"Loan Model Not Found: {MODEL_PATH}")


# ======================================
# Loan Agent
# ======================================

def loan_agent(state: AgentState) -> AgentState:
    """
    Loan Eligibility Agent
    """

    if loan_model is None:
        state["response"] = "Loan model is not available."
        state["final_answer"] = state["response"]
        return state

    # Demo input
    customer_data = pd.DataFrame([
        {
            "Income": 50000,
            "LoanAmount": 500000,
            "CreditHistory": 1
        }
    ])

    try:
        prediction = loan_model.predict(customer_data)[0]

        if prediction in [1, "Y", "Approved"]:
            result = "Loan Approved"
        else:
            result = "Loan Rejected"

    except Exception as e:
        result = f"Loan prediction failed: {str(e)}"

    state["response"] = result
    state["final_answer"] = result

    return state
