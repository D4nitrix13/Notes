<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# **Métodos Edit & Update**

---

## **1. Comando: `lsd`**

**Descripción:**  
*`lsd` (LSDeluxe) es una versión moderna del comando `ls` escrita en Rust. Ofrece una mejor visualización en forma de árbol, íconos, y colores. Es ideal para navegar estructuras de directorios de forma más clara.*

---

### **Subcomando: `--tree`**

**Descripción:**  
*Este subcomando muestra los archivos y directorios en formato de árbol jerárquico.*

- **Opciones:**

- **`--color=never`:**
  *Desactiva los colores en la salida. Útil si se quiere una salida plana o se redirige a archivos.*

- **`--tree`:**
  *Muestra el contenido en forma de árbol (jerarquía de directorios).*

- **Valores:**

- **`./resources/views/`:**
  *Es la ruta del directorio que se quiere listar en formato de árbol. Puedes usar rutas relativas (`./`) o absolutas (`/home/usuario/`).*

---

- **Ejemplo práctico:**

```bash
lsd --color=never --tree ./resources/views/
```

**Explicación:**  
*Muestra la estructura completa de carpetas y archivos dentro del directorio `resources/views/` sin usar colores, utilizando una vista en forma de árbol.*

- **Salida**

```bash
 views
├──  auth
│   ├──  login.blade.php
│   ├──  passwords
│   │   ├──  confirm.blade.php
│   │   ├──  email.blade.php
│   │   └──  reset.blade.php
│   ├──  register.blade.php
│   └──  verify.blade.php
├──  change-password.blade.php
├──  contact.blade.php
├──  home.blade.php
├──  layouts
│   └──  app.blade.php
└──  welcome.blade.php
```

---

### **2. Comando: `mkdir`**

**Descripción:**  
*`mkdir` se usa para crear uno o más directorios en el sistema de archivos.*

---

#### **Subcomando:** *No Tiene Subcomandos Explícitos, Pero Puede Usarse Con Opciones.*

---

- **Opciones:**

- **`-p`:**
  *Crea directorios intermedios en la ruta si no existen. No lanza error si ya existen.*

- **`-v`:**
  *Muestra en pantalla los directorios creados.*

- **Valores:**

- **`resources/views/contacts`:**
  *Especifica la ruta completa del nuevo directorio. En este caso, crea la carpeta `contacts` dentro de `resources/views/`.*

- **Ejemplo práctico:**

```bash
mkdir -pv resources/views/contacts
```

**Explicación:**  
*Crea la carpeta `contacts` dentro de `resources/views/`, y muestra un mensaje indicando su creación. Si alguno de los directorios intermedios no existe, los crea automáticamente.*

---

### **3. Comando: `mv`**

**Descripción:**  
*`mv` se utiliza para mover o renombrar archivos y directorios.*

- **Opciones:**

*Sin opciones en este caso, pero se puede usar `-v` para ver los movimientos realizados.*

---

- **Valores:**

- **`resources/views/contact.blade.php`:**
  *Es la ruta del archivo que se desea mover.*

- **`resources/views/contacts/create.blade.php`:**
  *Es la nueva ubicación y nombre del archivo. Aquí se renombra a `create.blade.php` y se mueve al nuevo directorio `contacts`.*

---

- **Ejemplo práctico:**

```bash
mv resources/views/contact.blade.php resources/views/contacts/create.blade.php
```

**Explicación:**  
*Mueve el archivo `contact.blade.php` al nuevo directorio `contacts` y lo renombra como `create.blade.php`, siguiendo la convención de Laravel.*

---

### **[Convención de Laravel](https://laravel.com/docs/12.x/controllers#main-content "https://laravel.com/docs/12.x/controllers#main-content")**

*Laravel recomienda organizar las vistas de cada recurso siguiendo el nombre del modelo en plural y en minúsculas, como carpeta, y dentro colocar los archivos blade con los nombres de las acciones (`index.blade.php`, `create.blade.php`, `edit.blade.php`, etc.), alineados con los métodos del controlador:*

| **Verbo HTTP** | **URI**                      | **Acción**  | **Nombre de Ruta**   |
| -------------- | ---------------------------- | ----------- | -------------------- |
| *`GET`*        | *`/contacts`*                | *`index`*   | *`contacts.index`*   |
| *`GET`*        | *`/contacts/create`*         | *`create`*  | *`contacts.create`*  |
| *`POST`*       | *`/contacts`*                | *`store`*   | *`contacts.store`*   |
| *`GET`*        | *`/contacts/{contact}`*      | *`show`*    | *`contacts.show`*    |
| *`GET`*        | *`/contacts/{contact}/edit`* | *`edit`*    | *`contacts.edit`*    |
| *`PUT/PATCH`*  | *`/contacts/{contact}`*      | *`update`*  | *`contacts.update`*  |
| *`DELETE`*     | *`/contacts/{contact}`*      | *`destroy`* | *`contacts.destroy`* |

---

