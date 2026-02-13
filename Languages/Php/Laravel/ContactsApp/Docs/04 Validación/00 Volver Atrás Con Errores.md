<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# **Volver Atrás Con Errores**

> [!IMPORTANT]
> *Validar los datos antes de insertarlos en la base de datos es **fundamental** para evitar inconsistencias y posibles fallos en la aplicación. En este caso, estamos viendo una forma **poco recomendada** de hacer validaciones, pero útil para entender cómo Laravel maneja los errores y la retroalimentación en los formularios.*

---

## **1. Mala Práctica: No Validar los Datos Antes de Guardarlos**

*El siguiente código en el controlador **no valida adecuadamente** los datos antes de guardarlos en la base de datos, lo cual es una **mala práctica**, pero se explica con fines educativos:*

```php
/**
 * Store a newly created resource in storage.
 *
 * @param  \Illuminate\Http\Request  $request
 * @return \Illuminate\Http\Response
 */
public function store(Request $request)
{
    // Si el campo "name" es nulo, redirigir con un mensaje de error
    if (
        is_null($request->get("name"))
    ) return Response::redirectTo("/contacts/create")->withErrors([
        "name" => "This field is required" // Mensaje de error si "name" está vacío
    ]);
    
    // No Recomendable: Guardar los datos sin validación
    Contact::create(
        $request->all() // Inserta todos los datos sin verificar si son válidos
    );

    return response("Contact Created"); // Responde con un mensaje de éxito
}
```

### **¿Por qué esta forma de validar es una mala práctica?**

1. **No usa el sistema de validación de Laravel,** *que es más seguro y eficiente.*
2. **No protege contra datos incorrectos** *que podrían afectar la integridad de la base de datos.*
3. **Permite la entrada de valores no deseados** *que podrían generar errores en la aplicación.*

*En lugar de hacer la validación de esta manera, se recomienda utilizar `validate()` en Laravel, lo cual veremos más adelante.*

---

## **2. Adaptando la Vista para Mostrar los Errores**

*Laravel proporciona una manera sencilla de **mostrar errores en los formularios** cuando se usan las validaciones del framework.*

*En el archivo **`resources/views/auth/register.blade.php`**, encontramos este código en el formulario de registro:*

```bash
@extends('layouts.app')

@section('content')
<div class="container">
    <div class="row justify-content-center">
        <div class="col-md-8">
            <div class="card">
                <div class="card-header">{{ __('Register') }}</div>

                <div class="card-body">
                    <form method="POST" action="{{ route('register') }}">
                        @csrf

                        <div class="row mb-3">
                            <label for="name" class="col-md-4 col-form-label text-md-end">{{ __('Name') }}</label>

                            <div class="col-md-6">
                                <input id="name" type="text" class="form-control @error('name') is-invalid @enderror" name="name" value="{{ old('name') }}" required autocomplete="name" autofocus>

                                @error('name')
                                    <span class="invalid-feedback" role="alert">
                                        <strong>{{ $message }}</strong>
                                    </span>
                                @enderror
                            </div>
                        </div>

                        <div class="row mb-3">
                            <label for="email" class="col-md-4 col-form-label text-md-end">{{ __('Email Address') }}</label>

                            <div class="col-md-6">
                                <input id="email" type="email" class="form-control @error('email') is-invalid @enderror" name="email" value="{{ old('email') }}" required autocomplete="email">

                                @error('email')
                                    <span class="invalid-feedback" role="alert">
                                        <strong>{{ $message }}</strong>
                                    </span>
                                @enderror
                            </div>
                        </div>

                        <div class="row mb-3">
                            <label for="password" class="col-md-4 col-form-label text-md-end">{{ __('Password') }}</label>

                            <div class="col-md-6">
                                <input id="password" type="password" class="form-control @error('password') is-invalid @enderror" name="password" required autocomplete="new-password">

                                @error('password')
                                    <span class="invalid-feedback" role="alert">
                                        <strong>{{ $message }}</strong>
                                    </span>
                                @enderror
                            </div>
                        </div>

                        <div class="row mb-3">
                            <label for="password-confirm" class="col-md-4 col-form-label text-md-end">{{ __('Confirm Password') }}</label>

                            <div class="col-md-6">
                                <input id="password-confirm" type="password" class="form-control" name="password_confirmation" required autocomplete="new-password">
                            </div>
                        </div>

                        <div class="row mb-0">
                            <div class="col-md-6 offset-md-4">
                                <button type="submit" class="btn btn-primary">
                                    {{ __('Register') }}
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

- **Code Important**

```php
<input id="name" type="text" class="form-control @error('name') is-invalid @enderror" name="name" value="{{ old('name') }}" required autocomplete="name" autofocus>
@error('name')
    <span class="invalid-feedback" role="alert">
        <strong>{{ $message }}</strong>
    </span>
