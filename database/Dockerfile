FROM postgres:17.2



# Copia los archivos necesarios al directorio de inicialización de PostgreSQL
COPY DDL.sql /docker-entrypoint-initdb.d/DDL.sql
COPY Registros.sql /docker-entrypoint-initdb.d/Registros.sql

# Establece las variables de entorno necesarias para PostgreSQL
ENV POSTGRES_USER=admin
ENV POSTGRES_PASSWORD=admin_password
ENV POSTGRES_DB=reporteria_db

# El contenedor ya expone el puerto 5432 de forma predeterminada
EXPOSE 5432
