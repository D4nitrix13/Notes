<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# **Reglas de validación**

## **Ejecución del comando `php artisan migrate:rollback`**

**Cuando ejecutamos el comando:**

```bash
php artisan migrate:rollback
```

**Se revierte la última migración aplicada en la base de datos, eliminando las tablas creadas en la última migración.**

### **Error por ambigüedad en el comando**

*Si intentamos ejecutar un comando de manera abreviada sin ser lo suficientemente específico, obtenemos un error de ambigüedad:*

```bash
root@7015cd5a1f73:/App/ApplicationLaravel# php artisan migrate:r

   ERROR  Command "migrate:r" is ambiguous. Did you mean one of these?

  ⇒ migrate:refresh
  ⇒ migrate:reset
  ⇒ migrate:rollback
```

**En este caso, `migrate:r` es ambiguo porque Laravel encuentra varias coincidencias (`refresh`, `reset`, `rollback`).**

### **Uso de autocompletado progresivo**

**Laravel permite escribir comandos parcialmente y autocompletarlos si no hay ambigüedad. Por ejemplo:**

#### **Comando con prefijo `ro`**

```bash
root@7015cd5a1f73:/App/ApplicationLaravel# php artisan migrate:ro

   INFO  Rolling back migrations.

  2025_03_22_030026_create_contacts_table .................................................. 16ms DONE
  2019_12_14_000001_create_personal_access_tokens_table .................................... 5ms DONE
```

#### **Comando con prefijo `roll`**

```bash
root@7015cd5a1f73:/App/ApplicationLaravel# php artisan migrate:roll

   INFO  Rolling back migrations.

  2025_03_22_030026_create_contacts_table .................................................. 25ms DONE
  2019_12_14_000001_create_personal_access_tokens_table .................................... 7ms DONE
```

**Estos comandos son interpretados por Laravel como `rollback`, ya que no hay otra coincidencia.**

**Para ilustrarlo, los siguientes comandos también funcionarían:**

```bash
php artisan migrate:ro
php artisan migrate:roll
php artisan migrate:rollb
php artisan migrate:rollba
php artisan migrate:rollbac
php artisan migrate:rollback
```

**Todos ellos serán interpretados como `php artisan migrate:rollback`.**

---

## **Modificación de una migración existente**

**Editamos el archivo de migración ubicado en:**

```bash
ApplicationLaravel/database/migrations/2025_03_22_030026_create_contacts_table.php
```

### **Contenido del archivo de migración**

```php
/**
 * Ejecuta la migración para crear la tabla `contacts`.
 *
 * @return void
 */
public function up()
{
    Schema::create('contacts', function (Blueprint $table) {
        $table->id(); // Crea un campo de tipo big integer auto incremental
        $table->string("name"); // Campo de texto para el nombre
        $table->string("phone_number"); // Campo de texto para el número de teléfono
        $table->string("email"); // Campo de texto para el correo electrónico
        
        // Definición de un campo de tipo tinyInteger sin signo (edad)
        // Es equivalente a: $table->tinyInteger("age", false, true);
        $table->tinyInteger("age", unsigned: true); // Disponible en PHP 8 en adelante
        // Explicación detallada sobre tinyInteger:
        // - Un `tinyInteger` almacena valores enteros pequeños (-128 a 127 o 0 a 255 si es unsigned)
        // - Ocupa solo 1 byte de espacio en la base de datos, optimizando almacenamiento y rendimiento
        // - Se diferencia de `integer` que ocupa 4 bytes y permite un rango mucho mayor
        // - Se usa para valores pequeños como edades, contadores de intentos, estatus de un campo, etc.
        $table->timestamps(); // Agrega `created_at` y `updated_at`
    });
}
```

> [!TIP]
> *En PHP 8 en adelante, podemos usar la sintaxis named arguments (argumentos nombrados). Esto nos permite especificar valores para parámetros de funciones de manera más clara, sin importar el orden en que aparezcan en la definición de la función.*

---

## **Aplicar la migración**

**Después de modificar el archivo de migración, ejecutamos:**

```bash
php artisan migrate
```

**Este comando aplicará la migración y actualizará la base de datos.**

### **Nota importante**

- *En una aplicación real con datos en producción, **no deberíamos hacer un `rollback` sin precaución**, ya que podríamos perder datos. En su lugar, simplemente ejecutar `php artisan migrate` es lo más seguro, ya que solo agregará nuevas migraciones sin eliminar las existentes.*

