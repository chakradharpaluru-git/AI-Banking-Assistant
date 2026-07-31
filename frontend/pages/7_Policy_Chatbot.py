import streamlit as st
import logging
from datetime import datetime


from api.api_client import policy_chat
from utils.session import is_authenticated



# =====================================
# LOGGER
# =====================================

logger = logging.getLogger(__name__)




# =====================================
# PAGE CONFIG
# =====================================

st.set_page_config(

    page_title="RBI Policy Chatbot",

    page_icon="📚",

    layout="wide"

)




# =====================================
# AUTH CHECK
# =====================================

if not is_authenticated():

    st.warning(
        "🔒 Please login to access Policy Chatbot"
    )

    st.stop()




# =====================================
# HEADER
# =====================================

st.title(
    "📚 RBI Policy Chatbot"
)


st.markdown(
"""
## 🤖 AI Banking Policy Assistant


Ask questions about:


📄 RBI Guidelines

🏦 Banking Rules

💳 Loan Policies

🪪 KYC Requirements

🔐 Digital Banking Rules


Technology:

🧠 LangGraph Agent

🔎 RAG Pipeline

📚 ChromaDB

📄 RBI Documents

"""
)


st.divider()




# =====================================
# USER QUESTION
# =====================================

st.subheader(
    "💬 Ask Your Question"
)



question = st.text_area(

    "Banking Policy Question",

    placeholder="""

Example:

What documents are required for KYC verification?

""",

    height=150

)



st.divider()




# =====================================
# SAMPLE QUESTIONS
# =====================================

st.subheader(
    "💡 Sample Questions"
)



sample_questions = [

    "What documents are required for KYC verification?",

    "What happens if KYC is not updated?",

    "What are RBI guidelines for failed UPI transactions?",

    "What documents are required for a home loan?",

    "How can I update my bank account details?"

]



for q in sample_questions:

    st.info(q)




st.divider()




# =====================================
# ASK BUTTON
# =====================================

if st.button(

    "🚀 Ask RBI Assistant",

    use_container_width=True

):


    if not question.strip():

        st.warning(

            "⚠ Please enter your question"

        )

        st.stop()



    # =================================
    # IMPORTANT FIX
    # Backend expects "question"
    # =================================

    payload = {


        "question": question

    }



    logger.info(

        f"""
        POLICY CHAT REQUEST

        User:
        {st.session_state.get("username")}


        Question:

        {question}

        """

    )



    with st.spinner(

        "📚 Searching RBI documents..."

    ):


        response = policy_chat(

            payload

        )



    logger.info(

        f"""

        POLICY CHAT RESPONSE:

        {response}

        """

    )



    st.divider()



    st.subheader(

        "🤖 AI Generated Answer"

    )




    # =================================
    # ERROR HANDLING
    # =================================


    if not response:


        st.error(

            "❌ No response from backend"

        )

        st.stop()



    if "error" in response:


        st.error(

            response["error"]

        )

        st.stop()



    if "detail" in response:


        st.error(

            response["detail"]

        )

        st.stop()




    # =================================
    # RESPONSE EXTRACTION
    # =================================


    answer = response.get(

        "response",

        response.get(

            "answer",

            response.get(

                "message",

                str(response)

            )

        )

    )



    agent = response.get(

        "agent",

        "Policy RAG Agent"

    )




    # =================================
    # DISPLAY
    # =================================


    st.success(

        "✅ Answer retrieved from RBI Knowledge Base"

    )



    st.write(

        answer

    )



    st.divider()



    col1, col2 = st.columns(2)



    with col1:


        st.metric(

            "🤖 Agent",

            agent

        )



    with col2:


        st.metric(

            "📚 Source",

            "RBI Documents"

        )



    st.caption(

        f"""

        ⏰ Generated Time:

        {datetime.now().strftime("%d-%m-%Y %H:%M:%S")}

        """

    )