@enderror
```

### **Explicación del Código:**

- *`@error('name') is-invalid @enderror` → Agrega la clase `is-invalid` al input si el campo `name` tiene errores de validación.*
- *`@error('name')` → Verifica si hay un error asociado al campo `name`.*
- *`<span class="invalid-feedback" role="alert">` → Se usa para mostrar el mensaje de error en Bootstrap.*
- *`{{ $message }}` → Muestra el mensaje de error asociado al campo `name`.*

---

## **3. Aplicando Esto en Nuestra Vista `contacts.blade.php`**

*Queremos agregar la misma funcionalidad en la vista de contactos para mostrar los errores si el usuario no completa el campo `name`.*

### **Modificamos `resources/views/contact.blade.php`**

```php
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

*Antes de modificar, el campo del formulario se veía así:*

```php
<input id="name" type="text" class="form-control @error('name') is-invalid @enderror" name="name" required autocomplete="name" autofocus>
@error('name')
<span class="invalid-feedback" role="alert">
    <strong>{{ $message }}</strong>
</span>
@enderror
```

*Ahora **quitamos el atributo `required`** para fines de prueba y aprendizaje:*

```php
<input id="name" type="text" class="form-control @error('name') is-invalid @enderror" name="name" autocomplete="name" autofocus>
@error('name')
<span class="invalid-feedback" role="alert">
    <strong>{{ $message }}</strong>
</span>
@enderror
```

- **New Code**