---

### **Modificación del Modelo Contact en Laravel**

## **Actualización de los atributos fillable en el modelo Contact**

*En Laravel, el modelo `Contact` se encuentra en el directorio `ApplicationLaravel/app/Models/Contact.php`. Este modelo define la estructura de la tabla `contacts` y especifica qué atributos pueden ser asignados de manera masiva.*

*Editamos el modelo para agregar los atributos `age` y `email` en la propiedad `$fillable`, permitiendo que estos campos puedan ser asignados en masa cuando se cree o actualice un registro en la base de datos.*

```php
protected $fillable = [
    "name",
    "phone_number",
    "age",
    "email"
];
```

## **Detección automática en VS Code**

*La extensión de VS Code puede detectar automáticamente estos cambios en los atributos del modelo y proporcionar autocompletado y documentación enriquecida.*

*Sin embargo, podemos definir manualmente los comentarios de documentación con la anotación `@property` en PHPDoc para mejorar la detección de los atributos del modelo:*

```php
/**
 * Contact Model
 *
 * @property string $name Nombre del contacto.
 * @property integer $phone_number Número de teléfono del contacto.
 * @property string $email Dirección de correo electrónico del contacto.
 * @property integer $age Edad del contacto.
 */
```

*Este comentario mejora la integración con herramientas de análisis estático y extensiones de VS Code.*

- **File Complete**

```php
<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

/**
 * Contact Model
 *
 * @property string $name
 * @property integer $phone_number
 * @property string $email
 * @property interger $age
 */
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
        "phone_number",
        "age",
        "email"
    ];
}
```

## **Extensiones recomendadas para Laravel en VS Code**

**Para mejorar la experiencia de desarrollo en Laravel y PHP, se recomienda instalar las siguientes extensiones:**

```bash
ID -> bmewburn.vscode-intelephense-client           # Proporciona inteligencia artificial y autocompletado para PHP.
ID -> amiralizadeh9480.laravel-extra-intellisense   # Agrega autocompletado para Laravel.
ID -> neilbrayfield.php-docblocker                  # Facilita la creación de comentarios de documentación PHPDoc.
```

## **Compilación de vistas Blade en Laravel**

*En Laravel, las vistas Blade (`.blade.php`) son plantillas que se compilan automáticamente a archivos PHP en tiempo de ejecución. Estos archivos compilados se almacenan en `storage/framework/views`.*

*Si listamos el contenido de ese directorio, podemos ver los archivos compilados con nombres hash asignados por Laravel:*

```bash
lsd -lAh
.rw-r--r-- 1000 1000  14 B  Tue Jun  7 15:03:59 2022  .gitignore
.rw-r--r-- 1000 1000 5.9 KB Sun Mar  2 02:57:01 2025  00acff51cdfbd9f812ae843e1d035506003a60ea.php
.rw-r--r-- 1000 1000 433 B  Thu Mar 13 03:53:54 2025  312c3471a6a062fb36eb05a4d63abd73e985e231.php
.rw-r--r-- 1000 1000 1.3 KB Thu Mar 20 03:25:14 2025  31c4014a9fa1241989f40a56dca960fbefbe6bf2.php
.rw-r--r-- 1000 1000 5.0 KB Sun Mar  2 02:56:45 2025  414d272e2953bb1c03766dcd1613a52cdd1e1132.php
.rw-r--r-- 1000 1000 427 B  Sat Mar  1 18:59:29 2025  4260de9cdaa66c9645a124b73495623b2ecc5733.php
.rw-r--r-- 1000 1000 664 B  Thu Mar 13 03:22:46 2025  428ef6123cbd4179245ae3c6a8c2ef1a4b753038.php
.rw-r--r-- 1000 1000 5.9 KB Wed Mar 26 02:30:32 2025  856f0c6b57a9f7d8c16bca0eaaa96b2529bd1111.php
.rw-r--r-- 1000 1000 3.6 KB Thu Mar 13 02:35:27 2025  be2b95ebe862a0243e36d04e3f10d4d182036946.php
.rw-r--r-- 1000 1000 6.7 KB Sat Mar  1 18:59:29 2025  c75be73a0aedcd7d7c5d3a5e09a03388a28cd482.php
.rw-r--r-- 1000 1000 932 B  Sun Mar  2 03:39:51 2025  edd14d85171a729957ef9ccde790fd3e304fa066.php
```

