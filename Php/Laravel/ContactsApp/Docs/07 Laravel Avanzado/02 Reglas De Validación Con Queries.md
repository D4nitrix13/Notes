<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- Gitlab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# **Reglas de Validación con Queries en Laravel**

## **File `app/Http/Requests/StoreContactRequest.php`**

```php
public function rules()
{
    return [
        "name" => "required",
        "phone_number" => "required|digits:9",
        "email" => "required|email|unique:contacts,email",
        "age" => "required|numeric|min:1|max:255",
        'profile_picture' => 'image|mimes:jpeg,png,jpg|max:2048',
    ];
}
```

### **Explicación de cada regla**

| **Campo**           | **Reglas**                                     | **Explicación**                                                                                                       |
| ------------------- | ---------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| *`name`*            | *`required`*                                   | *Campo obligatorio, no puede estar vacío.*                                                                            |
| *`phone_number`*    | *`required`, `digits:9`*                       | *Obligatorio y debe contener exactamente 9 dígitos numéricos.*                                                        |
| *`email`*           | *`required`, `email`, `unique:contacts,email`* | *Obligatorio, debe tener formato válido de correo y no puede repetirse en la columna `email` de la tabla `contacts`.* |
| *`age`*             | *`required`, `numeric`, `min:1`, `max:255`*    | *Obligatorio, solo acepta números, y debe estar entre 1 y 255.*                                                       |
| *`profile_picture`* | *`image`, `mimes:jpeg,png,jpg`, `max:2048`*    | *Opcional, pero si se envía, debe ser una imagen de tipo JPEG, PNG o JPG y pesar máximo 2048 KB (2 MB).*              |

---

## **Problema: Validación de correo única pero por usuario**

**El uso de:**

```php
"email" => "unique:contacts,email"
```

*valida que **ningún usuario** tenga un correo repetido. Pero en una app multiusuario, eso es incorrecto.*

> [!NOTE]
> **Queremos que un mismo correo no se repita solo entre los contactos de *un mismo usuario*.**

*Además, al editar un contacto existente, este código también fallará, ya que Laravel detectará el mismo correo como duplicado (aunque no haya cambiado).*

---

## **Solución: Validar correo único por usuario, ignorando el propio registro al editar**

```php
use Illuminate\Validation\Rule;

public function rules()
{
    return [
        "name" => "required",
        "phone_number" => "required|digits:9",
        "email" => [
            "required",
            "email",
            Rule::unique("contacts", "email")
                ->where("user_id", auth()->id())
                ->ignore(request()->route("contact")),
        ],
        "age" => "required|numeric|min:1|max:255",
        'profile_picture' => 'image|mimes:jpeg,png,jpg|max:2048',
    ];
}
```

### **Detalles del uso de `Rule::unique`**

```php
Rule::unique("contacts", "email")
```

* **Valida que el valor del campo `email` sea único en la columna `email` de la tabla `contacts`.**

```php
->where("user_id", auth()->id())
```

* *Añade una condición extra a la validación: que el campo `user_id` coincida con el ID del usuario autenticado.*
* *Así se asegura que los correos sean únicos **por usuario**, no globalmente.*

```php
->ignore(request()->route("contact"))
```

* **Evita fallos al editar.** *Ignora el registro actual (obtenido de la ruta `contact`) para que no lo considere duplicado.*

---

## **Mensajes personalizados**

```php
public function messages()
{
    return [
        "email.unique" => "You already have a contact with this email"
    ];
}
```

* *Define un mensaje de error personalizado cuando falle la validación `unique` del email.*
