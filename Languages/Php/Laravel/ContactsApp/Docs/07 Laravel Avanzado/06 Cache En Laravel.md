<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- Gitlab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# **Caché en Laravel: Uso con `Cache::remember`**

## **Objetivo**

*Reducir el tiempo de consulta de datos pesados o repetitivos (como contactos recientes) usando el sistema de caché de Laravel, específicamente la función `Cache::remember`.*

---

## **Modificamos el archivo:**

**`app/Http/Controllers/HomeController.php`**

## **Ejemplo**

```php
<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Cache;

class HomeController extends Controller
{
    /**
     * Create a new controller instance.
     *
     * @return void
     */
    public function __construct()
    {
        $this->middleware('auth');
    }

    /**
     * Show the application dashboard.
     *
     * @return \Illuminate\Contracts\Support\Renderable
     */
    public function index()
    {
        $contacts = Cache::remember(
            key: auth()->id(), // Clave Única Del Caché (Id Del Usuario Autenticado)
            ttl: now()->addMinutes(value: 30), // Tiempo de vida (TTL): 30 minutos desde "ahora"
            callback: fn() => auth()->user()->contacts()->latest()->take(9)->get() // Función de recuperación (si no está en caché)
        );

        return view(view: 'home', data: compact("contacts"));
        // return view(view: 'home', data: [
        //     "contacts" => auth()->user()->contacts()->latest()->take(9)->get()
        // ]);
    }
}
```

---

## **Explicación `Cache::remember`**

```php
Illuminate\Support\Facades\Cache::remember

<?php
public static function remember($key, $ttl, $callback) { }
@param string $key

@param \Closure|\DateTimeInterface|\DateInterval|int|null $ttl

@param \Closure $callback
```

| **Parámetro** | **Descripción**                                                                                                                           |
| ------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| *`$key`*      | *Clave única que identifica el dato en la caché. Puede ser un string simple o un identificador como `auth()->id()`*                       |
| *`$ttl`*      | *Time To Live – cuánto tiempo permanecerá el dato en caché. Puede ser: Entero (segundos) `Carbon`/`now()->addMinutes(30)` `DateInterval`* |
| *`$callback`* | *Función anónima (closure) que se ejecuta **solo si la clave no existe** en caché. El resultado será guardado bajo esa clave.*            |

---

## **¿Dónde se almacena la caché?**

**Laravel Guarda Los Archivos De Caché En:**

```bash
storage/framework/cache/data/
```

**Ejemplo de archivo generado:**

```bash
storage/framework/cache/data/35/6a/356a192b7913b04c54574d18c28d46e6395428ab
```

*Este archivo contiene los datos serializados del resultado de `contacts()->latest()->take(9)->get()`.*

---

## **Problema común**

*Si creamos un nuevo contacto, y luego regresamos al Home, **el nuevo contacto no aparece**.*

**¿Por qué?**
*Porque el resultado está almacenado en caché por 30 minutos, y Laravel no sabe que los datos han cambiado.*

---

## **Solución: invalidar la caché**

*Debemos **Eliminar Manualmente** La Entrada En Caché Cuando Se Agregue, Actualice O Elimine Un Contacto.*

---

## **Modificar `app/Http/Controllers/ContactController.php`**

**En los métodos que modifican los contactos:**

```php
// Invalidamos la caché del usuario
Cache::forget(key: auth()->id());
```