### **¿Cómo funciona la compilación de vistas Blade?**

1. **Cuando se accede a una vista Blade,** *Laravel compila su contenido a PHP si aún no ha sido compilada o si la vista ha cambiado.*
2. **El archivo compilado** *se almacena en `storage/framework/views/` con un nombre hash.*
3. **Laravel carga el archivo PHP compilado** *en lugar de analizar la plantilla Blade cada vez que se accede a la vista.*

### **Importancia de estos archivos**

- **Mejoran el rendimiento,** *ya que PHP puede ejecutar directamente el archivo compilado sin procesar la plantilla cada vez.*
- **Son generados automáticamente,** *por lo que* **no deben modificarse manualmente**.
- **Si se borra el contenido de `storage/framework/views/`**, *Laravel regenerará los archivos compilados la próxima vez que se acceda a una vista.*

**Para borrar manualmente los archivos compilados y forzar su regeneración, podemos ejecutar:**

```bash
php artisan view:clear
```

- **Salida**

```bash
php artisan view:clear

INFO  Compiled views cleared successfully.
```

*Este comando limpia el caché de vistas compiladas en Laravel.*

---

### **Búsqueda de código compilado en Laravel con `grep`**

*En nuestro caso, queremos encontrar dentro del directorio `storage/framework/views` el código generado para la vista que contiene el texto `Create New Contact`. Para esto usamos el siguiente comando:*

```bash
root@7015cd5a1f73:/App/ApplicationLaravel/storage/framework/views# grep -iEwr "Create New Contact" | xargs
```

#### **Explicación de cada flag en `grep -iEwr`**

- **`-i` →** *Ignora mayúsculas y minúsculas, es decir, encuentra `Create New Contact`, `create new contact`, etc.*
- **`-E` →** *Activa la sintaxis de expresiones regulares extendidas, permitiendo patrones más avanzados.*
- **`-w` →** *Coincidencia de palabra completa. Evita que se encuentren palabras similares dentro de otras.*
- **`-r` →** *Busca de manera recursiva dentro de los subdirectorios.*

#### **Explicación del uso de `xargs`**

- *`xargs` → Si `grep` encuentra varias coincidencias, `xargs` pasa los resultados como argumentos a otro comando.*
  
##### **Salida esperada**

```bash
856f0c6b57a9f7d8c16bca0eaaa96b2529bd1111.php: <div class=card-header>Create new contact</div>
```

**Esto indica que la cadena `Create New Contact` se encuentra en el archivo `856f0c6b57a9f7d8c16bca0eaaa96b2529bd1111.php`, generado por Laravel al compilar una vista Blade.**

---

## **Código generado por Laravel al compilar Blade**

**Blade** *lo convierte en un archivo PHP que se compila para ejecutar la lógica de errores y mostrar el contenido dinámico. Sin embargo, el código PHP generado no es tan legible como el original en Blade, y suele incluir código PHP adicional para manejar errores, lógica y otras funcionalidades que Blade proporciona por conveniencia.*

### **Blade genera contenido PHP ilegible (compilado)**

*El código generado por **Blade** cuando compila este archivo de plantilla es algo como lo siguiente (lo que aparece en el directorio `storage/framework/views`):*

### **Razones por las que es ilegible:**

1. **Optimización del rendimiento:** *Laravel genera código PHP que puede ser complejo a primera vista, pero está optimizado para la ejecución más rápida. Estos fragmentos de código incluyen verificaciones de errores, manejo de variables, y otras tareas que **Blade** simplifica con una sintaxis más comprensible para el desarrollador.*
  
2. **Manejo de errores:** *Laravel genera las verificaciones de errores y muestra mensajes de forma dinámica. Por ejemplo, cuando el campo de entrada no pasa la validación, Blade convierte los errores en una estructura PHP que se muestra en el HTML con el formato adecuado.*

3. **Código dinámico:** *Blade inserta variables y lógica PHP en las plantillas, lo que a veces puede hacer que el archivo resultante sea más largo y más difícil de leer para los desarrolladores que no están familiarizados con la compilación interna.*

---

### **¿Por qué es útil tener este código ilegible?**

*El código PHP generado por **Blade** es necesario para que Laravel maneje la lógica de validación, los errores y otros aspectos dinámicos de la aplicación. Aunque es difícil de leer para los desarrolladores humanos, es procesado de manera eficiente por el servidor para generar la vista correcta de forma rápida.*

---

