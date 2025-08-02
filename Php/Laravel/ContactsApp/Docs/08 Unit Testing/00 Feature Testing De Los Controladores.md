<!-- Autor: Joker Batman Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- Gitlab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: Jokerperezdev@proton.me -->

# **Feature Testing de los Controladores en Laravel**

*En Laravel, las pruebas unitarias y de integración se realizan utilizando el comando `php artisan test`. Este comando ejecuta todas las pruebas que se encuentren en el directorio `tests`, pero podemos especificar qué pruebas ejecutar según nuestras necesidades.*

## **Comandos Básicos para Ejecutar Pruebas**

* **Ejecutar todas las pruebas del proyecto:**

  ```bash
  php artisan test
  ```

  *Este comando ejecutará todas las pruebas que estén dentro de la carpeta `tests`, por defecto en la carpeta `tests/Feature`.*

* **Ejecutar pruebas de un directorio específico:**

  ```bash
  php artisan test tests/Feature/
  ```

  *Al especificar un directorio como `tests/Feature/`, el comando solo ejecutará las pruebas que se encuentren dentro de ese directorio.*

* **Ejecutar una prueba específica:**

  ```bash
  php artisan test tests/Feature/ContactControllerTest.php
  ```

  *Este comando ejecutará una prueba en específico, en este caso el archivo `ContactControllerTest.php`. Es útil cuando quieres probar un solo controlador o funcionalidad.*

### **Rutas de Consola Personalizadas**

*Laravel permite definir comandos personalizados para Artisan en el archivo `routes/console.php`. Este archivo es donde puedes registrar comandos que quieras ejecutar desde la terminal, pero que no son comandos predeterminados de Artisan.*

```php
Artisan::command('custom:command', function () {
    // Customized Logic
})->describe('Command Description');
```

### **Tipos de Pruebas en Laravel**

*Hay dos tipos de pruebas principales en Laravel: **Pruebas de Unidad - Unit Testing:** y **Pruebas de Características - Feature Testing**.*

1. **Pruebas de Unidad (Unit Tests):**

   * *Se utilizan para probar funcionalidades individuales y aisladas del código. Generalmente, prueban métodos específicos dentro de clases.*
   * **Comando para crear una prueba unitaria:**

     ```bash
     php artisan make:test ContactShareControllerTest --unit
     ```

     *Este comando crea una prueba unitaria en la carpeta `tests/Unit` si usas la opción `--unit`.*

2. **Pruebas de Características (Feature Tests):**

   * *Se enfocan en probar la interacción de varias partes del sistema o la integración entre controladores, bases de datos, servicios, etc.*
   * **Comando para crear una prueba de características:**

     ```bash
     php artisan make:test ContactControllerTest
     ```

     *Esto crea una prueba en la carpeta `tests/Feature`, que es la ubicación por defecto.*

### **Diferencia entre Unit Testing y Feature Testing en Laravel:**

1. **Unit Testing:**

   * *Se centra en probar componentes individuales del sistema, como funciones o métodos, de manera aislada, sin depender de otras partes del sistema (base de datos, rutas, etc.).*
   * *No involucra solicitudes HTTP ni interacción con la base de datos (excepto si usas `DatabaseMigrations` o `RefreshDatabase` para preparar el entorno de pruebas).*
   * *Su objetivo es verificar que una pequeña unidad de código funcione como se espera.*

2. **Feature Testing**:

   * *Está diseñado para probar **funcionalidades completas** del sistema, simulando interacciones del usuario, validaciones de entradas, respuestas HTTP y la interacción con la base de datos.*
   * ***Involucra rutas, controladores, respuestas HTTP, bases de datos y otros componentes del sistema** trabajando juntos.*
   * *En este caso, **verificar que un usuario pueda compartir contactos**, que pueda **ver un contacto compartido**, y que **no se pueda compartir un contacto ya compartido** son ejemplos de pruebas de características porque verifican cómo funcionan varias partes del sistema (como el controlador, la base de datos y las rutas).*

### **Configuración del Entorno de Prueba**

*Cuando trabajas con pruebas, es común configurar una base de datos separada para evitar que las pruebas afecten los datos reales de la aplicación. Para ello, se utiliza un archivo `.env.testing`, que tiene las configuraciones específicas para el entorno de prueba.*

