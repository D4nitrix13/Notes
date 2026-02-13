<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- Gitlab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# **Laravel Contacts Application**

*Este es un proyecto completo de una **aplicación de contactos** desarrollada con **Laravel**, con énfasis en buenas prácticas, modularidad, pruebas automatizadas, y despliegue con Docker. Está diseñado como guía de aprendizaje y base para proyectos reales.*

---

## **Tecnologías utilizadas**

- *Laravel 9.52.20*
- *PostgreSQL*
- *Stripe CLI*
- *PHP 8.x*
- *Laravel Mix (Webpack)*
- *Docker & Docker Compose*
- *PHPUnit*
- *VSCode (entorno sugerido)*

---

## **Estructura de contenidos (`Docs/`)**

*La documentación del proyecto está organizada en módulos progresivos. Cada carpeta contiene material práctico y conceptual en formato Markdown (`.md`), junto con ejemplos e imágenes cuando es necesario.*

### **Introducción**

- *Presentación general del proyecto*

### **Laravel Básico**

- *Rutas (`web.php`, `api.php`)*
- *Uso de Composer & Artisan*
- *Introducción al ORM (Eloquent)*
- *Configuración de base de datos*
- *Autenticación de usuarios*

### **Webpack Mix**

- *Activar tema oscuro*
- *Compilar y agrupar CSS y JS con Laravel Mix*

### **HTTP en Laravel**

- *Requests y Responses*
- *Prevención de ataques CSRF*
- *Formularios en Laravel*
- *Implementación del patrón MVC*

### **Validación**

- *Reglas de validación*
- *Manejo de errores y formularios*
- *Tests automatizados de validaciones (`.http` y `cartero`)*

### **CRUD Complete**

- *Métodos Create, Store, Edit, Update, Destroy*
- *Listado e inspección de contactos (`index`, `show`)*

### **Laravel Intermedio**

- *Relaciones Eloquent*
- *Políticas de acceso (`Policies`)*
- *Form Requests personalizados*
- *Mensajes Flash*
- *Componentes Blade reutilizables*
- *Almacenamiento de archivos*
- *Paginación de resultados*

### **Laravel Avanzado**

- *Pagos con Stripe y PayPal*
- *Middlewares personalizados*
- *Reglas de validación con consultas*
- *Relaciones muchos a muchos*
- *Consultas sobre tablas pivote*
- *Correos automáticos*
- *Caching de consultas*
- *Seeders personalizados*
- *Tokens de API (autenticación)*
- *Logging y trazabilidad (`Logger`)*

### **Pruebas Unitarias**

- *Feature Testing de controladores*
- *Unit Testing detallado*
- *Buenas prácticas con PHPUnit*

### **Configuración Limpia**

- *Separación de entornos y credenciales*
- *Configuración por entorno*

### **Arquitectura de Software**

- *Organización de carpetas*
- *Responsabilidades por capa*
- *Principios SOLID aplicados*

### **Dockerizando Laravel**

- *Uso de Docker Compose*
- *Personalización de Dockerfile para Laravel y PostgreSQL*
- *Secrets y configuración segura*
- *Stripe CLI como contenedor*
- *Scripts automatizados (`runApp.sh`, `docker-entrypoint.sh`)*

---

## **Testing**

```bash
php artisan test
```

**Incluye pruebas unitarias y funcionales organizadas por controlador, usando `DatabaseMigrations` para un entorno limpio en cada prueba.**

---

## **Uso con Docker**

```bash
# Copiar fichero de entorno
cp .env.example .env

# Iniciar
docker compose --project-name contacts-application --project-directory . -f docker-compose.yaml up -d

# Detener y limpiar
docker compose --project-name contacts-application --project-directory . -f docker-compose.yaml down --remove-orphans --rmi local --timeout 5
```

---

## **VSCode (Opcional)**

**Incluye archivos recomendados para trabajar en VSCode:**

- *`.vscode/extensions.json`: extensiones sugeridas (Laravel, PHP, Docker)*
- *`.vscode/settings.json`: configuración visual*
- *`.vscode/tasks.json`: tareas automáticas como levantar contenedores al abrir*

---

## **Capturas**

*La carpeta [`/Docs/Images/`](/Docs/Images "/Docs/Images") contiene ejemplos visuales del funcionamiento del sistema, incluyendo:*

- *Checkout con Stripe*
- *Confirmación de correo*
- *Configuración de oyentes locales*
- *Mensajes flash y formularios*

---

## **Licencia**

*MIT © [Daniel Benjamin Perez Morales](https://github.com/D4nitrix13 "https://github.com/D4nitrix13")*

---
