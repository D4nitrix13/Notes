<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- Gitlab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# **Ejercicio 4 — CRUD con relaciones, validaciones y políticas**

## **Descripción mejorada del Ejercicio 4**

1. *Crea un controlador para un modelo llamado **Product**. Para ello, primero debes generar una migración que añada una tabla llamada `products` en la base de datos, con los campos: `name`, `description` y `price`.*

2. *Los campos `name` y `description` deben ser de tipo **string**, mientras que `price` debe ser de tipo **integer**.*

3. *A continuación, crea el modelo **Product** y define con Eloquent las relaciones correspondientes:*

   * *Un **usuario tiene muchos productos** (`hasMany`).*
   * *Un **producto pertenece a un usuario** (`belongsTo`).*

4. *Una vez definido el modelo, crea el controlador **ProductController** y las rutas necesarias, siguiendo la convención RESTful que Laravel establece para implementar un CRUD.*

5. **El controlador deberá realizar las siguientes acciones en cada uno de sus métodos:**

   * **`store`:** *recibe mediante una petición `POST` un objeto JSON con los datos de un producto, lo almacena en la base de datos y devuelve una respuesta JSON con un mensaje y el producto creado.*
     **Formato de entrada:**

     ```json
     {
       "name": "Keyboard",
       "description": "Mechanical RGB keyboard",
       "price": 200
     }
     ```

6. *Se deben aplicar las siguientes reglas de validación:*

   * *El campo `price` debe ser un número **mayor que 0**.*
   * *El campo `name` debe tener un **máximo de 64 caracteres**.*
   * *El campo `description` debe tener un **máximo de 512 caracteres**.*

   **Formato esperado de la respuesta:**

   ```json
   {
     "message": "Product created successfully",
     "product": {
       "id": 1,
       "name": "Keyboard",
       "description": "Mechanical RGB keyboard",
       "price": 200,
       "created_at": "2022-04-01 13:55:00",
       "updated_at": "2022-04-01 13:55:00"
     }
   }
   ```

   ```php
   return [
    "message" => "Product created successfully",
    "product" => $product
   ];
   ```

> [!NOTE]
> *No es necesario convertir manualmente el modelo a JSON ni extraer cada campo individualmente. Si `$product` contiene una instancia del modelo `Product`, simplemente retorna:*

---

### **Otros métodos del controlador**

* **`update`:** *igual que `store`, pero actualiza un producto existente. El mensaje de respuesta debe ser:*
  *`"Product updated successfully"`.*

* **`delete`:** *elimina un producto de la base de datos y devuelve un mensaje:*
  *`"Product deleted successfully"` junto con los datos del producto eliminado.*

* **`show`:** *devuelve únicamente los datos del producto sin incluir ningún mensaje.*

* **`index`:** *devuelve todos los productos creados por el usuario autenticado. El formato debe ser:*

  ```php
  return ["products" => $products];
  ```

---

### **Políticas de acceso**

* *Solo el **usuario que ha creado un producto** puede **editarlo o eliminarlo**.*
* *Sin embargo, **todos los usuarios pueden ver cualquier producto**.*

---

## **1. Configuración del entorno de pruebas**

### *Cambio de rama para trabajar en el ejercicio*

```bash
git checkout Exercises4
```

*Esto cambia a una rama donde se implementará el CRUD del modelo `Product`.*

---

### **Configuración del archivo `.env`**

```ini
DB_CONNECTION=pgsql
DB_HOST=172.17.0.3
DB_PORT=5432
DB_DATABASE=products_app
DB_USERNAME=postgres
DB_PASSWORD=root
```

*Esto configura Laravel para usar PostgreSQL, conectándose al contenedor `db` en la IP 172.17.0.3, puerto 5432.*

---

### **Comando para crear la base de datos desde Docker**

