<!-- Autor: Joker Batman Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- Gitlab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: Jokerperezdev@proton.me -->

# **Test-Driven Development (TDD)**

> [!NOTE]
> ***Test-Driven Development (TDD)** es una metodología de desarrollo en la que escribes **pruebas antes** de escribir el código que implementa la funcionalidad. Los **unit tests** y **feature tests** son herramientas que se usan en TDD, pero TDD no se limita solo a esos tipos de pruebas. Te explico cómo encajan estos conceptos dentro de TDD:*

## **¿Qué es TDD?**

**Test-Driven Development** *es un enfoque de desarrollo de software en el que se sigue un ciclo iterativo compuesto por los siguientes pasos:*

1. **Escribir una prueba:** *Primero escribes una prueba que describe una pequeña parte de la funcionalidad que necesitas implementar. Esta prueba **debe fallar** inicialmente, porque aún no has implementado la funcionalidad.*

2. **Escribir el código:** *Luego escribes el código mínimo necesario para hacer que esa prueba pase. En este punto, solo escribes la lógica suficiente para que la prueba sea exitosa, sin agregar funcionalidad adicional.*

3. **Refactorizar:** *Finalmente, refactorizas el código, optimizando su estructura y asegurándote de que todas las pruebas sigan pasando.*

4. **Repetir:** *Repites el ciclo para agregar nuevas funcionalidades.*

### **Unit Test vs Feature Test en TDD**

#### **Unit Tests en TDD**

*Los **unit tests** son pruebas que verifican el funcionamiento de una **unidad específica de código** (por lo general, una clase o método) de forma aislada. En el contexto de TDD, estos tests se escriben **antes** de escribir la implementación de la unidad que estás probando. Se utilizan para asegurarse de que las pequeñas unidades de código funcionen de manera independiente.*

**Ejemplo:**
*Supón que tienes una clase `Calculator` con un método `add()`. En TDD, primero escribirías un test unitario que verifique que el método `add()` devuelve la suma correcta:*

```php
public function test_addition()
{
    $calculator = new Calculator();
    $result = $calculator->add(1, 2);
    $this->assertEquals(3, $result);
}
```

*Este test debe fallar inicialmente (si el método `add()` no está implementado). Luego, implementas la clase `Calculator` para que la prueba pase:*

```php
class Calculator
{
    public function add($a, $b)
    {
        return $a + $b;
    }
}
```

**Después, refactorizas el código si es necesario.**

#### **Feature Tests en TDD**

> [!NOTE]
> *Los **feature tests** son pruebas más amplias que verifican la funcionalidad completa de una **característica** o **función** del sistema. A menudo implican **interacciones con el sistema**, como solicitudes HTTP, acceso a la base de datos y respuestas de la API. En TDD, los feature tests también se escriben antes de implementar la funcionalidad.*

**Ejemplo:**
*Supón que tienes un controlador `ProductController` con un método `store()` que crea un producto. En TDD, primero escribirías un test de características (feature test) que verifica que el producto se crea correctamente cuando se hace una solicitud POST a la ruta correspondiente:*

```php
public function test_product_creation()
{
    $user = User::factory()->create();

    $data = [
        'name' => 'Keyboard',
        'description' => 'Mechanical keyboard',
        'price' => 200
    ];

    $response = $this->actingAs($user)->post(route('products.store'), $data);

    $response->assertStatus(201);
    $this->assertDatabaseHas('products', $data);
}
```

*Este test verificará que el proceso de creación de un producto funciona correctamente, desde la solicitud hasta la inserción en la base de datos. El test inicialmente fallará, luego implementas el código necesario para que pase.*

### **TDD en Laravel:**

> [!NOTE]
> *En Laravel, puedes usar **unit tests** y **feature tests** dentro de una metodología TDD. Ambos tipos de pruebas ayudan a garantizar que el código sea funcional y que se cumplan los requisitos desde el principio. Laravel facilita la escritura de ambos tipos de pruebas con su marco de pruebas integrado, que incluye características como `php artisan make:test`, `actingAs()`, `assertDatabaseHas()`, entre otras.*

### **Ciclo TDD con PHPUnit en Laravel**

1. **Escribir el test** *(unitario o de características).*
2. **Ejecutar el test:** *Verás que el test falla inicialmente.*
3. **Escribir el código mínimo necesario** *para pasar el test.*
4. **Ejecutar el test de nuevo:** *Asegúrate de que el test pase.*
5. **Refactorizar** *el código si es necesario.*
6. **Repetir** *para la siguiente funcionalidad.*

### **¿Por qué usar TDD?**

* **Código más limpio y bien estructurado:** *Al escribir las pruebas antes del código, te fuerzas a pensar en la estructura y los requisitos del código de manera más clara.*
* **Detecta errores tempranos:** *Los errores se detectan más rápido porque siempre tienes pruebas que validan que el código esté funcionando correctamente.*
* **Mejora la cobertura de pruebas:** *TDD te obliga a escribir pruebas para cada pequeña unidad de funcionalidad, lo que lleva a una cobertura de pruebas más completa.*

### **En resumen:**

* **Unit Tests:** *Se enfocan en probar unidades pequeñas de código (métodos o clases).*
* **Feature Tests:** *Se enfocan en probar la funcionalidad completa del sistema, a menudo con interacciones más amplias, como solicitudes HTTP y consultas a la base de datos.*
* **TDD:** *En este enfoque, escribes tus pruebas antes de implementar la funcionalidad, ya sea unitarias o de características, para garantizar que tu código cumpla con los requisitos y sea de alta calidad.*
