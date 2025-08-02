<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# **Patrón MVC - Model View Controller**

## **Exploración del comando `make` en Laravel**

*Laravel proporciona el comando `make` dentro de su interfaz de comandos `artisan`, que permite generar diversos archivos para el desarrollo del proyecto. Aunque al ejecutarlo sin argumentos se genera un mensaje de error, su salida nos proporciona una lista de las opciones disponibles:*

```bash
php artisan make --help
```

**Salida esperada:**

```bash
   ERROR  Command "make" is not defined. Did you mean one of these?

  ⇂ make:cast
  ⇂ make:channel
  ⇂ make:command
  ⇂ make:component
  ⇂ make:controller
  ⇂ make:event
  ⇂ make:exception
  ⇂ make:factory
  ⇂ make:job
  ⇂ make:listener
  ⇂ make:mail
  ⇂ make:middleware
  ⇂ make:migration
  ⇂ make:model
  ⇂ make:notification
  ⇂ make:observer
  ⇂ make:policy
  ⇂ make:provider
  ⇂ make:request
  ⇂ make:resource
  ⇂ make:rule
  ⇂ make:scope
  ⇂ make:seeder
  ⇂ make:test
```

*La opción que nos interesa aquí es `make:migration`, que nos permite generar archivos de migraciones de base de datos.*

## **Uso del comando `make:migration`**

**Para ver los detalles de este comando, ejecutamos:**

```bash
php artisan make:migration --help
```

**Salida esperada:**

```bash
Description:
  Create a new migration file

Usage:
  make:migration [options] [--] <name>

Arguments:
  name                   The name of the migration

Options:
      --create[=CREATE]  The table to be created
      --table[=TABLE]    The table to migrate
      --path[=PATH]      The location where the migration file should be created
      --realpath         Indicate any provided migration file paths are pre-resolved absolute paths
      --fullpath         Output the full path of the migration (Deprecated)
  -h, --help             Display help for the given command. When no command is given display help for the list command
  -q, --quiet            Do not output any message
  -V, --version          Display this application version
      --ansi|--no-ansi   Force (or disable --no-ansi) ANSI output
  -n, --no-interaction   Do not ask any interactive question
      --env[=ENV]        The environment the command should run under
  -v|vv|vvv, --verbose   Increase the verbosity of messages: 1 for normal output, 2 for more verbose output and 3 for debug
```

### **Explicación de los parámetros clave:**

- **`name`:** *Nombre de la migración.*
- **`--create=TABLE`:** *Especifica que la migración creará una nueva tabla.*
- **`--table=TABLE`:** *Indica que la migración modificará una tabla existente.*
- **`--path=PATH`:** *Permite especificar la ubicación donde se guardará el archivo de migración.*
- **`-v|vv|vvv`:** *Aumenta la verbosidad de la salida, proporcionando diferentes niveles de información.*

## **Monitoreo de cambios en los archivos de migración**

*Antes de ejecutar el comando `make:migration`, podemos instalar la herramienta `procps` para monitorear archivos en tiempo real:*

```bash
apt install procps -y
```

*Luego, en una terminal separada, ejecutamos el siguiente comando para observar los cambios en la carpeta de migraciones:*

```bash
watch -n 1 lsd -lAh
```

*Salida esperada antes de crear la nueva migración:*

```bash
.rw-r--r-- 1000 1000 793 B Tue Jun  7 15:03:59 2022 2014_10_12_000000_create_users_table.php
.rw-r--r-- 1000 1000 669 B Sun Mar  2 02:49:47 2025 2014_10_12_100000_create_password_resets_table.php
.rw-r--r-- 1000 1000 810 B Tue Jun  7 15:03:59 2022 2019_08_19_000000_create_failed_jobs_table.php
.rw-r--r-- 1000 1000 841 B Tue Jun  7 15:03:59 2022 2019_12_14_000001_create_personal_access_tokens_table.php
```

### **Creación de una migración**

*Ejecutamos el siguiente comando para generar una nueva migración:*

```bash
php artisan make:migration --ansi -vvv create_contacts_table
```

**Salida esperada:**

```bash
   INFO  Migration [database/migrations/2025_03_22_030026_create_contacts_table.php] created successfully.
```

*Salida esperada en `watch -n 1 lsd -lAh` después de crear la migración:*

```bash
.rw-r--r-- 1000 1000 793 B Tue Jun  7 15:03:59 2022 2014_10_12_000000_create_users_table.php
.rw-r--r-- 1000 1000 669 B Sun Mar  2 02:49:47 2025 2014_10_12_100000_create_password_resets_table.php
.rw-r--r-- 1000 1000 810 B Tue Jun  7 15:03:59 2022 2019_08_19_000000_create_failed_jobs_table.php
.rw-r--r-- 1000 1000 841 B Tue Jun  7 15:03:59 2022 2019_12_14_000001_create_personal_access_tokens_table.php
.rw-r--r-- root root 575 B Sat Mar 22 03:00:26 2025 2025_03_22_030026_create_contacts_table.php
```

*Como podemos ver, se creó el archivo `2025_03_22_030026_create_contacts_table.php` en la siguiente ruta:*

```bash
ApplicationLaravel/database/migrations/2025_03_22_030026_create_contacts_table.php
```

*Laravel utiliza este formato de nombres para las migraciones: `YYYY_MM_DD_HHMMSS_name_migration.php`, donde:*

- *`YYYY_MM_DD` representa la fecha en que se creó.*
- *`HHMMSS` es una marca de tiempo única.*
- *`name_migration` es el nombre asignado al comando.*

*De esta manera, Laravel permite mantener un orden cronológico de las migraciones y facilita la gestión de cambios en la base de datos.*

---

### **Contenido del archivo generado por Laravel para la migración**

*El archivo de migración generado por el comando `php artisan make:migration` es el siguiente:*

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

#### **Explicación detallada de cada parte del archivo:**

1. **`use Illuminate\Database\Migrations\Migration;`**
   - *Este `use` importa la clase `Migration` que Laravel proporciona. Esta clase es la base para crear migraciones en Laravel, lo que permite crear, modificar o eliminar tablas de la base de datos de manera estructurada.*

2. **`use Illuminate\Database\Schema\Blueprint;`**
   - *Se importa la clase `Blueprint`, que permite definir las columnas y las propiedades de la tabla en las migraciones.*

3. **`use Illuminate\Support\Facades\Schema;`**
   - *Esta línea importa el facade `Schema`, que es la herramienta principal que utilizamos para definir y manipular las estructuras de las tablas en la base de datos.*

4. **`return new class extends Migration`**
   - *Aquí estamos creando una clase anónima que extiende la clase `Migration`. Este es un patrón común en Laravel para definir migraciones sin la necesidad de declarar explícitamente una clase.*

5. **Método `up()`**
   - **`public function up()`:** *Este método es responsable de definir qué cambios se realizarán en la base de datos. En este caso, estamos creando una tabla llamada `contacts`.*
   - **`Schema::create('contacts', function (Blueprint $table) {...})`:** *Este es el comando que crea la tabla `contacts` en la base de datos. Dentro de la función, se definen las columnas de la tabla.*
   - **`$table->id();`:** *Esto agrega una columna `id` como clave primaria de la tabla. Laravel automáticamente asigna un valor autoincrementable para esta columna.*
   - **`$table->timestamps();`:** *Esto agrega dos columnas: `created_at` y `updated_at`, que son gestionadas automáticamente por Laravel. Son útiles para saber cuándo se creó y cuándo se actualizó un registro en la tabla.*

6. **Método `down()`**
   - **`public function down()`:** *Este método se ejecuta cuando deseas revertir los cambios realizados por la migración. En este caso, el comando **`Schema::dropIfExists('contacts');`** eliminará la tabla `contacts` si existe.*
   - *Es importante tener este método para permitir revertir migraciones de forma segura si se desea deshacer cambios en el proyecto.*

### **Modificación del archivo de migración:**

