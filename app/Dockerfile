FROM python:3.11-slim

WORKDIR /app

# 1. Copia solo requirements.txt primero para aprovechar la caché
COPY requirements.txt ./requirements.txt

# 2. Instala dependencias primero
RUN pip install --no-cache-dir -r requirements.txt

# 3. Ahora copia el resto del proyecto
COPY . .

# 4. Configura PYTHONPATH si tu código lo necesita
ENV PYTHONPATH="${PYTHONPATH}:/app/app"

EXPOSE 8501

CMD ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]