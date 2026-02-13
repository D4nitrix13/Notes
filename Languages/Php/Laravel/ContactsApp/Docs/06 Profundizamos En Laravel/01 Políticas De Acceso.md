<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- Gitlab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# **Políticas De Acceso**

---

## **¿Qué son los Gates en Laravel?**

> [!NOTE]
> *Los **Gates** (o puertas) son una forma de controlar el acceso a acciones específicas según las reglas de autorización que tú defines. Funcionan como **funciones de bajo nivel** que se ejecutan antes de realizar una acción sensible.*

*Laravel también ofrece **Policies**, que son una forma más estructurada y orientada a objetos, pero los **Gates son ideales para lógicas simples o personalizadas**.*

---

## **01 — Verificación de permisos manual**

```php
public function show(Contact $contact)
{
    // Validación manual
    // if ($contact->user_id !== auth()->id()) {
    //     abort(403); // Acceso prohibido
    // }

    // Mejor con constante:
    // use Symfony\Component\HttpFoundation\Response as HttpResponse;
    // abort(403) equivale a:
    // abort(HttpResponse::HTTP_FORBIDDEN);

    // Aún mejor: forma compacta con `abort_if`
    abort_if(
        boolean: $contact->user_id !== auth()->id(),
        code: HttpResponse::HTTP_FORBIDDEN
    );

    return view("contacts.show", compact("contact"));
}
```

---

## **02 — Uso de Gates: definición y uso**

### **Archivo: `App\Providers\AuthServiceProvider.php`**

```php
use Illuminate\Support\Facades\Gate;
use App\Models\User;
use App\Models\Contact;

class AuthServiceProvider extends ServiceProvider
{
    protected $policies = [
        // Aquí irían las policies si las usas
    ];

    public function boot()
    {
        $this->registerPolicies();

        Gate::define('show-contact', function (User $user, Contact $contact) {
            return $user->id === $contact->user_id;
        });
    }
}
```

### **Explicación**

| **Componente**                              | **Descripción**                                        |
| ------------------------------------------- | ------------------------------------------------------ |
| *`Gate::define('show-contact', ...)`*       | *Crea una puerta (gate) llamada `show-contact`.*       |
| *`function(User $user, Contact $contact)`*  | *Recibe al usuario autenticado y el modelo `Contact`.* |
| *`return $user->id === $contact->user_id;`* | *Verifica si el contacto pertenece al usuario.*        |

---

## **03 — Uso de Gates en un controlador**

### **Archivo: `app/Http/Controllers/ContactController.php`**

```php
use Illuminate\Support\Facades\Gate;

public function show(Contact $contact)
{
    // Alternativa 1: forma clásica
    // if (!Gate::allows('show-contact', $contact)) {
    //     abort(403);
    // }

    // Alternativa 2: forma recomendada
    Gate::authorize('show-contact', $contact);

    return view("contacts.show", compact("contact"));
}
```

### **¿Qué hace `Gate::authorize(...)`?**

| **Elemento**             | **Descripción**                                                   |
| ------------------------ | ----------------------------------------------------------------- |
| *`'show-contact'`*       | *Nombre de la puerta que se definió en `AuthServiceProvider`.*    |
| *`$contact`*             | *Argumento que se pasa al Gate para validarlo.*                   |
| *`Gate::authorize(...)`* | *Si no se autoriza, **lanza automáticamente una excepción 403**.* |

---

## **¿Cuándo usar Gates?**

**Usa Gates si:**

* *Solo necesitas proteger una acción específica (como ver o editar).*
* *Tu aplicación no necesita políticas completas por modelo.*
* *Querés tener control directo sobre la lógica de autorización.*

## **Comparación rápida**

| **Técnica**              | **Descripción**                                               |
| ------------------------ | ------------------------------------------------------------- |
| *`abort_if(..., 403)`*   | *Verificación manual. Rápida, pero no escalable.*             |
| *`Gate::authorize(...)`* | *Lógica centralizada, más limpia.*                            |
| *`Policies`*             | *Lógica organizada por modelo. Escalable para CRUD completo.* |

* **Resumen final**

| **Tema**                     | **Detalles clave**                                                          |
| ---------------------------- | --------------------------------------------------------------------------- |
| **Gates**                    | *Funciones que determinan si un usuario puede realizar una acción.*         |
| **Gate::define**             | *Define una nueva regla de autorización.*                                   |
| **Gate::allows / authorize** | *Verifica si el usuario actual tiene permiso.*                              |
| **abort_if(..., 403)**       | *Método manual para denegar acceso.*                                        |
| **Ubicación clave**          | *`App\Providers\AuthServiceProvider` y `ContactController`*                 |
| **Mejor práctica**           | *Usar `Gate::authorize` para una sintaxis más limpia y control de errores.* |

---

## **Policies En Laravel: Control De Acceso Avanzado**

## **¿Qué es una Policy?**