*Ahora vamos a modificar el archivo para añadir más columnas a la tabla `contacts`:*

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
            $table->id(); // Agrega una columna `id` autoincrementable
            $table->string("name"); // Agrega una columna `name` de tipo string
            $table->string("phone_number"); // Agrega una columna `phone_number` de tipo string
            $table->timestamps(); // Agrega las columnas `created_at` y `updated_at`
        });
    }

    /**
     * Reverse the migrations.
     *
     * @return void
     */
    public function down()
    {
        Schema::dropIfExists('contacts'); // Elimina la tabla `contacts` si existe
    }
};
```

#### **Explicación de las nuevas columnas añadidas:**

1. **`$table->string("name");`**
   - *Esta línea crea una columna llamada `name` de tipo `string`. En Laravel, `string` generalmente es un alias para una columna de tipo `VARCHAR` en SQL, y por defecto se le asigna una longitud de 255 caracteres.*
   - *Esta columna se utilizará para almacenar el nombre del contacto.*

2. **`$table->string("phone_number");`**
   - *Similar a la columna `name`, esta línea crea una columna llamada `phone_number` también de tipo `string`, y se utilizará para almacenar el número de teléfono del contacto.*

### **Qué sucede cuando ejecutamos esta migración**

*Cuando ejecutas el comando `php artisan migrate`, Laravel ejecuta el método `up()` de esta migración. La tabla `contacts` se crea con las columnas `id`, `name`, `phone_number`, `created_at`, y `updated_at`. Estos campos ahora están disponibles en la base de datos para almacenar información sobre los contactos.*

*En cuanto revertimos la migración con el comando `php artisan migrate:rollback`, Laravel ejecutará el método `down()` y eliminará la tabla `contacts`, dejándola como estaba antes de la migración.*

---

### **¿Por qué es importante el uso de migraciones?**

*Las migraciones permiten a los desarrolladores definir la estructura de la base de datos de forma programática, asegurando que todos los entornos de desarrollo, prueba y producción tengan la misma estructura de base de datos sin la necesidad de realizar cambios manuales. Además, las migraciones son versionadas, lo que facilita la reversión de cambios o la aplicación de nuevas modificaciones a lo largo del tiempo.*

### **Más recursos:**

- *[Documentación oficial de Migraciones en Laravel](https://laravel.com/docs/12.x/migrations "https://laravel.com/docs/12.x/migrations")*

### **Nombre de la migración y su interpretación**

> [!IMPORTANT]
> *La razón por la que Laravel sabe que la tabla debe llamarse `contacts` es debido a cómo se interpreta el nombre de la migración que generaste*

- **Comando para crear una migracion en Laravel**

```bash
php artisan make:migration --ansi -vvv create_contacts_table
```

**Laravel crea una migración con el nombre **`create_contacts_table`**. Laravel sigue una convención de nomenclatura para las migraciones.**

- *El **prefijo `create_`** indica que esta migración se utiliza para **crear una tabla**.*
- *El **nombre `contacts`** hace referencia al nombre de la tabla que deseas crear.*
- *El **sufijo `_table`** es una convención comúnmente usada para indicar que la migración crea una tabla (aunque no es obligatorio).*

*Así que cuando Laravel ve la migración con el nombre `create_contacts_table`, **asume que quieres crear una tabla llamada `contacts`**.*

### **Cómo Laravel genera la tabla**

*Cuando ejecutas la migración con `php artisan migrate`, Laravel interpreta que la migración debe crear una tabla llamada `contacts` porque ese es el nombre de la migración. El prefijo `create_` sugiere la acción de "crear", y el nombre `contacts` será usado como el nombre de la tabla.*

*Es importante destacar que si hubieras nombrado la migración de forma diferente, como `create_users_table`, Laravel intentaría crear una tabla llamada `users`.*

### **Cómo funciona el código**

*En la migración, cuando usas `Schema::create('contacts', function (Blueprint $table) {...})`, Laravel ya sabe que debes crear la tabla `contacts` por la convención de nombre que definimos en la migración. El nombre `contacts` se pasa explícitamente al método `create()` y es el nombre de la tabla que se va a crear en la base de datos.*

- **Resumen**

- **Convención de Laravel:** *Cuando usas el nombre `create_contacts_table`, Laravel sabe que es una migración para crear la tabla `contacts`.*
- **Método `Schema::create()`:** *El primer argumento que le pasas al método `create()` (en este caso, `'contacts'`) es el nombre de la tabla que deseas crear.*

*Este es el proceso detrás de la magia que Laravel maneja en segundo plano para facilitar el trabajo con migraciones.*

---

### **Ejecutamos la migración**

*El comando para ejecutar las migraciones es:*

```bash
php artisan migrate
```

**Salida del comando:**

```bash
php artisan migrate

   INFO  Running migrations.

  2019_12_14_000001_create_personal_access_tokens_table ................................................................................. 27ms DONE
  2025_03_22_030026_create_contacts_table ................................................................................................ 6ms DONE
```

#### **Explicación de la salida:**

1. **`INFO Running migrations.`**
   - *Esto es simplemente un mensaje informativo que indica que Laravel está comenzando a ejecutar las migraciones definidas en el proyecto.*

2. **`2019_12_14_000001_create_personal_access_tokens_table`:**
   - *Aquí vemos el nombre de una migración que ya se ha ejecutado. El nombre de la migración sigue el formato `YYYY_MM_DD_HHMMSS_name_of_migration`. En este caso, es una migración que crea una tabla llamada `personal_access_tokens`.*
   - *El `27ms` indica el tiempo que tardó en ejecutarse esta migración, en este caso, 27 milisegundos.*

3. **`2025_03_22_030026_create_contacts_table`:**
   - *Similar a la migración anterior, esta migración crea la tabla `contacts`. El tiempo de ejecución es de `6ms`.*

4. **`DONE`:**
   - *Esta palabra indica que la migración se ejecutó correctamente y que las tablas se crearon o modificaron según lo especificado en las migraciones.*

#### **Aclaración:**

- **`Schema`** *no es un ORM. El `Schema` es una herramienta proporcionada por Laravel para definir la estructura de la base de datos (crear tablas, agregar columnas, etc.) sin tener que escribir SQL manualmente.*
- **`ORM` (Eloquent)** *es el sistema de Laravel para interactuar con la base de datos usando modelos, sin necesidad de escribir consultas SQL directamente.*

---

### **Comando `make:model`**

*El siguiente comando se usa para crear un **modelo de Eloquent:***

```bash
php artisan make:model --help
```

*Salida del comando:*

```bash
Description:
  Create a new Eloquent model class

Usage:
  make:model [options] [--] <name>

Arguments:
  name                  The name of the model

Options:
  -a, --all             Generate a migration, seeder, factory, policy, resource controller, and form request classes for the model
  -c, --controller      Create a new controller for the model
  -f, --factory         Create a new factory for the model
      --force           Create the class even if the model already exists
  -m, --migration       Create a new migration file for the model
      --morph-pivot     Indicates if the generated model should be a custom polymorphic intermediate table model
      --policy          Create a new policy for the model
  -s, --seed            Create a new seeder for the model
  -p, --pivot           Indicates if the generated model should be a custom intermediate table model
  -r, --resource        Indicates if the generated controller should be a resource controller
      --api             Indicates if the generated controller should be an API resource controller
  -R, --requests        Create new form request classes and use them in the resource controller
      --test            Generate an accompanying PHPUnit test for the Model
      --pest            Generate an accompanying Pest test for the Model
  -h, --help            Display help for the given command. When no command is given display help for the list command
  -q, --quiet           Do not output any message
  -V, --version         Display this application version
      --ansi|--no-ansi  Force (or disable --no-ansi) ANSI output
  -n, --no-interaction  Do not ask any interactive question
      --env[=ENV]       The environment the command should run under
  -v|vv|vvv, --verbose  Increase the verbosity of messages: 1 for normal output, 2 for more verbose output and 3 for debug
```

#### **Explicación de las opciones del comando `make:model`:**

1. **`-a, --all`:** *Genera no solo el modelo, sino también:*
   - *Una migración para crear la tabla en la base de datos.*
   - *Un seeder para poblar la tabla con datos.*
   - *Una fábrica para crear instancias del modelo de manera sencilla.*
   - *Una política para controlar el acceso.*
   - *Un controlador de recursos (resource controller).*
   - *Un formulario de solicitud (form request) para validar los datos de entrada.*

2. **`-c, --controller`:** *Crea un **controlador** para el modelo. Los controladores manejan la lógica para interactuar con el modelo y la vista.*

3. **`-f, --factory`:** *Crea una **fábrica** para el modelo. Las fábricas son muy útiles para generar datos de prueba para las pruebas unitarias.*

4. **`--force`:** *Si el modelo ya existe, creará el archivo del modelo nuevamente, sobrescribiéndolo.*

5. **`-m, --migration`:** *Genera una migración automáticamente para el modelo. Esto es útil para crear la tabla correspondiente en la base de datos con la estructura de columnas adecuadas.*

6. **`--morph-pivot`:** *Indica que el modelo generado será para una tabla de **relación polimórfica** intermedia (pivot table).*

7. **`-s, --seed`:** *Crea un **seeder** para el modelo. Un seeder es útil para insertar datos de prueba en la base de datos.*

8. **`-p, --pivot`:** *Indica que el modelo generado será un **modelo de tabla intermedia personalizada**.*

9. **`-r, --resource`:** *Genera un **controlador de recursos**, que sigue la convención RESTful para manejar las operaciones CRUD (crear, leer, actualizar, eliminar).*

10. **`--test`:** *Crea una prueba **PHPUnit** para el modelo. Las pruebas ayudan a asegurar que el modelo y sus métodos funcionen correctamente.*

11. **`--pest`:** *Crea una prueba utilizando **Pest**, una herramienta moderna para pruebas unitarias en PHP.*

---

### **Creación del Modelo `Contact`**

**Ahora, ejecutamos el siguiente comando para crear el modelo `Contact`:**

```bash
php artisan make:model Contact
```

**Salida del comando:**

```bash
php artisan make:model Contact

   INFO  Model [app/Models/Contact.php] created successfully.
