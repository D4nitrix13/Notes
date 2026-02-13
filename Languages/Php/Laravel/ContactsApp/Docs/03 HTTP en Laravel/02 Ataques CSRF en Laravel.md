<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# **Ataques CSRF En Laravel**

## **1. Autenticación y Logs de Laravel:**

> [!IMPORTANT]
> *Cuando nos autenticamos en Laravel, la salida de los logs se puede ver en el archivo `laravel.log`, que normalmente se encuentra en la carpeta `storage/logs` dentro de tu proyecto. Para ver el primer registro de este archivo (el más reciente), puedes ejecutar el siguiente comando:*

```bash
head -n1 storage/logs/laravel.log
```

**Explicación del comando:**

- **`head`:** *Es un comando de Unix/Linux que muestra las primeras líneas de un archivo.*
- **`-n1`:** *Le indica a `head` que solo muestre la primera línea del archivo.*
- **`storage/logs/laravel.log`:** *Es la ruta al archivo de logs de Laravel.*

**Salida del Log:**
*Cuando te autenticas o realizas alguna acción en Laravel, la salida del log podría ser algo como esto:*

```bash
[2025-03-16 03:11:29] local.ERROR: could not find driver (SQL: select count(*) as aggregate from "users" where "email" = zeus@gmail.com) {"exception":"[object] (Illuminate\\Database\\QueryException(code: 0): could not find driver (SQL: select count(*) as aggregate from \"users\" where \"email\" = zeus@gmail.com) at /App/ApplicationLaravel/vendor/laravel/framework/src/Illuminate/Database/Connection.php:760)
```

**Desglosando la salida del log:**

- **`[2025-03-16 03:11:29]`:** *Esta es la fecha y hora en que ocurrió el error.*
- **`local.ERROR`:** *Indica el entorno (`local`) y el tipo de log (`ERROR`).*
- **`could not find driver`:** *El mensaje de error indica que Laravel no puede encontrar el controlador necesario para conectar con la base de datos. Esto normalmente ocurre cuando falta el driver de PHP para el motor de base de datos que estás utilizando (en este caso, probablemente PostgreSQL).*
- *El resto del mensaje muestra una excepción que indica que no se puede ejecutar la consulta SQL debido a la falta de un controlador (driver).*

**Referencias útiles para resolver el problema:**
*Se incluyen enlaces a Stack Overflow con posibles soluciones:*

- **PDOException: could not find driver** *en PostgreSQL, que sugiere instalar el driver adecuado para PDO (PHP Data Objects) en PostgreSQL.*

### **2. Conexión a PostgreSQL dentro de un contenedor Docker:**

```bash
docker container exec --interactive --tty --user 0:0 --privileged db psql -h 172.17.0.2 -U postgres -p 5432 -d contacts_app
```

**Explicación del comando:**

- **`docker container exec`:** *Ejecuta un comando dentro de un contenedor Docker en ejecución.*
- **`--interactive` o `-i`:** *Mantiene la entrada interactiva.*
- **`--tty` o `-t`:** *Asigna un terminal interactivo (similar a cuando ejecutas comandos directamente en la terminal).*
- **`--user 0:0`:** *Ejecuta el comando con el usuario root dentro del contenedor.*
- **`--privileged`:** *Otorga permisos elevados dentro del contenedor.*
- **`db`:** *El nombre del contenedor Docker donde está corriendo PostgreSQL.*
- **`psql`:** *Es el cliente de línea de comandos de PostgreSQL para ejecutar consultas SQL.*
- **`-h 172.17.0.2`:** *La dirección IP del servidor de la base de datos (en este caso, dentro de la red Docker).*
- **`-U postgres`:** *El usuario de PostgreSQL con el que te conectarás.*
- **`-p 5432`:** *El puerto en el que PostgreSQL está escuchando.*
- **`-d contacts_app`:** *El nombre de la base de datos a la que te estás conectando.*

*Este comando te permite conectarte a la base de datos de PostgreSQL dentro de un contenedor Docker y ejecutar consultas directamente desde la línea de comandos.*

### **3. Uso de la librería en Laravel:**

*En Laravel, podemos importar librerías usando la directiva `use`. Cuando importamos una librería, podemos asignarle un alias si la clase que estamos importando tiene un nombre largo o confuso. Por ejemplo:*

```php
use Illuminate\Support\Facades\Response;
```

*Esto importa la clase `Response` que se encuentra en el espacio de nombres `Illuminate\Support\Facades`.*

*Si deseas renombrar una clase para evitar conflictos o hacerlo más claro, puedes usar el alias `as`:*

```php
use Illuminate\Http\Response as HttpResponse;
```

*En este caso, `Response` de `Illuminate\Http` se renombra como `HttpResponse` para que sea más fácil de usar en el código.*

### **4. Creación de una ruta para cambiar la contraseña:**

