<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# **Método `destroy` en Laravel**

## **1. Formulario HTML para eliminar un recurso**

**Ubicación: `resources/views/home.blade.php`**

```php
<form action="{{ route('contacts.destroy', ['contact' => $contact->id]) }}" method="POST">
    @csrf
    @method("DELETE")
    <button type="submit" class="btn btn-danger mb-2">Delete Contact</button>
</form>
```

### **Explicación detallada**

- *`<form>`: Etiqueta HTML para crear un formulario.*
- *`action="{{ route('contacts.destroy', ['contact' => $contact->id]) }}"`:*
  - *`action`: Atributo que indica la URL a la que se enviarán los datos del formulario.*
  - *`route(...)`: Función de Laravel que genera la URL correspondiente a una ruta nombrada.*
    - *`'contacts.destroy'`: Nombre de la ruta definida en `web.php`.*
    - *`['contact' => $contact->id]`: Parámetro dinámico enviado en la ruta. Se pasa el identificador del contacto.*

- **`method="POST"`:**
  - *Todos los formularios HTML solo permiten los métodos `GET` y `POST`.*
  - *Para enviar una solicitud `DELETE`, Laravel requiere un campo oculto con la directiva `@method`.*

- **`@csrf`:**
  - *Directiva de Blade que incluye un token `CSRF (Cross-Site Request Forgery)`.*
  - *Protege el formulario contra ataques maliciosos evitando que formularios externos puedan realizar peticiones sin autorización.*

- **`@method("DELETE")`:**
  - *Esta directiva agrega un campo oculto `_method` con valor `DELETE`.*
  - *Laravel usa este campo para simular el método HTTP `DELETE`.*

- *`<button type="submit">`: Botón para enviar el formulario.*

---

## **2. Definición de la ruta**

**Ubicación: `routes/web.php`**

```php
Route::delete(
    uri: "/contacts/{contact:id}",
    action: [ContactController::class, "destroy"]
)->name(name: "contacts.destroy");
```

- **Explicación detallada**

- *`Route::delete(...)`:*
  - *Define una ruta HTTP que responde a solicitudes `DELETE`.*

- *`uri: "/contacts/{contact:id}"`:*
  - *`uri`: Segmento de la URL que identifica la ruta.*
  - *`{contact:id}`:*
    - *`{contact}`: Es una variable de ruta que representa un modelo `Contact`.*
    - *`:id`: Especifica que el campo `id` del modelo se usará para hacer la inyección automática del modelo.*

- **`action: [ContactController::class, "destroy"]`:**
  - *Se indica el controlador y método que manejarán la solicitud.*
  - *`ContactController::class`: Nombre del controlador.*
  - *`"destroy"`: Método del controlador.*

- *`->name(name: "contacts.destroy")`:*
  - *Nombra la ruta como `contacts.destroy`.*
  - *Permite generar URLs o redireccionamientos utilizando el nombre en lugar de escribir la URL completa.*

---

## **3. Método `destroy` en el controlador**

*Ubicación: `app/Http/Controllers/ContactController.php`*

```php
public function destroy(Contact $contact)
{
    dd($contact);
}
```

- **Explicación detallada**

- **`public function destroy(Contact $contact)`:**
  - **Define un método público llamado `destroy`.**
  - **Laravel utiliza *Route Model Binding*, por lo que inyecta automáticamente la instancia del modelo `Contact` correspondiente al `id` de la URL.**

- **`dd($contact)`:**
  - **`dd()` es una función auxiliar de Laravel que significa *Dump and Die*.**
  - **Muestra el contenido de `$contact` y detiene la ejecución del script.**
  - **Muy útil para depuración.**

---

## **4. Datos en la base de datos**

**Ejecutamos una consulta SQL para ver los registros actuales en la tabla `contacts`.**

```sql
SELECT * FROM contacts;
```

**Resultado:**

