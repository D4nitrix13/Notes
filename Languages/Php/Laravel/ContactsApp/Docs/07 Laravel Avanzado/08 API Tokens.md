<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- Gitlab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# **API Tokens con Laravel Sanctum**

## **Name ¿`api-token` o `api_token`?**

- **Recomendado:** *`api-token`*
- **No recomendado:** *`api_token`*

### **¿Por qué `api-token`?**

*Laravel sigue las convenciones de URLs tipo RESTful, donde los nombres de recursos se colocan en **kebab-case** (con guiones):*

- *`api-token` generará rutas como:*

  - *`POST /api/api-token` → `api-token.store`*
  - *`GET /api/api-token/create` → `api-token.create`*

*Laravel también usará automáticamente `kebab-case` en las URLs si usás `Route::resource('api-token', ApiTokenController::class)`.*

---

### **Codigo**

```php
Route::resource(name: "api-token", controller: ApiTokenController::class)
    ->only(methods: ["create", "store"]);
```

- **Por convención en Laravel, el nombre del recurso que pasás a `Route::resource()` debe ser en plural y en `kebab-case`, para mantener la coherencia con las rutas `RESTful`.**

---

### **Lo correcto sería**

```php
Route::resource('api-tokens', ApiTokenController::class)
     ->only(['create', 'store']);
```

**Esto genera:**

| **Método** | **URI**                  | **Nombre de ruta**  | **Acción del controlador**   |
| ---------- | ------------------------ | ------------------- | ---------------------------- |
| *GET*      | */api/api-tokens/create* | *api-tokens.create* | *ApiTokenController\@create* |
| *POST*     | */api/api-tokens*        | *api-tokens.store*  | *ApiTokenController\@store*  |

---

### **¿Por qué en plural?**

*Laravel espera que los recursos estén en plural porque cada recurso representa una **colección**. Por ejemplo:*

- *`users` → colección de usuarios*
- *`posts` → colección de publicaciones*
- *`api-tokens` → colección de tokens de API*

**Entonces la estructura de carpetas debe ser:**

```bash
resources/views/
└── api-tokens/
    └── create.blade.php
```

---

### **Resumen general**

| **Elemento**            | **Nombre sugerido**             | **Comentario**             |
| ----------------------- | ------------------------------- | -------------------------- |
| *Ruta resource*         | *`'api-tokens'`*                | *Plural + `kebab-case`*    |
| *Vista para `create()`* | *`api-tokens.create`*           | *Coincide con la ruta*     |
| *Carpeta de vistas*     | *`resources/views/api-tokens/`* | *Debe existir esa carpeta* |
| *Fichero Blade*         | *`create.blade.php`*            | *Dentro de `api-tokens/`*  |

