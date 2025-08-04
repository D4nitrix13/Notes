<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# **Laravel + Vite (Frontend moderno con integración eficiente)**

## **Recursos oficiales y útiles:**

* *[Laravel Vite Docs (v9)](https://laravel.com/docs/9.x/vite "https://laravel.com/docs/9.x/vite")*
* *[Laravel Starter Kits (v11)](https://laravel.com/docs/11.x/starter-kits "https://laravel.com/docs/11.x/starter-kits")*
* *[Laravel Breeze (Starter kit básico)](https://github.com/laravel/breeze "https://github.com/laravel/breeze")*
* *[Laravel UI (Alternativa basada en jQuery/Bootstrap)](https://github.com/laravel/ui "https://github.com/laravel/ui")*
* *[Migración de Laravel Mix a Vite](https://github.com/laravel/vite-plugin/blob/main/UPGRADE.md#migrating-from-vite-to-laravel-mix "https://github.com/laravel/vite-plugin/blob/main/UPGRADE.md#migrating-from-vite-to-laravel-mix")*
* *[Error común: No such table on fresh install](https://stackoverflow.com/questions/78700901/no-such-table-error-on-laravel-fresh-installation "https://stackoverflow.com/questions/78700901/no-such-table-error-on-laravel-fresh-installation")*

---

## **Nomenclatura recomendada**

**Para entornos **Linux/Unix**, se recomienda usar nombres de carpetas en:**

* **Proyecto De Laravel**

* *`kebab-case` (ej: `app-vite`)*
* *o completamente en `lowercase`.*

*Esto evita conflictos por diferencias en el manejo de mayúsculas/minúsculas entre sistemas operativos.*

---

## **Crear un nuevo proyecto con Laravel y Vite**

```bash
composer create-project laravel/laravel app-vite
cd app-vite
```

*Esto crea una nueva app Laravel en el directorio `app-vite`, usando la estructura base.*

---

## **Migraciones y frontend**

```bash
php artisan migrate
```

> [!NOTE]
> *Ejecuta todas las migraciones para crear las tablas en la base de datos (debe estar correctamente configurada en `.env`).*

```bash
npm install
```

> [!NOTE]
> *Instala todas las dependencias de frontend definidas en `package.json` (incluye Vite, Tailwind, etc.).*

```bash
npm run dev
```

> *Lanza el servidor de desarrollo de Vite. Compila CSS y JS y habilita recarga en caliente (Hot Module Replacement).*

### **Ejemplo de salida de `npm run dev`**

```bash
VITE v7.0.6  ready in 431 ms
➜  Local:   http://localhost:5173/
➜  Network: use --host to expose
➜  press h + enter to show help

LARAVEL v12.21.0  plugin v2.0.0
➜  APP_URL: http://localhost
```

---

## **Warnings comunes de npm**

```bash
npm warn Unknown builtin config "globalignorefile".
npm warn Unknown builtin config "python".
```

> **Estos mensajes indican que se están usando configuraciones obsoletas en `.npmrc` o el entorno. No afectan de forma crítica, pero conviene revisar.**

---

## **Blade y Vite**

**Laravel usa una directiva específica para importar archivos de frontend con Vite:**

```php
@vite(['resources/css/app.css', 'resources/js/app.js'])
```

> *Esta directiva se encarga de enlazar correctamente los archivos generados por Vite. Sustituye a `mix()` que se usaba con Laravel Mix.*

---

## **Configuración de red para Vite (en entornos Docker, WSL, etc.)**

* **File `app-vite/vite.config.js`**

```js
import laravel from 'laravel-vite-plugin';
import { defineConfig } from 'vite';

export default defineConfig({
    plugins: [
        laravel({
            input: ['resources/css/app.css', 'resources/js/app.js'],
            refresh: true,
        }),
    ],
    server: {
        // Escucha en todas las interfaces de red
        host: '0.0.0.0',
        port: 5174,
        origin: 'http://172.17.0.2:5174',
        cors: true,
        hmr: {
            // Listening on all network interfaces
            host: '172.17.0.2',
        },
    }

});
```

### **Nota:**

* *Usar `0.0.0.0` permite acceder desde fuera del contenedor.*
* *En producción o entornos seguros, se recomienda limitar esto o configurar reglas de red.*
* *También puedes usar directamente la IP de tu máquina host si no estás en Docker.*

---

## **Compilar para producción**

```bash
npm run build
```

> *Crea los archivos optimizados (minificados y sin sourcemaps) para producción. Debes ejecutarlo antes de hacer deploy.*

---

## **Instalar Breeze con Blade**

```bash
composer require laravel/breeze --dev
php artisan breeze:install blade
```

> *Breeze es un starter kit liviano que ofrece autenticación básica, rutas, vistas Blade, y configuración inicial de Vite + Tailwind. Ideal para proyectos simples o como base para personalización.*

---

## **Laravel + Vite + Breeze (Blade)**

---

## **Diferencia al instalar Breeze con o sin argumentos**

### **Instalación interactiva**

```bash
php artisan breeze:install
```

> [!NOTE]
> *Si ejecutas este comando **sin argumentos**, Laravel abrirá un menú interactivo como este:*

```bash
 ┌ Which Breeze stack would you like to install? ───────────────┐
 │ › ● Blade with Alpine                                        │
 │   ○ Livewire (Volt Class API) with Alpine                    │
 │   ○ Livewire (Volt Functional API) with Alpine               │
 │   ○ React with Inertia                                       │
 │   ○ Vue with Inertia                                         │
 │   ○ API only                                                 │
 └──────────────────────────────────────────────────────────────┘
```

*Esto requiere interacción manual (no es apto para automatización o Docker sin TTY).*

---

### **Instalación directa (evita el prompt)**

```bash
php artisan breeze:install blade
```

> *Instala directamente el stack **Blade + Alpine.js** sin requerir intervención del usuario. Ideal para scripting y automatización.*

---

## **`package.json`: scripts y dependencias**

### **Scripts disponibles**

```json
{
    "$schema": "https://json.schemastore.org/package.json",
    "private": true,
    "type": "module",
    "scripts": {
        "build": "vite build",
        "dev": "vite"
    },
    "devDependencies": {
        "@tailwindcss/forms": "^0.5.2",
        "@tailwindcss/vite": "^4.0.0",
        "alpinejs": "^3.4.2",
        "autoprefixer": "^10.4.2",
        "axios": "^1.8.2",
        "concurrently": "^9.0.1",
        "laravel-vite-plugin": "^2.0.0",
        "postcss": "^8.4.31",
        "tailwindcss": "^3.1.0",
        "vite": "^7.0.4"
    }
}
```

* **For production:** *`npm run dev` inicia Vite en modo desarrollo con recarga automática.*
* **For development:** *`npm run build` genera los archivos finales optimizados para producción.*

---

### **Dependencias destacadas**

| **Paquete**                  | **Descripción**                                      |
| ---------------------------- | ---------------------------------------------------- |
| *`vite`*                     | *Bundler moderno ultra rápido.*                      |
| *`laravel-vite-plugin`*      | *Plugin oficial para integrar Laravel con Vite.*     |
| *`alpinejs`*                 | *Framework JS ligero para interacción sin recargar.* |
| *`tailwindcss`*              | *Utilidades CSS modernas.*                           |
| *`@tailwindcss/forms`*       | *Plugin de Tailwind para mejorar formularios.*       |
| *`axios`*                    | *Cliente HTTP para JavaScript.*                      |
| *`postcss` + `autoprefixer`* | *Herramientas para transformar CSS automáticamente.* |

---

## **Explicación completa de `vite.config.js`**

```js
import { defineConfig } from 'vite';
import laravel from 'laravel-vite-plugin';

export default defineConfig({
  plugins: [
    laravel({
      input: ['resources/css/app.css', 'resources/js/app.js'], // Files to compile (entry points)
      refresh: true, // Enables automatic browser refresh on file changes
    }),
  ],
  server: {
    host: '0.0.0.0',                   // Listen on all network interfaces (useful for Docker)
    port: 5174,                        // Port for the Vite dev server
    origin: 'http://172.17.0.2:5174',  // URL used for HMR and CORS
    cors: true,                        // Enable CORS to allow external access
    hmr: {
      host: '172.17.0.2',              // Host/IP used by Hot Module Replacement (HMR)
    },
  },
});
```

---

## **Archivos que serán cargados automáticamente**

*Todo lo que modifiques en los archivos configurados como entrada será recompilado automáticamente por Vite al usar `npm run dev`.*

### **JavaScript (`resources/js/app.js`)**

```js
console.log("Test");
```

### **CSS (`resources/css/app.css`)**

```css
h1 {
  color: red;
}
```

---

## **Ejemplo práctico: `welcome.blade.php`**

*Este archivo de Blade muestra cómo se cargan los recursos con Vite:*

```php
<!DOCTYPE html>
<html lang="{{ str_replace('_', '-', app()->getLocale()) }}">

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Laravel</title>

  {{-- Enlaza los archivos JS y CSS generados por Vite --}}
  @vite(['resources/css/app.css', 'resources/js/app.js'])
</head>

<body class="bg-[#FDFDFC] dark:bg-[#0a0a0a] text-[#1b1b18] flex p-6 lg:p-8 items-center lg:justify-center min-h-screen flex-col">
  <h1>App Vite</h1>
</body>

</html>
```

> [!NOTE]
> *Si colocaste `console.log("Test")` en `app.js` y un estilo en `app.css`, se aplicarán automáticamente al cargar esta vista en el navegador.*

---
