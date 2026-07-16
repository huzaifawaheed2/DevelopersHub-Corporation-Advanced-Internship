import streamlit as st
import plotly.express as px
import pandas as pd


# Common Chart Layout
def apply_chart_layout(
    fig,
    title,
    x_title,
    y_title,
    height=420
):
    """
    Apply a consistent layout to all charts.
    """

    fig.update_layout(
        title=title,
        title_x=0.5,
        xaxis_title=x_title,
        yaxis_title=y_title,
        template="plotly_white",
        height=height
    )


# Display Plotly Chart
def display_chart(fig):
    """
    Display Plotly chart with consistent settings.
    """

    st.plotly_chart(
        fig,
        use_container_width=True,
        config={
            "displaylogo": False,
            "modeBarButtonsToRemove": [
                "lasso2d",
                "select2d",
                "autoScale2d"
            ],
            "responsive": True
        }
    )
    

def sales_by_category_chart(df):
    """
    Display Sales by Category Chart.
    """

    # Prepare Data
    category_sales = (
        df.groupby("Category", as_index=False)["Sales"]
        .sum()
        .sort_values(by="Sales", ascending=False)
    )

    # Create Figure
    fig = px.bar(
        category_sales,
        x="Category",
        y="Sales",
        text_auto=".2s"
    )

    # Apply Layout
    apply_chart_layout(
        fig,
        title="Sales by Category",
        x_title="Category",
        y_title="Sales (USD)"
    )

    # Hover Template
    fig.update_traces(
        hovertemplate="<b>%{x}</b><br>Sales: $%{y:,.2f}<extra></extra>"
    )

    # Display Chart
    display_chart(fig)


def profit_by_category_chart(df):
    """
    Display Profit by Category Chart.
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
        text_auto=".2s"
    )

    # Apply Layout
    apply_chart_layout(
        fig,
        title="Profit by Category",
        x_title="Category",
        y_title="Profit (USD)"
    )

    # Hover Template
    fig.update_traces(
        hovertemplate="<b>%{x}</b><br>Profit: $%{y:,.2f}<extra></extra>"
    )

    # Display Chart
    display_chart(fig)
    
    
def sales_by_region_chart(df):
    """
    Display Sales by Region Chart.
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
        text_auto=".2s"
    )

    # Apply Layout
    apply_chart_layout(
        fig,
        title="Sales by Region",
        x_title="Region",
        y_title="Sales (USD)"
    )

    # Hover Template
    fig.update_traces(
        hovertemplate="<b>%{x}</b><br>Sales: $%{y:,.2f}<extra></extra>"
    )

    # Display Chart
    display_chart(fig)


def sales_by_segment_chart(df):
    """
    Display Sales by Segment Chart.
    """

    # Prepare Data
    segment_sales = (
        df.groupby("Segment", as_index=False)["Sales"]
        .sum()
        .sort_values("Sales", ascending=False)
    )

    # Create Figure
    fig = px.bar(
        segment_sales,
        x="Segment",
        y="Sales",
        text_auto=".2s"
    )

    # Apply Layout
    apply_chart_layout(
        fig,
        title="Sales by Segment",
        x_title="Segment",
        y_title="Sales (USD)"
    )

    # Hover Template
    fig.update_traces(
        hovertemplate="<b>%{x}</b><br>Sales: $%{y:,.2f}<extra></extra>"
    )

    # Display Chart
    display_chart(fig)


def monthly_sales_trend_chart(df):
    """
    Display Monthly Sales Trend across different years.
    """

    # Prepare Data
    monthly_sales = (
        df.groupby(
            ["Order Year", "Order Month", "Order Month Name"],
            as_index=False
        )["Sales"]
        .sum()
        .sort_values(["Order Year", "Order Month"])
    )

    # Create Figure
    fig = px.line(
        monthly_sales,
        x="Order Month Name",
        y="Sales",
        color="Order Year",
        markers=True
    )

    # Apply Layout
    apply_chart_layout(
        fig,
        title="Monthly Sales Trend",
        x_title="Month",
        y_title="Sales (USD)"
    )

    fig.update_layout(
        hovermode="x unified",
        legend_title="Year"
    )

    # Hover Template
    fig.update_traces(
        hovertemplate="<b>%{x}</b><br>Sales: $%{y:,.2f}<extra>%{fullData.name}</extra>"
    )

    # Display Chart
    display_chart(fig)
    

