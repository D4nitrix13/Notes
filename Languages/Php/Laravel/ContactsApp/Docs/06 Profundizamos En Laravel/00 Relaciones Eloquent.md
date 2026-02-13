<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# **Relaciones Eloquent En Laravel**

## **¿Qué son?**

**Eloquent es el ORM (Object-Relational Mapper) de Laravel. Permite definir relaciones entre tablas (modelos) de forma declarativa y sencilla, por ejemplo:**

* **Uno a muchos** *(`hasMany`, `belongsTo`)*
* **Uno a uno** *(`hasOne`)*
* **Muchos a muchos** *(`belongsToMany`)*
* **Uno a muchos a través de** *(`hasManyThrough`)*

*Laravel usa convenciones para mapear automáticamente las relaciones si sigues sus reglas de nombres.*

---

## **Claves Foráneas En Migraciones**

*Laravel permite definir claves foráneas (foreign keys) en migraciones, lo que impone **integridad referencial** a nivel de base de datos.*

---

### **Forma clásica (manual)**

```php
$table->foreign('user_id')->references('id')->on('users');
```

* *`foreign('user_id')` ➜ Declara que `user_id` será una clave foránea.*
* *`references('id')` ➜ Apunta a la columna `id` de la tabla relacionada.*
* *`on('users')` ➜ Indica que se relaciona con la tabla `users`.*

*Esta es la forma **explícita** de definir una relación entre tablas.*

---

### **Forma moderna y simplificada (Laravel 7+)**

```php
$table->foreignIdFor(User::class);
```

*Esto **es equivalente** a la versión clásica, y Laravel asume automáticamente:*

* *La columna se llamará `user_id`*
* *Se referenciará a la columna `id`*
* *En la tabla `users` (nombre pluralizado del modelo)*

---

### **¿Cómo funciona internamente?**

*Laravel sigue **estas convenciones** al usar `foreignIdFor(Model::class)`:*

| **Modelo**       | **Columna generada** | **Tabla referenciada** |
| ---------------- | -------------------- | ---------------------- |
| *`User`*         | *`user_id`*          | *`users`*              |
| *`Character`*    | *`character_id`*     | *`characters`*         |
| *`ProductImage`* | *`product_image_id`* | *`product_images`*     |

#### **Reglas**

* *El nombre de la **columna** es `snake_case` del nombre del modelo + `_id`.*
* *El nombre de la **tabla** es `lower_case` y el **plural** de ese modelo.*
* *El modelo se pasa como `User::class` (singular y en `TitleCase`).*

---

### **Ejemplo completo de migración**

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

            // $table->foreign('user_id')->references('id')->on('users');
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
        Schema::dropIfExists('contacts');
    }
};
```

---

## **Migrate\:Rollback**

### **Comando**

```bash
php artisan migrate:rollback --step=1
```

### **¿Qué hace?**

* *Deshace (revierte) la última migración o grupo de migraciones.*
* *El `--step=1` indica que **solo se revierta una migración** (la última ejecutada).*

#### **¡Importante**

> *Al hacer rollback, **los datos de las tablas eliminadas también se pierden**, porque Laravel llama a `Schema::dropIfExists(...)` en `down()`.*

*Esto **no es problema en entornos de desarrollo**, donde los datos pueden regenerarse fácilmente.*

---

## **Consultar En La Base De Datos (Postgresql)**

**Comando con Docker:**

```bash
docker container exec -it db psql \
  -h localhost -U postgres -p 5432 -d contacts_app \
  -c "SELECT * FROM contacts;"
```

### **Desglose del comando**

| **Parte**                        | **Significado**                                           |
| -------------------------------- | --------------------------------------------------------- |
| *`docker container exec -it db`* | *Ejecuta un comando interactivo en el contenedor `db`.*   |
| *`psql`*                         | *Cliente de línea de comandos de PostgreSQL.*             |
| *`-h localhost`*                 | *Host de la base de datos (en este caso, el contenedor).* |
| *`-U postgres`*                  | *Usuario de la base de datos.*                            |
| *`-p 5432`*                      | *Puerto de conexión de PostgreSQL.*                       |
| *`-d contacts_app`*              | *Base de datos a la que nos conectamos.*                  |
| *`-c "SELECT * FROM contacts;"`* | *Consulta SQL que se desea ejecutar.*                     |

---

### **Resultado esperado**

```bash
 id |  name  | phone_number |      email       | age | user_id |     created_at      |     updated_at      