## **1. Modificación Del Método `create()` En El Controlador**

### **Archivo:** *`app/Http/Controllers/ContactController.php`*

#### **Fragmento De Código Actualizado**

```php
public function create()
{
    return view(view: "contacts.create");
}
```

---

### **Explicación Paso A Paso**

1. **Comando principal:** *`return view(...)`*
   - **Descripción:** *La función `view()` genera una respuesta de tipo vista en Laravel, cargando un archivo Blade (`.blade.php`) ubicado en el directorio `resources/views/`.*

2. **Subcomando:** *No aplica (es una función, no un comando con subcomandos).*

3. **Opciones:**
   - *`view:` es una **clave nombrada** que indica el nombre de la vista que Laravel debe buscar.*

4. **Valores:**
   - **`"contacts.create"`:**
    > [!NOTE]
    > *Laravel interpretará este string como `resources/views/contacts/create.blade.php`. El punto (`.`) indica subdirectorios. Por convención, Laravel usa puntos en lugar de `/`.*

---

### **Ejemplo práctico**

```php
return view(view: "contacts.create");
```

**Explicación:**
*Carga la vista ubicada en `resources/views/contacts/create.blade.php`.*

---

## **2. Modificación Del Archivo De Rutas**

### **Archivo:** *`routes/web.php`*

#### **Fragmento Agregado**

```php
Route::get(
    uri: "/contacts/{contact}/edit",
    action: [ContactController::class, "edit"]
)->name(name: "contacts.edit");
```

1. **Comando principal:** *`Route::get(...)`*
   - **Descripción:** *Define una ruta que responde a peticiones HTTP GET.*

2. **Subcomando:** *No aplica como subcomando en sí, pero `get` es una función específica para manejar GET.*

3. **Opciones y parámetros nombrados:**
   - *`uri:` Define el patrón de la URL que se escucha.*
     *Valor: `"/contacts/{contact}/edit"` significa que `{contact}` es un parámetro dinámico de la URI.*
   - *`action:` Define el controlador y método que manejarán la petición.*
     *Valor: `[ContactController::class, "edit"]`.*
   - *`name:` Define un nombre simbólico para esta ruta.*
     *Valor: `"contacts.edit"`, útil para generar URLs con `route("contacts.edit", $contact)`.*

- **Ejemplo práctico**

```php
Route::get(
    uri: "/contacts/{contact}/edit",
    action: [ContactController::class, "edit"]
)->name(name: "contacts.edit");
```

**Explicación:**
*Define una ruta que responde a `/contacts/1/edit` con el método `edit()` del `ContactController`, donde `1` es el identificador del contacto.*

---

## **3. Exploración del método `edit()`**

### **Versión A: Recepción directa del modelo**

```php
public function edit(Contact $contact)
{
    return view(view: "contacts.edit");
}
```

- *Laravel infiere automáticamente que el parámetro `{contact}` debe inyectar un modelo `Contact` con el ID `1` (por ejemplo).*
- *Esto se conoce como* **Route Model Binding.**

---

### **Versión B: Exploración didáctica usando `Request`**

```php
public function edit(Request $request)
{
    dd($request);
    return view(view: "contacts.edit");
}
```

- *Aquí se inspecciona el objeto `Request` completo con `dd()` (Dump and Die), útil para explorar su contenido.*

---

### **Versión C: Obtener el parámetro manualmente**

```php
public function edit()
{
    dd(request()->route(param: "contact"));
    return view(view: "contacts.edit");
}
```

- **`request()`:** *Helper global de Laravel para obtener la instancia actual de la petición.*
- **`->route("contact")`:** *Extrae el valor del parámetro `{contact}` definido en la URI.*
- *Esta versión demuestra que Laravel internamente está extrayendo ese valor.*

---

### *Versión D: Obtener el ID directamente como argumento*

```php
public function edit(int $contactId)
{
    dd($contactId);
    return view(view: "contacts.edit");
}
```

- *Laravel mapea el parámetro de la URL `{contact}` al parámetro del método `$contactId`, si no se usa route model binding.*
- *Muy útil si solo necesitas el ID y no el modelo completo.*

---

## **4. Prueba desde el navegador**

*Accede a esta URL:*

```bash
http://localhost:8000/contacts/1/edit
```

*Dependiendo de la versión del método `edit()`, se imprimirá:*

```bash
"1"
```

*En consola, por el uso de `dd()` en el controlador. Esto confirma que Laravel interpreta correctamente el parámetro `{contact}` como `1`.*

---

### **Comando Usado Para Consultar La Base De Datos**

```bash
docker container exec -it db psql -h localhost -U postgres -p 5432 -d contacts_app -c "SELECT * FROM contacts";
```

#### **1. Comando Principal: `docker`**

> [!NOTE]
> *Docker es una herramienta que permite crear, desplegar y ejecutar aplicaciones mediante contenedores. Es muy útil para encapsular entornos de desarrollo o producción.*

#### **2. Subcomando: `container exec`**