*En Laravel, puedes definir rutas utilizando el método `Route`. Aquí te muestro un ejemplo donde se define una ruta `POST` que maneja el cambio de contraseña:*

```php
Route::post(
    "/change-password",
    function () {
        if (Auth::check()) return new HttpResponse("Authenticated");
        else return (new HttpResponse("Not Authenticated"))->setStatusCode(401);
    }
);
```

**Explicación del código:**

- **`Route::post()`:** *Define una ruta que maneja solicitudes HTTP `POST` en el endpoint `/change-password`.*
- **`function () {}`:** *Define la función que se ejecutará cuando se acceda a esta ruta.*
- **`Auth::check()`:** *Verifica si el usuario está autenticado.*
- **`HttpResponse`:** *Es una clase que nos permite crear una respuesta HTTP. En este caso, si el usuario está autenticado, la respuesta es "Authenticated", de lo contrario, es "Not Authenticated" con un código de estado `401` (no autorizado).*

### **5. Uso de funciones predefinidas en Laravel:**

*En Laravel, muchas funciones y servicios están precargados, por lo que no es necesario cargarlos manualmente en cada controlador o archivo. Un ejemplo es la función `auth()` para acceder a la autenticación del usuario:*

```php
Route::post(
    "/change-password",
    function (Request $request) {
        if (auth()->check()) return response(
            "Password Changed to {$request->get('password')}"
        );
        else return new response("Not Password Changed", 401);
    }
);
```

**Desglosando el código:**

- **`auth()->check()`:** *Verifica si el usuario está autenticado. En lugar de usar `Auth::check()`, puedes usar el helper `auth()` para realizar la misma comprobación.*
- **`response()`:** *Es una función que devuelve una respuesta HTTP. Aquí se utiliza para devolver el mensaje de que la contraseña ha sido cambiada, junto con el nuevo valor de la contraseña (`$request->get('password')`).*
- **`new response()`:** *Si el usuario no está autenticado, se devuelve una respuesta con el mensaje "Not Password Changed" y el código de estado HTTP `401`.*

**Resumen:**

- **`auth()->check()`:** *Verifica si el usuario está autenticado.*
- **`response()`:** *Crea una respuesta HTTP, que puede ser configurada con diferentes valores, incluyendo texto y códigos de estado.*

---

### **1. Creación de un directorio y archivo HTML**

*Primero, creamos un nuevo directorio y un archivo HTML en ese directorio.*

```bash
mkdir attack-server
touch attack-server/index.html
```

**Explicación de los comandos:**

- **`mkdir attack-server`:** *Crea un directorio llamado `attack-server`. El comando `mkdir` es utilizado para crear directorios.*
- **`touch attack-server/index.html`:** *Crea un archivo vacío llamado `index.html` dentro del directorio `attack-server`. El comando `touch` se utiliza para crear archivos vacíos o actualizar la fecha y hora de modificación de un archivo existente.*

---

### **2. Contenido del archivo HTML**

*Dentro del archivo `index.html`, colocamos el siguiente código HTML:*

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Attacker website</title>
</head>
<body>
  <div>
    <h1>
      Some nice website
    </h1>
    <form name="form" action="http://172.17.0.2:80/change-password" method="POST">
      <input type="hidden" name="password" value="12345678">
    </form>
  </div>
  <script>
    document.form.submit();

    // fetch('http://172.17.0.2:80/change-password', {
    //   method: 'POST',
    //   credentials: 'include',
    //   mode: 'no-cors',
    //   headers: {
    //     'Content-Type': 'application/x-www-form-urlencoded',
    //   },
    //   body: 'email=hacker@hack.com',
    // })
    //   .then(res => console.log(res.status))
    //   .catch(err => console.log(err));

    // fetch('http://172.17.0.2:80/change-password', { credentials: 'include' })
    //   .then(res => res.text())
    //   .then(html => console.log(html))
    //   .catch(err => console.log(err));
  </script>
</body>
</html>
```

**Explicación del código HTML y JavaScript:**

- **Estructura HTML básica:** *El código define una página HTML básica con un título (`<title>Attacker website</title>`) y un formulario.*
  - **Formulario:** *El formulario tiene un `input` oculto (`type="hidden"`) con el nombre `password` y el valor `12345678`. Este formulario tiene la acción configurada para hacer una solicitud `POST` a la URL `http://172.17.0.2:80/change-password`, que es la ruta a la que se enviarán los datos del formulario.*
  - **JavaScript:** *El script en el archivo HTML automáticamente envía el formulario cuando la página se carga usando `document.form.submit();`.*
  - **Código comentado de `fetch`:** *Hay varios fragmentos de código comentado que intentan enviar una solicitud `POST` usando el método `fetch`.*
    - **`fetch`:** *El método `fetch` es utilizado para hacer solicitudes HTTP desde JavaScript. En este caso, se usa para hacer una solicitud `POST` a la misma URL con una cabecera específica y con datos de formulario en el cuerpo de la solicitud.*

