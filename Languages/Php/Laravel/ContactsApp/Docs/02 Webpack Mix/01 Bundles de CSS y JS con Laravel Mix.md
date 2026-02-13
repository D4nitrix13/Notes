<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# **Bundles de CSS y JS con Laravel Mix**

## **Explicación de cada parte del código `ApplicationLaravel/resources/views/welcome.blade.php`**

```blade
@extends('layouts.app')

@push('scripts')
  <script src="{{ asset('js/welcome.js') }}" defer></script>
@endpush

@section('content')
  <div class="welcome d-flex align-items-center justify-content-center">
    <div class="text-center">
      <h1>Store Your Contacts Now</h1>
      <a class="btn btn-lg btn-dark" href="register.php">Get Started</a>
    </div>
  </div>
@endsection
```

### **`@extends('layouts.app')`**

- **¿Qué hace?**  
  - *Indica que esta vista hereda de la plantilla `layouts.app`.*
  - *Laravel usa Blade como motor de plantillas, y `@extends` permite reutilizar estructuras de diseño.*

- **¿Dónde está ubicada `layouts.app`?**  
  - *Laravel sigue una convención donde las vistas están en `resources/views/`.*
  - *`layouts.app` se traduce a `resources/views/layouts/app.blade.php`.*

---

#### **`src="{{ asset('js/welcome.js') }}"`**

- **¿Qué hace?**  
  - *Genera la URL pública del archivo `js/welcome.js` usando la función `asset()`.*
  - *`asset('js/welcome.js')` devuelve la ruta absoluta según la configuración de Laravel, normalmente `/public/js/welcome.js`.*

- **¿Dónde está ubicado el archivo?**  
  - *Laravel sirve los archivos estáticos desde `public/`, por lo que `js/welcome.js` debe estar en:*

    ```bash
    /public/js/welcome.js
    ```

---

#### **`@push('scripts')`**

```blade
@push('scripts')
  <script src="{{ asset('js/welcome.js') }}" defer></script>
@endpush
```

- **¿Qué hace?**  
  - *Agrega contenido a una pila llamada `scripts`, que luego puede insertarse en `layouts.app` con `@stack('scripts')`.*
  - *`defer` indica que el script se ejecutará después de cargar la página.*

- **¿Dónde se insertará esto?**  
  - *En `layouts.app.blade.php`, debe haber algo como:*

    ```blade
    @stack('scripts')
    ```

  - *Esto asegura que los scripts adicionales sean insertados en la ubicación deseada.*

---

#### **`@section('content')`**

```blade
@section('content')
  <div class="welcome d-flex align-items-center justify-content-center">
    <div class="text-center">
      <h1>Store Your Contacts Now</h1>
      <a class="btn btn-lg btn-dark" href="register.php">Get Started</a>
    </div>
  </div>
@endsection
```

- **¿Qué hace?**  
  - *Define el contenido de la sección `content`, que se insertará en `layouts.app` donde haya `@yield('content')`.*

- **¿Dónde se inserta?**  
  - *En `resources/views/layouts/app.blade.php`, debe haber:*

    ```blade
    @yield('content')
    ```

  - *Esto coloca la sección en la plantilla principal.*

---

### **Resumen de Ubicaciones**

| **Código**                             | **Ubicación en Laravel**                                               |
| -------------------------------------- | ---------------------------------------------------------------------- |
| *`@extends('layouts.app')`*            | *`resources/views/layouts/app.blade.php`*                              |
| *`src="{{ asset('js/welcome.js') }}"`* | *`public/js/welcome.js`*                                               |
| *`@push('scripts')`*                   | *Depende de `@stack('scripts')` en `layouts.app.blade.php`*            |
| *`@section('content')`*                | *Se inserta donde esté `@yield('content')` en `layouts.app.blade.php`* |

---

### **Laravel: Gestión de Recursos y Blade**

### **Seguridad en Aplicaciones Laravel**

*En una aplicación web, no se debe permitir que los usuarios accedan directamente a los archivos fuente de la aplicación. Por ello, Laravel compila y coloca los archivos estáticos en la carpeta `public/`. Esto se logra mediante herramientas como Laravel Mix, que se ejecuta con:*

```bash
npm run watch
```

*Este comando observa los archivos fuente y los recompila automáticamente cuando se detectan cambios.*

---

## **¿Qué es Blade y para qué sirve?**

*Blade es el motor de plantillas de Laravel. Permite escribir vistas de manera estructurada y reutilizable con directivas como `@extends`, `@section`, `@yield`, entre otras.*

### **Características de Blade**