**Documentación oficial:** *[Sanctum — Laravel 12.x](https://laravel.com/docs/12.x/sanctum "https://laravel.com/docs/12.x/sanctum")*

*Laravel Sanctum permite emitir tokens API para usuarios autenticados, ideal para SPAs, apps móviles o uso de API personalizadas.*

---

## **1. Crear un controlador para los tokens**

```bash
php artisan make:controller ApiTokenController
```

- **`make:controller`:** *comando de Artisan para generar un nuevo controlador.*
- **`ApiTokenController`:** *nombre del controlador. Según la convención, debe estar en `PascalCase`.*

*También se puede generar un **API Resource** (útil para transformar respuestas JSON):*

```bash
php artisan make:resource ContactResource
```

- **`make:resource`:** *genera una clase que transforma modelos en JSON estructurado.*
- **`ContactResource`:** *nombre del recurso.*

---

## **2. Definición de rutas protegidas**

**Fichero: `routes/web.php`**

```php
Route::middleware(["auth", "subscription"])->group(callback: function () {
        Route::get(uri: '/home', action: [HomeController::class, 'index'])->name('home');
        Route::resource(name: "contacts", controller: ContactController::class);
        Route::resource(name: "contacts-shares", controller: ContactShareController::class)
                ->except(methods: ["show", "edit", "update"]);
        Route::resource(name: "api-tokens", controller: ApiTokenController::class)
                ->only(methods: ["create", "store"]);
});
```

### **Explicación:**

- **`middleware(["auth", "subscription"])`:** *protege las rutas, asegurando que el usuario esté autenticado y tenga una suscripción activa.*
- **`Route::resource()`:** *genera rutas RESTful para el recurso.*

  - *`only()` limita a los métodos especificados (`create` y `store`).*
  - *`except()` excluye métodos que no se usarán.*

---

## **3. Controlador `ApiTokenController`**

**Ubicación: `app/Http/Controllers/ApiTokenController.php`**

```php
<?php

namespace App\Http\Controllers;

use Illuminate\Contracts\View\View;
use Illuminate\Http\Request;

class ApiTokenController extends Controller
{
    public function create(): View
    {
        return view(view: "api-tokens.create");
    }

    public function store(Request $request)
    {
        ["name" => $name] =  $request->validate(rules: ["name" => "required|string"]);

        $token = $request->user()->createToken($name);

        // return ['token' => $token->plainTextToken];
        return view(
            view: "api-tokens.show",
            data: compact("token")
        );
    }
}
```

### **Detalles importantes:**

- **`create()`:** *retorna el formulario para crear un token.*
- **`store()`:**

  - *Valida que `name` sea obligatorio y de tipo cadena.*
  - *Llama a `createToken($name)` sobre el usuario autenticado, que genera un token.*
  - *Muestra la vista `show` pasando el token.*

---

## **4. Vistas utilizadas**

**Ubicación:**

```bash
resources/views/api-tokens/create.blade.php  
resources/views/api-tokens/show.blade.php
```

*Se recomienda que el nombre del folder (`api-tokens`) esté en **kebab-case** y en plural, para seguir la convención RESTful.*

---

## **5. Recurso API (`ContactResource`)**

*Ubicación: `app/Http/Resources/ContactResource.php`*

```php
<?php

namespace App\Http\Resources;

use Illuminate\Http\Resources\Json\JsonResource;

class ContactResource extends JsonResource
{
    /**
     * Transform the resource into an array.
     *
     * @param  \Illuminate\Http\Request  $request
     * @return array|\Illuminate\Contracts\Support\Arrayable|\JsonSerializable
     */
    public function toArray($request)
    {
        return parent::toArray($request);
    }
}
```

- *Hereda de `JsonResource`.*
- *`toArray($request)`: transforma automáticamente el modelo en JSON. Podés personalizar esto para filtrar o formatear campos.*

---

## **6. ¿Por qué `/api/` en las rutas?**

**En el fichero `app/Providers/RouteServiceProvider.php`:**

```php
$this->routes(function () {
    Route::middleware('api')
        ->prefix('api')
        ->group(base_path('routes/api.php'));

    Route::middleware('web')
        ->group(base_path('routes/web.php'));
});
```

- **Codigo Completo**

```php
<?php

namespace App\Providers;

use Illuminate\Cache\RateLimiting\Limit;
use Illuminate\Foundation\Support\Providers\RouteServiceProvider as ServiceProvider;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\RateLimiter;
use Illuminate\Support\Facades\Route;

class RouteServiceProvider extends ServiceProvider
{
    /**
     * The path to the "home" route for your application.
     *
     * Typically, users are redirected here after authentication.
     *
     * @var string
     */
    public const HOME = '/home';

    /**
     * Define your route model bindings, pattern filters, and other route configuration.
     *
     * @return void
     */
    public function boot()
    {
        $this->configureRateLimiting();

        $this->routes(function () {
            Route::middleware('api')
                ->prefix('api')
                ->group(base_path('routes/api.php'));

            Route::middleware('web')
                ->group(base_path('routes/web.php'));
        });
    }

    /**
     * Configure the rate limiters for the application.
     *
     * @return void
     */
    protected function configureRateLimiting()
    {
        RateLimiter::for('api', function (Request $request) {
            return Limit::perMinute(60)->by($request->user()?->id ?: $request->ip());
        });
    }
}
```

- *Las rutas de la API (fichero `routes/api.php`) llevan el prefijo `api/` automáticamente.*
- *Las rutas web (`routes/web.php`) no lo llevan.*

*Esto separa claramente las rutas web de las rutas API.*

---

## **7. Base de datos: tokens generados**

**Laravel Sanctum guarda los tokens en la tabla `personal_access_tokens`.**

**Ejemplo:**

```sql
SELECT * FROM personal_access_tokens;
```

**Resultado:**

```sql
4 | App\Models\User |            5 | D4nitrix13 | a22be6b2950de66b343fab7f0c4c8733fc7f1057560e857c069d17169a9a03e1 | ["*"]     | 2025-07-27 21:40:27 | 2025-07-27 21:23:18 | 2025-07-27 21:40:27
```

---

## **8. Pruebas con cURL**

```bash
# Obtener datos del usuario autenticado
curl -sSX GET "http://localhost:8000/api/user" \
  -H "Authorization: Bearer TU_TOKEN_AQUI" | jq

# Obtener contactos en formato JSON
curl -sSX GET "http://localhost:8000/api/contacts" \
  -H "Authorization: Bearer TU_TOKEN_AQUI" | jq
```

```bash
curl -sSX GET "http://172.17.0.2:8000/api/user" -H "Authorization: Bearer YBeZKJyVVj5rfLfyTejIHFtr7pg9dVuVMglXAw6P" | jq
{
  "id": 5,
  "name": "Daniel",
  "email": "daniel@gmail.com",
  "email_verified_at": null,
  "created_at": "2025-07-27T20:24:58.000000Z",
  "updated_at": "2025-07-27T20:24:58.000000Z",
  "stripe_id": null,
  "pm_type": null,
  "pm_last_four": null,
  "trial_ends_at": "2025-08-06T20:24:58.000000Z"
}
```

```bash
curl -sSX GET "http://172.17.0.2:8000/api/contacts" -H "Authorization: Bearer YBeZKJyVVj5rfLfyTejIHFtr7pg9dVuVMglXAw6P" | jq
{
  "data": [
    {
      "id": 46,
      "name": "Batman",
      "phone_number": "123456789",
      "email": "batman@gmail.com",
      "age": 24,
      "user_id": 5,
      "created_at": "2025-07-27T21:39:36.000000Z",
      "updated_at": "2025-07-27T21:39:59.000000Z",
      "profile_picture": "profiles/default.png"
    },
    {
      "id": 47,
      "name": "Joker",
      "phone_number": "987654321",
      "email": "joker@gmail.com",
      "age": 34,
      "user_id": 5,
      "created_at": "2025-07-27T21:40:24.000000Z",
      "updated_at": "2025-07-27T21:40:24.000000Z",
      "profile_picture": "profiles/default.png"
    }
  ]
}
```

### **Detalles:**

- *`-sS`: silencioso y muestra errores.*
- *`-X GET`: método HTTP usado (GET).*
- *`-H`: agrega un encabezado HTTP (en este caso, `Authorization`).*
- *`Bearer TU_TOKEN_AQUI`: tipo de token utilizado por Sanctum.*
- *`| jq`: formatea el JSON (requiere tener instalado [jq](https://jqlang.org/ "https://jqlang.org/")).*

---

## **9. Estructura sugerida para escalar el proyecto**

**Para mantener código limpio:**

```bash
app/Http/Controllers/
├── Api/
│   └── ContactApiController.php
└── Web/
    └── ContactController.php
```

**Separa los controladores web de los que responden a peticiones API.**
