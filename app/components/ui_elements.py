import streamlit as st
import pandas as pd

def render_table(title: str, data: list[dict]):
    st.subheader(title)
    if not data:
        st.info("No hay datos disponibles.")
        return
    df = pd.DataFrame(data)
    st.dataframe(df, use_container_width=True)

def render_metric(label: str, value: str | int | float, delta: str = ""):
    st.metric(label=label, value=value, delta=delta)
