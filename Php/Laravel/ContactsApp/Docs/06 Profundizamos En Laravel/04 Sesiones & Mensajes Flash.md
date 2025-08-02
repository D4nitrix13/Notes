<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- Gitlab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# **Sesiones & Mensajes Flash**

## *Uso de **mensajes flash** en Laravel con sesiones (`session()->flash()` y `with()`)*

> [!NOTE]
> *Laravel permite **mostrar mensajes temporales (flash messages)** que se almacenan en la sesión y están disponibles **solo durante la siguiente solicitud**. Son muy útiles para mostrar notificaciones tras acciones como crear, actualizar o eliminar registros.*

---

## **1. Guardar un mensaje flash manualmente**

*Archivo: `app/Http/Controllers/ContactController.php`*

```php
session()->flash(key: "alert", value: [
    "message" => "Contact $contact->name saved successfully",
    "type" => "info"
]);
```

### **Explicación**

* *`session()->flash()` guarda un valor **en la sesión** **solo para la siguiente solicitud**.*
* *`'alert'` es la **clave** bajo la cual se guarda el mensaje.*
* *El segundo parámetro es el **array de datos** que contiene el mensaje y su tipo.*

---

## **2. Forma más directa usando redirect con `with()`**

```php
return redirect(to: "home")->with(key: "alert", value: [
    "message" => "Contact $contact->name saved successfully",
    "type" => "success"
]);
```

* **Explicación**

* *`redirect('home')`: redirige a la ruta `home` (podés usar `route('home')` si tenés el nombre definido).*
* *`->with(...)`: adjunta datos a la sesión flash automáticamente.*
* *`'alert'`: nombre de la variable que se guardará temporalmente.*
* *El array incluye:*

  * *`'message'`: texto que se mostrará al usuario.*
  * *`'type'`: puede ser `success`, `error`, `info`, etc., útil para cambiar estilos de la alerta.*

---

## **3. Mostrar el mensaje flash en una vista**

*Archivo: `resources/views/layouts/app.blade.php`*
*(esto puede estar dentro del `@section('content')` o donde muestres alertas):*

```php
@if (session()->has('alert'))
  <div class="alert alert-{{ session('alert')['type'] }}">
    {{ session('alert')['message'] }}
  </div>
@endif
```

* **Explicación**

* *`session()->has('alert')`: verifica si existe el mensaje flash con clave `alert`.*
* *`session('alert')['message']`: accede al texto del mensaje.*
* *`session('alert')['type']`: accede al tipo (para Bootstrap puede ser: `success`, `danger`, `info`, etc.)*
* *`alert-{{ ... }}`: clase de Bootstrap dinámica (`alert-success`, `alert-danger`, etc.)*

---

## **Ejemplo completo de uso**

### **En `ContactController.php` (método `store`)**

```php
public function store(StoreContactRequest $request)
{
    $contact = auth()->user()->contacts()->create($request->validated());
    return redirect(to: "home")->with(key: "alert", value: [
        "message" => "Contact $contact->name saved successfully",
        "type" => "success"
    ]);
}
```

### **En `app.blade.php`**

