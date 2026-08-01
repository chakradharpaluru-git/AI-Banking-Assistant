from pathlib import Path

import joblib
import pandas as pd

from backend.agents.state import AgentState


# ======================================
# Paths
# ======================================

BASE_DIR = Path(__file__).resolve().parents[2]

MODEL_PATH = (
    BASE_DIR /
    "models" /
    "fraud_model.pkl"
)


# ======================================
# Load Model
# ======================================

if MODEL_PATH.exists():

    fraud_model = joblib.load(
        MODEL_PATH
    )

    print("Fraud Agent Model Loaded")

else:

    fraud_model = None

    print(
        "Fraud Model Not Found"
    )



# ======================================
# Fraud Agent
# ======================================

def fraud_agent(
    state: AgentState
) -> AgentState:


    if fraud_model is None:

        state["response"] = (
            "Fraud model unavailable"
        )

        state["final_answer"] = (
            state["response"]
        )

        return state



    # Same 30 features used during training

    transaction = {


        "Time":10000,


        "V1":-1.2,
        "V2":0.5,
        "V3":1.1,
        "V4":0.2,
        "V5":-0.3,
        "V6":0.4,
        "V7":0.8,
        "V8":-0.1,
        "V9":0.2,


        "V10":-0.4,
        "V11":0.6,
        "V12":-0.5,
        "V13":0.3,
        "V14":-0.7,
        "V15":0.1,
        "V16":0.2,


        "V17":-0.2,
        "V18":0.4,
        "V19":0.1,
        "V20":0.05,


        "V21":0.2,
        "V22":0.1,
        "V23":-0.1,
        "V24":0.05,
        "V25":0.2,
        "V26":0.1,
        "V27":-0.05,
        "V28":0.02,


        "Amount":25000

    }



    df = pd.DataFrame(
        [transaction]
    )


    try:

        prediction = fraud_model.predict(
            df
        )[0]


        if prediction == 1:

            result = """
🚨 Fraud Transaction Detected

Action:
- Block transaction
- Verify customer identity
- Contact fraud department
"""


        else:

            result = """
✅ Transaction is Genuine

No suspicious activity detected.
"""


    except Exception as e:


        result = (
            f"Prediction Error: {e}"
        )



    state["response"] = result

    state["final_answer"] = result


    return state