```php
<?php

namespace App\Http\Controllers;

use App\Http\Requests\StoreContactRequest;
use App\Models\Contact;
use Illuminate\Http\Request;
use Illuminate\Http\Response as HttpResponse;
use Illuminate\Support\Facades\Cache;
use Illuminate\Support\Facades\Gate;
use Illuminate\Support\Facades\Response;
use Illuminate\Support\Facades\Storage;

class ContactController extends Controller
{
    // protected $rules = [
    //     "name" => "required",
    //     "phone_number" => "required|digits:9",
    //     "email" => "required|email",
    //     "age" => "required|numeric|min:1|max:255"
    // ];

    /**
     * Display a listing of the resource.
     *
     * @return \Illuminate\Http\Response
     */
    public function index()
    {
        // dd(Contact::all());
        // return view(view: "contacts.index", data: ["contacts" => Contact::all()]);

        // $contacts = Contact::where(
        //     "user_id",
        //     "=",
        //     auth()->id()
        // )->get();

        // $contacts = Contact::where(
        //     "user_id",
        //     auth()->id()
        // )->get();

        // $contacts = Contact::query()->where(
        //     "user_id",
        //     "=",
        //     auth()->id()
        // )->get();

        // $contacts = auth()->user()->contacts()->get();
        // $contacts = auth()->user()->contacts;

        $contacts = auth()
            ->user()
            ->contacts()
            ->orderBy('name', 'desc')
            ->paginate(6);

        return view(view: "contacts.index", data: compact(var_name: "contacts"));
    }

    /**
     * Show the form for creating a new resource.
     *
     * @return \Illuminate\Http\Response
     */
    public function create()
    {
        // return Response::view("contact");
        return view(view: "contacts.create");
    }

    /**
     * Store a newly created resource in storage.
     *
     * @param  \Illuminate\Http\Request  $request
     * @return \Illuminate\Http\Response
     */
    public function store(StoreContactRequest $request)
    {
        // * Example [1]
        // if (
        //     is_null($request->get("name"))
        // ) return Response::redirectTo("/contacts/create")->withErrors([
        //     "name" => "This field is required"
        // ]);

        // * Example [2]
        // if (
        //     is_null($request->get("name"))
        // ) return redirect("/contacts/create")->withErrors([
        //     "name" => "This field is required"
        // ]);

        // * Example [3]
        // if (
        //     is_null($request->get("name"))
        // ) return redirect(route("contacts.create"))->withErrors([
        //     "name" => "This field is required"
        // ]);

        // * Example [4]
        // if (
        //     is_null($request->get("name"))
        // ) return redirect()->route("contacts.create")->withErrors([
        //     "name" => "This field is required"
        // ]);

        // * Example [5]
        // if (
        //     is_null($request->get("name"))
        // ) return redirect()->back()->withErrors([
        //     "name" => "This field is required"
        // ]);

        // * Example [6]
        // if (
        //     is_null($request->get("name"))
        // ) return back()->withErrors([
        //     "name" => "This field is required"
        // ]);

        // * Example [*]
        // // No Recomendable
        // Contact::create(
        //     $request->all()
        // );

        // * Example Validation [1]
        // $request->validate([
        //     "name" => "required",
        //     "phone_number" => ["required", "digits:9"],
        //     "email" => ["required",  "email"],
        //     "age" => ["required", "numeric", "min:1", "max:255"]
        // ]);

        // $data = $request->validate($this->rules);


        // $data["user_id"] = auth()->id();
        // Contact::create($data);

        $data = $request->validated();
        if ($request->hasFile(key: "profile_picture")) {
            $path = $request->file(key: "profile_picture")->store(path: "profiles", options: "public");
            $data["profile_picture"] = $path;
        }

        // dd(Storage::url(path: $path));
        $contact = auth()->user()->contacts()->create($data);

        Cache::forget(key: auth()->id());
        // return response("Contact Created");

        // session()->flash(key: "alert", value: [
        //     "message" => "Contact $contact->name saved successfully",
        //     "type" => "info"
        // ]);

        return redirect(to: "home")->with(key: "alert", value: [
            "message" => "Contact $contact->name saved successfully",
            "type" => "success"
        ]);
        // return redirect()->route(route: "home");
    }

    /**
     * Display the specified resource.
     *
     * @param  \App\Models\Contact  $contact
     * @return \Illuminate\Http\Response
     */
    public function show(Contact $contact)
    {
        // if ($contact->user_id !== auth()->id()) abort(code: 403);
        // if ($contact->user_id !== auth()->id()) abort(code: HttpResponse::HTTP_FORBIDDEN);
        // abort_if(boolean: $contact->user_id !== auth()->id(), code: HttpResponse::HTTP_FORBIDDEN);

        // if (!Gate::allows('show-contact', $contact)) {
        //     abort(403);
        // }

        // Gate::authorize(ability: "show-contact", arguments: $contact);

        $this->authorize(ability: "view", arguments: $contact);

        return view(view: "contacts.show", data: compact("contact"));
    }

    /**
     * Show the form for editing the specified resource.
     *
     * @param  \App\Models\Contact  $contact
     * @return \Illuminate\Http\Response
     */
    public function edit(Contact $contact, Request $request)
    {
        // dd($contact, $request);
        // public function edit(int $contactId)
        // dd(request()->route(param: "contact"));
        // dd($contactId);
        // $contact = Contact::findOrFail($contactId);

        $this->authorize(ability: "update", arguments: $contact);
        return view(view: "contacts.edit", data: compact(var_name: "contact"));
    }

    /**
     * Update the specified resource in storage.
     *
     * @param  \Illuminate\Http\Request  $request
     * @param  \App\Models\Contact  $contact
     * @return \Illuminate\Http\Response
     */
    public function update(StoreContactRequest $request, Contact $contact)
    {
        // dd($request["contact"]);
        $this->authorize(ability: "update", arguments: $contact);

        $data = $request->validated();
        if ($request->hasFile(key: "profile_picture")) {
            $path = $request->file(key: "profile_picture")->store(path: "profiles", options: "public");
            $data["profile_picture"] = $path;
        }

        // $data = $request->validate($this->rules);

        $contact->update($data);
        
        Cache::forget(key: auth()->id());

        // return redirect()->route(route: "home");
        return redirect(to: "home")->with(key: "alert", value: [
            "message" => "Contact $contact->name updated successfully",
            "type" => "success"
        ]);
    }

    /**
     * Remove the specified resource from storage.
     *
     * @param  \App\Models\Contact  $contact
     * @return \Illuminate\Http\Response
     */
    public function destroy(Contact $contact)
    {
        $this->authorize(ability: "delete", arguments: $contact);
        // dd(Storage::url(path: $contact["profile_picture"]));
        $path = Storage::url($contact["profile_picture"]);
        $realPath = str_replace('storage/', 'public/', $path);
        if ($realPath !== "/public/profiles/default.png" and Storage::exists(path: $realPath)) {
            Storage::delete(paths: $realPath);
        }

        $contact->delete();
        Cache::forget(key: auth()->id());

        // El método destroy() se utiliza para eliminar uno o varios registros a la vez.
        // Por ejemplo: Contact::destroy([1, 2, 3]) elimina varios contactos por sus IDs.
        // $contact->destroy();
        // return redirect(to: "home");

        // return redirect(to: "home")->with(key: "alert", value: [
        //     "message" => "Contact $contact->name deleted successfully",
        //     "type" => "success"
        // ]);

        return back()->with(key: "alert", value: [
            "message" => "Contact $contact->name deleted successfully",
            "type" => "success"
        ]);
    }
}
```

---

## **`Cache::forget(key: auth()->id());`**

* *Elimina una clave específica de la caché.*
* *En este caso, se elimina la caché del usuario autenticado, para que Laravel vuelva a ejecutar el `callback` y obtenga datos frescos.*

---

## **Comprobación**

1. *Visita el home → se guarda el caché por 30 minutos*
2. *Agrega un nuevo contacto → se borra el caché*
3. *Regresa al home → Laravel vuelve a ejecutar la consulta y actualiza el caché*
