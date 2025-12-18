import streamlit as st

def run():
    st.header("Advanced KPI Analysis")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Revenue Growth", "8.2%", "+0.6% YoY")

    with col2:
        st.metric("EBITDA Margin", "21.4%", "-0.9%")

    with col3:
        st.metric("FCF Margin", "14.1%", "+1.2%")