*Permite ejecutar un comando dentro de un contenedor en ejecución. Se usa cuando necesitas interactuar con el contenedor, como si estuvieras dentro de él.*

#### **3. Opciones:**

- *`-it`: Combina dos opciones:*
  - *`-i` (interactivo): Mantiene la entrada estándar (STDIN) abierta.*
  - *`-t` (tty): Asigna un pseudo-terminal para que el comando se ejecute como si fuera en una terminal real.*
- *`db`: Es el nombre del contenedor. Debes reemplazarlo por el nombre real de tu contenedor si es diferente.*
- *`psql`: Es el cliente de línea de comandos de PostgreSQL. Permite interactuar con bases de datos PostgreSQL.*
- *`-h localhost`: Define el host donde se encuentra la base de datos (en este caso, `localhost` dentro del contenedor).*
- *`-U postgres`: Especifica el usuario con el que te conectarás (aquí, el usuario es `postgres`).*
- *`-p 5432`: Especifica el puerto del servidor de PostgreSQL (5432 es el puerto por defecto).*
- *`-d contacts_app`: Indica el nombre de la base de datos a la que deseas conectarte.*
- *`-c "SELECT * FROM contacts;"`: Ejecuta el comando SQL directamente desde la línea de comandos.*

#### **4. Valores:**

- *`contacts`: Es el nombre de la tabla dentro de la base de datos `contacts_app`. El comando SQL selecciona todos los registros de esta tabla.*

#### **5. Ejemplo Práctico:**

```bash
docker container exec -it db psql -h localhost -U postgres -p 5432 -d contacts_app -c "SELECT * FROM contacts;"
```

**Explicación:** *Este comando ejecuta una consulta SQL dentro del contenedor `db` para obtener todos los registros de la tabla `contacts` en la base de datos `contacts_app`.*

---

### **Cambios en el archivo `ContactController.php` (método `edit`)**

```php
public function edit(Contact $contact)
{
    return view(view: "contacts.edit", data: compact(var_name: $contact));
}
```

#### **Explicación Técnica**

1. *Laravel hace **inyección automática de modelos** cuando el parámetro de la ruta (`{contact}`) coincide con una columna `id` del modelo `Contact`.*
2. *En lugar de extraer manualmente el parámetro de la URL (`request()->route('contact')`) o hacer una búsqueda con `Contact::findOrFail()`, Laravel automáticamente hace la búsqueda por ti si usas el tipo de dato `Contact` como parámetro.*
3. *El método `compact()` es un helper de PHP que genera un array asociativo. En este caso:*

   ```php
   compact(var_name: $contact)
   ```

   **Es equivalente a:**

   ```php
   ['contact' => $contact]
   ```

   *Lo cual es útil para enviar datos a la vista sin escribir manualmente las claves.*

---

### *Cambios en la vista `resources/views/contacts/edit.blade.php`*

```php
<form method="POST" action="{{ route(name: 'contacts.update', parameters: $contact->id) }}">
```

#### **Explicación**

- *`route()` es un helper de Laravel que genera la URL de una ruta nombrada.*
- *`name: 'contacts.update'`: Es el nombre de la ruta definida para actualizar un contacto.*
- *`parameters: $contact->id`: Es el parámetro que se pasa a la ruta, que corresponde al ID del contacto que se está editando.*

---

### ***Observación final***

*Cuando accediste a:*

```bash
http://172.17.0.2:8000/contacts/1/edit
```

*Y obtuviste un **404 Not Found**, fue porque el contacto con ID `1` no existía en la base de datos. En cambio, al acceder a:*

```bash
http://172.17.0.2:8000/contacts/3/edit
```

*Laravel encontró al contacto con ID `3` y lo pasó correctamente al método `edit`, gracias al route model binding.*

---

### **Definición formal:**

*Un **helper** (o función auxiliar) en Laravel (y en PHP en general) es una función accesible globalmente cuyo propósito es **facilitar tareas repetitivas o comunes**, como generar URLs, acceder al entorno, manipular arreglos, trabajar con rutas, vistas, strings, y más.*

---

### **Características de los helpers:**

- *Están disponibles en cualquier parte del proyecto (controladores, vistas, middlewares, etc.).*
- *No requieren instanciar clases.*
- *Ayudan a escribir código más limpio y legible.*
- *Laravel ya incluye muchos helpers por defecto, pero puedes crear los tuyos personalizados.*

---

### **Ejemplos comunes de helpers en Laravel:**

| **Helper**    | **Descripción**                                                            |
| ------------- | -------------------------------------------------------------------------- |
| *`route()`*   | *Genera la URL de una ruta con nombre.*                                    |
| *`view()`*    | *Retorna una vista (blade).*                                               |
| *`asset()`*   | *Retorna la URL de un recurso público (como CSS o JS).*                    |
| *`env()`*     | *Obtiene valores del archivo `.env`.*                                      |
| *`config()`*  | *Obtiene o establece valores de configuración.*                            |
| *`old()`*     | *Recupera el valor de un campo del formulario después de una redirección.* |
| *`now()`*     | *Retorna la fecha y hora actual como una instancia de Carbon.*             |
| *`auth()`*    | *Retorna la instancia del usuario autenticado.*                            |
| *`compact()`* | *Crea un array asociativo a partir de variables.*                          |

