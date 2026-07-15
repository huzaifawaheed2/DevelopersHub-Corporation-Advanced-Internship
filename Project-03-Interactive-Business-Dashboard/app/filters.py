import streamlit as st


def sidebar_filters(df):
    """
    Create sidebar filters and return the filtered dataframe.
    """


    # Sidebar Title
    st.sidebar.header("Dashboard Filters")


    # Reset All Filters
    if st.sidebar.button(
        "Reset All Filters",
        use_container_width=True
    ):

        st.session_state["year_filter"] = []
        st.session_state["market_filter"] = []
        st.session_state["region_filter"] = []
        st.session_state["category_filter"] = []
        st.session_state["subcategory_filter"] = []
        st.session_state["segment_filter"] = []

        st.session_state["start_date_filter"] = df["Order Date"].min().date()
        st.session_state["end_date_filter"] = df["Order Date"].max().date()

        st.rerun()


    # Create Working DataFrame
    filtered_df = df.copy()


    # Year Filter
    year = st.sidebar.multiselect(
        "Select Year",
        options=sorted(df["Order Year"].unique()),
        key="year_filter"
    )

    if year:
        filtered_df = filtered_df[
            filtered_df["Order Year"].isin(year)
        ]


    # Market Filter
    market = st.sidebar.multiselect(
        "Select Market",
        options=sorted(filtered_df["Market"].unique()),
        key="market_filter"
    )

    if market:
        filtered_df = filtered_df[
            filtered_df["Market"].isin(market)
        ]


    # Region Filter
    # Depends on selected Market
    region = st.sidebar.multiselect(
        "Select Region",
        options=sorted(filtered_df["Region"].unique()),
        key="region_filter"
    )

    if region:
        filtered_df = filtered_df[
            filtered_df["Region"].isin(region)
        ]


    # Category Filter
    category = st.sidebar.multiselect(
        "Select Category",
        options=sorted(filtered_df["Category"].unique()),
        key="category_filter"
    )

    if category:
        filtered_df = filtered_df[
            filtered_df["Category"].isin(category)
        ]


    # Sub-Category Filter
    # Depends on selected Category
    sub_category = st.sidebar.multiselect(
        "Select Sub-Category",
        options=sorted(filtered_df["Sub-Category"].unique()),
        key="subcategory_filter"
    )

    if sub_category:
        filtered_df = filtered_df[
            filtered_df["Sub-Category"].isin(sub_category)
        ]


    # Segment Filter
    segment = st.sidebar.multiselect(
        "Select Segment",
        options=sorted(filtered_df["Segment"].unique()),
        key="segment_filter"
    )

    if segment:
        filtered_df = filtered_df[
            filtered_df["Segment"].isin(segment)
        ]


    # Date Filters
    st.sidebar.divider()

    min_date = filtered_df["Order Date"].min().date()
    max_date = filtered_df["Order Date"].max().date()

    start_date = st.sidebar.date_input(
        "Start Date",
        value=min_date,
        min_value=min_date,
        max_value=max_date,
        key="start_date_filter"
    )

    end_date = st.sidebar.date_input(
        "End Date",
        value=max_date,
        min_value=min_date,
        max_value=max_date,
        key="end_date_filter"
    )


    # Apply Date Filter
    filtered_df = filtered_df[
        (filtered_df["Order Date"].dt.date >= start_date)
        &
        (filtered_df["Order Date"].dt.date <= end_date)
    ]


    # Sidebar Information
    st.sidebar.divider()

    st.sidebar.metric(
        "Records Found",
        len(filtered_df)
    )

    return filtered_df