1. **Copiar el archivo `.env` a `.env.testing`:**

   ```bash
   cp .env .env.testing
   ```

2. **Modificar el archivo `.env.testing`:**
   *Cambia la base de datos a una base de datos de prueba:*

   ```dotenv
   DB_DATABASE=contacts_app_test
   ```

3. **Crear la base de datos de prueba:**
   *Asegúrate de que la base de datos de prueba exista:*

   ```sql
   CREATE DATABASE contacts_app_test;
   ```

4. **Ejecutar migraciones en el entorno de prueba:**
   *Usa el comando `php artisan migrate` con la opción `--env=testing` para ejecutar las migraciones en la base de datos de prueba:*

   ```bash
   php artisan migrate --env=testing
   ```

   *Esto garantizará que las migraciones se ejecuten en el entorno de prueba y no en el entorno de producción.*

### **Ejemplo de Salida de Migración**

*Al ejecutar las migraciones, verás algo similar a esto en la consola:*

```bash
INFO  Preparing database.  

Creating migration table ............................................................................................. 4ms DONE

INFO  Running migrations.  

2014_10_12_000000_create_users_table ................................................................................. 3ms DONE
2014_10_12_100000_create_password_resets_table ....................................................................... 1ms DONE
2019_05_03_000001_create_customer_columns ............................................................................ 1ms DONE
2019_05_03_000002_create_subscriptions_table ......................................................................... 2ms DONE
2019_05_03_000003_create_subscription_items_table .................................................................... 2ms DONE
2019_08_19_000000_create_failed_jobs_table ........................................................................... 2ms DONE
2019_12_14_000001_create_personal_access_tokens_table ................................................................ 2ms DONE
2025_03_22_030026_create_contacts_table .............................................................................. 3ms DONE
2025_06_18_005935_add_profile_picture_to_contacts_table .............................................................. 1ms DONE
2025_07_12_033208_create_contact_shares_table ........................................................................ 1ms DONE
```

### **Importancia del Entorno de Prueba**

> [!IMPORTANT]
> *Es importante recordar que las pruebas deben ejecutarse en un entorno controlado para evitar que alteren la base de datos real. Al usar el entorno `--env=testing`, Laravel buscará un archivo `.env.testing` y lo usará para las configuraciones de base de datos, asegurando que los datos en producción no se vean afectados.*

### **Ejemplo de Creación de una Prueba**

*Puedes crear una prueba para un controlador como `ContactShareControllerTest` usando el siguiente comando:*

```bash
php artisan make:test ContactShareControllerTest
```

*Esto creará el archivo de prueba en `tests/Feature`. Luego, puedes ejecutar la prueba específica utilizando:*

```bash
php artisan test tests/Feature/ContactShareControllerTest.php
```

### **Consejo:** ***Nunca Fiarse Completamente De Las Pruebas***

*Las pruebas son una herramienta muy útil, pero no garantizan que el código sea completamente libre de errores. Siempre es importante realizar pruebas exhaustivas, incluyendo pruebas manuales y revisión del código, para detectar posibles problemas que las pruebas automáticas podrían pasar por alto.*

---

### **Cómo agregar el grupo `@group`**

*Para etiquetar las pruebas de este archivo, se agregarían las anotaciones `@group` en la parte superior de la clase o antes de cada método de prueba. Aquí te muestro cómo hacerlo:*

**File `app/Http/Controllers/ContactShareController.php`**

