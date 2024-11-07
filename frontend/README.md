
# Frontend del Proyecto Datamine

Este es el frontend del proyecto Datamine, desarrollado con **React**. Esta aplicación consume la API del backend para mostrar datos de usuarios, facturas y pagos.

## Tabla de Contenidos

1. [Requisitos](#requisitos)
2. [Instalación](#instalación)
3. [Ejecución del Servidor](#ejecución-del-servidor)
4. [Estructura de Carpetas](#estructura-de-carpetas)
5. [Pantallas del Frontend](#pantallas-del-frontend)
6. [Buenas Prácticas y Contribuciones](#buenas-prácticas-y-contribuciones)

---

## Requisitos

Asegúrate de tener instaladas las siguientes versiones:

- **Node.js** v14+ (para ejecutar el servidor de desarrollo y manejar dependencias)
- **React** v17+

## Instalación

1. Clona el repositorio si aún no lo tienes:

   ```bash
   git clone https://github.com/samusplay/datamine_proyect.git
   ```

2. Accede al directorio del frontend:

   ```bash
   cd datamine_proyect/frontend
   ```

3. Instala las dependencias necesarias:

   ```bash
   npm install
   ```

## Ejecución del Servidor

Para iniciar el servidor de desarrollo en el frontend, usa el siguiente comando:

```bash
npm start
```

La aplicación se abrirá en tu navegador predeterminado en [http://localhost:3000](http://localhost:3000).

---

## Estructura de Carpetas

Esta es la estructura de carpetas del frontend, donde cada sección cumple una función específica en la aplicación:

```
frontend/
├── node_modules/          # Dependencias instaladas
├── public/                # Archivos estáticos públicos (HTML, iconos, etc.)
│   └── index.html         # HTML base
├── src/                   # Código principal de la aplicación
│   ├── api/               # Funciones para llamadas a la API
│   ├── components/        # Componentes de React reutilizables en la interfaz
│   ├── App.js             # Componente raíz de la aplicación
│   ├── App.css            # Estilos globales
│   ├── index.js           # Punto de entrada de React
│   └── index.css          # Estilos generales
├── package.json           # Archivo de configuración de dependencias y scripts de npm
└── README.md              # Documentación del frontend
```

### Descripción de las Carpetas

- **api/**: Contiene funciones para hacer solicitudes a la API del backend, manejando la comunicación con los endpoints.
- **components/**: Aquí se almacenan los componentes de React, como formularios y elementos de interfaz que se utilizan en varias partes de la aplicación.
- **App.js**: Componente principal que organiza la estructura general de la aplicación.
- **index.js**: Punto de entrada que renderiza el componente principal (`App`) en el DOM.

---

## Pantallas del Frontend

### 1. **Inicio de Sesión de Usuarios**
   - Componente: `Login.js`
   - Funcionalidad: Permite a los usuarios autenticarse para acceder a sus datos de consumo y facturación.

### 2. **Dashboard de Usuario**
   - Componente: `Dashboard.js`
   - Funcionalidad: Resumen del consumo y pagos del usuario. Muestra las facturas recientes y el consumo total de energía.

### 3. **Historial de Facturas**
   - Componente: `FacturasList.js`
   - Funcionalidad: Listado de facturas con detalles del consumo por mes y el costo total.

### 4. **Pantalla de Detalle de Factura**
   - Componente: `FacturaDetail.js`
   - Funcionalidad: Muestra los detalles de una factura seleccionada, incluyendo el consumo en kWh, costo y fecha de emisión.

### 5. **Pantalla de Pago de Facturas**
   - Componente: `PagoFactura.js`
   - Funcionalidad: Permite realizar el pago de facturas pendientes, actualizando el estado de la factura en el backend.

---

## Buenas Prácticas y Contribuciones

### Crear una Rama de Trabajo

Para que cada colaborador trabaje en una funcionalidad separada, sigue estos pasos:

1. Crear una nueva rama:

   ```bash
   git checkout -b nombre_de_tu_rama
   ```

2. Hacer cambios y commits:

   ```bash
   git add .
   git commit -m "Descripción de los cambios"
   ```

3. Subir la rama al repositorio:

   ```bash
   git push origin nombre_de_tu_rama
   ```

### Hacer un Pull Request

Una vez que termines de trabajar en tu rama y quieras integrarla en la rama principal:

1. Ve a GitHub y abre un Pull Request hacia la rama `master`.
2. Solicita revisión de tus compañeros antes de fusionar.

---



