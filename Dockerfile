# Usa una imagen oficial de Python 3.13
FROM python:3.13-slim

# Evita que Python genere archivos .pyc y usa un buffer de salida más limpio
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Crea y usa un entorno virtual dentro del contenedor
ENV VIRTUAL_ENV=/opt/venv
RUN python -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos de dependencias primero (para aprovechar la caché)
COPY requirements.txt .

# Instala las dependencias, incluido uWSGI
# Instala dependencias del sistema y Python (incluye uWSGI)
RUN apt-get update && \
    apt-get install -y build-essential && \
    pip install --upgrade pip && \
    pip install -r requirements.txt && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copia el resto del código del proyecto
COPY . .

# Ejecuta collectstatic para recolectar archivos estáticos
RUN python manage.py collectstatic --noinput

# Expone el puerto 8000
EXPOSE 8000


# Comando de inicio con uWSGI
CMD ["uwsgi", "--ini", "uwsgi.ini"]
# Comando por defecto para correr el servidor de desarrollo
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