---

### **3. Iniciar el servidor PHP**

*Para servir el archivo `index.html` mediante un servidor PHP, usamos el siguiente comando:*

```bash
php -S 0.0.0.0:9000
```

**Explicación del comando:**

- **`php -S`:** *El comando `php -S` inicia un servidor web en PHP que puede servir archivos estáticos como HTML.*
- **`0.0.0.0:9000`:** *Especifica que el servidor debe escuchar en todas las interfaces de red (`0.0.0.0`) en el puerto `9000`. Esto permite que el servidor sea accesible desde cualquier dirección IP en la máquina.*

*Este comando pone en marcha un servidor PHP incorporado en el que puedes probar tu archivo HTML localmente.*

---

### **4. Cookies de autenticación**

*Para entender cómo funcionan las cookies en este contexto, debes saber que es necesario estar autenticado en el sistema antes de realizar ciertas acciones. Las cookies de autenticación están almacenadas en el archivo `cookies.sqlite`.*

**Ruta de las cookies de Firefox:**
*El archivo `cookies.sqlite` se encuentra en el siguiente directorio:*

```bash
/home/d4nitrix13/snap/firefox/common/.mozilla/firefox/kgsw5eou.default/cookies.sqlite
```

*Este archivo contiene las cookies utilizadas por Firefox para gestionar sesiones, incluyendo cookies de autenticación.*

---

### **5. Crear un contenedor Docker**

*Ahora vamos a crear un contenedor Docker para copiar el archivo `cookies.sqlite` dentro del contenedor y poder consultarlo desde allí.*

**Creación del contenedor:**

```bash
docker run -ituroot:root --rm --name alpine-sqlite alpine:latest
```

**Explicación del comando:**

- **`docker run`:** *Ejecuta un contenedor nuevo.*
- **`-it`:** *Activa el modo interactivo y asigna un terminal (TTY).*
- **`--user root:root`:** *Ejecuta el contenedor como el usuario `root` y el grupo `root`.*
- **`--rm`:** *Elimina el contenedor automáticamente después de que termine su ejecución.*
- **`--name alpine-sqlite`:** *Asigna el nombre `alpine-sqlite` al contenedor.*
- **`alpine:latest`:** *Usa la imagen `alpine:latest` de Docker, que es una imagen ligera de Linux basada en Alpine Linux.*

---

### **6. Copiar el archivo `cookies.sqlite` al contenedor**

*Para copiar el archivo `cookies.sqlite` dentro del contenedor, usamos el siguiente comando:*

```bash
docker container cp /home/d4nitrix13/snap/firefox/common/.mozilla/firefox/kgsw5eou.default/cookies.sqlite alpine-sqlite:/db/
```

**Explicación del comando:**

- **`docker container cp`:** *Copia archivos de la máquina local al contenedor.*
- **`/home/d4nitrix13/snap/firefox/common/.mozilla/firefox/kgsw5eou.default/cookies.sqlite`:** *Es la ruta completa del archivo `cookies.sqlite` en tu máquina local.*
- **`alpine-sqlite:/db/`:** *Copia el archivo al directorio `/db/` dentro del contenedor `alpine-sqlite`.*

*Otra forma de escribirlo sería:*

```bash
docker cp /home/d4nitrix13/snap/firefox/common/.mozilla/firefox/kgsw5eou.default/cookies.sqlite alpine-sqlite:/db/cookies.sqlite
```

*Este comando copia el archivo `cookies.sqlite` directamente al contenedor para que podamos usarlo dentro del entorno Docker.*

---

### **7. Consultar la base de datos SQLite (cookies)**

*Ahora, vamos a interactuar con la base de datos SQLite dentro del contenedor. Para ello, usamos el comando de SQLite.*

```bash
sqlite> .mode box
sqlite> .header on
sqlite> .shell clear -T xterm-256color && /home/linuxbrew/.linuxbrew/bin/tmux clear-history || clear -T xterm-256color || clear
```

**Explicación de los comandos:**

- **`.mode box`:** *Establece el formato de salida a "box", lo que organiza la información en un formato de tabla.*
- **`.header on`:** *Muestra los encabezados de las columnas en la salida de las consultas.*
- **`.shell clear`:** *Limpia la pantalla de la terminal, útil para hacer más legible la salida en un entorno interactivo.*

---

### **8. Ver la estructura de la tabla de cookies**

*Usamos el siguiente comando para ver la estructura de la tabla `moz_cookies` dentro de la base de datos SQLite:*

```bash
sqlite> PRAGMA TABLE_INFO(moz_cookies);
```

**Explicación del comando:**

- **`PRAGMA TABLE_INFO(moz_cookies);`:** *Este comando muestra la estructura de la tabla `moz_cookies`, que es donde se almacenan las cookies de Firefox.*

**La salida será algo como esto:**