---

### **Ejemplo práctico:**

#### **Usar `view()` con `compact()`**

```php
public function show()
{
    $name = "Daniel Benjamin Perez Morales";
    return view(view: "welcome", data: compact(var_name: "name"));
}
```

**Explicación:**

- *`view()` genera y retorna la vista `resources/views/welcome.blade.php`.*
- *`compact("name")` convierte la variable `$name` en un array asociativo `["name" => "Daniel Benjamin Perez Morales"]`, y se lo pasa a la vista.*

---

- **Comando Usado Para Consultar La Base De Datos**

```bash
docker container exec -it db psql -h localhost -U postgres -p 5432 -d contacts_app -c "SELECT * FROM contacts";
```

- **1. Comando Principal: `docker`**

> [!NOTE]
> *Docker es una herramienta que permite crear, desplegar y ejecutar aplicaciones mediante contenedores. Es muy útil para encapsular entornos de desarrollo o producción.*

- **2. Subcomando: `container exec`**

*Permite ejecutar un comando dentro de un contenedor en ejecución. Se usa cuando necesitas interactuar con el contenedor, como si estuvieras dentro de él.*

- **3. Opciones:**

- *`-it`: Combina dos opciones:*
  - *`-i` (interactivo): Mantiene la entrada estándar (STDIN) abierta.*
  - *`-t` (tty): Asigna un pseudo-terminal para que el comando se ejecute como si fuera en una terminal real.*
- *`db`: Es el nombre del contenedor. Debes reemplazarlo por el nombre real de tu contenedor si es diferente.*
- *`psql`: Es el cliente de línea de comandos de PostgreSQL. Permite interactuar con bases de datos PostgreSQL.*
- *`-h localhost`: Define el host donde se encuentra la base de datos (en este caso, `localhost` dentro del contenedor).*
- *`-U postgres`: Especifica el usuario con el que te conectarás (aquí, el usuario es `postgres`).*
- *`-p 5432`: Especifica el puerto del servidor de PostgreSQL (5432 es el puerto por defecto).*
- *`-d contacts_app`: Indica el nombre de la base de datos a la que deseas conectarte.*
- *`-c "SELECT * FROM contacts;"`: Ejecuta el comando SQL directamente desde la línea de comandos.*

- **4. Valores:**

- *`contacts`: Es el nombre de la tabla dentro de la base de datos `contacts_app`. El comando SQL selecciona todos los registros de esta tabla.*

- **5. Ejemplo Práctico:**

```bash
docker container exec -it db psql -h localhost -U postgres -p 5432 -d contacts_app -c "SELECT * FROM contacts;"
```

**Explicación:** *Este comando ejecuta una consulta SQL dentro del contenedor `db` para obtener todos los registros de la tabla `contacts` en la base de datos `contacts_app`.*

- **Cambios en el archivo `ContactController.php` (método `edit`)**

```php
public function edit(Contact $contact)
{
    return view(view: "contacts.edit", data: compact(var_name: $contact));
}
```

- **Explicación Técnica**

1. *Laravel hace **inyección automática de modelos** cuando el parámetro de la ruta (`{contact}`) coincide con una columna `id` del modelo `Contact`.*
2. *En lugar de extraer manualmente el parámetro de la URL (`request()->route('contact')`) o hacer una búsqueda con `Contact::findOrFail()`, Laravel automáticamente hace la búsqueda por ti si usas el tipo de dato `Contact` como parámetro.*
3. *El método `compact()` es un helper de PHP que genera un array asociativo. En este caso:*

   ```php
   compact(var_name: $contact)
   ```

   **Es equivalente a:**

   ```php
   ['contact' => $contact]
   ```

   *Lo cual es útil para enviar datos a la vista sin escribir manualmente las claves.*

- *Cambios en la vista `resources/views/contacts/edit.blade.php`*

```php
<form method="POST" action="{{ route(name: 'contacts.update', parameters: $contact->id) }}">
```

- **Explicación**

- *`route()` es un helper de Laravel que genera la URL de una ruta nombrada.*
- *`name: 'contacts.update'`: Es el nombre de la ruta definida para actualizar un contacto.*
- *`parameters: $contact->id`: Es el parámetro que se pasa a la ruta, que corresponde al ID del contacto que se está editando.*

- ***Observación final***

*Cuando accediste a:*

```bash
http://172.17.0.2:8000/contacts/1/edit
```

*Y obtuviste un **404 Not Found**, fue porque el contacto con ID `1` no existía en la base de datos. En cambio, al acceder a:*

```bash
http://172.17.0.2:8000/contacts/3/edit
```

*Laravel encontró al contacto con ID `3` y lo pasó correctamente al método `edit`, gracias al route model binding.*

