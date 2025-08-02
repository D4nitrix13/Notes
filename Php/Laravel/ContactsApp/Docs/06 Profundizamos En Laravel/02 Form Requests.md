<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- Gitlab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# **Form Requests**

*En Laravel, la validación de datos es una parte esencial del flujo de trabajo de los formularios. Normalmente, cuando recibimos datos de una petición HTTP (por ejemplo, desde un formulario), debemos asegurarnos de que la información esté bien estructurada antes de almacenarla en la base de datos.*

*Una **buena práctica** es **centralizar las reglas de validación** para no repetirlas en cada método como `store()` o `update()`.*

## **Estructura general del controlador con reglas protegidas**

```php
class ContactController extends Controller
{
    // Atributo protegido que almacena las reglas de validación
    protected $rules = [
        "name" => "required",
        "phone_number" => "required|digits:9",
        "email" => "required|email",
        "age" => "required|numeric|min:1|max:255"
    ];

    public function store(Request $request)
    {
        // Aplica las reglas de validación usando el atributo $rules
        $data = $request->validate($this->rules);

        // Aquí podrías guardar $data en la base de datos...
    }
}
```

---

## **Desglose de cada parte del código**

### **`protected $rules = [...]`**

* *`protected`: Especifica que el atributo solo puede usarse dentro de la clase o en clases hijas (herencia).*
* *`$rules`: Es una variable de clase (atributo) que almacena las reglas de validación.*
* *`[...]`: Es un arreglo asociativo (clave-valor) donde:*

  * *la **clave** representa el nombre del campo del formulario (`name`, `phone_number`, etc.).*
  * *el **valor** es un string con reglas de validación separadas por `|`.*

---

## **Explicación de cada regla de validación**

### **1. `"name" => "required"`**

* *`required`: Esta regla indica que el campo **no puede estar vacío**. Laravel mostrará un error si no se envía este campo en el formulario.*

---

### **2. `"phone_number" => "required|digits:9"`**

* *`required`: el campo debe estar presente.*
* *`digits:9`: el valor **debe contener exactamente 9 dígitos numéricos**. No más, no menos, y **solo números**. No permite letras ni espacios.*

---

### **3. `"email" => "required|email"`**

* *`required`: obligatorio.*
* *`email`: verifica que el valor tenga un formato válido de correo electrónico.*
  *Por ejemplo: `persona@example.com`*

* *Internamente, Laravel usa una expresión regular compatible con RFC y el validador nativo de PHP (`FILTER_VALIDATE_EMAIL`).*

---

### **4. `"age" => "required|numeric|min:1|max:255"`**

* *`required`: obligatorio.*
* *`numeric`: debe ser un **número**, ya sea entero o decimal.*
* *`min:1`: el valor numérico mínimo permitido es 1.*
* *`max:255`: el valor numérico máximo permitido es 255.*

* *Esto no significa que el número de caracteres sea 255, sino que el **valor numérico** debe estar entre 1 y 255*.

---

## **`request->validate($this->rules)`**

* *`$request`: es una instancia de `Illuminate\Http\Request`, representa la petición HTTP entrante.*
* *`validate(...)`: método que:*

  1. *Recibe un arreglo de reglas (como `$this->rules`).*
  2. *Valida los datos del formulario automáticamente.*
  3. *Si todo está bien, **retorna un array con los datos validados** (`$data`).*
  4. *Si hay errores, **redirige automáticamente** al formulario anterior con los errores cargados en la sesión (Laravel maneja esto automáticamente si usás `@error`, `old()`, etc.).*

---

## **Ventajas de usar `$this->rules` en lugar de repetir las reglas**

* *Centralización: Evita repetir las reglas en múltiples métodos (`store`, `update`).*
* *Fácil mantenimiento: Si querés cambiar una regla, solo lo hacés en un lugar.*
* *Claridad y orden: Mejora la legibilidad del controlador.*

---

## **Ejemplo de entrada válida**

```json
{
  "name": "Daniel Pérez",
  "phone_number": "84675321",
  "email": "daniel@example.com",
  "age": "32"
}
```

---

## **Ejemplo de entrada inválida**

```json
{
  "name": "",
  "phone_number": "1234",
  "email": "correo-no-valido",
  "age": "500"
}
```

**Errores esperados:**

* *name requerido*
* *phone_number debe tener 9 dígitos exactos*
* *email tiene un formato incorrecto*
* *age debe estar entre 1 y 255*

---

## **¿Qué es Form Request Validation en Laravel?**

