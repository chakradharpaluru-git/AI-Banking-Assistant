import streamlit as st
import requests

# Replace this with your actual Render backend URL
API_URL = "https://ai-banking-assistant-39vn.onrender.com"

st.title("🏦 AI Banking Assistant")
st.subheader("Create a New Account")

name = st.text_input("Full Name")
email = st.text_input("Email")
password = st.text_input("Password", type="password")
confirm_password = st.text_input("Confirm Password", type="password")

if st.button("Register"):

    if not name or not email or not password:
        st.error("Please fill all fields.")

    elif password != confirm_password:
        st.error("Passwords do not match.")

    else:
        try:
            response = requests.post(
                f"{API_URL}/auth/register",
                json={
                    "name": name,
                    "email": email,
                    "password": password
                },
                timeout=30
            )

            if response.status_code == 200:
                st.success("✅ Registration successful! Please login.")

            else:
                st.error(response.text)

        except Exception as e:
            st.error(f"Connection Error: {e}")