- **Definición formal:**

*Un **helper** (o función auxiliar) en Laravel (y en PHP en general) es una función accesible globalmente cuyo propósito es **facilitar tareas repetitivas o comunes**, como generar URLs, acceder al entorno, manipular arreglos, trabajar con rutas, vistas, strings, y más.*

- **Características de los helpers:**

- *Están disponibles en cualquier parte del proyecto (controladores, vistas, middlewares, etc.).*
- *No requieren instanciar clases.*
- *Ayudan a escribir código más limpio y legible.*
- *Laravel ya incluye muchos helpers por defecto, pero puedes crear los tuyos personalizados.*

- **Ejemplos comunes de helpers en Laravel:**

| **Helper**    | **Descripción**                                                            |
| ------------- | -------------------------------------------------------------------------- |
| *`route()`*   | *Genera la URL de una ruta con nombre.*                                    |
| *`view()`*    | *Retorna una vista (blade).*                                               |
| *`asset()`*   | *Retorna la URL de un recurso público (como CSS o JS).*                    |
| *`env()`*     | *Obtiene valores del archivo `.env`.*                                      |
| *`config()`*  | *Obtiene o establece valores de configuración.*                            |
| *`old()`*     | *Recupera el valor de un campo del formulario después de una redirección.* |
| *`now()`*     | *Retorna la fecha y hora actual como una instancia de Carbon.*             |
| *`auth()`*    | *Retorna la instancia del usuario autenticado.*                            |
| *`compact()`* | *Crea un array asociativo a partir de variables.*                          |

- **Ejemplo práctico:**

- **Usar `view()` con `compact()`**

```php
public function show()
{
    $name = "Daniel Benjamin Perez Morales";
    return view(view: "welcome", data: compact(var_name: "name"));
}
```

**Explicación:**

- *`view()` genera y retorna la vista `resources/views/welcome.blade.php`.*
- *`compact("name")` convierte la variable `$name` en un array asociativo `["name" => "Daniel Benjamin Perez Morales"]`, y se lo pasa a la vista.*

---

- **Definición formal:**

- *La **inyección automática de modelos** (model binding) es un mecanismo por el cual Laravel **resuelve automáticamente los modelos a partir de los parámetros de la ruta** y los pasa al método correspondiente del controlador.*

---

### **Ventajas:**

- *Te ahorras escribir `Model::find($id)` o `Model::findOrFail($id)`.*
- *Laravel devuelve un error 404 automáticamente si no se encuentra el modelo.*
- *Código más limpio y expresivo.*
- *Funciona tanto en controladores como en closures de rutas.*

---

### **Requisitos:**

1. *La ruta debe incluir un parámetro que coincida con el nombre del modelo (por convención).*
2. *El modelo debe estar **tipado explícitamente** en el método del controlador.*
3. *El parámetro de la ruta debe ser **una clave primaria o un campo con una clave única**.*

---

### **Ejemplo básico:**

#### **`routes/web.php`**

```php
Route::get('/contacts/{contact}/edit', [ContactController::class, 'edit']);
```

#### **`app/Http/Controllers/ContactController.php`**

```php
use App\Models\Contact;

public function edit(Contact $contact)
{
    // Laravel busca automáticamente el contacto cuyo id coincida con {contact}
    return view(view: "contacts.edit", data: compact(var_name: "contact"));
}
```

---

### **¿Qué hace Laravel por ti aquí?**

*Supongamos que el navegador accede a:*

```bash
http://localhost:8000/contacts/3/edit
```

*Laravel internamente ejecuta algo como:*

```php
$contact = Contact::findOrFail(3);
```

*Y pasa ese objeto `$contact` directamente al método `edit()`.*

---

### **Si no se encuentra el registro:**

*Laravel automáticamente lanza una excepción `ModelNotFoundException` y retorna un error 404, sin que tú lo tengas que programar.*

---

### **También puedes usar claves diferentes del ID:**

#### *Si tu modelo usa una clave diferente (por ejemplo un `slug`)*

```php
Route::get('/posts/{post:slug}', [PostController::class, 'show']);
```

*Esto le dice a Laravel: “Busca el post cuyo campo `slug` sea igual al valor en la URL.”*

---

### **Equivalente sin inyección automática:**

```php
public function edit($id)
{
    $contact = Contact::findOrFail($id);
    return view(view: "contacts.edit", data: compact(var_name: "contact"));
}
```

---

## **1. Comando Principal:** `Route::get`

```php
Route::get(
    uri: "/contacts/{contact:email}/edit",
    action: [ContactController::class, "edit"]
)->name(name: "contacts.edit");
```

**Descripción:**  
*El método `Route::get` en Laravel define una **ruta que responde a solicitudes HTTP de tipo GET**. Su propósito principal es mostrar datos, como páginas, formularios o vistas.*

---

## **2. Subcomando O Estructura De Parámetros Del Comando:**

```php
Route::get(uri: "/contacts/{contact}/edit", action: [ContactController::class, "edit"])
```

