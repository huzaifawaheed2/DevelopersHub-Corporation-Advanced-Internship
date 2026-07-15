import pandas as pd
import streamlit as st

from utils import (
    format_currency,
    format_percentage,
    format_number
)


def business_summary(df):
    """
    Display business summary table.
    """

    # Calculate Summary Metrics
    total_sales = df["Sales"].sum()
    total_profit = df["Profit"].sum()
    profit_margin = (
        (total_profit / total_sales) * 100 
        if total_sales != 0 
        else 0
    )
    
    total_orders = df["Order ID"].nunique()
    total_customers = df["Customer ID"].nunique()
    average_order_value = (
        (total_sales / total_orders) 
        if total_orders != 0
        else 0
    )
    average_profit_per_order = (
        (total_profit / total_orders)
        if total_orders != 0 
        else 0
    )
    
    
    # Create Summary DataFrame
    summary_df = pd.DataFrame(
        {
            "Business Metric": [
                "Total Sales",
                "Total Profit",
                "Profit Margin",
                "Total Orders",
                "Total Customers",
                "Average Order Value",
                "Average Profit per Order"
            ],

            "Value": [
                total_sales,
                total_profit,
                profit_margin,
                total_orders,
                total_customers,
                average_order_value,
                average_profit_per_order
            ]
        }
    )
    
    # Format Summary Values
    summary_df["Value"] = [
        format_currency(total_sales),
        format_currency(total_profit),
        format_percentage(profit_margin),
        format_number(total_orders),
        format_number(total_customers),
        format_currency(average_order_value),
        format_currency(average_profit_per_order)
    ]
    
    # Business Summary Heading
    st.subheader("Business Summary")

    # Display Summary Table
    st.dataframe(
        summary_df,
        use_container_width=True,
        hide_index=True
    )
        
        