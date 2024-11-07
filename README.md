# Datamine - Proyecto LuzClick ⚡️

### Transformando la forma en que los inquilinos y propietarios gestionan el consumo de energía y pagos de facturas

---

Bienvenido a **Datamine** 🚀, una empresa con visión de futuro enfocada en crear soluciones tecnológicas innovadoras para facilitar el monitoreo y pago de consumo energético en propiedades arrendadas. Nuestro primer proyecto, **LuzClick**, tiene como misión simplificar el proceso de seguimiento de consumo de energía y administración de pagos de facturas para propietarios e inquilinos. Creemos que una gestión eficiente de recursos energéticos y una experiencia de usuario transparente puede transformar la forma en que las personas interactúan con sus gastos y su impacto energético.

### 🌱 ¿Por qué LuzClick?

La administración de facturación de servicios, particularmente en situaciones de arrendamiento, puede ser complicada. El propietario necesita un sistema de confianza donde el consumo esté registrado de manera exacta, y el inquilino quiere transparencia en el cálculo de su factura. Nos basamos en esta necesidad para diseñar **LuzClick**, una plataforma que permite tanto al propietario como al inquilino gestionar estos procesos con precisión, simplicidad y claridad.

**Problema**  
Muchos propietarios deben gestionar manualmente el consumo de energía de sus propiedades arrendadas y hacer cálculos a mano para dividir las facturas de manera justa entre los inquilinos. Esto no solo consume tiempo, sino que también genera un riesgo de errores y desconfianza. Al mismo tiempo, los inquilinos necesitan una herramienta que les permita saber su consumo en tiempo real y su estado de facturación, para así pagar a tiempo y con transparencia.

### 🎯 Objetivos

1. **Desarrollo de un MVP** en 4 meses que permita a propietarios e inquilinos gestionar su consumo de energía y pago de facturas de manera automatizada.
2. **Validación** de la solución con usuarios reales, recibiendo retroalimentación en tiempo real.
3. **Iteración rápida** para ajustar y mejorar la solución, con un enfoque en **escalabilidad** y **eficiencia**.
4. **Escalabilidad futura** hacia una infraestructura en la nube (AWS) y una aplicación móvil para una experiencia omnicanal.

---

## ✨ Funcionalidades

### Interfaz de Usuario

**Para Inquilinos**  
- Visualización de su consumo actual de energía.
- Información transparente sobre el consumo total en kilovatios por hora y el costo estimado.
- Historial de pagos y facturas previas.
- Un sistema fácil y seguro para realizar pagos de su factura directamente desde la plataforma.

**Para Propietarios**  
- Administración de múltiples propiedades y sus inquilinos.
- Visualización de todos los consumos de sus propiedades, con desglose detallado por inquilino.
- Herramienta de notificación automática para informar a los inquilinos sobre sus próximas facturas y fechas de pago.
- Acceso a los registros históricos de consumo para analizar el uso de energía a lo largo del tiempo.

### Backend

El backend del proyecto utiliza **Django** y **Django REST Framework** para proporcionar una API REST robusta y segura. Este backend facilita la autenticación, el registro de usuarios, la administración de contadores de energía, la generación de facturas y la gestión de pagos.

1. **Autenticación y Gestión de Usuarios**: Registro y autenticación de usuarios con diferentes roles (Inquilino, Propietario) para gestionar el acceso a datos específicos.
2. **Generación Automática de Facturas**: Una vez que el inquilino introduce su contador actual, el sistema calcula automáticamente el consumo del mes comparado con el mes anterior y genera la factura.
3. **Cálculo Dinámico de Consumo y Costo**: Transforma el consumo en unidades de kilovatios por hora (kWh) en un costo monetario, calculado en pesos colombianos, con base en una tarifa predefinida.
4. **Endpoints Personalizados**: Para acceder a los registros de consumo, facturas y pagos, todo centralizado y fácilmente integrable con el frontend.

### Frontend

Nuestra interfaz de usuario está diseñada con **React**, brindando una experiencia intuitiva y atractiva. El frontend se comunica con el backend para:

- Mostrar al inquilino su consumo de energía y su factura actual.
- Permitir al propietario acceder a reportes detallados de consumo de sus propiedades.
- Facilitar el pago seguro de las facturas.
  
### Metodología de Trabajo: Lean Startup

Implementamos el enfoque **Lean Startup** para desarrollar y validar LuzClick. Este enfoque se centra en:

1. **Construir un MVP Rápido**: Un producto mínimo viable que permite lanzar al mercado las funcionalidades clave y obtener retroalimentación real.
2. **Medir y Aprender**: Cada iteración nos proporciona insights valiosos sobre el uso de nuestra solución, permitiéndonos ajustar y mejorar el producto de manera continua.
3. **Escalar solo lo necesario**: Validamos cada funcionalidad antes de expandirla, evitando así costos innecesarios y asegurando una solución efectiva y ajustada a las necesidades reales.

---

## 🚀 Instalación y Configuración

Para cualquier desarrollador que quiera colaborar en el proyecto, los pasos iniciales son:

### Clonar el Repositorio

```bash
git clone https://github.com/samusplay/datamine_proyect.git
cd datamine_proyect
```

### Estructura del Proyecto

```plaintext
datamine_proyect/
├── backend/
│   ├── api/
│   ├── usuarios/
│   ├── facturas/
│   ├── contadores/
│   └── pagos/
└── frontend/
    ├── public/
    └── src/
        ├── components/
        └── utils/
```

### Backend: Configuración e Instalación

1. Crear y activar un entorno virtual
2. Instalar las dependencias desde `requirements.txt`
3. Aplicar migraciones y correr el servidor.

```bash
# En el directorio backend
python manage.py runserver
```

### Frontend: Configuración e Instalación

1. Instalar dependencias con `npm install`
2. Ejecutar el servidor de desarrollo de React:

```bash
npm start
```

---

## 🌎 Endpoints Principales

Estos son algunos de los endpoints esenciales del proyecto:

- **Usuarios**: `/api/usuarios/`
- **Facturas**: `/api/facturas/`
- **Contadores**: `/api/contadores/`
- **Pagos**: `/api/pagos/`
  
---

## 👩‍💻 Buenas Prácticas para Desarrolladores

1. **Trabaja en Ramas**: Antes de hacer cambios, crea una rama:

   ```bash
   git checkout -b nueva-funcionalidad
   ```

2. **Commit y Push**: Al terminar tus cambios, realiza commits descriptivos y sube la rama.

   ```bash
   git add .
   git commit -m "Implementación de la funcionalidad X"
   git push origin nueva-funcionalidad
   ```

3. **Pull Requests**: Solicita un pull request para que tus cambios sean revisados.

---

## Visión de Escalabilidad 📈

En los próximos pasos, planeamos integrar **AWS** para gestionar la infraestructura en la nube y brindar una escalabilidad óptima. Una vez validada la idea, también expandiremos LuzClick a plataformas móviles, garantizando así que la solución esté disponible en cualquier dispositivo.

**Nuestra meta es simple**: Hacer que LuzClick sea la herramienta preferida para la gestión de consumo de energía y pagos en propiedades arrendadas. Queremos ofrecer una experiencia transparente, precisa y eficiente para propietarios e inquilinos. 

--- 

¡Bienvenidos a bordo de **Datamine** y nuestro viaje hacia un futuro más conectado, transparente y eficiente en el consumo de energía! 🌐⚡️