- *Permite la herencia de plantillas con `@extends('layouts.app')`.*
- *Usa `@yield('content')` para definir secciones.*
- *Permite lógica PHP dentro de la vista, por ejemplo:*

---

## **Creación de Recursos en Laravel**

*Para gestionar imágenes en el proyecto, creamos una carpeta específica dentro de `resources/` con:*

```bash
mkdir resources/img
```

*Esto nos permite mantener organizados los archivos de imagen antes de ser movidos a `public/`.*

---

## **Configuración de Laravel Mix**

*En el archivo `webpack.mix.js`, definimos cómo se deben compilar los recursos estáticos.*

**Primero, agregamos la compilación de CSS:**

```js
const mix = require('laravel-mix');

mix.js('resources/js/app.js', 'public/js')
    .sass('resources/sass/app.scss', 'public/css')
    .css('resources/css/app.css', 'public/css')
    .sourceMaps();
```

**Si ya estamos ejecutando `npm run watch`, debemos detenerlo para aplicar cambios:**

```bash
Ctrl + C
```

**A continuación, añadimos la copia de imágenes al final del archivo `webpack.mix.js`:**

```js
.copy('resources/img', 'public/img');
```

**El archivo final quedaría así:**

```js
const mix = require('laravel-mix');

mix.js('resources/js/app.js', 'public/js')
    .sass('resources/sass/app.scss', 'public/css')
    .css('resources/css/app.css', 'public/css')
    .copy('resources/img', 'public/img')
    .sourceMaps();
```

---

## **Verificación de Recursos Disponibles**

**Podemos comprobar qué recursos están accesibles desde un contenedor Docker ejecutando:**

```bash
curl -sSX GET http://$(docker container inspect -f "{{ .NetworkSettings.IPAddress }}" $(docker container list -qaf status=running -f expose=8000 -f publish=8000)):80/robots.txt
```

**Si el archivo `robots.txt` está disponible, se listará su contenido.**

---

## **Creación y Uso de `welcome.js`**

**Creamos un nuevo archivo JavaScript para la funcionalidad de la página de bienvenida:**

```bash
touch resources/js/welcome.js
```

**Pegamos el siguiente código en `resources/js/welcome.js`:**

```js
const navbar = document.querySelector(".navbar");
const welcome = document.querySelector(".welcome");
const navbarToggle = document.querySelector("#navbarSupportedContent");

const resizeBakgroundImg = () => {
  const height = window.innerHeight - navbar.clientHeight;
  welcome.style.height = `${height}px`;
};

navbarToggle.ontransitionend = resizeBakgroundImg;
navbarToggle.ontransitionstart = resizeBakgroundImg;
window.onresize = resizeBakgroundImg;
window.onload = resizeBakgroundImg;
document.querySelector('main').classList.remove('py-4');
```

**Ahora lo añadimos a `webpack.mix.js` para que se compile correctamente:**

```js
mix.js('resources/js/welcome.js', 'public/js/welcome.js');
```

- **El patrón es el siguiente:**
  - *El primer argumento es la ruta de origen, donde se encuentra el archivo que quieres procesar (resources/js/welcome.js).*
  - *El segundo argumento es la ruta de destino, donde se guardará el archivo procesado después de la compilación (public/js/welcome.js).*

**El archivo final de `webpack.mix.js` incluiría:**

```js
const mix = require('laravel-mix');

mix.js('resources/js/app.js', 'public/js')
    .js('resources/js/welcome.js', 'public/js/welcome.js')
    .sass('resources/sass/app.scss', 'public/css')
    .css('resources/css/app.css', 'public/css')
    .copy('resources/img', 'public/img')
    .sourceMaps();
```

---

## **Variables de Entorno en Laravel**

*En el archivo `.env`, se definen variables como el nombre de la aplicación:*

```ini
APP_NAME="Contacts App"
```

**Esto afecta cómo Laravel identifica la aplicación.**

---

## **Uso de `robots.txt` [Recurso](https://developers.google.com/search/docs/crawling-indexing/robots/create-robots-txt?hl=es "https://developers.google.com/search/docs/crawling-indexing/robots/create-robots-txt?hl=es")**

> [!NOTE]
> **El archivo `robots.txt` se usa para indicar a los motores de búsqueda qué páginas pueden rastrear. Ejemplo para bloquear el bot de Google en una ruta específica:**

```ini
User-agent: Googlebot
Disallow: /nogooglebot/
```

**Para permitir acceso a todos los bots:**

```ini
User-agent: *
Allow: /
```

**También se puede definir la ubicación del sitemap:**

```ini
Sitemap: https://www.example.com/sitemap.xml
```
