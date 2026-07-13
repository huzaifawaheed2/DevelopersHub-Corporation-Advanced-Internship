import streamlit as st

def sidebar_filters(df):
    """
    Create sidebar filters and return filtered dataframe.
    """
    
    st.sidebar.header("Dashboard Filters")
    
    st.sidebar.divider()
    
    # Date Range Filter
    start_date = df["Order Date"].min()
    end_date = df["Order Date"].max()
    
    date_range = st.sidebar.date_input(
        "Order Date Range",
        value=(start_date, end_date),
        min_value=start_date,
        max_value=end_date
    )
    
    st.sidebar.divider()
    
    # Year Filter
    year = st.sidebar.multiselect(
        "Select Year",
        options=sorted(df["Order Year"].unique()),
        default=sorted(df["Order Year"].unique())
    )
    
    # Market Filter
    market = st.sidebar.multiselect(
        "Select Market",
        options=sorted(df["Market"].unique()),
        default=sorted(df["Market"].unique())
    )
    
    # Region Filter
    region = st.sidebar.multiselect(
        "Select Region",
        options=sorted(df["Region"].unique()),
        default=sorted(df["Region"].unique())
    )
    
    # Category Filter
    category = st.sidebar.multiselect(
        "Select Category",
        options=sorted(df["Category"].unique()),
        default=sorted(df["Category"].unique())
    )
    
    # Segment Filter
    segment = st.sidebar.multiselect(
        "Select Segment",
        options=sorted(df["Segment"].unique()),
        default=sorted(df["Segment"].unique())
    )
    
    # Apply Date Filter
    filtered_df = df.copy()
    
    if len(date_range) == 2:
        
        start =date_range[0]
        end = date_range[1]
        filtered_df = filtered_df[
            (filtered_df["Order Date"].dt.date >= start) &
            (filtered_df["Order Date"].dt.date <= end)
        ]
    
    # Apply Other Filters
    filtered_df = df[
        (df["Order Year"].isin(year)) &
        (df["Market"].isin(market)) &
        (df["Region"].isin(region)) &
        (df["Category"].isin(category)) &
        (df["Segment"].isin(segment))
    ]
    
    # Sidebar Information
    st.sidebar.divider()
    
    st.sidebar.metric("Records Found", len(filtered_df))
    
    
    return filtered_df