### **¿Cómo hacer el código más legible?**

*Como ya se mencionó, el código generado por Blade es optimizado, lo que lo hace difícil de leer. Sin embargo, podemos **formatear manualmente** el código para que sea más comprensible. Por ejemplo, el fragmento de Blade que se compila en código PHP se puede reescribir de manera más legible, de modo que podamos ver claramente el comportamiento del formulario con la lógica de errores.*
*Al compilarse con **Blade**, se genera el código PHP para el manejo de errores, el cual se vuelve más difícil de leer, pero si lo tratamos manualmente, podríamos interpretarlo como un bloque de código PHP que gestiona la lógica de los errores y la validación.*
*Es importante tener en cuenta que esta conversión de Blade a PHP es algo que ocurre en el backend de Laravel y es transparente para el desarrollador, ya que Blade lo hace todo por nosotros. Sin embargo, si queremos depurar o entender cómo se están manejando los errores, podemos observar estos fragmentos PHP generados.*

- **En resumen:**
  - ***Blade** convierte el código HTML con directivas Laravel en código PHP optimizado.*
  - *Este código PHP a veces es difícil de leer para los humanos, pero está optimizado para la ejecución rápida y eficiente.*
  - *El código generado incluye **manejo de errores**, **validaciones** y **lógica dinámica** que facilita el desarrollo, pero hace que el archivo PHP resultante sea largo y complejo.*
  - *Aunque el código es ilegible, podemos **formatearlo manualmente** para entender mejor su funcionamiento.*

*Esta compilación permite que el servidor renderice las vistas dinámicamente y con la menor cantidad de procesamiento posible durante la ejecución.*

**El código de Blade original:**

```php
<div class="row mb-3">
    <label for="name" class="col-md-4 col-form-label text-md-end">Name</label>

    <div class="col-md-6">
        <input id="name" type="text" class="form-control @error('name') is-invalid @enderror" name="name" autocomplete="name" autofocus>
    @error('name')
        <span class="invalid-feedback" role="alert">
            <strong>{{ $message }}</strong>
        </span>
    @enderror
    </div>
</div>
```

**Se compila en:**

```php
<?php
    $__errorArgs = ['name'];
    $__bag = $errors->getBag( $__errorArgs[1] ?? 'default' );
    if ( $__bag->has( $__errorArgs[0] ) ) :
    if ( isset( $message ) ) { $__messageOriginal = $message; }
    $message = $__bag->first( $__errorArgs[0] );
?> is-invalid

<?php unset($message);
    if (isset($__messageOriginal)) { $message = $__messageOriginal; } endif;
    unset($__errorArgs, $__bag);
?>

<?php
    $__errorArgs = ['name'];
    $__bag = $errors->getBag( $__errorArgs[1] ?? 'default' );
    if ( $__bag->has( $__errorArgs[0] ) ) :
    if ( isset( $message ) ) { $__messageOriginal = $message; }
    $message = $__bag->first( $__errorArgs[0] );
?>

<span class="invalid-feedback" role="alert">
    <strong> <?php echo e($message); ?> </strong>
</span>

<?php
    unset( $message );

    if ( isset( $__messageOriginal) ) { $message = $__messageOriginal; }
    endif;
    unset( $__errorArgs, $__bag );
?>
```

---

## **Explicación detallada del código compilado**

### **Gestión de errores en Laravel Blade**

*El código generado maneja los errores de validación de Laravel usando la variable `$errors`, la cual es automáticamente inyectada en las vistas cuando utilizamos `@error('campo')` en Blade.*

#### **Desglose del código generado**

```php
$__errorArgs = ['name'];
```

- *Se define un array con el nombre del campo a validar (`name`).*

```php
$__bag = $errors->getBag( $__errorArgs[1] ?? 'default' );
```

- **Se obtiene el *bag* de errores (conjunto de mensajes de error) correspondiente al campo `name`.**
- **Laravel permite definir múltiples *bags* de errores, aunque si no se especifica uno, se usa `default`.**

```php
if ( $__bag->has( $__errorArgs[0] ) ) :
```

- *Se verifica si el campo `name` tiene errores de validación.*

```php
$message = $__bag->first( $__errorArgs[0] );
```

- *Se obtiene el primer mensaje de error asociado al campo `name`.*

```php
<span class="invalid-feedback" role="alert">
    <strong> <?php echo e( $message ); ?> </strong>
</span>
```

