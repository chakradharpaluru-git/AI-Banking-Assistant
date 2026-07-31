import streamlit as st
import logging
from datetime import datetime


from utils.session import (
    is_authenticated
)


# =====================================
# LOGGER
# =====================================

logger = logging.getLogger(__name__)


# =====================================
# PAGE CONFIG
# =====================================

st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
    layout="wide"
)



# =====================================
# AUTH CHECK
# =====================================

if not is_authenticated():

    st.warning(
        "🔒 Please login to access dashboard"
    )

    st.stop()



# =====================================
# USER DETAILS
# =====================================


username = st.session_state.username

role = st.session_state.role



logger.info(
    f"Dashboard opened by {username}"
)



# =====================================
# HEADER
# =====================================


st.title(
    "📊 AI Banking Dashboard"
)


st.markdown(
f"""
## 👋 Welcome {username}

Role: **{role}**

Your personalized AI banking overview.
"""
)


st.divider()



# =====================================
# USER FINANCIAL SUMMARY
# =====================================


st.subheader(
    "💳 Financial Profile"
)



col1, col2, col3 = st.columns(3)



with col1:

    st.metric(
        label="💯 Credit Score",
        value="780",
        delta="Good"
    )



with col2:

    st.metric(
        label="👥 Customer Segment",
        value="Premium"
    )



with col3:

    st.metric(
        label="🏦 Account Status",
        value="Active",
        delta="Verified"
    )



# =====================================
# CREDIT ANALYSIS CARD
# =====================================


st.divider()


st.subheader(
    "📈 Credit Analysis"
)


st.success(
"""
✅ Credit Score: Good

Reasons:

✔ Regular repayments

✔ Stable income

✔ Low credit risk

✔ Healthy banking history

"""
)



# =====================================
# CUSTOMER SEGMENT
# =====================================


st.subheader(
    "👥 Customer Segmentation"
)


segment_data = {

    "Segment": "Premium",

    "Risk Level": "Low",

    "Recommended Services":
    "Investment + Credit Cards"

}


for key,value in segment_data.items():

    st.write(
        f"**{key}:** {value}"
    )



# =====================================
# RECENT ACTIVITY
# =====================================


st.divider()


st.subheader(
    "📜 Recent Activity"
)



activities = [

    {
        "icon":"💰",
        "action":"Loan Prediction",
        "status":"Completed"
    },


    {
        "icon":"🚨",
        "action":"Fraud Checks",
        "status":"Completed"
    },


    {
        "icon":"💬",
        "action":"AI Banking Chats",
        "status":"Completed"
    },


]



for activity in activities:

    st.info(
        f"""
        {activity['icon']} 
        {activity['action']}

        Status: 🟢 {activity['status']}

        Time: {datetime.now().strftime("%d-%m-%Y %H:%M")}
        """
    )



# =====================================
# AI AGENTS STATUS
# =====================================


st.divider()


st.subheader(
    "🤖 AI Banking Agents"
)


agents = [

    "👨‍💼 Supervisor Agent",

    "💳 Loan Agent",

    "🚨 Fraud Agent",

    "📊 Credit Agent",

    "💰 Investment Agent",

    "📚 Policy RAG Agent"

]


for agent in agents:

    st.write(
        f"{agent} : 🟢 Running"
    )



# =====================================
# FOOTER
# =====================================


st.divider()


st.caption(
"""
🏦 AI Banking Assistant

Powered by:

🐍 Python  
⚡ FastAPI  
🧠 Machine Learning  
🔎 RAG  
🕸 LangGraph Multi-Agent AI
"""
)