```

*Esto indica que el modelo `Contact` se ha creado correctamente en la ruta **`app/Models/Contact.php`**.*

#### **Verificación del archivo creado:**

*Ejecutamos el comando `lsd` para verificar que el archivo se haya creado:*

```bash
lsd -lh app/Models/Contact.php
.rw-r--r-- root root 178 B Sat Mar 22 03:13:33 2025  app/Models/Contact.php
```

**Luego, utilizamos `cat` para ver el contenido del archivo:**

```bash
cat app/Models/Contact.php
```

**El contenido del archivo generado es:**

```php
<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Contact extends Model
{
    use HasFactory;
}
```

#### **Explicación del contenido del archivo:**

1. **`namespace App\Models;`:**
   - *Define el **espacio de nombres** para el modelo `Contact`. En este caso, está dentro del espacio de nombres `App\Models`, lo que significa que el modelo reside en la carpeta `app/Models`.*

2. **`use Illuminate\Database\Eloquent\Factories\HasFactory;`:**
   - *Esta línea importa el trait `HasFactory`, que permite que el modelo utilice **fábricas** para crear instancias del modelo con datos de prueba fácilmente.*

3. **`use Illuminate\Database\Eloquent\Model;`:**
   - *Importa la clase base `Model` de Eloquent. Esta es la clase que todos los modelos en Laravel extienden para interactuar con la base de datos.*

4. **`class Contact extends Model`:**
   - *Define la clase `Contact`, que extiende de `Model`. Esto significa que la clase `Contact` es un **modelo Eloquent**, lo que le permite interactuar con la base de datos de manera sencilla.*

5. **`use HasFactory;`:**
   - **Aquí se está utilizando el trait `HasFactory`, lo que permite usar fábricas para generar datos del modelo de manera sencilla.**

---

### **Ruta POST para almacenar un contacto**

```php
Route::post(
    "/contact",
    function (Request $request) {
        $data = $request->all();

        $contact = new Contact();
        $contact->name = $data["name"]; // Explicación: el modelo 'Contact' tiene un atributo 'name' porque lo definimos como un campo de tipo string en la migración.
        $contact->phone_number = $data["phone_number"]; // Explicación: el modelo 'Contact' tiene un atributo 'phone_number' porque lo definimos como un campo de tipo string en la migración.
        $contact->save();

        return Response::json(
            ["message" => "Contact Stored"],
            200
        );
    }
);
```

#### **Explicación detallada:**

1. **`Route::post("/contact", function(Request $request) {...});`:**
   - *Este es un **manejador de ruta POST**. En Laravel, `Route::post` se utiliza para definir una ruta que manejará solicitudes HTTP de tipo **POST**. En este caso, la ruta es `/contact`, que se encargará de recibir los datos de un contacto y almacenarlos en la base de datos.*
   - *El **`function(Request $request)`** es un **closure** (función anónima) que Laravel ejecutará cuando se haga una solicitud POST a la ruta `/contact`. Recibe un objeto `Request`, que contiene todos los datos enviados desde el formulario o cliente.*

2. **`$data = $request->all();`:**
   - *Este comando obtiene **todos los datos** enviados en la solicitud HTTP. La función `all()` devuelve un array con los datos del formulario, como `name` y `phone_number`, que el usuario envió.*

3. **`$contact = new Contact();`:**
   - *Aquí estamos creando una **nueva instancia** del modelo `Contact`. El modelo `Contact` es una **clase Eloquent**, lo que significa que representa una tabla en la base de datos y proporciona métodos para interactuar con esa tabla.*

4. **`$contact->name = $data["name"];`:**
   - *Este paso asigna el valor del campo `name` que fue enviado en la solicitud al atributo `name` del objeto `Contact`.*
   - **Explicación:** *El objeto `$contact` tiene un atributo `name` porque, en la migración que definimos anteriormente, creamos una columna `name` de tipo `string` en la tabla `contacts`.*
   - C*uando el modelo se instancia, automáticamente Laravel mapea las columnas de la tabla a atributos del modelo. En este caso, el atributo `name` en el modelo está vinculado a la columna `name` de la tabla `contacts`.*

5. **`$contact->phone_number = $data["phone_number"];`:**
   - *Similar a la asignación anterior, estamos asignando el valor de `phone_number` (que se encuentra en `$data["phone_number"]`) al atributo `phone_number` del objeto `$contact`.*
   - **Explicación:** *El modelo `Contact` también tiene un atributo `phone_number` porque lo definimos como una columna de tipo `string` en la migración de la tabla `contacts`. Laravel automáticamente asigna este valor a la columna correspondiente cuando se guarda el registro.*

6. **`$contact->save();`:**
   - *Este comando guarda el modelo `$contact` en la base de datos.*
   - **Explicación:** *Como el modelo `Contact` extiende de `Model`, tiene acceso al método `save()`, que insertará (o actualizará) el registro correspondiente en la tabla `contacts`. Laravel maneja la interacción con la base de datos utilizando **Eloquent ORM**, lo que significa que el modelo automáticamente sabe a qué tabla pertenece (en este caso, `contacts`) y qué columnas deben ser guardadas.*

7. **`return Response::json(["message" => "Contact Stored"], 200);`:**
   - *Este comando devuelve una **respuesta JSON** indicando que el contacto se ha almacenado correctamente. El código `200` es el **código de estado HTTP** que significa "OK".*
   - **Explicación:** *Laravel facilita el retorno de respuestas en formato JSON. Esto es útil en aplicaciones **API** y en general cuando se espera que los datos sean procesados por un cliente, como una aplicación de frontend o una aplicación móvil.*

---

### **Realizando la solicitud desde el navegador**

- *Una vez que esta ruta está configurada, podemos enviar una solicitud **POST** a la ruta `/contact` desde un formulario en el navegador o usando herramientas como **Postman** o **cURL**.*

#### **Ejemplo de solicitud:**

- *Supongamos que tenemos un formulario con dos campos: `name` y `phone_number`. Al completar estos campos y hacer clic en **enviar**, se realizará una solicitud POST al servidor con los datos que el usuario proporcionó.*

*La respuesta que veremos en el navegador será:*

```json
{"message": "Contact Stored"}
```

*Este es un **mensaje de éxito** que indica que el contacto se ha guardado correctamente en la base de datos.*

---

### **Verificación de los datos en la base de datos**

**Para verificar que los datos realmente se almacenaron en la base de datos, podemos ejecutar una consulta SQL en el contenedor de Docker donde está ejecutándose PostgreSQL.**

**Ejecutamos el siguiente comando:**

```bash
docker container exec --interactive --tty --user 0:0 --privileged -w / db psql -h localhost -U postgres -p 5432 -d contacts_app -c 'SELECT * FROM contacts';
```

#### **Explicación del comando:**

1. **`docker container exec --interactive --tty --user 0:0 --privileged -w / db`:**
   - *Este comando ejecuta un comando dentro de un contenedor Docker. Específicamente, estamos accediendo al contenedor que ejecuta PostgreSQL (`db`), de manera interactiva (`--interactive`) y con acceso de usuario root (`--user 0:0`).*
   - *`-w /` establece el directorio de trabajo en la raíz del contenedor.*

2. **`psql -h localhost -U postgres -p 5432 -d contacts_app`:**
   - *Esto es para ejecutar **psql**, el cliente de línea de comandos de PostgreSQL, dentro del contenedor. Nos conectamos a la base de datos `contacts_app` en el servidor `localhost` en el puerto `5432` usando el usuario `postgres`.*

3. **`-c 'SELECT * FROM contacts';`:**
   - *Ejecutamos la consulta SQL `SELECT * FROM contacts;` para obtener todos los registros de la tabla `contacts`.*

#### **Resultado de la consulta:**

```sql
 id |  name  | phone_number |     created_at      |     updated_at
----+--------+--------------+---------------------+---------------------
  1 | Daniel | 12345678     | 2025-03-22 03:23:49 | 2025-03-22 03:23:49
