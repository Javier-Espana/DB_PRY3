import streamlit as st
import pandas as pd
import plotly.express as px

def render_table(title: str, data: list[dict]):
    st.subheader(title)
    if not data:
        st.info("No hay datos disponibles.")
        return
    
    df = pd.DataFrame(data)
    
    # Configurar formato para columnas conocidas
    format_dict = {
        'monto_total': "${:,.2f}",
        'monto_recaudado': "${:,.2f}",
        'meta_monetaria': "${:,.2f}",
        'porcentaje_cumplimiento': "{:.2%}",
        'porcentaje_completado': "{:.2%}"
    }
    
    # Aplicar formatos solo a las columnas existentes
    format_columns = {k: v for k, v in format_dict.items() if k in df.columns}
    
    st.dataframe(
        df.style.format(format_columns),
        use_container_width=True,
        height=min(35 * len(df) + 3, 500)
    )

def render_metric(label: str, value: str | int | float, delta: str = ""):
    st.metric(label=label, value=value, delta=delta)

def render_filters(filters: dict):
    """Función para renderizar filtros comunes"""
    with st.expander("Filtros"):
        for key, config in filters.items():
            if config["type"] == "date":
                st.date_input(
                    label=config["label"],
                    value=config["value"],
                    key=key
                )
            elif config["type"] == "number":
                st.number_input(
                    label=config["label"],
                    min_value=config.get("min", 0),
                    max_value=config.get("max", None),
                    value=config["value"],
                    step=config.get("step", 1),
                    key=key
                )
            elif config["type"] == "select":
                st.selectbox(
                    label=config["label"],
                    options=config["options"],
                    key=key
                )