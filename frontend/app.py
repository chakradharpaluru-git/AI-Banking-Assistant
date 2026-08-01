import streamlit as st
import requests
import logging
import os


# =====================================================
# CONFIG
# =====================================================

st.set_page_config(
    page_title="AI Banking Assistant",
    page_icon="🏦",
    layout="wide"
)


BACKEND_URL = "https://ai-banking-assistant-39vn.onrender.com"


# =====================================================
# LOGGING
# =====================================================

LOG_DIR = "frontend/logs"

os.makedirs(
    LOG_DIR,
    exist_ok=True
)


logging.basicConfig(
    filename=f"{LOG_DIR}/banking_app.log",
    level=logging.INFO
)


logger = logging.getLogger()


# =====================================================
# SESSION
# =====================================================

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False


if "token" not in st.session_state:
    st.session_state.token = None


if "username" not in st.session_state:
    st.session_state.username = "Guest"



# =====================================================
# HEADER
# =====================================================

st.title("🏦 AI Banking Assistant")

st.write(
"""
### Intelligent Digital Banking Platform

Machine Learning + RAG + LangGraph Agents
"""
)


st.divider()



# =====================================================
# SIDEBAR
# =====================================================


st.sidebar.title(
    "🏦 Banking Portal"
)


page = st.sidebar.radio(

    "Navigate",

    [

        "Dashboard",

        "Register",

        "Login",

        "Loan Prediction",

        "Fraud Detection",

        "Credit Score",

        "Customer Segmentation",

        "Complaint Classification",

        "RBI Policy Chatbot",

        "AI Agent Assistant"

    ]

)



st.sidebar.divider()


st.sidebar.write(
f"""
👤 User:

{st.session_state.username}


Status:

{"🟢 Logged In" if st.session_state.logged_in else "🔴 Guest"}
"""
)



# =====================================================
# API FUNCTION
# =====================================================


def call_api(endpoint, payload):

    try:

        response = requests.post(

            f"{BACKEND_URL}{endpoint}",

            json=payload,

            timeout=60

        )


        return response.json()


    except Exception as e:

        return {

            "error":str(e)

        }



# =====================================================
# DASHBOARD
# =====================================================


if page=="Dashboard":


    st.subheader(
        "🚀 AI Banking Services"
    )


    c1,c2,c3 = st.columns(3)


    with c1:

        st.success(
        """
        ## 💰 Loan Prediction

        Predict loan approval using ML
        """
        )


    with c2:

        st.error(
        """
        ## 🚨 Fraud Detection

        Detect suspicious transactions
        """
        )


    with c3:

        st.info(
        """
        ## 📚 RBI Policy Chatbot

        Ask RBI banking questions
        """
        )



# =====================================================
# REGISTER
# =====================================================


elif page=="Register":


    st.subheader(
        "Create Account"
    )


    username = st.text_input(
        "Username"
    )


    email = st.text_input(
        "Email"
    )


    password = st.text_input(
        "Password",
        type="password"
    )


    if st.button("Register"):


        result = call_api(

            "/auth/register",

            {

            "username":username,

            "email":email,

            "password":password

            }

        )


        st.json(result)



# =====================================================
# LOGIN
# =====================================================


elif page=="Login":


    st.subheader(
        "Login"
    )


    username = st.text_input(
        "Username"
    )


    password = st.text_input(
        "Password",
        type="password"
    )


    if st.button("Login"):


        result = call_api(

            "/auth/login",

            {

            "username":username,

            "password":password

            }

        )


        if "access_token" in result:


            st.session_state.logged_in=True

            st.session_state.token=result["access_token"]

            st.session_state.username=username


            st.success(
                "Login Successful"
            )


        else:

            st.error(result)



# =====================================================
# LOAN
# =====================================================


elif page=="Loan Prediction":


    st.subheader(
        "💰 Loan Eligibility"
    )


    payload={

        "gender":"Male",

        "married":"Yes",

        "education":"Graduate",

        "self_employed":"No",

        "applicant_income":50000,

        "coapplicant_income":10000,

        "loan_amount":200000,

        "loan_amount_term":360,

        "credit_history":1,

        "dependents_1":0,

        "dependents_2":0,

        "dependents_3_plus":0,

        "property_area_semiurban":1,

        "property_area_urban":0

    }



    if st.button("Predict Loan"):


        result=call_api(

            "/loan/predict",

            payload

        )


        st.success(result)



# =====================================================
# FRAUD
# =====================================================


elif page=="Fraud Detection":


    st.subheader(
        "🚨 Fraud Detection"
    )


    payload={

        "Time":100,

        "V1":0,

        "V2":0,

        "V3":0,

        "V4":0,

        "V5":0,

        "V6":0,

        "V7":0,

        "V8":0,

        "V9":0,

        "V10":0,

        "V11":0,

        "V12":0,

        "V13":0,

        "V14":0,

        "V15":0,

        "V16":0,

        "V17":0,

        "V18":0,

        "V19":0,

        "V20":0,

        "V21":0,

        "V22":0,

        "V23":0,

        "V24":0,

        "V25":0,

        "V26":0,

        "V27":0,

        "V28":0,

        "Amount":2500

    }



    if st.button("Check Transaction"):


        result=call_api(

            "/fraud/predict",

            payload

        )


        st.write(result)



# =====================================================
# CREDIT
# =====================================================


elif page=="Credit Score":


    st.subheader(
        "📊 Credit Score Prediction"
    )


    st.info(
        "Uses trained credit score ML model"
    )



# =====================================================
# SEGMENTATION
# =====================================================


elif page=="Customer Segmentation":


    st.subheader(
        "👥 Customer Segment"
    )


    result=call_api(

        "/customer/segment",

        {

        "Monthly_Inhand_Salary":50000,

        "Num_Bank_Accounts":2,

        "Num_Credit_Card":2,

        "Interest_Rate":8,

        "Delay_from_due_date":0,

        "Num_Credit_Inquiries":1,

        "Credit_Utilization_Ratio":20,

        "Total_EMI_per_month":5000

        }

    )


    st.json(result)



# =====================================================
# COMPLAINT
# =====================================================


elif page=="Complaint Classification":


    text=st.text_area(
        "Enter complaint"
    )


    if st.button("Classify"):


        result=call_api(

            "/complaint/classify",

            {

            "text":text

            }

        )


        st.json(result)



# =====================================================
# RAG CHATBOT
# =====================================================


elif page=="RBI Policy Chatbot":


    question=st.text_input(
        "Ask RBI Question"
    )


    if st.button("Ask"):


        result=call_api(

            "/chatbot/chat",

            {

            "question":question

            }

        )


        st.write(
            result.get(
                "response"
            )
        )



# =====================================================
# LANGGRAPH AGENT
# =====================================================


elif page=="AI Agent Assistant":


    message=st.text_input(
        "Ask Banking AI Agent"
    )


    if st.button("Send"):


        result=call_api(

            "/agents/query",

            {

            "message":message

            }

        )


        st.success(

            result.get(
                "agent"
            )

        )


        st.write(

            result.get(
                "response"
            )

        )



# =====================================================
# FOOTER
# =====================================================


st.divider()


st.caption(
"""
AI Banking Assistant v1.0

Built with:

Python | FastAPI | Streamlit | ML | RAG | LangGraph
"""
)