```sql
┌─────┬───────────────────────────┬─────────┬─────────┬────────────┬────┐
│ cid │           name            │  type   │ notnull │ dflt_value │ pk │
├─────┼───────────────────────────┼─────────┼─────────┼────────────┼────┤
│ 0   │ id                        │ INTEGER │ 0       │            │ 1  │
│ 1   │ originAttributes          │ TEXT    │ 1       │ ''         │ 0  │
│ 2   │ name                      │ TEXT    │ 0       │            │ 0  │
│ 3   │ value                     │ TEXT    │ 0       │            │ 0  │
│ 4   │ host                      │ TEXT    │ 0       │            │ 0  │
│ 5   │ path                      │ TEXT    │ 0       │            │ 0  │
│ 6   │ expiry                    │ INTEGER │ 0       │            │ 0  │
│ 7   │ lastAccessed              │ INTEGER │ 0       │            │ 0  │
│ 8   │ creationTime              │ INTEGER │ 0       │            │ 0  │
│ 9   │ isSecure                  │ INTEGER │ 0       │            │ 0  │
│ 10  │ isHttpOnly                │ INTEGER │ 0       │            │ 0  │
│ 11  │ inBrowserElement          │ INTEGER │ 0       │ 0          │ 0  │
│ 12  │ sameSite                  │ INTEGER │ 0       │ 0          │ 0  │
│ 13  │ rawSameSite               │ INTEGER │ 0       │ 0          │ 0  │
│ 14  │ schemeMap                 │ INTEGER │ 0       │ 0          │ 0  │
│ 15  │ isPartitionedAttributeSet │ INTEGER │ 0       │ 0          │ 0  │
└─────┴───────────────────────────┴─────────┴─────────┴────────────┴────┘
```

**Explicación de los campos:**

- **id:** *Es el identificador único de la cookie.*
- **name:** *El nombre de la cookie.*
- **value:** *El valor de la cookie.*
- **host:** *El host para el que la cookie es válida.*
- **path:** *El path para el cual la cookie es válida.*
- **expiry:** *El tiempo de expiración de la cookie (en formato UNIX timestamp).*
- **isSecure:** *Indica si la cookie es segura (solo se envía a través de HTTPS).*
- **isHttpOnly:** *Indica si la cookie solo es accesible a través de HTTP (no mediante JavaScript).*
- **sameSite:** *Indica la política de cookies `SameSite` (como `Strict`, `Lax`, o `None`).*

---

### **9. Esquema de la tabla `moz_cookies`**

*Finalmente, podemos ver el esquema de la tabla `moz_cookies` usando el comando:*

```bash
sqlite> .schema moz_cookies
```

*Este comando muestra cómo está definida la tabla `moz_cookies`, incluyendo los tipos de datos y las restricciones de cada columna. La salida será algo como:*

```sql
CREATE TABLE moz_cookies (
    id INTEGER PRIMARY KEY,
    originAttributes TEXT NOT NULL DEFAULT '',
    name TEXT,
    value TEXT,
    host TEXT,
    path TEXT,
    expiry INTEGER,
    lastAccessed INTEGER,
    creationTime INTEGER,
    isSecure INTEGER,
    isHttpOnly INTEGER,
    inBrowserElement INTEGER DEFAULT 0,
    sameSite INTEGER DEFAULT 0,
    rawSameSite INTEGER DEFAULT 0,
    schemeMap INTEGER DEFAULT 0,
    isPartitionedAttributeSet INTEGER DEFAULT 0,
    CONSTRAINT moz_uniqueid UNIQUE (name, host, path, originAttributes)
);
```

*Este esquema define la estructura de la tabla, con varios campos relacionados con las cookies, como el nombre, valor, host, y otras propiedades de la cookie.*

---

### **Recursos adicionales:**

