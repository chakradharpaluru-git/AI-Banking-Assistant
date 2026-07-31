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
# Load Model
# ==========================================================

complaint_model = None
tfidf = None

if os.path.exists(MODEL_PATH) and os.path.exists(VECTORIZER_PATH):

    complaint_model = joblib.load(MODEL_PATH)
    tfidf = joblib.load(VECTORIZER_PATH)

    print("Complaint Classifier Loaded")

else:

    print("Complaint Model or TF-IDF Vectorizer Not Found")


# ==========================================================
# Text Cleaning
# ==========================================================

def preprocess_text(text: str):

    text = text.lower()
    text = re.sub(r"\d+", "", text)
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    text = re.sub(r"\s+", " ", text).strip()

    return text


# ==========================================================
# Support Agent
# ==========================================================

def support_agent(state: AgentState):

    query = state["query"]

    if complaint_model is not None and tfidf is not None:

        cleaned = preprocess_text(query)

        vector = tfidf.transform([cleaned])

        category = complaint_model.predict(vector)[0]

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
