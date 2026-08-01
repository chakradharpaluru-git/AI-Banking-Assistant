import requests


# =====================================================
# BACKEND URL
# =====================================================

BASE_URL = "https://ai-banking-assistant-39vn.onrender.com"



# =====================================================
# COMMON REQUEST HANDLER
# =====================================================

def post_request(endpoint, payload):

    try:

        response = requests.post(

            f"{BASE_URL}{endpoint}",

            json=payload,

            timeout=120

        )


        print("API:", endpoint)

        print("STATUS:", response.status_code)

        print("BODY:", response.text)



        if response.status_code == 200:

            return response.json()


        return {

            "error": response.text,

            "status_code": response.status_code

        }


    except requests.exceptions.Timeout:

        return {

            "error":
            "Backend timeout. Render service may be waking up."

        }


    except requests.exceptions.ConnectionError:

        return {

            "error":
            "Cannot connect to backend."

        }


    except Exception as e:

        return {

            "error": str(e)

        }



# =====================================================
# AUTH
# =====================================================


def login_user(payload):

    return post_request(

        "/auth/login",

        payload

    )



def register_user(payload):

    return post_request(

        "/auth/register",

        payload

    )



# =====================================================
# LOAN
# =====================================================


def loan_predict(payload):

    return post_request(

        "/loan/predict",

        payload

    )



# =====================================================
# FRAUD
# =====================================================


def fraud_predict(payload):

    return post_request(

        "/fraud/predict",

        payload

    )



# =====================================================
# CREDIT SCORE
# =====================================================


def credit_predict(payload):

    return post_request(

        "/credit/predict",

        payload

    )



# =====================================================
# CUSTOMER SEGMENTATION
# =====================================================


def customer_segment(payload):

    return post_request(

        "/customer/segment",

        payload

    )



# =====================================================
# COMPLAINT CLASSIFICATION
# =====================================================


def complaint_classify(payload):

    return post_request(

        "/complaint/classify",

        payload

    )



# =====================================================
# POLICY RAG CHATBOT
# =====================================================


def policy_chat(payload):

    return post_request(

        "/chatbot/chat",

        payload

    )



# =====================================================
# LANGGRAPH MULTI AGENT
# =====================================================


def agent_query(payload):

    return post_request(

        "/agents/query",

        payload

    )



# =====================================================
# PROFILE
# =====================================================


def get_profile(token):

    try:

        response = requests.get(

            f"{BASE_URL}/profile/",

            headers={

                "Authorization":
                f"Bearer {token}"

            },

            timeout=60

        )


        if response.status_code == 200:

            return response.json()


        return {

            "error": response.text

        }


    except Exception as e:

        return {

            "error": str(e)

        }