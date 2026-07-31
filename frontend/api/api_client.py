import requests


BASE_URL = "http://127.0.0.1:8000"



# =========================
# LOGIN
# =========================


def login_user(data):


    response = requests.post(

        f"{BASE_URL}/auth/login",

        json=data

    )


    return response.json()



# =========================
# LOAN
# =========================


def loan_prediction(data):


    response=requests.post(

        f"{BASE_URL}/loan/predict",

        json=data

    )


    return response.json()



# =========================
# FRAUD
# =========================


def fraud_prediction(data):


    response=requests.post(

        f"{BASE_URL}/fraud/predict",

        json=data

    )


    return response.json()



# =========================
# AGENT QUERY
# =========================


def agent_query(data):

    response = requests.post(
        f"{BASE_URL}/agents/query",
        json=data
    )

    print("Status Code:", response.status_code)
    print("Response:", response.text)

    return response.json()



# =========================
# COMPLAINT
# =========================


def complaint_classify(data):


    response=requests.post(

        f"{BASE_URL}/complaint/classify",

        json=data

    )


    return response.json()



# =========================
# POLICY CHATBOT
# =========================


def policy_chat(data):


    response=requests.post(

        f"{BASE_URL}/chatbot/chat",

        json=data

    )


    return response.json()



# =========================
# PROFILE
# =========================


def get_profile(token):


    headers={

        "Authorization":
        f"Bearer {token}"

    }


    response=requests.get(

        f"{BASE_URL}/profile/",

        headers=headers

    )


    return response.json()