**Subcomponentes explicados:**

- *`uri`: Especifica la **URL** a la que responde esta ruta.*
- *`"/contacts/{contact}/edit"`: Esta es una URL con un parámetro dinámico llamado `{contact}`. Laravel interpretará ese valor como el identificador de un recurso (por defecto, `id`).*
- *`action`: Define qué **controlador y método** se ejecutan cuando se accede a la ruta. En este caso, se llama al método `edit` del `ContactController`.*

- **3. Opciones:**

*Laravel permite una variante del nombre del parámetro, usando `:` para indicar una **clave alternativa** diferente del `id`. Por ejemplo:*

```php
{contact:email}     // Usa el campo "email" para hacer la búsqueda
{contact:phone_number} // Usa el campo "phone_number"
```

- *Usa el campo "phone_number"*

```php
Route::get(
    uri: "/contacts/{contact:phone_number}/edit",
    action: [ContactController::class, "edit"]
)->name(name: "contacts.edit");
```

- *Usa el campo "email"*

```php
Route::get(
    uri: "/contacts/{contact:email}/edit",
    action: [ContactController::class, "edit"]
)->name(name: "contacts.edit");
```

*Esto se denomina **Route Model Binding personalizado**.*

- **4. Valores:**

- *`{contact}`: Laravel buscará en la base de datos el modelo `Contact` cuyo campo `id` sea igual al valor recibido.*
- *`{contact:email}`: Laravel buscará el modelo `Contact` cuyo campo `email` coincida con el valor recibido.*
- *`{contact:phone_number}`: Buscará por el campo `phone_number`.*

> *Laravel Asume Automáticamente El Modelo Correcto (`Contact`) Si El Nombre Del Parámetro Coincide Con El Nombre De La Clase En Minúscula Y Singular (`Contact`).*

---

## **5. Ejemplo práctico: búsqueda por ID (por defecto)**

```php
Route::get(
    uri: "/contacts/{contact}/edit",
    action: [ContactController::class, "edit"]
)->name(name: "contacts.edit");
```

**Explicación:**

- *Esta ruta captura una URL como `/contacts/3/edit`*
- *Laravel busca `Contact::findOrFail(3)`*
- *Si el contacto existe, lo pasa al método `edit(Contact $contact)`*
- *Si no existe, retorna un error 404 automáticamente*

---

## **5.1 Ejemplo práctico: búsqueda por email**

```php
Route::get(
    uri: "/contacts/{contact:email}/edit",
    action: [ContactController::class, "edit"]
)->name(name: "contacts.edit");
```

**Explicación:**

- *Esta ruta captura una URL como `/contacts/messi@gmail.com/edit`*
- *Laravel buscará `Contact::where('email', 'messi@gmail.com')->firstOrFail()`*
- *Se pasa ese modelo al controlador*

---

## **5.2 Ejemplo práctico: búsqueda por número de teléfono**

```php
Route::get(
    uri: "/contacts/{contact:phone_number}/edit",
    action: [ContactController::class, "edit"]
)->name(name: "contacts.edit");
```

**Explicación:**

- *Se accede con una URL como `/contacts/123456789/edit`*
- *Laravel hace: `Contact::where('phone_number', '123456789')->firstOrFail()`*

---

## **6. Estructura del controlador:**

```php
use App\Models\Contact;

public function edit(Contact $contact)
{
    return view(view: "contacts.edit", data: compact("contact"));
}
```

**Explicación:**

- *Laravel **inyecta automáticamente el modelo** `Contact` usando la clave especificada en la ruta.*
- *Se pasa directamente a la vista `contacts.edit`.*

---

## **7. Estructura de la tabla `contacts`**

*Laravel busca los valores en los campos de esta tabla definida en la migración:*

*File `database/migrations/2025_03_22_030026_create_contacts_table.php`*

```php
<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        Schema::create('contacts', function (Blueprint $table) {
            $table->id();
            $table->string(column: "name");
            $table->string(column: "phone_number");
            $table->string(column: "email");

            // Definición de un campo de tipo tinyInteger sin signo (edad)
            // Es equivalente a: $table->tinyInteger("age", false, true);
            $table->tinyInteger("age", unsigned: true); // Disponible en PHP 8 en adelante
            // Explicación detallada sobre tinyInteger:
            // - Un `tinyInteger` almacena valores enteros pequeños (-128 a 127 o 0 a 255 si es unsigned)
            // - Ocupa solo 1 byte de espacio en la base de datos, optimizando almacenamiento y rendimiento
            // - Se diferencia de `integer` que ocupa 4 bytes y permite un rango mucho mayor
            // - Se usa para valores pequeños como edades, contadores de intentos, estatus de un campo, etc.
            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     *
     * @return void
     */
    public function down()
    {
        Schema::dropIfExists('contacts');
    }
};
```

- **Importante**

```php
$table->id();                        // clave primaria por defecto
$table->string("phone_number");     // clave personalizada posible
$table->string("email");            // clave personalizada posible
```