def top_products_chart(df):
    """
    Display Top 10 Products by Sales.
    """

    # Prepare Data
    top_products = (
        df.groupby("Product Name", as_index=False)["Sales"]
        .sum()
        .sort_values("Sales", ascending=False)
        .head(10)
    )

    # Create Figure
    fig = px.bar(
        top_products,
        x="Sales",
        y="Product Name",
        text_auto=".2s"
    )

    # Apply Layout
    apply_chart_layout(
        fig,
        title="Top 10 Products by Sales",
        x_title="Sales (USD)",
        y_title="Product"
    )

    fig.update_yaxes(autorange="reversed")

    # Hover Template
    fig.update_traces(
        hovertemplate="<b>%{y}</b><br>Sales: $%{x:,.2f}<extra></extra>"
    )

    # Display Chart
    display_chart(fig)
    

def top_customers_chart(df):
    """
    Display Top 10 Customers by Sales.
    """

    # Prepare Data
    top_customers = (
        df.groupby("Customer Name", as_index=False)["Sales"]
        .sum()
        .sort_values("Sales", ascending=False)
        .head(10)
    )

    # Create Figure
    fig = px.bar(
        top_customers,
        x="Sales",
        y="Customer Name",
        text_auto=".2s"
    )

    # Apply Layout
    apply_chart_layout(
        fig,
        title="Top 10 Customers by Sales",
        x_title="Sales (USD)",
        y_title="Customer"
    )

    fig.update_yaxes(autorange="reversed")

    # Hover Template
    fig.update_traces(
        hovertemplate="<b>%{y}</b><br>Sales: $%{x:,.2f}<extra></extra>"
    )

    # Display Chart
    display_chart(fig)
    

def profit_vs_sales_chart(df):
    """
    Display Profit vs Sales Scatter Plot.
    """

    # Create Figure
    fig = px.scatter(
        df,
        x="Sales",
        y="Profit",
        color="Profit Status",
        opacity=0.75,
        color_discrete_map={
            "Profit": "green",
            "Loss": "red",
            "Break-even": "gold"
        },
        hover_data={
            "Category": True,
            "Profit Status": True,
            "Sales": ":,.2f",
            "Profit": ":,.2f"
        }
    )

    # Apply Layout
    apply_chart_layout(
        fig,
        title="Profit vs Sales",
        x_title="Sales (USD)",
        y_title="Profit (USD)"
    )

    fig.update_layout(
        legend_title="Profit Status",
        hovermode="closest"
    )

    # Hover Template
    fig.update_traces(
        hovertemplate=
        "<b>%{customdata[0]}</b><br>"
        "Sales: $%{x:,.2f}<br>"
        "Profit: $%{y:,.2f}<br>"
        "Status: %{customdata[1]}"
        "<extra></extra>"
    )

    # Display Chart
    display_chart(fig)


def sales_by_ship_mode_chart(df):
    """
    Display Sales by Ship Mode.
    """

    # Prepare Data
    ship_mode_sales = (
        df.groupby("Ship Mode", as_index=False)["Sales"]
        .sum()
        .sort_values("Sales", ascending=False)
    )

    # Create Figure
    fig = px.bar(
        ship_mode_sales,
        x="Ship Mode",
        y="Sales",
        text_auto=".2s"
    )

    # Apply Layout
    apply_chart_layout(
        fig,
        title="Sales by Ship Mode",
        x_title="Ship Mode",
        y_title="Sales (USD)"
    )

    # Hover Template
    fig.update_traces(
        hovertemplate="<b>%{x}</b><br>Sales: $%{y:,.2f}<extra></extra>"
    )

    # Display Chart
    display_chart(fig)
    