```php
<?php

namespace Tests\Feature;

use App\Models\Contact;
use App\Models\User;
use Illuminate\Foundation\Testing\RefreshDatabase;
use Tests\TestCase;

class ContactShareControllerTest extends TestCase
{
    use RefreshDatabase;

    /**
     * @group contact-share
     */
    public function test_authenticated_user_can_share_a_contact_with_another_user()
    {
        $this->withExceptionHandling();
        [$user1, $user2] = User::factory(count: 2)->create();
        $contact = Contact::factory()->createOne(
            attributes: [
                "phone_number" => "123456789",
                "user_id" => $user1->id
            ]
        );

        $response = $this
            ->actingAs(user: $user1)
            ->post(
                uri: route(name: "contacts-shares.store"),
                data: [
                    "contact_email" => $contact->email,
                    "user_email" => $user2->email
                ]
            );

        $this->assertDatabaseCount(table: "contact_shares", count: 1);

        $sharedContacts = $user2->sharedContacts()->first();
        $this->assertTrue(condition: $contact->is(model: $sharedContacts));
    }

    /**
     * @group contact-share
     */
    public function test_user_can_view_a_contact_shared_with_them()
    {
        $this->withExceptionHandling();
        [$user1, $user2] = User::factory(count: 2)->hasContacts(5)->create();

        $contact = $user1->contacts()->first();
        $contact->sharedWithUsers()->attach($user2->id);

        $response = $this->actingAs(user: $user2)
            ->get(
                uri: route(
                    name: "contacts.show",
                    parameters: $contact->id
                )
            );
        $response->assertOk();
    }

    /**
     * @group contact-share
     * @depends test_authenticated_user_can_share_a_contact_with_another_user
     */
    public function test_user_cannot_share_a_contact_that_is_already_shared_with_the_same_user()
    {
        $this->withExceptionHandling();
        [$user1, $user2] = User::factory(count: 2)->hasContacts(5)->create();

        $contact = $user1->contacts()->first();
        $contact->sharedWithUsers()->attach($user2->id);

        $response = $this->actingAs(user: $user1)
            ->post(
                uri: route(
                    name: "contacts-shares.store",
                    parameters: $contact->id
                ),
                data: [
                    "contact_email" => $contact->email,
                    "user_email" => $user2->email
                ]
            );
        $response->assertSessionHasErrors(keys: [
            "contact_email"
        ]);

        $this->assertDatabaseCount(table: "contact_shares", count: 1);
    }
}
```

### **¿Cómo ejecutar las pruebas agrupadas por `contact-share`?**

*Una vez que has etiquetado las pruebas con `@group contact-share`, puedes ejecutar solo esas pruebas de la siguiente manera:*

```bash
php artisan test --group=contact-share
```

*Esto ejecutará únicamente las pruebas que tengan la etiqueta `contact-share`, permitiéndote centrarse en las pruebas relacionadas con el compartir contactos sin ejecutar todas las demás pruebas del proyecto.*

### **Resumen**

* **Agregar la anotación `@group` a tus pruebas:** *Puedes poner `@group contact-share` antes de los métodos de prueba o en la clase si todas las pruebas están relacionadas.*
* **Ejecutar las pruebas agrupadas:** *Usa `php artisan test --group=contact-share` para ejecutar solo las pruebas del grupo específico.*

---

#### **1. Ejecutar todos los tests:**

```bash
php artisan test
```

*Este comando ejecuta todas las pruebas de la aplicación que se encuentran en el directorio `tests`. La salida muestra que todas las pruebas han pasado correctamente:*

**Salida:**

```bash
PASS  Tests\Unit\ExampleTest
  ✓ that true is true

PASS  Tests\Unit\ContactControllerTest
  ✓ authenticated user can store valid contact data
  ✓ store contact fails when required fields are missing or invalid
  ✓ only contact owner can update or delete contact

PASS  Tests\Feature\ContactShareControllerTest
  ✓ authenticated user can share a contact with another user
  ✓ user can view a contact shared with them
  ✓ user cannot share a contact that is already shared with the same user

PASS  Tests\Feature\ExampleTest
  ✓ the application returns a successful response

Tests:  8 passed
Time:   0.33s
```

*En esta salida:*

* **PASS** *significa que todas las pruebas se han ejecutado correctamente y han pasado sin errores.*
* *Cada prueba se muestra con un nombre (por ejemplo, `authenticated user can store valid contact data`) y un `✓` indicando que esa prueba pasó exitosamente.*
* *Al final, se muestra que **8 pruebas pasaron** y el tiempo total de ejecución fue **0.33 segundos**.*

#### **2. Ejecutar pruebas del grupo `contact-share`:**

```bash
php artisan test --group=contact-share
```

*Este comando ejecuta solo las pruebas que están etiquetadas con el grupo `contact-share`. En la salida, puedes ver que las pruebas relacionadas con compartir contactos han pasado:*

**Salida:**

```bash
PASS  Tests\Feature\ContactShareControllerTest
  ✓ authenticated user can share a contact with another user
  ✓ user can view a contact shared with them
  ✓ user cannot share a contact that is already shared with the same user

Tests:  3 passed
Time:   0.19s
```

