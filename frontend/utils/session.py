import streamlit as st
import logging


logger = logging.getLogger(__name__)


# =====================================
# INITIALIZE SESSION
# =====================================

def initialize_session():

    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False


    if "username" not in st.session_state:
        st.session_state.username = None


    if "email" not in st.session_state:
        st.session_state.email = None


    if "role" not in st.session_state:
        st.session_state.role = None


    if "token" not in st.session_state:
        st.session_state.token = None



# =====================================
# LOGIN USER
# =====================================

def login_user(
        username,
        email,
        token,
        role="customer"
):

    st.session_state.logged_in = True

    st.session_state.username = username

    st.session_state.email = email

    st.session_state.token = token

    st.session_state.role = role


    logger.info(
        f"User Login Success : {username}"
    )



# =====================================
# LOGOUT USER
# =====================================

def logout_user():

    logger.info(
        f"User Logout : {st.session_state.username}"
    )


    st.session_state.logged_in = False

    st.session_state.username = None

    st.session_state.email = None

    st.session_state.token = None

    st.session_state.role = None



# =====================================
# CHECK AUTHENTICATION
# =====================================

def is_authenticated():

    return st.session_state.get(
        "logged_in",
        False
    )