- *Se muestra el mensaje de error dentro de un `span` con la clase `invalid-feedback`, lo que permite aplicar estilos de Bootstrap.*

```php
unset( $__errorArgs, $__bag );
```

- *Se eliminan las variables temporales para evitar conflictos en la vista.*

---

## **¿Por qué el código generado es ilegible?**

1. **Optimización:** *Laravel genera código eficiente, pero difícil de leer para humanos.*
2. **Conversión de directivas Blade:** *Las directivas como `@error` se transforman en PHP puro.*
3. **Manejo de variables temporales:** *Laravel usa nombres como `__errorArgs` para evitar conflictos con otras variables.*

- **Conclusión**
  - *Laravel compila vistas Blade en PHP puro y optimiza el código para ejecución eficiente.*
  - *El código resultante es difícil de leer porque usa variables temporales y estructuras dinámicas.*
  - *Podemos encontrar y analizar estas vistas compiladas en `storage/framework/views`.*
  - *El comando `grep -iEwr "Create New Contact"` nos ayuda a localizar el archivo exacto donde se encuentra el texto deseado.*
  - *Cada flag en `grep` tiene una función específica para mejorar la búsqueda.*

---

### **Contexto y Preparación**

- *Antes de empezar a ver los detalles de la validación, eliminaremos los atributos `required` de los campos de entrada HTML y se cambia el `type="text"`. Esto es porque, en lugar de dejar que el navegador valide los campos, vamos a hacer toda la validación en el backend usando Laravel. Laravel ofrece un sistema muy robusto para la validación de formularios, que podemos usar para asegurarnos de que los datos recibidos sean correctos.*

### **1. Validación en el Controlador:**

*Primero, vamos a trabajar en el controlador **`ContactController.php`**. Aquí es donde se procesa la solicitud POST para crear un nuevo contacto. Usamos el método **`validate`** de Laravel para realizar la validación de los datos.*

#### **Código del controlador para validación básica**

```php
/**
 * Store a newly created resource in storage.
 *
 * @param  \Illuminate\Http\Request  $request
 * @return \Illuminate\Http\Response
 */
public function store(Request $request)
{
    // Validación de los campos 'name', 'phone_number', 'email', 'age'
    // Aseguramos que los campos sean requeridos
    $request->validate([
        "name" => "required",         // 'name' es un campo obligatorio
        "phone_number" => "required", // 'phone_number' es obligatorio
        "email" => "required",        // 'email' es obligatorio
        "age" => "required",          // 'age' es obligatorio
    ]);
    
    // Si pasa la validación, respondemos con un mensaje de éxito
    return response("Contact Created");
}
```

**Explicación de la validación:**

- **`$request->validate()`:** *Este método de Laravel toma un array donde se definen las reglas de validación para cada campo. Si algún campo no pasa la validación, Laravel automáticamente redirige al usuario de vuelta al formulario con los mensajes de error.*
  
- **Reglas de validación:**
  - **`required`:** *Significa que el campo es obligatorio. Si no se proporciona un valor, se generará un error de validación.*

---

### **2. Validación Avanzada:**

*Ahora, vamos a hacer la validación más avanzada, añadiendo reglas adicionales, como la validación para el correo electrónico y el número de teléfono.*

#### **Código de validación avanzada**

```php
$request->validate([
    "name" => "required",                                 // 'name' sigue siendo obligatorio
    "phone_number" => ["required", "email"],              // 'phone_number' debe ser obligatorio y tener 9 dígitos
    "email" => ["required", "digits:9"],                  // 'email' es obligatorio y debe ser un email
    "age" => ["required", "numeric", "min:1", "max:255"], // 'age' debe ser numérico y entre 1 y 255
]);
```

**Explicación de las nuevas reglas:**

- **`phone_number`:**
  - **`required`:** *El campo es obligatorio, es decir, no puede dejarse vacío.*
  - **`digits:9`:** *Asegura que el campo contenga exactamente 9 dígitos. Esta regla es adecuada para validar números que tienen una longitud fija de dígitos, como un número de teléfono o una identificación. Sin embargo, para validar un número de teléfono, generalmente es mejor usar una expresión regular o la regla `numeric` si no te importa el formato exacto.*
  - **Solución recomendada:** *Para un número de teléfono, puedes considerar el uso de `numeric` o una validación con una expresión regular que permita incluir guiones, paréntesis, etc., si necesitas un formato específico. Si solo se requiere un número, `numeric` es más adecuado que `digits`.*