**En este caso:**

* **PASS** *significa que las pruebas agrupadas bajo el grupo `contact-share` se ejecutaron correctamente.*
* *Se muestra que **3 pruebas pasaron** dentro del grupo `contact-share`, y el tiempo total de ejecución fue **0.19 segundos**.*

#### **3. Ejecutar un grupo no existente (`--group=name`):**

```bash
php artisan test --group=name
```

*Este comando intenta ejecutar pruebas del grupo `name`, pero como no hay ninguna prueba etiquetada con ese grupo, la salida es la siguiente:*

**Salida:**

```bash
No tests executed! 

Time:   0.00s
```

**Explicación:**

* **No tests executed!** *significa que no se encontraron pruebas para ejecutar en el grupo `name`. Esto sucede porque no se ha definido ningún grupo de pruebas con el nombre `name`, o no hay ninguna prueba que esté etiquetada con `@group name`.*
* *El tiempo total de ejecución es **0.00 segundos** porque no se ejecutaron pruebas.*

### **Resumen de la salida**

1. **Ejecutar todas las pruebas (`php artisan test`):** *Muestra un resumen de todas las pruebas que han pasado.*
2. **Ejecutar pruebas de un grupo específico (`php artisan test --group=contact-share`):** *Solo ejecuta las pruebas relacionadas con el grupo `contact-share` y muestra cuántas pruebas han pasado en ese grupo.*
3. **Ejecutar un grupo no existente (`php artisan test --group=name`):** *Si el grupo no existe, no se ejecutan pruebas y se muestra un mensaje que indica que no se ejecutaron pruebas.*

### **Solución si ocurre el error de `No tests executed!`**

* *Asegúrate de que las pruebas estén correctamente etiquetadas con `@group` en la parte superior de los métodos de prueba. Por ejemplo:*

  ```php
  /**
   * @group name
   */
  public function test_example()
  {
      // Test code
  }
  ```

---

## **File `tests/Feature/ContactControllerTest.php` (`ContactController`):**

```php
namespace Tests\Unit;
```

* **`namespace Tests\Unit;`:** *Define el espacio de nombres (namespace) de la clase. En este caso, las pruebas pertenecen al espacio de nombres `Tests\Unit`, lo que significa que estas pruebas son unitarias.*

```php
use App\Models\Contact;
use App\Models\User;
use Illuminate\Foundation\Testing\RefreshDatabase;
use Tests\TestCase;
```

* **`use App\Models\Contact;`:** *Importa el modelo `Contact` para usarlo en las pruebas.*
* **`use App\Models\User;`:** *Importa el modelo `User` para crear usuarios en las pruebas.*
* **`use Illuminate\Foundation\Testing\RefreshDatabase;`:** *Trae el trait `RefreshDatabase`, que se usa para reiniciar la base de datos después de cada prueba, asegurando que no haya datos persistentes entre las pruebas.*
* **`use Tests\TestCase;`:** *Importa la clase base `TestCase`, de la cual heredan todas las pruebas en Laravel. Esta clase proporciona métodos útiles para las pruebas.*

```php
class ContactControllerTest extends TestCase
{
  use RefreshDatabase;
```

* **`class ContactControllerTest extends TestCase`:** *Define la clase de pruebas para el controlador `ContactController`.*
* **`use RefreshDatabase;`:** *Utiliza el trait `RefreshDatabase`, que restablece la base de datos después de cada prueba, para asegurarse de que las pruebas no afecten a los datos entre sí.*

### *Primer test: **`test_authenticated_user_can_store_valid_contact_data`***

```php
public function test_authenticated_user_can_store_valid_contact_data()
{
  $this->withExceptionHandling();
```

* **`public function test_authenticated_user_can_store_valid_contact_data()`:** *Define el método de prueba, que verifica que un usuario autenticado puede almacenar datos válidos de un contacto.*
* **`$this->withExceptionHandling();`:** *Habilita el manejo de excepciones en la prueba. Esto permite ver los errores generados durante la prueba (si ocurren).*

```php
$user = User::factory()->create();
$contact = Contact::factory()->makeOne(
  attributes: [
      "phone_number" => "123456789",
      "user_id" => $user->id
  ]
);
```