(1 row)
```

- *El resultado muestra que se ha **insertado un nuevo contacto** en la tabla `contacts`.*
- *El contacto tiene:*
  - **id:** *1 (el identificador único generado automáticamente).*
  - **name:** *Daniel (el valor del campo `name` que se envió en la solicitud).*
  - **phone_number:** *12345678 (el valor del campo `phone_number` enviado en la solicitud).*
  - **created_at** *y* **updated_at:** *estas columnas se gestionan automáticamente por Laravel utilizando `timestamps()` en la migración, y muestran la fecha y hora en que se creó el registro.*

---

### **¿Cómo sabe Laravel a qué tabla debe guardar los datos?**

*Laravel sabe a qué tabla debe guardar los datos debido a la forma en que está estructurado el modelo Eloquent. **Eloquent** es el ORM (Object Relational Mapping) de*
*Laravel, y sigue una convención muy clara y sencilla que ayuda a Laravel a determinar automáticamente cuál es la tabla asociada a un modelo.*

1. **Convención de nombres:**
   - *Eloquent sigue la convención de que el nombre de la **tabla** está en plural y en minúsculas, basado en el nombre del **modelo**. Por ejemplo:*
     - *Si tienes un modelo llamado `Contact`, Eloquent automáticamente asumirá que la tabla asociada en la base de datos es `contacts` (plural y en minúsculas).*
     - *Si el nombre del modelo fuera `Post`, la tabla asociada sería `posts`.*

   *Esto significa que, de forma predeterminada, Eloquent buscará una tabla llamada **contacts** en la base de datos cuando realices operaciones con el modelo `Contact`.*

2. **¿Y si la tabla no sigue la convención?**  
   *Si por alguna razón quieres que el modelo utilice una tabla con un nombre diferente al que sigue la convención, puedes especificarlo explícitamente en el modelo utilizando la propiedad `$table`.*

   **Ejemplo:**

   ```php
   class Contact extends Model
   {
       protected $table = 'my_custom_name_table';
   }
   ```

   **Con esto, Eloquent sabe que, aunque el nombre del modelo sea `Contact`, los datos deben guardarse en una tabla llamada `my_custom_name_table`.**

3. **Comportamiento automático:**
   - *Una vez que el modelo sabe qué tabla usar, cada vez que llamas a métodos como `save()`, Eloquent usa el nombre de la tabla para interactuar con ella.*
   - *Al hacer `$contact->save()`, Eloquent realiza una inserción en la tabla `contacts` (o en la tabla especificada si se configura un nombre personalizado de tabla).*
   - *Si tienes atributos como `name` y `phone_number` en el modelo, Eloquent automáticamente mapea estos atributos a las **columnas** de la tabla `contacts` (o la que hayas especificado).*

4. **Manejo de claves primarias:**
   - *Laravel asume por defecto que cada modelo tiene una clave primaria llamada `id`. Por ejemplo, el modelo `Contact` asumirá que tiene una columna llamada `id` en la tabla `contacts`, que se utiliza para identificar de manera única cada fila.*
   - *Si deseas usar una clave primaria diferente, puedes indicarlo en el modelo con la propiedad `$primaryKey`.*

   **Ejemplo:**

   ```php
   class Contact extends Model
   {
        protected $primaryKey = 'contact_id';
   }
   ```

---

### **Archivo del Modelo `Contact` con Personalización de Tabla y Clave Primaria**

*El archivo `Contact.php` del modelo quedaría de la siguiente manera:*

```php
<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Contact extends Model
{
    // Usamos el trait HasFactory para permitir la creación de instancias de la clase usando factorías
    use HasFactory;

    // Especificamos el nombre personalizado de la tabla en la base de datos
    protected $table = 'my_custom_name_table';

    // Definimos la clave primaria personalizada, ya que por defecto Laravel usa 'id'
    protected $primaryKey = 'contact_id';
}
```

#### **Explicación:**

- **`protected $table`:** *Esta propiedad se usa para especificar el nombre de la tabla en la base de datos. Laravel, por convención, utiliza el plural y el nombre del modelo en minúsculas, pero si necesitas que el modelo use una tabla diferente, puedes configurarlo manualmente. En este caso, hemos especificado que la tabla asociada al modelo `Contact` se llama `my_custom_name_table`.*

- **`protected $primaryKey`:** *Laravel asume que la clave primaria de cada tabla es `id`. Si en tu caso la tabla utiliza una clave primaria diferente, como `contact_id`, debes definirla explícitamente utilizando esta propiedad. Esto le indica a Laravel que la columna `contact_id` será la clave primaria en la tabla `my_custom_name_table`.*

---

### **Crear la Tabla en PostgreSQL**

*Ahora, para crear la tabla correspondiente en la base de datos, necesitamos ingresar a la base de datos PostgreSQL en el contenedor Docker:*

```bash
docker container exec --interactive --tty --user 0:0 --privileged db psql -h localhost -U postgres -p 5432 -d contacts_app
```

*Este comando te conecta al contenedor `db` y te permite ejecutar comandos SQL dentro de la base de datos `contacts_app`.*

#### **Creación de la Tabla:**

*Una vez dentro de PostgreSQL, ejecutamos el siguiente comando para crear la tabla `my_custom_name_table`:*

```sql
CREATE TABLE my_custom_name_table (
    contact_id int NOT NULL PRIMARY KEY GENERATED ALWAYS AS IDENTITY,  -- Definimos la clave primaria, generada automáticamente.
    name TEXT,  -- Columna 'name' de tipo TEXT
    phone_number INT,  -- Columna 'phone_number' de tipo INTEGER
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Columna 'created_at' para la fecha y hora de creación, con valor por defecto de la hora actual
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- Columna 'updated_at' para la fecha y hora de la última actualización, con valor por defecto de la hora actual
);
```

- **Explicación:**

- **`contact_id int NOT NULL PRIMARY KEY GENERATED ALWAYS AS IDENTITY`:** *Definimos la columna `contact_id` como la clave primaria de la tabla. Utilizamos la opción `GENERATED ALWAYS AS IDENTITY` para hacer que el valor de esta columna se genere automáticamente al insertar un nuevo registro (función similar a `AUTO_INCREMENT` en MySQL).*
- **`name TEXT` y `phone_number INT`:** *Estas son las columnas que almacenarán el nombre y el número de teléfono de cada contacto. Se utiliza `TEXT` para el nombre, lo cual permite almacenar cadenas de texto de longitud variable, y `INT` para el número de teléfono, considerando que es un valor numérico.*
- **`created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP` y `updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP`:** *Estas son las columnas predeterminadas que Laravel usa para manejar las marcas de tiempo de creación y actualización de los registros. Ambas tienen un valor predeterminado que es la fecha y hora actual.*

---

### **Hacer la Petición a través de la Ruta en el Navegador**

*Una vez que tienes la tabla creada y el modelo configurado, puedes hacer una petición HTTP al endpoint que has definido en la ruta de `web.php` para almacenar un nuevo contacto.*

#### **Flujo de la Petición:**

1. *Llenas los campos de `name` y `phone_number` en el formulario del navegador y envías la petición POST a la ruta `/contact`.*
2. *Laravel toma esos datos, crea una nueva instancia del modelo `Contact`, asigna los valores de los campos a los atributos `name` y `phone_number` del objeto `$contact`, y luego llama al método `$contact->save()` para almacenar el nuevo registro en la base de datos.*

*Al hacer esto, obtendrás una respuesta JSON:*

```json
{"message":"Contact Stored"}
```

*Esto indica que el contacto se ha almacenado correctamente en la base de datos.*

---

### **Verificar en la Base de Datos**

*Ahora, para verificar que el contacto fue guardado correctamente en la base de datos, ejecutamos la siguiente consulta SQL en PostgreSQL:*

```sql
SELECT * FROM my_custom_name_table;
```

#### **Resultado Esperado:**

```sql
 contact_id |  name  | phone_number |     created_at      |     updated_at
------------+--------+--------------+---------------------+---------------------
          1 | Daniel |    123456789 | 2025-03-24 02:36:49 | 2025-03-24 02:36:49
