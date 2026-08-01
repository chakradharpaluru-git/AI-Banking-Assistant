import os
import re
import joblib

from backend.agents.state import AgentState


# ==========================================================
# Paths
# ==========================================================

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.dirname(__file__)
    )
)


MODEL_PATH = os.path.join(
    BASE_DIR,
    "models",
    "complaint_classifier.pkl"
)


VECTORIZER_PATH = os.path.join(
    BASE_DIR,
    "models",
    "tfidf_vectorizer.pkl"
)



# ==========================================================
# Lazy Loaded Model
# ==========================================================

complaint_model = None
tfidf = None



def load_complaint_resources():

    global complaint_model
    global tfidf


    if complaint_model is None:


        if os.path.exists(MODEL_PATH) and os.path.exists(VECTORIZER_PATH):

            complaint_model = joblib.load(
                MODEL_PATH
            )


            tfidf = joblib.load(
                VECTORIZER_PATH
            )


            print(
                "✅ Complaint Classifier Loaded"
            )


        else:

            print(
                "⚠️ Complaint Model Files Not Found"
            )


    return complaint_model, tfidf



# ==========================================================
# Text Cleaning
# ==========================================================

def preprocess_text(text: str):

    text = text.lower()

    text = re.sub(
        r"\d+",
        "",
        text
    )

    text = re.sub(
        r"[^a-zA-Z\s]",
        "",
        text
    )

    text = re.sub(
        r"\s+",
        " ",
        text
    ).strip()


    return text



# ==========================================================
# Support Agent
# ==========================================================

def support_agent(state: AgentState):


    complaint_model, tfidf = load_complaint_resources()


    query = state["query"]



    if complaint_model is not None and tfidf is not None:


        cleaned = preprocess_text(
            query
        )


        vector = tfidf.transform(
            [cleaned]
        )


        category = complaint_model.predict(
            vector
        )[0]



        response = f"""
Complaint Category : {category}

Department : {category} Support Team

Our support team will assist you shortly.
"""


    else:


        response = """
Complaint classification model is unavailable.

Please contact customer support.
"""



    state["response"] = response


    return state