*En PostgreSQL (via `psql`), la tabla se ve así:*

```bash
docker container exec -it db psql -h localhost -U postgres -p 5432 -d contacts_app -c "\d contacts";
```

- **Salida**

```bash
                                           Table "public.contacts"
    Column    |              Type              | Collation | Nullable |               Default                
--------------+--------------------------------+-----------+----------+--------------------------------------
 id           | bigint                         |           | not null | nextval('contacts_id_seq'::regclass)
 name         | character varying(255)         |           | not null | 
 phone_number | character varying(255)         |           | not null | 
 email        | character varying(255)         |           | not null | 
 age          | smallint                       |           | not null | 
 created_at   | timestamp(0) without time zone |           |          | 
 updated_at   | timestamp(0) without time zone |           |          | 
Indexes:
    "contacts_pkey" PRIMARY KEY, btree (id)
```

---

## **8. Verificación Desde Postgresql (Ver Los Datos Existentes):**

```bash
docker container exec -it db psql -h localhost -U postgres -p 5432 -d contacts_app -c "SELECT * FROM contacts";
```

**Salida:**

```bash
 id |       name         | phone_number |       email       | age 
----+--------------------+--------------+-------------------+-----
  3 | Cristiano Ronaldo  | 123456789    | ronaldo@gmail.com |  44
```

---

## **9. Ver el SQL directamente:**

```bash
docker container exec -it db pg_dump -U postgres -d contacts_app -t contacts --schema-only | grep -iEw "create table" -A 8 --color=never
```

*Resultado:*

```sql
CREATE TABLE public.contacts (
    id bigint NOT NULL,
    name character varying(255) NOT NULL,
    phone_number character varying(255) NOT NULL,
    email character varying(255) NOT NULL,
    age smallint NOT NULL,
    created_at timestamp(0) without time zone,
    updated_at timestamp(0) without time zone
);
```

---

## **Conclusión:**

**Cuando defines una ruta como:**

```php
/contacts/{contact}/edit
```

*Laravel **automáticamente buscará el modelo `Contact` por su ID**.*
**Pero si defines:**

```php
/contacts/{contact:email}/edit
```

*Laravel buscará por el campo `email`.*
*Esta es la **inyección automática de modelos con claves personalizadas**, y permite rutas semánticas y controladores mucho más limpios.*

---

### **1. Comando principal:**

- **Inyección de dependencias en Laravel**

**Descripción:**
*La inyección de dependencias es un patrón de diseño que permite a Laravel "inyectar" automáticamente objetos que necesita un método o clase, sin que tú los crees manualmente. Laravel resuelve estos objetos a través del **Service Container** (contenedor de servicios), que administra instancias y dependencias.*

```php
public function edit(Contact $contact, Request $request)
    {
        dd($contact, $request)
        // public function edit(int $contactId)
        // dd(request()->route(param: "contact"));
        // dd($contactId);
        // $contact = Contact::findOrFail($contactId);

        return view(view: "contacts.edit", data: compact(var_name: "contact"));
    }
```

---

### **2. Subcomando (Contexto de uso):**

- **Método de controlador con parámetros tipados**

*Laravel permite declarar parámetros en métodos de controladores y automáticamente los resuelve:*

```php
public function edit(Contact $contact, Request $request)
```

**Significado:**

- *Laravel identificará que necesita una instancia del modelo `Contact` y un objeto `Request`.*
- *A partir de la ruta, buscará un `Contact` cuyo identificador coincida (por defecto con `id`, o con otro campo si se especifica).*

---

### **3. Opciones (Tipos de dependencias que se pueden inyectar):**

| *Tipo*                     | *Descripción*                                                                              |
| -------------------------- | ------------------------------------------------------------------------------------------ |
| *Modelos Eloquent*         | *Laravel usa **Route Model Binding** para resolver automáticamente instancias del modelo.* |
| *Objetos de Request*       | *Laravel inyecta el objeto `Illuminate\Http\Request` con todos los datos de la petición.*  |
| *Servicios personalizados* | *Cualquier clase registrada en el contenedor de servicios puede inyectarse.*               |

---

### **4. Valores (Cómo Laravel interpreta los valores):**

#### **a) Route Model Binding por defecto:**

```php
Route::get('/contacts/{contact}/edit', [ContactController::class, 'edit']);
```

- **Valor:** *`{contact}` → Laravel busca un `Contact` por el campo `id` (por defecto).*
- **Resultado:** *Se inyecta automáticamente el modelo `Contact` correspondiente.*

#### **b) Route Model Binding personalizado:**

```php
Route::get('/contacts/{contact:email}/edit', [ContactController::class, 'edit']);
```

- **Valor:** *`{contact:email}` → Laravel busca un `Contact` cuyo `email` coincida con el valor en la URL.*

---

### **5. Ejemplo práctico:**

#### **a) Ruta definida en `web.php`:**

