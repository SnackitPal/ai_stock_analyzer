import streamlit as st
from src.modules.broker_handler import initialize_api_connector, login_and_generate_session

st.title('AI Stock Analyzer')

connector = initialize_api_connector()

if connector:
    if st.button("Connect to Angel One"):
        user_profile = login_and_generate_session(connector)
        if user_profile:
            st.success("Login Successful!")
            st.write(user_profile)
        else:
            st.error("Login Failed. Please check your credentials or TOTP.")
else:
    st.error("Angel One API Key not found. Please check your .env file.")
