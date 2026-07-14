import streamlit as st

# Import Project Files

from config import page_config
from data_loader import load_data
from filters import sidebar_filters
from metrics import show_metrics
from charts import (
    sales_by_category_chart,
    profit_by_category_chart,
    sales_by_region_chart
)

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

# KPI Cards
show_metrics(filtered_df)

st.divider()

# Row 1
# Sales and Profit Charts
col1, col2 = st.columns(2)

with col1:
    sales_by_category_chart(filtered_df)

with col2:
    profit_by_category_chart(filtered_df)
    
st.divider()

# Row 2
# Sales by Region Chart

sales_by_region_chart(filtered_df)

# Dataset Information

st.subheader("Dataset Preview")

st.dataframe(filtered_df, use_container_width=True)

