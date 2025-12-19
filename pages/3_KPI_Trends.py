import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

st.set_page_config(layout="wide")

st.header("KPI Trend Analysis")

st.caption(
    "Historical trends for selected profitability and leverage metrics. "
    "Data shown here is illustrative and based on sample financial statements."
)

# --- Load data ---
DATA_DIR = os.path.join("data", "sample")

income = pd.read_csv(os.path.join(DATA_DIR, "comcast_income_statement.csv"))
balance = pd.read_csv(os.path.join(DATA_DIR, "comcast_balance_sheet.csv"))

# Normalize column names (defensive)
balance = balance.rename(
    columns={
        "TotalCurrentAssets": "CurrentAssets",
        "TotalCurrentLiabilities": "CurrentLiabilities",
    }
)

df = income.merge(balance, on="Year")

# --- Compute KPIs ---
df["OperatingMargin"] = df["OperatingIncome"] / df["Revenue"]
df["NetMargin"] = df["NetIncome"] / df["Revenue"]
df["ROE"] = df["NetIncome"] / df["TotalEquity"]
df["DebtToEquity"] = df["TotalLiabilities"] / df["TotalEquity"]

# --- Plot helper ---
def plot_trend(df, column, ylabel):
    fig, ax = plt.subplots(figsize=(7, 4))
    ax.plot(df["Year"], df[column], marker="o")
    ax.set_xlabel("Year")
    ax.set_ylabel(ylabel)
    ax.set_title(f"{column} Trend")
    ax.grid(True, linestyle="--", alpha=0.5)
    st.pyplot(fig)
    plt.close(fig)

# --- Layout ---
col1, col2 = st.columns(2)

with col1:
    plot_trend(df, "OperatingMargin", "Operating Margin")

with col2:
    plot_trend(df, "NetMargin", "Net Margin")

col3, col4 = st.columns(2)

with col3:
    plot_trend(df, "ROE", "Return on Equity")

with col4:
    plot_trend(df, "DebtToEquity", "Debt-to-Equity")
