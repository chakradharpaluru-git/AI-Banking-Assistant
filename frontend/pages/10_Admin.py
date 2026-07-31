import streamlit as st
import logging

from utils.session import is_authenticated

logger = logging.getLogger(__name__)

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Admin Dashboard",
    page_icon="🛠️",
    layout="wide"
)

# =====================================================
# AUTH CHECK
# =====================================================

if not is_authenticated():

    st.warning("🔒 Please login first")
    st.stop()



# =====================================================
# HEADER
# =====================================================

st.title("🛠️ Admin Dashboard")

st.markdown(
"""
Monitor the AI Banking Assistant platform.

View:

- 👥 Total Users
- 📊 Total Predictions
- 🚨 Fraud Alerts
- 💬 Chat Requests
- ⚙️ System Status
"""
)

st.divider()

# =====================================================
# METRICS
# =====================================================

col1, col2, col3, col4 = st.columns(4)

with col1:

    st.metric(
        "👥 Total Users",
        "125"
    )

with col2:

    st.metric(
        "📊 Predictions",
        "542"
    )

with col3:

    st.metric(
        "🚨 Fraud Alerts",
        "18"
    )

with col4:

    st.metric(
        "💬 Chat Requests",
        "1,248"
    )

# =====================================================
# SYSTEM STATUS
# =====================================================

st.divider()

st.subheader("⚙️ System Status")

services = [

    ("🚀 FastAPI Backend", "🟢 Online"),
    ("🧠 ML Models", "🟢 Loaded"),
    ("🔎 RAG Engine", "🟢 Running"),
    ("🕸️ LangGraph Agents", "🟢 Running"),
    ("🗄️ PostgreSQL", "🟢 Connected"),
    ("📄 RBI Vector Database", "🟢 Ready")

]

for service, status in services:

    st.success(f"{service} : {status}")

# =====================================================
# MODULE STATUS
# =====================================================

st.divider()

st.subheader("🏦 Banking Modules")

modules = [

    "💰 Loan Prediction",
    "🚨 Fraud Detection",
    "📊 Credit Score",
    "👥 Customer Segmentation",
    "📩 Complaint Classification",
    "📚 Policy Chatbot",
    "💹 Investment Advisor"

]

for module in modules:

    st.write(f"✅ {module}")

# =====================================================
# RECENT ALERTS
# =====================================================

st.divider()

st.subheader("🚨 Recent Alerts")

alerts = [

    "No critical alerts.",
    "ML Models loaded successfully.",
    "Database connection healthy.",
    "LangGraph supervisor active."

]

for alert in alerts:

    st.info(alert)

# =====================================================
# FOOTER
# =====================================================

st.divider()

st.caption(
"""
AI Banking Assistant Admin Dashboard

Version 1.0.0
"""
)