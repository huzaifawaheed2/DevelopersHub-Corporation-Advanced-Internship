import streamlit as st


def page_config():
    """
    Configure Streamlit page settings.
    """

    st.set_page_config(
        page_title="Global Superstore | Analytics Dashboard",
        page_icon="📈",
        layout="wide",
        initial_sidebar_state="expanded"
    )