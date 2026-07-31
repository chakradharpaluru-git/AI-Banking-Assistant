import streamlit as st
import logging
from datetime import datetime


from api.api_client import fraud_prediction
from utils.session import is_authenticated



# ==========================================
# LOGGER
# ==========================================

logger = logging.getLogger(__name__)



# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="Fraud Detection",
    page_icon="🚨",
    layout="wide"
)



# ==========================================
# AUTHENTICATION
# ==========================================

if not is_authenticated():

    st.warning(
        "🔒 Please login to access Fraud Detection"
    )

    st.stop()



# ==========================================
# HEADER
# ==========================================

st.title(
    "🚨 AI Fraud Detection System"
)


st.markdown(
"""
## 🧠 Intelligent Transaction Monitoring

Our AI model analyzes banking transactions
and detects suspicious activities.

### Detection Features:

✅ Transaction Amount Analysis  
✅ Fraud Pattern Detection  
✅ Risk Score Calculation  
✅ Machine Learning Classification  

"""
)


st.divider()



# ==========================================
# TRANSACTION INPUT
# ==========================================

st.subheader(
    "💳 Transaction Information"
)



col1, col2 = st.columns(2)



with col1:


    amount = st.number_input(

        "💰 Transaction Amount (₹)",

        min_value=0.0,

        value=25000.0

    )



with col2:


    transaction_time = st.number_input(

        "⏰ Transaction Time",

        min_value=0,

        value=0

    )



transaction_details = st.text_area(

    "📝 Transaction Details",

    placeholder=
    "Example: Online shopping payment"

)



st.divider()



# ==========================================
# FRAUD CHECK BUTTON
# ==========================================


if st.button(

    "🔍 Check Transaction",

    use_container_width=True

):


    # ======================================
    # CREATE MODEL INPUT
    # ======================================


    payload = {


        "Time": transaction_time,


        "V1": 0,
        "V2": 0,
        "V3": 0,
        "V4": 0,
        "V5": 0,
        "V6": 0,
        "V7": 0,
        "V8": 0,
        "V9": 0,
        "V10": 0,
        "V11": 0,
        "V12": 0,
        "V13": 0,
        "V14": 0,
        "V15": 0,
        "V16": 0,
        "V17": 0,
        "V18": 0,
        "V19": 0,
        "V20": 0,
        "V21": 0,
        "V22": 0,
        "V23": 0,
        "V24": 0,
        "V25": 0,
        "V26": 0,
        "V27": 0,
        "V28": 0,


        "Amount": amount

    }



    logger.info(
        f"""
        Fraud Detection Request

        User:
        {st.session_state.username}

        Amount:
        {amount}

        Details:
        {transaction_details}

        Payload:
        {payload}
        """
    )



    # ======================================
    # API CALL
    # ======================================


    with st.spinner(

        "🤖 AI analyzing transaction..."

    ):


        response = fraud_prediction(

            payload

        )



    logger.info(

        f"Fraud API Response: {response}"

    )



    # ======================================
    # RESULT
    # ======================================


    st.subheader(
        "📊 Fraud Analysis Result"
    )



    if not response:


        st.error(
            "❌ No response from server"
        )


    elif "detail" in response:


        st.error(
            response["detail"]
        )


    else:


        prediction = response.get(

            "prediction",

            ""

        )



        risk_score = response.get(

            "risk_score",

            None

        )



        prediction_text = str(
            prediction
        ).lower()



        if (
            "fraud" in prediction_text
            or
            "suspicious" in prediction_text
        ):


            st.error(
"""
# 🚨 Fraud Detected

This transaction looks suspicious.

Recommended Actions:

⚠ Verify transaction  
⚠ Contact bank support  
⚠ Check account activity
"""
            )



        elif (

            "genuine" in prediction_text

            or

            "normal" in prediction_text

            or

            "safe" in prediction_text

        ):


            st.success(
"""
# ✅ Genuine Transaction

Transaction appears safe.

No suspicious activity detected.
"""
            )


        else:


            st.info(
                f"Prediction: {prediction}"
            )



        if risk_score is not None:


            st.metric(

                "⚠ Risk Score",

                risk_score

            )



    st.caption(

        f"""
        Analysis Completed:

        {datetime.now().strftime("%d-%m-%Y %H:%M:%S")}
        """

    )