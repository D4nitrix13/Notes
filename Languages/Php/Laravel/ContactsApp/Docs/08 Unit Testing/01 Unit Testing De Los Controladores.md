<!-- Autor: Joker Batman Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- Gitlab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: Jokerperezdev@proton.me -->

# **Unit Testing de los Controladores en Laravel**

*El **unit testing** es una parte esencial del proceso de desarrollo para asegurar que cada parte de tu código funciona correctamente de forma aislada. En Laravel, podemos utilizar PHPUnit junto con la infraestructura que Laravel ofrece para realizar pruebas unitarias, específicamente para los controladores.*

## **Preparación del entorno de pruebas:**

1. **Cambiar de rama en Git:**

   *Para implementar una nueva funcionalidad o solución, primero cambiamos a la rama correspondiente. En este caso, vamos a cambiar a la rama `Challenge1`:*

   ```bash
   git switch Challenge1
   ```

   * **Comando:** *`git switch <branch>`*
   * **Descripción:** *Cambia a la rama especificada en el repositorio de Git.*
   * **Opciones:** *No hay subcomandos en este caso, pero puedes usar `git branch` para ver todas las ramas disponibles.*

2. **Generación de un test unitario para el controlador:**

   *El siguiente paso es generar un test unitario específico para el controlador `ProductController`. Para ello, usamos el comando:*

   ```bash
   php artisan make:test --unit ProductControllerUnitTest
   ```

   * **Comando:** *`php artisan make:test --unit <TestName>`*
   * **Descripción:** *Genera un archivo de prueba unitario. El flag `--unit` o `-u` especifica que es una prueba unitaria.*
   * **Opciones:**

     * ***`--unit`:** *Crea un test que no depende de un entorno de Laravel completo (sin interacción con la base de datos o rutas).**

   *Esto creará un archivo de prueba en `tests/Unit/ProductControllerUnitTest.php`.*

3. **Generación de una fábrica de productos:**

   *Para facilitar la creación de registros de productos durante las pruebas, se debe crear una fábrica para el modelo `Product`:*

   ```bash
   php artisan make:factory -m Product ProductFactory
   ```

   * **Comando:** *`php artisan make:factory <FactoryName> -m <ModelName>`*
   * **Descripción:** *Crea una fábrica para un modelo específico. El flag `-m` crea automáticamente una migración para la tabla relacionada.*
   * **Opciones:**

     * ***`-m <ModelName>`:** *Crea una migración para el modelo asociado a la fábrica (en este caso, `Product`).**
   * **Resultado:** *Esto generará un archivo en `database/factories/ProductFactory.php` que define cómo se generan los datos de prueba para los productos.*

### **Implementación del test en el controlador ProductController**

*A continuación, escribimos las pruebas unitarias para los métodos del controlador `ProductController`, en específico para la creación de un usuario y la creación de un producto.*

```php
<?php

namespace Tests\Unit;

use App\Models\Product;
use App\Models\User;
use Illuminate\Foundation\Testing\RefreshDatabase;

// use PHPUnit\Framework\TestCase;

use Tests\TestCase;


class ProductControllerUnitTest extends TestCase
{
    use RefreshDatabase;
    public function testCreateUser()
    {
        $user = User::factory()->create([
            'name' => 'Joker',
            'email' => 'joker@email.com',
        ]);

        $this->assertDatabaseHas('users', [
            'id' => $user->id,
            'name' => 'Joker',
            'email' => 'joker@email.com',
        ]);
    }

    public function testCreateProduct()
    {
        $product = Product::factory()->create();

        $this->assertDatabaseHas('products', [
            'id' => $product->id,
            'name' => $product->name,
            'description' => $product->description,
            'price' => $product->price,
            'user_id' => $product->user_id,
        ]);
    }
}
```

### **Explicación del código**

1. **Test para crear un usuario (`testCreateUser`):**

   * **Fábrica:** *Utilizamos `User::factory()->create()` para crear un nuevo usuario con un nombre y correo electrónico específico.*
   * **Verificación:** *Usamos `$this->assertDatabaseHas()` para comprobar que el usuario se ha guardado correctamente en la base de datos con los valores esperados.*

2. **Test para crear un producto (`testCreateProduct`):**

   * **Fábrica:** *Similar al test de usuario, utilizamos `Product::factory()->create()` para crear un producto.*
   * **Verificación:** *Comprobamos que el producto se haya guardado correctamente en la base de datos, verificando todos sus atributos (`name`, `description`, `price`, `user_id`).*

### **Consideraciones adicionales**

* **Uso de `RefreshDatabase`:** *La trait `RefreshDatabase` es utilizada para restablecer la base de datos después de cada prueba, asegurando que no haya datos persistentes entre pruebas.*
* **Asserts disponibles:**

  * **`assertDatabaseHas`:** *Verifica que los datos existen en la base de datos.*
  * **`assertEquals`:** *Verifica que dos valores sean iguales.*

### **Ejecutando los tests**

**Para ejecutar las pruebas, puedes usar el siguiente comando:**

```bash
php artisan test
```

* **Y Tambien**

```bash
php artisan test tests/Unit/
```

*Este comando ejecutará todas las pruebas, incluidas las pruebas unitarias en `tests/Unit/ProductControllerUnitTest.php`.*

---

### *Resumen de los pasos clave*

1. **Crear un test unitario** *para el controlador: `php artisan make:test --unit ProductControllerUnitTest`*
2. **Crear una fábrica de productos:** *`php artisan make:factory -m Product ProductFactory`*
3. **Escribir pruebas** *para la creación de usuarios y productos, verificando que los datos se guardan correctamente en la base de datos.*
4. **Ejecutar los tests:** *`php artisan test`*

