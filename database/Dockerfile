FROM postgres:17.2

# Copia los scripts de inicialización (DDL.sql y Registros.sql)
COPY DDL.sql /docker-entrypoint-initdb.d/
COPY Registros.sql /docker-entrypoint-initdb.d/

# Establece las variables de entorno necesarias para PostgreSQL
ENV POSTGRES_USER=admin
ENV POSTGRES_PASSWORD=password
ENV POSTGRES_DB=reporteria_db

# El contenedor ya expone el puerto 5432 de forma predeterminada
EXPOSE 5432
