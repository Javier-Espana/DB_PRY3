FROM python:3.11-slim

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Ajusta las rutas para que coincidan con el contexto de construcción
COPY . ./
COPY requirements.txt ./requirements.txt

# Añade el directorio app al PYTHONPATH
ENV PYTHONPATH="${PYTHONPATH}:/app/app"

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto usado por Streamlit
EXPOSE 8501

# Comando por defecto para iniciar la app
CMD ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]
