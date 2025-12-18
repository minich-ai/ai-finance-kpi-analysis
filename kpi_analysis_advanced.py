import streamlit as st

def run():
    st.header("Advanced KPI Analysis")

    st.caption(
        "These KPIs focus on profitability quality, cash generation, and balance-sheet risk. "
        "They are commonly reviewed by senior finance leaders and investors."
    )

    # --- KPI values (hardcoded for now; will later come from real data) ---
    ebitda_margin = "21.4%"
    ebitda_delta = "-0.9% YoY"

    fcf_margin = "14.1%"
    fcf_delta = "+1.2% YoY"

    debt_to_ebitda = "2.3x"
    debt_delta = "-0.2x YoY"

    # --- KPI layout ---
    col1, col2, col3 = st.columns(3)

    with col1:
        st.m

