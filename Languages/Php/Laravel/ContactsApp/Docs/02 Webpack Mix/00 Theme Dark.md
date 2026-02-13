<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# **Aplicar un tema oscuro en Laravel con Bootswatch**  

*Para aplicar un tema oscuro a nuestra aplicación Laravel utilizando **Bootswatch**, seguimos estos pasos:*

---

## **Instalar Bootswatch**

*Ejecutamos el siguiente comando para instalar **Bootswatch** con npm:*

```bash
npm install bootswatch
```

- **Explicación del comando:**  

- **`npm install` →** *Instala un paquete desde el registro de npm.*
- **`bootswatch` →** *Es el paquete que queremos instalar, contiene temas personalizados para Bootstrap.*

---

### **Importar el tema en `app.scss`**  

*Después de la instalación, modificamos el archivo **`/ApplicationLaravel/resources/sass/app.scss`** para importar los estilos de Bootswatch.*

- **Código a agregar en `app.scss`:**  

```scss
// Your variable overrides go here, e.g.:
// $h1-font-size: 3rem;

@import "~bootswatch/dist/darkly/variables";  // Variables del tema oscuro "Darkly"
@import "~bootstrap/scss/bootstrap";         // Importamos Bootstrap
@import "~bootswatch/dist/darkly/bootswatch"; // Aplicamos los estilos del tema oscuro
```

- **Explicación:**  

- **`@import "~bootswatch/dist/darkly/variables";` →** *Importa las variables de diseño del tema "Darkly".*
- **`@import "~bootstrap/scss/bootstrap";` →** *Importa los estilos base de Bootstrap.*
- **`@import "~bootswatch/dist/darkly/bootswatch";` →** *Aplica los estilos del tema "Darkly" encima de Bootstrap.*

- **Importante:**  
*En **`app.scss`** debemos comentar o eliminar la siguiente línea, ya que el tema oscuro ya define su propio color de fondo:*

```scss
// @import '~bootstrap/scss/bootstrap';
```

*También, en **`ApplicationLaravel/resources/sass/_variables.scss`**, debemos comentar o eliminar esta línea:*

```scss
// $body-bg: #f8fafc;
```

*Esto evita que Laravel sobrescriba el fondo del tema oscuro.*

---

### **Modificar la vista `home.blade.php`**  

*Abrimos el archivo **`ApplicationLaravel/resources/views/home.blade.php`** y verificamos que su contenido sea el siguiente:*

```php
@extends('layouts.app')

@section('content')
<div class="container">
    <div class="row justify-content-center">
        <div class="col-md-8">
            <div class="card">
                <div class="card-header">{{ __('Dashboard') }}</div>

                <div class="card-body">
                    @if (session('status'))
                        <div class="alert alert-success" role="alert">
                            {{ session('status') }}
                        </div>
                    @endif

                    {{ __('You are logged in!') }}
                </div>
            </div>
        </div>
    </div>
</div>
@endsection
```

- **Explicación:**  

- **`@extends('layouts.app')` →** *Indica que esta vista hereda de `layouts.app`, que es la plantilla principal.*
- **`@section('content') ... @endsection` →** *Define la sección `content`, donde se carga el contenido principal de la página.*

---

### **Modificar la barra de navegación**  

**En el archivo **`ApplicationLaravel/resources/views/layouts/app.blade.php`**, buscamos esta línea:**

```html
<nav class="navbar navbar-expand-md navbar-light bg-white shadow-sm">
```

**Y la reemplazamos por:**

```html
<nav class="navbar navbar-expand-md navbar-dark bg-dark shadow-sm">
```

- **Explicación de los cambios:**  

- **`navbar-dark` →** *Indica que estamos usando un tema oscuro.*
- **`bg-dark` →** *Cambia el fondo de la barra de navegación a color oscuro.*

---

### **Compilar los cambios automáticamente**  

*En lugar de ejecutar `npm run dev` cada vez que hagamos un cambio, podemos usar el siguiente comando para que los archivos se recompilen automáticamente:*

```bash
npm run watch
```

- **Explicación:**  

- **`npm run watch` →** *Mantiene activo un proceso que recompila los archivos cuando detecta cambios.*
- *Evita que tengamos que ejecutar `npm run dev` manualmente cada vez que hagamos una modificación en los estilos o JavaScript.*

*Si queremos ejecutar el comando en segundo plano sin que bloquee la terminal, usamos:*

```bash
npm run watch &>/dev/null & disown
```

- **Explicación de cada parte del comando:**  

- **`&` →** *Ejecuta el proceso en segundo plano.*
- **`>/dev/null` →** *Redirige la salida estándar a `null` para que no muestre mensajes en la terminal.*
- **`& disown` →** *Separa el proceso de la terminal para que siga ejecutándose incluso si cerramos la sesión.*

---

### **Iniciar el servidor de Laravel**  

*Finalmente, iniciamos el servidor de Laravel con el siguiente comando:*

```bash
php artisan serve --host=0.0.0.0 --port=3030 --tries=10 --ansi -vvv
```

- **Explicación de cada opción:**  

- **`php artisan serve` →** *Inicia el servidor embebido de Laravel.*
- **`--host=0.0.0.0` →** *Permite acceder al servidor desde cualquier IP (ideal para desarrollo en red local).*
- **`--port=3030` →** *Especifica el puerto en el que correrá la aplicación.*
- **`--tries=10` →** *Intenta iniciar el servidor hasta 10 veces si hay errores.*
- **`--ansi` →** *Habilita colores en la salida de la terminal.*
- **`-vvv` →** *Muestra el nivel máximo de detalle en los logs de Laravel.*

---

### **Acceder a la aplicación**  

*Abrimos el navegador y visitamos:*

```bash
http://172.17.0.2:3030/register
```

---

### **Conclusión**  

- *Con estos pasos, hemos instalado Bootswatch, configurado un tema oscuro en nuestra aplicación Laravel y automatizado la compilación de los estilos con `npm run watch`. Ahora, la aplicación cargará automáticamente el tema oscuro sin necesidad de recompilar manualmente.*