```php
Route::get(
    uri: '/contacts/{contact}/edit',
    action: [ContactController::class, 'edit']
)->name(name: 'contacts.edit');
```

#### **b) Método del controlador `app/Http/Controllers/ContactController.php`:**

```php
public function edit(Contact $contact, Request $request)
{
    dd($contact, $request); // Muestra el modelo Contact y el objeto Request

    return view(view: 'contacts.edit', data: compact('contact'));
}
```

#### **c) Resultado en navegador:**

**Si se accede a:**

```bash
http://localhost:8000/contacts/3/edit
```

**Laravel hace lo siguiente:**

- *Busca el `Contact` con `id = 3` en la base de datos.*
- *Inyecta el modelo `$contact` y el objeto `$request`.*
- *Devuelve la vista `contacts.edit` con los datos del contacto.*

```bash
App\Models\Contact {#658 ▼ // app/Http/Controllers/ContactController.php:130
  #connection: "pgsql"
  #table: "contacts"
  #primaryKey: "id"
  #keyType: "int"
  +incrementing: true
  #with: []
  #withCount: []
  +preventsLazyLoading: false
  #perPage: 15
  +exists: true
  +wasRecentlyCreated: false
  #escapeWhenCastingToString: false
  #attributes: array:7 [▶]
  #original: array:7 [▶]
  #changes: []
  #casts: []
  #classCastCache: []
  #attributeCastCache: []
  #dates: []
  #dateFormat: null
  #appends: []
  #dispatchesEvents: []
  #observables: []
  #relations: []
  #touches: []
  +timestamps: true
  #hidden: []
  #visible: []
  #fillable: array:4 [▶]
  #guarded: array:1 [▶]
}

Illuminate\Http\Request {#44 ▼ // app/Http/Controllers/ContactController.php:130
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
  #pathInfo: "/contacts/3/edit"
  #requestUri: "/contacts/3/edit"
  #baseUrl: ""
  #basePath: null
  #method: "GET"
  #format: null
  #session: Illuminate\Session\Store {#294 ▶}
  #locale: null
  #defaultLocale: "en"
  -preferredFormat: null
  -isHostValid: true
  -isForwardedValid: true
  #json: null
  #convertedFiles: null
  #userResolver: Closure($guard = null) {#251 ▶}
  #routeResolver: Closure() {#260 ▶}
  basePath: ""
  format: "html"
}
```

---

### **Nota adicional: "Viejos valores" y `??` en Blade**

*En los formularios de edición, se utiliza la función `old()` de Laravel para preservar los datos anteriores si hubo errores de validación.*

```php
<input id="name" type="text" class="form-control @error('name') is-invalid @enderror" required value="{{ old('name') ?? $contact->name }}" name="name" autocomplete="name" autofocus>
<input id="phone_number" type="tel" class="form-control @error('phone_number') is-invalid @enderror" required value="{{ old('phone_number') ?? $contact->phone_number }}" name="phone_number" autocomplete="phone_number">
<input id="email" type="text" class="form-control @error('email') is-invalid @enderror" required value="{{ old('email') ?? $contact->email }}" name="email" autocomplete="email">
<input id="age" type="text" class="form-control @error('age') is-invalid @enderror" required value="{{ old('age') ?? $contact->age }}" name="age" autocomplete="age">
```

- **old('name'):** *Si el formulario falló, se muestra el valor anterior enviado por el usuario.*
- **$contact->name:** *Si no hay error, se muestra el valor actual del modelo.*

---

### **Problema HTML: métodos PUT, PATCH, DELETE**

> [!IMPORTANT]
> *HTML **no admite métodos PUT o DELETE**. Laravel lo soluciona con una directiva especial:*

```php
<form method="POST" action="{{ route(name: 'contacts.update', parameters: $contact->id ) }}">
    {{-- <input type="hidden" name="_token" value="{{ csrf_token() }}"> --}}
    @csrf
    @method("PUT")
```

**Esto simula una petición `PUT`, útil para actualizaciones.**

---

### **Método `update()` en `ContactController.php`**

```php
public function update(Request $request, Contact $contact)
{
    $data = $request->validate([
        "name" => "required",
        "phone_number" => "required|digits:9",
        "email" => "required|email",
        "age" => "required|numeric|min:1|max:255"
    ]);

    $contact->update($data);
    return redirect()->route(route: 'home');
}
```

- *Laravel valida los datos.*
- *Si son correctos, actualiza el contacto con `$contact->update($data)`.*
- *Redirige a la ruta `home`.*

---

### **Verificación con PostgreSQL**

```bash
docker container exec -it db psql -h localhost -U postgres -p 5432 -d contacts_app -c "select * from contacts";
```

**Salida esperada:**

```bash
 id |       name        | phone_number |       email       | age |     created_at      |     updated_at
----+-------------------+--------------+-------------------+-----+---------------------+---------------------
  3 | Cristiano Ronaldo | 123456789    | ronaldo@gmail.com |  44 | 2025-04-20 20:25:59 | 2025-04-20 21:30:04
```
