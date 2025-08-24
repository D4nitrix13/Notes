# **Middlewares y protección de rutas**

*[Checking Subscription Status](https://laravel.com/docs/12.x/cashier-paddle#checking-subscription-status "https://laravel.com/docs/12.x/cashier-paddle#checking-subscription-status")*

## **Definición de Middleware**

* *Un **middleware** es un componente intermedio en una aplicación o sistema que se ejecuta entre la **solicitud (request)** del usuario y la **respuesta (response)** del servidor.*
* *Su función principal es **interceptar, procesar o modificar** la comunicación para aplicar reglas, seguridad, validaciones o transformaciones antes de que la solicitud llegue al núcleo de la aplicación o la respuesta vuelva al cliente.*

**En pocas palabras:**
*Es como un **“filtro”** o **“puente”** que se ejecuta antes o después de la lógica principal.*

---

## *Características principales de un Middleware*

1. **Intermediario**

   * *Se ubica entre el cliente y la aplicación/servidor.*
   * *Procesa las peticiones entrantes y las respuestas salientes.*

2. **Modular y reutilizable**

   * *Se pueden encadenar varios middleware.*
   * *Cada uno cumple una tarea específica (ej. autenticación, logging, CORS, encriptación).*

3. **Transparente**

   * *El cliente no percibe directamente el middleware, solo recibe la respuesta procesada.*

4. **Personalizable**

   * *Los desarrolladores pueden crear middleware propios para necesidades específicas.*

5. **Ejecuta lógica transversal**

   * *Maneja aspectos que se repiten en muchas partes del sistema: seguridad, validación de datos, sesiones, compresión, cacheo, etc.*

6. **Independiente de la lógica de negocio**

   * *No altera la funcionalidad principal de la aplicación, solo controla el flujo antes o después.*

---

## **Ejemplos comunes de Middleware**

* **Autenticación y autorización** *→ verificar si el usuario tiene acceso.*
* **Gestión de sesiones** *→ mantener la sesión activa del usuario.*
* **Registro de logs** *→ almacenar información de cada request.*
* **Protección CSRF / CORS** *→ seguridad en peticiones HTTP.*
* **Compresión y encriptación** *→ mejorar rendimiento y proteger datos.*

> [!NOTE]
> **Si no estamos autenticados, ni siquiera deberíamos poder acceder a este lugar.”**

*Esto se refiere a que cualquier acceso a rutas sensibles (como `/contacts/`) debe estar protegido mediante middleware como `auth`, para que solo usuarios autenticados puedan acceder.*

---

## **Prueba con `curl`**

*Se ejecutó el siguiente comando:*

```bash
curl -sSX GET 'http://172.17.0.2:8000/contacts/' \
  -H 'Cookie: XSRF-TOKEN=eyJpdiI6IklFRXhjT1dKVDVUOTdleGNsNE9ad0E9PSIsInZhbHVlIjoidjgvMUF5enVBYnFBWG83emVGQnJ3T0RjZWU3amxlNmNScHFnVHdSZTNkbkpBNHk2UWZXRVVEV2s5TC83eXFtcGtqUnhOYXZ2U0w2N1dTK2ZBa3ZDSmkwc3Vib1daa1FOOWlmMGV5OC9yZ1NVNE5xekJLZ0hIckhEZkF6QVZuT3IiLCJtYWMiOiI0ZGU5YmQ2OTliMjkyNDQyOWQxMjRkMWY1OGRhOTBkYzQ1OGY2NDk4YThiOTBhMWUxMGRhYTM1YTQyNTEyMjE5IiwidGFnIjoiIn0%3D; contacts_app_session=eyJpdiI6IlpBMGVhQWd5YThtZGYySmVUUU9weFE9PSIsInZhbHVlIjoiMkNNYklwWlBQa0JwOWNTUXlldkhJRW1hcDFjZ3I1eGtGMU9aSDArRjk2TDZrTytjaW9aKzFrM29RU2hSdWNZYjVjcVp6NFJKK2taa2ROeHF4VW90TlYyV0JtRjEzTmNGeXk4SGlhT2pLOGZrTkpyNUlzNHZCRVBBdmx6cWVjR1IiLCJtYWMiOiIxN2JlMTc1YjliM2EzMjBiYWUzZDRjODEyMTMzYWM3MGJiYWNlNzYwZjNlMDg2OGJkODE0MjRkODJlNjY5M2MxIiwidGFnIjoiIn0%3D' | html2text
```

*Este comando intenta simular una petición HTTP GET a la ruta `/contacts/` incluyendo cookies de sesión y token CSRF.*

---

## **Resultado del comando**

```bash
  Error: Call to a member function contacts() on null in file /App/ApplicationLaravel/app/Http/Controllers/ContactController.php on line 54

    #0 /App/ApplicationLaravel/vendor/laravel/framework/src/Illuminate/Routing/Controller.php(54): App\Http\Controllers\ContactController->index()
    #1 /App/ApplicationLaravel/vendor/laravel/framework/src/Illuminate/Routing/ControllerDispatcher.php(43): Illuminate\Routing\Controller->callAction('index', Array)
    #2 /App/ApplicationLaravel/vendor/laravel/framework/src/Illuminate/Routing/Route.php(259): Illuminate\Routing\ControllerDispatcher->dispatch(Object(Illuminate\Routing\Route), Object(App\Http\Controllers\ContactController), 'index')
    #3 /App/ApplicationLaravel/vendor/laravel/framework/src/Illuminate/Routing/Route.php(205): Illuminate\Routing\Route->runController()
    #4 /App/ApplicationLaravel/vendor/laravel/framework/src/Illuminate/Routing/Router.php(798): Illuminate\Routing\Route->run()
    #5 /App/ApplicationLaravel/vendor/laravel/framework/src/Illuminate/Pipeline/Pipeline.php(141): Illuminate\Routing\Router->Illuminate\Routing\{closure}(Object(Illuminate\Http\Request))
    #6 /App/ApplicationLaravel/vendor/laravel/framework/src/Illuminate/Routing/Middleware/SubstituteBindings.php(50): Illuminate\Pipeline\Pipeline->Illuminate\Pipeline\{closure}(Object(Illuminate\Http\Request))
    #7 /App/ApplicationLaravel/vendor/laravel/framework/src/Illuminate/Pipeline/Pipeline.php(180): Illuminate\Routing\Middleware\SubstituteBindings->handle(Object(Illuminate\Http\Request), Object(Closure))
    #8 /App/ApplicationLaravel/vendor/laravel/framework/src/Illuminate/Foundation/Http/Middleware/VerifyCsrfToken.php(78): Illuminate\Pipeline\Pipeline->Illuminate\Pipeline\{closure}(Object(Illuminate\Http\Request))
    #9 /App/ApplicationLaravel/vendor/laravel/framework/src/Illuminate/Pipeline/Pipeline.php(180): Illuminate\Foundation\Http\Middleware\VerifyCsrfToken->handle(Object(Illuminate\Http\Request), Object(Closure))
    #10 /App/ApplicationLaravel/vendor/laravel/framework/src/Illuminate/View/Middleware/ShareErrorsFromSession.php(49): Illuminate\Pipeline\Pipeline->Illuminate\Pipeline\{closure}(Object(Illuminate\Http\Request))
    #11 /App/ApplicationLaravel/vendor/laravel/framework/src/Illuminate/Pipeline/Pipeline.php(180): Illuminate\View\Middleware\ShareErrorsFromSession->handle(Object(Illuminate\Http\Request), Object(Closure))
    #12 /App/ApplicationLaravel/vendor/laravel/framework/src/Illuminate/Session/Middleware/StartSession.php(121): Illuminate\Pipeline\Pipeline->Illuminate\Pipeline\{closure}(Object(Illuminate\Http\Request))
    #13 /App/ApplicationLaravel/vendor/laravel/framework/src/Illuminate/Session/Middleware/StartSession.php(64): Illuminate\Session\Middleware\StartSession->handleStatefulRequest(Object(Illuminate\Http\Request), Object(Illuminate\Session\Store), Object(Closure))
    #14 /App/ApplicationLaravel/vendor/laravel/framework/src/Illuminate/Pipeline/Pipeline.php(180): Illuminate\Session\Middleware\StartSession->handle(Object(Illuminate\Http\Request), Object(Closure))
    #15 /App/ApplicationLaravel/vendor/laravel/framework/src/Illuminate/Cookie/Middleware/AddQueuedCookiesToResponse.php(37): Illuminate\Pipeline\Pipeline->Illuminate\Pipeline\{closure}(Object(Illuminate\Http\Request))
    #16 /App/ApplicationLaravel/vendor/laravel/framework/src/Illuminate/Pipeline/Pipeline.php(180): Illuminate\Cookie\Middleware\AddQueuedCookiesToResponse->handle(Object(Illuminate\Http\Request), Object(Closure))
    #17 /App/ApplicationLaravel/vendor/laravel/framework/src/Illuminate/Cookie/Middleware/EncryptCookies.php(67): Illuminate\Pipeline\Pipeline->Illuminate\Pipeline\{closure}(Object(Illuminate\Http\Request))
    #18 /App/ApplicationLaravel/vendor/laravel/framework/src/Illuminate/Pipeline/Pipeline.php(180): Illuminate\Cookie\Middleware\EncryptCookies->handle(Object(Illuminate\Http\Request), Object(Closure))
    #19 /App/ApplicationLaravel/vendor/laravel/framework/src/Illuminate/Pipeline/Pipeline.php(116): Illuminate\Pipeline\Pipeline->Illuminate\Pipeline\{closure}(Object(Illuminate\Http\Request))
    #20 /App/ApplicationLaravel/vendor/laravel/framework/src/Illuminate/Routing/Router.php(797): Illuminate\Pipeline\Pipeline->then(Object(Closure))
    #21 /App/ApplicationLaravel/vendor/laravel/framework/src/Illuminate/Routing/Router.php(776): Illuminate\Routing\Router->runRouteWithinStack(Object(Illuminate\Routing\Route), Object(Illuminate\Http\Request))
    #22 /App/ApplicationLaravel/vendor/laravel/framework/src/Illuminate/Routing/Router.php(740): Illuminate\Routing\Router->runRoute(Object(Illuminate\Http\Request), Object(Illuminate\Routing\Route))
    #23 /App/ApplicationLaravel/vendor/laravel/framework/src/Illuminate/Routing/Router.php(729): Illuminate\Routing\Router->dispatchToRoute(Object(Illuminate\Http\Request))
    #24 /App/ApplicationLaravel/vendor/laravel/framework/src/Illuminate/Foundation/Http/Kernel.php(190): Illuminate\Routing\Router->dispatch(Object(Illuminate\Http\Request))
    #25 /App/ApplicationLaravel/vendor/laravel/framework/src/Illuminate/Pipeline/Pipeline.php(141): Illuminate\Foundation\Http\Kernel->Illuminate\Foundation\Http\{closure}(Object(Illuminate\Http\Request))
    #26 /App/ApplicationLaravel/vendor/laravel/framework/src/Illuminate/Foundation/Http/Middleware/TransformsRequest.php(21): Illuminate\Pipeline\Pipeline->Illuminate\Pipeline\{closure}(Object(Illuminate\Http\Request))
    #27 /App/ApplicationLaravel/vendor/laravel/framework/src/Illuminate/Foundation/Http/Middleware/ConvertEmptyStringsToNull.php(31): Illuminate\Foundation\Http\Middleware\TransformsRequest->handle(Object(Illuminate\Http\Request), Object(Closure))
    #28 /App/ApplicationLaravel/vendor/laravel/framework/src/Illuminate/Pipeline/Pipeline.php(180): Illuminate\Foundation\Http\Middleware\ConvertEmptyStringsToNull->handle(Object(Illuminate\Http\Request), Object(Closure))
    #29 /App/ApplicationLaravel/vendor/laravel/framework/src/Illuminate/Foundation/Http/Middleware/TransformsRequest.php(21): Illuminate\Pipeline\Pipeline->Illuminate\Pipeline\{closure}(Object(Illuminate\Http\Request))
    #30 /App/ApplicationLaravel/vendor/laravel/framework/src/Illuminate/Foundation/Http/Middleware/TrimStrings.php(40): Illuminate\Foundation\Http\Middleware\TransformsRequest->handle(Object(Illuminate\Http\Request), Object(Closure))
    #31 /App/ApplicationLaravel/vendor/laravel/framework/src/Illuminate/Pipeline/Pipeline.php(180): Illuminate\Foundation\Http\Middleware\TrimStrings->handle(Object(Illuminate\Http\Request), Object(Closure))
    #32 /App/ApplicationLaravel/vendor/laravel/framework/src/Illuminate/Foundation/Http/Middleware/ValidatePostSize.php(27): Illuminate\Pipeline\Pipeline->Illuminate\Pipeline\{closure}(Object(Illuminate\Http\Request))
    #33 /App/ApplicationLaravel/vendor/laravel/framework/src/Illuminate/Pipeline/Pipeline.php(180): Illuminate\Foundation\Http\Middleware\ValidatePostSize->handle(Object(Illuminate\Http\Request), Object(Closure))
    #34 /App/ApplicationLaravel/vendor/laravel/framework/src/Illuminate/Foundation/Http/Middleware/PreventRequestsDuringMaintenance.php(86): Illuminate\Pipeline\Pipeline->Illuminate\Pipeline\{closure}(Object(Illuminate\Http\Request))
    #35 /App/ApplicationLaravel/vendor/laravel/framework/src/Illuminate/Pipeline/Pipeline.php(180): Illuminate\Foundation\Http\Middleware\PreventRequestsDuringMaintenance->handle(Object(Illuminate\Http\Request), Object(Closure))
    #36 /App/ApplicationLaravel/vendor/laravel/framework/src/Illuminate/Http/Middleware/HandleCors.php(49): Illuminate\Pipeline\Pipeline->Illuminate\Pipeline\{closure}(Object(Illuminate\Http\Request))
    #37 /App/ApplicationLaravel/vendor/laravel/framework/src/Illuminate/Pipeline/Pipeline.php(180): Illuminate\Http\Middleware\HandleCors->handle(Object(Illuminate\Http\Request), Object(Closure))
    #38 /App/ApplicationLaravel/vendor/laravel/framework/src/Illuminate/Http/Middleware/TrustProxies.php(39): Illuminate\Pipeline\Pipeline->Illuminate\Pipeline\{closure}(Object(Illuminate\Http\Request))
    #39 /App/ApplicationLaravel/vendor/laravel/framework/src/Illuminate/Pipeline/Pipeline.php(180): Illuminate\Http\Middleware\TrustProxies->handle(Object(Illuminate\Http\Request), Object(Closure))
    #40 /App/ApplicationLaravel/vendor/laravel/framework/src/Illuminate/Pipeline/Pipeline.php(116): Illuminate\Pipeline\Pipeline->Illuminate\Pipeline\{closure}(Object(Illuminate\Http\Request))
    #41 /App/ApplicationLaravel/vendor/laravel/framework/src/Illuminate/Foundation/Http/Kernel.php(165): Illuminate\Pipeline\Pipeline->then(Object(Closure))
    #42 /App/ApplicationLaravel/vendor/laravel/framework/src/Illuminate/Foundation/Http/Kernel.php(134): Illuminate\Foundation\Http\Kernel->sendRequestThroughRouter(Object(Illuminate\Http\Request))
    #43 /App/ApplicationLaravel/public/index.php(51): Illuminate\Foundation\Http\Kernel->handle(Object(Illuminate\Http\Request))
    #44 /App/ApplicationLaravel/vendor/laravel/framework/src/Illuminate/Foundation/resources/server.php(16): require_once('/App/Applicatio...')
    #45 {main}
```

*Este error ocurre porque **`auth()->user()` es `null`**, lo cual indica que no hay un usuario autenticado. Al intentar acceder a `auth()->user()->contacts()`, Laravel lanza un error porque no se puede invocar un método en `null`.*

---

## **Causa del error**

*El error revela que **no hay middleware `auth` protegiendo la ruta**, lo cual permitió que un usuario no autenticado llegara hasta el controlador.*

**Solución:** *proteger la ruta con el middleware `auth`:*

```php
Route::middleware('auth')->group(function () {
    Route::get('/contacts', [ContactController::class, 'index']);
});
```

---

## **Cashier Paddle / Stripe y prueba de suscripción**

```bash
php artisan make:controller StripeController
```

*Aunque Laravel recomienda que los controladores sigan su convención, aquí mencionas que romperás la convención probablemente para agrupar lógica específica de Stripe, como suscripciones, pagos o webhooks.*

---

## **Middleware personalizado**

```bash
php artisan make:middleware EnsureUserIsSubscribed
```

*Este comando crea un middleware llamado `EnsureUserIsSubscribed`. Sirve para proteger rutas que requieren que el usuario tenga una suscripción activa.*

---

## **Cómo funciona un middleware**

> *"llega una peticion va el primer midleware luego al siguiente es una especie de pila"*

*Laravel ejecuta middlewares en orden, como una pila (stack). Cada middleware puede permitir continuar (`$next($request)`) o abortar la ejecución.*

---

## **Registro del middleware**

```php
// En app/Http/Kernel.php
"subscription" => \App\Http\Middleware\EnsureUserIsSubscribed::class,
```

*Esto permite usar el middleware como `subscription` en las rutas:*

```php
Route::middleware(['auth', 'subscription'])->group(function () {
    // Rutas protegidas
});
```

---

## **Uso de `Route::middleware()`**

```php
Route::middleware('auth'); // un middleware
Route::middleware(['auth', 'subscription']); // múltiples middlewares
```

*Laravel acepta tanto una cadena como un arreglo de strings, siempre que estén registrados en `Kernel.php`.*

---

## **Consulta SQL para prueba de suscripciones**

```sql
-- Verificar cuándo termina el periodo de prueba
SELECT trial_ends_at FROM users WHERE email = 'non-payment@gmail.com';

-- Forzar que ya haya terminado el periodo
UPDATE users SET trial_ends_at = '2025-06-25 23:39:46' WHERE email = 'non-payment@gmail.com';
```

*Esto se usa para probar que el middleware `EnsureUserIsSubscribed` **bloquea al usuario** si su suscripción o periodo de prueba ha expirado.*

---

## **Renderizar HTML en Blade**

*Por defecto, Blade escapa el contenido de variables por seguridad:*

```blade
{{ $message }} // esto escapa HTML
```

*Si necesitas **renderizar HTML crudo**, usa:*

```blade
{!! $message !!} // NO escapa HTML — úsalos con cuidado para evitar XSS
```

*Esto es útil si `$message` contiene etiquetas HTML como `<strong>` o `<a>` y quieres que se muestren como tal.*

---

## **Conclusión**

**Este bloque de apuntes cubre cómo:**

* *Proteger rutas con middleware*
* *Evitar errores por usuarios no autenticados*
* *Aplicar lógica de suscripción con Cashier*
* *Usar middlewares personalizados*
* *Modificar base de datos para pruebas*
* *Renderizar contenido HTML en vistas Blade*
