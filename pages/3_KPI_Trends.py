import streamlit as st
import matplotlib.pyplot as plt

from plot_kpi_trends import load_or_build_kpi_table

st.header("KPI Trend Visualizations")

df = load_or_build_kpi_table()

def render_trend(df, column, ylabel):
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(df["Year"], df[column], marker="o")
    ax.set_xlabel("Year")
    ax.set_ylabel(ylabel)
    ax.set_title(f"{column} Trend")
    ax.grid(True, linestyle="--", alpha=0.5)
    st.pyplot(fig)
    plt.close(fig)

render_trend(df, "OperatingMargin", "Operating Margin")
render_trend(df, "NetMargin", "Net Margin")
render_trend(df, "ROE", "Return on Equity")
render_trend(df, "DebtToEquity", "Debt-to-Equity")