(1 row)
```

*Esto muestra el registro que acabamos de insertar, con el `contact_id` generado automáticamente, el `name` como "Daniel", el `phone_number` como 123456789, y las fechas de creación y actualización (que son iguales en este caso, ya que no se han realizado actualizaciones adicionales).*

---

### **Eliminar la Tabla**

*Si deseas eliminar la tabla creada, puedes ejecutar el siguiente comando SQL:*

```sql
drop table my_custom_name_table;
```

*Esto eliminará la tabla `my_custom_name_table` de la base de datos, lo que también eliminará todos los registros almacenados en ella.*

- **Resultado Esperado:**

```sql
DROP TABLE
```

---

### **Resumen Final:**

1. **Modelo Personalizado:** *Definimos el modelo `Contact`, especificando una tabla personalizada (`my_custom_name_table`) y una clave primaria personalizada (`contact_id`).*
2. **Creación de la Tabla:** *Creamos la tabla en la base de datos, asegurándonos de que los tipos de datos para `created_at` y `updated_at` sean apropiados para evitar errores.*
3. **Petición y Almacenamiento:** *Creamos una ruta para almacenar un nuevo contacto en la base de datos. Usamos el modelo Eloquent para interactuar con la base de datos.*
4. **Verificación:** *Consultamos la base de datos para verificar que el contacto se almacenó correctamente.*
5. **Eliminación de la Tabla:** *Eliminamos la tabla creada para limpiar el entorno de prueba.*

---

## **Modelo Contact con Convenciones de Laravel**

```php
<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Contact extends Model
{
    use HasFactory;

    // En lugar de personalizar la tabla y la clave primaria, seguimos la convención de Laravel.
    // Laravel asume por defecto que la tabla se llama 'contacts' (plural y en minúsculas) y
    // que la clave primaria es 'id'.
    // protected $table = 'my_custom_name_table';
    // protected $primaryKey = 'contact_id';

}
```

---

### **Simplificación del Código con `Contact::create()`**

*En lugar de usar un proceso largo para crear una instancia del modelo `Contact`, asignar sus atributos uno por uno y luego guardar la instancia, Laravel ofrece una forma más sencilla de hacerlo utilizando el método estático `create()`. Este método facilita la creación y el guardado de nuevos registros en la base de datos en una sola línea de código.*

---

### **Código Simplificado:**

**El siguiente es el código simplificado utilizando el método `create()` (Generate Error):**

```php
Route::post(
    "/contact",
    function (Request $request) {
        $data = $request->all();

        // Utilizamos el método estático `create()` para crear y guardar el contacto en la base de datos
        Contact::create(
            $data
        );

        // Devolvemos una respuesta JSON para confirmar que el contacto ha sido almacenado
        return Response::json(
            ["message" => "Contact Stored"],
            200
        );
    }
);
```

---

### **Explicación de lo que sucede:**

1. **Recibo de datos desde la solicitud (`$request->all()`):**
   - *`$data = $request->all();` captura todos los datos enviados en la solicitud. En este caso, esperamos que el cuerpo de la solicitud contenga los datos del contacto, como `name` y `phone_number`.*

2. **Método `create()`:**
   - *`Contact::create($data);` es el método que simplifica el proceso de creación de un nuevo registro en la base de datos. En lugar de crear una instancia del modelo (`new Contact()`), asignar valores manualmente a cada atributo, y luego guardar la instancia (`$contact->save()`), `create()` hace todo esto en una sola llamada.*
   - *Este método acepta un arreglo de atributos (`$data`) y crea un nuevo registro en la base de datos con esos valores. Laravel se encarga de asignar los valores al modelo y luego guardar el registro.*

3. **Respuesta JSON:**
   - *Finalmente, después de crear el registro, la respuesta es enviada como un JSON con el mensaje `"Contact Stored"`, indicando que el contacto fue guardado correctamente en la base de datos.*

---

### **El Error: `MassAssignmentException`**

*Cuando intentamos enviar una solicitud con el método `create()`, nos encontramos con el siguiente error:*

```bash
Illuminate\Database\Eloquent\MassAssignmentException
PHP 8.3.0
9.52.20
Add [_token] to fillable property to allow mass assignment on [App\Models\Contact].
```

*Este error ocurre porque Laravel está bloqueando la **asignación masiva** de datos. La **asignación masiva** es una característica de Eloquent que permite asignar muchos atributos de un modelo al mismo tiempo, como hacemos con el método `create()`. Sin embargo, para proteger tu aplicación de posibles **vulnerabilidades de seguridad**, Laravel requiere que definas explícitamente qué atributos son **permitidos** para la asignación masiva.*

---

### **Solución al Error: Definir los Atributos Permitidos con `$fillable`**

*Para resolver este problema, necesitamos decirle a Laravel que los campos `name` y `phone_number` son **permitidos** para la asignación masiva. Esto se hace añadiendo estos atributos a la propiedad `$fillable` en el modelo `Contact`.*

E*l archivo del modelo `Contact` se vería así:*

```php
<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Contact extends Model
{
    use HasFactory;

    // Aquí especificamos los campos que pueden ser asignados masivamente.
    protected $fillable = [
        "name",        // El nombre del contacto
        "phone_number" // El número de teléfono del contacto
    ];
}
```

- **`protected $fillable`:** *Especificamos qué campos son **seguro** que se asignen masivamente. Los campos en este arreglo (`name` y `phone_number`) son los que permitimos que el método `create()` pueda asignar desde los datos que vienen en la solicitud.*

### **Por qué es Necesario `$fillable`:**

- **Seguridad:** *Sin `$fillable`, si intentamos asignar atributos que no están definidos, Laravel podría permitir la asignación masiva de atributos no deseados, lo que podría ser un riesgo de seguridad. Por ejemplo, si un usuario envía un campo no deseado como `is_admin`, que no debería ser asignado, Laravel lo bloquearía si no está incluido en `$fillable`.*
  
- **Evitar Manipulación de Atributos Sensibles:** *Si no se especifican los campos permitidos, cualquier campo enviado en la solicitud podría modificarse en la base de datos. Definir `$fillable` garantiza que solo los atributos controlados y definidos explícitamente puedan ser modificados.*

---

### **Probando de Nuevo la Funcionalidad:**

*Una vez que hayas agregado el arreglo `$fillable` en el modelo `Contact`, vuelve a hacer la solicitud. Esta vez, **Laravel no debería quejarse** sobre la asignación masiva y el contacto debería guardarse correctamente en la base de datos.*

---

### **Verificación en la Base de Datos:**

*Para confirmar que los datos se guardaron correctamente, puedes realizar la consulta a la base de datos directamente:*

```bash
docker container exec --interactive --tty --user 0:0 --privileged -w / db psql -h localhost -U postgres -p 5432 -d contacts_app -c 'SELECT * FROM contacts';
```

*La salida debería mostrar algo similar a esto:*

```bash
 id |   name   | phone_number |     created_at      |     updated_at
----+----------+--------------+---------------------+---------------------
  1 | Daniel   | 12345678     | 2025-03-22 03:23:49 | 2025-03-22 03:23:49
  2 | Benjamin | 87654321     | 2025-03-22 03:44:44 | 2025-03-22 03:44:44
(2 rows)
```

**Esto muestra que los contactos han sido almacenados correctamente en la tabla `contacts`.**

- **Resumen Final:**

1. **Simplificación con `create()`:** *Utilizar `Contact::create($data)` hace que el código sea más limpio y conciso, evitando la necesidad de crear instancias del modelo y asignar manualmente los valores.*
2. **Protección contra asignación masiva:** *Laravel requiere que definamos qué atributos son seguros para la asignación masiva a través de `$fillable`, lo que previene vulnerabilidades de seguridad.*
3. **Verificación:** *Siempre puedes verificar en la base de datos que los datos fueron correctamente guardados utilizando herramientas como `psql` o un cliente de base de datos.*

---

### **Uso de Controladores en Laravel para Organizar la Lógica de la Aplicación**

> [!NOTE]
> *En Laravel, los controladores proporcionan una forma más estructurada de manejar la lógica de las solicitudes HTTP. En lugar de manejar directamente la lógica en las rutas, lo ideal es delegarla a controladores para mantener el código limpio, modular y fácil de mantener. Los controladores también permiten reutilizar la lógica y facilitan la gestión de la autenticación, validación, y otros aspectos importantes en aplicaciones web complejas.*

---

### **Creación de un Controlador con Artisan**

*Para crear un controlador, utilizamos el comando `php artisan make:controller`. Este comando genera un archivo de controlador donde podemos definir los métodos que responderán a las solicitudes.*

#### **Comando: `php artisan make:controller --help`**

*Cuando ejecutamos `php artisan make:controller --help`, obtenemos información sobre cómo utilizar el comando para generar un controlador. Aquí está la salida detallada:*

```bash
php artisan make:controller --help

  Create a new controller class

Usage:
  make:controller [options] [--] <name>

Arguments:
  name                   The name of the controller

Options:
      --api              Exclude the create and edit methods from the controller
      --type=TYPE        Manually specify the controller stub file to use
      --force            Create the class even if the controller already exists
  -i, --invokable        Generate a single method, invokable controller class
  -m, --model[=MODEL]    Generate a resource controller for the given model
  -p, --parent[=PARENT]  Generate a nested resource controller class
  -r, --resource         Generate a resource controller class
  -R, --requests         Generate FormRequest classes for store and update
  -s, --singleton        Generate a singleton resource controller class
      --creatable        Indicate that a singleton resource should be creatable
      --test             Generate an accompanying PHPUnit test for the Controller
      --pest             Generate an accompanying Pest test for the Controller
  -h, --help             Display help for the given command. When no command is given display help for the list command
  -q, --quiet            Do not output any message
  -V, --version          Display this application version
      --ansi|--no-ansi   Force (or disable --no-ansi) ANSI output
  -n, --no-interaction   Do not ask any interactive question
      --env[=ENV]        The environment the command should run under
  -v|vv|vvv, --verbose   Increase the verbosity of messages: 1 for normal output, 2 for more verbose output and 3 for debug
```

**Argumento:**

- **`name`:** *El nombre del controlador que deseas crear. Este será el nombre del archivo del controlador y la clase que se generará dentro del archivo.*

**Opciones:**

- **`--api`:** *Excluye los métodos `create` y `edit` del controlador, ideal para controladores que solo sirven para una API.*
- **`--type=TYPE`:** *Permite especificar manualmente el archivo de plantilla (stub) que se debe usar para crear el controlador.*
- **`--force`:** *Permite sobrescribir un controlador existente si ya existe un archivo con ese nombre.*
- **`-i, --invokable`:** *Genera un controlador con un solo método, invocable, lo que significa que el controlador solo tendrá un método que se ejecutará cuando se llame al controlador.*
- **`-m, --model[=MODEL]`:** *Vincula el controlador al modelo proporcionado, creando un controlador de recursos con las acciones necesarias para trabajar con ese modelo.*
- **`-p, --parent[=PARENT]`:** *Genera un controlador de recursos anidado, ideal cuando estás trabajando con relaciones de recursos en tus modelos.*
- **`-r, --resource`:** *Genera un controlador de recursos, con los métodos comunes como `index`, `store`, `update`, `destroy`.*
- **`-R, --requests`:** *Genera las clases `FormRequest` necesarias para las operaciones de almacenamiento y actualización en el controlador.*
- **`-s, --singleton`:** *Crea un controlador de recursos que solo gestionará una única instancia del recurso (ideal para controladores que gestionan una única entidad o recurso).*
- **`--creatable`:** *Indica que el recurso de tipo singleton puede ser creado.*
- **`--test`:** *Genera una prueba PHPUnit acompañante para el controlador.*
- **`--pest`:** *Genera una prueba Pest acompañante para el controlador.*
- **`-h, --help`:** *Muestra ayuda sobre el comando.*
- **`-q, --quiet`:** *Ejecuta el comando sin mostrar ningún mensaje de salida.*
- **`-V, --version`:** *Muestra la versión de la aplicación.*
- **`--ansi|--no-ansi`:** *Controla si se habilita o deshabilita la salida en formato ANSI (con colores y estilo).*
- **`-n, --no-interaction`:** *Ejecuta el comando sin interacción, no te pedirá ninguna confirmación durante la ejecución.*
- **`--env[=ENV]`:** *Especifica el entorno en el que debe ejecutarse el comando (por ejemplo, `local`, `production`).*
- **`-v|vv|vvv, --verbose`:** *Incrementa la verbosidad de la salida del comando, lo que proporciona más detalles (ideal para la depuración).*

#### **Ejemplo de Comando:**

```bash
php artisan make:controller ContactController
```

*Este comando genera un nuevo archivo de controlador llamado `ContactController.php` dentro de la carpeta `app/Http/Controllers/`. La salida esperada es:*

```bash
php artisan make:controller ContactController
   INFO  Controller [app/Http/Controllers/ContactController.php] created successfully.
