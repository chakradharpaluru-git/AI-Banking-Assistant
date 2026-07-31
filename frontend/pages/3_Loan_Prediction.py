import streamlit as st
import logging
from datetime import datetime


from api.api_client import loan_prediction
from utils.session import is_authenticated



# ==========================================
# LOGGER
# ==========================================

logger = logging.getLogger(__name__)



# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="Loan Prediction",
    page_icon="💰",
    layout="wide"
)



# ==========================================
# AUTHENTICATION CHECK
# ==========================================

if not is_authenticated():

    st.warning(
        "🔒 Please login to access Loan Prediction"
    )

    st.stop()



# ==========================================
# HEADER
# ==========================================

st.title(
    "💰 AI Loan Eligibility Prediction"
)


st.markdown(
"""
### 🤖 Machine Learning Based Loan Approval System

The AI model analyzes:

✅ Applicant Profile  
✅ Income Details  
✅ Employment Information  
✅ Credit History  
✅ Property Information  

to predict loan eligibility.

"""
)


st.divider()



# ==========================================
# APPLICANT DETAILS
# ==========================================

st.subheader(
    "👤 Applicant Information"
)


col1, col2 = st.columns(2)



with col1:


    gender = st.selectbox(
        "⚥ Gender",
        [
            "Male",
            "Female"
        ]
    )


    married = st.selectbox(
        "💍 Married Status",
        [
            "Yes",
            "No"
        ]
    )


    dependents = st.selectbox(
        "👨‍👩‍👧 Dependents",
        [
            "0",
            "1",
            "2",
            "3+"
        ]
    )


    education = st.selectbox(
        "🎓 Education",
        [
            "Graduate",
            "Not Graduate"
        ]
    )



with col2:


    employment = st.selectbox(
        "💼 Self Employed",
        [
            "Yes",
            "No"
        ]
    )


    property_area = st.selectbox(
        "🏠 Property Area",
        [
            "Urban",
            "Semiurban",
            "Rural"
        ]
    )



st.divider()



# ==========================================
# FINANCIAL DETAILS
# ==========================================


st.subheader(
    "💵 Financial Information"
)



col3, col4 = st.columns(2)



with col3:


    applicant_income = st.number_input(
        "💰 Applicant Income (₹)",
        min_value=0,
        value=50000
    )


    coapplicant_income = st.number_input(
        "👥 Co-Applicant Income (₹)",
        min_value=0,
        value=0
    )



with col4:


    loan_amount = st.number_input(
        "🏦 Loan Amount (₹)",
        min_value=0,
        value=200000
    )


    loan_term = st.number_input(
        "📅 Loan Term (Months)",
        min_value=0,
        value=360
    )



credit_history = st.selectbox(

    "📊 Credit History",

    [
        "Good",
        "Bad"
    ]

)



st.divider()



# ==========================================
# PREDICTION BUTTON
# ==========================================


if st.button(
    "🚀 Predict Loan Eligibility",
    use_container_width=True
):


    # ===============================
    # ENCODING INPUTS
    # ===============================


    payload = {


        "gender":

            1 if gender == "Male" else 0,


        "married":

            1 if married == "Yes" else 0,


        "education":

            1 if education == "Graduate" else 0,


        "self_employed":

            1 if employment == "Yes" else 0,


        "applicant_income":

            applicant_income,


        "coapplicant_income":

            coapplicant_income,


        "loan_amount":

            loan_amount,


        "loan_amount_term":

            loan_term,


        "credit_history":

            1 if credit_history == "Good" else 0,



        "dependents_1":

            1 if dependents == "1" else 0,


        "dependents_2":

            1 if dependents == "2" else 0,


        "dependents_3_plus":

            1 if dependents == "3+" else 0,



        "property_area_semiurban":

            1 if property_area == "Semiurban" else 0,


        "property_area_urban":

            1 if property_area == "Urban" else 0

    }



    logger.info(
        f"""
        Loan Prediction Request

        User:
        {st.session_state.username}

        Data:
        {payload}
        """
    )



    with st.spinner(
        "🤖 AI Model analyzing application..."
    ):


        response = loan_prediction(
            payload
        )



    logger.info(
        f"Loan Prediction Response : {response}"
    )



    # =====================================
    # DISPLAY RESULT
    # =====================================


    st.subheader(
        "📋 Prediction Result"
    )



    if "error" in response:


        st.error(
            response["error"]
        )



    else:


        prediction = response.get(
            "prediction",
            ""
        )



        confidence = response.get(
            "confidence",
            None
        )



        if prediction.lower() in [
            "approved",
            "loan approved"
        ]:


            st.success(
"""
## ✅ Loan Approved

Congratulations 🎉

Your application satisfies
the eligibility criteria.
"""
            )



        elif prediction.lower() in [
            "rejected",
            "loan rejected"
        ]:


            st.error(
"""
## ❌ Loan Rejected

Your application does not
meet current eligibility criteria.
"""
            )



        else:


            st.info(
                response
            )



        if confidence:


            st.metric(
                "🤖 Model Confidence",
                f"{confidence*100:.2f}%"
            )



    st.caption(
        f"""
        Prediction Time:
        {datetime.now()}
        """
    )