| **id** | **name**            | **phone_number** | **email**             | **age** | **created_at**        | **updated_at**        |
| ------ | ------------------- | ---------------- | --------------------- | ------- | --------------------- | --------------------- |
| *3*    | *Cristiano Ronaldo* | *123456789*      | *`ronaldo@gmail.com`* | *44*    | *2025-04-20 20:25:59* | *2025-04-20 21:30:04* |
| *4*    | *Messi*             | *123456789*      | *`messi@gmail.com`*   | *40*    | *2025-04-20 21:31:27* | *2025-04-20 21:31:27* |

- **Salida Al Hacer Petition `http://172.17.0.2:8000/contacts/4`**

```bash
App\Models\Contact {#648 ▼ // app/Http/Controllers/ContactController.php:167
  #connection: "pgsql"
  #table: "contacts"
  #primaryKey: "id"
  #keyType: "int"
  +incrementing: true
  #with: []
  #withCount: []
  +preventsLazyLoading: false
  #perPage: 15
  +exists: true
  +wasRecentlyCreated: false
  #escapeWhenCastingToString: false
  #attributes: array:7 [▼
    "id" => 4
    "name" => "messi"
    "phone_number" => "123456789"
    "email" => "messi@gmail.com"
    "age" => 40
    "created_at" => "2025-04-20 21:31:27"
    "updated_at" => "2025-04-20 21:31:27"
  ]
  #original: array:7 [▼
    "id" => 4
    "name" => "messi"
    "phone_number" => "123456789"
    "email" => "messi@gmail.com"
    "age" => 40
    "created_at" => "2025-04-20 21:31:27"
    "updated_at" => "2025-04-20 21:31:27"
  ]
  #changes: []
  #casts: []
  #classCastCache: []
  #attributeCastCache: []
  #dates: []
  #dateFormat: null
  #appends: []
  #dispatchesEvents: []
  #observables: []
  #relations: []
  #touches: []
  +timestamps: true
  #hidden: []
  #visible: []
  #fillable: array:4 [▼
    0 => "name"
    1 => "phone_number"
    2 => "age"
    3 => "email"
  ]
  #guarded: array:1 [▼
    0 => "*"
  ]
}
```

---

## **Método `destroy` actualizado en `ContactController`**

*Ubicación: `app/Http/Controllers/ContactController.php`*

```php
public function destroy(Contact $contact)
{
    $contact->delete();
    // El método destroy es estático y se usa para eliminar múltiples registros a la vez
    // Contact::destroy([1, 2, 3]);
    return redirect(to: "home");
}
```

- **Explicación detallada**

### **`$contact->delete();`**

- **Este método elimina **la instancia específica del modelo** de la base de datos.**
- **Se invoca sobre un objeto ya instanciado de `Contact`, que Laravel inyectó automáticamente usando *Route Model Binding*.**
- **Realiza una consulta `DELETE` con una cláusula `WHERE id = ?`, utilizando el ID del modelo.**

#### **Comentario sobre `destroy()`**

```php
// $contact->destroy();
```

- **Este comentario tiene un pequeño error conceptual. El método `destroy()` es **estático**, es decir, se invoca directamente sobre la clase y no sobre una instancia.**
- **Uso correcto:**
  
  ```php
  Contact::destroy(3); // elimina el contacto con ID 3
  Contact::destroy([3, 4, 5]); // elimina múltiples contactos por ID
  ```

- **No se usa `$contact->destroy()`, ya que esto no funcionará correctamente y puede generar errores.**

#### **`return redirect(to: "home");`**

- *Esta instrucción redirige al usuario después de completar la eliminación.*
- *Laravel proporciona el helper `redirect()` para facilitar las redirecciones HTTP.*
- `to: "home"`:
  - *`"home"` debe ser una ruta válida definida en `web.php`.*
  - *Alternativamente, puedes redirigir usando el nombre de una ruta:*

    ```php
    return redirect()->route("contacts.index");
    ```

---

### **Resultado tras enviar la solicitud**

**Después de enviar el formulario HTML con el método `DELETE`, y si el contacto fue eliminado exitosamente:**

- *Se ejecuta el método `destroy`.*
- *El registro correspondiente es eliminado de la base de datos.*
- *El usuario es redirigido a la vista asociada a `"home"`.*
