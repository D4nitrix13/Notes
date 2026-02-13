<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- Gitlab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# **Laravel - Database Seeders y Factories**

## **¿Qué son los Seeders y Factories?**

* **Seeders:** *Se utilizan para poblar la base de datos con datos de prueba automáticamente.*
* **Factories:** *Definen cómo se deben generar datos ficticios (fake) para un modelo.*

*Laravel usa la librería **Faker** para generar estos datos aleatorios.*

---

## **Comando para crear un Factory**

```bash
php artisan make:factory ContactFactory --model=Contact
```

### **Explicación**

| **Parte**           | **Significado**                                                               |
| ------------------- | ----------------------------------------------------------------------------- |
| *`php artisan`*     | **Comando base para ejecutar herramientas de Laravel.**                       |
| *`make:factory`*    | **Subcomando para crear una nueva *factory*.**                                |
| *`ContactFactory`*  | **Nombre del archivo factory. Laravel lo guardará en `database/factories/`.** |
| *`--model=Contact`* | **Indica que este factory pertenece al modelo `Contact`.**                    |

* **Laravel mostrará:**

```bash
INFO  Factory [database/factories/ContactFactory.php] created successfully.
```

---

## **Resetear Y Poblar Base De Datos**

### **1. Borrar Todas Las Tablas Y Migrarlas Nuevamente**

```bash
php artisan migrate:fresh
```

* **`migrate:fresh`:** *Elimina todas las tablas y vuelve a ejecutar las migraciones desde cero.*

---

### **2. Ejecutar todos los Seeders**

```bash
php artisan db:seed
```

* **`db:seed`:** *Ejecuta el método `run()` definido en `database/seeders/DatabaseSeeder.php`.*

---

### **3. Comando Combinado (Migrar + Seed En Una Sola Línea)**

```bash
php artisan migrate:fresh --seed
```

* **`--seed`:** *Opción que le indica a `migrate:fresh` que debe ejecutar el seeder principal después de migrar.*

---

## **Contraseña Por Defecto De Usuarios**

**El archivo `database/factories/UserFactory.php` tiene la contraseña codificada en hash de bcrypt:**

```php
'password' => '$2y$10$92IXUNpkjO0rOQ5byMi.Ye4oKoEa3Ro9llC/.og/at2.uheWG/igi',
```

*Este hash corresponde a la contraseña **`password`**.*

---

## **Ejemplo Completo De Factory De Usuario**

```php
<?php

namespace Database\Factories;

use Illuminate\Database\Eloquent\Factories\Factory;
use Illuminate\Support\Str;

/**
 * @extends \Illuminate\Database\Eloquent\Factories\Factory<\App\Models\User>
 */
class UserFactory extends Factory
{
    /**
     * Define the model's default state.
     *
     * @return array<string, mixed>
     */
    public function definition()
    {
        return [
            'name' => $this->faker->name(),
            'email' => $this->faker->unique()->safeEmail(),
            'email_verified_at' => now(),
            'password' => '$2y$10$92IXUNpkjO0rOQ5byMi.Ye4oKoEa3Ro9llC/.og/at2.uheWG/igi', // password
            'remember_token' => Str::random(length: 10),
            'trial_ends_at' => now()->addDays(value: 10)
        ];
    }

    /**
     * Indicate that the model's email address should be unverified.
     *
     * @return static
     */
    public function unverified()
    {
        return $this->state(function (array $attributes) {
            return [
                'email_verified_at' => null,
            ];
        });
    }
}
```

---

## **Factory para Contact: `database/factories/ContactFactory.php`**

```php
<?php

namespace Database\Factories;

use Illuminate\Database\Eloquent\Factories\Factory;

/**
 * @extends \Illuminate\Database\Eloquent\Factories\Factory<\App\Models\Contact>
 */
class ContactFactory extends Factory
{
    /**
     * Define the model's default state.
     *
     * @return array<string, mixed>
     */
    public function definition()
    {
        return [
            "name" => $this->faker->name(),
            "email" => $this->faker->unique()->safeEmail(),
            "phone_number" => $this->faker->phoneNumber(),
            "age" => $this->faker->numberBetween(int1: 20, int2: 60),

        ];
    }
}
```

### **Detalles**

* *`faker->name()` → Genera un nombre aleatorio.*
* *`faker->unique()->safeEmail()` → Email aleatorio y único.*
* *`faker->phoneNumber()` → Número aleatorio con formato internacional.*
* *`faker->numberBetween(20, 60)` → Número entero aleatorio entre 20 y 60.*

---

## **Seeder personalizado: `DatabaseSeeder.php`: `database/seeders/DatabaseSeeder.php`**

