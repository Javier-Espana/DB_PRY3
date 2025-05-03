import streamlit as st
from services.reports import get_donaciones_por_campana, get_voluntarios_por_actividad
from components.ui_elements import render_table, render_metric
from utils.helpers import format_currency

st.set_page_config(page_title="Reportería ONG", layout="wide")

st.title("Panel de Reportería - ONG")

st.markdown("---")
st.header("Resumen de Donaciones por Campaña")

donaciones = get_donaciones_por_campana()
render_table("Donaciones por Campaña", donaciones)

if donaciones:
    monto_total = sum(d["monto_total"] or 0 for d in donaciones)
    total_donaciones = sum(d["total_donaciones"] or 0 for d in donaciones)
    col1, col2 = st.columns(2)
    col1.write("### Total Donaciones")
    render_metric("Total Donaciones", total_donaciones)
    col2.write("### Monto Total")
    render_metric("Monto Total", format_currency(monto_total))

st.markdown("---")
st.header("Participación de Voluntarios por Actividad")

voluntarios = get_voluntarios_por_actividad()
render_table("Voluntarios por Actividad", voluntarios)
