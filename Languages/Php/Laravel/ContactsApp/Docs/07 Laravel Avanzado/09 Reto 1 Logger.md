<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- Gitlab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# **Reto 1 Logger**

## **Descripción del Reto**

**El objetivo de este reto es:**

* *Registrar logs en Laravel cuando se crea o elimina un producto.*
* *Los logs deben tener un mensaje específico y un contexto que incluya el modelo del producto.*
* *Se debe usar el sistema de logging de Laravel (`Log::info`).*
* *También se implementan políticas (`Policy`) para restringir que solo el dueño del producto pueda eliminarlo.*

---

## **Comandos Utilizados**

### **1. Crear el modelo `Product`:**

```bash
php artisan make:model Product
```

**Explicación:**

* **`php artisan`:** *Ejecuta comandos CLI de Laravel.*
* **`make:model`:** *Subcomando que crea un nuevo modelo Eloquent.*
* **`Product`:** *Nombre del modelo. Laravel automáticamente buscará la tabla `products`.*

> **Convención**: *El nombre del modelo debe estar en singular (`Product`) y la tabla correspondiente en plural y minúsculas (`products`).*

---

### **2. Crear el controlador con el modelo y migración:**

```bash
php artisan make:controller ProductController -m Product
```

**Explicación:**

* **`make:controller`:** *Subcomando para generar un nuevo controlador.*
* **`ProductController`:** *Nombre del controlador.*
* **`-m Product`:** *Crea simultáneamente el archivo de migración vinculado al modelo `Product`.*

---

### **3. Crear Migración:**

```bash
php artisan make:migration create_products_table
```

**Explicación:**

* **`make:migration`:** *Crea un archivo de migración.*
* **`create_products_table`:** *Nombre que describe la migración. Laravel infiere que es una creación de tabla y usa `Schema::create()`.*

---

### **4. Crear una política de autorización para el modelo:**

```bash
php artisan make:policy ProductPolicy --model=Product
```

**Explicación:**

* **`make:policy`:** *Genera una clase para definir reglas de autorización.*
* **`ProductPolicy`:** *Nombre de la clase.*
* **`--model=Product`:** *Vincula automáticamente la política al modelo `Product`.*

---

## **Estructura del Modelo `Product`**

```php
protected $fillable = ['name', 'description', 'price', 'user_id'];
```

**Explicación:**

* **`fillable`:** *Define qué atributos pueden ser asignados masivamente (ej. `$model->create($data)`).*
* *Esto es esencial para evitar vulnerabilidades como Mass Assignment.*

**File `app/Models/Product.php`**

```php
<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Product extends Model
{
    use HasFactory;
    protected $fillable = [
        "name",
        "description",
        "price",
        "user_id"
    ];
}
```

---

## **Política `ProductPolicy`**

```php
public function delete(User $user, Product $product)
{
    return $user->id === $product->user_id;
}
```

**Explicación:**

* *Verifica que el usuario autenticado sea el dueño del producto antes de permitir que lo elimine.*
* *Se utiliza `authorize('delete', $product)` en el controlador.*

**File `app/Policies/ProductPolicy.php`**

```php
<?php

namespace App\Policies;

use App\Models\Product;
use App\Models\User;
use Illuminate\Auth\Access\HandlesAuthorization;

class ProductPolicy
{
    use HandlesAuthorization;

    /**
     * Determine whether the user can view any models.
     *
     * @param  \App\Models\User  $user
     * @return \Illuminate\Auth\Access\Response|bool
     */
    public function viewAny(User $user)
    {
        //
    }

    /**
     * Determine whether the user can view the model.
     *
     * @param  \App\Models\User  $user
     * @param  \App\Models\Product  $product
     * @return \Illuminate\Auth\Access\Response|bool
     */
    public function view(User $user, Product $product)
    {
        return $user->id === $product->user_id;
    }

    /**
     * Determine whether the user can create models.
     *
     * @param  \App\Models\User  $user
     * @return \Illuminate\Auth\Access\Response|bool
     */
    public function create(User $user)
    {
        //
    }

    /**
     * Determine whether the user can update the model.
     *
     * @param  \App\Models\User  $user
     * @param  \App\Models\Product  $product
     * @return \Illuminate\Auth\Access\Response|bool
     */
    public function update(User $user, Product $product)
    {
        return $user->id === $product->user_id;
    }

    /**
     * Determine whether the user can delete the model.
     *
     * @param  \App\Models\User  $user
     * @param  \App\Models\Product  $product
     * @return \Illuminate\Auth\Access\Response|bool
     */
    public function delete(User $user, Product $product)
    {
        return $user->id === $product->user_id;
    }

    /**
     * Determine whether the user can restore the model.
     *
     * @param  \App\Models\User  $user
     * @param  \App\Models\Product  $product
     * @return \Illuminate\Auth\Access\Response|bool
     */
    public function restore(User $user, Product $product)
    {
        //
    }

    /**
     * Determine whether the user can permanently delete the model.
     *
     * @param  \App\Models\User  $user
     * @param  \App\Models\Product  $product
     * @return \Illuminate\Auth\Access\Response|bool
     */
    public function forceDelete(User $user, Product $product)
    {
        //
    }
}
```

