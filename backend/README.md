

# Backend del Proyecto Datamine

Este documento proporciona una guía detallada para trabajar en el backend del proyecto Datamine. Este sistema utiliza **Django** y **Django REST Framework** para la gestión de usuarios, facturas, pagos y contadores, permitiendo una administración eficiente de datos a través de una **API REST**.

## Tabla de Contenidos

1. [Requisitos](#requisitos)
2. [Instalación y Configuración](#instalación-y-configuración)
3. [Ejecución del Servidor y URLs](#ejecución-del-servidor-y-urls)
4. [Estructura de Carpetas](#estructura-de-carpetas)
5. [Descripción de Archivos Clave](#descripción-de-archivos-clave)
6. [Endpoints y Funcionalidades](#endpoints-y-funcionalidades)
7. [Buenas Prácticas y Colaboración en GitHub](#buenas-prácticas-y-colaboración-en-github)

---

## Requisitos

Para ejecutar este proyecto, asegúrate de tener instalados:

- **Python** 3.8 o superior
- **Django** 5.1.2
- **Django REST Framework**

## Instalación y Configuración

### Clonar el Repositorio

Clona el repositorio desde GitHub:

```bash
git clone https://github.com/samusplay/datamine_proyect.git
```

### Acceder al Directorio del Backend

Navega al directorio del backend:

```bash
cd datamine_proyect/backend
```

### Crear un Entorno Virtual

Crea un entorno virtual para manejar las dependencias del proyecto:

```bash
python3 -m venv env
```

### Activar el Entorno Virtual

- En macOS y Linux:

  ```bash
  source env/bin/activate
  ```

- En Windows:

  ```bash
  .\env\Scripts\activate
  ```

### Instalar Dependencias

Instala todas las dependencias necesarias desde el archivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

### Crear y Aplicar Migraciones

Ejecuta las migraciones de la base de datos:

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## Ejecución del Servidor y URLs

Para ejecutar el servidor de desarrollo:

```bash
python manage.py runserver
```

Accede a la aplicación en los siguientes URLs:

- **API principal**: [http://localhost:8000/api/](http://localhost:8000/api/) *(Revisa si esta URL es la correcta de acuerdo a la configuración actual)*
- **Módulo de Facturas**: [http://localhost:8000/api/facturas/](http://localhost:8000/api/facturas/)
- **Módulo de Usuarios**: [http://localhost:8000/api/usuarios/](http://localhost:8000/api/usuarios/)
- **Módulo de Contadores**: [http://localhost:8000/api/contadores/](http://localhost:8000/api/contadores/)
- **Módulo de Pagos**: [http://localhost:8000/api/pagos/](http://localhost:8000/api/pagos/)
- **Panel de Administración**: [http://localhost:8000/admin/](http://localhost:8000/admin/)

---

## Estructura de Carpetas

Esta es la estructura de carpetas del backend, organizada en módulos que corresponden a las funcionalidades de usuarios, facturas, pagos y contadores.

```
backend/
├── api/                    # Módulo de API
├── contadores/             # Módulo de gestión de contadores
├── facturas/               # Módulo de facturación
│   ├── migrations/         # Migraciones de la base de datos
│   ├── models.py           # Modelos de base de datos de facturas
│   ├── views.py            # Vistas y lógica de la API de facturas
│   └── serializers.py      # Serializadores para formato JSON
├── pagos/                  # Módulo de pagos
│   ├── models.py
│   ├── views.py
│   └── serializers.py
├── usuarios/               # Módulo de usuarios y autenticación
│   ├── models.py
│   ├── views.py
│   └── serializers.py
├── settings.py             # Configuración del proyecto
├── urls.py                 # Rutas de la API
└── wsgi.py                 # Configuración para el servidor WSGI
```

---

## Descripción de Archivos Clave

### `models.py`

Define los modelos de la base de datos para cada módulo (usuarios, facturas, pagos, contadores). Cada modelo representa una tabla en la base de datos:

- **Facturas**: Contiene campos como `contador_mes_anterior`, `contador_mes_actual`, `consumo`, `costo_total`.
- **Usuarios**: Gestiona la información de los usuarios que interactúan con la aplicación.
- **Pagos**: Controla los registros de pagos y su estado.
- **Contadores**: Almacena el número de contador de cada usuario para seguimiento de consumo.

### `serializers.py`

Convierte los datos de los modelos en JSON y viceversa, permitiendo que el frontend y el backend intercambien datos de forma estructurada.

### `views.py`

Contiene la lógica de las vistas de la API:

- **FacturaListCreateView**: Vista para listar y crear facturas, calcula automáticamente el consumo de energía y el costo total.
- **UsuarioListCreateView**: Vista para gestionar la creación y consulta de usuarios.
- **PagoListCreateView**: Vista para la gestión de pagos realizados por los usuarios.

### `urls.py`

Define las rutas de cada endpoint. Configura los caminos para que el frontend pueda interactuar con los módulos del backend. Incluye:

- `/api/facturas/` para el módulo de facturas.
- `/api/usuarios/` para el módulo de usuarios.
- `/api/pagos/` para el módulo de pagos.

---

## Endpoints y Funcionalidades

1. **Usuarios**
   - `POST /api/usuarios/crear/`: Crea un nuevo usuario en el sistema.
   - `GET /api/usuarios/`: Lista todos los usuarios registrados.

2. **Facturas**
   - `POST /api/facturas/crear/`: Genera una nueva factura, calculando automáticamente el consumo basado en el contador.
   - `GET /api/facturas/`: Lista todas las facturas registradas.

3. **Pagos**
   - `POST /api/pagos/`: Registra un pago nuevo y su estado.
   - `GET /api/pagos/`: Lista todos los pagos registrados.

---

## Buenas Prácticas y Colaboración en GitHub

### Creación de Ramas y Subida de Cambios

Cada desarrollador debe trabajar en su propia rama para evitar conflictos:

1. **Crear una nueva rama**:

   ```bash
   git checkout -b nombre-de-la-rama
   ```

2. **Realizar cambios** en el código y luego hacer un commit:

   ```bash
   git add .
   git commit -m "Descripción breve del cambio"
   ```

3. **Subir la rama al repositorio remoto**:

   ```bash
   git push origin nombre-de-la-rama
   ```

4. **Solicitar un Pull Request** en GitHub para que los cambios puedan ser revisados e integrados en la rama principal (`master`).

### Buenas Prácticas

- **Usar nombres descriptivos** en los commits para facilitar la revisión del historial.
- **Documentar funciones** y clases clave para que otros desarrolladores puedan entender la lógica del código.
- **Mantener los archivos organizados** y en sus carpetas correspondientes para evitar confusión.

---

## Objetivos del Proyecto

Este proyecto sigue la metodología **Lean Startup**. Los objetivos principales son:

1. **Validar el MVP** en el menor tiempo posible para obtener retroalimentación.
2. **Iterar sobre el producto**, haciendo mejoras en base a la retroalimentación de los usuarios.
3. **Optimizar funcionalidades** esenciales (facturas, pagos y gestión de usuarios) para asegurar que el sistema sea escalable y eficiente.