* **`$user = User::factory()->create();`:** *Crea un usuario utilizando la fábrica de modelos (`User::factory()`) y lo persiste en la base de datos.*
* **`$contact = Contact::factory()->makeOne(...);`:** *Crea un contacto usando la fábrica del modelo `Contact` pero **no lo guarda en la base de datos**. Solo se crea el objeto de contacto con los atributos proporcionados.*

```php
$response = $this->actingAs(user: $user)->post(
  uri: route(name: "contacts.store"),
  data: $contact->getAttributes(),
  headers: []
);
```

* **`$this->actingAs(user: $user)`:** *Simula que las solicitudes HTTP se hacen con el usuario autenticado `$user`. Esto es necesario para simular que el usuario está logueado.*
* **`$this->post(...)`:** *Realiza una solicitud POST al `route("contacts.store")`, que corresponde a la ruta de almacenamiento de contactos (`contacts.store`). Los datos del contacto se envían en el cuerpo de la solicitud (`$contact->getAttributes()`), que devuelve un array con los atributos del modelo de contacto.*

```php
$response->assertRedirect(
    uri: route(name: "home")
);
```

* **`$response->assertRedirect(route(name: "home"));`:** *Verifica que la respuesta de la solicitud es una redirección a la ruta `home`, lo que indica que el contacto se ha guardado correctamente y el usuario ha sido redirigido a la página de inicio.*

```php
$this->assertDatabaseCount(table: "contacts", count: 1);
```

* **`$this->assertDatabaseCount(table: "contacts", count: 1);`:** *Verifica que la tabla `contacts` ahora tiene **1 registro**, lo que confirma que el contacto ha sido guardado en la base de datos.*

```php
  $this->assertDatabaseHas(
      table: "contacts",
      data: [
          "user_id" => $user->id,
          "name" => $contact->name,
          "email" => $contact->email,
          "age" => $contact->age,
          "phone_number" => $contact->phone_number
      ]
  );
}
```

* **`$this->assertDatabaseHas()`:** *Verifica que la tabla `contacts` contiene un registro con los datos esperados (el `user_id`, `name`, `email`, `age`, y `phone_number` del contacto que hemos creado).*

### *Segundo test: **`test_store_contact_fails_when_required_fields_are_missing_or_invalid`***

```php
public function test_store_contact_fails_when_required_fields_are_missing_or_invalid()
{
    $this->withExceptionHandling();
    $user = User::factory()->create();
    $contact = Contact::factory()->makeOne(
        attributes: [
            "phone_number" => "Wrong Phone Number",
            "email" => "Wrong Email",
            "name" => null,
        ]
    );
```

* *Este test comprueba que, cuando se envían datos inválidos (como un número de teléfono incorrecto, un correo incorrecto o un campo `name` nulo), la solicitud de guardar un contacto falla.*

```php
$response = $this->actingAs(user: $user)->post(
  uri: route(name: "contacts.store"),
  data: $contact->getAttributes(),
  headers: []
);
```

* *Aquí se realiza una solicitud POST al mismo endpoint de almacenamiento de contactos, pero con datos inválidos.*

```php
$response->assertSessionHasErrors(keys: [
    "phone_number",
    "email",
    "name"
]);
```

* **`$response->assertSessionHasErrors()`:** *Verifica que la respuesta contiene errores de validación en los campos `phone_number`, `email` y `name`, indicando que la solicitud falló debido a los datos inválidos.*

```php
  $this->assertDatabaseCount(table: "contacts", count: 0);
}
```

* **`$this->assertDatabaseCount(table: "contacts", count: 0);`:** *Verifica que no se haya creado ningún contacto en la base de datos, ya que los datos eran inválidos.*

### *Tercer test: **`test_only_contact_owner_can_update_or_delete_contact`***

```php
public function test_only_contact_owner_can_update_or_delete_contact()
{
  $this->withExceptionHandling();
  [$owner, $notOwner] = User::factory(count: 2)->create();
```

* *Este test verifica que solo el propietario del contacto pueda actualizar o eliminar el contacto. Aquí, **`[$owner, $notOwner]`** crea dos usuarios: uno es el propietario del contacto y el otro no lo es.*

```php
$contact = Contact::factory()->createOne(
    attributes: [
        "phone_number" => "123456789",
        "user_id" => $owner->id
    ]
);
```

