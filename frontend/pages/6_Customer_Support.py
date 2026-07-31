import streamlit as st
import logging
from datetime import datetime


from api.api_client import complaint_classify
from utils.session import is_authenticated



# =====================================
# LOGGER
# =====================================

logger = logging.getLogger(__name__)




# =====================================
# PAGE CONFIG
# =====================================

st.set_page_config(

    page_title="Customer Support",

    page_icon="📞",

    layout="wide"

)




# =====================================
# AUTHENTICATION CHECK
# =====================================

if not is_authenticated():

    st.warning(
        "🔒 Please login to access Customer Support"
    )

    st.stop()




# =====================================
# HEADER
# =====================================

st.title(
    "📞 AI Customer Support Assistant"
)


st.markdown(
"""
## 🤖 NLP Based Complaint Resolution System

The AI system automatically analyzes customer
complaints and routes them to the correct support team.

### Workflow:

📝 Complaint Text

⬇️

🧠 NLP Classification Model

⬇️

🏷 Complaint Category

⬇️

👨‍💼 Support Department

"""
)


st.divider()




# =====================================
# COMPLAINT INPUT
# =====================================

st.subheader(
    "📝 Enter Your Complaint"
)



complaint = st.text_area(

    "Complaint Message",

    placeholder="""

Example:

My credit card payment failed while making an online transaction.

""",

    height=180

)



st.divider()




# =====================================
# ANALYZE BUTTON
# =====================================

if st.button(

    "🚀 Analyze Complaint",

    use_container_width=True

):


    if not complaint.strip():

        st.warning(
            "⚠ Please enter a complaint message"
        )

        st.stop()



    # =================================
    # IMPORTANT FIX
    # Backend expects "text"
    # =================================

    payload = {

        "text": complaint

    }



    logger.info(
        f"""
        Complaint Request

        User:
        {st.session_state.get("username")}

        Text:
        {complaint}

        """
    )



    with st.spinner(

        "🧠 NLP Model analyzing complaint..."

    ):


        response = complaint_classify(

            payload

        )



    logger.info(

        f"Complaint API Response: {response}"

    )



    st.divider()


    st.subheader(
        "📊 Complaint Analysis Result"
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
    # RESPONSE HANDLING
    # Supports multiple formats
    # =================================


    category = response.get(

        "category",

        response.get(

            "prediction",

            "Unknown"

        )

    )



    department = response.get(

        "department",

        response.get(

            "response",

            "Customer Support"

        )

    )



    confidence = response.get(

        "confidence",

        None

    )




    # =================================
    # DISPLAY RESULT
    # =================================


    col1, col2 = st.columns(2)



    with col1:


        st.success(

            f"""
🏷 Complaint Category

{category}

"""

        )



    with col2:


        st.info(

            f"""
🏢 Assigned Department

{department}

"""

        )




    if confidence is not None:


        st.metric(

            "🤖 AI Confidence",

            f"{float(confidence)*100:.2f}%"

        )




    st.divider()



    # =================================
    # SUPPORT AGENT MESSAGE
    # =================================


    st.subheader(

        "👨‍💼 Support Agent Recommendation"

    )



    category_text = str(

        category

    ).lower()



    if "card" in category_text:


        st.write(
"""
💳 **Card Support Team**

Your complaint has been assigned to the
Card Support department.

They handle:

✅ Credit card issues  
✅ Failed payments  
✅ Card transactions  
✅ Unauthorized charges
"""
        )



    elif "loan" in category_text:


        st.write(
"""
🏦 **Loan Support Team**

They handle:

✅ Loan applications  
✅ Loan approval issues  
✅ EMI problems  
✅ Loan account queries
"""
        )



    elif "kyc" in category_text:


        st.write(
"""
🪪 **KYC Support Team**

They handle:

✅ KYC verification  
✅ Document issues  
✅ Account verification
"""
        )



    else:


        st.write(
"""
📞 **General Banking Support**

Your complaint has been forwarded
to the customer support team.
"""
        )



    st.caption(

        f"""
⏰ Analysis Completed:

{datetime.now().strftime("%d-%m-%Y %H:%M:%S")}

"""

    )