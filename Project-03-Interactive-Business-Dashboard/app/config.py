import streamlit as st


def page_config():
    """
    Configure the Streamlit Page.
    """
    
    st.set_page_config(
        page_title="Global Superstore Dashboard",
        page_icon="📊",
        layout="wide",
        initial_sidebar_state="expanded"
    )