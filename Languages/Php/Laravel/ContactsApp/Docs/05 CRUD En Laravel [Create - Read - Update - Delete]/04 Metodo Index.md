<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# *¿Qué es **user friendly** en programación?*

> [!NOTE]
> ***"User friendly"** significa que algo es **fácil de usar, entender o interactuar**, especialmente para personas que no son expertas en tecnología. En programación, puede referirse a:*

- *Interfaces intuitivas para el usuario (UI).*
- *Mensajes de error claros.*
- *Navegación sencilla.*
- *Automatización de tareas comunes.*

*En Laravel, por ejemplo, el comando `php artisan route:list` es una herramienta **user friendly** para que los desarrolladores vean todas las rutas activas de su app con claridad.*

---

## **Comando `php artisan route:list`**

### **Descripción**

*Este comando **muestra en consola una tabla con todas las rutas registradas en tu aplicación Laravel**, incluyendo:*

- *El método HTTP que usan (`GET`, `POST`, `PUT`, `DELETE`, etc.).*
- *La URI (parte final de la URL que accede el navegador).*
- *El **nombre de la ruta**, si tiene uno.*
- *El **controlador y método** que maneja esa ruta.*

---

### **Sintaxis general**

```bash
php artisan route:list [opciones]
```

---

## **Ejemplo real del comando**

```bash
php artisan route:list
```

**Esto genera una salida como:**

```bash
GET|HEAD  / ................................................................................................................................................................................ 
POST      _ignition/execute-solution ......................................................................... ignition.executeSolution › Spatie\LaravelIgnition › ExecuteSolutionController
GET|HEAD  _ignition/health-check ..................................................................................... ignition.healthCheck › Spatie\LaravelIgnition › HealthCheckController
POST      _ignition/update-config .................................................................................. ignition.updateConfig › Spatie\LaravelIgnition › UpdateConfigController
GET|HEAD  api/user ......................................................................................................................................................................... 
POST      contacts ................................................................................................................................ contacts.store › ContactController@store
GET|HEAD  contacts ................................................................................................................................ contacts.index › ContactController@index
GET|HEAD  contacts/create ....................................................................................................................... contacts.create › ContactController@create
PUT       contacts/{contact} .................................................................................................................... contacts.update › ContactController@update
DELETE    contacts/{contact} .................................................................................................................. contacts.destroy › ContactController@destroy
GET|HEAD  contacts/{contact} ........................................................................................................................ contacts.show › ContactController@show
GET|HEAD  contacts/{contact}/edit ................................................................................................................... contacts.edit › ContactController@edit
GET|HEAD  home .............................................................................................................................................. home › ContactController@index
GET|HEAD  login ................................................................................................................................. login › Auth\LoginController@showLoginForm
POST      login ................................................................................................................................................. Auth\LoginController@login
POST      logout ...................................................................................................................................... logout › Auth\LoginController@logout
GET|HEAD  password/confirm ............................................................................................... password.confirm › Auth\ConfirmPasswordController@showConfirmForm
POST      password/confirm .......................................................................................................................... Auth\ConfirmPasswordController@confirm
POST      password/email ................................................................................................. password.email › Auth\ForgotPasswordController@sendResetLinkEmail
GET|HEAD  password/reset .............................................................................................. password.request › Auth\ForgotPasswordController@showLinkRequestForm
POST      password/reset .............................................................................................................. password.update › Auth\ResetPasswordController@reset
GET|HEAD  password/reset/{token} ............................................................................................... password.reset › Auth\ResetPasswordController@showResetForm
GET|HEAD  register ................................................................................................................. register › Auth\RegisterController@showRegistrationForm
POST      register ........................................................................................................................................ Auth\RegisterController@register
GET|HEAD  sanctum/csrf-cookie .................................................................................................................. Laravel\Sanctum › CsrfCookieController@show

                                                                                                                                                                        Showing [25] routes
```

---

## **`Route::resource(...)` en Laravel**

### **¿Qué hace?**

*El helper `Route::resource()` **genera automáticamente** todas las rutas necesarias para manejar un recurso CRUD (Create, Read, Update, Delete) siguiendo las **convenciones RESTful** de Laravel.*

---

### **Sintaxis**

```php
Route::resource(name: "contacts", controller: ContactController::class);
```

*Esto equivale a **escribir manualmente** las siguientes rutas:*

| **Método** | **URI**                    | **Nombre**         | **Acción**                   |
| ---------- | -------------------------- | ------------------ | ---------------------------- |
| *GET*      | */contacts*                | *contacts.index*   | *ContactController\@index*   |
| *GET*      | */contacts/create*         | *contacts.create*  | *ContactController\@create*  |
| *POST*     | */contacts*                | *contacts.store*   | *ContactController\@store*   |
| *GET*      | */contacts/{contact}*      | *contacts.show*    | *ContactController\@show*    |
| *GET*      | */contacts/{contact}/edit* | *contacts.edit*    | *ContactController\@edit*    |
| *PUT*      | */contacts/{contact}*      | *contacts.update*  | *ContactController\@update*  |
| *DELETE*   | */contacts/{contact}*      | *contacts.destroy* | *ContactController\@destroy* |

**Laravel también acepta `PATCH` para `update`.**

---

### **Métodos que debes tener en tu controlador**

**Para que `Route::resource(...)` funcione correctamente, tu `ContactController` debe tener estos métodos:**

```php
// Mostrar todos los contactos
public function index() {

} 
// Formulario para crear contacto
public function create() {

} 
// Guardar contacto nuevo
public function store() {

} 
// Ver contacto específico
public function show($id) {

} 
// Formulario para editar
public function edit($id) {

} 
// Actualizar contacto
public function update($id)

// Eliminar contacto
public function destroy($id) {

}
```

---

## **Bonus: Otras rutas comunes que viste**

- ***login** y **logout** → vienen de `Auth::routes()` (autenticación generada automáticamente).*
- ***password/reset** y similares → relacionadas con recuperación de contraseñas.*
- ***sanctum/csrf-cookie** → utilizada para protección CSRF cuando se usa **Laravel Sanctum** con SPA (Single Page Apps).*

---

## **Conclusión resumida**

- *`php artisan route:list` te muestra todas las rutas activas de tu app con detalles.*
- *`Route::resource(...)` te ahorra escribir manualmente todas las rutas CRUD.*
- *Laravel sigue convenciones RESTful para organizar rutas y controladores.*
- *Puedes filtrar, ordenar y exportar rutas fácilmente usando opciones del comando.*