def sales_by_market_chart(df):
    """
    Display Sales by Market.
    """

    # Prepare Data
    market_sales = (
        df.groupby("Market", as_index=False)["Sales"]
        .sum()
        .sort_values("Sales", ascending=False)
    )

    # Create Figure
    fig = px.bar(
        market_sales,
        x="Market",
        y="Sales",
        text_auto=".2s"
    )

    # Apply Layout
    apply_chart_layout(
        fig,
        title="Sales by Market",
        x_title="Market",
        y_title="Sales (USD)"
    )

    # Hover Template
    fig.update_traces(
        hovertemplate="<b>%{x}</b><br>Sales: $%{y:,.2f}<extra></extra>"
    )

    # Display Chart
    display_chart(fig)
    


def global_sales_map_chart(df):
    """
    Display Global Sales by Country.
    """

    # Prepare Data
    country_sales = (
        df.groupby("Country", as_index=False)["Sales"]
        .sum()
    )

    # Create Figure
    fig = px.choropleth(
        country_sales,
        locations="Country",
        locationmode="country names",
        color="Sales",
        hover_name="Country",
        color_continuous_scale="Blues",
        projection="natural earth"
    )

    # Apply Layout
    apply_chart_layout(
        fig,
        title="Global Sales by Country",
        x_title="",
        y_title="",
        height=500
    )

    fig.update_layout(
        margin=dict(
            l=0,
            r=0,
            t=60,
            b=0
        ),
        coloraxis_colorbar_title="Sales"
    )

    # Hover Template
    fig.update_traces(
        hovertemplate="<b>%{location}</b><br>Sales: $%{z:,.2f}<extra></extra>"
    )

    # Display Chart
    display_chart(fig)
    

def top_subcategories_chart(df):
    """
    Display Top 10 Sub-Categories by Sales.
    """

    # Prepare Data
    top_subcategories = (
        df.groupby("Sub-Category", as_index=False)["Sales"]
        .sum()
        .sort_values("Sales", ascending=False)
        .head(10)
    )

    # Create Figure
    fig = px.bar(
        top_subcategories,
        x="Sales",
        y="Sub-Category",
        text_auto=".2s"
    )

    # Apply Layout
    apply_chart_layout(
        fig,
        title="Top 10 Sub-Categories by Sales",
        x_title="Sales (USD)",
        y_title="Sub-Category"
    )

    # Highest Sales at the Top
    fig.update_yaxes(
        autorange="reversed"
    )

    # Hover Template
    fig.update_traces(
        hovertemplate="<b>%{y}</b><br>Sales: $%{x:,.2f}<extra></extra>"
    )

    # Display Chart
    display_chart(fig)
    


def top_profitable_subcategories_chart(df):
    """
    Display Top 10 Most Profitable Sub-Categories.
    """

    # Prepare Data
    top_profit_subcategories = (
        df.groupby("Sub-Category", as_index=False)["Profit"]
        .sum()
        .sort_values("Profit", ascending=False)
        .head(10)
    )

    # Create Figure
    fig = px.bar(
        top_profit_subcategories,
        x="Profit",
        y="Sub-Category",
        text_auto=".2s"
    )

    # Apply Layout
    apply_chart_layout(
        fig,
        title="Top 10 Most Profitable Sub-Categories",
        x_title="Profit (USD)",
        y_title="Sub-Category"
    )

    # Highest Profit at the Top
    fig.update_yaxes(
        autorange="reversed"
    )

    # Green color for profit
    fig.update_traces(
        hovertemplate="<b>%{y}</b><br>Profit: $%{x:,.2f}<extra></extra>"
    )

    # Display Chart
    display_chart(fig)