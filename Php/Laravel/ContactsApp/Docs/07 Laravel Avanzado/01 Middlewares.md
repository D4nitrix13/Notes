<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- Gitlab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# **Middlewares**

si no estamos autenticados ni siquiera deberiamos poder acceder aqui

```bash
curl -sSX GET 'http://172.17.0.2:8000/contacts/' \
  -H 'Cookie: XSRF-TOKEN=eyJpdiI6IklFRXhjT1dKVDVUOTdleGNsNE9ad0E9PSIsInZhbHVlIjoidjgvMUF5enVBYnFBWG83emVGQnJ3T0RjZWU3amxlNmNScHFnVHdSZTNkbkpBNHk2UWZXRVVEV2s5TC83eXFtcGtqUnhOYXZ2U0w2N1dTK2ZBa3ZDSmkwc3Vib1daa1FOOWlmMGV5OC9yZ1NVNE5xekJLZ0hIckhEZkF6QVZuT3IiLCJtYWMiOiI0ZGU5YmQ2OTliMjkyNDQyOWQxMjRkMWY1OGRhOTBkYzQ1OGY2NDk4YThiOTBhMWUxMGRhYTM1YTQyNTEyMjE5IiwidGFnIjoiIn0%3D; contacts_app_session=eyJpdiI6IlpBMGVhQWd5YThtZGYySmVUUU9weFE9PSIsInZhbHVlIjoiMkNNYklwWlBQa0JwOWNTUXlldkhJRW1hcDFjZ3I1eGtGMU9aSDArRjk2TDZrTytjaW9aKzFrM29RU2hSdWNZYjVjcVp6NFJKK2taa2ROeHF4VW90TlYyV0JtRjEzTmNGeXk4SGlhT2pLOGZrTkpyNUlzNHZCRVBBdmx6cWVjR1IiLCJtYWMiOiIxN2JlMTc1YjliM2EzMjBiYWUzZDRjODEyMTMzYWM3MGJiYWNlNzYwZjNlMDg2OGJkODE0MjRkODJlNjY5M2MxIiwidGFnIjoiIn0%3D' | html2text
```

salida

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

php artisan make:controller StripeController

aqui romperemos la nomenclatura de laravel ya que ...

<https://laravel.com/docs/12.x/cashier-paddle#checking-subscription-status>

php artisan make:middleware EnsureUserIsSubscribed

llega una peticion va el primer midleware luego al siguiente es una especie de pila

app/Http/Kernel.php
ponemos la siguitene linea en

"subscription" => \App\Http\Middleware\EnsureUserIsSubscribed::class

en web.php
esto pude recibir una string o una lista de string siempre y cuato los nombres esten registrados
Route::middleware();

```sql
SELECT trial_ends_at FROM users WHERE email = 'nopago@gmail.com'; 
    trial_ends_at    
---------------------
 2025-07-09 23:39:46
(1 row)

UPDATE users SET trial_ends_at = '2025-06-25 23:39:46' WHERE email = 'nopago@gmail.com';

```

<https://stackoverflow.com/questions/29253979/displaying-html-with-blade-shows-the-html-code>

para renderizar html en blender en vez de esto hariamos lo siguiente
resources/views/components/alert.blade.php

{{ $message }}
{!! $message !!}
