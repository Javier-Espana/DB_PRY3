from db.connection import get_connection

def get_donaciones_por_campana():
    query = """
    SELECT c.nombre AS campana, COUNT(d.donacion_id) AS total_donaciones, SUM(d.monto) AS monto_total
    FROM campana c
    LEFT JOIN donacion d ON c.campana_id = d.campana_id
    GROUP BY c.nombre
    ORDER BY monto_total DESC;
    """
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(query)
            return cur.fetchall()

def get_voluntarios_por_actividad():
    query = """
    SELECT a.nombre AS actividad, COUNT(va.voluntario_id) AS total_voluntarios
    FROM actividad a
    LEFT JOIN voluntario_actividad va ON a.actividad_id = va.actividad_id
    GROUP BY a.nombre
    ORDER BY total_voluntarios DESC;
    """
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(query)
            return cur.fetchall()
