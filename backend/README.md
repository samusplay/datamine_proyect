README para Backend (backend/README.md)
1. Introducción
Este es el backend del proyecto Datamine, creado con Django y Django REST Framework. La aplicación maneja módulos para la gestión de facturas, usuarios, pagos y contadores, ofreciendo una API para el consumo desde el frontend.

2. Requisitos
Python 3.8+
Django 5.1.2
Virtualenv para crear entornos virtuales
3. Instalación
bash
Copiar código
# Clonar el repositorio
git clone https://github.com/samusplay/datamine_proyect.git

# Acceder al directorio backend
cd datamine_proyect/backend

# Crear un entorno virtual
python3 -m venv env

# Activar el entorno virtual
source env/bin/activate  # En macOS o Linux
env\Scripts\activate     # En Windows

# Instalar dependencias
pip install -r requirements.txt
4. Migraciones y Base de Datos
bash
Copiar código
# Crear las migraciones
python manage.py makemigrations

# Aplicar las migraciones
python manage.py migrate
5. Ejecutar el Servidor de Desarrollo
bash
Copiar código
python manage.py runserver
El servidor se iniciará en http://127.0.0.1:8000/.

6. Estructura de Carpetas
api/: Módulos de API.
facturas/: Funcionalidades y modelos para la gestión de facturas.
usuarios/: Administración de usuarios.
pagos/: Módulo de pagos.
settings.py: Configuraciones de Django.
7. Rutas Principales del API
Usuarios: /api/usuarios/
Facturas: /api/facturas/
Pagos: /api/pagos/
