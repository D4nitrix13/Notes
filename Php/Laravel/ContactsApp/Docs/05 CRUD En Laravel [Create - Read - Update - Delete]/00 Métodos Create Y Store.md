<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# **Métodos Create Y Store**

---

## **1. Controlador: `ContactController`**

### **Método: `index()`**

- **Comando principal:**  
  *`return view()`*
  - **Descripción:** *Esta función Laravel devuelve una vista (archivo Blade) al navegador. Se utiliza para mostrar páginas HTML renderizadas con datos dinámicos.*
  
- **Subcomando:**  
  *`view(view: "home", data: [...])`*
  - **Descripción:**  
    - *`view: "home"` indica el nombre de la vista que se debe renderizar. Laravel buscará un archivo en `resources/views/home.blade.php`.*
    - *`data: [...]` es un array asociativo que contiene datos que se pasan a la vista. En este caso:*

      ```php
      ["contacts" => Contact::all()]
      ```

      *se pasan todos los contactos almacenados en la base de datos a la vista.*

- **Valores:**  
  *`Contact::all()` recupera todos los registros del modelo `Contact`.*

- **Ejemplo práctico:**

  ```php
  return view(view: "home", data: ["contacts" => Contact::all()]);
  ```

  **Explicación:** *Muestra la vista `home.blade.php` y le pasa la variable `$contacts` que contiene todos los registros del modelo `Contact`.*

---

#### **Método: `store(Request $request)`**

- **Comando principal:**  
  `Contact::create($data)`
  - **Descripción:** *Crea un nuevo registro en la base de datos usando el modelo `Contact`.*

- **Subcomando:**  
  *`$request->only([...])` o `$request->validate([...])` (no presente en tu ejemplo pero comúnmente usado)*
  - **Descripción:** *Se usa para obtener datos del formulario o validarlos antes de guardarlos.*

- **Opción:**  
  `$data`  
  - **Descripción:** *Debe ser un array asociativo con claves que correspondan a columnas en la tabla de `contacts`.*

- **Comando adicional:**  
  `return redirect(to: "home");`
  - **Descripción:** *Redirige al usuario a la ruta especificada (en este caso, la página principal `"home"`). Alternativamente:*

    ```php
    return redirect()->route(route: "home");
    ```

    *que redirige usando el nombre de ruta definido en `web.php`.*

- **Ejemplo práctico:**

  ```php
  public function store(Request $request)
  {
      $data = $request->all(); // o usar solo los campos necesarios
      Contact::create($data);
      return redirect(to: "home");
  }
  ```

  **Explicación:** *Guarda un nuevo contacto y redirige a la vista principal.*

---

### **2. Directivas Blade**

#### **Directiva: `@forelse`**

- **Descripción:**  
  *Recorre una colección (como un array de objetos), y si está vacía, ejecuta el bloque `@empty`.*

- **Subdirectivas:**
  - *`@empty`: Se ejecuta si la colección está vacía.*
  - *`@endforelse`: Finaliza el bloque.*

- **Valores:**  
  *En `@forelse ($contacts as $contact)`, la variable `$contacts` es un array de objetos `Contact`, y `$contact` es cada uno de esos objetos.*

- **Ejemplo práctico:**

  ```php
  @forelse ($contacts as $contact)
      <div class="col-md-4 mb-3">
          <div class="card text-center">
          <div class="card-body">

              <h3 class="card-title text-capitalize">{{ $contact->name }}</h3>
              <p class="m-2">{{ $contact->phone_number }}</p>
              <a href="{{ route('contacts.edit', $contact->id) }}" class="btn btn-secondary mb-2">Edit Contact</a>
              <a href="" class="btn btn-danger mb-2">Delete Contact</a>
          </div>
          </div>
      </div>
      @empty
      <div class="col-md-4 mx-auto">
          <div class="card card-body text-center">
          <p>No contacts saved yet</p>
          <a href="{{ route('contacts.create') }}">Add One!</a>
          </div>
      </div>
  @endforelse
  ```

#### **Otras directivas comunes usadas**

| *Directiva*     | *Uso*                                                   |
| --------------- | ------------------------------------------------------- |
| *`@if`*         | *Ejecuta un bloque si la condición es verdadera.*       |
| *`@else`*       | *Alternativa a `@if` cuando no se cumple la condición.* |
| *`@endif`*      | *Finaliza un bloque `@if`.*                             |
| *`@foreach`*    | *Itera sobre una colección.*                            |
| *`@endforeach`* | *Finaliza un bloque `@foreach`.*                        |

---

### **3. Acceso a atributos en Blade**

```php
{{ $contact->name }}
```

- **Descripción:**  
  *Imprime el valor del atributo `name` del objeto `$contact`.*

- **Sintaxis alternativa:**  
  *También se puede usar lógica PHP en Blade:*

  ```php
  <?php echo $contact->name; ?>
  ```

---

### **4. Ejemplo completo del archivo Blade**

*Este fragmento renderiza tarjetas para cada contacto o muestra un mensaje si no hay ninguno:*

- **Codigo Recomendado**

```php
@extends('layouts.app')

@section('content')
  <div class="container pt-4 p-3">
    <div class="row">
      @forelse ($contacts as $contact)
        <div class="col-md-4 mb-3">
          <div class="card text-center">
            <div class="card-body">

              <h3 class="card-title text-capitalize">{{ $contact->name }}</h3>
              <p class="m-2">{{ $contact->phone_number }}</p>
              <a href="{{ route('contacts.edit', $contact->id) }}" class="btn btn-secondary mb-2">Edit Contact</a>
              <a href="" class="btn btn-danger mb-2">Delete Contact</a>
            </div>
          </div>
        </div>
      @empty
        <div class="col-md-4 mx-auto">
          <div class="card card-body text-center">
            <p>No contacts saved yet</p>
            <a href="{{ route('contacts.create') }}">Add One!</a>
          </div>
        </div>
      @endforelse
    </div>
  </div>
@endsection
```

- **Codigo No Recomendado**

```php
@extends('layouts.app')

@section('content')
  <div class="container pt-4 p-3">
    <div class="row">
      @if ($contacts->count() === 0)
        <div class="col-md-4 mx-auto">
          <div class="card card-body text-center">
            <p>No contacts saved yet</p>
            <a href="{{ route('contacts.create') }}">Add One!</a>
          </div>
        </div>
      @else
        @foreach ($contacts as $contact)
          <div class="col-md-4 mb-3">
            <div class="card text-center">
              <div class="card-body">

                <h3 class="card-title text-capitalize">{{ $contact->name }}</h3>
                <p class="m-2">{{ $contact->phone_number }}</p>
                <a href="{{ route('contacts.edit', $contact->id) }}" class="btn btn-secondary mb-2">Edit Contact</a>
                <a href="" class="btn btn-danger mb-2">Delete Contact</a>
              </div>
            </div>
          </div>
        @endforeach
      @endif
    </div>
  </div>
@endsection
```
