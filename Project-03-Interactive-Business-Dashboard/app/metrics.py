import streamlit as st

from utils import format_currency
from utils import format_number

def show_metrics(df):
    """
    Display Dashboard KPI Cards
    """
    
    total_sales = df["Sales"].sum()
    total_profit = df["Profit"].sum()
    total_orders = df["Order ID"].nunique()
    total_customers = df["Customer ID"].nunique()
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            label="Total Sales",
            value=format_currency(total_sales)
        )
        
    with col2:
        st.metric(
            label="Total Profit",
            value=format_currency(total_profit)
        )
        
    with col3:
        st.metric(
            label="Total Orders",
            value=format_number(total_orders)
        )
    
    with col4:
        st.metric(
            label="Total Customers",
            value=format_number(total_customers)
        )
    
    