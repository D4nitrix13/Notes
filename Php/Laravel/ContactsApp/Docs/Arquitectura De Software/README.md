<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# **MVC** *(Modelo-Vista-Controlador)*

*Es un **patrón de arquitectura de software** que se utiliza comúnmente en el desarrollo de aplicaciones web y de escritorio. Su propósito es **separar las responsabilidades** dentro de una aplicación para mejorar la organización, mantenimiento y escalabilidad del código.*

## **1. Modelo (Model)**

*El **Modelo** es la representación de los datos y la lógica de negocio. En el contexto de una base de datos, el modelo generalmente maneja la **interacción con la base de datos**, como recuperar, almacenar, actualizar y eliminar datos. Además, encapsula la **lógica de negocio** que puede incluir validaciones y cálculos sobre esos datos.*

**Responsabilidades:**

- *Gestiona los datos de la aplicación.*
- *Define las reglas de negocio y validaciones de los datos.*
- *Interactúa con la base de datos a través de consultas, recuperando y manipulando los registros.*

**Ejemplo:**
*En Laravel, un modelo se define como una clase que extiende de `Illuminate\Database\Eloquent\Model`. Los modelos están directamente relacionados con las tablas de la base de datos y representan los registros de esas tablas como objetos.*

```php
<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Contact extends Model
{
    use HasFactory;
    
    // En lugar de personalizar la tabla y la clave primaria, seguimos la convención de Laravel.
    // Laravel asume por defecto que la tabla se llama 'contacts' (plural y en minúsculas) y
    // que la clave primaria es 'id'.
    // protected $table = 'my_custom_name_table';
    // protected $primaryKey = 'contact_id';

    // Campos que se pueden asignar masivamente
    protected $fillable = [
        "name",
        "phone_number"
    ];
}
```

### **2. Vista (View)**

*La **Vista** es la parte encargada de la **presentación** de los datos al usuario. Es lo que el usuario ve en la interfaz gráfica. La vista no debe contener lógica de negocio o interacción con la base de datos, solo se encarga de mostrar la información de manera estructurada y comprensible.*

**Responsabilidades:**

- *Muestra los datos al usuario.*
- *Recibe las acciones del usuario, como clics o envíos de formularios.*
- *Generalmente se generan a partir de plantillas o componentes dinámicos.*

**Ejemplo:**
*En Laravel, las vistas se crean con el motor de plantillas **Blade**, donde puedes escribir HTML con lógica PHP para mostrar los datos. File -> `ApplicationLaravel/resources/views/contact.blade.php`.*

```php
// ApplicationLaravel/resources/views/contact.blade.php
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

### **3. Controlador (Controller)**

*El **Controlador** es responsable de gestionar las peticiones del usuario, interactuar con el modelo y seleccionar la vista adecuada para presentar la respuesta. El controlador actúa como un intermediario entre el **modelo** y la **vista**. Recibe las solicitudes, procesa los datos (con la ayuda del modelo) y luego pasa la información necesaria a la vista.*

**Responsabilidades:**

- *Recibe las solicitudes del usuario (GET, POST, PUT, DELETE, etc.).*
- *Interactúa con el modelo para obtener o manipular los datos.*
- *Selecciona la vista adecuada para mostrar los resultados o devolver una respuesta.*

**Ejemplo:**
*En Laravel, los controladores se definen como clases que contienen métodos para manejar las peticiones HTTP.*

```php
<?php

namespace App\Http\Controllers;

use App\Models\Contact;
use Illuminate\Http\Request;

class ContactController extends Controller
{
    /**
     * Display a listing of the resource.
     *
     * @return \Illuminate\Http\Response
     */
    public function index()
    {
        //
    }

    /**
     * Show the form for creating a new resource.
     *
     * @return \Illuminate\Http\Response
     */
    public function create()
    {
        // return Response::view("contact");
        return view("contact"); // Devuelve la vista de creación de contacto
    }

    /**
     * Store a newly created resource in storage.
     *
     * @param  \Illuminate\Http\Request  $request
     * @return \Illuminate\Http\Response
     */
    public function store(Request $request)
    {
        // No Recomendable
        Contact::create(
            $request->all() // Crea un nuevo contacto en la base de datos
        );

        return response("Contact Created"); // Responde con un mensaje
    }

    /**
     * Display the specified resource.
     *
     * @param  \App\Models\Contact  $contact
     * @return \Illuminate\Http\Response
     */
    public function show(Contact $contact)
    {
        //
    }

    /**
     * Show the form for editing the specified resource.
     *
     * @param  \App\Models\Contact  $contact
     * @return \Illuminate\Http\Response
     */
    public function edit(Contact $contact)
    {
        //
    }

    /**
     * Update the specified resource in storage.
     *
     * @param  \Illuminate\Http\Request  $request
     * @param  \App\Models\Contact  $contact
     * @return \Illuminate\Http\Response
     */
    public function update(Request $request, Contact $contact)
    {
        //
    }

    /**
     * Remove the specified resource from storage.
     *
     * @param  \App\Models\Contact  $contact
     * @return \Illuminate\Http\Response
     */
    public function destroy(Contact $contact)
    {
        //
    }
}
```

### **Flujo de MVC en Laravel:**

1. **El usuario realiza una solicitud (petición HTTP),** *por ejemplo, accede a `GET /contacts/create`.*
2. **El enrutador (router) de Laravel** *asigna esa solicitud a una ruta definida en `routes/web.php` que está asociada a un **controlador**. Por ejemplo:*

    ```php
    Route::get('/contacts/create', [ContactController::class, 'create']);
    ```

3. **El controlador (`ContactController`)** *recibe la solicitud y decide qué hacer. En el caso de la acción `create`, devuelve la vista `contacts.create`.*
4. **La vista (`contacts.create`)** *es un archivo Blade que muestra el formulario de creación de un contacto.*
5. **El usuario envía los datos** *del formulario, lo cual hace una solicitud POST a `POST /contacts`. El controlador maneja esta solicitud con el método `store`.*
6. **El controlador `store`** *recibe los datos del formulario, los pasa al **modelo `Contact`** para crear un nuevo registro en la base de datos, y luego devuelve una respuesta, como un mensaje de éxito o redirige a otra página.*

### **¿Por qué usar el patrón MVC?**

- **Separación de responsabilidades:** *Al separar la lógica de negocio, la presentación y el manejo de solicitudes, el patrón MVC hace que el código sea más fácil de entender y mantener.*
- **Escalabilidad:** *Puedes hacer cambios en una parte de la aplicación sin afectar a las demás, lo que facilita la expansión de la aplicación.*
- **Reutilización del código:** *Los modelos, vistas y controladores pueden reutilizarse en diferentes partes de la aplicación o incluso en otros proyectos.*

---

### **Enlace de recursos:**

- *[Patrón MVC - Wikipedia](https://es.wikipedia.org/wiki/Modelo-vista-controlador "https://es.wikipedia.org/wiki/Modelo-vista-controlador")*
- *[Documentación oficial de Laravel sobre Controladores](https://laravel.com/docs/12.x/controllers "https://laravel.com/docs/12.x/controllers")*
- *[Documentación oficial de Laravel sobre Modelos Eloquent](https://laravel.com/docs/12.x/eloquent "https://laravel.com/docs/12.x/eloquent")*
- *[Blade Templates - Laravel](https://laravel.com/docs/12.x/blade "https://laravel.com/docs/12.x/blade")*
