import os
import joblib
import pandas as pd

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.dirname(__file__)
    )
)

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

model = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)


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


segment_mapping = {

    0: "Premium Customer",

    1: "Regular Customer",

    2: "High Risk Customer",

    3: "Investment Customer"

}


def predict_segment(data):

    input_df = pd.DataFrame([data])

    input_df = input_df[feature_order]

    scaled = scaler.transform(input_df)

    cluster = model.predict(scaled)[0]

    return segment_mapping.get(cluster, "Unknown Customer")