* *Crea un contacto asociado con el **propietario** (el usuario `$owner`).*

```php
$response = $this->actingAs(user: $notOwner)->put(
    uri: route(name: "contacts.update", parameters: $contact->id),
    data: $contact->getAttributes(),
    headers: []
);
```

* *Aquí, simula que el usuario que no es el propietario intenta **actualizar** el contacto. Se espera que esta operación falle.*

```php
$response->assertForbidden();
```

* **`$response->assertForbidden();`:** *Verifica que la respuesta sea **403 Forbidden**, lo que indica que el usuario no tiene permisos para actualizar el contacto.*

```php
$response = $this->actingAs(user: $notOwner)->delete(
  uri: route(name: "contacts.destroy", parameters: $contact->id),
  data: $contact->getAttributes(),
  headers: []
);
```

* *Simula que el usuario no propietario intenta **eliminar** el contacto.*

```php
  $response->assertForbidden();
}
```

* *Verifica que la respuesta sea también **403 Forbidden**, indicando que no tiene permisos para eliminar el contacto.*

---

### **Resumen:**

*Este conjunto de pruebas está diseñado para verificar el funcionamiento correcto de las funcionalidades de almacenamiento, validación y permisos en el controlador `ContactController`. Se realizan pruebas para asegurar que:*

1. *Un usuario autenticado puede almacenar datos válidos de contacto.*
2. *El sistema rechaza los datos de contacto inválidos.*
3. *Solo el propietario de un contacto puede actualizar o eliminar ese contacto.*

*El uso de métodos como `assertRedirect`, `assertDatabaseCount`, `assertSessionHasErrors`, y `assertForbidden` ayuda a validar tanto la lógica del negocio como la integridad de la base de datos.*

---

### **Sintaxis de Desempaquetado en PHP (Desestructuración de un arreglo)**

```php
[$owner, $notOwner] = User::factory(count: 2)->create();
```

### **¿Qué significa esta línea?**

1. **`User::factory(count: 2)->create();`**:

   * *Aquí se utiliza la **fábrica de modelos** (`User::factory`) para crear **2 usuarios** en la base de datos. La función `create()` persiste esos usuarios en la base de datos y los devuelve como una colección de objetos.*
   * **`count: 2`** *indica que se crearán dos usuarios.*

2. **Desempaquetado de un arreglo (Array Destructuring)**:

   * *PHP permite asignar los elementos de un **array** o **colección** a variables individuales utilizando una sintaxis llamada "desempaquetado" o **array destructuring**.*
   * **`[$owner, $notOwner]`** *es una forma de desempaquetar el **array** (o colección) que se devuelve de `create()` y asignar el primer elemento a `$owner` y el segundo a `$notOwner`.*

   *Este es un ejemplo clásico de desestructuración en PHP, que permite asignar directamente valores de un array a variables, sin tener que acceder a cada índice del array manualmente.*

### **¿Por qué se permite esta sintaxis?**

*La sintaxis de desestructuración en PHP fue introducida en **PHP 7.1** y permite asignar valores de un array o un objeto iterable (como una colección) a variables de manera directa. En tu caso:*

* *`User::factory(count: 2)->create()` devuelve un **array** o **colección** de dos usuarios.*
* *La sintaxis `[$owner, $notOwner]` asigna el primer elemento del array a la variable `$owner` y el segundo elemento a la variable `$notOwner`.*

*Este es un ejemplo de desestructuración, una forma concisa de asignar valores de un array a variables individuales.*

### **Ejemplo más claro:**

*Supongamos que `User::factory(count: 2)->create()` devuelve un arreglo con dos usuarios, por ejemplo:*

```php
$users = [
  User::make(['id' => 1, 'name' => 'Joker']),
  User::make(['id' => 2, 'name' => 'Batman'])
];
```

*Entonces, con esta línea:*

```php
[$owner, $notOwner] = $users;
```

*Se está haciendo lo siguiente:*

* **`$owner`** *toma el primer elemento de `$users`, que sería el primer usuario (id: 1, nombre: 'Joker').*
* **`$notOwner`** *toma el segundo elemento de `$users`, que sería el segundo usuario (id: 2, nombre: 'Batman').*

