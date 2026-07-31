import streamlit as st
import logging


from api.api_client import login_user
from utils.session import (
    login_user as create_session,
    is_authenticated
)


# ======================================
# LOGGER
# ======================================

logger = logging.getLogger(__name__)


# ======================================
# PAGE CONFIG
# ======================================

st.set_page_config(
    page_title="Login - AI Banking Assistant",
    page_icon="🔐",
    layout="centered"
)



# ======================================
# CHECK LOGIN STATUS
# ======================================

if is_authenticated():

    st.success(
        "✅ You are already logged in"
    )

    st.info(
        f"""
        User: {st.session_state.username}

        Role: {st.session_state.role}
        """
    )

    st.stop()



# ======================================
# LOGIN UI
# ======================================


st.image(
    "https://cdn-icons-png.flaticon.com/512/2919/2919592.png",
    width=120
)


st.title(
    "🔐 AI Banking Login"
)


st.write(
"""
Welcome back!

Login to access:

💰 Loan Prediction

🚨 Fraud Detection

📊 Credit Analysis

🤖 AI Banking Agents

📚 RBI Policy Assistant

"""
)



st.divider()



email = st.text_input(
    "📧 Email"
)



password = st.text_input(
    "🔑 Password",
    type="password"
)



# ======================================
# LOGIN BUTTON
# ======================================


if st.button(
    "🚀 Login",
    use_container_width=True
):


    if not email or not password:

        st.warning(
            "Please enter email and password"
        )


    else:


        payload = {

            "email": email,

            "password": password

        }


        logger.info(
            f"Login attempt : {email}"
        )


        response = login_user(
            payload
        )


        # ===============================
        # SUCCESS RESPONSE
        # ===============================


        if "access_token" in response:


            token = response[
                "access_token"
            ]


            username = response.get(
                "username",
                email.split("@")[0]
            )


            role = response.get(
                "role",
                "customer"
            )



            create_session(

                username,

                email,

                token,

                role

            )


            logger.info(
                f"Login successful : {email}"
            )


            st.success(
                "🎉 Login Successful"
            )


            st.balloons()


            st.switch_page(
                "pages/2_Dashboard.py"
            )



        else:


            logger.error(
                f"Login failed : {email}"
            )


            st.error(
                response.get(
                    "detail",
                    "Invalid credentials"
                )
            )