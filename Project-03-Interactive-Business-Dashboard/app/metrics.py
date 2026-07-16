import streamlit as st

from utils import (
    format_currency,
    format_number,
    format_percentage
)

def metric_card(title, value, icon, subtext=None):
    """
    Display a custom KPI card.
    """

    subtext_html = f"<div class=\"metric-subtext\">{subtext}</div>" if subtext else ""

    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-icon">{icon}</div>
            <div class="metric-title">{title}</div>
            <div class="metric-value">{value}</div>
            {subtext_html}
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

    st.markdown("### Key Performance Indicators")
    st.caption("A quick business snapshot of the currently filtered dataset.")


    # KPI Cards - Row 1
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        metric_card("Total Sales", format_currency(total_sales), "💰", "Revenue across the filtered records")

    with col2:
        metric_card("Total Profit", format_currency(total_profit), "📈", "Net profit after costs")

    with col3:
        metric_card("Total Orders", format_number(total_orders), "🧾", "Unique orders placed")

    with col4:
        metric_card("Total Customers", format_number(total_customers), "👥", "Unique customers in view")


    # KPI Cards - Row 2
    col5, col6, col7, col8 = st.columns(4)

    with col5:
        metric_card("Profit Margin", format_percentage(profit_margin), "🎯", "Profit as a share of sales")

    with col6:
        metric_card("Avg. Order Value", format_currency(average_order_value), "🛒", "Average sales per order")

    with col7:
        metric_card("Avg. Profit / Order", format_currency(average_profit_per_order), "✨", "Average contribution per order")

    with col8:
        metric_card("Avg. Sales / Customer", format_currency(average_sales_per_customer), "📊", "Revenue generated per customer")

    st.markdown("<div class='kpi-bottom-spacer'></div>", unsafe_allow_html=True)