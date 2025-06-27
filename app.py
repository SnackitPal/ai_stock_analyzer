import streamlit as st
from src.modules.broker_handler import initialize_api_connector

st.title('AI Stock Analyzer')

connector = initialize_api_connector()

if connector:
    st.button("Connect to Angel One")
else:
    st.error("Angel One API Key not found. Please check your .env file.")
