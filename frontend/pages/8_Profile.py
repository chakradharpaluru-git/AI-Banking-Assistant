import streamlit as st

from api.api_client import get_profile



st.set_page_config(

    page_title="Profile",

    page_icon="👤",

    layout="wide"

)



st.title(
"👤 Customer Profile"
)



st.write(
"View your banking profile details"
)



token = st.session_state.get(
    "token"
)



if not token:


    st.error(
        "🔒 Please login first"
    )


    st.stop()



data = get_profile(token)



if "detail" in data:


    st.error(
        data["detail"]
    )


else:


    st.subheader(
        "👤 Personal Information"
    )


    col1,col2 = st.columns(2)



    with col1:

        st.info(
            f"""
            Name

            {data.get('name')}
            """
        )


    with col2:

        st.info(
            f"""
            Email

            {data.get('email')}
            """
        )



    st.divider()



    st.subheader(
        "🏦 Account Information"
    )


    col1,col2=st.columns(2)



    with col1:

        st.success(

            f"""
            Account Type

            {data.get('account_type')}
            """

        )


    with col2:

        st.success(

            f"""
            Status

            {data.get('account_status')}
            """

        )



    st.divider()



    st.subheader(
        "🤖 AI Banking Insights"
    )


    col1,col2=st.columns(2)



    with col1:

        st.metric(

            "💳 Credit Score",

            data.get(
                "credit_score"
            )

        )


    with col2:

        st.metric(

            "📊 Customer Segment",

            data.get(
                "customer_segment"
            )

        )



    st.divider()



    st.subheader(
        "📜 Account Summary"
    )


    st.json(data)