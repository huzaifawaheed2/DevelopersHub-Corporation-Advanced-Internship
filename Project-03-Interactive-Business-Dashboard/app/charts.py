import streamlit as st
import plotly.express as px
import pandas as pd

def sales_by_category_chart(df):
    """
    Display Sales by Category Chart.
    """
    
    # Calculate Sales by Category.
    category_sales = (
        df.groupby("Category", as_index=False)["Sales"]
        .sum()
        .sort_values(by="Sales", ascending=False)
    )
    
    # Create Chart
    fig = px.bar(
        category_sales,
        x="Category",
        y="Sales",
        title="Sales by Category",
        text_auto=".2s",
    )
    
    # Update Layout
    fig.update_layout(
        xaxis_title="Category",
        yaxis_title="Sales (USD)",
        title_x=0.5,
        template="plotly_white"
    )
    
    # Show Chart
    st.plotly_chart(fig, use_container_width=True)
    
    
def profit_by_category_chart(df):
    """
    Display Profit by Category chart.
    """

    # Prepare Data
    category_profit = (
        df.groupby("Category", as_index=False)["Profit"]
        .sum()
        .sort_values("Profit", ascending=False)
    )

    # Create Figure
    fig = px.bar(
        category_profit,
        x="Category",
        y="Profit",
        title="Profit by Category",
        text_auto=".2s"
    )

    # Update Layout
    fig.update_layout(
        xaxis_title="Category",
        yaxis_title="Profit (USD)",
        title_x=0.5,
        template="plotly_white"
    )

    # Display Chart
    st.plotly_chart(
        fig,
        use_container_width=True
    )
    
def sales_by_region_chart(df):
    """
    Display Sales by Region chart.
    """

    # Prepare Data
    region_sales = (
        df.groupby("Region", as_index=False)["Sales"]
        .sum()
        .sort_values("Sales", ascending=False)
    )

    # Create Figure
    fig = px.bar(
        region_sales,
        x="Region",
        y="Sales",
        title="Sales by Region",
        text_auto=".2s"
    )

    # Update Layout
    fig.update_layout(
        xaxis_title="Region",
        yaxis_title="Sales (USD)",
        title_x=0.5,
        template="plotly_white"
    )

    # Display Chart
    st.plotly_chart(
        fig,
        use_container_width=True
    )
    
