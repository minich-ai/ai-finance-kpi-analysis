import streamlit as st

def run():
    st.header("Advanced KPI Analysis")

    metrics = {
        "EBITDA Margin": ("21.4%", "+0.9%"),
        "FCF Margin": ("14.1%", "+1.2%"),
        "Debt / EBITDA": ("2.3x", "-0.2x"),
    }

    cols = st.columns(len(metrics))
    for col, (label, (value, delta)) in zip(cols, metrics.items()):
        with col:
            st.metric(label, value, delta)