*Una **Policy** en Laravel es una clase donde se definen **reglas de autorización** para acciones sobre un modelo, como ver, editar, actualizar o eliminar un recurso.*

> *Las policies actúan como "guardias" que dicen si un usuario **puede o no** hacer algo con un modelo.*

---

## **Creación de una Policy**

### **Comando**

```bash
php artisan make:policy ContactPolicy --model=Contact
```

* **Explicación**

| **Parte**           | **Descripción**                                                                                                |
| ------------------- | -------------------------------------------------------------------------------------------------------------- |
| *`php artisan`*     | *Ejecuta un comando Artisan.*                                                                                  |
| *`make:policy`*     | *Subcomando que genera una nueva Policy.*                                                                      |
| *`ContactPolicy`*   | *Nombre de la clase Policy que se va a crear.*                                                                 |
| *`--model=Contact`* | *Asocia la policy al modelo `Contact`. Laravel generará métodos comunes como `view`, `update`, `delete`, etc.* |

---

### **Estructura generada**

**Ruta:**

```bash
ApplicationLaravel/app/Policies/ContactPolicy.php
```

*Laravel crea automáticamente esta clase con métodos vacíos para autorización, como `view()`, `create()`, `update()`, etc.*

---

## **Contenido `ContactPolicy.php`**

```php
public function view(User $user, Contact $contact)
{
    return $user->id === $contact->user_id;
}

public function update(User $user, Contact $contact)
{
    return $user->id === $contact->user_id;
}

public function delete(User $user, Contact $contact)
{
    return $user->id === $contact->user_id;
}
```

> *Cada método retorna `true` o `false`, indicando si el usuario puede realizar la acción sobre ese modelo específico.*

---

## **Registro de la Policy**

**En `App\Providers\AuthServiceProvider.php`, debes registrar la relación entre el modelo y su policy:**

```php
protected $policies = [
    \App\Models\Contact::class => \App\Policies\ContactPolicy::class,
];
```

**Y en `boot()`:**

```php
public function boot()
{
    $this->registerPolicies();
}
```

*Esto le dice a Laravel que use `ContactPolicy` para autorizar acciones sobre instancias del modelo `Contact`.*

---

## **Uso de la Policy en un controlador**

### **`ContactController.php`**

```php
public function show(Contact $contact)
{
    $this->authorize('view', $contact);
    return view("contacts.show", compact("contact"));
}
```

### **¿Qué hace `authorize(...)`?**

* *Llama automáticamente al método correspondiente en la policy (`view`, en este caso).*
* *Si retorna `false`, Laravel lanza un error **403 Forbidden**.*

---

## **Otros ejemplos con explicación**

### **Editar**

```php
public function edit(Contact $contact)
{
    $this->authorize('update', $contact);
    return view("contacts.edit", compact("contact"));
}
```

*Llama a `ContactPolicy::update(...)`.*

---

### **Actualizar**

```php
public function update(Request $request, Contact $contact)
{
    $this->authorize('update', $contact);

    $data = $request->validate([
        "name" => "required",
        "phone_number" => "required|digits:9",
        "email" => "required|email",
        "age" => "required|numeric|min:1|max:255"
    ]);

    $contact->update($data);
    return redirect()->route("home");
}
```

---

### **Eliminar**

```php
public function destroy(Contact $contact)
{
    $this->authorize('delete', $contact);
    $contact->delete();

    // Comentario mejorado:
    // destroy() es un método estático para eliminar uno o varios registros por su ID:
    // Ejemplo: Contact::destroy([1, 2, 3])
    // No se debe usar como $contact->destroy(), porque ese método no existe en la instancia.

    return redirect("home");
}
```

---

## **Métodos comunes generados en una Policy**

| **Método**                   | **¿Qué autoriza?**                      |
| ---------------------------- | --------------------------------------- |
| *`viewAny(User $u)`*         | *Ver todos los registros (como lista).* |
| *`view(User $u, $m)`*        | *Ver un registro específico.*           |
| *`create(User $u)`*          | *Crear nuevos registros.*               |
| *`update(User $u, $m)`*      | *Actualizar registros.*                 |
| *`delete(User $u, $m)`*      | *Eliminar registros.*                   |
| *`restore(User $u, $m)`*     | *Restaurar eliminados.*                 |
| *`forceDelete(User $u, $m)`* | *Eliminar de forma permanente.*         |

---

## **Resumen final**

| **Tema**                            | **Descripción clara**                                       |
| ----------------------------------- | ----------------------------------------------------------- |
| **Policy**                          | *Clase con métodos de autorización por acción.*             |
| **make:policy --model**             | *Crea una policy enlazada a un modelo.*                     |
| **authorize()**                     | *Método Laravel para aplicar una regla de Policy.*          |
| **User y modelo**                   | *Siempre se pasan a los métodos de la Policy para validar.* |
| **Registro en AuthServiceProvider** | *Es obligatorio para que Laravel reconozca la policy.*      |