*[Form Request Validation](https://laravel.com/docs/11.x/validation#form-request-validation "https://laravel.com/docs/11.x/validation#form-request-validation")*
*[Authorizing Form Requests](https://laravel.com/docs/11.x/validation#authorizing-form-requests "https://laravel.com/docs/11.x/validation#authorizing-form-requests")*

*Es una técnica de Laravel para **separar la lógica de validación** del controlador. En lugar de escribir las reglas directamente en métodos como `store()` o `update()`, creamos una clase especial que contiene toda la validación. Esto mejora la organización del código y lo hace más mantenible.*

---

## **Comando para generar una clase de validación (Form Request)**

```bash
php artisan make:request StoreContactRequest
```

### **Explicación de cada parte**

* *`php artisan`: herramienta de línea de comandos integrada en Laravel. Sirve para generar clases, correr migraciones, ejecutar pruebas, etc.*
* *`make:request`: subcomando que **genera una clase de Form Request personalizada**.*
* *`StoreContactRequest`: nombre que le damos a la clase de validación. Por convención, usamos `Store...Request` para peticiones `POST`, y `Update...Request` para peticiones `PUT` o `PATCH`.*

* **Esto crea el archivo:**

```bash
app/Http/Requests/StoreContactRequest.php
```

**Y Laravel mostrará en consola:**

```bash
INFO  Request [app/Http/Requests/StoreContactRequest.php] created successfully.
```

---

## **Código generado automáticamente**

```php
<?php

namespace App\Http\Requests;

use Illuminate\Foundation\Http\FormRequest;

class StoreContactRequest extends FormRequest
{
    public function authorize()
    {
        return false;
    }

    public function rules()
    {
        return [
            // Aquí van las reglas de validación
        ];
    }
}
```

---

### **¿Qué significa cada método?**

#### `authorize()`

* *Este método determina si el usuario está **autorizado para hacer esta solicitud**.*
* *Devuelve `false` por defecto. Si lo dejás así, Laravel bloqueará la solicitud con un error 403.*
* *Lo común es poner `return true;` para permitir la solicitud:*

```php
public function authorize()
{
    return true;
}
```

```php
public function authorize(): bool
{
    // $contact = Contact::find(
    //     $this->route('contact')
    // );
    // return $contact && $this->user()->can('update', $contact);
    return true;
}
```

**Si necesitás más control, podés validar con lógica condicional o con políticas (Policies).**

---

#### **`rules()`**

*Aquí se definen las **reglas de validación** usando el mismo formato que usás en `$request->validate([...])`.*

**Ejemplo completo:**

```php
public function rules()
{
    return [
        "name" => "required|string|max:255",
        "phone_number" => "required|digits:9",
        "email" => "required|email",
        "age" => "required|numeric|min:1|max:255"
    ];
}
```

---

## **Cambiar el tipo de parámetro en el controlador**

### **Antes**

```php
public function store(Request $request)
{
    $data = $request->validate([
        // reglas aquí
    ]);
}
```

### **Después**

```php
use App\Http\Requests\StoreContactRequest;

public function store(StoreContactRequest $request)
{
    // Los datos ya están validados al llegar aquí
    $contact = auth()->user()->contacts()->create($request->validated());
}
```

---

## **`$request->validated()`**

* *Este método retorna **únicamente los datos validados**, descartando cualquier dato adicional no incluido en las reglas.*
* *Es seguro usarlo directamente para crear registros en la base de datos:*

```php
auth()->user()->contacts()->create($request->validated());
```

---

## **Ventajas de usar Form Request**

| **Ventaja**       | **Explicación**                                                                                     |
| ----------------- | --------------------------------------------------------------------------------------------------- |
| *Código limpio*   | *Los controladores se enfocan en la lógica del negocio, no en la validación.*                       |
| *Reutilización*   | *Podés usar la misma clase `StoreContactRequest` en varios métodos.*                                |
| *Seguridad*       | *Solo se procesan los campos definidos en las reglas.*                                              |
| *Personalización* | *Podés sobrescribir métodos como `messages()` o `attributes()` para mostrar errores más amigables.* |

---

---

## **¿Y para `update()`?**

**Podés crear otra clase:**

```bash
php artisan make:request UpdateContactRequest
```

**Y cambiar el método `update()`:**

```php
public function update(UpdateContactRequest $request, Contact $contact)
{
    $contact->update($request->validated());
}
```

*Si las reglas son idénticas, podés compartir la misma clase o incluso mover las reglas a un **trait** reutilizable.*
