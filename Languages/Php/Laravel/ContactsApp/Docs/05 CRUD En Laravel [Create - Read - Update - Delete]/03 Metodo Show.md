<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# **Método `show` en Laravel**

## **1. Crear La Vista**

```bash
touch resources/views/contacts/show.blade.php
```

**Explicación del comando:**

- *`touch`: comando de Unix que crea un archivo vacío si no existe.*
- *`resources/views/contacts/show.blade.php`: ruta donde se almacenan las vistas de Laravel. Aquí se crea la vista que se encargará de mostrar la información del contacto.*

---

### **2. Registrar la ruta en `routes/web.php`**

```php
Route::get(
    uri: '/contacts/{contact:id}/',
    action: [ContactController::class, 'show']
)->name(name: 'contacts.show');
```

**Explicación:**

- *`Route::get(...)`: define una ruta HTTP de tipo `GET`.*
- *`uri: '/contacts/{contact:id}/'`: indica la URL de acceso. Laravel hace "route-model binding" automático con `{contact:id}`:*
  - *`contact` se refiere al modelo `Contact`.*
  - *`id` indica que se usará la columna `id` de la tabla `contacts` para buscar el registro.*
- *`action: [ContactController::class, 'show']`: define que se ejecutará el método `show` del controlador `ContactController`.*
- *`->name(name: 'contacts.show')`: le da un nombre interno a la ruta para referenciarla en vistas y controladores. Usar nombres de rutas permite cambios fáciles en las URLs sin afectar el resto del código.*

**Ejemplo de uso en vista o redirección:**

```php
<a href="{{ route('contacts.show', $contact->id) }}">Ver contacto</a>
```

---

### **3. Implementar la vista en `resources/views/contacts/show.blade.php`**

```php
@extends('layouts.app')

@section('content')
  <div class="container">
    <div class="row justify-content-center">
      <div class="col-md-8">
        <div class="card">
          <div class="card-header">Contact Information</div>

          <div class="card-body">
            <p>Name: {{ $contact->name }}</p>
            <p>Email:
              <a href="mailto:{{ $contact->email }}">
                {{ $contact->email }}
              </a>
            </p>
            <p>Age: {{ $contact->age }}</p>
            <p>Phone number:
              <a href="tel:{{ $contact->phone_number }}">
                {{ $contact->phone_number }}
              </a>
            </p>
            <p>Created At: {{ $contact->created_at }}</p>
            <p>Updated At: {{ $contact->updated_at }}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
@endsection
```

**Explicación detallada:**

- *`@extends('layouts.app')`: indica que esta vista extiende una plantilla base (`layouts/app.blade.php`).*
- *`@section('content') ... @endsection`: define el contenido que se inyectará en la sección `content` de la plantilla base.*

**Contenido de la tarjeta (`card`):**

- *Se usa Bootstrap (v5.0) para dar estilo.*
- *Cada propiedad del modelo `Contact` se muestra con `{{ $contact->propiedad }}`.*
- *El uso de enlaces `mailto:` y `tel:` permite abrir automáticamente la aplicación de correo o de llamadas cuando se hace clic.*

**Referencia a Bootstrap:**
*[Bootstrap Utilities Colors](https://getbootstrap.com/docs/5.0/utilities/colors/ "https://getbootstrap.com/docs/5.0/utilities/colors/")*

---

### **4. Método `show` en el controlador**

*Asegúrate de tener el siguiente método en `app/Http/Controllers/ContactController.php`:*

```php
public function show(Contact $contact)
{
    return view('contacts.show', compact('contact'));
}
```

**Explicación:**

- *`Contact $contact`: gracias al "route model binding", Laravel inyecta automáticamente la instancia del modelo `Contact` correspondiente al ID de la URL.*
- *`view('contacts.show', compact('contact'))`: retorna la vista `contacts.show` y le pasa el objeto `$contact` usando `compact`, que es equivalente a hacer `['contact' => $contact]`.*
