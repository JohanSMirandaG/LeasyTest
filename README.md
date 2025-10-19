PRUEBA TÉCNICA — LEASY
----------------------

Este proyecto fue desarrollado como parte de la prueba técnica para desarrollador Django (Semi Senior / Senior) en LEASY.

El sistema permite autenticación por correo electrónico, gestión básica de usuarios, clientes, autos, contratos e invoices, y visualización mediante un dashboard con Bootstrap 5. Incluye despliegue con Docker y uWSGI.

-------------------------------------------------
TECNOLOGÍAS UTILIZADAS
-------------------------------------------------
- Python 3.13
- Django 5.2.7
- PostgreSQL
- uWSGI
- Docker y Docker Compose
- Bootstrap 5
- django-widget-tweaks
- pandas / openpyxl
- whitenoise

-------------------------------------------------
ESTRUCTURA DEL PROYECTO
-------------------------------------------------
LeasyTest/

├── accounts/       -> Autenticación y creación de usuarios

├── cars/           -> Gestión de vehículos

├── clients/        -> Gestión de clientes

├── contracts/      -> Contratos (Dashboard principal)

├── invoices/       -> Cuotas e invoices

├── leasy_test_project/   -> Configuraciones globales (settings.py, urls.py, wsgi.py)

├── static/         -> Archivos estáticos

├── templates/      -> HTML con Bootstrap 5

├── manage.py

├── uwsgi.ini

├── docker-compose.yml

├── Dockerfile

└── requirements.txt

-------------------------------------------------
INSTALACIÓN Y EJECUCIÓN CON DOCKER
-------------------------------------------------

1. Clonar el repositorio:
   git clone https://github.com/JohanSMirandaG/LeasyTest.git

   cd LeasyTest


2. Crear un archivo .env en la raíz del proyecto con el siguiente contenido:

    SECRET_KEY=XXXXX

    POSTGRES_DB=XXXXX

    POSTGRES_USER=XXXXX

    POSTGRES_PASSWORD=XXXXX

    POSTGRES_HOST=XXXXX

    POSTGRES_PORT=XXXXX

    DEBUG=False 


3. Construir y levantar los contenedores:

   docker compose build --no-cache

   docker compose up -d

   Esto instalará las dependencias, aplicará migraciones y levantará uWSGI en el puerto 8000.


4. Crear el superusuario:
   docker compose exec web python manage.py createsuperuser

   Luego acceder desde:
   http://localhost:8000/accounts/login/

-------------------------------------------------
AUTENTICACIÓN Y PERMISOS
-------------------------------------------------
- Los usuarios inician sesión con correo y contraseña.
- Solo los administradores pueden crear nuevos usuarios.
- No se manejan roles personalizados en esta versión (solo admin).

-------------------------------------------------
DASHBOARD
-------------------------------------------------
- Listado paginado de contratos (20 por página).
- Buscador por nombre, documento o placa.
- Acceso solo a usuarios autenticados.
- Consultas optimizadas con select_related para mejorar rendimiento.

-------------------------------------------------
CARGA DE ARCHIVOS (OPCIONAL / PENDIENTE)
-------------------------------------------------
- Admite carga de archivos Excel (.xlsx) o CSV.
- Valida columnas requeridas (cliente, auto, monto, fecha).
- Inserta registros en las tablas Client, Car, Contract e Invoice.
- Muestra mensajes de éxito o error según el resultado.

-------------------------------------------------
BUENAS PRÁCTICAS IMPLEMENTADAS
-------------------------------------------------
- Arquitectura modular: cada entidad es una app independiente.
- Uso de vistas basadas en clases (CBV).
- Paginación con el sistema nativo de Django.
- Manejo de mensajes del framework.
- Protección CSRF y autenticación personalizada.
- Uso de Bootstrap 5 para UI moderna.
- Configuración de uWSGI para entornos productivos.
- whitenoise para servir archivos estáticos en Docker.

-------------------------------------------------
COMANDOS ÚTILES
-------------------------------------------------
Crear migraciones en local:
  python manage.py makemigrations

Aplicar migraciones en local:
  python manage.py migrate

Recolectar estáticos en local:
  python manage.py collectstatic --noinput

Ejecutar servidor local:
  python manage.py runserver 0.0.0.0:8000

Ejecutar en Docker:
  docker compose up

Entrar al contenedor:
  docker compose exec web bash

Crear superusuario con Docker:
  docker compose exec web python manage.py createsuperuser

-------------------------------------------------
LICENCIA Y AUTOR
-------------------------------------------------
Proyecto desarrollado exclusivamente con fines evaluativos
para el proceso técnico de selección de **LEASY**.

👤 Johan Miranda  
💻 Desarrollador Full Stack — Django | Ruby on Rails | Spring Boot  
📍 Bogotá, Colombia  
📅 2025