```bash
docker container exec --interactive --tty --user 0:0 --privileged db \
  /bin/bash -c "export PGPASSWORD=root; \
  psql -h 172.17.0.3 -U postgres -p 5432 \
  -c 'DROP DATABASE IF EXISTS products_app;'"

docker container exec --interactive --tty --user 0:0 --privileged db \
  /bin/bash -c "export PGPASSWORD=root; \
  psql -h 172.17.0.3 -U postgres -p 5432 \
  -c 'CREATE DATABASE products_app;'"
```

**Esto reinicia la base de datos PostgreSQL desde el contenedor `db`.**

---

## **2. Creación del modelo y migración**

### **Crear la migración**

```bash
php artisan make:migration --ansi -vvv create_products_table
```

* *`--ansi`: fuerza salida con colores.*
* *`-vvv`: muestra información muy detallada (nivel de verbosidad 3).*

### **Editar la migración (`2025_06_16_020456_create_products_table.php`)**

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
            $table->string(column: "description");
            $table->integer(column: "price");
            $table->foreignIdFor(model: User::class)->constrained();
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

* *`foreignIdFor(User::class)->constrained()` crea `user_id` y le agrega una clave foránea a `users(id)`.*

---

### **Crear el modelo**

```bash
php artisan make:model Product
```

**Modificar `app/Models/Product.php`:**

```php
protected $fillable = ['name', 'description', 'price', 'user_id'];

public function user(): BelongsTo
{
    return $this->belongsTo(User::class);
}
```

**Y en `User.php`:**

```php
public function products(): HasMany
{
    return $this->hasMany(Product::class);
}
```

---

## **3. Controlador y Form Requests**

### **Crear el controlador**

```bash
php artisan make:controller --model=Product ProductController
```

**Esto genera el controlador con el modelo `Product` vinculado.**

---

### **Crear los Form Requests**

```bash
php artisan make:request StoreProductRequest
php artisan make:request UpdateProductRequest
```

**Luego, en cada uno definir reglas de validación:**

```php
return [
  'name' => 'required|string|max:64',
  'description' => 'required|string|max:512',
  'price' => 'required|numeric|min:1'
];
```

**Usarlos en `ProductController`:**

```php
public function store(StoreProductRequest $request)
{
    $product = auth()->user()->products()->create($request->validated());

    return response()->json([
        'message' => 'Product created successfully',
        'product' => $product
    ]);
}
```

---

## **4. Políticas de acceso**

### **Crear la política**

```bash
php artisan make:policy ProductPolicy --model=Product
```

### **Registrar en `app/Providers/AuthServiceProvider.php`**

```php
protected $policies = [
    \App\Models\Product::class => \App\Policies\ProductPolicy::class,
];
```

**Dentro de la política, permitir solo al **usuario creador** editar o eliminar:**

```php
public function update(User $user, Product $product)
{
    return $user->id === $product->user_id;
}

public function delete(User $user, Product $product)
{
    return $user->id === $product->user_id;
}
```

---

## **5. Rutas (en `web.php`)**

```php
Route::resource(name: "products", controller: ProductController::class);
```

---

## **6. Pruebas**

### **Ejecutar una prueba específica**

```bash
php artisan test --filter test_usuario_puede_crear_producto
```

```bash
PASS  Tests\Feature\Ejercicio4Test
✓ usuario puede crear producto

Tests:  1 passed
Time:   0.12s
```

### **Ejecutar todos los tests**

```bash
php artisan test
```

**Resultado exitoso:**

```bash
PASS  Tests\Feature\Ejercicio4Test
✓ usuario puede crear producto
✓ index devuelve todos los productos que pertenecen al usuario
✓ usuario puede ver producto creado por otro usuario
✓ usuario puede editar producto
✓ usuario puede borrar producto
✓ solo usuario propietario del producto puede borrarlo o editarlo

Tests: 6 passed
Time: 0.32s
```

---

## **¿Por qué migrar en cada test?**

**Usás el trait `DatabaseMigrations`:**

```php
use Illuminate\Foundation\Testing\DatabaseMigrations;

class Ejercicio4Test extends TestCase
{
    use DatabaseMigrations;
}
```

*Esto borra y recrea la base de datos antes de cada test para asegurar **aislamiento total** entre pruebas.*
