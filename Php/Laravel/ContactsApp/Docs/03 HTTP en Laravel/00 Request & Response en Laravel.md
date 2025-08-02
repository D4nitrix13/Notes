<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# **Request & Response en Laravel**

> [!NOTE]
> *En Laravel, las solicitudes (**requests**) y respuestas (**responses**) son fundamentales para manejar la comunicación entre el cliente y el servidor. Laravel proporciona una API elegante para trabajar con estas operaciones.*

## **Sintaxis Sugar en Laravel**

*Laravel permite simplificar la sintaxis de rutas utilizando funciones anónimas o funciones flecha en PHP.*

### **Ejemplo 1: Definir una ruta con una función anónima**

```php
Route::get(
    "/contact",
    function () {
        return Response::view("contact");
    }
);
```

### **Ejemplo 2: Utilizando una función flecha (arrow function)**

```php
Route::get(
    "/contact",
    fn() => Response::view("contact")
);
```

*La segunda forma es más concisa y mejora la legibilidad del código.*

## **Función `dd` en Laravel**

*La función `dd()` significa **Dump and Die**. Se usa para depurar código, mostrando la información de una variable y deteniendo la ejecución del script inmediatamente.*

### **Ejemplo:**

```php
Route::post(
    "/contact",
    function (Request $request) {
        dd($request);
    }
);
```

*Si hacemos una solicitud POST a `/contact`, Laravel mostrará los detalles del objeto `$request` en una interfaz amigable.*

## **Manejo de Token CSRF en Laravel**

*Laravel protege las solicitudes POST, PUT, PATCH y DELETE mediante tokens CSRF. Para evitar este chequeo en ciertas rutas, podemos agregar la URL al arreglo `$except` en el middleware `VerifyCsrfToken`.*

**Ubicación del archivo:**
*`ApplicationLaravel/app/Http/Middleware/VerifyCsrfToken.php`*

```php
protected $except = [
    "/contact"
];
```

*Esto evita que Laravel devuelva un error 419 (CSRF Token Mismatch) al hacer una petición POST a `/contact` sin un token CSRF.*

## **Ejemplo de salida de `dd($request);`**

*Cuando depuramos la solicitud con `dd($request);`, podemos obtener una estructura similar a esta:*

```php
Illuminate\Http\Request {#44 ▼ // routes/web.php:35
  #json: null
  #convertedFiles: null
  #userResolver: Closure($guard = null) {#251 ▶}
  #routeResolver: Closure() {#260 ▶}
  +attributes: Symfony\Component\HttpFoundation\ParameterBag {#46 ▶}
  +request: Symfony\Component\HttpFoundation\InputBag {#45 ▶}
  +query: Symfony\Component\HttpFoundation\InputBag {#52 ▶}
  +server: Symfony\Component\HttpFoundation\ServerBag {#48 ▶}
  +files: Symfony\Component\HttpFoundation\FileBag {#49 ▶}
  +cookies: Symfony\Component\HttpFoundation\InputBag {#47 ▶}
  +headers: Symfony\Component\HttpFoundation\HeaderBag {#50 ▶}
  #content: null
  #languages: null
  #charsets: null
  #encodings: null
  #acceptableContentTypes: null
  #pathInfo: "/contact"
  #requestUri: "/contact"
  #baseUrl: ""
  #basePath: null
  #method: "POST"
  #format: null
  #session: Illuminate\Session\Store {#289 ▶}
  #locale: null
  #defaultLocale: "en"
  -preferredFormat: null
  -isHostValid: true
  -isForwardedValid: true
  basePath: ""
  format: "html"
}
```

*Esta estructura muestra los datos de la solicitud, incluyendo las cabeceras, parámetros y método HTTP utilizado.*

## **Acceder a parámetros de la solicitud**

*Podemos extraer información específica de la solicitud mediante métodos de Laravel.*

### **Obtener un valor específico del request**

*Si enviamos un parámetro `phone_number`, podemos acceder a él así:*

```php
dd($request->get("phone_number"));
```

**Salida esperada:**

```bash
"1234" // routes/web.php:35
```

### **Acceder a Query Params**

*Podemos capturar parámetros enviados en la URL.*

#### **Ejemplo de formulario con Query Params:**

```html
<form method="POST" action="/contact?name=Daniel&age=19">
```

**Para acceder a estos valores:**

```php
dd($request->query("name"));
```

**Salida esperada:**

```bash
"Daniel" // routes/web.php:35
```

## **Hacer una petición con `curl`**

*Podemos enviar una solicitud POST con `curl` y visualizar la respuesta JSON usando `jq`.*

### **Ejemplo de petición**

```bash
curl -LsSX POST "http://172.17.0.2:80/contact" \
-H 'Content-Type: application/x-www-form-urlencoded' \
-d "name=Daniel&phone_number=12345678" | jq --ascii-output --indent 2 --color-output
```

**Salida esperada:**

```json
{
  "message": "Hello My Name Is Daniel"
}
```

## **Conclusión**

*Laravel proporciona herramientas poderosas para manejar requests y responses de forma eficiente. Con `dd()`, podemos depurar solicitudes y examinar su contenido en detalle. Además, podemos acceder a los datos enviados por el usuario de diversas formas y gestionar las restricciones de seguridad como CSRF de manera adecuada.*
