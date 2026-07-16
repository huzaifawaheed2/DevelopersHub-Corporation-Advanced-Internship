import streamlit as st

# Import Project Files

from config import page_config
from data_loader import load_data
from filters import sidebar_filters
from metrics import show_metrics
from utils import format_number
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

# CSS Styling Import
from pathlib import Path

def load_css():
    css_file = Path(__file__).parent / "assets" / "style.css"

    with open(css_file, encoding="utf-8") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )


# Page Configuration
page_config()

# Load Custom CSS
load_css()

# Load Data
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




def render_section(title, subtitle):
    st.markdown(f"<div class='section-title'>{title}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='section-subtitle'>{subtitle}</div>", unsafe_allow_html=True)


# Dashboard Title
st.markdown(
    f"""
    <div class="hero-card">
        <div class="hero-badge">Data Science & Analytics Project</div>
        <h1>Global Superstore Business Dashboard</h1>
        <p>
            A polished, interactive view of sales performance, profitability, customer behavior,
            product performance, and regional trends for presentation-ready analysis.
        </p>
        <div class="hero-stats">
            <div class="hero-chip">{format_number(len(filtered_df))} records in view</div>
            <div class="hero-chip">{format_number(filtered_df["Order ID"].nunique())} unique orders</div>
            <div class="hero-chip">{format_number(filtered_df["Customer ID"].nunique())} unique customers</div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
Use the sidebar filters to focus the analysis, then review the KPI cards and charts below for a presentation-ready business summary.
"""
)

# Key Performance Indicators (KPIs)
with st.container():
    show_metrics(filtered_df)


# Category Performance Analysis
# Compare total sales and profit across product categories.

render_section("Category Performance", "Compare how sales and profit are distributed across product categories.")

col1, col2 = st.columns(2)

with col1:
    sales_by_category_chart(filtered_df)

with col2:
    profit_by_category_chart(filtered_df)


# Market Performance Analysis
# Compare sales across regions and customer segments.

render_section("Market Performance", "See where revenue is coming from across regions and customer segments.")

col1, col2 = st.columns(2)

with col1:
    sales_by_region_chart(filtered_df)

with col2:
    sales_by_segment_chart(filtered_df)



# Sales Trend Analysis
# Analyze monthly sales performance over time.

render_section("Sales Trend", "Track monthly sales movement across the available years.")

monthly_sales_trend_chart(filtered_df)


# Product & Customer Performance Analysis
# Analyze top-performing products and customers by sales.

render_section("Customer and Product Leaders", "Highlight the top-performing products and customers by sales.")

col1, col2 = st.columns([1.2,1])

with col1:
    top_products_chart(filtered_df)

with col2:
    top_customers_chart(filtered_df)
    


# Sales & Profit Relationship Analysis
# Analyze the relationship between sales, profit, and top-performing sub-categories.

render_section("Profitability Mix", "Understand the link between sales, profit, and the most profitable sub-categories.")

col1, col2 = st.columns(2)

with col1:
    profit_vs_sales_chart(filtered_df)

with col2:
    top_profitable_subcategories_chart(filtered_df)
    


# Logistics & Market Analysis
# Analyze sales by shipping mode and market.

render_section("Logistics and Market Mix", "Review how shipping mode and market composition affect total sales.")

col1, col2 = st.columns(2)

with col1:
    sales_by_ship_mode_chart(filtered_df)

with col2:
    sales_by_market_chart(filtered_df)
    
    

# Global Sales Analysis
# Display sales distribution across countries.

render_section("Global Reach", "Visualize how sales are distributed across countries worldwide.")

global_sales_map_chart(filtered_df)




# Product Performance Analysis
# Display top-selling product sub-categories.

render_section("Product Depth", "Inspect the top sub-categories driving revenue and profit.")

top_subcategories_chart(filtered_df)



# Dataset Preview
# View and download the filtered dataset.

render_section("Filtered Dataset", "Download or inspect the records currently matching your filters.")

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



# About Dashboard
with st.container(border=True):
    st.markdown("<div class='about-kicker'>About this dashboard</div>", unsafe_allow_html=True)

    st.markdown(
        "<div class='about-title'>Built for business storytelling and executive analysis</div>",
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <p class='about-text'>
            This Streamlit dashboard turns the Global Superstore dataset into a clean executive
            view of sales, profit, customers, products, and geography. It is designed for clear
            presentation, quick decision-making, and portfolio-ready storytelling.
        </p>
        """,
        unsafe_allow_html=True,
    )

    developer_col, project_col = st.columns(2)


    # Developer

    with developer_col:
        with st.container(border=True):

            st.markdown(
                "<div class='about-section-title'>Developer</div>",
                unsafe_allow_html=True,
            )

            st.markdown("**Muhammad Huzaifa Waheed**")

            st.caption(
                "Data Analyst | Data Science & Analytics | Power BI | "
                "Business Analytics | Data Visualization | Python | SQL | Excel"
            )

            st.markdown(
                """
                <div class='about-block'>
                    <div class='about-section-title'>Tools Used</div>
                    <div class='about-chip-row'>
                        <span class='about-chip'>Python</span>
                        <span class='about-chip'>Pandas</span>
                        <span class='about-chip'>Streamlit</span>
                        <span class='about-chip'>Plotly</span>
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

            st.markdown(
                "<div class='about-block'><div class='about-section-title'>Connect</div></div>",
                unsafe_allow_html=True,
            )

            github_col, linkedin_col, email_col = st.columns(3)

            with github_col:
                st.link_button(
                    "GitHub",
                    "https://github.com/huzaifawaheed2",
                    use_container_width=True,
                )

            with linkedin_col:
                st.link_button(
                    "LinkedIn",
                    "https://www.linkedin.com/in/muhammad-huzaifa-waheed-70043338b",
                    use_container_width=True,
                )

            with email_col:
                st.link_button(
                    "Email",
                    "mailto:huzaifawaheed1258@gmail.com",
                    use_container_width=True,
                )


    # Project Snapshot

    with project_col:
        with st.container(border=True):

            st.markdown(
                "<div class='about-section-title'>Project Snapshot</div>",
                unsafe_allow_html=True,
            )

            st.markdown("**Global Superstore Business Dashboard**")

            st.caption("Global Superstore Dataset")

            st.markdown(
                """
                Interactive filters, KPI cards, trend charts, category and market
                breakdowns, a world sales map, and an exportable filtered dataset.
                """
            )

            st.markdown(
                """
                - Sales and profit performance
                - Customer and product concentration
                - Regional and segment distribution
                - Logistics, market mix, and country-level sales
                """
            )