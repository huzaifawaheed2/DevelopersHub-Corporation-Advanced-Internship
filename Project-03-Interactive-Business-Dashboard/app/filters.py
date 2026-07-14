import streamlit as st

def sidebar_filters(df):
    """
    Create sidebar filters and return filtered dataframe.
    """
    
    # Sidebar Title
    st.sidebar.header("Dashboard Filters")
    
    st.sidebar.divider()
    
    # Start & End Date Filters

    min_date = df["Order Date"].min().date()
    max_date = df["Order Date"].max().date()

    start_date = st.sidebar.date_input(
        "Start Date",
        value=min_date,
        min_value=min_date,
        max_value=max_date
    )

    end_date = st.sidebar.date_input(
        "End Date",
        value=max_date,
        min_value=min_date,
        max_value=max_date
    )
    
    st.sidebar.divider()
    
    # Year Filter
    year = st.sidebar.multiselect(
        "Select Year",
        options=sorted(df["Order Year"].unique())
    )
    
    # Market Filter
    market = st.sidebar.multiselect(
        "Select Market",
        options=sorted(df["Market"].unique())
    )
    
    # Region Filter
    region = st.sidebar.multiselect(
        "Select Region",
        options=sorted(df["Region"].unique())
    )
    
    # Category Filter
    category = st.sidebar.multiselect(
        "Select Category",
        options=sorted(df["Category"].unique())
    )
    
    # Segment Filter
    segment = st.sidebar.multiselect(
        "Select Segment",
        options=sorted(df["Segment"].unique())
    )
    
    # Apply Date Filter
    filtered_df = df.copy()
    
    if start_date and end_date:
        filtered_df = filtered_df[
            (filtered_df["Order Date"].dt.date >= start_date) &
            (filtered_df["Order Date"].dt.date <= end_date)
        ]
    
    # Apply Year Filters
    if year:
        filtered_df = filtered_df[filtered_df["Order Year"].isin(year)]
    
    # Apply Market Filter
    if market:
        filtered_df = filtered_df[filtered_df["Market"].isin(market)]
    
    # Apply Region Filter
    if region:
        filtered_df = filtered_df[filtered_df["Region"].isin(region)]
    
    # Apply Category Filter
    if category:
        filtered_df = filtered_df[filtered_df["Category"].isin(category)]
    
    # Apply Segment Filter
    if segment:
        filtered_df = filtered_df[filtered_df["Segment"].isin(segment)]



    # Sidebar Information
    st.sidebar.divider()
    
    st.sidebar.metric("Records Found", len(filtered_df))
    
    
    return filtered_df