```

---

### **Contenido Inicial del Controlador:**

*Una vez que el controlador ha sido creado, su estructura inicial estará vacía. El archivo `app/Http/Controllers/ContactController.php` generado por Laravel se verá algo así:*

```php
<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class ContactController extends Controller
{
    //
}
```

- **Explicación:**

1. **Namespace:**
   - **`namespace App\Http\Controllers;`:** *Define el espacio de nombres para el controlador. Esto permite que Laravel identifique correctamente el controlador dentro de la estructura de la aplicación.*

2. **Uso de `Request`:**
   - **`use Illuminate\Http\Request;`:** *Importa la clase `Request` que Laravel usa para manejar las solicitudes HTTP. Esta clase es esencial para acceder a los datos enviados por el usuario en las solicitudes.*

3. **Clase Controlador:**
   - **`class ContactController extends Controller`:** *La clase `ContactController` hereda de la clase base `Controller`. En Laravel, todos los controladores deben extender esta clase base, que proporciona funcionalidades comunes a todos los controladores, como manejo de middleware y validación.*

---

### **Conectando un Controlador con un Modelo en Laravel**

*Para organizar y estructurar mejor las funcionalidades en una aplicación Laravel, es recomendable separar la lógica de las rutas mediante el uso de controladores. Además, Laravel facilita la interacción con las bases de datos mediante el uso de **modelos**, que representan las tablas de la base de datos. Los controladores se conectan a los modelos para gestionar de manera eficiente las operaciones CRUD (Crear, Leer, Actualizar, Eliminar) en la base de datos.*

---

### **Borrando el Controlador Vacío:**

*En primer lugar, si un controlador no está implementando ninguna lógica o no está conectado al modelo, puedes eliminarlo con el comando:*

```bash
rm !$ 
```

*El `!$` en la terminal es un atajo para usar el último argumento de la última línea de comandos. En este caso, `!$` hace referencia al nombre del archivo del controlador creado anteriormente (por ejemplo, `ContactController.php`). Esto es útil cuando quieres eliminar rápidamente un archivo que fue mencionado en el último comando.*

---

### **Creación del Controlador Vinculado a un Modelo:**

*En lugar de crear un controlador vacío, ahora vamos a vincular el controlador con un modelo específico, en este caso, el modelo `Contact`. Para hacer esto, utilizamos el siguiente comando:*

```bash
php artisan make:controller --model=Contact ContactController
```

*O también puedes usar la forma abreviada:*

```bash
php artisan make:controller -m Contact ContactController
```

#### **Explicación del Comando:**

- **`php artisan make:controller`:** *Es el comando de Artisan que se utiliza para crear un nuevo controlador.*
- **`--model=Contact` o `-m Contact`:** *Especifica que el controlador debe estar vinculado al modelo `Contact`. Esto hace que el controlador genere un conjunto de métodos CRUD básicos y facilite la interacción con la tabla asociada al modelo `Contact` en la base de datos.*
- **`ContactController`:** *Es el nombre del controlador que se creará. Este será el archivo y la clase dentro del controlador.*

#### **Salida esperada del comando:**

*Cuando ejecutamos el comando, veremos la siguiente salida:*

```bash
php artisan make:controller --model=Contact ContactController

   INFO  Controller [app/Http/Controllers/ContactController.php] created successfully.
```

*Esto indica que el controlador `ContactController.php` ha sido creado correctamente y está vinculado al modelo `Contact`.*

---

### **Explorando el Controlador Generado:**

*Una vez que se ha generado el controlador, podemos abrir el archivo en la ruta `app/Http/Controllers/ContactController.php` y ver cómo está estructurado.*

```php
<?php

namespace App\Http\Controllers;

use App\Models\Contact;
use Illuminate\Http\Request;

class ContactController extends Controller
{
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
        //
    }

    /**
     * Display the specified resource.
     *
     * @param  \App\Models\Contact  $contact
     * @return \Illuminate\Http\Response
     */
    public function show(Contact $contact)
    {
        //
    }

    /**
     * Show the form for editing the specified resource.
     *
     * @param  \App\Models\Contact  $contact
     * @return \Illuminate\Http\Response
     */
    public function edit(Contact $contact)
    {
        //
    }

    /**
     * Update the specified resource in storage.
     *
     * @param  \Illuminate\Http\Request  $request
     * @param  \App\Models\Contact  $contact
     * @return \Illuminate\Http\Response
     */
    public function update(Request $request, Contact $contact)
    {
        //
    }

    /**
     * Remove the specified resource from storage.
     *
     * @param  \App\Models\Contact  $contact
     * @return \Illuminate\Http\Response
     */
    public function destroy(Contact $contact)
    {
        //
    }
}
```

#### **Explicación del Controlador Generado:**

1. **Importación del Modelo `Contact`:**

   - **`use App\Models\Contact;`:** *Esto importa el modelo `Contact`, lo que permite que el controlador interactúe con la tabla `contacts` en la base de datos.*

2. **Métodos del Controlador:**

   - *Laravel genera automáticamente los métodos básicos para las operaciones CRUD cuando se utiliza el parámetro `--model=Contact` o `-m Contact`. Estos métodos están destinados a interactuar con el modelo `Contact`.*

   - **`index()`:** *Este método generalmente se utiliza para mostrar una lista de recursos (en este caso, contactos). Aún no tiene lógica, pero se puede llenar con una consulta para obtener todos los contactos de la base de datos.*

   - **`create()`:** *Se utiliza para mostrar un formulario para crear un nuevo recurso. Aunque está vacío, generalmente aquí se devolvería una vista con un formulario para ingresar los datos del contacto.*

   - **`store(Request $request)`:** *Este método se utiliza para almacenar un nuevo recurso en la base de datos. Recibe los datos de la solicitud y los guarda en la base de datos utilizando el modelo `Contact`. Este método generalmente contiene la lógica para validar y guardar un nuevo contacto.*

   - **`show(Contact $contact)`:** *Este método se utiliza para mostrar un recurso específico. Recibe el modelo `Contact` como un parámetro, lo que significa que Laravel automáticamente inyectará el contacto de la base de datos basado en el ID proporcionado en la URL.*

   - **`edit(Contact $contact)`:** *Similar al método `show`, este método se utiliza para mostrar un formulario de edición para un recurso específico. Recibe el modelo `Contact` y generalmente se usa para pasar los datos a una vista de edición.*

   - **`update(Request $request, Contact $contact)`:** *Este método se utiliza para actualizar un recurso específico. Recibe los datos de la solicitud y el modelo `Contact` para actualizar la información en la base de datos.*

   - **`destroy(Contact $contact)`:** *Este método se utiliza para eliminar un recurso específico. Recibe el modelo `Contact` y lo elimina de la base de datos.*

---

### **Más Recursos:**

*Para obtener más información sobre cómo trabajar con controladores y modelos en Laravel, puedes consultar la [documentación oficial de controladores](https://laravel.com/docs/12.x/controllers "https://laravel.com/docs/12.x/controllers") en el sitio web de Laravel.*

---

### **Conclusión:**

- **Vinculación del Controlador al Modelo:** *Usando la opción `--model=Contact` o `-m Contact`, Laravel genera automáticamente un controlador que ya está vinculado al modelo `Contact`, lo que facilita la creación de métodos CRUD para gestionar recursos de la base de datos.*  
- **Estructura del Controlador:** *El controlador generado proporciona los métodos básicos para realizar operaciones CRUD. Estos métodos pueden ser fácilmente personalizados para satisfacer las necesidades específicas de la aplicación.*

---

### **Flujo con Controladores en Laravel**

---

#### **Cambio en el Flujo de Rutas con Controladores:**

*Hasta ahora, en los ejemplos anteriores, hemos utilizado **rutas con funciones anónimas** para manejar las peticiones HTTP. Esto significa que en el archivo `routes/web.php`, definíamos las rutas de forma sencilla con una función directa:*

```php
Route::post(
    "/contact",
    function (Request $request) {
        // lógica para almacenar contacto
    }
);
```

> [!IMPORTANT]
> *Sin embargo, **usando controladores** cambia el flujo. Ahora, en lugar de usar funciones anónimas, asociamos una ruta a un **método específico dentro de un controlador**. Este cambio tiene la ventaja de que la lógica está mejor estructurada, lo que facilita la gestión de las acciones del controlador y hace que el código sea más limpio y modular.*

---

#### **Actualización de la Ruta para Usar el Controlador:**

*En este caso, modificamos la ruta en el archivo `routes/web.php` para que apunte al controlador `ContactController` y a su método `create`. El código actualizado en `routes/web.php` sería:*

```php
Route::get(
    "/contacts/create",
    [ContactController::class, "create"]
);
```

**Explicación de la Ruta:**

- **`Route::get(...)`:** *Esto indica que esta es una ruta de tipo **GET**. Este verbo HTTP se usa generalmente para obtener información de la aplicación (en este caso, mostrar el formulario para crear un nuevo contacto).*
- **`"/contacts/create"`:** *Es la URL que será accedida en el navegador para invocar la acción. Cuando el usuario visita esta URL, el sistema ejecutará el método `create` del controlador.*
- **`[ContactController::class, "create"]`:** *Aquí, Laravel resuelve la clase `ContactController` y el método `create`. Laravel se encarga de la inyección de dependencias y de resolver este controlador y método automáticamente.*

*Este cambio significa que, en lugar de tener una **función anónima**, ahora el flujo de la aplicación pasa por el **controlador** y su método. Así, podemos manejar la lógica en un lugar separado y más organizado.*

---

#### **Modificación del Método `create` en el Controlador:**

*En el controlador `ContactController`, tenemos el método `create` que se ejecutará cuando el usuario visite la ruta `/contacts/create`. Originalmente, el método `create` estaba vacío, pero lo modificamos para devolver una vista que será mostrada al usuario.*

```php
 /**
     *Show the form for creating a new resource.
     *
     *@return \Illuminate\Http\Response
     */
    public function create()
    {
        //
    }