---

### **Nombres Recomendados Para Una Clase Example: `ProductController`:**

#### **1.*Feature Test:**

*Un **Feature Test** verifica la funcionalidad completa de una característica o flujo de trabajo del sistema, como la interacción entre rutas, controladores, base de datos, validación, etc.*

*La convención para un **Feature Test** relacionado con el controlador `ProductController` sería:*

* **Nombre del archivo:** *`ProductControllerTest.php`*
* **Ubicación:** *`tests/Feature/`*

*El nombre **`ProductControllerTest`** refleja que la prueba está verificando la funcionalidad del controlador `ProductController`.*

#### **2. Unit Test:**

*Un **Unit Test** verifica el comportamiento aislado de un componente específico, como un método de clase, sin interactuar con la base de datos o la aplicación externa. Generalmente, un **Unit Test** de un controlador no se recomienda, ya que los controladores gestionan solicitudes HTTP y lógica de múltiples componentes, pero en algunos casos, puedes tener pruebas unitarias para funciones de lógica interna del controlador si se extraen y encapsulan.*

*Si necesitas escribir un **Unit Test** para una clase o método relacionado con `ProductController`, podrías llamarlo:*

* **Nombre del archivo:** *`ProductControllerUnitTest.php`*
* **Ubicación:** *`tests/Unit/`*

*Sin embargo, como mencioné, los controladores generalmente no se prueban a nivel de unidad, a menos que sea para algún método de lógica de negocio específico dentro de él.*

### **Resumiendo las convenciones:**

* *Para un **Feature Test** de un controlador, el nombre del archivo sería: **`ProductControllerTest.php`**, y se encuentra en `tests/Feature/`.*
* *Para un **Unit Test** (aunque poco común para un controlador), el nombre del archivo sería: **`ProductControllerUnitTest.php`**, y se encuentra en `tests/Unit/`.*

---

## **En Laravel puedes utilizar tanto `PHPUnit\Framework\TestCase` como `Tests\TestCase` para escribir tus pruebas unitarias (unit tests). La diferencia radica en el propósito y las características adicionales que ofrece cada uno.**

### **`PHPUnit\Framework\TestCase`**

* **Propósito:** *Es la clase base proporcionada por PHPUnit para escribir pruebas unitarias en PHP.*

* **Uso:** *Ideal para pruebas que no requieren interacción con Laravel, como pruebas de lógica de negocio aislada.*

* **Ejemplo:**

  ```php
  use PHPUnit\Framework\TestCase;

  class MiTest extends TestCase
  {
      public function testSum()
      {
        $this->assertEquals(expected: 5, actual: 2 + 3);
      }
  }
  ```

* **Ventaja:** *Ligero y rápido, sin dependencias adicionales.*

---

### **`Tests\TestCase` (Base de pruebas de Laravel)**

* **Propósito:** *Es una clase base personalizada de Laravel que extiende `PHPUnit\Framework\TestCase` y agrega funcionalidades específicas de Laravel.*

* **Uso:** *Ideal para pruebas que interactúan con el framework, como pruebas de controladores, modelos, rutas, bases de datos, etc.*

* **Características adicionales:**

  * *Soporte para migraciones y bases de datos en memoria.*
  * *Acceso a helpers de Laravel como `artisan`, `assertDatabaseHas`, `assertSee`, entre otros.*
  * *Integración con el contenedor de servicios de Laravel.*

* **Ejemplo:**

  ```php
  namespace Tests\Unit;

  use Tests\TestCase;
  use App\Models\User;

  class UserTest extends TestCase
  {
      public function testCreateUser()
      {
          $user = User::factory()->create([
              'name' => 'Joker',
              'email' => 'joker@example.com',
          ]);

          $this->assertDatabaseHas('users', [
              'name' => 'Joker',
              'email' => 'joker@example.com',
          ]);
      }
  }
  ```

* **Ventaja:** *Proporciona un entorno de prueba completo con todas las herramientas de Laravel.*

---

### **¿Cuál deberías usar?**

* **`PHPUnit\Framework\TestCase`:** *Úsalo para pruebas puras de PHP que no dependen de Laravel. Es más rápido y ligero.*
* **`Tests\TestCase`:** *Úsalo para pruebas que requieren la infraestructura de Laravel, como pruebas de controladores, rutas, bases de datos, etc.*

---

### **Ejemplo de prueba unitaria con `PHPUnit\Framework\TestCase`**

```php
namespace Tests\Unit;

use PHPUnit\Framework\TestCase;

class CalculadoraTest extends TestCase
{
    public function testSum()
    {
        $this->assertEquals(expected: 5, actual: 2 + 3);
    }
}
```

### **Ejemplo de prueba con `Tests\TestCase` en Laravel**

```php
namespace Tests\Unit;

use Tests\TestCase;
use App\Models\User;

class UserTest extends TestCase
{
    public function testCreateUser()
    {
        $user = User::factory()->create([
            'name' => 'Carol',
            'email' => 'carol@example.com',
        ]);

        $this->assertDatabaseHas('users', [
            'name' => 'Carol',
            'email' => 'carol@example.com',
        ]);
    }
}
```

---

### **Conclusión**

* **`PHPUnit\Framework\TestCase`:** *Ideal para pruebas unitarias puras sin dependencias de Laravel.*
* **`Tests\TestCase`:** *Recomendado para pruebas que interactúan con el framework Laravel, ya que proporciona herramientas y helpers específicos.*
