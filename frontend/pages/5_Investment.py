THIS_IS_NEW_FILE = True

import streamlit as st
import logging
from datetime import datetime

st.write("NEW INVESTMENT PAGE LOADED")

from api.api_client import agent_query
from utils.session import is_authenticated


# ==========================================
# LOGGER
# ==========================================

logger = logging.getLogger(__name__)



# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(

    page_title="Investment Advisor",

    page_icon="💰",

    layout="wide"

)



# ==========================================
# AUTH CHECK
# ==========================================

if not is_authenticated():

    st.warning(
        "🔒 Please login to access Investment Advisor"
    )

    st.stop()



# ==========================================
# HEADER
# ==========================================

st.title(
    "💰 AI Investment Advisor"
)


st.markdown(
"""
## 🤖 LangGraph Powered Investment Assistant

Get personalized investment suggestions
based on:

✅ Savings Amount  
✅ Risk Appetite  
✅ Financial Goals  

The AI agent recommends suitable options
like:

📈 Mutual Funds  
🏦 Fixed Deposits  
📜 Bonds  
💹 Stocks  

"""
)


st.divider()



# ==========================================
# USER INPUT
# ==========================================


st.subheader(
    "📝 Investment Details"
)



col1, col2 = st.columns(2)



with col1:


    savings_amount = st.number_input(

        "💵 Savings Amount (₹)",

        min_value=0,

        value=50000

    )


    risk_level = st.selectbox(

        "⚠ Risk Level",

        [

            "Low Risk",

            "Medium Risk",

            "High Risk"

        ]

    )



with col2:


    goal = st.selectbox(

        "🎯 Investment Goal",

        [

            "Wealth Growth",

            "Emergency Fund",

            "Retirement Planning",

            "Short Term Savings",

            "Tax Saving"

        ]

    )



st.divider()



# ==========================================
# CUSTOM QUERY
# ==========================================


st.subheader(
    "💬 Ask Investment Agent"
)



question = st.text_area(

    "Your Question",

    value=
    "I have savings. Where should I invest?"

)



# ==========================================
# BUTTON
# ==========================================


if st.button(

    "🚀 Get Investment Advice",

    use_container_width=True

):


    query = f"""

    I have ₹{savings_amount} savings.

    My risk level is {risk_level}.

    My investment goal is {goal}.

    {question}

    Suggest suitable investment options.

    """



    payload = {


        "message": query

    }



    logger.info(

        f"""

        Investment Query

        User:
        {st.session_state.username}

        Query:
        {query}

        """

    )



    with st.spinner(

        "🤖 Investment Agent thinking..."

    ):


        response = agent_query(

            payload

        )



    logger.info(

        f"Investment Response: {response}"

    )



    st.divider()



    st.subheader(

        "📊 AI Recommendation"

    )



    if not response:


        st.error(

            "❌ No response from AI Agent"

        )



    elif "detail" in response:


        st.error(

            response["detail"]

        )



    else:


        answer = response.get(

            "response",

            response

        )



        st.success(

            "✅ Investment Analysis Completed"

        )


        st.write(

            answer

        )



    st.caption(

        f"""

        Generated:

        {datetime.now().strftime("%d-%m-%Y %H:%M:%S")}

        """

    )



# ==========================================
# SAMPLE RECOMMENDATIONS
# ==========================================


st.divider()


st.subheader(
    "💡 Common Investment Options"
)



options = [

    (
        "📈 Mutual Funds",
        "Suitable for medium to long-term wealth creation"
    ),

    (
        "🏦 Fixed Deposit",
        "Lower risk with stable returns"
    ),

    (
        "📜 Bonds",
        "Fixed income investment option"
    ),

    (
        "💹 Stocks",
        "Higher risk with higher growth potential"
    )

]


for title, description in options:

    st.info(

        f"""
        {title}

        {description}

        """

    )