----+--------+--------------+------------------+-----+---------+---------------------+---------------------
  1 | Batman | 123456789    | batman@gmail.com |  25 |       1 | 2025-06-05 17:21:14 | 2025-06-05 17:21:14
(1 row)
```

* **Resumen final**

| **Concepto**                              | **Explicación clave**                                                     |
| ----------------------------------------- | ------------------------------------------------------------------------- |
| *`foreign()` + `references()`*            | *Forma manual de crear claves foráneas.*                                  |
| *`foreignIdFor(User::class)`*             | *Forma automática y moderna en Laravel.*                                  |
| *Convenciones Laravel*                    | *Usa nombre del modelo en singular → `snake_case` + `_id`, tabla plural.* |
| *`php artisan migrate:rollback --step=1`* | *Revierte una migración (y pierde sus datos).*                            |
| *Docker + `psql`*                         | *Permite consultar los datos directamente desde la terminal.*             |

*[Eloquent Relationships Main Content](https://laravel.com/docs/12.x/eloquent-relationships#main-content "https://laravel.com/docs/12.x/eloquent-relationships#main-content")*
*[Eloquent Relationships One To many](https://laravel.com/docs/12.x/eloquent-relationships#one-to-many "https://laravel.com/docs/12.x/eloquent-relationships#one-to-many")*

## **Uso de relaciones Eloquent y buenas prácticas en Laravel**

---

## **Ruta De Trabajo**

```bash
ApplicationLaravel/
├── app/
│   ├── Http/
│   │   └── Controllers/
│   │       └── ContactController.php
│   └── Models/
│       ├── Contact.php
│       └── User.php
├── database/
│   └── migrations/
│       └── 2025_03_22_030026_create_contacts_table.php
```

---

## **Uso de consultas Eloquent con atajos**

### **Caso largo y explícito**

```php
$contacts = Contact::query()->where(
    "user_id",
    "=",
    auth()->id()
)->get();
```

#### **Desglose**

* *`Contact::query()` → Inicia una instancia de consulta.*
* *`where("user_id", "=", auth()->id())` → Filtra los contactos del usuario autenticado.*
* *`->get()` → Ejecuta la consulta y devuelve una colección.*

### **Versión simplificada**

```php
$contacts = Contact::where("user_id", auth()->id())->get();
```

> [!TIP]
> **Laravel detecta automáticamente el operador `=` si no lo escribís.**

---

## *Versión **más limpia aún** con relaciones Eloquent*

```php
$contacts = auth()->user()->contacts;
```

* *`auth()->user()` → Retorna el modelo del usuario autenticado.*
* *`contacts` → Accede directamente a la **relación hasMany** definida en `User.php`.*

---

## **Nomenclatura estándar en relaciones**

**Laravel espera convenciones para inferir automáticamente relaciones, claves foráneas y nombres de columnas:**

| **Modelo**    | **Campo relacionado en tabla hija** | **Tabla inferida** |
| ------------- | ----------------------------------- | ------------------ |
| *`User`*      | *`user_id`*                         | *`users`*          |
| *`Character`* | *`character_id`*                    | *`characters`*     |

---

### **Si No Seguís La Convención**

**Ejemplo personalizado:**

**Migración (contactos):**

```php
$table->foreign('user_id_number')->references('id')->on('users');
```

**Modelo `User`:**

```php
public function contacts()
{
    return $this->hasMany(
        related: Contact::class,
        foreignKey: 'user_id_number'
    );
}
```

**Modelo `Contact`:**

```php
protected $fillable = [
    'name',
    'phone_number',
    'age',
    'email',
    'user_id_number',
];
```

*Esto **funciona**, pero te obliga a **especificar manualmente la relación** en lugar de dejar que Laravel la deduzca automáticamente.*

---

### **Si seguís la nomenclatura correcta**

**Migración:**

```php
$table->foreignIdFor(User::class);
```

**Laravel genera automáticamente:**

* *Columna: `user_id`*
* *Referencia: `id`*
* *Tabla: `users`*

**Modelo `User`:**

```php
public function contacts()
{
    return $this->hasMany(Contact::class); // Laravel deduce foreignKey = user_id
}
```

**Modelo `Contact`:**

```php
protected $fillable = ['name', 'phone_number', 'age', 'email', 'user_id'];
```

**Y luego podés hacer lo siguiente:**

```php
$contacts = auth()->user()->contacts; // Funciona sin código adicional
```

---

## **Atajo en método `store()` de `ContactController`**

### **Forma larga**

```php
$data['user_id'] = auth()->id();
Contact::create($data);
```

### **Mejor forma si seguís la relación**

```php
auth()->user()->contacts()->create($data);
```

* **¿Qué hace?**

* *Usa directamente la relación `contacts()` del usuario autenticado.*
* *Agrega automáticamente el `user_id` al crear el contacto.*
* *Es más limpio, más seguro y más semántico.*

---

## **Resumen de buenas prácticas**

| **Acción**                         | **Buena práctica**                                                  |
| ---------------------------------- | ------------------------------------------------------------------- |
| *Crear relaciones entre modelos*   | *Usar `hasMany()`, `belongsTo()` con convenciones Laravel*          |
| *Crear clave foránea en migración* | *Usar `foreignIdFor(User::class)`*                                  |
| *Consultar datos relacionados*     | *Usar `auth()->user()->contacts`*                                   |
| *Insertar datos con relación*      | *Usar `auth()->user()->contacts()->create($data)`*                  |
| *Nombres personalizados*           | *Evitarlos si no es estrictamente necesario, requiere código extra* |

---

## **Glosario de funciones usadas**

| **Función / Helper**           | **Significado**                                                           |
| ------------------------------ | ------------------------------------------------------------------------- |
| *`auth()`*                     | *Retorna la instancia del helper de autenticación.*                       |
| *`auth()->user()`*             | *Usuario autenticado (modelo `User`).*                                    |
| *`->contacts()`*               | *Llama a la relación `hasMany()` definida en `User.php`.*                 |
| *`->create($data)`*            | *Crea un nuevo registro con `$data` y lo guarda.*                         |
| *`fillable`*                   | *Atributos permitidos para asignación masiva (`create`, `update`).*       |
| *`foreignIdFor(Model::class)`* | *Agrega columna `model_id` y define la relación foránea automáticamente.* |

---

## **`php artisan tinker` + relaciones Eloquent**

---

## **¿Qué es `php artisan tinker`?**

*`php artisan tinker` es una herramienta **interactiva** incluida con Laravel que permite:*

* *Ejecutar código PHP desde la línea de comandos.*
* *Probar modelos, relaciones, consultas Eloquent y helpers sin necesidad de navegador.*
* *Depurar código directamente.*

*Tinker usa **PsySH**, una shell interactiva de PHP.*

---

### **Comando básico**

```bash
php artisan tinker
```

* **¿Qué hace?**

**Abre un entorno interactivo donde podés escribir código PHP directamente.**

---

## **Ejemplo de uso**

```bash
User::find(1)->contacts()->get()
```

### **¿Qué significa?**

1. *`User::find(1)` → Busca el usuario con `id = 1`.*
2. *`->contacts()` → Llama a la relación `hasMany()` definida en el modelo `User`.*
3. *`->get()` → Ejecuta la consulta y devuelve una colección de resultados.*

### **Resultado en Tinker**

```bash
Psy Shell v0.12.7 (PHP 8.3.0 — cli) by Justin Hileman
> User::find(1)->contacts()->get()
[!] Aliasing 'User' to 'App\Models\User' for this Tinker session.
= Illuminate\Database\Eloquent\Collection {#6045
    all: [
      App\Models\Contact {#6043
        id: 1,
        name: "Batman",
        phone_number: "123456789",
        email: "batman@gmail.com",
        age: 25,
        user_id: 1,
        created_at: "2025-06-05 17:21:14",
        updated_at: "2025-06-05 17:21:14",
      },
    ],
  }