```php
<?php

namespace Database\Seeders;

use App\Models\User;
use Illuminate\Database\Console\Seeds\WithoutModelEvents;
use Illuminate\Database\Seeder;

class DatabaseSeeder extends Seeder
{
    /**
     * Seed the application's database.
     *
     * @return void
     */
    public function run()
    {
        // User::factory(count: 10)->create();
        
        // Crea un usuario llamado "Testing" con 30 contactos
        $testUser = User::factory()->hasContacts(30)->createOne([
            "name" => "Testing",
            "email" => "test@test.com",
        ]);

        // Crea 3 usuarios, cada uno con 5 contacto
        $users = User::factory(count: 3)->hasContacts(5)->create()->each(
            fn($user) => $user->contacts->first()->sharedWithUsers()->attach($testUser->id)
        );

        // Comparte el primer contacto del testUser con los 3 usuarios anteriores
        $testUser->contacts->first()->sharedWithUsers()->attach($users->pluck("id"));

        // \App\Models\User::factory()->create([
        //     'name' => 'Test User',
        //     'email' => 'test@example.com',
        // ]);
    }
}
```

### **Explicación Línea Por Línea**

```php
User::factory()->hasContacts(30)->createOne([...])
```

* *Crea un usuario con 30 contactos relacionados usando una relación `hasContacts()` definida en el modelo `User`.*

```php
User::factory(3)->hasContacts(5)->create()
```

* **Crea 3 usuarios. Cada uno con 5 contactos generados automáticamente.**

```php
->each(fn($user) => ...)
```

* *Itera sobre cada usuario recién creado y comparte su primer contacto con el usuario de prueba `testUser`.*

```php
$testUser->contacts->first()->sharedWithUsers()->attach(...)
```

* *El contacto del usuario "Testing" se comparte con los 3 usuarios recién creados.*

---

## **Extra: Ver IDs de usuarios en Tinker**

```bash
php artisan tinker
```

```php
User::all()->pluck("id")
```

### **Resultado**

```php
Illuminate\Support\Collection {#6062
  all: [1, 2, 3, 4],
}
```

* *`pluck("id")` devuelve solo los valores de la columna `id` en una colección.*

---

## **¿Por qué Laravel permite usar `hasContacts()` en el seeder?**

*Cuando escribes esto en el seeder:*

```php
User::factory()->hasContacts(30)->create();
```

*Laravel **no está buscando un método llamado `hasContacts()` en tu modelo `User`**. En realidad, este método **es generado dinámicamente por Laravel**, gracias a la **API fluida de model factories** introducida en Laravel 8 con `HasFactory`.*

---

## **¿Cómo funciona mágicamente `hasContacts()`?**

### **Laravel internamente analiza los métodos de relaciones definidos en tu modelo**

**En tu modelo `User` tienes:**

```php
public function contacts()
{
  return $this->hasMany(Contact::class);
}
```

*Laravel usa reflexión (reflection) para detectar las relaciones Eloquent en tu modelo, y cuando encuentra este método `contacts()`, automáticamente te permite llamar:*

```php
User::factory()->hasContacts(30)
```

* *Laravel toma el nombre de la relación **contacts**, le antepone **has**, y lo convierte en un método **dinámico** de la factory: `hasContacts()`.*

---

## **¿Qué hace `hasContacts(30)`?**

*Internamente llama a `Contact::factory()` y crea 30 contactos **relacionados automáticamente con el `user_id`** del modelo `User`.*

*Esto requiere que en el modelo `Contact` exista la relación inversa adecuada (`belongsTo`) y que el campo `user_id` sea parte del esquema.*

---

## **Resumen**

| **Elemento**                               | **¿Es necesario?**                                                 |
| ------------------------------------------ | ------------------------------------------------------------------ |
| *`contacts()`*                             | *Sí. Debe Estar En El Modelo `User` Como Método Eloquent*          |
| *`hasContacts()`*                          | *No. Laravel Lo **Crea Automáticamente** A Partir De `contacts()`* |
| *Relación inversa en `Contact` (`user()`)* | *Sí. Para Que Laravel Pueda Hacer El Vínculo Al Crear El Contacto* |

---

## **Bonus: Relación inversa recomendada en el modelo `Contact`**

*Para que la factory funcione correctamente, asegúrate que el modelo `Contact` tenga:*

```php
public function user()
{
  return $this->belongsTo(User::class);
}
```

---

## **Conclusión**

*El Método `Hascontacts()` **No Existe Como Código En Tu Modelo Ni Factory**, Pero Laravel Lo **Genera Dinámicamente** A Partir De La Relación `Contacts()` Que **Sí Definiste En El Modelo `User`**. Es Una Característica Poderosa De La Api Fluida De Las **Model Factories De Laravel 8+**.*