```

*El código del controlador modificado sería:*

```php
/**
 * Show the form for creating a new resource.
 *
 * @return \Illuminate\Http\Response
 */
public function create()
{
    // return Response::view("contacts");
    return view("contacts");
}
```

**Explicación de la Modificación:**

- **`return view("contacts");`:** *Este método de Laravel devuelve una vista llamada `contacts`. Laravel buscará un archivo de vista en `resources/views/contacts.blade.php`. Si ese archivo existe, Laravel lo renderizará y lo enviará como respuesta al navegador del usuario.*

*Anteriormente, el método estaba vacío y no hacía nada, pero con esta modificación estamos siguiendo la convención y haciendo que el controlador devuelva la vista para que el usuario vea un formulario de creación de un nuevo contacto.*

> [!NOTE]
> **Nota:** *Si prefieres usar `Response::view("contacts")`, también es válido, pero `view("contacts")` es más común en Laravel.*

---

#### **Convención de Rutas de Controlador en Laravel:**

*Laravel sigue una convención para las rutas y los controladores de recursos. Al crear un controlador de recursos (con `php artisan make:controller --resource` o el modificador `-r`), Laravel genera un conjunto estándar de rutas para un CRUD básico.*

*Según la documentación de Laravel, las rutas gestionadas por un controlador de recursos siguen esta convención:*

| **Verbo**     | **URI**                  | **Acción**  | **Nombre de la Ruta** |
| ------------- | ------------------------ | ----------- | --------------------- |
| *`GET`*       | *`/photos`*              | *`index`*   | *`photos.index`*      |
| *`GET`*       | *`/photos/create`*       | *`create`*  | *`photos.create`*     |
| *`POST`*      | *`/photos`*              | *`store`*   | *`photos.store`*      |
| *`GET`*       | *`/photos/{photo}`*      | *`show`*    | *`photos.show`*       |
| *`GET`*       | *`/photos/{photo}/edit`* | *`edit`*    | *`photos.edit`*       |
| *`PUT/PATCH`* | *`/photos/{photo}`*      | *`update`*  | *`photos.update`*     |
| *`DELETE`*    | *`/photos/{photo}`*      | *`destroy`* | *`photos.destroy`*    |

> [!NOTE]
> **Referencia:** *Para más detalles sobre las rutas y controladores de recursos, consulta la [documentación oficial de Laravel sobre controladores](https://laravel.com/docs/12.x/controllers "https://laravel.com/docs/12.x/controllers").*

*Esta convención ayuda a que Laravel gestione las rutas de manera consistente y facilita el trabajo con la API de Laravel.*

---

#### **Haciendo la Petición GET a la Ruta:**

*Finalmente, al hacer una **petición GET** a la ruta `/contacts/create`, se activará el método `create` del `ContactController`. El flujo será el siguiente:*

1. *El navegador hace una solicitud GET a `http://172.17.0.2/contacts/create`.*
2. *Laravel resuelve la ruta y llama al método `create` del `ContactController`.*
3. *El método `create` devuelve la vista `contacts`, que se encuentra en `resources/views/contacts.blade.php`.*
4. *El navegador muestra el formulario de creación de contacto.*

---

### **Resumen:**

1. **Cambio de Rutas a Controlador:**
   - *Usamos rutas basadas en **controladores** en lugar de funciones anónimas, lo que mejora la organización del código.*
   - *La ruta ahora es gestionada por un controlador, en este caso, `ContactController`, con el método `create`.*

2. **Modificación del Método `create`:**
   - *Modificamos el método `create` en el controlador para devolver la vista `contacts` en lugar de dejarlo vacío.*

3. **Convención de Controladores de Recursos:**
   - *Laravel sigue una convención estándar para los controladores de recursos, lo que facilita la creación de rutas y acciones CRUD.*

4. **Petición GET a la Ruta:**
   - *Al hacer una solicitud GET a `http://172.17.0.2/contacts/create`, el método `create` del controlador es invocado y devuelve la vista `contacts`.*

---

### **Ruta, Controlador, y Formularios en Laravel**

---

#### **Uso de Controladores para Evitar Inserción Directa en HTML:**

*En Laravel, la mejor práctica es **no** insertar directamente la lógica de manejo de datos dentro de los archivos HTML, sino que debemos delegar esa responsabilidad a los **controladores**. Esto ayuda a mantener el código limpio, modular y más fácil de mantener.*

*Por ejemplo, en lugar de realizar una solicitud directamente en el formulario HTML con una ruta como `"/contact"`, utilizamos un controlador para gestionar esa acción. De esta manera, toda la lógica del manejo de datos se centraliza en el controlador y no en las vistas.*

---

#### **Renombramiento de Rutas Usando la Convención de Laravel:**

*Laravel sigue una convención para nombrar las rutas y facilitar el uso de URLs. Al **renombrar las rutas**, estamos haciendo que el sistema sea más consistente y fácil de mantener. Laravel permite asociar un **nombre** a cada ruta, lo que facilita la generación de URLs en las vistas mediante el uso de `route()`.*

**Código Original:**

```php
<form method="POST" action="/contact">
```

*En este código, la ruta `action="/contact"` estaba definida de forma estática, lo que puede ser menos flexible si necesitas cambiar la ruta en el futuro.*

**Código Modificado en `routes/web.php`:**

```php
Route::get(
    "/contacts/create",
    [ContactController::class, "create"]
)->name("contacts.create");

Route::post(
    "/contacts",
    [ContactController::class, "store"]
)->name("contacts.store");
```

- **`Route::get("/contacts/create", [ContactController::class, "create"])`:** *Aquí estamos creando una ruta GET para mostrar el formulario de creación de contacto. Cuando el usuario visite `/contacts/create`, se invocará el método `create` del `ContactController`.*
- **`Route::post("/contacts", [ContactController::class, "store"])`:** *Esta es la ruta POST que se encarga de almacenar un nuevo contacto. El formulario de creación de contacto enviará los datos a esta ruta.*
- **`->name("contacts.create")` y `->name("contacts.store")`:** *Al asignar nombres a las rutas, ahora podemos hacer referencia a ellas en el código de manera más legible y reutilizable. Usar nombres en lugar de URLs directamente en las vistas es la forma recomendada de manejar rutas en Laravel.*

**Formulario Modificado:**

```php
<form method="POST" action="{{ route('contacts.store') }}">
```

- **`{{ route('contacts.store') }}`:** *Usando `route()`, Laravel genera automáticamente la URL de la ruta `contacts.store`. Esto es más flexible que usar la URL directamente en el `action`, ya que si la ruta cambia en el futuro, solo necesitarás modificar la definición de la ruta, no el formulario.*

---

#### **Uso del Método `store` en el Controlador:**

*Dentro del controlador `ContactController`, el método `store` es el encargado de almacenar un nuevo contacto en la base de datos. Sin embargo, **no es recomendable** usar `$request->all()` directamente debido a preocupaciones de seguridad, ya que podría permitir la asignación masiva (Mass Assignment) de datos no deseados.*

```php
/**
 * Store a newly created resource in storage.
 *
 * @param  \Illuminate\Http\Request  $request
 * @return \Illuminate\Http\Response
 */
public function store(Request $request)
{
    // 
}
```

**Código del método `store` modificado:**

```php
/**
 * Store a newly created resource in storage.
 *
 * @param  \Illuminate\Http\Request  $request
 * @return \Illuminate\Http\Response
 */
public function store(Request $request)
{
    // No recomendable
    Contact::create(
        $request->all()
    );

    return response("Contact Created");
}
```

**Explicación del Código:**

- **`$request->all()`:** *Este método obtiene todos los datos enviados en el formulario. Aunque funciona, **no es recomendable** usarlo directamente porque permite la asignación masiva de cualquier dato. Esto puede llevar a **vulnerabilidades de seguridad**, como la modificación de campos que no deberían ser modificables (por ejemplo, el ID de un registro).*
  
