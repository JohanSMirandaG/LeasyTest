# Usa una imagen oficial de Python
FROM python:3.12-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el archivo de requerimientos
COPY requirements.txt .

# Instala las dependencias
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copia el resto del código del proyecto
COPY . .

# Expone el puerto 8000 para la aplicación
EXPOSE 8000

# Comando por defecto para ejecutar la aplicación
CMD ["gunicorn", "leasy_test_project.wsgi:application", "--bind", "0.0.0.0:8000"]