---

## **Logging en Laravel**

```php
use Illuminate\Support\Facades\Log;

Log::info("Product created", ['product' => $product]);
```

**Explicación:**

* **`Log::info()`:** *Escribe una entrada en el archivo de log con nivel `info`.*
* **Primer argumento (`message`):** *Es el mensaje del log.*
* **Segundo argumento (`context`):** *Array con información adicional que se registrará, en este caso, el objeto `$product`.*

> [!NOTE]
> *Los logs se guardan en `storage/logs/laravel.log`.*

---

## **Controlador `ProductController`**

### **Método `store(Request $request)`**

1. **Valida los datos usando:**

    ```php
    $request->validate($this->productRules);
    ```

2. **Crea el producto:**

    ```php
    $product = auth()->user()->products()->create($data);
    ```

3. **Registra el log:**

    ```php
    Log::info("Product created", ['product' => $product]);
    ```

**File `app/Http/Controllers/ProductController.php`**

```php
<?php

namespace App\Http\Controllers;

use App\Models\Product;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Log;

class ProductController extends Controller
{
    protected array $productRules = [
        'name' => 'required|string|max:64',
        'description' => 'required|string|max:512',
        'price' => 'required|integer|gt:0',
    ];

    /**
     * Display a listing of the resource.
     *
     * @return \Illuminate\Http\Response
     */
    public function index()
    {
        //
    }

    /**
     * Show the form for creating a new resource.
     *
     * @return \Illuminate\Http\Response
     */
    public function create()
    {
        //
    }

    /**
     * Store a newly created resource in storage.
     *
     * @param  \Illuminate\Http\Request  $request
     * @return \Illuminate\Http\Response
     */
    public function store(Request $request)
    {
        $data = $request->validate(rules: $this->productRules);
        $product = auth()->user()->products()->create($data);

        Log::info("Product created", ['product' => $product]);

        // Log::channel(channel: null)->info(
        //     message: "Product created",
        //     context: ["product" => $product]
        // );
        return response()->json(data: [
            "message" => "Product created successfully",
            "product" => $product,
        ]);
    }

    /**
     * Display the specified resource.
     *
     * @param  \App\Models\Product  $product
     * @return \Illuminate\Http\Response
     */
    public function show(Product $product)
    {
        //
    }

    /**
     * Show the form for editing the specified resource.
     *
     * @param  \App\Models\Product  $product
     * @return \Illuminate\Http\Response
     */
    public function edit(Product $product)
    {
        //
    }

    /**
     * Update the specified resource in storage.
     *
     * @param  \Illuminate\Http\Request  $request
     * @param  \App\Models\Product  $product
     * @return \Illuminate\Http\Response
     */
    public function update(Request $request, Product $product)
    {
        //
    }

    /**
     * Remove the specified resource from storage.
     *
     * @param  \App\Models\Product  $product
     * @return \Illuminate\Http\Response
     */
    public function destroy(Product $product)
    {
        $this->authorize(ability: "delete", arguments: $product);
        
        $product->delete();

        Log::info(
            message: "Product deleted",
            context: ["product" => $product]
        );

        return response()->json(data: [
            'message' => 'Product deleted successfully',
            'product' => $product
        ]);
    }
}
```

---

### **Método `destroy(Product $product)`**

1. **Autoriza la acción:**

    ```php
    $this->authorize('delete', $product);
    ```

2. **Elimina el producto:**

    ```php
    $product->delete();
    ```

3. **Registra el log:**

    ```php
    Log::info("Product deleted", ['product' => $product]);
    ```

---

## **Migración `database/migrations/2025_07_27_225915_create_products_table.php`**

```php
$table->string("name");
$table->text("description");
$table->integer("price", unsigned: true);
$table->foreignIdFor(User::class);
```

**Explicación de cada tipo de columna:**

* **`string`:** *Almacena cadenas de texto cortas (`VARCHAR`).*
* **`text`:** *Cadenas largas (`TEXT`).*
* **`integer`:** *Enteros.*
* **`unsigned`:** *Valor no negativo.*
* **`foreignIdFor(User::class)`:** *Crea automáticamente una columna `user_id` y define la relación foránea a la tabla `users`.*
* **File**

    ```php
    <?php

    use App\Models\User;
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
            Schema::create('products', function (Blueprint $table) {
                $table->id();
                $table->string(column: "name");
                $table->text(column: "description");
                $table->integer(column: "price", unsigned: true);
                $table->foreignIdFor(model: User::class);
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
            Schema::dropIfExists('products');
        }
    };
    ```

---

## **Registro de Política en `AuthServiceProvider`**

```php
protected $policies = [
    Product::class => ProductPolicy::class,
];
```

