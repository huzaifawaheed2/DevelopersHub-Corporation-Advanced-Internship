import streamlit as st

from utils import (
    format_currency,
    format_number,
    format_percentage
)

def metric_card(title, value, icon):
    """
    Display a custom KPI card.
    """

    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-icon">{icon}</div>
            <div class="metric-title">{title}</div>
            <div class="metric-value">{value}</div>
        </div>
        """,
        unsafe_allow_html=True
    )


def show_metrics(df):
    """
    Display Dashboard KPI Cards.
    """

    # Calculate KPI Metrics
    total_sales = df["Sales"].sum()
    total_profit = df["Profit"].sum()
    total_orders = df["Order ID"].nunique()
    total_customers = df["Customer ID"].nunique()

    profit_margin = (
        (total_profit / total_sales) * 100
        if total_sales != 0
        else 0
    )

    average_order_value = (
        total_sales / total_orders
        if total_orders != 0
        else 0
    )

    average_profit_per_order = (
        total_profit / total_orders
        if total_orders != 0
        else 0
    )

    average_sales_per_customer = (
        total_sales / total_customers
        if total_customers != 0
        else 0
    )


    # KPI Cards - Row 1
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


    # KPI Cards - Row 2
    col5, col6, col7, col8 = st.columns(4)

    with col5:
        st.metric(
            label="Profit Margin",
            value=format_percentage(profit_margin)
        )

    with col6:
        st.metric(
            label="Avg. Order Value",
            value=format_currency(average_order_value)
        )

    with col7:
        st.metric(
            label="Avg. Profit / Order",
            value=format_currency(average_profit_per_order)
        )

    with col8:
        st.metric(
            label="Avg. Sales / Customer",
            value=format_currency(average_sales_per_customer)
        )