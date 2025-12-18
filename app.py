import streamlit as st
from kpi_analysis_basic import run as run_basic
from kpi_analysis_advanced import run as run_advanced

st.set_page_config(
    page_title="Finance KPI Analysis",
    layout="wide"
)

st.title("Finance KPI Analysis Tool")

choice = st.sidebar.radio(
    "Choose analysis:",
    ["Basic KPIs", "Advanced KPIs"]
)

if choice == "Basic KPIs":
    run_basic()
elif choice == "Advanced KPIs":
    run_advanced()
