

```markdown
# Datamine Project - Backend

## Descripción General
Este backend es parte del proyecto Datamine, desarrollado con Django y Django REST Framework. Su objetivo es gestionar la facturación de consumo eléctrico de los usuarios, con funcionalidades específicas para manejar:
- **Facturas**: Registro de consumo mensual de energía.
- **Usuarios**: Autenticación y gestión de perfiles de usuarios.
- **Pagos**: Registro de transacciones realizadas por los usuarios.

Este README documenta el trabajo realizado en el backend, los endpoints disponibles, y las instrucciones para que el equipo pueda colaborar eficientemente en el desarrollo.

## Estructura del Proyecto
```plaintext
backend/
├── api/
├── contadores/
├── facturas/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
├── pagos/
├── usuarios/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
├── settings.py
├── urls.py
└── wsgi.py
```

## Modelos Implementados

### 1. Factura
Este modelo gestiona el registro del consumo de energía de cada usuario en un período mensual. A continuación, se detallan los atributos y su funcionalidad:
- **numero_contador**: Identificador del contador del usuario.
- **contador_mes_anterior**: Valor del contador al finalizar el mes anterior.
- **contador_mes_actual**: Valor actual del contador al final del mes.
- **consumo**: Consumo total de energía en el mes (calculado automáticamente).
- **costo_total**: Costo total del consumo en pesos colombianos (calculado automáticamente).
- **usuario**: Relación con el modelo de usuario.
- **fecha_emision**: Fecha de emisión de la factura.

### 2. Usuario
El modelo de usuario gestiona la información básica y autenticación de los usuarios. Este modelo está conectado al frontend para permitir el registro y autenticación de usuarios.

## Endpoints Disponibles

### Facturas
El endpoint de facturas permite realizar operaciones CRUD en las facturas de los usuarios. A continuación, se detallan los endpoints específicos:

- **GET /api/facturas/**: Obtiene la lista de facturas registradas.
- **POST /api/facturas/**: Crea una nueva factura para un usuario. Este endpoint valida automáticamente el consumo y el costo basados en el valor del contador actual y el del mes anterior.

Ejemplo de datos para el endpoint POST:
```json
{
  "numero_contador": "12345",
  "contador_mes_actual": 12000,
  "usuario": 1
}
```

La respuesta incluirá los campos calculados:
```json
{
  "numero_contador": "12345",
  "contador_mes_anterior": 11500,
  "contador_mes_actual": 12000,
  "consumo": 500,
  "costo_total": 7500,
  "usuario": 1,
  "fecha_emision": "2023-11-07"
}
```

#### Validaciones
- El contador del mes actual debe ser mayor que el del mes anterior.
- Si ya existe una factura para el mismo usuario y mes, devuelve un error para evitar duplicados.

### Usuarios
Actualmente, el modelo de usuario está conectado con el frontend, permitiendo:
- Registro de nuevos usuarios.
- Autenticación y manejo de perfiles.

## Pruebas de API
Se han realizado pruebas para verificar el funcionamiento de los endpoints de facturas. Todas las pruebas han sido satisfactorias y los endpoints funcionan según lo esperado. 

Ejemplos de pruebas:
- Creación de una factura con el valor del contador actual y verificación del cálculo automático del consumo y costo.
- Validación de duplicados para evitar múltiples facturas para el mismo mes y usuario.
- Verificación de errores al ingresar un contador actual menor que el contador anterior.

## Instrucciones para Contribuir

### Crear una Rama de Trabajo en Git
Para mantener la organización y evitar conflictos, cada colaborador debe trabajar en su propia rama de Git.

#### Pasos:
1. **Crear una nueva rama**: Cambia `nombre_de_tu_rama` por un nombre relevante a la funcionalidad en la que estás trabajando.
   ```bash
   git checkout -b nombre_de_tu_rama
   ```
2. **Realizar cambios y hacer commit**:
   ```bash
   git add .
   git commit -m "Descripción de los cambios realizados"
   ```
3. **Subir la rama a GitHub**:
   ```bash
   git push origin nombre_de_tu_rama
   ```
4. **Abrir un Pull Request (PR)** en GitHub para revisión. Asegúrate de describir bien los cambios en el PR.

### Instrucciones de Instalación

#### Clonar el Repositorio
```bash
git clone https://github.com/samusplay/datamine_proyect.git
cd datamine_proyect/backend
```

#### Crear y Activar el Entorno Virtual
```bash
python3 -m venv env
source env/bin/activate  # En macOS y Linux
env\Scripts\activate  # En Windows
```

#### Instalar Dependencias
```bash
pip install -r requirements.txt
```

#### Crear y Aplicar Migraciones
```bash
python manage.py makemigrations
python manage.py migrate
```

#### Ejecutar el Servidor de Desarrollo
```bash
python manage.py runserver
```

## Notas Adicionales
- La documentación actual cubre principalmente la API de facturas y el modelo de usuario. Para nuevas funcionalidades, asegúrate de actualizar el README para que esté siempre sincronizado con los cambios del código.
- Siguiendo la metodología Lean Startup, cada iteración debe ser probada con usuarios reales y optimizada en función del feedback recibido.

---

```

### Explicación

Este README incluye todo lo que hemos discutido y trabajado en el backend. Asegúrate de incluir este Markdown en el archivo `README.md` de tu directorio `backend`, y luego puedes hacer commit y push de este archivo a GitHub.

Este enfoque paso a paso ayudará a tus compañeros a entender y colaborar en el proyecto, manteniendo claridad en los objetivos y un buen flujo de trabajo. Además, la metodología **Lean Startup** proporciona un marco para iterar rápidamente y validar el trabajo con usuarios finales, lo que permite ajustar y mejorar la aplicación de manera continua.
