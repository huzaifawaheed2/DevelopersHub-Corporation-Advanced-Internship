import streamlit as st

# Import Project Files

from config import page_config
from data_loader import load_data
from filters import sidebar_filters
from metrics import show_metrics
from charts import (
    sales_by_category_chart,
    profit_by_category_chart,
    sales_by_region_chart,
    sales_by_segment_chart,
    monthly_sales_trend_chart,
    top_products_chart,
    top_customers_chart,
    profit_vs_sales_chart,
    sales_by_ship_mode_chart,
    sales_by_market_chart,
    global_sales_map_chart,
    top_subcategories_chart,
    top_profitable_subcategories_chart
)

# Page Configuration
page_config()


# Load Dataset
df = load_data()

# Apply Sidebar Filters
filtered_df = sidebar_filters(df)


# No Data Handling
if filtered_df.empty:

    st.warning(
        "No data available for the selected filters.\n\n"
        "Please modify or reset the filters and try again."
    )

    st.stop()

# Dashboard Title
st.title("Global Superstore Business Dashboard")

st.markdown(
    """
Welcome to the **Global Superstore Interactive Business Dashboard**.

Use the filters in the sidebar to analyze sales performance,
customer behavior, regional performance, and business insights.
"""
)

# Key Performance Indicators (KPIs)

st.divider()

show_metrics(filtered_df)


# Category Performance Analysis
# Compare total sales and profit across product categories.

st.divider()

col1, col2 = st.columns(2)

with col1:
    sales_by_category_chart(filtered_df)

with col2:
    profit_by_category_chart(filtered_df)


# Market Performance Analysis
# Compare sales across regions and customer segments.

st.divider()

col1, col2 = st.columns(2)

with col1:
    sales_by_region_chart(filtered_df)

with col2:
    sales_by_segment_chart(filtered_df)



# Sales Trend Analysis
# Analyze monthly sales performance over time.

st.divider()

monthly_sales_trend_chart(filtered_df)


# Product & Customer Performance Analysis
# Analyze top-performing products and customers by sales.

st.divider()

col1, col2 = st.columns([1.2,1])

with col1:
    top_products_chart(filtered_df)

with col2:
    top_customers_chart(filtered_df)
    


# Sales & Profit Relationship Analysis
# Analyze the relationship between sales, profit, and top-performing sub-categories.

st.divider()

col1, col2 = st.columns(2)

with col1:
    profit_vs_sales_chart(filtered_df)

with col2:
    top_profitable_subcategories_chart(filtered_df)
    


# Logistics & Market Analysis
# Analyze sales by shipping mode and market.

st.divider()

col1, col2 = st.columns(2)

with col1:
    sales_by_ship_mode_chart(filtered_df)

with col2:
    sales_by_market_chart(filtered_df)
    
    

# Global Sales Analysis
# Display sales distribution across countries.

st.divider()

global_sales_map_chart(filtered_df)




# Product Performance Analysis
# Display top-selling product sub-categories.

st.divider()

top_subcategories_chart(filtered_df)



# Dataset Preview
# View and download the filtered dataset.
st.divider()

with st.expander("View Filtered Dataset"):

    # Download Filtered Data
    csv = filtered_df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="Download Filtered Data",
        data=csv,
        file_name="filtered_superstore_data.csv",
        mime="text/csv",
        use_container_width=True
    )

    st.dataframe(
        filtered_df,
        use_container_width=True,
        hide_index=True
    )


# -------------------------------------------------------------------
# About Dashboard
# -------------------------------------------------------------------

st.divider()

with st.container(border=True):

    st.subheader("About Dashboard")

    col1, col2 = st.columns([1, 2])

    # ---------------------------------------------------------------
    # Developer Information
    # ---------------------------------------------------------------
    with col1:

        st.markdown("### Developer")

        st.markdown("**Muhammad Huzaifa Waheed**")

        st.markdown("**Role:** Data Analyst")

        st.markdown("### Built With")

        st.markdown("""
- Python
- Pandas
- Streamlit
- Plotly
""")

        st.markdown("### Connect With Me")

        github_col, linkedin_col, email_col = st.columns(3)

        with github_col:
            st.link_button(
                "GitHub",
                "https://github.com/huzaifawaheed2",
                use_container_width=True
            )

        with linkedin_col:
            st.link_button(
                "LinkedIn",
                "https://www.linkedin.com/in/muhammad-huzaifa-waheed-70043338b",
                use_container_width=True
            )

        with email_col:
            st.link_button(
                "Email",
                "mailto:huzaifawaheed1258@gmail.com",
                use_container_width=True
            )

    # ---------------------------------------------------------------
    # Project Information
    # ---------------------------------------------------------------
    with col2:

        st.markdown("### Project Information")

        st.markdown("""
**Project Name**

Global Superstore Business Dashboard

**Project Overview**

This interactive Business Intelligence dashboard provides insights into sales performance, profitability, customer behavior, product performance, and regional trends using the Global Superstore dataset.

### Key Features

- Interactive Dashboard Filters
- KPI Summary Cards
- Business Summary
- Sales & Profit Analysis
- Customer & Product Analysis
- Regional & Market Analysis
- Global Sales Map
- Download Filtered Dataset

### Dataset

Global Superstore Dataset
""")