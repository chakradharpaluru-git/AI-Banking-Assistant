import requests
import streamlit as st


# ==============================
# BACKEND URL
# ==============================

try:
    BASE_URL = st.secrets["BACKEND_URL"]

except Exception:
    BASE_URL = "https://ai-banking-assistant-39vn.onrender.com"


BASE_URL = BASE_URL.rstrip("/")



# ==============================
# COMMON API FUNCTION
# ==============================

def api_request(endpoint, payload=None):

    try:

        response = requests.post(
            BASE_URL + endpoint,
            json=payload,
            timeout=180
        )


        print("STATUS:", response.status_code)
        print("RESPONSE:", response.text)


        if response.status_code != 200:

            return {
                "error": response.text
            }


        try:

            return response.json()


        except:

            return {
                "error": "Backend did not return JSON",
                "raw": response.text
            }



    except Exception as e:

        return {
            "error": str(e)
        }



# ==============================
# LOGIN
# ==============================

def login_user(payload):

    return api_request(
        "/auth/login",
        payload
    )



# ==============================
# REGISTER
# ==============================

def register_user(payload):

    return api_request(
        "/auth/register",
        payload
    )



# ==============================
# LOAN
# ==============================

def loan_prediction(payload):

    return api_request(
        "/loan/predict",
        payload
    )



# ==============================
# FRAUD
# ==============================

def fraud_prediction(payload):

    return api_request(
        "/fraud/predict",
        payload
    )



# ==============================
# CREDIT
# ==============================

def credit_prediction(payload):

    return api_request(
        "/credit/predict",
        payload
    )



# ==============================
# SEGMENTATION
# ==============================

def customer_segmentation(payload):

    return api_request(
        "/customer/segment",
        payload
    )



# ==============================
# COMPLAINT
# ==============================

def complaint_classification(payload):

    return api_request(
        "/complaint/classify",
        payload
    )



# ==============================
# POLICY CHATBOT
# ==============================

def policy_chat(payload):

    return api_request(
        "/chatbot/chat",
        payload
    )



# ==============================
# AGENTS
# ==============================

def agent_query(payload):

    return api_request(
        "/agents/query",
        payload
    )