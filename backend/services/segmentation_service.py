import os
import joblib
import pandas as pd


# ==========================================================
# Project Base Directory
# ==========================================================

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.dirname(__file__)
    )
)


# ==========================================================
# Model Paths
# ==========================================================

MODEL_PATH = os.path.join(
    BASE_DIR,
    "models",
    "customer_segmentation_model.pkl"
)


SCALER_PATH = os.path.join(
    BASE_DIR,
    "models",
    "customer_scaler.pkl"
)


# ==========================================================
# Lazy Loaded Resources
# ==========================================================

model = None
scaler = None



def load_segmentation_resources():

    global model
    global scaler


    if model is None:

        model = joblib.load(
            MODEL_PATH
        )


        scaler = joblib.load(
            SCALER_PATH
        )


        print(
            "✅ Customer Segmentation Model Loaded"
        )


    return model, scaler



# ==========================================================
# Feature Order
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
# Segment Labels
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

def predict_segment(data: dict):


    model, scaler = load_segmentation_resources()



    input_df = pd.DataFrame(
        [data]
    )


    # Arrange columns exactly as training

    input_df = input_df[
        feature_order
    ]



    # Scale input

    scaled = scaler.transform(
        input_df
    )



    # Predict cluster

    cluster = model.predict(
        scaled
    )[0]



    return segment_mapping.get(
        cluster,
        "Unknown Customer"
    )