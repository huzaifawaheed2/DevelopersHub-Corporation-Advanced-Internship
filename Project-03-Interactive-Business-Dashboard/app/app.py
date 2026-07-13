import streamlit as st

# Import Project Files

from config import page_config
from data_loader import load_data
from filters import sidebar_filters

# Page Configuration
page_config()

# Load Dataset
df = load_data()

# Apply Sidebar Filters
filtered_df = sidebar_filters(df)

# Dashboard Title
st.title("Global Superstore Business Dashboard")

st.markdown(
    """
Welcome to the **Global Superstore Interactive Business Dashboard**.

Use the filters in the sidebar to analyze sales performance,
customer behavior, regional performance, and business insights.
"""
)

st.divider()

# Dataset Information

st.subheader("Dataset Preview")

st.dataframe(filtered_df, use_container_width=True)

