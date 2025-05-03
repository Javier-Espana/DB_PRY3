import streamlit as st
from services.reports import (
    get_donaciones_por_campana,
    get_voluntarios_por_actividad,
    get_donaciones_por_donante,
    get_distribucion_voluntarios_por_edad,
    get_efectividad_campanas
)
from components.ui_elements import render_table, render_metric, render_filters
from utils.helpers import format_currency, format_percentage
from datetime import datetime, timedelta

st.set_page_config(page_title="Reportería ONG", layout="wide")
st.title("Panel de Reportería - ONG")

# Fechas por defecto para los filtros
default_start = datetime.now() - timedelta(days=365)
default_end = datetime.now()

# Reporte 1: Donaciones por Campaña
st.markdown("---")
st.header("Resumen de Donaciones por Campaña")

with st.expander("Filtros"):
    fecha_inicio_don = st.date_input("Fecha inicio donaciones", value=default_start, key="fecha_inicio_don")
    fecha_fin_don = st.date_input("Fecha fin donaciones", value=default_end, key="fecha_fin_don")
    monto_min = st.number_input("Monto mínimo", min_value=0.0, value=0.0, step=10.0, key="monto_min")
    monto_max = st.number_input("Monto máximo", min_value=0.0, value=10000.0, step=10.0, key="monto_max")

donaciones = get_donaciones_por_campana(
    fecha_inicio=fecha_inicio_don,
    fecha_fin=fecha_fin_don,
    monto_minimo=monto_min,
    monto_maximo=monto_max
)
render_table("Donaciones por Campaña", donaciones)

if donaciones:
    monto_total = sum(d["monto_total"] or 0 for d in donaciones)
    total_donaciones = sum(d["total_donaciones"] or 0 for d in donaciones)
    col1, col2 = st.columns(2)
    col1.write("### Total Donaciones")
    render_metric("Total Donaciones", total_donaciones)
    col2.write("### Monto Total")
    render_metric("Monto Total", format_currency(monto_total))

# Reporte 2: Voluntarios por Actividad
st.markdown("---")
st.header("Participación de Voluntarios por Actividad")

with st.expander("Filtros"):
    fecha_inicio_vol = st.date_input("Fecha inicio actividades", value=default_start, key="fecha_inicio_vol")
    fecha_fin_vol = st.date_input("Fecha fin actividades", value=default_end, key="fecha_fin_vol")
    edad_min = st.number_input("Edad mínima", min_value=16, max_value=100, value=18, key="edad_min")
    edad_max = st.number_input("Edad máxima", min_value=16, max_value=100, value=65, key="edad_max")

voluntarios = get_voluntarios_por_actividad(
    fecha_inicio=fecha_inicio_vol,
    fecha_fin=fecha_fin_vol,
    edad_minima=edad_min,
    edad_maxima=edad_max
)
render_table("Voluntarios por Actividad", voluntarios)

if voluntarios:
    total_voluntarios = sum(v["total_voluntarios"] or 0 for v in voluntarios)
    st.write("### Total Voluntarios")
    render_metric("Total Voluntarios", total_voluntarios)

# Reporte 3: Donaciones por Donante
st.markdown("---")
st.header("Donaciones por Donante")

with st.expander("Filtros"):
    fecha_inicio_donante = st.date_input("Fecha inicio", value=default_start, key="fecha_inicio_donante")
    fecha_fin_donante = st.date_input("Fecha fin", value=default_end, key="fecha_fin_donante")
    tipo_donante = st.selectbox("Tipo de donante", ["Todos", "individual", "empresa"], key="tipo_donante")
    monto_min_donante = st.number_input("Monto mínimo", min_value=0.0, value=100.0, step=10.0, key="monto_min_donante")

donantes = get_donaciones_por_donante(
    fecha_inicio=fecha_inicio_donante,
    fecha_fin=fecha_fin_donante,
    tipo_donante=tipo_donante if tipo_donante != "Todos" else None,
    monto_minimo=monto_min_donante
)
render_table("Donaciones por Donante", donantes)

# Reporte 4: Distribución de Voluntarios por Edad
st.markdown("---")
st.header("Distribución de Voluntarios por Edad")

with st.expander("Filtros"):
    fecha_inicio_edad = st.date_input("Fecha inicio", value=default_start, key="fecha_inicio_edad")
    fecha_fin_edad = st.date_input("Fecha fin", value=default_end, key="fecha_fin_edad")
    genero = st.selectbox("Género", ["Todos", "Masculino", "Femenino", "Otro"], key="genero")
    actividad_id = st.number_input("ID de Actividad (opcional)", min_value=1, value=None, key="actividad_id")

distribucion = get_distribucion_voluntarios_por_edad(
    fecha_inicio=fecha_inicio_edad,
    fecha_fin=fecha_fin_edad,
    genero=genero if genero != "Todos" else None,
    actividad_id=actividad_id if actividad_id else None
)
render_table("Distribución por Edad", distribucion)

if distribucion:
    st.bar_chart(
        data=distribucion,
        x="grupo_edad",
        y="total_voluntarios",
        use_container_width=True
    )

# Reporte 5: Efectividad de Campañas
st.markdown("---")
st.header("Efectividad de Campañas")

with st.expander("Filtros"):
    fecha_inicio_efec = st.date_input("Fecha inicio campañas", value=default_start, key="fecha_inicio_efec")
    fecha_fin_efec = st.date_input("Fecha fin campañas", value=default_end, key="fecha_fin_efec")
    monto_objetivo_min = st.number_input("Monto objetivo mínimo", min_value=0.0, value=1000.0, step=100.0, key="monto_objetivo_min")
    monto_objetivo_max = st.number_input("Monto objetivo máximo", min_value=0.0, value=100000.0, step=1000.0, key="monto_objetivo_max")

efectividad = get_efectividad_campanas(
    fecha_inicio=fecha_inicio_efec,
    fecha_fin=fecha_fin_efec,
    monto_objetivo_min=monto_objetivo_min,
    monto_objetivo_max=monto_objetivo_max
)

# Formatear porcentaje para mostrar
for campana in efectividad:
    campana["porcentaje_cumplimiento"] = format_percentage(campana["porcentaje_cumplimiento"])

render_table("Efectividad de Campañas", efectividad)

if efectividad:
    st.line_chart(
        data=efectividad,
        x="campana",
        y="monto_recaudado",
        use_container_width=True
    )