- *[SQLite Docker Container](https://thriveread.com/sqlite-docker-container-and-docker-compose/ "https://thriveread.com/sqlite-docker-container-and-docker-compose/")*
- *[How to change the format of SELECT output SQLite](https://stackoverflow.com/questions/72272830/how-to-change-the-format-of-select-output-sqlite "https://stackoverflow.com/questions/72272830/how-to-change-the-format-of-select-output-sqlite")*
- *[Is there a command to clear screen in SQLite3?](https://stackoverflow.com/questions/21616375/is-there-a-command-to-clear-screen-in-sqlite3 "https://stackoverflow.com/questions/21616375/is-there-a-command-to-clear-screen-in-sqlite3")*

*Voy a desglosar lo que sigue en tus apuntes, detallando cada aspecto de los comandos y explicando qué significa todo en el contexto de la manipulación de cookies en una base de datos SQLite y cómo funciona el ataque:*

### **Comando para Consultar las Cookies**

*El comando `SELECT` en SQLite te permite consultar información de la base de datos de cookies.*

```sql
sqlite> SELECT name, value, host, path, isHttpOnly FROM moz_cookies WHERE name IN ('laravel_session', 'contacts_app_session', 'XSRF-TOKEN') AND host = '172.17.0.2';
```

#### **Desglosando la Consulta SQL**

- **`SELECT`:** *Es el comando básico de SQL que selecciona columnas específicas para mostrar en los resultados.*
- **`name, value, host, path, isHttpOnly`:** *Estas son las columnas de la tabla `moz_cookies` que queremos mostrar en los resultados. Vamos a detallar cada una:*
  - **`name`:** *El nombre de la cookie.*
  - **`value`:** *El valor de la cookie, que generalmente contiene datos importantes de sesión.*
  - **`host`:** *El dominio asociado a la cookie. En este caso, solo seleccionamos cookies cuyo `host` es `172.17.0.2`.*
  - **`path`:** *La ruta en la cual la cookie es válida dentro del servidor.*
  - **`isHttpOnly`:** *Un valor que indica si la cookie está marcada como `HttpOnly` (lo que significa que no puede ser accedida mediante JavaScript en el cliente).*
- **`WHERE`:** *Filtra las filas basándose en condiciones específicas. Aquí, seleccionamos solo las cookies con los nombres `laravel_session`, `contacts_app_session` o `XSRF-TOKEN` y un `host` igual a `172.17.0.2`.*

#### **Salida de la Consulta SQL**

*La salida de esta consulta es una tabla con las cookies seleccionadas:*

```sql
┌──────────────────────┬──────────────────────────────────────────────────────────────┬────────────┬──────┬────────────┐
│         name         │                            value                             │    host    │ path │ isHttpOnly │
├──────────────────────┼──────────────────────────────────────────────────────────────┼────────────┼──────┼────────────┤
│ XSRF-TOKEN           │ eyJpdiI6IjBTVGJEZE1IZlViM2l2R1pZR1lsbXc9PSIsInZhbHVlIjoibTk4 │ 172.17.0.2 │ /    │ 0          │
│                      │ UWNuUCsxa2VJK0FuM01CVStvU0lSc2hBVUVpTC81VXVUS0ZTRnZJMCtLekJZ │            │      │            │
│                      │ bGRoaUttTHh0MnJ6MGsxSFpINzhVUWVBQ3ljODhybzhuMCtsKy9nS1ExQ0w1 │            │      │            │
│                      │ YW05WlBEbmp5WHljcjZlS1VjRzZ2d2sxeVB4NUtqdzNBZXUiLCJtYWMiOiI4 │            │      │            │
│                      │ YmY2Mjc3NWM2MDU1YjIyYmY4MmRjZWFhMzc4MTRlY2VmM2Y2YWY3Y2ZkY2Yx │            │      │            │
│                      │ ODA1Y2YyNTIyNDM3NTk4NWY5IiwidGFnIjoiIn0%3D                   │            │      │            │
├──────────────────────┼──────────────────────────────────────────────────────────────┼────────────┼──────┼────────────┤
│ contacts_app_session │ eyJpdiI6Im94ZnNCYTN2cEw1TTBwUitja3pvTnc9PSIsInZhbHVlIjoiVWMy │ 172.17.0.2 │ /    │ 1          │
│                      │ blNPUjM5Wncxa3hLaVlzeDQrTXVtK3p5OGNCZ2tZN0tqV0FpWnBIZnBqZE91 │            │      │            │
│                      │ MTBKRDN5NTUwNjFLQmY0TU1uZEx5eUkrdnNORFdjRUdXVUZDZ1JWZXdZN1kx │            │      │            │
│                      │ RjhYSlArM1RFb01ybG1WL050U3ZHcjRoeVpJNkRwOHU0elAiLCJtYWMiOiJh │            │      │            │
│                      │ OWMxNTBiYjRjOTA5ODEwY2RlY2NhYWE1NzAwZTM3MmMwOWY3ZGRmZjRhM2Uw │            │      │            │
│                      │ ZmViYjc4MTI5Y2FkNWRhODk4IiwidGFnIjoiIn0%3D                   │            │      │            │
├──────────────────────┼──────────────────────────────────────────────────────────────┼────────────┼──────┼────────────┤
│ laravel_session      │ eyJpdiI6IjFHTDVwSnNrU1pLOWxoRHZKbFR3c0E9PSIsInZhbHVlIjoibGFr │ 172.17.0.2 │ /    │ 1          │
│                      │ cHZqNk5vWHFWTjdKcTBZeUEzbXNpcnZ5RUsvNXlaL1NiNnFtS0dhSU1yVGw5 │            │      │            │
│                      │ eWpLTzFIcUtYSWRPaklrYm4vcXhZb1VQTEdScFp3V0UzTlV0RkNzT1VTQjBt │            │      │            │
│                      │ aXhEaU8zM21UTG0zUFNKR2lYN1FOazQzZ3kramt3TFZMNnIiLCJtYWMiOiI3 │            │      │            │
│                      │ ODk5ZjE5NjhlOTk5ZGJiYmUxYmM5NGYyMGFhOWRmNDRiOTYyZGMwNzJiNGE4 │            │      │            │
│                      │ YTQ4OTIzYjk4YWZkZThhMmVhIiwidGFnIjoiIn0%3D                   │            │      │            │
└──────────────────────┴──────────────────────────────────────────────────────────────┴────────────┴──────┴────────────┘
```

- **XSRF-TOKEN:** *Este es un token CSRF (Cross-Site Request Forgery) que se utiliza como medida de seguridad para prevenir ciertos tipos de ataques.*
- **contacts_app_session y laravel_session:** *Son cookies de sesión que identifican al usuario autenticado en la aplicación web. Contienen datos cifrados y específicos para cada sesión.*

**`isHttpOnly`:** *La columna `isHttpOnly` indica si la cookie está marcada para que no pueda ser accedida desde JavaScript en el navegador. En el caso de las cookies `contacts_app_session` y `laravel_session`, su valor es `1`, lo que significa que están marcadas como `HttpOnly` y no pueden ser leídas desde el código JavaScript. Sin embargo, en el caso de `XSRF-TOKEN`, el valor es `0`, lo que indica que sí puede ser accedida por JavaScript.*

### **El Flujo de la Petición y el Ataque**

- **Cómo funciona el ataque:**
  - *En el navegador, si un usuario está autenticado y tiene la cookie correspondiente (por ejemplo, `laravel_session`, `contacts_app_session` o `XSRF-TOKEN`), cualquier petición que se envíe al servidor incluirá esa cookie.*
  - *Esto significa que el atacante puede hacer que el navegador del usuario realice una solicitud legítima sin que el usuario lo sepa, si ya está autenticado.*
  
  *En este caso, al enviar una petición mediante el navegador, el servidor puede redirigir al usuario a otro endpoint:*

  ```bash
  http://172.17.0.2:9000/ → redirige a → http://172.17.0.2:80/change-password
  ```

  - **Redirección:** *La redirección ocurre cuando el navegador recibe una respuesta del servidor solicitando que vaya a una nueva URL. El ataque depende de que el servidor esté configurado para redirigir la petición al endpoint `/change-password`.*
  
  - **Cambio de Contraseña:** *Al llegar al endpoint `/change-password`, el formulario enviado realiza una solicitud **POST** con el siguiente campo oculto:*

    ```html
    <form name="form" action="http://172.17.0.2:80/change-password" method="POST">
      <input type="hidden" name="password" value="12345678">
    </form>
    ```

    - **`<input type="hidden" name="password" value="12345678">`:** *Este campo oculto tiene un valor `12345678`, que es el valor que se enviará al servidor para cambiar la contraseña del usuario sin que este lo sepa.*
    - **`document.form.submit();`:** *Esto automáticamente envía el formulario tan pronto como la página cargue, redirigiendo al usuario y ejecutando el cambio de contraseña.*

**Efecto del Ataque:**

- *El servidor recibe la solicitud `POST` con el valor de la contraseña `12345678` gracias a las cookies que identifican al usuario. Como el usuario ya está autenticado, el servidor procesa la solicitud y cambia la contraseña sin que el usuario tenga que interactuar.*
- **Resultado final:** *El atacante cambia la contraseña del usuario sin que este se dé cuenta, aprovechándose de la autenticación automática mediante las cookies del navegador.*

### **Recursos Utilizados**

- **SQLite:** *[Documentación sobre SQLite](https://www.sqlite.org/docs.html "https://www.sqlite.org/docs.html")*
- **Seguridad con cookies HTTPOnly:** *[MDN Web Docs sobre Cookies](https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies "https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies")*

### **1. Desactivación de la Protección CSRF para una Ruta Específica**

*En tu código, estás desactivando la protección CSRF (Cross-Site Request Forgery) para una ruta específica de la aplicación. Esto se logra modificando el archivo `VerifyCsrfToken.php`.*

```php
<?php

namespace App\Http\Middleware;

use Illuminate\Foundation\Http\Middleware\VerifyCsrfToken as Middleware;

class VerifyCsrfToken extends Middleware
{
    /**
     * The URIs that should be excluded from CSRF verification.
     *
     * @var array<int, string>
     */
    protected $except = [
        "/contact",
        // "/change-password"
    ];
}
```

#### **Explicación**

- **`namespace App\Http\Middleware;`:** *Esta línea define el espacio de nombres para el archivo, especificando que el middleware está en la carpeta `Http/Middleware` de la aplicación Laravel.*
  
- **`use Illuminate\Foundation\Http\Middleware\VerifyCsrfToken as Middleware;`:** *Aquí estamos utilizando la clase `VerifyCsrfToken` proporcionada por Laravel, que maneja la verificación del token CSRF en las peticiones.*

- **`class VerifyCsrfToken extends Middleware`:** *Esto indica que estamos extendiendo la clase `VerifyCsrfToken` para personalizar el comportamiento de verificación de CSRF.*

- **`protected $except = [...]`:** *Este es el array donde puedes especificar las rutas que no deben ser verificadas por CSRF. Las rutas que agregues en este array estarán exentas de la verificación CSRF. En este caso, la ruta `/contact` está exenta, y comentaste `/change-password`, lo que significa que si lo descomentamos, esa ruta también quedaría exenta de CSRF.*

#### **¿Por qué no es lo más recomendable?**

*Aunque deshabilitar la protección CSRF para ciertas rutas puede ser necesario en algunos casos (por ejemplo, si la aplicación tiene una API que debe permitir solicitudes externas), **no es una práctica recomendada** debido a los riesgos de seguridad que puede implicar. CSRF es una medida de seguridad para prevenir que un atacante pueda hacer solicitudes no autorizadas en nombre de un usuario autenticado. Desactivarla en rutas críticas puede abrir puertas a ataques.*

### **2. Uso de CSRF Token en el Formulario**

#### **Uso manual de CSRF token en un formulario**

```html
<form method="POST" action="/change-password">
  <input type="hidden" name="_token" value="{{ csrf_token() }}">
</form>
```

- **Explicación**

- **`method="POST"`:** *Este atributo especifica que el formulario usará el método HTTP POST, lo cual es adecuado para enviar datos sensibles como una contraseña.*
  
- **`action="/change-password"`:** *Especifica la URL a la cual se enviarán los datos del formulario. En este caso, es la ruta `/change-password`, que está relacionada con el cambio de contraseña.*

- **`<input type="hidden" name="_token" value="{{ csrf_token() }}">`:** *Este campo oculto incluye el token CSRF.*
  - **`{{ csrf_token() }}`:** *Esta función de Laravel genera un token único que se envía con la solicitud POST. Este token se verifica en el servidor para asegurarse de que la solicitud provenga de una fuente legítima y no de un atacante. El servidor verifica que este token coincida con el que tiene registrado antes de procesar la solicitud.*
  
#### **¿Por qué es importante el CSRF Token?**

*El CSRF token ayuda a prevenir ataques de tipo CSRF, donde un atacante podría intentar enviar una solicitud en nombre de un usuario autenticado, sin que el usuario lo sepa.*

### **3. Hacer una Petición para Ver el Token CSRF**

*Usamos `curl` para hacer una petición GET al formulario de cambio de contraseña y luego filtramos el HTML para obtener el valor del `_token`.*

```bash
curl -sSLX GET http://172.17.0.2/change-password | grep -iEw "_token" | xargs
```

- **Explicación**

- **`curl -sSLX GET http://172.17.0.2/change-password`:** *Esta es una petición HTTP GET a la URL `/change-password`. Aquí usamos las siguientes opciones de `curl`:*
  - **`-s`:** *Silencia la salida de progreso de `curl`, solo mostrando la respuesta del servidor.*
  - **`-S`:** *Muestra los errores si ocurren.*
  - **`-L`:** *Sigue cualquier redirección que el servidor pueda hacer (por ejemplo, si la página redirige a otro recurso).*
  - **`-X GET`:** *Fuerza el método HTTP GET. Es redundante aquí, ya que `curl` usa GET por defecto.*

- **`grep -iEw "_token"`:** *Filtra la salida de `curl` para encontrar la palabra `_token`, que es el nombre del campo que contiene el token CSRF. El parámetro `-i` hace la búsqueda insensible a mayúsculas/minúsculas, y `-Ew` asegura que busque la palabra completa `_token`.*

- **`xargs`:** *Este comando toma la salida del comando anterior y la convierte en un argumento de comando, en este caso, mostrando el valor del `_token`.*

#### **Salida esperada**

```html
<input type=hidden name=_token value=CP8SH6ZDY6HxZzfg8iZfbUgET5TNgqkC4upalGBd>
```

*Este es el valor del token CSRF generado por Laravel para la ruta `/change-password`.*

### **4. Uso del `@csrf` Blade Directive**

*Laravel proporciona un método más simple para agregar el token CSRF a los formularios mediante su directiva Blade `@csrf`.*

```html
<form method="POST" action="/change-password">
  @csrf
```

- **Explicación**

- **`@csrf`:** *Esta directiva de Blade se encarga automáticamente de incluir el campo oculto con el token CSRF en el formulario. Es una forma más simple y menos propensa a errores que escribir el código manualmente, ya que Laravel se encarga de generar el token de manera automática.*

#### **Verificación con `curl`**

*Al ejecutar nuevamente el comando `curl`:*

```bash
curl -sSLX GET http://172.17.0.2/change-password | grep -iEw "_token" | xargs
```

*Obtendremos una salida similar, que contiene el nuevo valor del token CSRF:*

```html
<input type=hidden name=_token value=AUoT7YaCFAigUWujuNWN6Xc4XjvFZ1nDCJfV9T5p>
```

### **5. SameSite Cookies**

*A partir de los navegadores modernos, se ha implementado la política de **SameSite Cookies**. Esta es una medida de seguridad que ayuda a prevenir ataques CSRF al restringir el envío de cookies en peticiones cross-site (de un dominio a otro).*

- **SameSite=None:** *Permite que la cookie sea enviada en solicitudes cross-site, pero solo si también está marcada como `Secure` (requiere HTTPS).*
- **SameSite=Strict:** *La cookie solo se envía en solicitudes que provienen del mismo sitio, lo que significa que no se enviará en peticiones externas.*
- **SameSite=Lax:** *Permite que la cookie se envíe en algunas solicitudes cross-site, como las de navegación de primer nivel (por ejemplo, si un usuario hace clic en un enlace).*

#### **¿Cómo afecta esto a los ataques CSRF?**

*SameSite Cookies hace que los ataques CSRF sean más difíciles de llevar a cabo, ya que impide que el navegador envíe automáticamente las cookies en solicitudes de otros dominios, lo que protege las aplicaciones de ser vulnerables a este tipo de ataques.*

### **Recursos**

- **[SameSite Cookies en MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie/SameSite "https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie/SameSite")**
- **[Laravel CSRF Protection](https://laravel.com/docs/12.x/csrf "https://laravel.com/docs/12.x/csrf")**

> [!NOTE]
> *El término **"cross-site"** (en español "entre sitios") se refiere a cualquier acción que involucra recursos o solicitudes entre diferentes dominios o sitios web. En el contexto de seguridad y programación web, "cross-site" se utiliza principalmente para describir interacciones entre diferentes orígenes o dominios en la web.*

### **Ejemplos de Cross-Site**

1. **Cross-Site Request:** *Se refiere a una solicitud HTTP que un sitio web (A) hace a otro sitio web (B), es decir, el origen de la solicitud (dominio A) es diferente del origen del recurso solicitado (dominio B).*
   - **Ejemplo:** *Si tienes un sitio en `www.sitioA.com` y haces una solicitud a una API que está alojada en `api.sitioB.com`, esta es una solicitud **cross-site**.*

2. **Cross-Site Scripting (XSS):** *Este es un tipo de vulnerabilidad de seguridad donde un atacante puede inyectar scripts maliciosos en páginas web vistas por otros usuarios. En este ataque, el código malicioso se ejecuta en el navegador de la víctima, no en el servidor.*
   - **Ejemplo:** *Si un atacante inserta un script malicioso en un campo de entrada de una aplicación web, que luego se ejecuta cuando otros usuarios visitan la página afectada.*

3. **Cross-Site Request Forgery (CSRF):** *Este es otro tipo de ataque donde un atacante intenta hacer que un usuario autenticado envíe solicitudes no deseadas a un sitio web en el que el usuario está autenticado. El atacante aprovecha las cookies o sesiones de un usuario para realizar acciones en su nombre sin su consentimiento.*
   - **Ejemplo:** *Si un usuario está logueado en `www.sitioA.com` y un atacante les engaña para que hagan clic en un enlace que ejecuta una acción maliciosa en `www.sitioA.com`, como cambiar su contraseña, eso es un ataque **CSRF**.*

### **¿Por qué "cross-site" es importante en seguridad?**

> [!NOTE]
> *La razón por la que "cross-site" es un concepto tan relevante en seguridad es que los navegadores web, por defecto, restringen las interacciones entre sitios diferentes (cross-site), ya que permiten muchos de los ataques mencionados anteriormente (como XSS o CSRF). Para protegerse, los navegadores y las aplicaciones implementan políticas de seguridad como **SameSite Cookies** o **CORS (Cross-Origin Resource Sharing)**.*

### *Conceptos clave relacionados*

- **SameSite Cookies:** *Esta política de seguridad ayuda a prevenir ataques CSRF al no permitir que las cookies se envíen en solicitudes **cross-site** a menos que se configure explícitamente lo contrario. Esto hace que un sitio web no pueda enviar solicitudes automáticas en nombre de un usuario autenticado desde un dominio diferente.*

- **CORS (Cross-Origin Resource Sharing):** *Este es un mecanismo que permite o restringe que un sitio web haga peticiones a otro dominio (origen). Con CORS, los desarrolladores pueden configurar qué orígenes pueden interactuar con sus servidores, proporcionando más control sobre las solicitudes **cross-site**.*

### **Resumen**

*"Cross-site" se refiere a cualquier interacción entre sitios diferentes (dominios distintos). En seguridad web, se usa para describir vulnerabilidades y medidas de protección para evitar que un sitio web pueda realizar acciones no autorizadas en otro sitio web, como en los casos de XSS o CSRF.*