*En resumen, **`[$owner, $notOwner] = User::factory(count: 2)->create();`** desempaqueta la colección de usuarios devuelta por la fábrica de modelos, asignando el primer usuario a `$owner` y el segundo a `$notOwner`.*

### **¿Por qué es útil esto?**

*La desestructuración es útil cuando necesitas trabajar con varios valores que vienen en un array o colección. Te permite asignar estos valores directamente a variables con nombres más significativos, en lugar de acceder a cada elemento usando índices numéricos (como `$users[0]` o `$users[1]`).*

### **Conclusión:**

* *La línea **`[$owner, $notOwner] = User::factory(count: 2)->create();`** es válida porque se está utilizando la sintaxis de desestructuración para asignar los dos usuarios creados a las variables `$owner` y `$notOwner`.*
* *Es una forma más limpia y eficiente de asignar los valores de un array a variables, sin necesidad de hacer `$users[0]` y `$users[1]`.*

---

### **File `tests/Feature/ContactShareControllerTest.php` (`ContactShareControllerTest`)**

### **1. Configuración:**

```php
namespace Tests\Feature;

use App\Models\Contact;
use App\Models\User;
use Illuminate\Foundation\Testing\RefreshDatabase;
use Tests\TestCase;
```

* **`namespace Tests\Feature;`:** *Define el espacio de nombres para esta clase de pruebas. `Feature` se utiliza generalmente para pruebas que verifican la funcionalidad de las rutas y la interacción de los controladores.*
* **`use App\Models\Contact;`:** *Importa el modelo `Contact` para interactuar con los contactos dentro de las pruebas.*
* **`use App\Models\User;`:** *Importa el modelo `User` para interactuar con los usuarios en las pruebas.*
* **`use Illuminate\Foundation\Testing\RefreshDatabase;`:** *Utiliza el trait `RefreshDatabase` que asegura que la base de datos se reinicie después de cada prueba, lo que garantiza que las pruebas sean independientes y no afecten los datos entre sí.*
* **`use Tests\TestCase;`:** *Importa la clase base `TestCase` de Laravel, de la cual todas las pruebas deben heredar.*

### **2. Clase `ContactShareControllerTest`**

```php
class ContactShareControllerTest extends TestCase
{
    use RefreshDatabase;
```

* *La clase **`ContactShareControllerTest`** hereda de `TestCase` y utiliza el trait `RefreshDatabase`, lo que garantiza que se reinicie la base de datos entre cada prueba.*

### **3. Prueba 1: Un usuario autenticado puede compartir un contacto con otro usuario**

```php
/**
 * @group contact-share
 */
public function test_authenticated_user_can_share_a_contact_with_another_user()
{
    $this->withExceptionHandling();
    [$user1, $user2] = User::factory(count: 2)->create();
    $contact = Contact::factory()->createOne(
        attributes: [
            "phone_number" => "123456789",
            "user_id" => $user1->id
        ]
    );

    $response = $this
        ->actingAs(user: $user1)
        ->post(
            uri: route(name: "contacts-shares.store"),
            data: [
                "contact_email" => $contact->email,
                "user_email" => $user2->email
            ]
        );

    $this->assertDatabaseCount(table: "contact_shares", count: 1);

    $sharedContacts = $user2->sharedContacts()->first();
    $this->assertTrue(condition: $contact->is(model: $sharedContacts));
}
```

* **`@group contact-share`:** *Etiqueta esta prueba con el grupo `contact-share` para que puedas ejecutar solo las pruebas de este grupo con `php artisan test --group=contact-share`.*
* **`$this->withExceptionHandling();`:** *Permite manejar y mostrar las excepciones durante la prueba, lo que es útil para depurar.*
* **`[$user1, $user2] = User::factory(count: 2)->create();`:** *Crea dos usuarios usando la fábrica de usuarios (`User::factory()`).*
* **`$contact = Contact::factory()->createOne([...]);`:** *Crea un contacto con un número de teléfono y asignado al primer usuario (`$user1`).*
* **`$this->actingAs(user: $user1)`:** *Establece que la solicitud se realizará como si `$user1` estuviera autenticado.*
* **`$this->post(...)`:** *Realiza una solicitud POST al endpoint `contacts-shares.store`, que es responsable de compartir el contacto. Los datos enviados incluyen el correo del contacto y el correo del segundo usuario.*
* **`$this->assertDatabaseCount(table: "contact_shares", count: 1);`:** *Verifica que la tabla `contact_shares` tenga exactamente 1 registro, confirmando que el contacto ha sido compartido correctamente.*
* **`$sharedContacts = $user2->sharedContacts()->first();`:** *Obtiene el primer contacto compartido con `$user2`.*
* **`$this->assertTrue(condition: $contact->is(model: $sharedContacts));`:** *Verifica que el contacto original de `$user1` está efectivamente en los contactos compartidos de `$user2`.*

