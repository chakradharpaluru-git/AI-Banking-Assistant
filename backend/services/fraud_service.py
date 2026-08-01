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
    "fraud_model.pkl"
)


model = None



def load_model():

    global model

    if model is None:

        model = joblib.load(
            MODEL_PATH
        )

    return model




def predict_fraud(data: dict):

    model = load_model()


    columns = [

        "Time",

        "V1","V2","V3","V4","V5","V6",
        "V7","V8","V9",

        "V10","V11","V12","V13","V14",
        "V15","V16",

        "V17","V18","V19","V20",

        "V21","V22","V23","V24",
        "V25","V26","V27","V28",

        "Amount"
    ]


    input_df = pd.DataFrame(
        [data]
    )


    input_df = input_df[
        columns
    ]


    prediction = model.predict(
        input_df
    )[0]


    if prediction == 0:

        return "Genuine Transaction"


    return "Fraudulent Transaction"