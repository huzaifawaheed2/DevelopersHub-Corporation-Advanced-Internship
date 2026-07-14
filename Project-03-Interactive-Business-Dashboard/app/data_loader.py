from pathlib import Path

import pandas as pd
import streamlit as st


@st.cache_data
def load_data():
    """
    Load cleaned Global Superstore dataset.
    """

    project_root = Path(__file__).resolve().parent.parent

    dataset_path = (
        project_root
        / "dataset"
        / "Global_Superstore_Cleaned.csv"
    )

    df = pd.read_csv(
        dataset_path,
        parse_dates=["Order Date"]
    )

    return df