* *Permite que Laravel reconozca `ProductPolicy` como la política oficial para el modelo `Product`.*

**File `app/Providers/AuthServiceProvider.php`**

```php
<?php

namespace App\Providers;

use App\Models\Product;
use App\Policies\ProductPolicy;
use Illuminate\Foundation\Support\Providers\AuthServiceProvider as ServiceProvider;
use Illuminate\Support\Facades\Gate;

class AuthServiceProvider extends ServiceProvider
{
    /**
     * The policy mappings for the application.
     *
     * @var array<class-string, class-string>
     */
    protected $policies = [
        // 'App\Models\Model' => 'App\Policies\ModelPolicy',
        "App\Models\Product" => "App\Policies\ProductPolicy"
    ];

    /**
     * Register any authentication / authorization services.
     *
     * @return void
     */
    public function boot()
    {
        $this->registerPolicies();

        //
    }
}
```

---

## **Rutas**

```php
Route::resource('products', ProductController::class);
```

**Explicación:**

* **`resource`:** *Crea automáticamente las 7 rutas REST (`index`, `create`, `store`, `show`, `edit`, `update`, `destroy`).*

* **File `routes/web.php**

    ```php
    <?php

    use App\Http\Controllers\ProductController;
    use Illuminate\Http\Request;
    use Illuminate\Support\Facades\Response;
    use Illuminate\Support\Facades\Route;

    /*
    |--------------------------------------------------------------------------
    | Web Routes
    |--------------------------------------------------------------------------
    |
    | Here is where you can register web routes for your application. These
    | routes are loaded by the RouteServiceProvider within a group which
    | contains the "web" middleware group. Now create something great!
    |
    */

    Route::get('/', function () {
        return view('welcome');
    });

    // Ejercicio 1

    Route::get('/ejercicio1', function () {
        return "GET OK";
    });

    Route::post('/ejercicio1', function () {
        return "POST OK";
    });

    // Challenge1

    Route::resource('products', ProductController::class);
    ```

---

### **Explicación completa de `protected $policies = [...]`**

*En el archivo `app/Providers/AuthServiceProvider.php`, se encuentra este fragmento:*

```php
protected $policies = [
    Product::class => ProductPolicy::class,
];
```

#### **¿Qué Significa?**

*Este arreglo le indica a Laravel qué política (`Policy`) usar para cada modelo. En este caso:*

* *`Product::class`: es una forma abreviada de escribir `'App\Models\Product'`*
* *`ProductPolicy::class`: es igual a `'App\Policies\ProductPolicy'`*

> *Es decir, Laravel usará la clase `ProductPolicy` para autorizar acciones sobre el modelo `Product`.*

#### *Forma completa (no abreviada)*

*También podrías escribirlo así, de forma explícita:*

```php
protected $policies = [
    'App\Models\Product' => 'App\Policies\ProductPolicy',
];
```

*Ambas formas son completamente válidas. La diferencia es que `::class` es una **forma abreviada, segura y moderna** que además permite autocompletado en los editores.*

---

### **¿Por qué se usa `\` a veces en Laravel?**

**Cuando ves algo como:**

```php
\App\Models\Product
```

> [!NOTE]
> *El carácter `\` (backslash) indica que se hace referencia al **espacio de nombres raíz**. Esto es útil cuando estás en un namespace como `App\Providers` y quieres acceder a una clase que está en otro namespace sin importar el contexto actual.*

**Ejemplo:**

```php
namespace App\Providers;

// Sin \
use App\Models\Product;

// Con \ Explícito Desde La Raíz
use \App\Models\Product;
```

*Ambas funcionan, pero el `\` se usa a veces para evitar conflictos de resolución de nombres.*

---

### **¿Qué es "Mass Assignment" y por qué usamos `$fillable`?**

> [!NOTE]
> *El **mass assignment** (asignación masiva) es una forma rápida de crear o actualizar modelos Eloquent con un array de datos:*

```php
Product::create([
    'name' => 'Laptop',
    'description' => 'Gaming laptop',
    'price' => 1500,
    'user_id' => 1
]);
```

> [!CAUTION]
> *Pero esto puede ser **peligroso** si no se controlan los campos permitidos.*

#### **Solución: `$fillable`**

**En tu modelo:**

```php
protected $fillable = ['name', 'description', 'price', 'user_id'];
```

*Laravel solo permitirá la asignación masiva a esos campos. Cualquier otro campo enviado será ignorado.*

*Esto previene ataques como el intento de sobrescribir un campo no permitido (por ejemplo, `is_admin`).*

---

## **Resumen**

| **Acción**        | **Resultado**                                                                              |
| ----------------- | ------------------------------------------------------------------------------------------ |
| *Crear producto*  | *Se crea y se registra `"Product created"` con el producto como contexto.*                 |
| *Borrar producto* | *Se autoriza, se elimina y se registra `"Product deleted"` con el producto como contexto.* |