### **4. Prueba 2: Un usuario puede ver un contacto que le ha sido compartido**

```php
/**
 * @group contact-share
 */
public function test_user_can_view_a_contact_shared_with_them()
{
    $this->withExceptionHandling();
    [$user1, $user2] = User::factory(count: 2)->hasContacts(5)->create();

    $contact = $user1->contacts()->first();
    $contact->sharedWithUsers()->attach($user2->id);

    $response = $this->actingAs(user: $user2)
        ->get(
            uri: route(
                name: "contacts.show",
                parameters: $contact->id
            )
        );
    $response->assertOk();
}
```

* **`$user1->contacts()->first();`:** *Obtiene el primer contacto de `$user1`.*
* **`$contact->sharedWithUsers()->attach($user2->id);`:** *Comparte el contacto con `$user2` usando la relación `sharedWithUsers()`.*
* **`$this->actingAs(user: $user2)`:** *Simula que la solicitud se hace como si `$user2` estuviera autenticado.*
* **`$this->get(...)`:** *Realiza una solicitud GET al endpoint `contacts.show`, que muestra el detalle de un contacto. El ID del contacto es pasado como parámetro.*
* **`$response->assertOk();`:** *Verifica que la respuesta de la solicitud es exitosa (código de estado 200).*

### **5. Prueba 3: Un usuario no puede compartir un contacto que ya ha sido compartido con el mismo usuario**

```php
/**
 * @group contact-share
 * @depends test_authenticated_user_can_share_a_contact_with_another_user
 */
public function test_user_cannot_share_a_contact_that_is_already_shared_with_the_same_user()
{
    $this->withExceptionHandling();
    [$user1, $user2] = User::factory(count: 2)->hasContacts(5)->create();

    $contact = $user1->contacts()->first();
    $contact->sharedWithUsers()->attach($user2->id);

    $response = $this->actingAs(user: $user1)
        ->post(
            uri: route(
                name: "contacts-shares.store",
                parameters: $contact->id
            ),
            data: [
                "contact_email" => $contact->email,
                "user_email" => $user2->email
            ]
        );
    $response->assertSessionHasErrors(keys: [
        "contact_email"
    ]);

    $this->assertDatabaseCount(table: "contact_shares", count: 1);
}
```

* **`@depends test_authenticated_user_can_share_a_contact_with_another_user`:** *Esta prueba depende de que la prueba `test_authenticated_user_can_share_a_contact_with_another_user` pase antes de ejecutarse. Laravel ejecutará esta prueba solo si la prueba dependiente pasa correctamente.*
* **`$contact->sharedWithUsers()->attach($user2->id);`:** *Comparte el contacto con `$user2`.*
* **`$this->actingAs(user: $user1)`:** *Realiza la acción como si `$user1` estuviera autenticado.*
* **`$this->post(...)`:** *Intenta compartir el mismo contacto con `$user2` nuevamente.*
* **`$response->assertSessionHasErrors(keys: ["contact_email"])`:** *Verifica que haya un error en el campo `contact_email`, ya que no se puede compartir un contacto con el mismo usuario dos veces.*
* **`$this->assertDatabaseCount(table: "contact_shares", count: 1);`:** *Asegura que el contacto solo ha sido compartido una vez (es decir, no se han creado registros duplicados).*

### **Conclusión**

*Este archivo de prueba contiene tres pruebas que verifican la correcta funcionalidad de la operación de compartir contactos entre usuarios:*

1. **Un usuario autenticado puede compartir un contacto con otro.**
2. **Un usuario puede ver un contacto que le ha sido compartido.**
3. **Un usuario no puede compartir un contacto que ya ha sido compartido con el mismo usuario.**