```php
<!doctype html>
<html lang="{{ str_replace('_', '-', app()->getLocale()) }}">

  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- CSRF Token -->
    <meta name="csrf-token" content="{{ csrf_token() }}">

    <title>{{ config('app.name', 'Laravel') }}</title>

    <!-- Scripts -->
    <script src="{{ asset('js/app.js') }}" defer></script>
    @stack('scripts')

    <!-- Fonts -->
    <link rel="dns-prefetch" href="//fonts.gstatic.com">
    <link href="https://fonts.googleapis.com/css?family=Nunito" rel="stylesheet">

    <!-- Styles -->
    <link href="{{ asset('css/app.css') }}" rel="stylesheet">
  </head>

  <body>
    <div id="app">
      <nav class="navbar navbar-expand-md navbar-dark bg-dark shadow-sm">
        <div class="container">
          {{-- Adding Image Logo --}}
          <img src="/img/logo.png" class="me-1">
          <a class="navbar-brand" href="{{ url('/') }}">
            {{ config('app.name', 'Laravel') }}
          </a>
          <button class="navbar-toggler" type="button" data-bs-toggle="collapse"
            data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false"
            aria-label="{{ __('Toggle navigation') }}">
            <span class="navbar-toggler-icon"></span>
          </button>

          <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <!-- Left Side Of Navbar -->
            <ul class="navbar-nav me-auto">

            </ul>

            <!-- Right Side Of Navbar -->
            <ul class="navbar-nav ms-auto">
              <!-- Authentication Links -->
              @guest
                @if (Route::has('login'))
                  <li class="nav-item">
                    <a class="nav-link" href="{{ route('login') }}">{{ __('Login') }}</a>
                  </li>
                @endif

                @if (Route::has('register'))
                  <li class="nav-item">
                    <a class="nav-link" href="{{ route('register') }}">{{ __('Register') }}</a>
                  </li>
                @endif
              @else
                <li class="nav-item">
                  <a class="nav-link" href="{{ route('contacts.index') }}"> My Contacts </a>
                </li>

                <li class="nav-item">
                  <a class="nav-link" href="{{ route('contacts.create') }}"> Create New Contact </a>
                </li>
                <li class="nav-item dropdown">
                  <a id="navbarDropdown" class="nav-link dropdown-toggle" href="#" role="button"
                    data-bs-toggle="dropdown" aria-haspopup="true" aria-expanded="false" v-pre>
                    {{ Auth::user()->name }}
                  </a>

                  <div class="dropdown-menu dropdown-menu-end" aria-labelledby="navbarDropdown">
                    <a class="dropdown-item" href="{{ route('logout') }}"
                      onclick="event.preventDefault();
                                                     document.getElementById('logout-form').submit();">
                      {{ __('Logout') }}
                    </a>

                    <form id="logout-form" action="{{ route('logout') }}" method="POST" class="d-none">
                      @csrf
                    </form>
                  </div>
                </li>
              @endguest
            </ul>
          </div>
        </div>
      </nav>

      <main class="py-4">
        @if (session()->has('alert'))
          <div class="container">
            <svg xmlns="http://www.w3.org/2000/svg" style="display: none;">
              <symbol id="success" fill="currentColor" viewBox="0 0 16 16">
                <path
                  d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0zm-3.97-3.03a.75.75 0 0 0-1.08.022L7.477 9.417 5.384 7.323a.75.75 0 0 0-1.06 1.06L6.97 11.03a.75.75 0 0 0 1.079-.02l3.992-4.99a.75.75 0 0 0-.01-1.05z" />
              </symbol>
              <symbol id="info" fill="currentColor" viewBox="0 0 16 16">
                <path
                  d="M8 16A8 8 0 1 0 8 0a8 8 0 0 0 0 16zm.93-9.412-1 4.705c-.07.34.029.533.304.533.194 0 .487-.07.686-.246l-.088.416c-.287.346-.92.598-1.465.598-.703 0-1.002-.422-.808-1.319l.738-3.468c.064-.293.006-.399-.287-.47l-.451-.081.082-.381 2.29-.287zM8 5.5a1 1 0 1 1 0-2 1 1 0 0 1 0 2z" />
              </symbol>
              <symbol id="warning" fill="currentColor" viewBox="0 0 16 16">
                <path
                  d="M8.982 1.566a1.13 1.13 0 0 0-1.96 0L.165 13.233c-.457.778.091 1.767.98 1.767h13.713c.889 0 1.438-.99.98-1.767L8.982 1.566zM8 5c.535 0 .954.462.9.995l-.35 3.507a.552.552 0 0 1-1.1 0L7.1 5.995A.905.905 0 0 1 8 5zm.002 6a1 1 0 1 1 0 2 1 1 0 0 1 0-2z" />
              </symbol>
              <symbol id="danger" fill="currentColor" viewBox="0 0 16 16">
                <path
                  d="M8.982 1.566a1.13 1.13 0 0 0-1.96 0L.165 13.233c-.457.778.091 1.767.98 1.767h13.713c.889 0 1.438-.99.98-1.767L8.982 1.566zM8 5c.535 0 .954.462.9.995l-.35 3.507a.552.552 0 0 1-1.1 0L7.1 5.995A.905.905 0 0 1 8 5zm.002 6a1 1 0 1 1 0 2 1 1 0 0 1 0-2z" />
              </symbol>
            </svg>

            <div class="alert alert-{{ session()->get('alert')['type'] }} d-flex align-items-center" role="alert">
              <svg class="bi flex-shrink-0 me-2" width="24" height="24" role="img" aria-label="Info:">
                <use xlink:href="#{{ session()->get('alert')['type'] }}" />
              </svg>
              <div>
                {{ session()->get('alert')['message'] }}
              </div>
            </div>
          </div>
        @endif
        @yield('content')
      </main>
    </div>
  </body>

</html>
```

---

## **Estilos con Bootstrap**

*Usá el campo `'type'` para mostrar estilos como:*

| **Tipo**    | **Clase Bootstrap**                                               |
| ----------- | ----------------------------------------------------------------- |
| *`success`* | *`alert-success`*                                                 |
| *`info`*    | *`alert-info`*                                                    |
| *`warning`* | *`alert-warning`*                                                 |
| *`error`*   | *`alert-danger` (Laravel usa `error`, Bootstrap espera `danger`)* |