- **`email`:**
  - **`required`:** *Este campo es obligatorio.*
  - **`email`:** *La regla `email` asegura que el campo contenga una dirección de correo electrónico válida, como `example@domain.com`. Es importante notar que en el ejemplo dado, el campo `phone_number` debería ser validado como un número, no como un correo electrónico. Si se quiere validar que `phone_number` contenga un número, la regla apropiada sería `numeric`, no `email`.*

- **`age`:**
  - **`required`:** *Es obligatorio.*
  - **`numeric`:** *Asegura que el valor sea un número.*
  - **`min:1`:** *El valor debe ser al menos 1.*
  - **`max:255`:** *El valor debe ser como máximo 255.*

---

### **3. Uso del Delimitador `|` para Validaciones:**

*También puedes usar el delimitador **`|`** para simplificar la definición de reglas de validación, especialmente cuando tienes múltiples reglas para un campo.*

#### **Ejemplo utilizando `|`**

```php
$request->validate([
    "name" => "required",                      // 'name' sigue siendo obligatorio
    "phone_number" => "required|digits:9",     // 'phone_number' es obligatorio y debe ser un email
    "email" => "required|email",               // 'email' debe ser obligatorio y tener 9 dígitos
    "age" => "required|numeric|min:1|max:255", // 'age' debe ser numérico y entre 1 y 255
]);
```

**Explicación:**

- *Cada campo puede tener múltiples reglas separadas por el **`|`**. Esto es más limpio y compacto que pasar un array con cada regla como en el ejemplo anterior.*
  
---

### **4. Mantener los Valores del Formulario Después de la Validación:**

*Después de que se realiza la validación y los datos no son correctos, Laravel redirige de vuelta al formulario, pero se pierden los valores previamente ingresados. Para evitar esto y mantener los valores introducidos por el usuario, usamos la directiva **`old()`** en Blade.*
*Por ejemplo, si el usuario ya escribió un nombre y un número de teléfono, al fallar la validación, podemos volver a llenar los campos con los valores que el usuario ya había ingresado:*

#### **Formulario con valores antiguos**

```php
<input id="name" type="text" class="form-control @error('name') is-invalid @enderror" value="{{ old('name') }}" name="name" autocomplete="name" autofocus>
```

**Explicación de `old('name')`:**

- **`old('name')`:** *Esta función recupera el valor anterior de un campo dado, en este caso, el campo **`name`**. Si el formulario fue enviado y falló la validación, Laravel pasa los valores previos al formulario, para que el usuario no tenga que volver a escribir toda la información.*
- **`@error('name')`:** *Esta directiva se usa para mostrar errores de validación para el campo **`name`**. Si hay un error, se aplica la clase **`is-invalid`** al campo de entrada, lo que puede activar un estilo CSS que resalte el campo como incorrecto.*

---

### **5. Agregar `required` en los campos HTML:**

*Al final, si queremos agregar la validación del lado del cliente, podemos usar el atributo **`required`** en los campos del formulario. Esto asegura que el navegador valide los campos antes de enviarlos al servidor. Sin embargo, esto no debe ser el único nivel de validación, ya que la validación del lado del servidor siempre debe ser la principal.*

#### **Ejemplo con `required` en los campos**

```php
<input id="name" type="text" class="form-control @error('name') is-invalid @enderror" value="{{ old('name') }}" name="name" autocomplete="name" autofocus required>
```

- **`required`:** *Esto asegura que el campo no puede estar vacío en el navegador antes de que el formulario sea enviado al servidor.*

---

### **Conclusión:**

- *Laravel ofrece un sistema robusto para la **validación de datos** tanto en el cliente como en el servidor.*
- *La validación del lado del servidor es la más confiable, pero **puedes agregar validación del lado del cliente** para mejorar la experiencia del usuario.*
- **`old('field')`** *es fundamental para mantener los valores en los formularios después de una validación fallida.*
- **`required`** *en HTML se utiliza para la validación rápida del navegador, pero siempre debe complementarse con la validación del servidor.*

- *[Laravel 12.x Validation Documentation](https://laravel.com/docs/12.x/validation "https://laravel.com/docs/12.x/validation")*
- *[Available Validation Rules (Reglas de Validación Disponibles)](https://laravel|.com/docs/12.x/validation#available-validation-rules "https://laravel.com/docs/12.x/validation#available-validation-rules")*
