import os
import joblib
import pandas as pd

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.dirname(__file__)
    )
)

MODEL_PATH = os.path.join(BASE_DIR, "models", "credit_score_model.pkl")
SCALER_PATH = os.path.join(BASE_DIR, "models", "credit_scaler.pkl")
FEATURE_PATH = os.path.join(BASE_DIR, "models", "credit_feature_names.pkl")
ENCODER_PATH = os.path.join(BASE_DIR, "models", "credit_target_encoder.pkl")

model = None
scaler = None
feature_names = None
encoder = None

try:
    model = joblib.load(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)
    feature_names = joblib.load(FEATURE_PATH)
    encoder = joblib.load(ENCODER_PATH)
    print("✅ Credit Score Model Loaded")

except FileNotFoundError:
    print("⚠️ credit_score_model.pkl not found. Credit Score API disabled.")

except Exception as e:
    print(f"⚠️ Error loading Credit Score Model: {e}")


def predict_credit(data):

    if model is None:
        raise Exception(
            "Credit Score model is not available on this server."
        )

    input_df = pd.DataFrame([data])

    for col in feature_names:
        if col not in input_df.columns:
            input_df[col] = 0

    input_df = input_df[feature_names]

    input_scaled = scaler.transform(input_df)

    prediction = model.predict(input_scaled)

    label = encoder.inverse_transform(prediction)[0]

    return label