```

---

## **Definición de relación inversa en el modelo `Contact`**

### **`ApplicationLaravel/app/Models/Contact.php`**

```php
public function user()
{
    return $this->belongsTo(related: User::class);
}
```

* **¿Qué significa?**

* *`belongsTo(...)` ➜ Define una **relación inversa** a `hasMany`.*
* *Laravel asume que:*

  * *La columna es `user_id`.*
  * *Apunta a la tabla `users`.*
  * *Referencia la columna `id`.*

## **Consulta inversa en Tinker**

> [!NOTE]
> *También podés escribir el **namespace completo**:*

```bash
App\Models\Contact::first()->user
```

* **¿Qué hace?**

1. *`Contact::first()` → Devuelve el primer contacto registrado.*
2. *`->user` → Accede automáticamente al usuario **asociado** a ese contacto.*

* **Resultado esperado**

```php
> App\Models\Contact::first()->user
= App\Models\User {#6061
    id: 1,
    name: "Daniel Benjamin Perez Morales",
    email: "daniel@gmail.com",
    email_verified_at: null,
    #password: "$2y$10$lnY6h3z5y2Kq86BweVmsIOv6iaTDZxh1d.2/h5nHPHhgbv6mIpZUa",
    #remember_token: null,
    created_at: "2025-06-05 16:54:42",
    updated_at: "2025-06-05 16:54:42",
  }