---

#### **Verificación de los Datos en la Base de Datos:**

*Una vez que el formulario haya sido enviado y el contacto haya sido creado, podemos verificar en la base de datos si el registro se ha insertado correctamente.*

**Petición HTTP a la Ruta:**

```bash
http://172.17.0.2/contacts
```

*Al hacer una solicitud **GET** a esta URL, Laravel invoca el método `index` del controlador (si es que está definido) o simplemente nos muestra la lista de contactos almacenados. Esta es la forma en que puedes acceder a la información almacenada en la base de datos a través de una ruta.*

*Si la inserción ha sido exitosa, deberías ver el nuevo contacto en la base de datos, que se puede consultar con una herramienta de gestión de bases de datos como **PostgreSQL** o cualquier otra herramienta que estés usando.*

- **Resumen:**

1. **Renombramiento de Rutas:**
   - *Usar el método `name()` para nombrar las rutas permite una mayor flexibilidad y facilita la gestión de URLs en las vistas.*
   - *Ejemplo: `route('contacts.store')` en lugar de escribir la URL directamente.*

2. **Controlador `store`:**
   - *El controlador se encarga de manejar la lógica del negocio, como almacenar los datos.*
   - **No es recomendable** *usar `$request->all()` directamente para evitar problemas de seguridad (asignación masiva).*

3. **Creación de Contacto:**
   - *Usamos `Contact::create()` para insertar el contacto en la base de datos.*
   - **Alternativa más segura:** *usar `$request->only()` para especificar qué datos se deben almacenar.*

4. **Verificación en la Base de Datos:**
   - *Al hacer una petición GET a `http://172.17.0.2/contacts`, verificamos que el contacto se haya insertado correctamente en la base de datos.*

---

## *El flujo final en Laravel sigue el patrón **MVC** (Modelo-Vista-Controlador), que es una arquitectura de diseño comúnmente utilizada para estructurar aplicaciones web*

### **1. Modelo (Model):**

*El **modelo** representa los datos y la lógica de negocio de la aplicación. En Laravel, los modelos interactúan directamente con la base de datos.*

**En tu caso:**

- *Tienes el modelo `Contact` que es responsable de interactuar con la tabla `contacts` en la base de datos.*
- *Este modelo define cómo se deben almacenar, recuperar, actualizar o eliminar los registros de contacto.*
- **Code:**
  
  ```php
  <?php
    namespace App\Models;

    use Illuminate\Database\Eloquent\Factories\HasFactory;
    use Illuminate\Database\Eloquent\Model;

    class Contact extends Model
    {
        use HasFactory;
        
        // En lugar de personalizar la tabla y la clave primaria, seguimos la convención de Laravel.
        // Laravel asume por defecto que la tabla se llama 'contacts' (plural y en minúsculas) y
        // que la clave primaria es 'id'.
        // protected $table = 'my_custom_name_table';
        // protected $primaryKey = 'contact_id';

        protected $fillable = [
            "name",
            "phone_number"
        ];
    }
  ```

### **2. Vista (View):**

*La **vista** es responsable de la interfaz de usuario, es decir, lo que ve el usuario en el navegador. Laravel utiliza Blade, un motor de plantillas, para gestionar las vistas.*

**En Nuestro Caso:**

- *La vista `contacts.create` (o cualquier otra vista) es responsable de mostrar el formulario de creación de contacto.*
- *Blade maneja la presentación de los datos en una estructura HTML fácil de entender y editar.*
- **Ejemplo** *de la vista en `resources/views/contacts/create.blade.php`:*

  ```html
  @extends('layouts.app')

    @section('content')
    <div class="container">
        <div class="row justify-content-center">
        <div class="col-md-8">
            <div class="card">
            <div class="card-header">Create new contact</div>

            <div class="card-body">
                <form method="POST" action="{{ route("contacts.store") }}">
                {{-- <input type="hidden" name="_token" value="{{ csrf_token() }}"> --}}
                @csrf
                <div class="row mb-3">
                    <label for="name" class="col-md-4 col-form-label text-md-end">Name</label>

                    <div class="col-md-6">
                    <input id="name" type="text" class="form-control" name="name"
                        required autocomplete="name" autofocus>

                    </div>
                </div>

                <div class="row mb-3">
                    <label for="phone_number" class="col-md-4 col-form-label text-md-end">Phone Number</label>

                    <div class="col-md-6">
                    <input id="phone_number" type="tel" class="form-control" name="phone_number" required
                        autocomplete="phone_number">
                    </div>
                </div>

                <div class="row mb-0">
                    <div class="col-md-6 offset-md-4">
                    <button type="submit" class="btn btn-primary">
                        Submit
                    </button>
                    </div>
                </div>
                </form>
            </div>
            </div>
        </div>
        </div>
    </div>
    @endsection
  ```

- **`{{ route('contacts.store') }}`** *genera la URL de la ruta `contacts.store`, que está asociada al método `store` del `ContactController`.*

### **3. Controlador (Controller):**

*El **controlador** gestiona la lógica de la aplicación, interactúa con los modelos y pasa los datos a las vistas. El controlador recibe las peticiones HTTP, procesa los datos (por ejemplo, validación y almacenamiento), y luego devuelve una respuesta (ya sea una vista, una redirección o un JSON).*

**En tu caso:**

- *El controlador `ContactController` maneja las peticiones relacionadas con el recurso `Contact`.*
- *Define métodos como `create` (para mostrar el formulario de creación) y `store` (para almacenar un nuevo contacto en la base de datos).*
- **Code:**

  ```php
  <?php

    namespace App\Http\Controllers;

    use App\Models\Contact;
    use Illuminate\Http\Request;

    class ContactController extends Controller
    {
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
            // return Response::view("contact");
            return view("contact");
        }

        /**
        * Store a newly created resource in storage.
        *
        * @param  \Illuminate\Http\Request  $request
        * @return \Illuminate\Http\Response
        */
        public function store(Request $request)
        {
            // No Recomendable
            Contact::create(
                $request->all()
            );

            return response("Contact Created");
        }

        /**
        * Display the specified resource.
        *
        * @param  \App\Models\Contact  $contact
        * @return \Illuminate\Http\Response
        */
        public function show(Contact $contact)
        {
            //
        }

        /**
        * Show the form for editing the specified resource.
        *
        * @param  \App\Models\Contact  $contact
        * @return \Illuminate\Http\Response
        */
        public function edit(Contact $contact)
        {
            //
        }

        /**
        * Update the specified resource in storage.
        *
        * @param  \Illuminate\Http\Request  $request
        * @param  \App\Models\Contact  $contact
        * @return \Illuminate\Http\Response
        */
        public function update(Request $request, Contact $contact)
        {
            //
        }

        /**
        * Remove the specified resource from storage.
        *
        * @param  \App\Models\Contact  $contact
        * @return \Illuminate\Http\Response
        */
        public function destroy(Contact $contact)
        {
            //
        }
    }
  ```

### **Flujo Final:**

1. **El usuario visita la ruta `/contacts/create`:** *Esto dispara la ruta `Route::get("/contacts/create", [ContactController::class, "create"])`, que ejecuta el método `create` del controlador `ContactController`. El controlador devuelve la vista `contacts.create`, que es el formulario de creación de contacto.*
  
2. **El usuario llena el formulario y lo envía:** *El formulario realiza una solicitud **POST** a la ruta `/contacts`. Laravel utiliza el método `store` del controlador `ContactController` para manejar esta solicitud.*

3. **El controlador procesa la solicitud:**
    - *El método `store` obtiene los datos del formulario (a través de `$request`), y luego crea un nuevo contacto usando el modelo `Contact`.*
    - *`Contact::create($request->only(['name', 'phone_number']))` almacena el nuevo contacto en la base de datos.*

4. **Respuesta:** *Una vez que el contacto se ha creado, el controlador devuelve una respuesta, en este caso, simplemente un mensaje de texto diciendo que el contacto ha sido creado, pero en una aplicación real probablemente redirigirías a otra vista o mostrarías un mensaje de éxito.*

---

### **Resumen del Flujo MVC Final:**

- **Modelo (`Contact`):** *Maneja la interacción con la base de datos, como la creación de nuevos contactos.*
- **Vista (`contacts.create`):** *Muestra el formulario HTML para que el usuario ingrese datos.*
- **Controlador (`ContactController`):** *Gestiona las solicitudes HTTP, llama al modelo para guardar datos y pasa la respuesta al usuario.*

*El patrón **MVC** facilita la organización del código y permite que cada parte del proceso (manejando datos, mostrando contenido y gestionando la lógica) esté claramente separada, lo que resulta en un código más limpio y fácil de mantener.*

---

### **Recursos adicionales:**

- *[Documentación de Laravel sobre controladores](https://laravel.com/docs/12.x/controllers "https://laravel.com/docs/12.x/controllers")*
- *[Blade Templates - Motor de plantillas de Laravel](https://laravel.com/docs/12.x/blade "https://laravel.com/docs/12.x/blade")*
- *[Documentación de Laravel sobre Modelos Eloquent](https://laravel.com/docs/12.x/eloquent "https://laravel.com/docs/12.x/eloquent")*
