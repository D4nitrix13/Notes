<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# **Manejo de Rutas en Laravel**  

- *En Laravel, Las Rutas Definen **Cómo La Aplicación Responde A Diferentes Solicitudes Http**. Estas Se Configuran En El Archivo:*

- **Ubicación de las rutas:**  

```bash
ApplicationLaravel/routes/web.php
```

## **Ejemplo de una Ruta GET en Laravel (Path: `/routes/web.php`)**

```php
Route::get('/data', function () {
    return 'My Name Is Daniel';
});
```

- **Explicación:**

- *`Route::get('/data', function() {...})`:*
  - *Define una ruta accesible mediante **GET** en la URL `http://localhost:3000/data`.*
  - *Retorna la cadena `"My Name Is Daniel"` cuando se accede a esta ruta.*

### **Prueba con `curl`**

*Podemos probar esta ruta en la terminal con:*

```bash
curl -X GET -sS http://localhost:3000/data; echo
```

**Salida esperada:**

```bash
My Name Is Daniel
```

- **Explicación del comando `curl`:**

- *`-X GET`: Especifica que la petición HTTP es de tipo **GET**.*
- *`-sS`:*
  - *`-s` (silent): Evita mostrar el progreso de la petición.*
  - *`-S` (show error): Muestra errores si ocurren.*
- *`http://localhost:3000/data`: URL a la que se hace la petición.*
- *`echo`: Agrega un salto de línea para que la salida sea más clara.*

---

## **Manejo de Peticiones POST en Laravel**

### **Creando una Ruta POST (Path: `/routes/web.php`)**

```php
Route::post('/data/info', function () {
    return 'Post Ok';
});
```

- **Explicación:**

- *`Route::post('/data/info', function() {...})`:*
  - *Define una ruta accesible mediante **POST** en `http://localhost:3000/data/info`.*
  - *Retorna `"Post Ok"` cuando se accede a esta ruta con una petición POST.*

### **Probando con `curl`**

```bash
curl -X POST -sS http://localhost:3000/data/info; echo
```

**Salida Esperada (Posible Error):**

```bash
Post Ok
```

### **Problema con CSRF y Solución**

> [!NOTE]
> *Laravel protege todas las rutas POST, PUT, PATCH y DELETE contra **ataques CSRF**.*

- *Si intentamos la petición sin deshabilitar esta protección, obtendremos un error **419 Page Expired**.*

### **Cómo Deshabilitar la Protección CSRF para una Ruta Específica**

- **Ubicación:**  

```bash
ApplicationLaravel/app/Http/Middleware/VerifyCsrfToken.php
```

*Dentro de la clase `VerifyCsrfToken`, agregamos la ruta en `$except`:*

```php
protected $except = [
    'data/info'
];
```

- **Explicación:**

- *`$except` es un **array** que almacena rutas **exentas** de la verificación CSRF.*
- *Agregamos `'data/info'` para que Laravel **permita peticiones POST sin token CSRF**.*

*Después de esta modificación, la petición POST con `curl` funcionará correctamente.*

---

## **Explicación Detallada de Opciones y Comandos**

### **Opciones de `curl` en profundidad**

| *Opción* | *Descripción*                                                       |
| -------- | ------------------------------------------------------------------- |
| *`-X`*   | *Especifica el método HTTP (`GET`, `POST`, `PUT`, `DELETE`, etc.).* |
| *`-s`*   | *Modo silencioso (no muestra barra de progreso).*                   |
| *`-S`*   | *Muestra errores si ocurren.*                                       |
| *`-H`*   | *Permite agregar encabezados HTTP personalizados.*                  |
| *`-d`*   | *Envía datos en una petición (ejemplo en POST).*                    |

---

## **Resumen y Recomendaciones**

- *Laravel maneja rutas en `routes/web.php`.*
- *Las rutas **GET** son directas y no requieren protección CSRF.*
- *Las rutas **POST** están protegidas por defecto contra CSRF.*
- *Podemos deshabilitar CSRF en `VerifyCsrfToken.php` para rutas específicas.*
- *`curl` es útil para probar rutas sin usar un navegador.*
