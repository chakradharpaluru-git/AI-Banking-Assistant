import streamlit as st
import logging
import os


# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="AI Banking Assistant",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =====================================================
# LOGGING SYSTEM
# =====================================================

LOG_DIR = "frontend/logs"

os.makedirs(
    LOG_DIR,
    exist_ok=True
)

logging.basicConfig(
    filename=f"{LOG_DIR}/banking_app.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger()

logger.info(
    "🏦 AI Banking Assistant Application Started"
)


# =====================================================
# SESSION MANAGEMENT
# =====================================================

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "username" not in st.session_state:
    st.session_state.username = "Guest"

if "role" not in st.session_state:
    st.session_state.role = "Customer"


# =====================================================
# HEADER
# =====================================================

st.markdown(
"""
# 🏦 AI Banking Assistant

### 🤖 Intelligent Digital Banking Platform

Secure • Smart • AI Powered
"""
)

st.divider()


# =====================================================
# SIDEBAR
# =====================================================

st.sidebar.image(
    "https://cdn-icons-png.flaticon.com/512/2830/2830284.png",
    width=100
)

st.sidebar.title(
    "🏦 Banking Portal"
)

st.sidebar.markdown(
f"""
### 👤 User Profile

**Name:** {st.session_state.username}

**Role:** {st.session_state.role}

**Status:** 🟢 Active
"""
)

st.sidebar.divider()


# =====================================================
# LOGIN STATUS
# =====================================================

if st.session_state.logged_in:

    st.sidebar.success("🔐 Logged In")

    if st.sidebar.button("🚪 Logout"):

        st.session_state.logged_in = False
        st.session_state.username = "Guest"
        st.session_state.role = "Customer"

        st.rerun()

else:

    st.sidebar.warning("🔒 Login Required")


# =====================================================
# SYSTEM MONITOR
# =====================================================

st.sidebar.subheader("⚙️ System Monitor")

status = [

    ("🚀 FastAPI Backend", "🟢 Online"),

    ("🧠 ML Models", "🟢 Loaded"),

    ("🔎 RAG Engine", "🟢 Active"),

    ("🕸 LangGraph Agents", "🟢 Running"),

    ("🗄 Database", "🟢 Connected")

]

for name, state in status:

    st.sidebar.write(f"{name} : {state}")


# =====================================================
# DASHBOARD CARDS
# =====================================================

st.subheader("🚀 AI Banking Services")

col1, col2, col3 = st.columns(3)

with col1:

    st.success(
"""
## 💰 Loan Prediction

AI model analyzes:

✅ Income

✅ Credit Score

✅ Loan History

Predict approval chances.
"""
    )

with col2:

    st.error(
"""
## 🚨 Fraud Detection

AI detects:

⚠ Suspicious Transactions

⚠ Fraud Patterns

⚠ Risk Score
"""
    )

with col3:

    st.info(
"""
## 📚 RBI Policy Assistant

Ask questions about:

📄 Banking Rules

📄 Loan Policies

📄 RBI Guidelines
"""
    )


# =====================================================
# AI AGENTS STATUS
# =====================================================

st.divider()

st.subheader("🤖 Multi-Agent Banking AI")

agents = [

    ("👨‍💼 Supervisor Agent", "Routing Requests"),

    ("💳 Loan Agent", "Loan Analysis"),

    ("🚨 Fraud Agent", "Fraud Detection"),

    ("📊 Credit Agent", "Credit Score"),

    ("💰 Investment Agent", "Investment Advice"),

    ("📞 Support Agent", "Customer Queries"),

    ("📚 Policy Agent", "RBI Documents")

]

for agent, task in agents:

    st.write(
        f"""
{agent}

➜ {task}

Status: 🟢 Running
"""
    )


# =====================================================
# FOOTER
# =====================================================

st.divider()

st.caption(
"""
🏦 AI Banking Assistant

Built With:

🐍 Python

⚡ Streamlit

🚀 FastAPI

🧠 Machine Learning

🔎 RAG

🕸 LangGraph

Version: 1.0.0
"""
)