```

*Laravel detecta que el modelo `Contact` tiene una relación `user()` y la ejecuta automáticamente si se accede como propiedad (`->user`), gracias al método mágico `__get()`.*

---

## **Importante: Aplicar cambios en modelos**

### **Si hacés cambios en el código (por ejemplo, en los modelos)**

> [!CAUTION]
> **No se reflejan automáticamente en Tinker**.

* *Debés **salir y volver a entrar** para que Tinker cargue el código actualizado.*

### **Salir de Tinker**

```bash
exit
```

**Laravel mostrará:**

```bash
INFO  Goodbye.
```

---

## **Resumen de conceptos**

| **Elemento**               | **Explicación**                                              |
| -------------------------- | ------------------------------------------------------------ |
| *`php artisan tinker`*     | *Abre consola interactiva para probar código Laravel.*       |
| *`User::find(1)`*          | *Encuentra un usuario con ID 1.*                             |
| *`contacts()`*             | *Relación `hasMany` definida en el modelo `User`.*           |
| *`Contact::first()->user`* | *Accede al usuario al que pertenece un contacto.*            |
| *`belongsTo(User::class)`* | *Relación inversa a `hasMany`. Laravel deduce el `user_id`.* |
| *`exit`*                   | *Sale de Tinker.*                                            |
| *Reiniciar Tinker*         | *Obligatorio tras cambios en el código fuente.*              |

---

## **¿Por qué el nombre del método en una relación Eloquent se escribe en plural o en singular?**

---

## **Veredicto sobre la validez del contenido**

* **Verdadero y correcto:**

* *La afirmación de que se usa `contacts()` en plural cuando un usuario tiene muchos contactos (**hasMany**) es correcta.*
* *También es correcto usar `user()` en singular cuando un contacto pertenece a un solo usuario (**belongsTo**).*

> [!IMPORTANT]
> *Laravel **no impone** el uso de nombres en plural o singular, pero sí lo **recomienda como convención** para que el código sea más legible y coherente.*

---

### ***Tabla original***

*La tabla es técnicamente correcta. Solo haría un pequeño ajuste de formato para mayor claridad:*

| **Modelo**  | **Relación**                  | **Nombre del método** | **Tipo de relación** |
| ----------- | ----------------------------- | --------------------- | -------------------- |
| *`User`*    | *Tiene muchos contactos*      | *`contacts()`*        | *`hasMany()`*        |
| *`Contact`* | *Pertenece a un solo usuario* | *`user()`*            | *`belongsTo()`*      |

---

### **Afirmación sobre "Laravel infla esa lógica"**

> [!NOTE]
> *Laravel interpreta automáticamente la relación a partir del nombre del método y del tipo de relación definido (hasMany, belongsTo, etc.) para cargar los datos correspondientes.*

---

## **Versión resumida**

* *En Eloquent, se recomienda usar nombres de método en plural o singular **según la cardinalidad de la relación**:*
* *Usa nombres **en plural** (`contacts()`) para relaciones que retornan **múltiples modelos** (`hasMany`, `belongsToMany`).*
* *Usa nombres **en singular** (`user()`) para relaciones que retornan **una única instancia** (`hasOne`, `belongsTo`).*
* *Aunque Laravel no lo exige, **seguir esta convención mejora la legibilidad** y coherencia del código.*
