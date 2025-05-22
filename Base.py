import streamlit as st
import Home
import About
import Model

st.set_page_config(page_title="Water Potability Checker", layout="wide")

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Model", "About"])

# Page router
if page == "Home":
    Home.app()
elif page == "Model":
    Model.app()
elif page == "About":
    About.app()
