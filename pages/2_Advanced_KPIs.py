import streamlit as st

st.set_page_config(layout="wide")

st.header("Advanced KPI Analysis")

st.caption(
    "Advanced profitability, cash flow, and leverage metrics commonly used by "
    "senior finance leaders and investors."
)

# --- KPI values (hard-coded demo values for now) ---
ebitda_margin = "21.4%"
ebitda_delta = "-0.9% YoY"

fcf_margin = "14.1%"
fcf_delta = "+1.2% YoY"

debt_to_ebitda = "2.3x"
debt_delta = "-0.2x YoY"

# --- Layout ---
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("EBITDA Margin", ebitda_margin, ebitda_delta)
    st.caption("Operating profitability before capital structure effects.")

with col2:
    st.metric("Free Cash Flow Margin", fcf_margin, fcf_delta)
    st.caption("Efficiency of revenue converted into discretionary cash.")

with col3:
    st.metric("Debt / EBITDA", debt_to_ebitda, debt_delta)
    st.caption("Leverage ratio commonly reviewed in credit analysis.")

st.divider()

st.subheader("Interpretation")

st.write(
    """
    While EBITDA margin declined modestly year-over-year, improvements in free cash
    flow margin and reduced leverage suggest stronger underlying cash discipline and
    balance-sheet resilience. This mixed signal is often viewed favorably during
    periods of margin pressure.
    """
)