```php
@extends('layouts.app')

@section('content')
  <div class="container">
    <div class="row justify-content-center">
      <div class="col-md-8">
        <div class="card">
          <div class="card-header">Create new contact</div>

          <div class="card-body">
            <form method="POST" action="{{ route('contacts.store') }}">
              {{-- <input type="hidden" name="_token" value="{{ csrf_token() }}"> --}}
              @csrf
              <div class="row mb-3">
                <label for="name" class="col-md-4 col-form-label text-md-end">Name</label>

                <div class="col-md-6">
                  <input id="name" type="text" class="form-control @error('name') is-invalid @enderror"
                    name="name" autocomplete="name" autofocus>
                  @error('name')
                    <span class="invalid-feedback" role="alert">
                      <strong>{{ $message }}</strong>
                    </span>
                  @enderror
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

### **¿Qué cambia con esto?**

- *Ahora **no es obligatorio** llenar el campo en el navegador (antes el navegador bloqueaba el envío si el campo `name` estaba vacío debido al `required`).*
- *Si el usuario deja el campo vacío y envía el formulario, Laravel **redirige de vuelta** con un mensaje de error.*
- *Bootstrap mostrará el mensaje `"This field is required"` debajo del campo `name`.*

---

## **4. Prueba de Validación en la Aplicación**

1. *Accedemos a la página para crear un contacto:*

   ```bash
   http://172.17.0.2:80/contacts/create
   ```

2. **No llenamos el campo `name`,** *pero sí `phone_number`.*
3. *Presionamos el botón de envío del formulario.*
4. **Laravel nos redirige de vuelta** *y muestra el mensaje de error `"This field is required"` debajo del campo `name`.*

### **Recursos Útiles**

- *[Validación en Laravel](https://laravel.com/docs/12.x/validation "https://laravel.com/docs/12.x/validation")*
- *[Blade Templates en Laravel](https://laravel.com/docs/12.x/blade "https://laravel.com/docs/12.x/blade")*
- *[Redirección con errores en Laravel](https://laravel.com/docs/12.x/responses#redirecting-with-flashed-session-data "https://laravel.com/docs/12.x/responses#redirecting-with-flashed-session-data")*

---

### **Diferentes Formas de Redirigir en Laravel con Errores**

*Laravel es un framework expresivo y flexible, lo que significa que existen **varias maneras de lograr el mismo resultado**. En este caso, estamos viendo **diferentes formas de redirigir con errores** cuando el campo `name` no está presente en la solicitud (`$request`).*

---

## **1. Primera Forma: Usando `Response::redirectTo()`**

> [!NOTE]
> *Importar `use Illuminate\Support\Facades\Response;`*

```php
if (
    is_null($request->get("name"))
) return Response::redirectTo("/contacts/create")->withErrors([
    "name" => "This field is required"
]);
```

### **Explicación**

- **`Response::redirectTo("/contacts/create")` →** *Usa la **clase `Response`** para generar una redirección a la URL `"/contacts/create"`.*
- **`withErrors([...])` →** *Envía mensajes de error a la sesión para que puedan mostrarse en la vista.*

### **Desventajas**

- **No es la forma más común en Laravel,** *ya que el método `redirect()` es más flexible y utilizado.*

---

## **2. Segunda Forma: Usando `redirect("/ruta")`**

```php
if (
    is_null($request->get("name"))
) return redirect("/contacts/create")->withErrors([
    "name" => "This field is required"
]);
```

- **Explicación**

- **`redirect("/contacts/create")` →** *Redirige directamente a la URL `"/contacts/create"`.*

### **Ventajas**

- *Es más corto y directo que `Response::redirectTo()`.*
- *Se usa frecuentemente en Laravel.*

- **Desventajas**

- *Si la ruta cambia en `routes/web.php`, **habría que actualizar la URL manualmente** en el código.*

---

## **3. Tercera Forma: Usando `redirect(route("name_route"))`**

```php
if (
    is_null($request->get("name"))
) return redirect(route("contacts.create"))->withErrors([
    "name" => "This field is required"
]);
```

- **Explicación**

- **`route("contacts.create")` →** *Genera la URL correspondiente al **nombre de la ruta `"contacts.create"`** definido en `routes/web.php`.*
- **`redirect(route("contacts.create"))` →** *Redirige a la URL generada.*

- **Ventajas**

- **No dependemos de URLs estáticas,** *lo que hace el código más mantenible.*
- *Si cambia la URL en `routes/web.php`,* **no hay que modificar este código.**

---

## **4. Cuarta Forma: Usando `redirect()->route("name_route")`**

```php
if (
    is_null($request->get("name"))
) return redirect()->route("contacts.create")->withErrors([
    "name" => "This field is required"
]);
```

- **Explicación**

- **`redirect()->route("contacts.create")` →** *Es una forma más clara de redirigir a una* **ruta con nombre.**
- *Laravel entiende que queremos* **redirigir a una ruta nombrada.**

- **Ventajas**

- **Código más limpio y expresivo** *en comparación con `redirect(route("name_route"))`.*
- **Mismo beneficio de no depender de URLs estáticas.**

---

## **5. Quinta Forma: Usando `redirect()->back()`**

```php
if (
    is_null($request->get("name"))
) return redirect()->back()->withErrors([
    "name" => "This field is required"
]);
```

- **Explicación**

- **`redirect()->back()` →** *Redirige al usuario **a la página anterior** (la que envió la solicitud).*
- **`withErrors([...])` →** *Manda los errores para ser mostrados en la vista.*

- **Ventajas**

- **Útil cuando el usuario viene de diferentes rutas** *(por ejemplo, si hay varios formularios que pueden enviar datos al mismo controlador).*
- **Evita tener que especificar una ruta manualmente.**

### **Casos de Uso**

- *Cuando un usuario envía un formulario y queremos* **devolverlo a la misma página si hay errores.**
- *Cuando se usa un botón "Volver" que regresa a la página anterior.*

---

## **6. Sexta Forma: Usando `back()`**

```php
if (
    is_null($request->get("name"))
) return back()->withErrors([
    "name" => "This field is required"
]);
```

- **Explicación**

- *`back()` es* **un alias más corto de `redirect()->back()`,** *por lo que funciona de la misma manera.*

- **Ventajas**

- **Es la forma más corta y limpia** *de redirigir a la página anterior.*
- **Más expresivo y fácil de leer.**
- **Mismo uso que `redirect()->back()`,** *pero con menos código.*

---

## **Comparación de Todas las Formas**

| *Método*                            | *Explicación*                               | *Ventajas*                         | *Desventajas*                                     |
| ----------------------------------- | ------------------------------------------- | ---------------------------------- | ------------------------------------------------- |
| *`Response::redirectTo("/ruta")`*   | *Usa la clase `Response` para redirigir*    | *Se basa en la API de Laravel*     | *No es la forma más usada*                        |
| *`redirect("/ruta")`*               | *Redirige a una URL estática*               | *Rápido y directo*                 | *Si la URL cambia, el código debe actualizarse*   |
| *`redirect(route("name_route"))`*   | *Redirige usando el nombre de la ruta*      | *No depende de URLs estáticas*     | *Un poco más largo*                               |
| *`redirect()->route("name_route")`* | *Mejor sintaxis que `redirect(route(...))`* | *Más claro y expresivo*            | *Ninguna significativa*                           |
| *`redirect()->back()`*              | *Redirige a la página anterior*             | *Evita escribir rutas manualmente* | *Si el usuario accede directamente, puede fallar* |
| *`back()`*                          | *Alias de `redirect()->back()`*             | *Más corto y fácil de leer*        | *Puede fallar si el historial está vacío*         |

---

## **Conclusión**

1. *Si quieres redirigir a* **una ruta específica con nombre,** *usa:*

   ```php
   return redirect()->route("contacts.create")->withErrors([...]);
   ```

2. *Si quieres redirigir a* **la página anterior,** *usa:*

   ```php
   return back()->withErrors([...]);
   ```

3. **Evita usar `Response::redirectTo()`,** *ya que Laravel tiene métodos más expresivos (`redirect()`, `route()`, `back()`).*

- **Recomendación:**

- **Para rutas fijas:** *Usa `redirect()->route("name_route")`.*
- **Para volver atrás:** *Usa `back()`.*

- **Recursos Útiles:**

- *[Documentación de Redirecciones en Laravel](https://laravel.com/docs/12.x/responses#redirects "https://laravel.com/docs/12.x/responses#redirects")*
- *[Cómo manejar errores de validación en Laravel](https://laravel.com/docs/12.x/validation#quick-displaying-the-validation-errors "https://laravel.com/docs/12.x/validation#quick-displaying-the-validation-errors")*
